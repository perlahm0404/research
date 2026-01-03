# TIER 2 Research Prompt - Split-Board States
**Version:** 1.0
**Created:** 2026-01-02
**Target Completion Time:** 10-14 hours per state (5-7 hours per license type)
**License Types:** MD AND DO (separate documents required)

---

## OVERVIEW

You are researching a **split-board state** where MD and DO physicians are regulated by **DIFFERENT boards with DIFFERENT CME requirements**.

**What makes Tier 2 challenging:**
- Separate MD board vs. DO board (not unified)
- **Different CME hours** (e.g., Maine: MD 40/2yr vs. DO 100/2yr)
- **Different renewal cycles** (e.g., Washington: MD 200/4yr vs. DO 150/3yr)
- **Different category requirements** (e.g., Arizona: MD AMA vs. DO AOA 1-A)
- Each license type requires SEPARATE comprehensive research

**Tier 2 Split-Board States (13 total):**
AZ, CA, FL, ME, MI, NV, PA, TN, VT, WA, WV

---

## CRITICAL PROTOCOL: DUAL RESEARCH DOCUMENTS

### TWO Separate Documents Required

For a split-board state like **Arizona**, you will produce:

1. `Arizona-MD-Renewal-Requirements-Narrative-2026-01-02.md`
2. `Arizona-DO-Renewal-Requirements-Narrative-2026-01-02.md`

**EACH document:**
- Is complete and standalone
- Covers ONE license type only
- Includes board-specific governing statute
- Documents board-specific CME requirements
- Cannot make assumptions about the other board

### Why Separate Documents?

From FSMB analysis:
- **Arizona:** MD board (40 hrs, AMA Category 1) vs. DO board (40 hrs, 24 AOA 1-A required)
- **Maine:** MD board (40 hrs/2yr) vs. DO board (100 hrs/2yr) - 2.5x difference
- **Nevada:** MD board (40 hrs/2yr) vs. DO board (40 hrs/YEAR) - doubled frequency
- **Washington:** MD board (200 hrs/4yr) vs. DO board (150 hrs/3yr) - different cycles

---

## RESEARCH APPROACH: SEQUENTIAL, NOT PARALLEL

### Recommended Sequence for Split-Board State

**Step 1: MD Research (5-7 hours)**
- Complete full MD document using Tier 1 protocol
- Identify MD board, statute, admin code
- Document all MD-specific requirements

**Step 2: DO Research (5-7 hours)**
- Complete full DO document
- Identify separate DO board (often different agency)
- Document all DO-specific requirements
- Compare with MD findings (create comparison table)

**Step 3: Comparison & Validation (1-2 hours)**
- Create side-by-side comparison table
- Note all differences with citations
- Validate each board's statutory authority
- Update tracker for BOTH documents

---

## FINDING SEPARATE BOARDS

### Common Board Name Patterns

**MD Boards:**
- "State Medical Board"
- "Board of Medical Examiners"
- "Department of Health - Medical Licensing"
- "[STATE] Medical Board"

**DO Boards:**
- "State Board of Osteopathic Physicians"
- "State Board of Osteopathic Examiners"
- "Osteopathic Medical Board"
- "[STATE] Osteopathic Board"
- Sometimes: Department of Health (different division)

**Different Agencies:**
- MD: Department of Health, Board of Medical Licensing
- DO: Department of Regulatory Affairs, Osteopathic Board
- They may have DIFFERENT statutes, DIFFERENT portals, DIFFERENT CME systems

### Search Strategy for DO Board

1. Google: "[STATE] osteopathic board"
2. Google: "[STATE] DO license renewal"
3. Check main medical board website for "Osteopathic Physician" link
4. State legislative website: search "osteopathic" in bills/statutes
5. If not found: Contact MD board and ask "Where do DOs renew?"

---

## STATUTORY AUTHORITY FOR EACH BOARD

### DO NOT Assume Same Statute

**Arizona Example:**
- **MD Board:** Governed by A.R.S. § 32-3248 (Medical Practice Act)
- **DO Board:** Governed by A.R.S. § 32-3248.02 (separate section for osteopathic)
- Different statutes = potentially different requirements

**Maine Example:**
- **MD Board:** 02 ME Code Rules § 373-1-11 (covers allopathic physicians)
- **DO Board:** 02 ME Code Rules § 383-14-1 (separate title for osteopathic)
- Over 2.5x CME hours difference (40 vs. 100)

### Your Task: Find BOTH Statutes

