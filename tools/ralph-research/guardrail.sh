#!/usr/bin/env bash
set -euo pipefail

# Research Repository Anti-Shortcut Guardrails
# Purpose: Detect and block documentation shortcuts (TODO, incomplete sections, placeholder evidence)
# Returns: 0 if clean, 1 if violations found

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Paths
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Detect search tool (ripgrep preferred, fallback to grep)
if command -v rg &> /dev/null; then
    SEARCH_TOOL="rg"
else
    SEARCH_TOOL="grep"
fi

# Track violations
VIOLATIONS_FOUND=0
VIOLATION_REPORT=""

log_violation() {
    local pattern_name="$1"
    local details="$2"
    VIOLATIONS_FOUND=1
    VIOLATION_REPORT="${VIOLATION_REPORT}
${RED}[VIOLATION]${NC} ${pattern_name}
${details}
"
}

search_pattern() {
    local pattern="$1"
    local exclude_args="$2"

    if [ "$SEARCH_TOOL" = "rg" ]; then
        # Use ripgrep for markdown files
        rg -n "${pattern}" \
            --type md \
            --iglob "!audit-*/**" \
            --iglob "!prior/**" \
            --iglob "!README.md" \
            --iglob "!QUICK-START.md" \
            --iglob "!*PROMPT*.md" \
            --iglob "!*START-HERE*.md" \
            --iglob "!SESSION-*.md" \
            --iglob "!.claude/**" \
            ${exclude_args} \
            "${REPO_ROOT}" 2>/dev/null || true
    else
        # Fallback to grep
        grep -rn -E "${pattern}" "${REPO_ROOT}" \
            --include="*-MD-*.md" \
            --include="*-DO-*.md" \
            --exclude-dir=audit-* \
            --exclude-dir=prior \
            --exclude-dir=.claude \
            --exclude="README.md" \
            --exclude="QUICK-START.md" \
            --exclude="*PROMPT*.md" \
            --exclude="*START-HERE*.md" \
            --exclude="SESSION-*.md" \
            2>/dev/null || true
    fi
}

echo -e "${YELLOW}[GUARDRAIL]${NC} Running anti-shortcut checks for documentation..."
echo ""

cd "${REPO_ROOT}"

# ============================================================================
# CHECK 1: Incomplete Work Markers
# ============================================================================
echo -e "${YELLOW}[1/7]${NC} Checking for incomplete work markers..."

INCOMPLETE_MARKERS=$(search_pattern "\bTODO\b|\bFIXME\b|\bWIP\b|\bHACK\b|\bXXX\b|\bSTUB\b|\[PLACEHOLDER\]|\[TBD\]|\[TO BE DETERMINED\]|\bINCOMPLETE\b|\bPARTIAL\b" "")

if [ -n "$INCOMPLETE_MARKERS" ]; then
    # Filter out exceptions
    FILTERED=$(echo "$INCOMPLETE_MARKERS" | grep -v "guardrail-exception" || true)
    if [ -n "$FILTERED" ]; then
        log_violation "Incomplete Work Markers" "$FILTERED

Fix: Complete the work and remove markers, or add exception comment.
Allowed exception format: <!-- guardrail-exception: [reason] -->"
    fi
fi

# ============================================================================
# CHECK 2: Research Pending Markers
# ============================================================================
echo -e "${YELLOW}[2/7]${NC} Checking for research pending markers..."

RESEARCH_PENDING=$(search_pattern "\[NEED MORE RESEARCH\]|\[REQUIRES FURTHER INVESTIGATION\]|\[PENDING VERIFICATION\]" "")

if [ -n "$RESEARCH_PENDING" ]; then
    FILTERED=$(echo "$RESEARCH_PENDING" | grep -v "guardrail-exception" || true)
    if [ -n "$FILTERED" ]; then
        log_violation "Research Pending Markers" "$FILTERED

Fix: Complete research or document as [CRITICAL GAP] with explanation.
Allowed exception format: <!-- guardrail-exception: [reason] -->"
    fi
fi

# ============================================================================
# CHECK 3: Lazy Section Completion
# ============================================================================
echo -e "${YELLOW}[3/7]${NC} Checking for lazy section references..."

LAZY_SECTIONS=$(search_pattern "See section above|See previous section|Same as [A-Z]{2}|Similar to [A-Z]{2}|Not applicable \(research pending\)" "")

if [ -n "$LAZY_SECTIONS" ]; then
    FILTERED=$(echo "$LAZY_SECTIONS" | grep -v "guardrail-exception" || true)
    if [ -n "$FILTERED" ]; then
        log_violation "Lazy Section Completion" "$FILTERED

Fix: Write complete content for each section, don't reference other sections.
Cross-references are OK in context, but each section must stand alone."
    fi
fi

# ============================================================================
# CHECK 4: Evidence Shortcuts
# ============================================================================
echo -e "${YELLOW}[4/7]${NC} Checking for evidence shortcuts..."

EVIDENCE_SHORTCUTS=$(search_pattern "\[FACT\].*\(no source\)|\[FACT\].*\(unable to verify\)|Citation: \(pending\)|Source: \(TBD\)|Source: \(none\)|Citation: TBD|Source: TBD" "")

