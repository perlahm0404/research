#!/usr/bin/env bash
set -euo pipefail

# Ralph Loop - Local Harness for Iterative Documentation Verification
# This is NOT required, just a convenience for local development
# The SSOT gate is verify.sh

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
VERIFY_SCRIPT="${REPO_ROOT}/tools/ralph-research/verify.sh"
STATE_DIR="${REPO_ROOT}/tools/ralph-research/state"
LOOP_LOG="${STATE_DIR}/loop.log"

# Configuration
MAX_ITERATIONS=${MAX_ITERATIONS:-20}
CIRCUIT_BREAKER_NO_CHANGE=2
CIRCUIT_BREAKER_SAME_FAILURE=3

# State tracking
iteration=0
last_verify_failure=""
failure_count=0
no_change_count=0
last_git_diff_hash=""

log() {
    echo -e "${1}" | tee -a "${LOOP_LOG}"
}

log "${BLUE}======================================${NC}"
log "${BLUE}Ralph Loop - Documentation Verification${NC}"
log "${BLUE}======================================${NC}"
log "Max iterations: ${MAX_ITERATIONS}"
log "Started at: $(date)"
log ""

> "${LOOP_LOG}"

while [ ${iteration} -lt ${MAX_ITERATIONS} ]; do
    iteration=$((iteration + 1))

    log "${YELLOW}[ITER ${iteration}/${MAX_ITERATIONS}]${NC} Starting iteration"

    # Step 1: Run verification
    log "${BLUE}→${NC} Running verification..."

    if bash "${VERIFY_SCRIPT}"; then
        log "${GREEN}[SUCCESS]${NC} All verification checks passed!"
        log ""
        log "${GREEN}✓ COMPLETE${NC}"
        log "Completed at: $(date)"
        log ""
        log "Documentation quality meets 85%+ threshold"
        log "No shortcuts detected"
        log "CSV trackers consistent with documents"
        exit 0
    else
        # Verification failed
        current_failure=$(tail -20 "${STATE_DIR}/verify.log" | grep -E '\[FAIL\]' | head -1 || echo "unknown")

        log "${RED}[FAIL]${NC} Verification failed: ${current_failure}"

        # Circuit breaker: same failure repeated
        if [ "${current_failure}" == "${last_verify_failure}" ]; then
            failure_count=$((failure_count + 1))
            log "${YELLOW}⚠${NC} Same failure repeated (${failure_count}/${CIRCUIT_BREAKER_SAME_FAILURE})"

            if [ ${failure_count} -ge ${CIRCUIT_BREAKER_SAME_FAILURE} ]; then
                log "${RED}[STOP]${NC} Circuit breaker: same failure ${CIRCUIT_BREAKER_SAME_FAILURE} times"
                log "Last failure: ${current_failure}"
                log ""
                log "Manual intervention required:"
                log "  1. Review logs in: ${STATE_DIR}/runs/"
                log "  2. Check STATUS.md: cat ${STATE_DIR}/STATUS.md"
                log "  3. Fix the underlying issue"
                log "  4. Re-run: bash tools/ralph-research/ralph.sh"
                exit 1
            fi
        else
            failure_count=1
        fi

        last_verify_failure="${current_failure}"
    fi

    # Step 2: Check for document changes (simple git diff hash)
    current_git_diff_hash=$(git diff --stat 2>/dev/null | grep -E '\.md$' | md5 2>/dev/null || echo "")

    if [ -n "${last_git_diff_hash}" ] && [ "${current_git_diff_hash}" == "${last_git_diff_hash}" ]; then
        no_change_count=$((no_change_count + 1))
        log "${YELLOW}⚠${NC} No document changes detected (${no_change_count}/${CIRCUIT_BREAKER_NO_CHANGE})"

        if [ ${no_change_count} -ge ${CIRCUIT_BREAKER_NO_CHANGE} ]; then
            log "${RED}[STOP]${NC} Circuit breaker: no changes for ${CIRCUIT_BREAKER_NO_CHANGE} iterations"
            log ""
            log "No progress detected. Manual intervention required:"
            log "  - Are you making changes to fix the issues?"
            log "  - Check recent verification logs for guidance"
            log "  - View STATUS.md: cat ${STATE_DIR}/STATUS.md"
            exit 1
        fi
    else
        no_change_count=0
    fi

    last_git_diff_hash="${current_git_diff_hash}"

    # Step 3: Pause for manual fix (this is a local harness)
    log ""
    log "${BLUE}→${NC} Iteration ${iteration} complete."
    log "   Fix issues identified in logs and press Enter to continue (or Ctrl+C to stop)..."
    log ""
    log "Quick commands:"
    log "  - View status: cat ${STATE_DIR}/STATUS.md"
    log "  - View last log: ls -t ${STATE_DIR}/runs/ | head -1"
    log ""
    read -r

done

log "${RED}[TIMEOUT]${NC} Reached max iterations (${MAX_ITERATIONS})"
log "Verification did not pass within ${MAX_ITERATIONS} iterations."
log ""
log "Next steps:"
log "  - Review accumulated evidence in ${STATE_DIR}/runs/"
log "  - Consider if documents need major revisions"
log "  - Run single-file verification: bash tools/ralph-research/verify.sh --file <FILE>"
exit 1