For each board (MD and DO):
1. Locate governing statute (full citation)
2. Locate admin code (full citation)
3. Locate board website and portal
4. Document both in separate YAML frontmatters

---

## RESEARCH PROCESS (10-14 hours total)

### Phase 1: MD Document (5-7 hours)
Follow **TIER-1-Research-Prompt** exactly:

1. Identify MD board & statute
2. Extract core MD requirements
3. MD-specific controlled substance context
4. MD-specific CME tracking system
5. MD exemptions & board certification
6. MD audit & reinstatement procedures
7. Verify against FSMB
8. Complete all 14 sections

**Output:** `[STATE]-MD-Renewal-Requirements-Narrative-YYYY-MM-DD.md`

---

### Phase 2: DO Document (5-7 hours)
Follow **TIER-1-Research-Prompt** but for DO board:

1. Identify separate DO board (different website, different contacts)
2. Extract core DO requirements (likely DIFFERENT from MD)
3. DO-specific controlled substance context
4. DO-specific CME tracking system (may be different portal)
5. DO exemptions (AOA vs. ABMS)
6. DO audit & reinstatement procedures
7. Verify against FSMB (if DO listed separately)
8. Complete all 14 sections

**Output:** `[STATE]-DO-Renewal-Requirements-Narrative-YYYY-MM-DD.md`

**Critical:** DO NOT copy from MD document. Research independently.

---

### Phase 3: Comparison & Gap Analysis (1-2 hours)

#### Create Comparison Table

Add to DO document:

```markdown
## Comparison: [STATE] MD vs. DO Renewal Requirements

| Factor | MD Board | DO Board | Difference |
|--------|----------|----------|-----------|
| **Board Name** | [Name] | [Name] | Different agency? Same? |
| **Governing Statute** | [Citation] | [Citation] | Same statute or different? |
| **Administrative Code** | [Citation] | [Citation] | |
| **Total CME Hours** | [X] hrs/[Y] yrs | [X] hrs/[Y] yrs | Same or different? |
| **Renewal Cycle** | [Frequency] | [Frequency] | Same or different? |
| **CME Categories** | [AMA/AOA] | [AOA specific] | |
| **Mandatory Topics** | [List] | [List] | Topics differ? |
| **Opioid CME Requirement** | [Yes/No, X hrs] | [Yes/No, X hrs] | |
| **CME Tracking System** | [System name] | [System name] | Same or different portal? |
| **Renewal Fee** | $[X] | $[X] | |
| **Board Cert Exemption** | ABMS/AOA/Both | AOA only | |
| **Audit Frequency** | [Random/For-cause] | [Random/For-cause] | |

### Key Differences Requiring Special Attention

1. **[Difference 1]** - [Explains why this matters]
   - MD statute: [Citation]
   - DO statute: [Citation]
   - Impact: [Rules engine consideration]

2. **[Difference 2]** - [Why it matters]
   - Impact: [Rules engine consideration]

[etc.]
```

#### Identify Critical Differences

Flag any of these situations:

1. **Different CME hours** (e.g., MD 40/2yr, DO 100/2yr)
   - Research WHY (statute mandate? AOA requirement?)
   - Cite statute sections that differ

2. **Different renewal cycles** (e.g., MD biennial, DO triennial)
   - Confirm in both statutes
   - Impact on compliance calendar

3. **Different category requirements** (e.g., MD all AMA, DO 50% AOA 1-A)
   - Document exact requirements for each
   - Rules engine must calculate separately

4. **Different controlled substance rules**
   - Opioid hours differ between MD/DO?
   - Cite relevant statute sections

5. **Different exemptions**
   - ABMS for MD but AOA only for DO?
   - Board certification requirements differ?

---

## VALIDATION: CROSS-BOARD CONGRUENCY

### Verify Each Board Independently

For MD document:
```
[FACT - STATUTE] Arizona Medical Practice Act requires 40 hours Category 1 CME every 2 years.
Citation: A.R.S. § 32-3248
Source: https://legislature.az.gov
Congruency Check: FSMB says "40 hours every 2 years, AMA Category 1" ✅
```

For DO document:
```
[FACT - STATUTE] Arizona Osteopathic Medical Board requires 40 hours CME every 2 years,
of which 24 must be AOA Category 1-A.
Citation: A.R.S. § 32-3248.02
Source: https://legislature.az.gov
Congruency Check: FSMB says "40 hours every 2 years; 24 must be AOA Category 1-A" ✅
```