if [ -n "$EVIDENCE_SHORTCUTS" ]; then
    FILTERED=$(echo "$EVIDENCE_SHORTCUTS" | grep -v "guardrail-exception" || true)
    if [ -n "$FILTERED" ]; then
        log_violation "Evidence Shortcuts" "$FILTERED

Fix: Provide proper citations with Source URLs, or reclassify as [INFERENCE] or [CRITICAL GAP].
All [FACT] tags require Citation: and Source: fields."
    fi
fi

# ============================================================================
# CHECK 5: Quality Threshold Bypasses
# ============================================================================
echo -e "${YELLOW}[5/7]${NC} Checking for quality threshold bypasses..."

QUALITY_BYPASSES=$(search_pattern "completion_percentage: (100|[89][0-9]).*\[?NOTE:.*placeholder|completion_percentage: (100|[89][0-9]).*\(temporary\)|Skip audit|Bypass validation|status: COMPREHENSIVE.*\(temp" "")

if [ -n "$QUALITY_BYPASSES" ]; then
    log_violation "Quality Threshold Bypasses" "$QUALITY_BYPASSES

Fix: Set accurate completion_percentage based on actual quality.
Don't claim 85%+ completion with placeholder notes."
fi

# ============================================================================
# CHECK 6: CSV Manipulation Markers
# ============================================================================
echo -e "${YELLOW}[6/7]${NC} Checking CSV files for manipulation markers..."

# Check CSV files directly with grep (not markdown-specific)
if [ -f "${REPO_ROOT}/state-research-tracker.csv" ]; then
    CSV_MANIPULATION=$(grep -n "TEMP_COMPLETE\|FAKE_STATUS\|999" "${REPO_ROOT}/state-research-tracker.csv" 2>/dev/null || true)
    if [ -n "$CSV_MANIPULATION" ]; then
        log_violation "CSV Manipulation Markers" "state-research-tracker.csv:
${CSV_MANIPULATION}

Fix: Use valid status values (COMPLETE, PENDING, IN_PROGRESS) and realistic completion percentages."
    fi
fi

if [ -f "${REPO_ROOT}/audit-2026-01-03/67-board-audit-tracker-MD-DO.csv" ]; then
    CSV_MANIPULATION=$(grep -n "TEMP_COMPLETE\|FAKE_STATUS\|999" "${REPO_ROOT}/audit-2026-01-03/67-board-audit-tracker-MD-DO.csv" 2>/dev/null || true)
    if [ -n "$CSV_MANIPULATION" ]; then
        log_violation "CSV Manipulation Markers" "67-board-audit-tracker-MD-DO.csv:
${CSV_MANIPULATION}

Fix: Use valid status values and realistic audit scores."
    fi
fi

# ============================================================================
# CHECK 7: Inference Without Reasoning
# ============================================================================
echo -e "${YELLOW}[7/7]${NC} Checking for inferences without reasoning..."

INFERENCE_NO_REASONING=$(search_pattern "\[INFERENCE[^\]]*\](?!.*Reasoning:)" "")

if [ -n "$INFERENCE_NO_REASONING" ]; then
    # This is a more lenient check - we'll look for inferences that appear alone on a line
    # Real inferences should have explanation text and "Reasoning:" field
    FILTERED=$(echo "$INFERENCE_NO_REASONING" | grep -v "guardrail-exception" || true)
    # Only flag if there are many (>5) to avoid false positives
    LINE_COUNT=$(echo "$FILTERED" | wc -l | tr -d ' ')
    if [ -n "$FILTERED" ] && [ "$LINE_COUNT" -gt 5 ]; then
        log_violation "Inferences Without Reasoning (Warning)" "Found ${LINE_COUNT} potential inferences without reasoning.

Best Practice: All [INFERENCE] tags should include Reasoning: field explaining the logic.
This is a warning - not blocking, but should be addressed for quality."
    fi
fi

# ============================================================================
# REPORT
# ============================================================================
echo ""
echo -e "${YELLOW}================================${NC}"

if [ $VIOLATIONS_FOUND -eq 0 ]; then
    echo -e "${GREEN}[PASS]${NC} No shortcuts detected"
    echo -e "${YELLOW}================================${NC}"
    exit 0
else
    echo -e "${RED}[FAIL]${NC} Shortcuts detected"
    echo -e "${YELLOW}================================${NC}"
    echo ""
    echo -e "${VIOLATION_REPORT}"
    echo ""
    echo -e "${YELLOW}Guardrail Policy:${NC}"
    echo "  - Complete all research, no TODO/FIXME markers"
    echo "  - All [FACT] tags must have citations and sources"
    echo "  - No lazy section completion (\"See above\", \"Same as X\")"
    echo "  - No quality threshold bypasses or fake completion %"
    echo "  - CSV trackers must have valid, accurate data"
    echo "  - [INFERENCE] tags should include reasoning"
    echo ""
    echo "Exception format: <!-- guardrail-exception: [specific reason] -->"
    echo -e "${YELLOW}================================${NC}"
    exit 1
fi
