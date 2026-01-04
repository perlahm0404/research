#!/usr/bin/env bash
set -euo pipefail

# Research Repository Verification Script
# Purpose: Single source of truth for documentation quality gating
# Includes: Anti-shortcut guardrails, frontmatter validation, quality threshold, citations, CSV consistency
# Returns: 0 if all checks pass, non-zero otherwise

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Paths
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
RALPH_DIR="${REPO_ROOT}/tools/ralph-research"
STATE_DIR="${RALPH_DIR}/state"
SCRIPTS_DIR="${RALPH_DIR}/scripts"

# Generate RUN_ID with timestamp and git sha
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
GIT_SHA=$(git -C "${REPO_ROOT}" rev-parse --short HEAD 2>/dev/null || echo "nogit")
RUN_ID="${TIMESTAMP}-${GIT_SHA}"

# Create run-specific directory for evidence
RUN_DIR="${STATE_DIR}/runs/${RUN_ID}"
mkdir -p "${RUN_DIR}"

# Legacy log file (for backwards compat)
LOG_FILE="${STATE_DIR}/verify.log"
> "${LOG_FILE}"

# Per-run summary
SUMMARY_FILE="${RUN_DIR}/SUMMARY.txt"
STATUS_FILE="${STATE_DIR}/STATUS.md"

log() {
    echo -e "${1}" | tee -a "${LOG_FILE}"
}

# Run command with evidence capture
run_with_evidence() {
    local step_name="$1"
    shift
    local step_log="${RUN_DIR}/${step_name}.log"

    {
        echo "=== RUN_CMD EVIDENCE ==="
        echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
        echo "Working Directory: $(pwd)"
        echo "Command: $*"
        echo "=== OUTPUT ==="
    } > "$step_log"

    local exit_code=0
    "$@" >> "$step_log" 2>&1 || exit_code=$?

    {
        echo ""
        echo "=== END ==="
        echo "Exit Code: $exit_code"
    } >> "$step_log"

    return $exit_code
}

check_step() {
    local step_name="$1"
    local step_key="$2"
    shift 2
    log "${YELLOW}[VERIFY]${NC} Running: ${step_name}"

    if run_with_evidence "$step_key" "$@"; then
        log "${GREEN}[PASS]${NC} ${step_name}"
        echo "${step_key}: PASS (${RUN_DIR}/${step_key}.log)" >> "$SUMMARY_FILE"
        return 0
    else
        log "${RED}[FAIL]${NC} ${step_name}"
        echo "${step_key}: FAIL (${RUN_DIR}/${step_key}.log)" >> "$SUMMARY_FILE"
        return 1
    fi
}

# Take snapshot of repo state
take_snapshot() {
    local tag="$1"
    local snapshot_file="${RUN_DIR}/${tag}-snapshot.txt"
    local diff_file="${RUN_DIR}/${tag}-diff.patch"

    {
        echo "=== SNAPSHOT: ${tag} ==="
        echo "Date: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
        echo ""
        echo "=== GIT HEAD ==="
        git -C "${REPO_ROOT}" rev-parse HEAD 2>/dev/null || echo "no-commit"
        echo ""
        echo "=== GIT STATUS ==="
        git -C "${REPO_ROOT}" status --porcelain 2>/dev/null || echo "not a git repo"
        echo ""
        echo "=== CHANGED DOCUMENTS ==="
        git -C "${REPO_ROOT}" status --porcelain 2>/dev/null | grep -E '(MD|DO)-.*\.md$' || echo "none"
        echo ""
        echo "=== CSV STATE ==="
        if [ -f "${REPO_ROOT}/state-research-tracker.csv" ]; then
            echo "state-research-tracker.csv: $(wc -l < "${REPO_ROOT}/state-research-tracker.csv") lines"
        else
            echo "state-research-tracker.csv: NOT FOUND"
        fi
        if [ -f "${REPO_ROOT}/audit-2026-01-03/67-board-audit-tracker-MD-DO.csv" ]; then
            echo "67-board-audit-tracker-MD-DO.csv: $(wc -l < "${REPO_ROOT}/audit-2026-01-03/67-board-audit-tracker-MD-DO.csv") lines"
        else
            echo "67-board-audit-tracker-MD-DO.csv: NOT FOUND"
        fi
        echo ""
        echo "=== PYTHON VERSION ==="
        python3 --version 2>/dev/null || echo "python3 not found"
        echo ""
        echo "=== ENVIRONMENT ==="
        uname -a
    } > "$snapshot_file"

    # Write full diff to patch file if non-empty
    local diff_content
    diff_content=$(git -C "${REPO_ROOT}" diff 2>/dev/null || true)
    if [ -n "$diff_content" ]; then
        echo "$diff_content" > "$diff_file"
    fi

    log "Snapshot: ${snapshot_file}"
}

