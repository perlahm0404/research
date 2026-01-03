# State License Renewal Requirements Research Prompt - v3.0

**Version:** 3.0.0
**Created:** 2026-01-02
**Purpose:** Comprehensive renewal requirements research across MD, DO, and NP license types with regulatory validation
**Output Format:** Narrative markdown with regulatory citations
**Scope:** Renewal requirements ONLY (not initial licensing, unless directly affects renewal)
**Gold Standard Reference:** [OKLAHOMA_FINDINGS.md](OKLAHOMA_FINDINGS.md) (344KB comprehensive)

---

## CRITICAL REQUIREMENTS - READ FIRST

### Separate License Type Research

**You will research ONE license type per research session:**

- **MD** (Medical Doctors/Allopathic Physicians)
- **DO** (Doctors of Osteopathic Medicine)
- **NP** (Nurse Practitioners)

**EACH license type gets its OWN separate deliverable document.** Do NOT mix requirements from different license types in the same document.

### Split-Board State Protocol

Some states have **separate regulatory boards** for different license types with **DIFFERENT CME requirements.**

#### Split-Board Examples:
- **MD + DO Split:** AZ, CA, FL, ME, MI, NV, **OK**, PA, TN, VT, WA, WV
- **NP + RN Split:** Most states (NPs regulated by Board of Nursing, separate from medical boards)

#### Research Protocol:
1. **Identify all boards** that regulate the target license type
2. **Determine if split boards exist** (separate MD board vs DO board, or unified)
3. **Research ONLY the relevant board** for the license type specified
4. **Create comparison table** (if applicable) showing MD vs DO vs NP differences
5. **Produce separate deliverables** for each license type/board combination

#### Deliverable Naming:
- `[STATE]-MD-Renewal-Requirements-Narrative-YYYY-MM-DD.md`
- `[STATE]-DO-Renewal-Requirements-Narrative-YYYY-MM-DD.md`
- `[STATE]-NP-Renewal-Requirements-Narrative-YYYY-MM-DD.md`

**Example: Oklahoma (Split-Board State)**

| Factor | MD Board (OBMLS) | DO Board (OSBOE) | NP (Board of Nursing) |
|--------|-----------------|------------------|-----------------------|
| Governing Statute | 59 O.S. § 480-518.1 | 62 O.S. § 620-642 | 59 O.S. § 567 |
| Total CME | 60 Category 1 hrs/3 yrs | 1h prescribing/yr + [TBD] | [Research needed] |
| Renewal Cycle | Triennial (3 years) | [TBD] | [Research needed] |
| Portal | pay.apps.ok.gov/medlic/md/ | ok.gov/osboe/ | ok.gov/nursing |
| CME Tracking | CE Broker | CE Broker | [System TBD] |

---

## DELIVERABLE STRUCTURE

### File Format: Markdown Narrative (.md)

**NOT** YAML, Excel, or structured data. **Narrative markdown** with embedded regulatory citations and validation markers.

### Document Sections (Required Order)

1. **Frontmatter (YAML Header)**
2. **Executive Summary**
3. **Board Information & Authority**
4. **Lifecycle Phases & Grace Periods**
5. **CME Requirements - Total Hours & Categories**
6. **CME Topic Requirements**
7. **Controlled Substance Context** (MD/DO only)
8. **Audit & Verification Procedures**
9. **Exemptions & Alternatives**
10. **Renewal Fees & Timeline**
11. **Lapsed License Reinstatement**
12. **CME Tracking Systems**
13. **State-Specific Requirements** (Medical marijuana, jurisprudence, etc.)
14. **Research Gaps & Limitations**
15. **Sources Cited**
16. **Appendix: Uncovered Topics** (optional, for items found but out-of-scope)

---

## FRONTMATTER SPECIFICATION (YAML Header)

