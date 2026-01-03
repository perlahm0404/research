# Comprehensive Audit Prompt - State License Renewal Research v3.0

**Version:** 1.0
**Created:** 2026-01-03
**Purpose:** Standardized audit template for validating state research documents against v3.0 requirements
**Scope:** MD and DO license renewal research documents

---

## AUDIT OVERVIEW

This prompt provides a comprehensive validation framework for auditing state license renewal research documents against the v3.0 research prompt standard. All documents are scored against v3.0 requirements regardless of when they were created.

**Audit Outputs:**
1. Document score (0-100 scale)
2. Compliance level (EXCELLENT/GOOD/FAIR/POOR/CRITICAL)
3. Missing elements checklist
4. Detailed remediation guidance

---

## PHASE 1: DOCUMENT IDENTIFICATION

### Extract Basic Metadata

**From Frontmatter (YAML header):**
- `state_abbr`: [Extract state abbreviation]
- `state_name`: [Extract full state name]
- `license_type`: [MD or DO]
- `board_name`: [Extract official board name]
- `tier`: [TIER-1, TIER-2, or TIER-3]
- `research_date`: [Extract research date]
- `last_verified`: [Extract verification date]
- `completion_percentage`: [Extract claimed %]
- `status`: [Extract status]

**From Filename:**
- Format: `[State]-[Type]-Renewal-Requirements-Narrative-YYYY-MM-DD.md`
- Document date: [Extract from filename]
- Naming convention compliance: YES / NO

**Document Statistics:**
- Total line count: [Count all lines]
- Total word count: [Estimate]
- File size: [KB]

---

## PHASE 2: FRONTMATTER VALIDATION (25 points)

### 2.1 Document Metadata (5 points)

**Required Fields:**
- [ ] `state_abbr` present
- [ ] `state_name` present
- [ ] `license_type` present (MD or DO only)
- [ ] `board_name` present
- [ ] `research_date` present (format: YYYY-MM-DD)
- [ ] `last_verified` present
- [ ] `researcher` present

**Scoring:**
- All 7 fields present: **5 points**
- 5-6 fields present: **3 points**
- 3-4 fields present: **1 point**
- <3 fields: **0 points**

**Missing Fields:** [List any missing fields]

---

### 2.2 Governance Section (5 points)

**Required Structure:**
```yaml
governance:
  framework: "State Medical/Osteopathic Board Regulatory Framework"
  authority_level: "STATE"
  primary_statute: "[Citation]"
  administrative_code: "[Citation]"
```

**Checklist:**
- [ ] `governance:` section exists
- [ ] `framework` field present
- [ ] `authority_level` present (should be "STATE")
- [ ] `primary_statute` present with actual citation
- [ ] `administrative_code` present with actual citation

**Scoring:**
- All 5 elements present: **5 points**
- 3-4 elements present: **3 points**
- 1-2 elements present: **1 point**
- None: **0 points**

**Remediation (if missing):**
```yaml
governance:
  framework: "State Medical Board Regulatory Framework"
  authority_level: "STATE"
  primary_statute: "[Insert state statute citation, e.g., '59 O.S. § 480-518.1']"
  administrative_code: "[Insert admin code, e.g., '435 OAC']"
```

---

### 2.3 SOC2 Compliance Section (3 points)

**Required Structure:**
```yaml
soc2_compliance:
  scope: "Renewal requirements research document"
  data_classification: "Public (regulatory information)"
  version_control: "Git-tracked markdown"
  change_management: "Updated by [METHOD] when regulations change"
  audit_trail: "Research methodology documented in Section: Validation Standards"
```

**Checklist:**
- [ ] `soc2_compliance:` section exists
- [ ] At least 3 of 5 fields present

**Scoring:**
- Section present with 4-5 fields: **3 points**
- Section present with 2-3 fields: **2 points**
- Section present with 1 field: **1 point**
- Section missing: **0 points**

**Remediation (if missing):**
Add entire SOC2 section per v3.0 template (lines 107-113 of research prompt).

---

### 2.4 ISO Standards Section (3 points)