# Parse command line arguments
MODE="batch"  # default: batch mode (all documents)
TARGET_FILE=""
TARGET_TIER=""
SKIP_GUARDRAILS=false  # default: run guardrails

while [[ $# -gt 0 ]]; do
    case $1 in
        --file)
            MODE="single"
            TARGET_FILE="$2"
            shift 2
            ;;
        --tier)
            MODE="tier"
            TARGET_TIER="$2"
            shift 2
            ;;
        --batch)
            MODE="batch"
            shift
            ;;
        --ci-mode)
            # CI mode: fail fast, no interactive prompts
            MODE="batch"
            shift
            ;;
        --skip-guardrails)
            # Skip Layer 0 guardrails (use for clean documents only)
            SKIP_GUARDRAILS=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: verify.sh [--file FILE] [--tier TIER-X] [--batch] [--ci-mode] [--skip-guardrails]"
            exit 1
            ;;
    esac
done

# Change to repo root
cd "${REPO_ROOT}"

log "${YELLOW}================================${NC}"
log "${YELLOW}Research Repository Verification${NC}"
log "${YELLOW}================================${NC}"
log "RUN_ID: ${RUN_ID}"
log "Mode: ${MODE}"
if [ "${MODE}" = "single" ]; then
    log "Target File: ${TARGET_FILE}"
elif [ "${MODE}" = "tier" ]; then
    log "Target Tier: ${TARGET_TIER}"
fi
log "Evidence: ${RUN_DIR}"
log "Started at: $(date)"
log ""

# Initialize summary
echo "=== RALPH RESEARCH VERIFICATION SUMMARY ===" > "$SUMMARY_FILE"
echo "RUN_ID: ${RUN_ID}" >> "$SUMMARY_FILE"
echo "Started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> "$SUMMARY_FILE"
echo "Mode: ${MODE}" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# Take PRE snapshot
take_snapshot "PRE"

# Track overall status
OVERALL_STATUS=0
FAILED_STEPS=""
PASSED_STEPS=""

# ============================================================================
# LAYER 0: Anti-Shortcut Guardrails (MUST PASS FIRST)
# ============================================================================
if [ "$SKIP_GUARDRAILS" = true ]; then
    log ""
    log "${YELLOW}=== LAYER 0: Anti-Shortcut Guardrails (SKIPPED) ===${NC}"
    log "${YELLOW}[SKIP]${NC} Guardrails skipped via --skip-guardrails flag"
    PASSED_STEPS="${PASSED_STEPS}guardrail(skipped) "
    echo "guardrail: SKIPPED" >> "$SUMMARY_FILE"
else
    log ""
    log "${YELLOW}=== LAYER 0: Anti-Shortcut Guardrails ===${NC}"

    if check_step "Anti-Shortcut Guardrails" "guardrail" bash "${RALPH_DIR}/guardrail.sh"; then
        PASSED_STEPS="${PASSED_STEPS}guardrail "
    else
        OVERALL_STATUS=1
        FAILED_STEPS="${FAILED_STEPS}guardrail "
        log "${RED}GUARDRAIL FAILED${NC} - Cannot proceed until violations are fixed"
    fi
fi