```yaml
---
# ===== DOCUMENT METADATA =====
document_type: "License Renewal Requirements - Narrative Research"
state: "[STATE ABBREVIATION]" # e.g., OK, CA, PA
license_type: "[MD|DO|NP]" # One license type only
board_name: "[Full official board name]"
board_abbreviation: "[e.g., OBMLS, OSBOE, OK Board of Nursing]"
board_code: "[State-specific code, e.g., OK-M, OK-DO, OK-NP]"
board_website: "[URL]"
renewal_portal: "[URL if available]"
research_date: "[YYYY-MM-DD]"
last_verified: "[YYYY-MM-DD]"
researcher: "[Name or 'Claude AI']"

# ===== GOVERNANCE & COMPLIANCE =====
governance:
  framework: "State Medical/Nursing Board Regulatory Framework"
  authority_level: "STATE"
  primary_statute: "[Citation, e.g., 59 O.S. § 480-518.1]"
  administrative_code: "[Citation, e.g., 435 OAC]"

soc2_compliance:
  scope: "Renewal requirements research document"
  data_classification: "Public (regulatory information)"
  version_control: "Git-tracked markdown"
  change_management: "Updated by [METHOD] when regulations change"
  audit_trail: "Research methodology documented in Section: Validation Standards"

iso_standards:
  applicable_standards:
    - "ISO 9001:2015 (Quality management - documentation & records)"
    - "ISO 27001:2022 (Information security - regulatory data handling)"
  documentation_standard: "ISO/IEC/IEEE 42010 (Architecture description)"
  approval_status: "[DRAFT|APPROVED|IN REVIEW]"

# ===== RESEARCH QUALITY METRICS =====
research_quality:
  completeness_percentage: [0-100] # e.g., 75
  validation_level: "[COMPREHENSIVE|PARTIAL|PRELIMINARY]"
  source_count_minimum: "2 per requirement"
  source_hierarchy_applied: true
  cross_source_congruency_tracked: true
  gap_documentation_standard: "CRITICAL|HIGH|MEDIUM|LOW"

# ===== SCOPE STATEMENT =====
scope:
  included:
    - "License renewal frequency and deadlines"
    - "CME requirements (hours, categories, topics)"
    - "Renewal fees and late penalties"
    - "First renewal grace periods (affects renewal timeline)"
    - "Residency/fellowship CME credit (affects renewal calculation)"
    - "CME audit and verification procedures"
    - "Lapsed license reinstatement CME requirements"
    - "Exemptions and alternatives to CME"
    - "Controlled substance prescribing context (MD/DO only)"
    - "All state-specific requirements discovered during research"
  excluded:
    - "Initial licensing exam requirements (USMLE, COMLEX, NBME, FLEX)"
    - "Medical school accreditation standards (LCME, ECFMG)"
    - "Postgraduate training years required for initial licensure"
    - "Background check procedures for new applicants"
    - "Citizenship/visa status requirements for initial application"

# ===== RESEARCH GAPS SUMMARY =====
critical_gaps:
  - gap: "[Description]"
    priority: "CRITICAL"
    impact: "[Blocks rules engine deployment if not resolved]"

high_gaps:
  - gap: "[Description]"
    priority: "HIGH"
    impact: "[Affects compliance validation]"

medium_gaps:
  - gap: "[Description]"
    priority: "MEDIUM"
    impact: "[Affects edge cases]"

# ===== CROSS-BOARD COMPARISON (if applicable) =====
comparison_required: [true|false]
comparison_with_boards:
  - "[Board name and type if comparing MD vs DO or NP]"

# ===== VERSION HISTORY =====
version: "3.0.0"
version_history:
  - version: "3.0.0"
    date: "2026-01-02"
    changes: "Restructured as narrative with regulatory validation markers"

---
```

---

## NARRATIVE CONTENT STRUCTURE

### 1. EXECUTIVE SUMMARY

**Format:** 3-5 bullet points

- **Key Finding 1:** [Main renewal requirement with confidence level]
- **Key Finding 2:** [Secondary finding]
- **Unique Features:** [State-specific requirements not found in other states]
- **Critical Gaps:** [Major unknowns that block full understanding]
- **Validation Status:** [Percentage complete, which areas validated vs. preliminary]

**Example:**
```
- **Total CME Requirement:** 60 hours of Category 1 CME every 3 years
  [FACT - STATUTE: 59 O.S. § 495a.1] [FACT - BOARD: okmedicalboard.org]
- **Grace Period:** 3 years from initial licensure [FACT - STATUTE]
- **Unique Feature:** Separate MD and DO boards with drastically different requirements
- **Critical Gap:** DO board total CME hours unknown [HIGH PRIORITY for research]
- **Validation:** MD requirements ~85% complete; DO requirements ~15% complete
```

---

### 2. BOARD INFORMATION & AUTHORITY

**Narrative format describing:**
- Official board name and jurisdiction
- Primary governing statute with full citation and URL
- Administrative code authority with citations
- Board website and portal URLs
- Current licensed population (if available)
- Board structure and composition (if relevant to renewal)

**Format:**
```
The [STATE] State Board of [LICENSE TYPE] is the official regulatory body
governing [LICENSE TYPE] licensure and renewal in [STATE]. The board operates
under the authority of:

[STATUTE] [Full statute citation and title]
Source: [URL to statute]
Governing scope: [What the statute covers regarding renewal]

[ADMIN_CODE] [Full administrative code citation]
Source: [URL to admin code]
Regulatory detail: [What the admin code specifies]

Official website: [URL]
Online renewal portal: [URL]
Current licensees: [Number, if available, with source]
```

---

### 3. LIFECYCLE PHASES & GRACE PERIODS

Research and document THREE distinct phases:

#### Phase 1: First Renewal Cycle (Newly Licensed Physicians/Practitioners)

**Research questions:**
- Is there a grace period before CME requirements begin?
- When does CME tracking start relative to initial license date?
- Are first-time renewal requirements different from ongoing requirements?

**Format with validation markers:**