**Required Structure:**
```yaml
iso_standards:
  applicable_standards:
    - "ISO 9001:2015 (Quality management - documentation & records)"
    - "ISO 27001:2022 (Information security - regulatory data handling)"
  documentation_standard: "ISO/IEC/IEEE 42010 (Architecture description)"
  approval_status: "[DRAFT|APPROVED|IN REVIEW]"
```

**Checklist:**
- [ ] `iso_standards:` section exists
- [ ] `applicable_standards` array present
- [ ] `approval_status` field present

**Scoring:**
- Section present with all 3 fields: **3 points**
- Section present with 2 fields: **2 points**
- Section present with 1 field: **1 point**
- Section missing: **0 points**

**Remediation (if missing):**
Add entire ISO section per v3.0 template (lines 114-120 of research prompt).

---

### 2.5 Research Quality Metrics (4 points)

**Required Structure:**
```yaml
research_quality:
  completeness_percentage: [0-100]
  validation_level: "[COMPREHENSIVE|PARTIAL|PRELIMINARY]"
  source_count_minimum: "2 per requirement"
  source_hierarchy_applied: true
  cross_source_congruency_tracked: true
  gap_documentation_standard: "CRITICAL|HIGH|MEDIUM|LOW"
```

**Checklist:**
- [ ] `research_quality:` section exists
- [ ] `completeness_percentage` present (0-100)
- [ ] `validation_level` present
- [ ] `source_hierarchy_applied` present (true/false)
- [ ] `cross_source_congruency_tracked` present

**Scoring:**
- All 5+ fields present: **4 points**
- 3-4 fields present: **2 points**
- 1-2 fields present: **1 point**
- Section missing: **0 points**

**Remediation (if missing):**
Add complete research_quality section. Estimate completeness_percentage based on gaps documented.

---

### 2.6 Scope Statement (2 points)

**Required Structure:**
```yaml
scope:
  included:
    - "License renewal frequency and deadlines"
    - "CME requirements (hours, categories, topics)"
    - [Additional included items...]
  excluded:
    - "Initial licensing exam requirements"
    - "Medical school accreditation standards"
    - [Additional excluded items...]
```

**Checklist:**
- [ ] `scope:` section exists
- [ ] `included:` array with at least 5 items
- [ ] `excluded:` array with at least 3 items

**Scoring:**
- Both arrays present with adequate items: **2 points**
- One array present: **1 point**
- Section missing: **0 points**

**Remediation (if missing):**
Copy scope section from v3.0 prompt template (lines 131-149).

---

### 2.7 Gap Documentation in Frontmatter (3 points)

**Required Structure:**
```yaml
critical_gaps:
  - gap: "[Description]"
    priority: "CRITICAL"
    impact: "[Impact description]"

high_gaps:
  - gap: "[Description]"
    priority: "HIGH"
    impact: "[Impact description]"

medium_gaps:
  - gap: "[Description]"
    priority: "MEDIUM"
    impact: "[Impact description]"
```

**Checklist:**
- [ ] `critical_gaps:` array exists (may be empty)
- [ ] `high_gaps:` array exists (may be empty)
- [ ] Gap items include `gap`, `priority`, and `impact` fields

**Scoring:**
- All 3 gap arrays present with proper structure: **3 points**
- 2 gap arrays present: **2 points**
- 1 gap array present: **1 point**
- No gap arrays: **0 points**

**Remediation (if missing):**
Add gap arrays even if empty. Populate based on [CRITICAL GAP] tags found in document body.

---

**FRONTMATTER SCORE: ____ / 25**

---

## PHASE 3: SECTION COMPLETENESS (20 points)

### 3.1 Required Sections Present (15 points)

**Per v3.0 Prompt, Required Sections (in order):**