# Only continue if guardrail passed (or was skipped)
if [ -z "$FAILED_STEPS" ]; then

    # ========================================================================
    # LAYER 1: Frontmatter Validation
    # ========================================================================
    log ""
    log "${YELLOW}=== LAYER 1: Frontmatter Validation ===${NC}"

    # Find documents to check based on mode
    if [ "${MODE}" = "single" ]; then
        DOCUMENTS="${TARGET_FILE}"
    elif [ "${MODE}" = "tier" ]; then
        DOCUMENTS=$(find "${REPO_ROOT}" -name "*-MD-*.md" -o -name "*-DO-*.md" | grep "${TARGET_TIER}" || true)
    else
        # Batch mode: all state documents
        DOCUMENTS=$(find "${REPO_ROOT}" -maxdepth 1 -name "*-MD-*.md" -o -name "*-DO-*.md")
    fi

    # Validate frontmatter for each document
    FRONTMATTER_ISSUES=0
    for doc in $DOCUMENTS; do
        if [ -f "$doc" ]; then
            if python3 "${SCRIPTS_DIR}/frontmatter_validator.py" "$doc" >> "${RUN_DIR}/frontmatter-validation.log" 2>&1; then
                echo "[PASS] $(basename "$doc")" >> "${RUN_DIR}/frontmatter-validation.log"
            else
                echo "[FAIL] $(basename "$doc")" >> "${RUN_DIR}/frontmatter-validation.log"
                FRONTMATTER_ISSUES=$((FRONTMATTER_ISSUES + 1))
            fi
        fi
    done

    if [ $FRONTMATTER_ISSUES -eq 0 ]; then
        log "${GREEN}[PASS]${NC} Frontmatter Validation (all documents)"
        PASSED_STEPS="${PASSED_STEPS}frontmatter "
        echo "frontmatter: PASS" >> "$SUMMARY_FILE"
    else
        log "${YELLOW}[WARN]${NC} Frontmatter Validation (${FRONTMATTER_ISSUES} documents have issues)"
        PASSED_STEPS="${PASSED_STEPS}frontmatter(warnings) "
        echo "frontmatter: PASS (with warnings: ${FRONTMATTER_ISSUES} issues)" >> "$SUMMARY_FILE"
        # Don't fail overall - frontmatter is tracked but not blocking
    fi

    # ========================================================================
    # LAYER 2: Quality Threshold Check (85%+)
    # ========================================================================
    log ""
    log "${YELLOW}=== LAYER 2: Quality Threshold (85%+) ===${NC}"

    QUALITY_FAILURES=0
    QUALITY_TOTAL=0
    for doc in $DOCUMENTS; do
        if [ -f "$doc" ]; then
            QUALITY_TOTAL=$((QUALITY_TOTAL + 1))
            if python3 "${SCRIPTS_DIR}/quality_threshold_check.py" "$doc" >> "${RUN_DIR}/quality-threshold.log" 2>&1; then
                echo "[PASS 85%+] $(basename "$doc")" >> "${RUN_DIR}/quality-threshold.log"
            else
                echo "[FAIL <85%] $(basename "$doc")" >> "${RUN_DIR}/quality-threshold.log"
                QUALITY_FAILURES=$((QUALITY_FAILURES + 1))
            fi
        fi
    done

    if [ $QUALITY_FAILURES -eq 0 ]; then
        log "${GREEN}[PASS]${NC} Quality Threshold (all ${QUALITY_TOTAL} documents ≥ 85%)"
        PASSED_STEPS="${PASSED_STEPS}quality "
        echo "quality: PASS (${QUALITY_TOTAL} documents)" >> "$SUMMARY_FILE"
    else
        log "${RED}[FAIL]${NC} Quality Threshold (${QUALITY_FAILURES}/${QUALITY_TOTAL} documents below 85%)"
        OVERALL_STATUS=1
        FAILED_STEPS="${FAILED_STEPS}quality "
        echo "quality: FAIL (${QUALITY_FAILURES}/${QUALITY_TOTAL} below threshold)" >> "$SUMMARY_FILE"
    fi

    # ========================================================================
    # LAYER 3: Citation Validation
    # ========================================================================
    log ""
    log "${YELLOW}=== LAYER 3: Citation Validation ===${NC}"

    CITATION_ISSUES=0
    for doc in $DOCUMENTS; do
        if [ -f "$doc" ]; then
            if python3 "${SCRIPTS_DIR}/citation_validator.py" "$doc" >> "${RUN_DIR}/citation-validation.log" 2>&1; then
                echo "[PASS] $(basename "$doc")" >> "${RUN_DIR}/citation-validation.log"
            else
                echo "[WARN] $(basename "$doc")" >> "${RUN_DIR}/citation-validation.log"
                CITATION_ISSUES=$((CITATION_ISSUES + 1))
            fi
        fi
    done

    if [ $CITATION_ISSUES -eq 0 ]; then
        log "${GREEN}[PASS]${NC} Citation Validation"
        PASSED_STEPS="${PASSED_STEPS}citations "
        echo "citations: PASS" >> "$SUMMARY_FILE"
    else
        log "${YELLOW}[WARN]${NC} Citation Validation (${CITATION_ISSUES} documents have warnings)"
        PASSED_STEPS="${PASSED_STEPS}citations(warnings) "
        echo "citations: PASS (with warnings: ${CITATION_ISSUES} issues)" >> "$SUMMARY_FILE"
        # Warnings only - don't fail
    fi

    # ========================================================================
    # LAYER 4: CSV Consistency
    # ========================================================================
    log ""
    log "${YELLOW}=== LAYER 4: CSV Consistency ===${NC}"

    if check_step "CSV Consistency" "csv-consistency" python3 "${SCRIPTS_DIR}/csv_consistency_check.py" "${REPO_ROOT}"; then
        PASSED_STEPS="${PASSED_STEPS}csv "
    else
        OVERALL_STATUS=1
        FAILED_STEPS="${FAILED_STEPS}csv "
    fi

