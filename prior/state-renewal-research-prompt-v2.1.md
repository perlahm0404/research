# State Medical License Renewal Requirements Research Prompt v2.1

**Version:** 2.1
**Date:** 2026-01-01
**Purpose:** Comprehensive research framework for MD, DO, and NP license renewal requirements with focus on CME and related activities
**Output Format:**
1. Comprehensive narrative markdown (.md) file
2. Structured Excel-compatible tables (.xlsx or .csv)
**Scope:** Single state per research session, reusable framework

---

## RESEARCH OBJECTIVES

You are conducting comprehensive research on medical/nursing license renewal requirements for a SINGLE STATE to support a compliance tracking rules engine. Your deliverables will include:

1. **Comprehensive Findings Document** - Full narrative with all research details
2. **Structured Data Tables** - Excel-compatible tables for rules engine import

### Primary Focus Areas
1. **CME Requirements** - Total hours, categories, topics, providers, tracking systems
2. **Related Activities** - Board certification, MOC, residency credit, specialty requirements
3. **Renewal Process** - Frequency, fees, deadlines, attestation vs. audit systems
4. **Compliance & Penalties** - Late fees, non-compliance consequences, audit procedures
5. **Special Cases** - First renewal, newly licensed, lapsed licenses, exemptions

---

## CRITICAL INSTRUCTIONS - READ FIRST

### Scope Limitation: RENEWAL REQUIREMENTS ONLY

**DO NOT research initial licensing requirements** unless they directly affect renewal:

#### ❌ EXCLUDE (Out of Scope)
- Exam requirements (USMLE, COMLEX, NBME, FLEX)
- Medical school accreditation (LCME, ECFMG)
- Postgraduate training years required for initial license
- Background check procedures for new applicants
- Citizenship/visa requirements for initial application
- Application fees and processing timelines for initial licensure

#### ✅ INCLUDE (Affects Renewal)
- First renewal grace periods for newly licensed (e.g., Oklahoma: 3 years)
- Residency/fellowship CME credit (e.g., Oklahoma: 50h/year)
- Training exemptions from CME during active residency
- How "newly licensed" is defined (date of initial license vs date CME tracking begins)

**Why**: This prompt focuses on **renewal-specific requirements** only to avoid scope creep.

---

### License Type Specification
**YOU MUST RESEARCH ONLY ONE LICENSE TYPE PER SESSION:**
- **MD** (Allopathic Physicians) - Medical Doctors
- **DO** (Osteopathic Physicians) - Doctors of Osteopathic Medicine
- **NP** (Nurse Practitioners) - Advanced Practice Registered Nurses

**If the user specifies "MD":** Research MD renewal requirements ONLY.
**If the user specifies "DO":** Research DO renewal requirements ONLY.
**If the user specifies "NP":** Research NP renewal requirements ONLY.

### Split Board States - AUTOMATIC DETECTION REQUIRED
Many states have **separate boards** for MD and DO physicians:
- **Separate MD Board:** Regulates allopathic physicians only
- **Separate DO Board:** Regulates osteopathic physicians only

**Confirmed Split-Board States:**
AZ, CA, FL, ME, MI, NV, OK, PA, TN, VT, WA, WV