1. [ ] **Executive Summary** (3-5 bullet points with key findings)
2. [ ] **Board Information & Authority** (Official board name, statute, admin code, URLs)
3. [ ] **Lifecycle Phases & Grace Periods** (Phase 1: First renewal, Phase 2: After grace, Phase 3: Ongoing)
4. [ ] **CME Requirements - Total Hours & Categories** (Total hours, category breakdown, cycle)
5. [ ] **CME Topic Requirements** (Mandatory topics with [FACT] tags)
6. [ ] **Controlled Substance Context** (MD/DO only: Opioid limits, telemedicine, PMP)
7. [ ] **Audit & Verification Procedures** (CME verification, audit process, penalties)
8. [ ] **Exemptions & Alternatives** (Board cert, residency, military, hardship)
9. [ ] **Renewal Fees & Timeline** (Fees, late fees, renewal windows, grace periods)
10. [ ] **Lapsed License Reinstatement** (Tier 1: <1yr, Tier 2: 1-3yr, Tier 3: >3yr)
11. [ ] **CME Tracking Systems** (CE Broker, board portal, reporting method)
12. [ ] **State-Specific Requirements** (Medical marijuana, jurisprudence, other unique requirements)
13. [ ] **Research Gaps & Limitations** (Critical/High/Medium/Low gaps documented)
14. [ ] **Sources Cited** (Primary sources, secondary sources, hierarchy)
15. [ ] **Appendix: Uncovered Topics** (Optional: Out-of-scope items)

**Scoring:**
- 15 sections present: **15 points**
- 13-14 sections: **12 points**
- 11-12 sections: **9 points**
- 9-10 sections: **6 points**
- 7-8 sections: **3 points**
- <7 sections: **0 points**

**Missing Sections:** [List any missing sections]

**Remediation:**
For each missing section, add heading and populate with template structure from v3.0 prompt.

---

### 3.2 Sections in Correct Order (5 points)

**Check if sections follow the v3.0 prescribed order (1-15 above).**

**Scoring:**
- Sections in exact order: **5 points**
- Minor deviations (1-2 sections out of order): **3 points**
- Major deviations (3+ sections out of order): **1 point**
- Completely out of order: **0 points**