```
**Grace Period for Newly Licensed [LICENSE TYPE]**

[FACT - STATUTE] Newly licensed [LICENSE TYPE] physicians have a [X]-year grace period
from the date of initial licensure before CME requirements begin.

Citation: [Full statute citation]
Source URL: [Link to statute]
Quote: "[Exact text from statute]"
Last Verified: [YYYY-MM-DD]

Interpretation: [Explain what this means for renewal timeline]

[INFERENCE - HIGH CONFIDENCE] This grace period means a physician licensed in Year 1
will begin reporting CME in Year [X] at their first renewal cycle.

Supporting facts:
- [FACT] CME required every [X] years per [citation]
- [FACT] Newly licensed physicians begin reporting [X] years from license date per [citation]

Verification needed: Contact board at [phone/email] to confirm interpretation
```

#### Phase 2: First Renewal After Grace Period Expires

**Extract:**
- Are CME requirements reduced for first renewal?
- Are all mandatory topics required?
- Is CME calculated pro-rata or full requirement?

#### Phase 3: Ongoing Renewals (Steady-State)

**Extract:**
- Standard CME hours per cycle
- Renewal frequency
- All recurring requirements

---

### 4. CME REQUIREMENTS - TOTAL HOURS & CATEGORIES

**Format:**

```
**Total CME Hour Requirement**

[FACT - STATUTE] [STATE] requires [X] hours of [CATEGORY] CME within every
[Y]-year renewal cycle.

Citation: [Full statute/admin code citation]
Source: [URL]
Last Verified: [Date]
Quote: "[Exact regulatory language]"

Cross-Source Validation:
- [FACT - STATUTE]: [X] hours [CONGRUENCY: 1/3 sources]
- [FACT - BOARD_WEBSITE]: [X] hours [CONGRUENCY: 3/3 sources]
- [INFERENCE]: Renewal cycle is [Y] years based on 3-year CME requirement [CONFIDENCE: HIGH]

**Category Requirements**

[FACT - STATUTE] All [X] hours must be [CATEGORY TYPE, e.g., "AMA Category 1" or "AOA Category 1-A"]

OR

[FACT - STATUTE] CME requirements include:
- Minimum [X] hours of Category 1
- Up to [Y] hours of Category 2 allowed
- Other categories: [Details]

Sources: [Citations]
```

---

### 5. CME TOPIC REQUIREMENTS

**For EACH mandatory topic found, document:**

```
**[TOPIC NAME]**

Requirement Status: [FACT|INFERENCE|NOT FOUND]

[FACT - STATUTE] [STATE] requires [X] hours of [TOPIC] CME for [LICENSE TYPE].

Statute Citation: [Full citation, e.g., "59 O.S. § 495a.1"]
Source URL: [Link to statute database]
Verbatim Quote: "[Exact text from statute]"

Frequency:
- [FACT - STATUTE] Required [ANNUAL|PER CYCLE|ONE-TIME|OTHER]
- Applies to: [All licensees|DEA holders only|Condition-specific]

Lifecycle Phase:
- [FACT - STATUTE] Applies to [first renewal only|ongoing|both]

Topic Details:
- Required hours: [X]
- Acceptable accreditors: [e.g., AMA, state board-approved]
- Can be waived/exempted: [Yes/No/Conditional]

Cross-Source Validation:
- STATE_STATUTE agrees: ✅
- STATE_BOARD agrees: ✅
- ADMIN_CODE agrees: ✅
- FSMB data: [Match|Conflict|Not mentioned]

Evidence Classification: [FACT] (stated directly in statute)
OR [INFERENCE - CONFIDENCE] (derived from regulatory context)
```

**Common Topics to Research:**
- Pain Management / Opioid Prescribing Education
- Healthcare Provider Rights & Responsibilities
- Medical Marijuana / Cannabis Education
- Ethics / Professionalism
- Cultural Competency / Implicit Bias
- Human Trafficking Awareness
- Child Abuse Recognition & Reporting
- Domestic Violence
- PDMP (Prescription Drug Monitoring Program) Training
- Jurisprudence Examination
- Any other state-specific mandates discovered

---

### 6. CONTROLLED SUBSTANCE CONTEXT (MD/DO Only)

**Format:**

```
**Opioid Prescribing Limits**

[FACT - STATUTE] Acute pain opioid prescribing is limited to a [X]-day supply.

Citation: [Statute/Admin Code]
Source: [URL]
Quote: "[Exact language]"

Exemptions: [Cancer pain|Palliative care|Postoperative|None]

[FACT - STATUTE] Chronic pain management requires:
1. [FACT] Documentation requirement 1
2. [FACT] Documentation requirement 2
3. [FACT] Patient-provider agreement: [Required|Recommended|Not specified]
4. [FACT] Urine screening: [Required for high-risk|Recommended|Not specified]

Cross-Source Validation:
- [FACT - STATUTE]: [Details] [CONGRUENCY: 3/3 sources]
- [FACT - ADMIN_CODE]: [Details]
- [FACT - BOARD]: [Details]
```

**Telemedicine Restrictions:**