### Explain Why Boards Differ

If CME hours differ, research WHY:

**Example: Maine (40 MD vs. 100 DO)**
```
Potential Reasons Researched:
- [ ] Different statute mandates (DO statute requires more hours)
- [ ] AOA requirements (osteopathic physicians have additional training requirement)
- [ ] Different board policy (contact board to confirm)
- [ ] Historical precedent (DO board more stringent)

Finding: ME statute § 383-14-1 (DO board) explicitly requires "100 hours every 2 years"
while § 373-1-11 (MD board) requires "40 hours every 2 years". Different statutory
provisions explain the 2.5x difference.
```

---

## SPLIT-BOARD SPECIFIC RESEARCH TASKS

### Task 1: Identify Board Separation

Document:
- Is there a separate DO board or division?
- Different website?
- Different contact info?
- Different renewal portal or same system?

**Research Steps:**
1. Look at main medical board website
2. Search for "Osteopathic" link or separate board
3. Check state legislative database for DO licensing statute
4. Contact MD board: "Where do DOs renew?"

---

### Task 2: Verify Statutory Separation

For both MD and DO:
1. Find the exact statute section governing that board
2. Note if same statute or different statute
3. Document if same admin code or different
4. Check effective dates of any recent changes

**Example:**
```
MD Board Statute: 59 O.S. § 480-518.1
DO Board Statute: 62 O.S. § 620-642
These are DIFFERENT titles (59 vs. 62) = separate governing authorities
```

---

### Task 3: Compare CME Tracking Systems

Do MD and DO physicians:
- Use same portal or different portals?
- Report to same CME tracking system or different?
- Have access to same information?

**Why it matters:**
- Physician confusion if different portals
- Data consistency issues for compliance checking

---

### Task 4: Controlled Substance Prescribing Rules

For both MD and DO:
1. Opioid prescribing limits (same or different)?
2. PDMP requirements (same or different)?
3. DEA registration (same or different)?
4. Telemedicine restrictions (same or different)?

**Research:**
- Prescription monitoring program statute (often shared)
- But board-specific CME requirements may differ

---

## FRONTMATTER FOR SPLIT-BOARD STATES

### MD Document Frontmatter

```yaml
---
document_type: "License Renewal Requirements - Narrative Research"
state: "AZ"
license_type: "MD"
board_name: "Arizona Medical Board"
board_abbreviation: "AMB"
board_code: "AZ-M"
board_website: "https://medicalboard.az.gov"
renewal_portal: "https://medicalboard.az.gov/licensee-services"
split_board_state: true
split_board_partner: "Arizona Board of Osteopathic Medicine Examiners"
split_board_partner_research_doc: "Arizona-DO-Renewal-Requirements-Narrative-YYYY-MM-DD.md"
research_date: "2026-01-02"
last_verified: "2026-01-02"
researcher: "Claude AI"

governance:
  framework: "State Medical Board Regulatory Framework"
  authority_level: "STATE"
  primary_statute: "A.R.S. § 32-3248 (Arizona Medical Practice Act)"
  administrative_code: "Arizona Administrative Code Title 4, Chapter 19"

research_quality:
  completeness_percentage: 75
  validation_level: "COMPREHENSIVE"
  source_count_minimum: 2
  source_hierarchy_applied: true
  cross_source_congruency_tracked: true
  split_board_comparison_included: true

scope:
  split_board_note: "This document covers ALLOPATHIC PHYSICIANS (MD) only. Osteopathic physicians (DO) are regulated separately by Arizona Board of Osteopathic Medicine Examiners and have different CME requirements."
  included:
    - "MD-specific license renewal frequency and deadlines"
    - "MD CME requirements (hours, categories, topics)"
    - "MD renewal fees and late penalties"
    - "MD-specific grace periods"
    - "MD-specific residency/fellowship CME credit"
    - "MD CME audit and verification procedures"
    - "MD lapsed license reinstatement"
    - "MD exemptions and alternatives to CME"
    - "MD controlled substance prescribing context"
  excluded:
    - "DO (Osteopathic Physician) requirements - see separate document"
    - "NP (Nurse Practitioner) requirements"
    - "Initial licensing exam requirements"

comparison_required: true
comparison_with_boards:
  - "Arizona Board of Osteopathic Medicine Examiners (DO board)"

version: "1.0.0"
version_history:
  - version: "1.0.0"
    date: "2026-01-02"
    changes: "Initial research for split-board state MD requirements"

---
```