**Remediation:**
Reorder sections to match v3.0 sequence. Use markdown headings (##) consistently.

---

**SECTION COMPLETENESS SCORE: ____ / 20**

---

## PHASE 4: EVIDENCE CLASSIFICATION SYSTEM (25 points)

### 4.1 [FACT] Tags Used Consistently (7 points)

**Evidence Types Required:**
- `[FACT - STATUTE]` - Direct from state statute
- `[FACT - ADMIN_CODE]` - Direct from administrative code
- `[FACT - BOARD]` - Direct from official board website/portal
- `[FACT]` - General facts with clear source

**Audit Questions:**
- Are factual claims consistently prefixed with [FACT - SOURCE] tags?
- Are [FACT] tags used for all major requirements (CME hours, renewal cycle, fees, mandatory topics)?
- Do [FACT] tags specify source type (STATUTE, ADMIN_CODE, BOARD)?

**Tag Count:**
- Total [FACT] tags in document: [Count]
- [FACT - STATUTE] tags: [Count]
- [FACT - ADMIN_CODE] tags: [Count]
- [FACT - BOARD] tags: [Count]

**Scoring:**
- 50+ [FACT] tags with consistent source typing: **7 points**
- 30-49 [FACT] tags: **5 points**
- 15-29 [FACT] tags: **3 points**
- <15 [FACT] tags: **0 points**

**Remediation:**
Add [FACT - SOURCE] tags to all factual claims. Example:
```
[FACT - STATUTE] Alabama requires 25 hours of AMA PRA Category 1 CME per calendar year.
Citation: Ala. Code § 34-24-75
```

---

### 4.2 Citations with URLs (8 points)

**For each [FACT] tag, verify:**
- [ ] Citation included (statute number, code section, or URL)
- [ ] URL to source included
- [ ] Quote from source included (verbatim text)
- [ ] Last verified date included

**Example Gold Standard Format:**
```
[FACT - STATUTE] Oklahoma requires 60 hours of Category 1 CME every 3 years.

Citation: 59 O.S. § 495a.1
Source: https://legislature.ok.gov/bills/
Quote: "Each physician shall complete a minimum of 60 hours of Category I
continuing medical education within every three-year period."
Last Verified: 2026-01-02
```

**Citation Quality Assessment:**
- Sample 10 random [FACT] tags
- Count how many include citation + URL + quote

**Percentage with full citations:** [Calculate]

**Scoring:**
- 90-100% facts with citation + URL + quote: **8 points**
- 70-89%: **6 points**
- 50-69%: **4 points**
- 30-49%: **2 points**
- <30%: **0 points**

**Remediation:**
For each [FACT] tag missing components, add:
1. Full citation (statute section or admin code rule)
2. Direct URL to official source
3. Verbatim quote from source
4. Last verified date

---

### 4.3 [FACT] Statements Include Verbatim Quotes (5 points)

**Check if [FACT] tags include actual quoted regulatory language.**

**Quote Format:**
```
Quote: "[Exact text from statute or regulation]"
```

**Sample Assessment:**
- Sample 10 [FACT - STATUTE] or [FACT - ADMIN_CODE] tags
- Count how many include verbatim quotes in quotation marks

**Percentage with quotes:** [Calculate]

**Scoring:**
- 80-100% include quotes: **5 points**
- 60-79%: **4 points**
- 40-59%: **2 points**
- <40%: **0 points**

**Remediation:**
Add `Quote: "[verbatim text]"` line after each statutory [FACT] tag.

---

### 4.4 [INFERENCE] Tags with Confidence Levels (3 points)

**Required Format:**
```
[INFERENCE - HIGH CONFIDENCE] Description of inferred fact

Reasoning: [Explain logic]
Supporting facts:
- [FACT 1]
- [FACT 2]
Confidence: HIGH (because...)
```

**Confidence Levels:**
- `HIGH CONFIDENCE` - Strong evidence from multiple sources
- `MEDIUM CONFIDENCE` - Some evidence but gaps exist
- `LOW CONFIDENCE` - Speculative, needs verification

**Audit:**
- Total [INFERENCE] tags: [Count]
- [INFERENCE] tags with confidence level: [Count]
- Percentage with confidence level: [Calculate]

**Scoring:**
- 90-100% inferences include confidence level: **3 points**
- 70-89%: **2 points**
- 50-69%: **1 point**
- <50%: **0 points**

**Remediation:**
For each [INFERENCE] without confidence level:
1. Add `- HIGH CONFIDENCE`, `- MEDIUM CONFIDENCE`, or `- LOW CONFIDENCE`
2. Add "Reasoning:" section explaining logic
3. Add "Supporting facts:" list
4. Add verification method if medium/low confidence

---

### 4.5 [CRITICAL GAP] Tags Used (2 points)

**Required Format:**
```
[CRITICAL GAP] Description of what is unknown

What We Know:
- [FACT 1]
- [FACT 2]

What We Don't Know:
- [Gap 1]
- [Gap 2]

Attempted Sources:
- [Source 1 URL] - Searched for "[terms]" - NOT FOUND
- [Source 2 URL] - Checked [sections] - NOT FOUND

Verification Methods:
1. Contact board at [phone/email]
2. FOIA request for [documents]

Rules Engine Impact: [Explain why critical]
Priority: CRITICAL
```

**Audit:**
- Total [CRITICAL GAP] tags: [Count]
- [HIGH GAP] / [MEDIUM GAP] / [LOW GAP] tags: [Count]

**Scoring:**
- Gap tags used with proper structure: **2 points**
- Gap tags used but incomplete structure: **1 point**
- No gap tags (or gaps exist but not tagged): **0 points**

**Remediation:**
Identify unknowns and add [CRITICAL GAP] tags with full structure.

---

**EVIDENCE CLASSIFICATION SCORE: ____ / 25**

---

## PHASE 5: SOURCE VALIDATION & CITATIONS (15 points)

### 5.1 Cross-Source Congruency Tracking (5 points)

**Check for Cross-Validation Format:**
```
Cross-Source Validation:
- [FACT - STATUTE]: 60 hours [CONGRUENCY: 3/3 sources]
- [FACT - ADMIN_CODE]: 60 hours [CONGRUENCY: 3/3 sources]
- [FACT - BOARD]: 60 hours [CONGRUENCY: 3/3 sources]
```

**Or Conflict Documentation:**
```
Cross-Source Congruency: Conflict detected ⚠️
[FACT - STATUTE]: 40 hours
[FACT - BOARD]: 50 hours - CONFLICT

Resolution: Applied source hierarchy - STATUTE takes precedence
Authority: Per conflict resolution policy, statute > board website
```

**Audit:**
- Are major requirements validated across multiple sources?
- Is congruency explicitly tracked (e.g., "3/3 sources agree")?
- Are conflicts documented and resolved?

**Scoring:**
- Consistent cross-source validation throughout: **5 points**
- Partial cross-source validation (some sections): **3 points**
- Minimal cross-source validation: **1 point**
- No cross-source validation: **0 points**

**Remediation:**
For major requirements (CME hours, renewal cycle, fees, mandatory topics):
1. Check statute
2. Check admin code
3. Check board website
4. Document congruency: "[CONGRUENCY: X/Y sources agree]"

---

### 5.2 "Sources Cited" Section Complete (5 points)

**Required Structure:**
```
## SOURCES CITED

### PRIMARY SOURCES (Regulatory Authority)

#### STATE STATUTES
1. [State Name] Medical Practice Act
   - Citation: [Full citation]
   - URL: [Link]
   - Sections Referenced: [List]
   - Last Accessed: [Date]

#### STATE ADMINISTRATIVE CODE
1. [State] Administrative Code - Medical Board Rules
   - Citation: [Full citation]
   - URL: [Link]
   - Last Accessed: [Date]

#### STATE BOARD OFFICIAL SOURCES
1. [State] Medical Board Website
   - URL: [Link]
   - Sections accessed: [List]
   - Last Accessed: [Date]

### SECONDARY SOURCES (Corroboration Only)
1. FSMB CME Comparison
2. [State] Medical Association

### SOURCE HIERARCHY (For Conflict Resolution)
1. STATE STATUTE (HIGHEST AUTHORITY)
2. STATE ADMINISTRATIVE CODE
3. STATE BOARD OFFICIAL REGULATIONS
4. STATE BOARD WEBSITE / GUIDANCE
5. BOARD PORTAL INSTRUCTIONS
6. SECONDARY SOURCES (LOWEST)
```

**Checklist:**
- [ ] "Sources Cited" section exists
- [ ] Primary sources listed (statute, admin code, board)
- [ ] Each source includes citation, URL, and last accessed date
- [ ] Source hierarchy documented
- [ ] Conflicts documented (if any)

**Scoring:**
- Complete sources section with hierarchy: **5 points**
- Sources listed but missing some URLs/dates: **3 points**
- Minimal sources section: **1 point**
- No sources section: **0 points**

**Remediation:**
Create full Sources Cited section using v3.0 template (lines 758-837 of prompt).

---

### 5.3 Primary Sources with URLs (3 points)

**Verify:**
- [ ] Primary statute URL included and accessible
- [ ] Administrative code URL included
- [ ] Board website URL included
- [ ] All URLs tested and working (as of last verified date)

**Scoring:**
- All primary source URLs present and formatted correctly: **3 points**
- Most URLs present (2/3): **2 points**
- Some URLs (1/3): **1 point**
- No URLs: **0 points**

**Remediation:**
Add missing URLs. Verify links are to official state sources.

---

### 5.4 Source Conflict Resolution (2 points)

**If sources disagree, check for documentation:**
```
**Conflicts Documented in This Research:**

| Requirement | Source 1 | Source 2 | Resolution | Authority |
|-------------|----------|----------|------------|-----------|
| CME Hours | 40 (statute) | 50 (board website) | 40 hours | STATUTE > BOARD |
```

**Scoring:**
- Conflicts documented with resolution: **2 points**
- N/A (no conflicts found): **2 points** (auto-award)
- Conflicts exist but not documented: **0 points**

**Remediation:**
If conflicting information found, create conflicts table and resolve per hierarchy.

---

**SOURCE VALIDATION SCORE: ____ / 15**

---

## PHASE 6: RESEARCH GAP DOCUMENTATION (10 points)

### 6.1 Critical Gaps Identified (3 points)

**Check "Research Gaps & Limitations" section for:**
```
## CRITICAL GAPS (Block Rules Engine Deployment)

- [ ] **GAP ID:** [STATE]-[TOPIC]-001
  **Description:** [What we don't know]
  **Impact:** [Why this matters]
  **What We Know:** [Related facts]
  **Attempted Sources:** [List with URLs]
  **Verification Method:** [How to resolve]
  **Priority:** CRITICAL
```

**Scoring:**
- Critical gaps documented with full structure: **3 points**
- Critical gaps listed but incomplete: **2 points**
- Some gaps mentioned but not structured: **1 point**
- No gap documentation: **0 points**

**Remediation:**
Add "Research Gaps & Limitations" section. Document all unknowns with GAP ID, description, impact, and verification method.

---

### 6.2 Gap Search Attempts Documented (3 points)

**For each gap, verify "Attempted Sources" section:**
```
Attempted Sources:
- [Statute URL] - Searched for "[keywords]" - NOT FOUND
- [Admin Code URL] - Checked Chapters X-Y - NOT FOUND
- [Board website] - Reviewed FAQs, renewal section - NOT FOUND
- Board contact attempted: [phone/email] - [Result]
```

**Scoring:**
- All gaps document search attempts (3+ sources per gap): **3 points**
- Most gaps document attempts: **2 points**
- Some gaps document attempts: **1 point**
- No search documentation: **0 points**

**Remediation:**
For each gap, add "Attempted Sources:" with at least 3 specific searches and results.

---

### 6.3 Verification Methods Specified (2 points)

**For each gap, check "Verification Method" or "Next Steps":**
```
Verification Method:
1. Contact [STATE] Board at [phone/email]
2. FOIA request for board meeting minutes
3. Search [specific statute sections]
```

**Scoring:**
- All gaps include verification methods: **2 points**
- Most gaps include methods: **1 point**
- No verification methods: **0 points**

**Remediation:**
Add specific, actionable verification steps for each gap.

---

### 6.4 Gap Priority Levels Assigned (2 points)

**Check that gaps are categorized:**
- CRITICAL GAPS (block rules engine)
- HIGH GAPS (affect compliance validation)
- MEDIUM GAPS (affect edge cases)
- LOW GAPS (nice-to-have context)

**Scoring:**
- All gaps assigned priority levels: **2 points**
- Some gaps assigned priorities: **1 point**
- No priority levels: **0 points**

**Remediation:**
Assign priority to each gap based on rules engine impact.

---

**RESEARCH GAP DOCUMENTATION SCORE: ____ / 10**

---

## PHASE 7: SPLIT-BOARD COMPLIANCE (5 points, if applicable)

### 7.1 Comparison Table (3 points) - TIER-2 States Only

**Required for TIER-2 Split-Board States:**
```
## Comparison: MD vs DO

| Factor | MD Board | DO Board |
|--------|----------|----------|
| Board Name | [Name] | [Name] |
| Governing Statute | [Citation] | [Citation] |
| Total CME Hours | [X hrs/Y yrs] | [X hrs/Y yrs] |
| Renewal Frequency | [Cycle] | [Cycle] |
| Mandatory Topics | [List] | [List] |
| CME Tracking System | [System] | [System] |
| Renewal Fee | $[X] | $[X] |

**Key Differences:**
- [Difference 1 with citation]
- [Difference 2 with citation]
```

**Scoring (TIER-2 only):**
- Comprehensive comparison table: **3 points**
- Partial comparison: **2 points**
- Comparison mentioned but not detailed: **1 point**
- No comparison: **0 points**

**Scoring (TIER-1 unified states):**
- Auto-award **3 points** (N/A)

**Remediation:**
If TIER-2 split-board state, create full MD vs DO comparison table.

---

### 7.2 Separate Deliverable for Each License Type (2 points)

**Check:**
- [ ] Document covers ONLY one license type (MD or DO, not both)
- [ ] Frontmatter clearly specifies `license_type: "MD"` or `license_type: "DO"`
- [ ] Scope statement notes separate deliverable for other license type

**Scoring:**
- Single license type, properly scoped: **2 points**
- Mixed license types (both MD and DO in one doc): **0 points**

**Remediation:**
If document mixes MD and DO, split into two separate documents.

---

**SPLIT-BOARD COMPLIANCE SCORE: ____ / 5**

---

## FINAL AUDIT SCORE CALCULATION

| Component | Points Earned | Points Possible |
|-----------|---------------|-----------------|
| 1. Frontmatter Structure | ____ | 25 |
| 2. Section Completeness | ____ | 20 |
| 3. Evidence Classification | ____ | 25 |
| 4. Source Validation | ____ | 15 |
| 5. Research Gap Documentation | ____ | 10 |
| 6. Split-Board Compliance | ____ | 5 |
| **TOTAL SCORE** | **____** | **100** |

---

## AUDIT SCORE INTERPRETATION

**90-100: EXCELLENT** - Fully v3.0 compliant
- Document meets or exceeds all v3.0 requirements
- Evidence classification system applied consistently
- All sources cited with URLs and quotes
- Research gaps fully documented
- Ready for production use

**85-89: GOOD** - Meets 85% standard, minor gaps
- Document substantially meets v3.0 requirements
- Minor missing elements (e.g., some URLs, some quotes)
- Frontmatter mostly complete
- Suitable for use with minor updates

**70-84: FAIR** - Substantial work needed for v3.0 compliance
- Document has good content but missing v3.0 structure
- Frontmatter incomplete (missing SOC2/ISO sections)
- Evidence tags inconsistent or sparse
- Sources cited but not fully formatted
- Needs significant remediation before v3.0 compliance

**50-69: POOR** - Major restructuring required
- Document lacks v3.0 structure
- Evidence classification system not applied
- Sources not properly cited
- Major sections missing
- Requires substantial rework

**0-49: CRITICAL** - Does not meet basic v3.0 requirements
- Document fundamentally incompatible with v3.0 standard
- Missing most required sections
- No evidence classification
- No source citations
- Complete rewrite recommended

---

## DETAILED REMEDIATION GUIDANCE

### For Documents Scoring 70-84 (FAIR)

**Priority 1 - Frontmatter Updates (15 mins per document):**
1. Add missing governance section:
   ```yaml
   governance:
     framework: "State Medical Board Regulatory Framework"
     authority_level: "STATE"
     primary_statute: "[Extract from document body]"
     administrative_code: "[Extract from document body]"
   ```

2. Add SOC2 compliance section (copy from v3.0 template lines 107-113)

3. Add ISO standards section (copy from v3.0 template lines 114-120)

4. Add research_quality metrics:
   ```yaml
   research_quality:
     completeness_percentage: [Current claimed %]
     validation_level: "COMPREHENSIVE"
     source_count_minimum: "2 per requirement"
     source_hierarchy_applied: true
     cross_source_congruency_tracked: true
   ```

5. Add scope statement (copy from v3.0 template lines 131-149)

6. Add gap arrays (populate from [CRITICAL GAP] tags in body)

**Priority 2 - Evidence Tags (30 mins per document):**
1. Search for factual statements (CME hours, renewal dates, fees, topics)
2. Add `[FACT - SOURCE]` prefix to each
3. Add citation, URL, and quote after each fact
4. Example transformation:
   ```
   BEFORE:
   Alabama requires 25 hours of CME per year.

   AFTER:
   [FACT - STATUTE] Alabama requires 25 hours of AMA PRA Category 1 CME per calendar year.

   Citation: Ala. Code § 34-24-75
   Source: https://legislature.alabama.gov/
   Quote: "Each physician shall complete a minimum of twenty-five (25) AMA PRA
   Category I Credits™ or equivalent in each calendar year."
   Last Verified: 2026-01-02
   ```

**Priority 3 - Section Additions (45 mins per document):**
1. Add any missing v3.0 sections (check Phase 3.1 checklist)
2. Reorganize sections into v3.0 order
3. Add "Sources Cited" section with full hierarchy
4. Add "Research Gaps & Limitations" section with structured gaps

**Expected Time:** 90 mins per document to move from FAIR (70-84) to GOOD (85-89)

---

### For Documents Scoring 85-89 (GOOD)

**Quick Fixes (30 mins per document):**
1. Add missing URLs to existing citations
2. Add verbatim quotes to [FACT - STATUTE] tags
3. Complete frontmatter (add any missing SOC2/ISO/scope fields)
4. Add confidence levels to [INFERENCE] tags
5. Add "Attempted Sources" to [CRITICAL GAP] tags

**Expected Time:** 30 mins per document to move from GOOD (85-89) to EXCELLENT (90+)

---

### For Documents Scoring 50-69 (POOR)

**Major Rework Required (3-4 hours per document):**
1. Extract all factual content from existing document
2. Create new document from v3.0 template
3. Populate frontmatter completely
4. Add all 15 required sections in order
5. Apply [FACT], [INFERENCE], [CRITICAL GAP] tags throughout
6. Add full citations with URLs and quotes
7. Create Sources Cited section
8. Document all gaps with structured format

**Recommendation:** Consider starting fresh with v3.0 research prompt rather than remediating.

---

### For Documents Scoring 0-49 (CRITICAL)

**Recommendation:** Complete rewrite using v3.0 research prompt.

Existing document can be used as reference for content, but structure is incompatible with v3.0 requirements.

---

## COMMON ISSUES & FIXES

### Issue: Missing Frontmatter Fields

**Quick Fix:**
Copy entire frontmatter template from v3.0 prompt (lines 83-179) and populate with state-specific data.

---

### Issue: No Evidence Classification Tags

**Quick Fix:**
1. Use find/replace to add [FACT - BOARD] before board website citations
2. Use find/replace to add [FACT - STATUTE] before statute citations
3. Add [INFERENCE - HIGH CONFIDENCE] to inferred conclusions
4. Add [CRITICAL GAP] to documented unknowns

---

### Issue: Sources Not Cited with URLs

**Quick Fix:**
Create "Sources Cited" section and list:
- Primary statute with URL to official state code
- Administrative code with URL
- State board website
- Any secondary sources used

Then add inline citations referencing these sources.

---

### Issue: Missing Required Sections

**Quick Fix:**
For each missing section, copy template from v3.0 prompt:
- Executive Summary (lines 185-203)
- Board Information (lines 205-234)
- Lifecycle Phases (lines 236-287)
- CME Requirements (lines 289-323)
- CME Topics (lines 325-375)
- Controlled Substance (lines 377-427)
- Audit Procedures (lines 429-459)
- Exemptions (lines 461-504)
- Fees & Timeline (lines 506-551)
- Reinstatement (lines 553-610)
- CME Tracking (lines 612-653)
- State-Specific (lines 655-694)
- Gaps & Limitations (lines 696-753)
- Sources Cited (lines 755-837)
- Appendix (lines 839-876)

---

### Issue: Completion % Seems Inflated

**Recalibrate:**
Actual completion % should reflect:
- Frontmatter completeness (25% weight)
- Section presence (20% weight)
- Evidence quality (25% weight)
- Source documentation (15% weight)
- Gap documentation (10% weight)
- Split-board compliance (5% weight)

Formula: `Audit Score = Realistic Completion %`

If document claims 95% but scores 72%, update frontmatter:
```yaml
completion_percentage: 72
validation_level: "PARTIAL"
```

---

## GOLD STANDARD REFERENCE

**Oklahoma MD Document** ([OKLAHOMA_FINDINGS.md](OKLAHOMA_FINDINGS.md)):
- 344KB comprehensive
- Full frontmatter with all v3.0 fields
- Extensive [FACT] tags with citations, URLs, quotes
- Cross-source congruency tracked
- Complete gap documentation
- **Use as reference for excellent v3.0 compliance**

**Alabama MD Document** (AL-MD-Renewal-Requirements-Narrative-2026-01-02.md):
- 634 lines, 93 citations
- 95% completion claimed
- Strong evidence classification
- Well-structured frontmatter
- **Use as reference for GOOD-level compliance**

---

## AUDIT WORKFLOW CHECKLIST

- [ ] Phase 1: Extract document metadata
- [ ] Phase 2: Score frontmatter (25 pts)
- [ ] Phase 3: Score section completeness (20 pts)
- [ ] Phase 4: Score evidence classification (25 pts)
- [ ] Phase 5: Score source validation (15 pts)
- [ ] Phase 6: Score gap documentation (10 pts)
- [ ] Phase 7: Score split-board compliance (5 pts)
- [ ] Calculate total score (0-100)
- [ ] Assign compliance level (EXCELLENT/GOOD/FAIR/POOR/CRITICAL)
- [ ] Generate remediation guidance
- [ ] Populate CSV tracker row
- [ ] Document key findings

---

**END OF AUDIT PROMPT**

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-03 | Initial comprehensive audit prompt created. Scoring rubric aligned with v3.0 requirements (25+20+25+15+10+5 = 100 pts). Detailed remediation guidance added. Common issues reference included. |
