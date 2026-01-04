# Ralph Research - Documentation Quality Verification Harness

Ralph Research is a comprehensive verification system for documentation quality, adapted from the KareMatch Ralph verification harness. It enforces the 85%+ quality threshold, prevents agent shortcuts, and ensures CSV/document consistency through automated verification gates.

**Core Philosophy:** Documentation quality requires different verification than code, but the same anti-shortcut philosophy applies: evidence-based verification with no escape hatches.

---

## Quick Start

```bash
# Verify entire repository
bash tools/ralph-research/verify.sh

# Verify specific document
bash tools/ralph-research/verify.sh --file GA-MD-Renewal-Requirements-Narrative-2026-01-02.md

# Verify documents in a tier
bash tools/ralph-research/verify.sh --tier TIER-1

# Run iterative verification loop (for development)
bash tools/ralph-research/ralph.sh
```

---

## Architecture

### Verification Pipeline (5 Layers)

Ralph runs a sequential verification pipeline with fail-fast behavior:

**LAYER 0: Anti-Shortcut Guardrails** ⚠️ **MUST PASS FIRST**
- Detects TODO/FIXME/WIP/PLACEHOLDER markers
- Blocks lazy section completion ("See above", "Same as X state")
- Catches evidence shortcuts ([FACT] without sources)
- Prevents quality threshold bypasses
- Validates CSV integrity

**LAYER 1: Frontmatter Validation**
- v3.0 template compliance
- Required sections: governance, soc2_compliance, iso_standards, scope, research_quality
- Gap arrays properly populated
- Version 3.0 metadata present

**LAYER 2: Quality Threshold (85%+ Required)**
- Implements 100-point audit rubric:
  - Frontmatter structure (25 pts)
  - Section completeness (20 pts)
  - Evidence classification (25 pts)
  - Citation quality (15 pts)
  - Gap documentation (10 pts)
  - Cross-source congruency (5 pts)
- **FAILS if score < 85**

**LAYER 3: Citation Validation**
- All [FACT] tags have Citation: and Source: fields
- URLs are well-formed
- Source hierarchy (STATUTE > ADMIN_CODE > BOARD)
- Warnings for low citation ratios

**LAYER 4: CSV Consistency**
- Document filename matches CSV entry
- Completion % consistent between frontmatter and CSV (±5% tolerance)
- Status fields consistent across trackers
- Cross-tracker validation (state-research-tracker.csv vs audit CSV)

---

## File Structure

```
tools/ralph-research/
├── verify.sh               # Main verification orchestrator
├── guardrail.sh            # Anti-shortcut pattern detection
├── ralph.sh                # Iterative loop harness (optional)
├── scripts/
│   ├── frontmatter_validator.py      # v3.0 compliance checker
│   ├── evidence_analyzer.py          # [FACT]/[INFERENCE]/[GAP] analysis
│   ├── quality_threshold_check.py    # 100-point rubric scorer
│   ├── citation_validator.py         # Citation quality validator
│   ├── csv_consistency_check.py      # CSV tracker validator
│   └── utils.py                      # Shared utilities
├── config/
│   ├── required-sections.conf        # 14 required sections
│   ├── quality-thresholds.conf       # Scoring thresholds
│   └── guardrail-patterns.conf       # Anti-shortcut patterns
└── state/
    ├── STATUS.md                     # Latest verification status (tracked in git)
    ├── verify.log                    # Latest verification log (ignored)
    └── runs/                         # Per-run evidence (ignored)
        └── YYYYMMDD-HHMMSS-SHA/
            ├── PRE-snapshot.txt
            ├── POST-snapshot.txt
            ├── guardrail.log
            ├── frontmatter-validation.log
            ├── quality-threshold.log
            ├── citation-validation.log
            ├── csv-consistency.log
            └── SUMMARY.txt
```

---

## Usage Modes

### Batch Mode (Default)

Verify all state documents in the repository:

```bash
bash tools/ralph-research/verify.sh
```

### Single-File Mode

Verify one specific document:

```bash
bash tools/ralph-research/verify.sh --file ID-MD-Renewal-Requirements-Narrative-2026-01-02.md
```

### Tier Mode

Verify all documents in a specific tier:

```bash
bash tools/ralph-research/verify.sh --tier TIER-1
```

### Iterative Loop (Development)

For local development with manual fixes between iterations:

```bash
bash tools/ralph-research/ralph.sh
```

The loop will:
1. Run verification
2. If failed, pause for manual fixes
3. Repeat (max 20 iterations)
4. Stop if same failure 3x or no changes 2x

---

## Evidence Collection

Every verification run creates a unique RUN_ID and captures complete evidence:

**RUN_ID Format:** `YYYYMMDD-HHMMSS-{git-sha}`
Example: `20260103-193000-abc123f`