### DO Document Frontmatter

Same structure but:
- `license_type: "DO"`
- `board_name: "Arizona Board of Osteopathic Medicine Examiners"`
- `board_code: "AZ-O"`
- `split_board_partner_research_doc: "Arizona-MD-Renewal-Requirements-Narrative-YYYY-MM-DD.md"`
- Note in scope: "This document covers OSTEOPATHIC PHYSICIANS (DO) only."

---

## COMPLETION RUBRIC FOR SPLIT-BOARD STATES

### Minimum (50% completion):
- [ ] MD document: Core requirements, fees, board info
- [ ] DO document: Core requirements, fees, board info
- [ ] Both documents identify as split-board state
- [ ] Reference each other in frontmatter

### Standard (70% completion):
- [ ] MD document: 12 sections complete, gaps identified
- [ ] DO document: 12 sections complete, gaps identified
- [ ] Comparison table created
- [ ] Key differences highlighted with citations
- [ ] Evidence classification applied to all major claims

### Comprehensive (85%+ completion):
- [ ] Both documents: All 14 sections complete
- [ ] Cross-source congruency verified for both boards
- [ ] Statutory differences explained
- [ ] All gaps documented with search attempts
- [ ] Comparison table comprehensive with impact analysis
- [ ] Ready for validation with both boards

---

## UPDATING TRACKER FOR SPLIT-BOARD STATE

After completing BOTH documents:

1. Open `/Users/tmac/research/state-research-tracker.csv`
2. Find state row
3. Update:
   - `md_status`: "COMPLETE"
   - `md_completion_%`: Percentage (target 80%+)
   - `md_document`: "Arizona-MD-Renewal-Requirements-Narrative-2026-01-02.md"
   - `do_status`: "COMPLETE"
   - `do_completion_%`: Percentage (target 80%+)
   - `do_document`: "Arizona-DO-Renewal-Requirements-Narrative-2026-01-02.md"
   - `last_updated`: Today's date
   - `notes`: "Split-board comparison included. Key differences: [list them]"

---

## QUALITY CHECKS FOR SPLIT-BOARD RESEARCH

Before marking complete:

**MD Document:**
- [ ] Frontmatter identifies as split-board
- [ ] All 14 sections complete (or gaps documented)
- [ ] Evidence classification on all claims
- [ ] No DO requirements included
- [ ] References DO document in frontmatter

**DO Document:**
- [ ] Frontmatter identifies as split-board
- [ ] All 14 sections complete (or gaps documented)
- [ ] Evidence classification on all claims
- [ ] No MD requirements included (except comparison)
- [ ] References MD document in frontmatter

**Comparison:**
- [ ] Comparison table included in one document
- [ ] All major differences highlighted
- [ ] Differences cited to statute
- [ ] Explains WHY boards differ (if known)
- [ ] Rules engine impact noted

**Consistency:**
- [ ] Same research date for both documents
- [ ] Same researcher name for both documents
- [ ] Consistent formatting in both documents
- [ ] Cross-references accurate in both frontmatters

---

## TIME ALLOCATION (10-14 hours)

| Phase | Time | Output |
|-------|------|--------|
| MD Research | 5-7 hrs | MD document (70-80% complete) |
| DO Research | 5-7 hrs | DO document (70-80% complete) |
| Comparison & Validation | 1-2 hrs | Comparison table, gap analysis |
| **TOTAL** | **10-14 hrs** | **2 documents ready for validation** |

---

## TIER 2 STATE PRIORITY ORDER

Research states in this order (easiest to hardest):

**Priority 1 (Similar requirements):**
- AZ (both 40/2yr, similar topics)
- TN (both 40/2yr)
- VT (both 30/2yr)

**Priority 2 (Different categories):**
- CA (both 50/2yr but different AOA requirements)
- PA (both 100/2yr but different Cat 1-A split)
- FL (similar hours but different AOA topics)

**Priority 3 (Significantly different):**
- MI (both 150/3yr but different Cat 1 split)

**Priority 4 (Major differences):**
- ME (40 vs. 100 - 2.5x) ⚠️
- NV (40/2yr vs. 40/yr - doubled frequency) ⚠️
- WA (200/4yr vs. 150/3yr - different cycles) ⚠️
- WV (50 vs. 32 - DO less than MD) ⚠️

---

*This research prompt supports CREDMATE's CME accuracy framework for TIER 2 (Split-Board) states requiring dual MD/DO research.*