**MANDATORY PROTOCOL:**
1. **Before starting research:** Determine if the target state has separate MD and DO boards
2. **If separate boards exist:**
   - Research ONLY the board corresponding to the license type specified
   - Document that separate boards exist (note the other board's name/URL for reference)
   - DO NOT mix requirements from both boards
   - Create comparison table showing MD vs DO differences
3. **If unified board exists:**
   - Research the single unified board
   - Note whether MD and DO have different requirements within the same board

**Split-Board Comparison Table (if applicable):**

| Factor | MD Board | DO Board |
|--------|----------|----------|
| Board Name | [Full name] | [Full name] |
| Governing Statute | [Citation] | [Citation] |
| Total CME Hours | [X hours/Y years] | [X hours/Y years] |
| Renewal Cycle | [Annual/Biennial/Triennial] | [Annual/Biennial/Triennial] |
| CME Categories | [AMA Category 1/2] | [AOA Category 1-A/1-B/2-A/2-B] |
| Portal URL | [URL] | [URL] |
| CME Tracking System | [CE Broker/Other] | [CE Broker/Other] |

**NP License Type:**
- NPs are typically regulated by **Board of Nursing**, NOT medical boards
- Automatically research Board of Nursing for NP license type
- Document if NP requirements differ from MD/DO

---

## LIFECYCLE PHASES FRAMEWORK (CRITICAL)

Extract and differentiate renewal requirements across **THREE lifecycle phases**:

### Phase 1: Initial Licensure (Pre-License)
**SKIP THIS PHASE** - Out of scope per instructions above.

### Phase 2: First Renewal Cycle
**Research question:** "What CME or other requirements must be met BEFORE the first license renewal?"

**Extract:**
1. Grace periods for newly licensed physicians (e.g., Oklahoma: 3 years from license date)
2. Reduced requirements for first-time renewers
3. One-time requirements (HIV/AIDS, child abuse, human trafficking)
4. Exemptions for recent graduates or residents/fellows
5. Documentation requirements for first renewal
6. When CME tracking begins vs when license was issued

**Evidence Classification Required:**
- [FACT] - Explicitly stated in statute/admin code/board website
- [INFERENCE - HIGH/MEDIUM/LOW CONFIDENCE] - Derived from available facts
- [CRITICAL GAP] - Not found despite thorough search

### Phase 3: Ongoing Renewals (Steady-State)
**Research question:** "What are the recurring CME requirements for SUBSEQUENT renewals after the first?"

**Extract:**
1. Total CME hours per cycle
2. Cycle length (years/months)
3. Category requirements (Category 1, AOA 1-A, etc.)
4. Topic-specific mandates (pain management, ethics, prescribing, etc.)
5. Rollover policies
6. Exemptions and alternatives
7. Verification requirements
8. Audit process
9. Non-compliance penalties

---

## DATA CLASSIFICATION STANDARDS - CRITICAL

**Purpose:** Prevent confusion between FACTS (directly stated), INFERENCES (derived), and ASSUMPTIONS (unverified).

### Classification System

#### [FACT] - Direct Statement from Primary Source
**Requirements:**
- Must include exact quote from source
- Must include source URL
- Must specify source type (STATE_STATUTE, STATE_ADMIN_CODE, STATE_BOARD_WEBSITE)

**Example:**
```
[FACT] Oklahoma requires 60 hours of Category 1 CME every 3 years.

Source: [ADMIN_CODE] Oklahoma Administrative Code Title 435, Section 10-15-1
URL: https://oklahoma.gov/oac/435-10-15-1
Last Verified: 2026-01-01

Verbatim Quote:
"Each physician shall complete 60 hours of Category 1 continuing medical education every three years."
```

#### [INFERENCE] - Derived from Facts or Logical Reasoning
**Requirements:**
- Must explain reasoning clearly
- Must state confidence level: HIGH / MEDIUM / LOW
- Must specify what primary source would confirm it
- Must document supporting facts

**Example:**
```
[INFERENCE - MEDIUM CONFIDENCE] Oklahoma license renewal is likely triennial (every 3 years).

Reasoning: CME is tracked on 3-year cycle per statute. Renewal notices sent 60 days before expiration per board website. Statute does not explicitly state license expiration frequency, but 3-year CME cycle suggests 3-year renewal.

Supporting Facts:
- [FACT] CME required every 3 years (OAC 435:10-15-1)
- [FACT] Renewal notices sent 60 days before expiration (okmedicalboard.org)

Verification Method: Search 59 O.S. § 481-518 for "license expiration" OR "validity period" OR contact board at (405) 962-1400
```

#### [CRITICAL GAP] - Not Found Despite Thorough Search
**Requirements:**
- Document what was searched
- List attempted sources
- Recommend verification method
- State impact on rules engine

**Example:**
```
[CRITICAL GAP] CME audit percentage unknown.

What We Know:
- [FACT] Board conducts random audits (okmedicalboard.org/cme-audit)

What We Don't Know:
- What percentage of licensees are audited annually?
- Is it truly random or stratified by specialty/risk?

Attempted Sources:
- 59 O.S. § 481-518 (Medical Practice Act) - searched for "audit" - NOT FOUND
- OAC 435:10-15-1 (CME requirements) - searched for "audit percentage" - NOT FOUND
- okmedicalboard.org/cme-audit - states "random audits" but no percentage
- Board FAQ - no audit statistics

Verification Method:
1. Contact Oklahoma State Board directly (405-962-1400)
2. FOIA request for audit statistics

Rules Engine Impact: Cannot estimate audit risk for licensees. Affects compliance reminder timing.

Priority: HIGH
```

---

## CROSS-SOURCE CONGRUENCY VALIDATION

For EACH requirement, track which sources agree to build confidence.

**Congruency Count Format:**
```
Cross-Source Congruency: 3/4
Sources: STATE_STATUTE | STATE_ADMIN_CODE | BOARD_WEBSITE
Disagrees: FSMB (shows 50 hours, but state board shows 60 hours - board website takes precedence)
```

**Congruency Scoring:**
- **4+ sources agree** = Highest confidence
- **3 sources agree** = High confidence
- **2 sources agree** = Medium confidence
- **1 source only** = Low confidence - flag for follow-up
- **Sources conflict** = Document conflict, resolve per hierarchy

**Source Hierarchy for Conflicts:**
1. **State Statute** (HIGHEST AUTHORITY)
2. **State Administrative Code**
3. **State Board Official Regulations/Rules**
4. **State Board Website / Official Guidance**
5. **Board Portal Instructions**
6. **Secondary Sources** (LOWEST - corroboration only)

---

## RESEARCH PROTOCOL - MANDATORY SEQUENCE

### PHASE 1: STATUTORY RESEARCH (PRIMARY AUTHORITY)
**Source Type Code:** `[STATUTE]`

**Step 1.1: Identify Primary Medical Practice Statutes**
1. Search for state's primary medical practice act
2. Common statute locations:
   - Title/Chapter on "Professions and Occupations"
   - Title/Chapter on "Medicine and Surgery"
   - Title/Chapter on "Health Professions"
3. Document:
   - Full statute citation (e.g., "Oklahoma Statutes Title 59, Section 495a.1")
   - Statute title
   - Last amended date (if available)
   - URL to official state statute repository

**Step 1.2: Search Official State Statute Repositories**
Priority order:
1. Official state legislature website
2. State-maintained legal code website
3. Justia State Law (https://law.justia.com/codes/[state]/)
4. FindLaw State Statutes
5. State bar association legal resources

**Step 1.3: Extract Statutory Requirements**
Search for:
- License renewal frequency and deadlines
- Continuing education requirements (hours, categories, topics)
- Renewal fees and late penalties
- Attestation and reporting requirements
- Exemptions and special cases
- Non-compliance consequences

**Required Documentation Format:**
```
[STATUTE] Citation: [Full citation]
Source: [URL]
Last Verified: [YYYY-MM-DD]
Last Amended: [Date if available]

Verbatim Quote:
"[Exact text from statute]"

Analysis: [Your interpretation]
Evidence Classification: [FACT] or [INFERENCE - confidence level]
Cross-Source Congruency: [X/Y sources]
```

---

### PHASE 2: ADMINISTRATIVE CODE RESEARCH (SECONDARY AUTHORITY)
**Source Type Code:** `[ADMIN_CODE]`

**Step 2.1: Identify State Administrative Code**
Common naming patterns:
- "[State] Administrative Code"
- "[State] Code of Regulations"
- "[State] Board Rules"

Search for:
- Title/Chapter on the specific medical board
- Sections on license renewal, CME, continuing education

**Step 2.2: Extract Administrative Requirements**
Administrative codes typically specify:
- Exact CME hour requirements
- Required CME topics
- Approved CME providers
- CME documentation and retention
- Audit procedures
- Exemptions and alternatives

---

### PHASE 3: STATE BOARD WEBSITE RESEARCH (OFFICIAL GUIDANCE)
**Source Type Code:** `[BOARD_WEBSITE]`

**Step 3.1: Review Board Website Sections**
1. Renewal/License Renewal Section
2. CME/Continuing Education Section
3. Laws & Rules Section
4. Forms & Applications Section
5. FAQs/Frequently Asked Questions

**Step 3.2: Download Official Board Documents**
- Renewal instruction PDFs
- CME guidelines documents
- Board newsletters/bulletins
- Licensing handbooks

---

### PHASE 4: REGULATORY & THIRD-PARTY SOURCE RESEARCH
**Source Codes:** `[CME_VENDOR]`, `[COMPACT]`, `[PROFESSIONAL_ASSOC]`, `[SPECIALTY_BOARD]`

**CME Tracking System Vendors:**
- CE Broker: https://www.cebroker.com/[STATE]
- Document how system works and integration with board

**Interstate Compacts:**
- IMLC (Interstate Medical Licensure Compact)
- NLC (Nurse Licensure Compact for NPs)

**Professional Associations:**
- State medical association
- State osteopathic association
- State nurses association

---

## COMPREHENSIVE RESEARCH REQUIREMENTS

### SECTION A: RENEWAL FREQUENCY & TIMELINE

**Required Data Points:**

| Data Point | Source Type | Evidence Level | Congruency |
|------------|-------------|----------------|------------|
| Renewal cycle (years) | [STATUTE]/[ADMIN_CODE] | [FACT]/[INFERENCE] | X/Y |
| Renewal deadline method | [STATUTE]/[ADMIN_CODE] | [FACT]/[INFERENCE] | X/Y |
| Renewal window opening | [BOARD_WEBSITE] | [FACT]/[INFERENCE] | X/Y |
| Grace period duration | [STATUTE]/[ADMIN_CODE] | [FACT]/[CRITICAL GAP] | X/Y |
| License status during grace | [STATUTE]/[ADMIN_CODE] | [FACT]/[CRITICAL GAP] | X/Y |

---

### SECTION B: CME TOTAL HOUR REQUIREMENTS

**Required Data Points:**

| Data Point | Source Type | Evidence Level | Congruency |
|------------|-------------|----------------|------------|
| Total hours per cycle | [ADMIN_CODE] | [FACT]/[CRITICAL GAP] | X/Y |
| Category 1 minimum | [ADMIN_CODE] | [FACT]/[CRITICAL GAP] | X/Y |
| Category 2 maximum | [ADMIN_CODE] | [FACT]/[INFERENCE] | X/Y |
| Accepted CME accreditors | [ADMIN_CODE]/[BOARD_WEBSITE] | [FACT]/[INFERENCE] | X/Y |

---

### SECTION C: MANDATORY CME TOPICS

**Common Mandatory Topics to Research:**

| Topic Category | Hours | Frequency | Applies To | Evidence | Congruency |
|----------------|-------|-----------|------------|----------|------------|
| Pain Management | [X] | [Annual/Per cycle] | [DEA holders/All] | [FACT]/[INFERENCE] | X/Y |
| Opioid Prescribing | [X] | [Annual/Per cycle] | [DEA holders/All] | [FACT]/[INFERENCE] | X/Y |
| Medical Marijuana | [X] | [One-time/Recurring] | [Recommenders/All] | [FACT]/[INFERENCE] | X/Y |
| Ethics | [X] | [Per cycle] | [All] | [FACT]/[INFERENCE] | X/Y |
| Cultural Competency | [X] | [Per cycle] | [All] | [FACT]/[INFERENCE] | X/Y |
| Implicit Bias | [X] | [Per cycle] | [All] | [FACT]/[INFERENCE] | X/Y |
| Human Trafficking | [X] | [One-time/Recurring] | [All] | [FACT]/[INFERENCE] | X/Y |
| Child Abuse | [X] | [One-time/Recurring] | [All] | [FACT]/[INFERENCE] | X/Y |
| Domestic Violence | [X] | [Per cycle] | [All] | [FACT]/[INFERENCE] | X/Y |

**For EACH mandatory topic found, document:**
```
Topic: [Topic name]
Hours Required: [X hours]
Frequency: [Annual/Per renewal cycle/One-time]
Applies To: [All licensees/DEA holders only/Condition]
Lifecycle Phase: [First renewal only/Ongoing/Both]

Source: [STATUTE]/[ADMIN_CODE]
Citation: [Full citation]
URL: [Direct link]
Last Verified: [Date]

Verbatim Quote:
"[Exact statutory/regulatory language]"

Evidence Classification: [FACT] or [INFERENCE - confidence]
Cross-Source Congruency: [X/Y sources agree]
```

---

### SECTION D: CONTROLLED SUBSTANCE PRESCRIBING CONTEXT

**Purpose:** Document the prescribing framework that creates the CONTEXT for pain management/opioid CME.

**Extract:**
- Acute pain opioid supply limits (days)
- Chronic pain documentation requirements (treatment plan, patient agreement)
- Telemedicine restrictions for controlled substances
- Prescription Monitoring Program (PMP) mandatory use
- Patient-provider agreement requirements
- Urine/serum screening requirements

**Why This Matters:** Pain management CME is not isolated - it's part of a comprehensive prescribing framework. Rules engine needs this context.

---

### SECTION E: CME AUDIT PROCEDURES

**Required Documentation:**

**Audit Type:**
- [ ] Random audit
- [ ] For-cause audit
- [ ] Universal submission (all licensees)
- [ ] Targeted/stratified audit
- [ ] No audit (attestation only)

**Random Audit Details (if applicable):**
```
Audit Percentage: [X% of renewals annually]
Evidence: [FACT] or [INFERENCE] or [CRITICAL GAP]
Source: [Citation]

Selection Method: [Truly random/Stratified/Other]
Source: [Citation]

Frequency: [Annual/Per cycle/Continuous]
Source: [Citation]
```

**Audit Documentation Requirements:**
```
Required for Audit:
- [ ] CME certificates showing [required elements]
- [ ] Course completion verification
- [ ] Provider accreditation proof
- [ ] Transcript from CME tracking system
- [ ] Other: [Specify]

Audit Response Timeline: [X days from notification]
Source: [Citation]

Penalties for Non-Compliance:
- Failure to respond: [Fine/Suspension/Other]
- Insufficient CME found: [Remediation required/Fine/Other]
- False attestation: [Disciplinary action possible]

CME Retention Period: [X years from completion OR current cycle + X years]
Evidence: [FACT] or [CRITICAL GAP]
Source: [Citation]
```

---

### SECTION F: EXEMPTIONS & ALTERNATIVES TO CME

**Board Certification as CME Alternative:**
```
Accepted: [Yes/No/Partial]
Evidence: [FACT] or [INFERENCE - confidence]
Source: [Citation]

Accepted Specialty Boards:
- ABMS (American Board of Medical Specialties): [Yes/No]
  CME Credit: [Full requirement met OR X hours credited]
  Timing: [Obtained during cycle OR active certified status]
- AOA (American Osteopathic Association): [Yes/No]
  CME Credit: [Full requirement met OR X hours credited]

Requirements:
- Must be obtained during current renewal cycle: [Yes/No]
- Ongoing certified status sufficient: [Yes/No]
- Satisfies topic requirements: [Yes/No - list exceptions]
```

**Residency/Fellowship Credit:**
```
Accepted: [Yes/No]
Evidence: [FACT] or [INFERENCE - confidence]
Source: [Citation]

Credit Awarded:
- Per year of completed training: [X hours]
- Maximum credit per cycle: [X hours]
- Applies to preceding [X years] only
- Documentation required: [Program director letter/Certificate]
```

**Other Exemptions:**
- Age-based (e.g., over 70 years old)
- Inactive/retired status
- Disability/hardship
- Military service
- COVID-19 waivers (check if still active)

---

### SECTION G: FIRST RENEWAL & NEWLY LICENSED REQUIREMENTS

**Grace Period Research:**
```
Grace Period Exists: [Yes/No]
Evidence: [FACT] or [INFERENCE] or [CRITICAL GAP]
Source: [Citation]

Duration: [X years from initial licensure]
Example: "Physician licensed in Year 1 not subject to CME until Year 4 renewal"

CME Requirements for First Renewal:
- Same as ongoing: [Yes/No]
- Reduced hours: [X hours instead of Y hours]
- Mandatory topics apply: [Yes/No]
- Pro-rated based on license date: [Yes/No]

CME Clock Start:
- Immediately upon licensure: [Yes/No]
- First full year after licensure: [Yes/No]
- [X months/years] after licensure
```

---

### SECTION H: RENEWAL FEES & LATE PENALTIES

**Fee Structure:**
```
Standard Renewal Fee: $[X]
Source: [Citation]
Last Updated: [Date]

Late Renewal:
- Late renewal period: [X days after expiration]
- Late fee: $[X] OR [Percentage increase]
- License status during late period: [Active/Inactive/Grace]
- Can practice during late period: [Yes/No]

License Expiration:
- License lapses after: [X days post-expiration]
- Lapsed license status: [Expired/Inactive/Suspended]

Reinstatement (vs. Late Renewal):
- Reinstatement required after: [X days/months lapsed]
- Reinstatement fee: $[X]
- Additional requirements: [Background check/CME makeup/Re-exam]

CME Non-Compliance Fees:
- Fine for CME non-completion: $[X]
- Classification: [Disciplinary/Non-disciplinary]
```

---

### SECTION I: LAPSED LICENSE REINSTATEMENT CME REQUIREMENTS

**Three-Tier Framework (common pattern):**

| Lapse Duration | Process | CME Required | Background Check | Re-Examination |
|----------------|---------|--------------|------------------|----------------|
| < 1 year | Automatic renewal | Current cycle | No | No |
| 1-3 years | Formal reinstatement | Makeup for lapsed period | May be required | May be required |
| > 3 years | New application | Full requirements | Required | Required |

**Document for each tier:**
- CME calculation method (per year lapsed, full cycle, proportional)
- Additional requirements
- Fees
- Timeline

---

### SECTION J: CME TRACKING & REPORTING SYSTEMS

**System Details:**
```
CME Tracking System: [CE Broker/Board-operated/None]
Vendor: [Vendor name if applicable]
Vendor URL: [URL]
Licensee Portal: [URL]

Reporting Method:
- [ ] Attestation at renewal (honor system)
- [ ] Manual certificate upload
- [ ] CME provider auto-reporting
- [ ] Universal submission required

Provider Integration:
- Auto-reporting providers: [List if available]
- Manual entry required for: [Which providers]

Licensee Access:
- Can view CME transcript: [Yes/No]
- Can print CME summary: [Yes/No]
```

---

### SECTION K: STATE-SPECIFIC REQUIREMENTS

**Medical Marijuana/Cannabis Education:**
```
State Has Medical Marijuana Program: [Yes/No]
CME Required to Recommend: [Yes/No]
Evidence: [FACT] or [CRITICAL GAP]
Source: [Citation]

Hours Required: [X hours]
Frequency: [One-time/Annual/Per cycle]
Topics: [State law/Clinical use/Dosing]
State-Approved Course: [Yes - provider/No - any course]
```

**Jurisprudence Examination:**
```
Required: [Yes/No]
When: [Initial licensure/Every renewal/Every X years]
Format: [Online/Open-book/Closed-book]
Passing Score: [X%]
CME Credit: [X hours if applicable]
```

**PDMP Training:**
```
Required: [Yes/No]
Hours: [X hours]
Frequency: [One-time/Recurring]
Applies To: [All prescribers/DEA holders/Controlled substance prescribers]
```

---

## GAP DOCUMENTATION STANDARD

Use this template for documenting research gaps:

```
GAP ID: [STATE-BOARD-TOPIC-ISSUE]
Gap Description: [Brief description]
Priority: [CRITICAL/HIGH/MEDIUM/LOW]

What We Know:
- [FACT] fact 1 with source
- [FACT] fact 2 with source
- [INFERENCE] inference 1 with reasoning

What We Don't Know:
- Specific unanswered question 1
- Specific unanswered question 2

Attempted Sources:
- Source 1 (URL) - searched for [terms] - NOT FOUND
- Source 2 (URL) - checked [sections] - NOT FOUND
- Source 3 (contact attempted) - [result]

Verification Method: [How to resolve]
Rules Engine Impact: [Impact description]
Workaround: [Temporary solution if needed]
```

**Gap Priority Definitions:**
- **CRITICAL:** Blocks rules engine deployment (total hours, renewal frequency, mandatory topics)
- **HIGH:** Impacts compliance validation (audit procedures, verification methods)
- **MEDIUM:** Affects edge cases (rollover, reinstatement details)
- **LOW:** Nice-to-have context (board statistics, historical changes)

---

## COMPLETION PERCENTAGE TRACKING

Calculate research completeness for each section:

```
Research Completion Status: [X%]

Section Breakdown:
- Lifecycle phases (first renewal vs ongoing): [Complete/Partial/Missing]
- Total CME hours: [Complete/Partial/Missing]
- Topic requirements: [Complete/Partial/Missing]
- Audit process: [Complete/Partial/Missing]
- Exemptions: [Complete/Partial/Missing]
- First renewal grace: [Complete/Partial/Missing]
- Fees & timeline: [Complete/Partial/Missing]
- Lapsed license: [Complete/Partial/Missing]
- CME tracking system: [Complete/Partial/Missing]
- State-specific requirements: [Complete/Partial/Missing]

Overall Completion: [X/10 sections complete = X%]

Next Steps:
1. [Specific research action needed]
2. [Source to access]
3. [Contact if needed]
```

---

## OUTPUT FORMAT SPECIFICATION

### Two-File Deliverable System

#### FILE 1: Comprehensive Findings Document (Narrative)
**Filename:** `[STATE]_[LICENSE_TYPE]_FINDINGS.md`
**Example:** `OKLAHOMA_MD_FINDINGS.md`

**Purpose:** Capture ALL research including context, out-of-scope details, and full quotes

**Structure:**
```markdown
# [STATE] [LICENSE TYPE] License Renewal: Comprehensive Findings

**State:** [State name]
**License Type:** [MD/DO/NP]
**Board Name:** [Full official board name]
**Board Website:** [URL]
**Research Date:** [YYYY-MM-DD]
**Researcher:** [Name]
**Completion:** [X%]

---

## EXECUTIVE SUMMARY

[2-3 paragraph overview of key findings, unique requirements, critical gaps]

---

## TABLE OF CONTENTS

1. Board & Regulatory Overview
2. Lifecycle Phases (First Renewal vs Ongoing)
3. Renewal Frequency & Timeline
4. CME Total Hour Requirements
5. Mandatory CME Topics
6. Approved CME Providers & Accreditors
7. CME Tracking & Reporting Systems
8. CME Audit Procedures
9. Exemptions & Alternatives to CME
10. First Renewal & Newly Licensed Requirements
11. Renewal Fees & Late Penalties
12. Lapsed License Reinstatement CME
13. Attestation & Renewal Process
14. Controlled Substance Prescribing Context
15. State-Specific Requirements
16. Cross-Source Validation & Conflicts
17. Research Gaps & Follow-Up
18. Appendices

---

## 1. BOARD & REGULATORY OVERVIEW

### 1.1 Official Board Information
- Board Name: [Full name]
- Address: [Physical address]
- Phone: [Phone number]
- Website: [URL]
- Renewal Portal: [URL]

### 1.2 Statutory Authority
- Primary Statute: [Citation with URL]
- Administrative Code: [Citation with URL]

### 1.3 Split Board Status (if applicable)
[Document if state has separate MD/DO boards]

---

## 2. LIFECYCLE PHASES

### Phase 1: Initial Licensure
**Status:** OUT OF SCOPE (excluded per research protocol)

### Phase 2: First Renewal Cycle

[Document grace periods, reduced requirements, one-time topics]

**Grace Period:**
[FACT] or [INFERENCE] or [CRITICAL GAP]
Source: [Citation]
Evidence: [Quote]

### Phase 3: Ongoing Renewals

[Document recurring requirements]

---

## 3. RENEWAL FREQUENCY & TIMELINE

| Attribute | Requirement | Source | Evidence | Congruency |
|-----------|-------------|--------|----------|------------|
| Renewal cycle | [X years] | [Citation] | [FACT]/[INFERENCE] | X/Y |
| Renewal deadline | [Method] | [Citation] | [FACT]/[INFERENCE] | X/Y |
| Grace period | [X days] | [Citation] | [FACT]/[GAP] | X/Y |

---

[Continue with all sections following the structure...]

---

## 17. RESEARCH GAPS & FOLLOW-UP

### Critical Gaps Summary

| Gap ID | Description | Priority | Verification Method |
|--------|-------------|----------|---------------------|
| GAP-001 | [Description] | CRITICAL | [Method] |
| GAP-002 | [Description] | HIGH | [Method] |

### Detailed Gap Documentation

[Use gap template for each identified gap]

---

## 18. APPENDICES

### Appendix A: Full Statutory Citations
[Complete text of key statute sections]

### Appendix B: Administrative Code Citations
[Complete text of key rule sections]

### Appendix C: Source URLs Master List
[All URLs with last verified dates]

### Appendix D: Glossary
[CME categories, terms, acronyms]
```

---

#### FILE 2: Structured Excel Tables
**Filename:** `[STATE]_[LICENSE_TYPE]_CME_Requirements.xlsx` or `.csv`
**Example:** `OKLAHOMA_MD_CME_Requirements.xlsx`

**Purpose:** Excel-compatible structured data for rules engine import

**Required Tables/Sheets:**

**Sheet 1: Summary**
| Field | Value | Source | Evidence | Congruency |
|-------|-------|--------|----------|------------|
| State | [State] | - | - | - |
| License Type | [MD/DO/NP] | - | - | - |
| Board Name | [Name] | [URL] | - | - |
| Renewal Cycle (Years) | [X] | [Citation] | [FACT]/[INFERENCE] | X/Y |
| Total CME Hours | [X] | [Citation] | [FACT]/[INFERENCE] | X/Y |
| CME Cycle (Years) | [X] | [Citation] | [FACT]/[INFERENCE] | X/Y |
| First Renewal Grace (Years) | [X] | [Citation] | [FACT]/[GAP] | X/Y |
| Audit Type | [Random/For-cause/Universal] | [Citation] | [FACT]/[GAP] | X/Y |

**Sheet 2: Mandatory Topics**
| Topic | Hours | Frequency | Applies To | Lifecycle Phase | Source | Evidence | Congruency |
|-------|-------|-----------|------------|-----------------|--------|----------|------------|
| Pain Management | [X] | [Annual/Cycle] | [DEA/All] | [Ongoing] | [Citation] | [FACT] | X/Y |
| Opioid Education | [X] | [Annual/Cycle] | [DEA/All] | [Ongoing] | [Citation] | [FACT] | X/Y |
| [etc.] |

**Sheet 3: Exemptions**
| Exemption Type | Accepted | Credit Amount | Requirements | Source | Evidence |
|----------------|----------|---------------|--------------|--------|----------|
| ABMS Board Cert | [Yes/No] | [Full/X hours] | [Details] | [Citation] | [FACT] |
| AOA Board Cert | [Yes/No] | [Full/X hours] | [Details] | [Citation] | [FACT] |
| Residency/Fellowship | [Yes/No] | [X hours/year] | [Details] | [Citation] | [FACT] |
| AMA PRA | [Yes/No] | [Full/Partial] | [Details] | [Citation] | [FACT] |

**Sheet 4: Fees & Timeline**
| Fee Type | Amount | Notes | Source | Evidence |
|----------|--------|-------|--------|----------|
| Standard Renewal | $[X] | [Details] | [Citation] | [FACT] |
| Late Renewal | $[X] | [Grace period: X days] | [Citation] | [FACT] |
| Reinstatement | $[X] | [Varies by duration] | [Citation] | [FACT] |

**Sheet 5: Lapsed License Tiers**
| Lapse Duration | Process | CME Required | Bg Check | Re-Exam | Fee | Source |
|----------------|---------|--------------|----------|---------|-----|--------|
| < 1 year | [Process] | [X hours] | [Yes/No] | [Yes/No] | $[X] | [Citation] |
| 1-3 years | [Process] | [X hours] | [Yes/No] | [Yes/No] | $[X] | [Citation] |
| > 3 years | [Process] | [X hours] | [Yes/No] | [Yes/No] | $[X] | [Citation] |

**Sheet 6: Research Gaps**
| Gap ID | Description | Priority | What We Know | What We Don't Know | Verification Method | Impact |
|--------|-------------|----------|--------------|-------------------|---------------------|--------|
| GAP-001 | [Desc] | [CRITICAL/HIGH/MEDIUM/LOW] | [Facts] | [Questions] | [Method] | [Impact] |

**Sheet 7: Source Citations**
| Source ID | Source Type | Citation | URL | Last Verified | Used For |
|-----------|-------------|----------|-----|---------------|----------|
| SRC-001 | [STATUTE] | [Citation] | [URL] | [Date] | [Requirements] |
| SRC-002 | [ADMIN_CODE] | [Citation] | [URL] | [Date] | [Requirements] |

---

## QUALITY CHECKLIST

Before submitting research, verify:

### Completeness
- [ ] All lifecycle phases researched (first renewal vs ongoing)
- [ ] Every mandatory topic searched systematically
- [ ] First renewal grace period documented or flagged as gap
- [ ] Audit procedures fully researched
- [ ] Fees and penalties documented
- [ ] All gaps identified and prioritized
- [ ] Cross-source validation completed
- [ ] Completion percentage calculated

### Evidence Quality
- [ ] Every requirement tagged with [FACT]/[INFERENCE]/[CRITICAL GAP]
- [ ] All [FACT] entries include exact source quote and URL
- [ ] All [INFERENCE] entries include reasoning, confidence level, verification method
- [ ] All [CRITICAL GAP] entries document attempted sources
- [ ] Cross-source congruency count calculated (minimum 2 sources per requirement)
- [ ] Source hierarchy followed for conflict resolution

### Output Format
- [ ] Comprehensive findings document (.md) complete with all sections
- [ ] Excel tables (.xlsx or .csv) created with all required sheets
- [ ] Both files use consistent naming convention
- [ ] All tables properly formatted (Excel-compatible markdown)
- [ ] Document metadata complete (date, researcher, completion %)

### Special Cases
- [ ] Split-board status checked (if MD or DO research)
- [ ] Controlled substance prescribing context documented
- [ ] State-specific requirements researched (marijuana, jurisprudence, PDMP)
- [ ] First renewal vs ongoing differentiation clear

---

## WORKFLOW SUMMARY

```
START RESEARCH
    ↓
1. Identify state and license type (MD/DO/NP)
    ↓
2. Check split-board status (if MD or DO)
    ↓
3. PHASE 1: Search statutes
   - Medical Practice Act
   - Renewal sections
   - Topic-specific mandates (pain, ethics, etc.)
   - Document with [STATUTE] tag + evidence level
    ↓
4. PHASE 2: Search administrative code
   - Board rules on CME
   - Total hours, categories, topics
   - Audit procedures
   - Document with [ADMIN_CODE] tag + evidence level
    ↓
5. PHASE 3: Search board website
   - Renewal pages, CME guidelines, FAQs
   - Download official documents
   - Document with [BOARD_WEBSITE] tag + evidence level
    ↓
6. PHASE 4: Third-party sources
   - CME tracking vendors (CE Broker)
   - Interstate compacts (IMLC, NLC)
   - Professional associations
   - Document with appropriate tags
    ↓
7. Cross-validate all sources
   - Calculate congruency counts
   - Flag conflicts
   - Resolve per hierarchy
    ↓
8. Differentiate lifecycle phases
   - First renewal (grace periods, one-time topics)
   - Ongoing renewals (recurring requirements)
    ↓
9. Document controlled substance context
   - Why pain/opioid CME exists
   - Prescribing framework
    ↓
10. Identify gaps
    - Classify priority (CRITICAL/HIGH/MEDIUM/LOW)
    - Document attempted sources
    - Recommend verification methods
    ↓
11. Calculate completion percentage
    - Rate each section (Complete/Partial/Missing)
    - Overall percentage
    ↓
12. Generate deliverables
    - File 1: Comprehensive findings (.md)
    - File 2: Structured tables (.xlsx or .csv)
    ↓
13. Quality check
    - Run through checklist
    - Verify all evidence tags
    - Confirm congruency counts
    ↓
SUBMIT DELIVERABLES
```

---

## USER SPECIFICATION CONFIRMATION

Before beginning research, confirm:

**Please specify:**
1. **State:** [Which state to research]
2. **License Type:** [MD, DO, or NP]
3. **Special Focus:** [Any particular areas of concern]
4. **Output Format Preference:** [Excel .xlsx or .csv for tables]

**Then begin research following the protocol above.**

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-01 | Initial v1 prompt |
| 2.0 | 2026-01-01 | Expanded with comprehensive framework |
| 2.1 | 2026-01-01 | Added: (1) Lifecycle phases framework (first renewal vs ongoing), (2) Evidence classification system ([FACT]/[INFERENCE]/[CRITICAL GAP]), (3) Cross-source congruency validation, (4) Gap documentation templates, (5) Controlled substance prescribing context, (6) Completion percentage tracking, (7) Two-file deliverable system (narrative + Excel tables), (8) Split-board comparison tables, (9) Scope limitation (renewal only, exclude initial licensing), (10) Quality checklist with evidence rigor requirements |

---

**END OF RESEARCH PROMPT v2.1**