**Evidence Artifacts:**
- `PRE-snapshot.txt` - Repository state before verification (git status, CSV state)
- `POST-snapshot.txt` - Repository state after verification
- `guardrail.log` - Anti-shortcut pattern detection results
- `frontmatter-validation.log` - v3.0 compliance per document
- `quality-threshold.log` - Detailed scoring per document
- `citation-validation.log` - Citation quality analysis
- `csv-consistency.log` - CSV tracker validation results
- `SUMMARY.txt` - Overall pass/fail summary with recommendations

**View Latest Status:**
```bash
cat tools/ralph-research/state/STATUS.md
```

**View Latest Run Evidence:**
```bash
ls -lt tools/ralph-research/state/runs/ | head -2
```

---

## Python Scripts

### frontmatter_validator.py

Validates v3.0 frontmatter compliance.

```bash
python3 tools/ralph-research/scripts/frontmatter_validator.py GA-MD-*.md
```

**Checks:**
- Required top-level fields (document_type, state_abbr, tier, license_type, etc.)
- Required v3.0 sections (governance, soc2_compliance, iso_standards, scope, etc.)
- Gap arrays populated
- Version 3.0 metadata

**Scoring:** Max 25 points

---

### evidence_analyzer.py

Analyzes evidence tag usage and quality.

```bash
python3 tools/ralph-research/scripts/evidence_analyzer.py HI-MD-*.md
```

**Analyzes:**
- [FACT] tag count and citation ratio
- [INFERENCE] tag count and reasoning ratio
- [CRITICAL GAP] tag count
- Evidence distribution across sections

**Scoring:** Max 25 points

---

### quality_threshold_check.py

Calculates comprehensive quality score using 100-point rubric.

```bash
python3 tools/ralph-research/scripts/quality_threshold_check.py KS-MD-*.md
```

**Rubric Breakdown:**
- Frontmatter (25 pts) - via frontmatter_validator
- Sections (20 pts) - completeness and depth
- Evidence (25 pts) - via evidence_analyzer
- Citations (15 pts) - via citation_validator
- Gaps (10 pts) - documentation quality
- Congruency (5 pts) - cross-source tracking

**Pass Threshold:** ≥ 85 points

**JSON Output:**
```bash
python3 tools/ralph-research/scripts/quality_threshold_check.py FILE.md --json
```

---

### citation_validator.py

Validates citation format and quality.

```bash
python3 tools/ralph-research/scripts/citation_validator.py ID-MD-*.md
```

**Checks:**
- Citation: field present for [FACT] tags
- Source: URL present and well-formed
- Quote: or direct evidence present
- .gov domain preference (statute/admin code)

**Scoring:** Max 15 points
**Pass Threshold:** ≥ 10 points (67%)

---

### csv_consistency_check.py

Validates consistency between CSV trackers and documents.

```bash
python3 tools/ralph-research/scripts/csv_consistency_check.py /Users/tmac/research
```

**Validates:**
- Document filename matches CSV entry
- Completion % matches between frontmatter and CSV (±5%)
- Status consistency (COMPREHENSIVE → COMPLETE, PARTIAL → IN_PROGRESS)
- Cross-tracker consistency (state tracker vs audit tracker)

**Hard Fail:** Any inconsistency fails verification

---

## Guardrail Patterns

Ralph detects and blocks these documentation shortcuts:

### Category 1: Incomplete Work Markers
- `TODO`, `FIXME`, `WIP`, `HACK`, `XXX`, `STUB`
- `[PLACEHOLDER]`, `[TBD]`, `[TO BE DETERMINED]`
- `INCOMPLETE`, `PARTIAL`

### Category 2: Research Pending
- `[NEED MORE RESEARCH]`
- `[REQUIRES FURTHER INVESTIGATION]`
- `[PENDING VERIFICATION]`

### Category 3: Lazy Sections
- "See section above"
- "Same as X state"
- "Not applicable (research pending)"

### Category 4: Evidence Shortcuts
- `[FACT] (no source)`
- `Citation: (pending)`, `Source: (TBD)`
- `[FACT] (unable to verify)`

### Category 5: Quality Bypasses
- `completion_percentage: 100 [NOTE: placeholder]`
- "Skip audit", "Bypass validation"

### Category 6: CSV Manipulation
- `TEMP_COMPLETE`, `FAKE_STATUS`
- Obviously fake values (999%)

### Exception Mechanism

Allow documented exceptions with clear reasoning:

```markdown
<!-- guardrail-exception: TODO for pending regulatory change (SB 25 effective 2025-09-01) -->
TODO: Update nutrition CME requirement when SB 25 final rules published
```

---

## Integration Points

### Pre-Commit Hook

Run guardrails before every commit (recommended):

```bash
# .git/hooks/pre-commit
#!/usr/bin/env bash
bash tools/ralph-research/guardrail.sh
if [ $? -ne 0 ]; then
    echo "❌ Commit blocked: Guardrail violations"
    exit 1
fi
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Agent Workflow

For AI agent sessions:

```bash
# Start Ralph loop
bash tools/ralph-research/ralph.sh

# Loop automatically verifies after each iteration
# Agent fixes issues between iterations
# Stops on success or circuit breaker
```

### CI/CD (Optional)

```yaml
# .github/workflows/ralph-verify.yml
name: Ralph Research Verification