```
[FACT - STATUTE] Telemedicine opioid prescribing is [PROHIBITED|ALLOWED|CONDITIONAL]

Citation: [OAC 435:10-7-13 or similar]
Source: [URL]
Quote: "[Exact restrictive language]"

Exceptions: [Opioid antagonists only|None|Other]
```

**Prescription Monitoring Program (PMP):**

```
[FACT - STATUTE] PMP usage is [MANDATORY|RECOMMENDED|OPTIONAL]

Citation: [Statute]
Source: [URL]
PMP System: [Oklahoma Prescription Monitoring Program or equivalent]
Portal: [URL if available]
```

---

### 7. AUDIT & VERIFICATION PROCEDURES

**Format:**

```
**CME Verification at Renewal**

[FACT - BOARD] Licensees must verify CME completion by [ATTESTATION|CERTIFICATE UPLOAD|AUTOMATIC|OTHER]

Evidence: [Source URL or citation]
Process: [Describe the actual verification workflow]

**Audit Process**

[FACT - STATUTE] The board conducts [RANDOM AUDITS|FOR-CAUSE AUDITS|BOTH|UNIVERSAL AUDIT]

Citation: [Statute/Admin Code]
Source: [URL]

Audit Details:
- [FACT - ADMIN_CODE] Audit type: [Random percentage X% per year|For-cause|Both]
- [FACT - ADMIN_CODE] Audit response timeline: [X days to submit documentation]
- [FACT - ADMIN_CODE] Required documentation: [List: certificates, transcripts, other]
- [FACT - STATUTE|CRITICAL GAP] CME record retention: [X years|Current cycle + X years|Unknown]

Penalties for Non-Compliance:
- [FACT - STATUTE] Failure to respond to audit: [Fine|Suspension|Hearing required|Other]
- [FACT - STATUTE] CME shortfall found: [Remediation required|Fine|Suspension|Other]
- [FACT - STATUTE] False attestation: [Disciplinary action|License revocation|Other]
```

---

### 8. EXEMPTIONS & ALTERNATIVES

**Format:**

```
**Board Certification as CME Alternative**

[FACT - STATUTE] ABMS board certification obtained during the renewal cycle
[SATISFIES FULL CME REQUIREMENT|PROVIDES PARTIAL CREDIT|NOT ACCEPTED]

Citation: [Statute/Admin Code]
Source: [URL]
Quote: "[Exact language]"

Details:
- [FACT] Accepted specialty boards: [ABMS|AOA|Both|Other]
- [FACT] Credit awarded: [Entire CME requirement OR X hours]
- [FACT] Timing: [Must be obtained during current cycle|Ongoing certification status accepted|Other]
- [FACT] Topic exemptions: [Full exemption OR topic requirements still apply to non-certified areas]

**Residency / Fellowship Credit**

[FACT - STATUTE] Physicians in active residency or fellowship training
[ARE EXEMPT FROM CME|RECEIVE CME CREDIT of X hours per year|OTHER]

Citation: [Statute]
Source: [URL]
Quote: "[Exact language]"

Details:
- [FACT] Credit per year: [X hours]
- [FACT] Maximum credit per cycle: [Y hours]
- [FACT] Documentation required: [Program verification letter|Completion certificate|Other]

**Military Service / Hardship**

[FACT - STATUTE|CRITICAL GAP] Military service exemption: [FOUND|NOT FOUND]
Hardship exemption: [FOUND|NOT FOUND]

If found, document citation and requirements.
```

---

### 9. RENEWAL FEES & TIMELINE

**Format:**

```
**Renewal Fees**

[FACT - BOARD] Standard renewal fee: $[X]

Source: [URL, date published]
Last Updated: [YYYY-MM-DD]

[FACT - STATUTE] Late renewal fee: $[X]

Citation: [Statute]
Source: [URL]

Grace period for late payment: [X days after expiration]
License status during grace period: [Active|Inactive|Suspended]

[FACT - STATUTE] Reinstatement fee (if license lapses > X days): $[Y]

Citation: [Statute]
Source: [URL]

**Renewal Timeline**

[FACT - BOARD] Renewal notice is mailed [X] days before expiration.

Source: [Board website, date]
Renewal portal opens: [X] days before expiration
Renewal deadline: [Specific date relative to license expiration]
License status after deadline: [Inactive|Suspended]
Can practice if late: [Yes|No]

**Late Renewal Deadline**

[FACT - STATUTE] Licensees have [X] days after expiration to renew with late fee

Citation: [Statute]
Source: [URL]

After [X] days, license status becomes: [Suspended|Expired|Other]
Reinstatement process required: [Yes|No]
```

---

### 10. LAPSED LICENSE REINSTATEMENT

**Format (3-Tier Framework):**