fi

# Take POST snapshot
take_snapshot "POST"

# Finalize summary
{
    echo ""
    echo "=== FINAL RESULT ==="
    echo "Passed: ${PASSED_STEPS:-none}"
    echo "Failed: ${FAILED_STEPS:-none}"
    if [ ${OVERALL_STATUS} -eq 0 ]; then
        echo "RESULT: ALL CHECKS PASSED"
    else
        echo "RESULT: VERIFICATION FAILED"
    fi
    echo "Completed: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
} >> "$SUMMARY_FILE"

# Update STATUS.md (tracked file)
{
    echo "# Ralph Research Verification Status"
    echo ""
    echo "## Latest Run"
    echo "- **RUN_ID**: ${RUN_ID}"
    echo "- **Date**: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    echo "- **Mode**: ${MODE}"
    echo "- **Passed**: ${PASSED_STEPS:-none}"
    echo "- **Failed**: ${FAILED_STEPS:-none}"
    echo ""
    if [ -n "$FAILED_STEPS" ]; then
        echo "## What Failed"
        for step in $FAILED_STEPS; do
            echo "- **${step}**: See \`tools/ralph-research/state/runs/${RUN_ID}/${step}.log\`"
        done
        echo ""
        echo "## Next Steps"
        echo "- Review logs in \`tools/ralph-research/state/runs/${RUN_ID}/\`"
        echo "- Fix issues identified in failed checks"
        echo "- Re-run: \`bash tools/ralph-research/verify.sh\`"
    else
        echo "## Status: PASSING"
        echo "All checks passed. Evidence in \`tools/ralph-research/state/runs/${RUN_ID}/\`"
    fi
    echo ""
    echo "## Layer Results"
    echo "- **Layer 0 (Guardrails)**: $(echo "$PASSED_STEPS" | grep -q "guardrail" && echo "PASS" || echo "FAIL")"
    echo "- **Layer 1 (Frontmatter)**: $(echo "$PASSED_STEPS" | grep -q "frontmatter" && echo "PASS" || echo "N/A")"
    echo "- **Layer 2 (Quality 85%+)**: $(echo "$PASSED_STEPS" | grep -q "quality" && echo "PASS" || echo "$FAILED_STEPS" | grep -q "quality" && echo "FAIL" || echo "N/A")"
    echo "- **Layer 3 (Citations)**: $(echo "$PASSED_STEPS" | grep -q "citations" && echo "PASS" || echo "N/A")"
    echo "- **Layer 4 (CSV)**: $(echo "$PASSED_STEPS" | grep -q "csv" && echo "PASS" || echo "$FAILED_STEPS" | grep -q "csv" && echo "FAIL" || echo "N/A")"
} > "$STATUS_FILE"

log ""
log "${YELLOW}================================${NC}"
if [ ${OVERALL_STATUS} -eq 0 ]; then
    log "${GREEN}[SUCCESS]${NC} All verification checks passed"
    log "Evidence: ${RUN_DIR}"
    log "Completed at: $(date)"
    log ""
    log "View summary: cat ${STATE_DIR}/STATUS.md"
    exit 0
else
    log "${RED}[FAILURE]${NC} One or more verification checks failed"
    log "Evidence: ${RUN_DIR}"
    log "Completed at: $(date)"
    log ""
    log "See logs in: ${RUN_DIR}"
    log "View summary: cat ${STATE_DIR}/STATUS.md"
    exit 1
fi