on:
  pull_request:
    paths:
      - '**-MD-*.md'
      - '**-DO-*.md'
      - '*.csv'

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pyyaml

      - name: Run Ralph Verification
        run: bash tools/ralph-research/verify.sh
```

---

## Success Criteria

✅ **Ralph PASSES when:**
1. No shortcut patterns detected (TODO, FIXME, placeholders)
2. All documents ≥ 85% quality score
3. v3.0 frontmatter compliance
4. CSV trackers consistent with documents
5. All citations properly formatted with sources

❌ **Ralph FAILS when:**
1. Any guardrail pattern detected
2. Any document < 85% quality score
3. Missing required frontmatter sections
4. CSV/document mismatch (completion %, status)
5. Evidence of premature completion claims

---

## Common Workflows

### Check Current Status

```bash
cat tools/ralph-research/state/STATUS.md
```

### View Latest Run Details

```bash
RUN_DIR=$(ls -td tools/ralph-research/state/runs/* | head -1)
cat ${RUN_DIR}/SUMMARY.txt
```

### Debug Failed Quality Check

```bash
# See which documents failed
grep '\[FAIL' tools/ralph-research/state/runs/*/quality-threshold.log | tail -20

# Check specific document score
python3 tools/ralph-research/scripts/quality_threshold_check.py GA-MD-*.md
```

### Fix Guardrail Violations

```bash
# See what patterns were detected
cat tools/ralph-research/state/runs/*/guardrail.log | grep '\[VIOLATION\]'

# Or run guardrails standalone
bash tools/ralph-research/guardrail.sh
```

### Verify Single Document After Fix

```bash
bash tools/ralph-research/verify.sh --file ID-MD-Renewal-Requirements-Narrative-2026-01-02.md
```

---

## Dependencies

**Runtime:**
- Bash 4.0+ (orchestration)
- Python 3.11+ (scoring scripts)
- Git (snapshots, diffs)
- ripgrep (pattern detection, optional - falls back to grep)

**Python Libraries:**
- `pyyaml` (frontmatter parsing)

Install dependencies:
```bash
pip install pyyaml
```

On macOS with Homebrew:
```bash
brew install ripgrep
```

---

## Troubleshooting

### "No module named 'yaml'"

Install PyYAML:
```bash
pip3 install pyyaml
```

### "Permission denied" when running scripts

Make scripts executable:
```bash
chmod +x tools/ralph-research/*.sh
chmod +x tools/ralph-research/scripts/*.py
```

### Verification fails on CSV consistency

Check that CSV trackers exist:
```bash
ls -l state-research-tracker.csv
ls -l audit-2026-01-03/67-board-audit-tracker-MD-DO.csv
```

Update CSV with current document state.

### False positive guardrail violations

Add exception comment:
```markdown
<!-- guardrail-exception: Legitimate use case explanation -->
TODO: Update when official rule published
```

---

## Philosophy

Ralph Research follows these principles:

1. **Evidence-Based Verification** - Every run produces immutable evidence artifacts
2. **Single Source of Truth** - `verify.sh` is the definitive quality gate
3. **Fail-Fast Design** - Guardrails run first, block if violations found
4. **No Shortcuts Allowed** - Agents must complete work properly, not claim completion
5. **Deterministic Gating** - Binary pass/fail with clear exit codes
6. **Multi-Layer Enforcement** - Redundant validation layers prevent bypasses
7. **Zero External Dependencies** - Pure bash + Python, works anywhere

---

## Comparison: Karematch vs Research

| Aspect | Karematch (Code) | Research (Documentation) |
|--------|------------------|--------------------------|
| **Quality Gate** | `npm run lint` → ESLint | `guardrail.sh` → Pattern detection |
| **Type Safety** | `npm run check` → TypeScript | `frontmatter_validator.py` → YAML |
| **Testing** | `npm test` → Vitest | `quality_threshold_check.py` → Rubric |
| **Threshold** | 80% test coverage | 85% quality score |
| **Shortcuts Blocked** | TypeScript suppressions | TODO/FIXME/placeholders |
| **Test Skips** | `.skip()` patterns | Incomplete sections |
| **Evidence** | Test coverage reports | Citation quality analysis |

---

## Next Steps

After implementing Ralph:

1. **Test on existing documents** - Run verification on current state
2. **Fix failing documents** - Apply v3.0 frontmatter, add citations, complete gaps
3. **Install pre-commit hook** - Prevent shortcuts from being committed
4. **Integrate with agent workflow** - Use `ralph.sh` loop during research sessions
5. **Monitor STATUS.md** - Track verification status over time

---

## Support

For issues or questions:

- View evidence artifacts in `tools/ralph-research/state/runs/`
- Check `STATUS.md` for latest verification results
- Review Python script output for detailed error messages
- Run individual validators for targeted debugging

Ralph is your documentation quality guardian - trust the process, fix the root causes, and maintain high standards! 🛡️