```
**Reinstatement When License Lapses**

Oklahoma uses a three-tier system based on lapse duration:

**TIER 1: Lapsed < 1 Year**

[FACT - STATUTE] Reinstatement type: [AUTOMATIC RENEWAL|SIMPLE REINSTATEMENT]

Citation: [OAC 435:5-1-6 or similar]
Source: [URL]
Quote: "[Exact language describing process]"

Requirements:
- [FACT] CME requirement: [Current cycle CME required|No additional CME needed|Other]
- [FACT] Background check: [Required|Not required|Board discretion]
- [FACT] Re-examination: [Required|Not required|Board discretion]
- [FACT] Fees: $[X]
- [FACT] Timeline: [X-Y] weeks typical

**TIER 2: Lapsed 1-3 Years**

[FACT - STATUTE] Reinstatement type: [FORMAL REINSTATEMENT|BOARD DISCRETION REQUIRED]

Citation: [Statute]
Source: [URL]

Requirements:
- [FACT] CME makeup requirement: [Make up CME for lapsed period|Current cycle only|Full requirement]
- [FACT] Background check: [Required|May be required at board discretion|Not required]
- [FACT] Re-examination: [Required|May be required at board discretion|Not required]
- [FACT] Application type: [Written application form required|Board review required]
- [FACT] Fees: $[X]
- [FACT] Timeline: [X-Y] weeks typical

**TIER 3: Lapsed > 3 Years**

[FACT - STATUTE] Reinstatement type: [NEW APPLICATION|FULL REAPPLICATION]

Citation: [Statute]
Source: [URL]
Quote: "[Exact language]"

Requirements:
- [FACT] Treated as: [New initial applicant|Special lapsed applicant]
- [FACT] CME makeup: [Full requirements|Makeup for lapsed period|Other]
- [FACT] Background check: [Required|Not required]
- [FACT] Re-examination: [Required|Not required]
- [FACT] All initial licensure requirements: [Must be met again|Waived|Conditional]
- [FACT] Fees: $[X]
- [FACT] Timeline: [X-Y] weeks typical
```

---

### 11. CME TRACKING SYSTEMS

**Format:**

```
**Official CME Tracking System**

[FACT - BOARD] The [STATE] [BOARD NAME] uses [CE BROKER|BOARD-OPERATED|OTHER SYSTEM]
for CME tracking and reporting.

System Name: [Official name]
Vendor (if applicable): [Vendor name]
System URL: [https://...]
Licensee Portal: [https://...]
Last Verified: [YYYY-MM-DD]

**Integration Details**

[FACT - BOARD] CME providers [AUTO-REPORT|MUST BE MANUALLY ENTERED|MIXED] to the system

Source: [Board website or FAQ]
URL: [Link]

[FACT - BOARD] Physicians [CAN|CANNOT] access their CME transcript through the portal

Source: [Board website]
URL: [Link]

[FACT - BOARD] Renewal verification is handled [AUTOMATICALLY BY SYSTEM|REQUIRES MANUAL ATTESTATION|MIXED]

Source: [Board website or admin code]
URL: [Link]

**Reporting Method at Renewal**

[FACT - BOARD] Licensees must [ATTEST to CME completion|UPLOAD CERTIFICATES|PROVIDE CME TRANSCRIPT|OTHER]

Source: [Board portal instructions or renewal FAQ]
URL: [Link]
```

---

### 12. STATE-SPECIFIC REQUIREMENTS

**Research and document any unique requirements not typically found in other states:**

```
**Medical Marijuana / Cannabis Education**

[FACT - STATUTE|NOT FOUND] [STATE] requires CME on medical marijuana before recommending

Citation: [Statute if found]
Source: [URL]
Quote: "[Exact language]"

If found:
- [FACT] Hours required: [X hours]
- [FACT] Frequency: [One-time|Annual|Per cycle]
- [FACT] When required: [Before first recommendation|At renewal|Other]
- [FACT] Effective date: [YYYY-MM-DD]
- [FACT] Board-approved courses: [List or reference to list]

**Jurisprudence Examination**

[FACT - STATUTE|NOT FOUND] [STATE] requires a jurisprudence exam

Citation: [Statute]
Source: [URL]
Quote: "[Exact language]"

If found:
- [FACT] Frequency: [At renewal|Every X years|Initial licensure only]
- [FACT] Format: [Online|Open-book|Closed-book|Other]
- [FACT] Passing score: [X%]
- [FACT] CME credit: [Counts as X hours CME|No CME credit]

**[Any Other State-Specific Requirement Discovered]**

[Document similar format as above]
```

---

### 13. RESEARCH GAPS & LIMITATIONS

**Format:**

```
## CRITICAL GAPS (Block Rules Engine Deployment)

- [ ] **GAP ID:** [STATE]-[TOPIC]-001
  **Description:** [What we don't know]
  **Impact:** [Why this matters for rules engine]
  **What We Know:** [FACT statements related to the gap]
  **Attempted Sources:**
    - [Source 1 URL] - Searched for "[search terms]" - NOT FOUND
    - [Source 2 URL] - Checked [sections] - NOT FOUND
    - [Board contact attempted] - [Result]
  **Verification Method:** [How to resolve: contact board, FOIA, statute search, etc.]
  **Priority:** CRITICAL

## HIGH GAPS (Affects Compliance Validation)

- [ ] **GAP ID:** [STATE]-[TOPIC]-002
  **Description:** [Gap description]
  **Priority:** HIGH
  [Same format as CRITICAL]

## MEDIUM GAPS (Affects Edge Cases)

- [ ] **GAP ID:** [STATE]-[TOPIC]-003
  [Format as above]
  **Priority:** MEDIUM

## LOW GAPS (Nice-to-Have Context)

- [ ] **GAP ID:** [STATE]-[TOPIC]-004
  [Format as above]
  **Priority:** LOW

**Research Completion Summary:**

| Section | Status | Completeness | Notes |
|---------|--------|--------------|-------|
| Lifecycle Phases | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |
| CME Total Hours | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |
| CME Topics | [COMPLETE|PARTIAL|MISSING] | [%] | [Topics confirmed, Topics unknown] |
| Audit Process | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |
| Exemptions | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |
| Fees & Timeline | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |
| Reinstatement | [COMPLETE|PARTIAL|MISSING] | [%] | [Details] |

**Overall Completion: [X]%**

**Next Steps to Complete Research:**
1. [Specific action, e.g., "Contact OSBOE at (405) 528-8625 to verify DO total CME hours"]
2. [Specific action, e.g., "Search 62 O.S. § 620-642 for statutory CME mandates"]
3. [Specific action, e.g., "Request FOIA for board meeting minutes on audit procedures"]
```

---

### 14. SOURCES CITED

**Format:**

```
## PRIMARY SOURCES (Regulatory Authority)

### STATE STATUTES

1. **[State Name] Medical Practice Act** (or equivalent for DO/NP)
   - Citation: [Full citation, e.g., "Oklahoma Statutes Title 59, Sections 480-518.1"]
   - URL: [Link to official statute database]
   - Scope: [What sections cover renewal, CME, etc.]
   - Last Accessed: [YYYY-MM-DD]
   - Sections Referenced: [List relevant sections, e.g., § 495a.1, § 481]

2. **[Additional statute if applicable]**

### STATE ADMINISTRATIVE CODE

1. **[State] Administrative Code - Medical Board Rules**
   - Citation: [Full citation, e.g., "Title 435 of the Oklahoma Administrative Code"]
   - Chapter/Title: [Specific chapters on renewal, CME]
   - URL: [Link if available]
   - Last Accessed: [YYYY-MM-DD]

### STATE BOARD OFFICIAL SOURCES

1. **[State] Medical Board Website - Renewal Section**
   - URL: [https://...]
   - Sections accessed: [Renewal, CME, FAQs, etc.]
   - Last Accessed: [YYYY-MM-DD]
   - Authority: Operational requirements

2. **[State] Medical Board - CME Guidelines Document**
   - URL: [https://...]
   - Format: [PDF, webpage, etc.]
   - Last Accessed: [YYYY-MM-DD]

3. **[State] Medical Board - Online Renewal Portal**
   - URL: [https://...]
   - Portal instructions reviewed: [Date]
   - Features verified: [What was tested/confirmed]

### CME TRACKING SYSTEMS

1. **CE Broker - [State] CME Tracking**
   - URL: [https://cebroker.com/[STATE]/...]
   - Integration: [Integration details]
   - Last Accessed: [YYYY-MM-DD]

### SECONDARY SOURCES (Corroboration Only)

1. **FSMB (Federation of State Medical Boards) CME Comparison**
   - Data checked against: [Oklahoma FSMB profile]
   - Discrepancies noted: [Yes/No - list if found]
   - Authority: Validation purposes only (NOT primary authority)

2. **[State Medical Association] Resources**
   - URL: [https://...]
   - Last Accessed: [YYYY-MM-DD]

## SOURCE HIERARCHY (For Conflict Resolution)

When sources disagree, apply this priority order:

1. **STATE STATUTE** (HIGHEST AUTHORITY) - Legislative mandate
2. **STATE ADMINISTRATIVE CODE** - Regulatory implementation
3. **STATE BOARD OFFICIAL REGULATIONS** - Board-adopted rules
4. **STATE BOARD WEBSITE / OFFICIAL GUIDANCE** - Operational procedures
5. **BOARD PORTAL INSTRUCTIONS** - User-facing documentation
6. **SECONDARY SOURCES** (LOWEST) - Corroboration only

**Conflicts Documented in This Research:**

If any sources contradicted each other, document:

| Requirement | Source 1 | Source 2 | Resolution | Authority |
|-------------|----------|----------|------------|-----------|
| [Requirement] | [Value A] | [Value B] | [Chose Value X] | [Per hierarchy: STATUTE beats BOARD] |
```

---

### 15. APPENDIX: UNCOVERED TOPICS (Optional)

**Document any topics researched but found to be out-of-scope or not applicable:**

```
## Topics Researched But Not Included (Out-of-Scope)

The following topics were researched to determine applicability but are documented here
as NOT INCLUDED in renewal requirements per scope limitations:

- **Initial Licensing Examinations** (USMLE, COMLEX, NBME, FLEX)
  - Status: Out-of-scope (covered in initial licensing rubric)
  - Finding: Not applicable to renewal

- **Medical School Accreditation Requirements** (LCME, ECFMG)
  - Status: Out-of-scope (applies only to initial licensure)
  - Finding: No renewal impact

- **[Other topic researched]**
  - Status: [Out-of-scope|Not applicable|Found but incomplete]
  - Brief findings: [1-2 sentence summary if relevant]

## Additional Information Discovered (For Future Consideration)

During research, the following information was discovered that may be relevant
for future CREDMATE enhancements but falls outside current scope:

- **[Topic found]:** [Brief description]
  - Relevance: [Why this matters]
  - Source: [Where found]
  - Recommendation: [Consider adding to v4.0 scope?]

- **[Another discovery]:** [Description]
  - Relevance: [Why this matters]
  - Source: [Where found]
```

---

## VALIDATION STANDARDS & NOTATION

### Evidence Classification System

Use **inline notation** to classify every factual statement:

**Format:**
```
[EVIDENCE TYPE] Statement

[FACT - SOURCE_TYPE] Description of fact
[INFERENCE - CONFIDENCE] Description of inference
[CRITICAL GAP] Description of unknown
```

### Evidence Types:

#### [FACT - STATUTE]
- Directly quoted from state statute
- Must include: citation, URL, exact quote
- Authority: HIGHEST

**Example:**
```
[FACT - STATUTE] Oklahoma requires 60 hours of Category 1 CME every 3 years.

Citation: 59 O.S. § 495a.1
Source: https://legislature.ok.gov/bills/
Quote: "Each physician shall complete a minimum of 60 hours of Category I continuing
medical education within every three-year period."
Last Verified: 2026-01-02
```

#### [FACT - ADMIN_CODE]
- Directly from state administrative code
- Must include: citation, URL, exact quote
- Authority: HIGH

#### [FACT - BOARD]
- Directly from official board website or portal documentation
- Must include: URL, date accessed, exact quote or clear reference
- Authority: MEDIUM-HIGH

**Example:**
```
[FACT - BOARD] Online renewal is available 60 days before license expiration.

Source: https://www.okmedicalboard.org/licensing_faq
Section: "Renewal Timeline"
Quote: "The online renewal system becomes available 60 days prior to your
license expiration date."
Last Accessed: 2026-01-02
```

#### [INFERENCE - CONFIDENCE]
- Derived from facts, not directly stated
- Must explain reasoning
- Must state confidence level: HIGH / MEDIUM / LOW
- Must specify what primary source would verify

**Example:**
```
[INFERENCE - HIGH CONFIDENCE] The license renewal cycle is triennial (every 3 years).

Reasoning: CME is required over a 3-year cycle per statute (59 O.S. § 495a.1).
Board website confirms renewal notices are sent 60 days before expiration.
If CME tracking is on a 3-year cycle and renewal is also on a 3-year cycle,
license expiration is triennial.

Supporting facts:
- [FACT - STATUTE] "CME required within every three-year period"
- [FACT - BOARD] "Renewal notices sent 60 days before expiration"

Verification method: Contact board at (405) 962-1400 to confirm license
validity period matches 3-year CME cycle

Confidence: HIGH (two independent sources corroborate)
```

#### [CRITICAL GAP]
- Extensively searched for but not found
- Must document search effort
- Must explain rules engine impact

**Example:**
```
[CRITICAL GAP] DO board total CME hour requirement unknown

What We Know:
- [FACT - BOARD] 1 hour of Approved Proper Prescribing Courses required annually
- [FACT - BOARD] CE Broker is the official tracking system
- [FACT - STATUTE] 62 O.S. § 620-642 governs osteopathic physician licensing

What We Don't Know:
- Total CME hours per renewal cycle (beyond prescribing requirement)
- Renewal frequency (annual? biennial? triennial?)
- Category requirements (AOA Category 1-A or other?)
- Topic-specific mandates beyond prescribing

Attempted Sources:
- 62 O.S. § 620-642 (Full statute) - Searched for "continuing education" -
  Found only prescribing requirement
- OK Administrative Code (Title TBD) - Could not locate specific title
- OSBOE website (https://www.ok.gov/osboe/) - FAQ doesn't detail total hours
- OSBOE board meeting minutes - Not publicly available online

Verification Methods (in priority order):
1. Contact OSBOE directly at (405) 528-8625
2. FOIA request for board meeting minutes
3. Locate OAC title for OSBOE (contact OK Secretary of State)

Rules Engine Impact:
CRITICAL - Cannot calculate compliance for DO physicians without knowing total
CME requirement and renewal frequency

Priority: CRITICAL - Blocks rules engine deployment for DO license type
```

---

## CROSS-SOURCE CONGRUENCY TRACKING

For each major requirement, track source alignment:

**Format:**

```
**[Requirement]**

[FACT - STATUTE] [Value] per [Citation]
[FACT - ADMIN_CODE] [Value] per [Citation]
[FACT - BOARD] [Value] per [Board source]

Cross-Source Congruency: 3/3 sources agree ✅

OR

[FACT - STATUTE] [Value A]
[FACT - BOARD] [Value B] - CONFLICT

Cross-Source Congruency: Conflict detected ⚠️
Resolution: Applied source hierarchy - STATUTE takes precedence
Authority: Per conflict resolution policy, statute (legislative)
> board website (operational)
```

---

## SPECIAL INSTRUCTIONS FOR NP RESEARCH

### License Type Context

Nurse Practitioners are typically regulated by **State Boards of Nursing**, NOT medical boards.

**Research Protocol for NPs:**

1. **Identify the correct board:**
   - State Board of Nursing (most common)
   - Separate Advanced Practice Nursing Board (some states)
   - Medical board (rare - a few states)

2. **Understand NP licensure structure:**
   - RN (Registered Nurse) licensure vs. NP (Advanced Practice) licensure
   - Many states require active RN license + NP certification
   - CME requirements may apply to RN renewal, NP renewal, or both

3. **Research NP-specific renewal requirements:**
   - Does NP have separate renewal from RN?
   - Are CME requirements different for NP vs RN?
   - Do NPs have specialty-specific requirements (ACNP, FNP, etc.)?

4. **Document clearly:**
   - Is this RN renewal requirements or NP renewal requirements?
   - If both apply, document both separately
   - Clarify any interdependencies (e.g., RN CME + NP CME both required?)

5. **Controlled Substance Context:**
   - Many states grant NPs prescriptive authority conditionally
   - Prescribing CME requirements may differ from MD/DO
   - Document prescribing context separately if applicable

---

## SPLIT-BOARD COMPARISON TABLE (If Applicable)

If researching a split-board state, create a comprehensive comparison:

```
## Comparison: [LICENSE TYPE 1] vs [LICENSE TYPE 2]

| Factor | [LICENSE TYPE 1] Board | [LICENSE TYPE 2] Board |
|--------|---|---|
| **Board Name** | [Name] | [Name] |
| **Governing Statute** | [Citation] | [Citation] |
| **Administrative Code** | [Citation] | [Citation] |
| **Website** | [URL] | [URL] |
| **Renewal Portal** | [URL] | [URL] |
| **Total CME Hours** | [X hrs/Y yrs] | [X hrs/Y yrs] |
| **Renewal Frequency** | [Cycle] | [Cycle] |
| **CME Categories** | [Category types] | [Category types] |
| **Mandatory Topics** | [Topics] | [Topics] |
| **Audit Frequency** | [Annual/Per cycle] | [Annual/Per cycle] |
| **Board Cert Exemption** | [ABMS|AOA|Both|None] | [ABMS|AOA|Both|None] |
| **CME Tracking System** | [System] | [System] |
| **Renewal Fee** | $[X] | $[X] |

**Key Differences to Note:**
- [Difference 1 with citation]
- [Difference 2 with citation]
- [Difference 3 with citation]
```

---

## DOCUMENT QUALITY CHECKLIST

Before finalizing the narrative document, verify:

- [ ] Frontmatter YAML is complete with all required fields
- [ ] All factual statements have evidence classification ([FACT], [INFERENCE], [GAP])
- [ ] All [FACT] statements include source citation, URL, and quote
- [ ] All [INFERENCE] statements explain reasoning and state confidence level
- [ ] All [CRITICAL GAP] statements document search attempts and next steps
- [ ] Cross-source congruency tracked for all major requirements
- [ ] Sections follow consistent structure and formatting
- [ ] Split-board comparison table included (if applicable)
- [ ] Research gaps clearly documented with priority levels
- [ ] Sources Cited section is complete with URLs and access dates
- [ ] Appendix includes uncovered topics and additional discoveries
- [ ] Completion percentage calculated
- [ ] Document is tagged with research date and last verified date
- [ ] SOC2/ISO frontmatter fields completed

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-01-02 | **Major Restructure**: Narrative markdown focus with regulatory validation markers ([FACT], [INFERENCE], [GAP]), Comprehensive frontmatter with SOC2/ISO compliance metadata, Separate license type protocol (MD vs DO vs NP), Split-board research protocol clarified, Evidence classification system with inline notation, Cross-source congruency tracking, Gap documentation with priority tiers, All sources must be cited with URL and quote, Appendix section for uncovered topics and additional discoveries |
| 2.1.0 | 2026-01-01 | Added split-board recognition, Question 14 (medical marijuana), CME tracking systems, renewal fees section |
| 2.0.0 | 2026-01-01 | Oklahoma gold standard integration, YAML output format |
| 1.0.0 | 2026-01-01 | Initial prompt creation |

---

*This research prompt establishes a comprehensive framework for validating and documenting state medical/nursing license renewal requirements with regulatory citations, supporting CREDMATE's CME accuracy framework.*
