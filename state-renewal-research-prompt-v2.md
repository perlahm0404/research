# State Medical License Renewal Requirements Research Prompt v2.0

**Version:** 2.0
**Date:** 2026-01-01
**Purpose:** Comprehensive research framework for MD, DO, and NP license renewal requirements with focus on CME and related activities
**Output Format:** Narrative prose with structured tables (Excel-compatible markdown)
**Scope:** Single state per research session, reusable framework

---

## RESEARCH OBJECTIVES

You are conducting comprehensive research on medical/nursing license renewal requirements for a SINGLE STATE to support a compliance tracking rules engine. Your deliverable will be a detailed findings document that captures ALL renewal requirements with rigorous source documentation.

### Primary Focus Areas
1. **CME Requirements** - Total hours, categories, topics, providers, tracking systems
2. **Related Activities** - Board certification, MOC, residency credit, specialty requirements
3. **Renewal Process** - Frequency, fees, deadlines, attestation vs. audit systems
4. **Compliance & Penalties** - Late fees, non-compliance consequences, audit procedures
5. **Special Cases** - First renewal, newly licensed, lapsed licenses, exemptions

---

## CRITICAL INSTRUCTIONS - READ FIRST

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

**MANDATORY PROTOCOL:**
1. **Before starting research:** Determine if the target state has separate MD and DO boards
2. **If separate boards exist:**
   - Research ONLY the board corresponding to the license type specified
   - Document that separate boards exist (note the other board's name/URL for reference)
   - DO NOT mix requirements from both boards
3. **If unified board exists:**
   - Research the single unified board
   - Note whether MD and DO have different requirements within the same board

**Examples of Split Board States (verify current status):**
- Oklahoma: Separate MD and DO boards
- Michigan: Separate MD and DO boards
- Texas: Separate MD and DO boards
- Pennsylvania: Separate MD and DO boards

**NP License Type:**
- NPs are typically regulated by **Board of Nursing**, NOT medical boards
- Automatically research Board of Nursing for NP license type
- Document if NP requirements differ from MD/DO

---

## RESEARCH PROTOCOL - MANDATORY SEQUENCE

### PHASE 1: STATUTORY RESEARCH (PRIMARY AUTHORITY)
**Source Type Code:** `[STATUTE]`

**Step 1.1: Identify Primary Medical Practice Statutes**
1. Search for state's primary medical practice act (typically titled "Medical Practice Act" or similar)
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
Search in this priority order:
1. Official state legislature website (e.g., legislature.state.XX.gov)
2. State-maintained legal code website
3. Justia State Law (https://law.justia.com/codes/[state]/)
4. FindLaw State Statutes
5. State bar association legal resources

**Step 1.3: Extract Statutory Requirements**
Search statutes for sections covering:
- License renewal frequency and deadlines
- Continuing education requirements (hours, categories, topics)
- Renewal fees and late penalties
- Attestation and reporting requirements
- Exemptions and special cases
- Non-compliance consequences
- Board authority to promulgate rules

**Required Documentation Format:**
```
[STATUTE] Citation: [Full citation]
Source: [URL]
Last Verified: [YYYY-MM-DD]
Last Amended: [Date if available]

Verbatim Quote:
"[Exact text from statute - use quotation marks]"

Analysis: [Your interpretation with evidence classification]
```

**Evidence Classification for Statutory Findings:**
- `[FACT]` - Explicitly stated in statute, no interpretation needed
- `[INFERENCE - HIGH CONFIDENCE]` - Strongly implied by statutory language
- `[INFERENCE - MEDIUM CONFIDENCE]` - Reasonable interpretation, but needs rule clarification
- `[INFERENCE - LOW CONFIDENCE]` - Speculative, requires administrative code verification
- `[CRITICAL GAP]` - Statute delegates to board rules, no detail in statute itself

---

### PHASE 2: ADMINISTRATIVE CODE RESEARCH (SECONDARY AUTHORITY)
**Source Type Code:** `[ADMIN_CODE]`

**Step 2.1: Identify State Administrative Code**
Administrative codes contain the detailed rules promulgated by the medical board pursuant to statutory authority.

Common naming patterns:
- "[State] Administrative Code" (e.g., Oklahoma Administrative Code)
- "[State] Code of Regulations"
- "[State] Board Rules"

Search for:
- Title/Chapter on the specific medical board (e.g., "Title 435 - Board of Medical Licensure")
- Sections on license renewal, CME, continuing education

**Step 2.2: Search Administrative Code Repositories**
Search in priority order:
1. Official state administrative code website
2. Secretary of State administrative rules database
3. Medical board website (rules/regulations section)
4. State archives/law library

**Step 2.3: Extract Administrative Requirements**
Administrative codes typically specify:
- Exact CME hour requirements (total and by category)
- Required CME topics (pain management, ethics, cultural competency, etc.)
- Approved CME providers and accrediting bodies
- CME documentation and retention requirements
- Audit procedures (random, for-cause, universal submission)
- Exemptions and alternatives (board certification, MOC, residency credit)
- Renewal process details

**Required Documentation Format:**
```
[ADMIN_CODE] Citation: [Full citation]
Source: [URL]
Last Verified: [YYYY-MM-DD]
Effective Date: [Date]

Verbatim Quote:
"[Exact text from administrative code]"

Analysis: [Interpretation with evidence classification]
```

---

### PHASE 3: STATE BOARD WEBSITE RESEARCH (OFFICIAL GUIDANCE)
**Source Type Code:** `[BOARD_WEBSITE]`

**Step 3.1: Locate Official State Medical Board Website**
For MD/DO: Search "[State] Medical Board" or "[State] Board of Medicine"
For NP: Search "[State] Board of Nursing"

Document:
- Official board name
- Board website URL
- Website last updated date (if shown)

**Step 3.2: Review Board Website Sections**
Systematically review:
1. **Renewal/License Renewal Section**
   - Renewal instructions
   - Online renewal portal links
   - Renewal FAQs
   - Renewal checklists

2. **CME/Continuing Education Section**
   - CME requirements summary
   - Approved CME providers list
   - CME tracking systems (CE Broker, etc.)
   - CME audit information
   - Downloadable CME forms/worksheets

3. **Laws & Rules Section**
   - Links to statutes and administrative code
   - Board policies and guidance documents
   - Position statements on CME topics

4. **Forms & Applications Section**
   - Renewal application forms
   - CME attestation forms
   - Audit response forms

5. **FAQs/Frequently Asked Questions**
   - Common renewal questions
   - CME requirement clarifications
   - Special case guidance

**Step 3.3: Download Official Board Documents**
Capture information from:
- Renewal instruction PDFs
- CME guidelines documents
- Board newsletters/bulletins
- Licensing handbooks
- Continuing education manuals

**Required Documentation Format:**
```
[BOARD_WEBSITE] Page Title: [Title]
URL: [Direct URL to page]
Last Verified: [YYYY-MM-DD]
Last Updated (per site): [Date if shown]

Content Summary:
[Detailed summary of relevant information]

Verbatim Quotes (if applicable):
"[Direct quotes from website]"

Analysis: [Interpretation]
```

---

### PHASE 4: REGULATORY & THIRD-PARTY SOURCE RESEARCH
**Source Type Code:** `[REGULATORY]` or specific codes below

**Step 4.1: FSMB (Federation of State Medical Boards)**
**Source Code:** `[FSMB]`

Resources to check:
- FSMB State-by-State Comparison documents
- FSMB Policy Documents
- FSMB Board Actions Database
- URL: https://www.fsmb.org

**Step 4.2: CME Tracking System Vendors**
**Source Code:** `[CME_VENDOR]`

If state uses third-party CME tracking:
- **CE Broker:** https://www.cebroker.com/[STATE]
- **Other vendors:** Document vendor name and URL

Research:
- How system works (auto-reporting vs. manual entry)
- Licensee access and reporting requirements
- Approved course catalogs
- Integration with board renewal system

**Step 4.3: Interstate Compacts**
**Source Code:** `[COMPACT]`

For applicable states:
- **Interstate Medical Licensure Compact (IMLC):** Check if state is member
  - URL: https://www.imlcc.org
  - Document compact-specific CME requirements (if any)

- **Nurse Licensure Compact (NLC):** For NP research
  - URL: https://www.ncsbn.org/nlc.htm
  - Document multi-state license implications

**Step 4.4: State-Specific CME Course Vendors**
**Source Code:** `[STATE_CME_VENDOR]`

Some states offer or require specific courses:
- State medical association CME programs
- State-mandated courses (e.g., prescribing, opioid education)
- Board-developed courses

Document:
- Course titles
- Required vs. optional status
- Credit hours awarded
- Provider/vendor name and URL

**Step 4.5: Professional Associations**
**Source Code:** `[PROFESSIONAL_ASSOC]`

Check state-level associations:
- State medical association
- State osteopathic association (for DO)
- State nurses association (for NP)

Research:
- CME offerings
- Renewal guidance for members
- Legislative updates affecting renewal

**Step 4.6: Specialty Board Organizations**
**Source Code:** `[SPECIALTY_BOARD]`

If board certification/MOC is mentioned:
- **ABMS (American Board of Medical Specialties):** For MD specialty boards
- **AOA (American Osteopathic Association):** For DO specialty boards
- **AANP/ANCC:** For NP certification

Document how specialty board activities count toward CME.

---

## COMPREHENSIVE RESEARCH REQUIREMENTS

### SECTION A: RENEWAL FREQUENCY & TIMELINE

**Research Questions:**
1. What is the renewal period? (Annual, biennial, triennial, other)
2. What is the renewal deadline? (Fixed date, birth month, license issue date)
3. When does the renewal window open? (60 days prior, 90 days prior, etc.)
4. Is there a grace period after expiration?
5. What is license status during grace period? (Active, inactive, expired)

**Required Information to Extract:**

| Data Point | Source Type | Evidence Level |
|------------|-------------|----------------|
| Renewal cycle (years) | [STATUTE]/[ADMIN_CODE] | [FACT] or [INFERENCE] |
| Renewal deadline calculation method | [STATUTE]/[ADMIN_CODE] | [FACT] or [INFERENCE] |
| Renewal window opening | [BOARD_WEBSITE] | [FACT] or [INFERENCE] |
| Grace period duration | [STATUTE]/[ADMIN_CODE] | [FACT] or [INFERENCE] or [CRITICAL GAP] |
| License status during grace | [STATUTE]/[ADMIN_CODE] | [FACT] or [INFERENCE] or [CRITICAL GAP] |

**Statute Search Terms:**
- "license renewal"
- "license reregistration"
- "biennial renewal"
- "triennial renewal"
- "expiration"
- "renewal period"

---

### SECTION B: CME TOTAL HOUR REQUIREMENTS

**Research Questions:**
1. What is the total CME hour requirement per renewal cycle?
2. What CME categories are required? (Category 1, Category 2, AOA Category 1-A, 1-B, 2-A, 2-B)
3. Are there minimum requirements for specific categories?
4. What is the definition of each category?
5. Which organizations' CME classification systems are accepted? (AMA, AOA, ACCME, AAFP, other)

**Required Information to Extract:**

| Data Point | Source Type | Evidence Level |
|------------|-------------|----------------|
| Total hours per cycle | [ADMIN_CODE]/[STATUTE] | [FACT] or [CRITICAL GAP] |
| Category 1 minimum | [ADMIN_CODE] | [FACT] or [CRITICAL GAP] |
| Category 2 maximum | [ADMIN_CODE] | [FACT] or [INFERENCE] |
| Accepted CME accreditors | [ADMIN_CODE]/[BOARD_WEBSITE] | [FACT] or [INFERENCE] |
| Category definitions source | [ADMIN_CODE]/[BOARD_WEBSITE] | [FACT] or [INFERENCE] |

**Admin Code Search Terms:**
- "continuing medical education"
- "continuing education hours"
- "CME requirements"
- "Category 1"
- "Category 2"
- "AMA PRA Category 1"
- "AOA Category"
- "ACCME"

---

### SECTION C: MANDATORY CME TOPICS

**Research Questions:**
1. Are there state-mandated CME topics beyond general practice?
2. How many hours required for each mandatory topic?
3. Are mandatory topics annual or per renewal cycle?
4. Can one course satisfy multiple topic requirements?
5. Are there specific approved courses or can any accredited course on the topic count?

**Common Mandatory Topics to Research:**

| Topic Category | Search Terms | Typical States Requiring |
|----------------|--------------|--------------------------|
| **Pain Management** | "pain management CME", "chronic pain education" | Most states post-2016 |
| **Opioid Prescribing** | "opioid CME", "opioid prescribing", "substance abuse" | Most states post-2016 |
| **Controlled Substances** | "controlled substance prescribing", "DEA education" | Many states |
| **Medical Marijuana/Cannabis** | "medical marijuana", "cannabis education", "medical cannabis" | States with medical marijuana programs |
| **Ethics** | "medical ethics", "professional ethics", "bioethics" | ~30 states |
| **Cultural Competency** | "cultural competency", "diversity", "health disparities" | ~15 states |
| **Implicit Bias** | "implicit bias", "unconscious bias" | Growing number of states |
| **Human Trafficking** | "human trafficking recognition", "trafficking victim identification" | ~20 states |
| **Child Abuse** | "child abuse recognition", "mandated reporter training" | ~25 states |
| **Domestic Violence** | "domestic violence", "intimate partner violence" | Several states |
| **End-of-Life Care** | "palliative care", "advance directives", "end of life" | Several states |
| **HIV/AIDS** | "HIV/AIDS education", "bloodborne pathogens" | Several states |
| **Infection Control** | "infection control", "disease prevention" | Some states |
| **Telemedicine** | "telemedicine standards", "telehealth" | Growing number |
| **Risk Management** | "risk management", "patient safety" | Some states |
| **Prescribing Standards** | "prescribing practices", "medication safety" | Many states |

**Required Documentation Format:**

For EACH mandatory topic found:

```
[ADMIN_CODE] or [STATUTE] Citation: [Full citation]
Topic: [Topic name]
Hours Required: [Number] hours
Frequency: [Annual/Per cycle]
Timing: [When must be completed - e.g., "each year preceding renewal"]
Exemptions: [Any exemptions - e.g., "Non-DEA holders exempt"]
Approved Courses: [Board-specific courses required OR any accredited course on topic]
Source URL: [Direct link]
Last Verified: [Date]

Verbatim Statutory/Rule Language:
"[Exact quote]"

Evidence Level: [FACT] or [INFERENCE - confidence level]
```

**Special Cases to Document:**
- **DEA-conditional requirements:** Topics required ONLY if physician has DEA registration
- **Specialty-specific topics:** Requirements that vary by specialty
- **One-time vs. recurring:** Topics required only once vs. every cycle
- **Cumulative topics:** Can hours from previous cycles carry forward?

---

### SECTION D: APPROVED CME PROVIDERS & ACCREDITORS

**Research Questions:**
1. Which accrediting organizations' CME is accepted?
2. Are there state-specific approved provider lists?
3. Can out-of-state CME be used?
4. Can international CME be used?
5. Are there prohibited providers?
6. What documentation is required from providers?

**Standard Accrediting Bodies to Check:**

| Accreditor | Type | Typical Acceptance |
|------------|------|-------------------|
| **ACCME** | Accreditation Council for Continuing Medical Education | MD/DO - Universal |
| **AMA** | American Medical Association | MD - Universal |
| **AOA** | American Osteopathic Association | DO - Universal, MD varies |
| **AAFP** | American Academy of Family Physicians | MD/DO - Common |
| **ANCC** | American Nurses Credentialing Center | NP - Universal |
| **AANP** | American Association of Nurse Practitioners | NP - Common |
| **State Medical Associations** | State-level organizations | State-specific |
| **AAPA** | American Academy of Physician Assistants | If researching PA |

**Required Documentation:**

```
[ADMIN_CODE] or [BOARD_WEBSITE]
Section: Approved CME Providers

Accepted Accreditors:
- [Accreditor name]: [Explicit acceptance or inferred]
  Source: [Citation/URL]
  Evidence: [FACT] or [INFERENCE]

State-Specific Provider List:
- [Yes/No]
- If yes, URL: [Link to list]
- Last updated: [Date]

Special Requirements:
- Out-of-state CME: [Accepted/Restricted/Prohibited]
- International CME: [Accepted/Restricted/Prohibited]
- Online/Self-Study CME: [Limits or restrictions]
- Industry-sponsored CME: [Restrictions]

Provider Documentation Requirements:
- Certificate requirements: [What must certificate include]
- Provider accreditation verification: [How verified]
```

---

### SECTION E: CME TRACKING & REPORTING SYSTEMS

**Research Questions:**
1. How do licensees report CME completion?
2. Is there an official state tracking system?
3. Is tracking system vendor-operated (e.g., CE Broker)?
4. Is CME auto-reported by providers or manually entered by licensee?
5. What is licensee's access to the tracking system?
6. When must CME be entered into system?

**Tracking System Types:**

| System Type | Description | Common States |
|-------------|-------------|---------------|
| **Attestation-Only** | Licensee attests to completion at renewal, no submission required unless audited | Many states |
| **Universal Submission** | ALL licensees must submit CME certificates/documentation at every renewal | Some states |
| **Third-Party Tracking** | State contracts with vendor (CE Broker, etc.) for centralized tracking | Growing number |
| **Hybrid** | Combination of attestation + random verification + vendor tracking | Some states |

**Required Documentation:**

```
[BOARD_WEBSITE] or [CME_VENDOR]
CME Tracking System: [Name or "Attestation-based"]

System Details:
- Vendor: [Vendor name or "Board-operated" or "None"]
- Vendor URL: [If applicable]
- Licensee Portal: [URL for licensee access]
- Access Requirements: [How licensees log in]

Reporting Method:
- [X] Attestation at renewal (honor system)
- [X] Manual certificate upload
- [X] CME provider auto-reporting to system
- [X] Manual entry by licensee into tracking system
- [X] Universal submission of all certificates at renewal

Deadlines:
- CME entry deadline: [When must be entered]
- Submission deadline: [When must be submitted if required]

Provider Integration:
- Auto-reporting providers: [List if available]
- Manual entry required for: [Which providers]

Access & Features:
- Licensee can view CME transcript: [Yes/No]
- Licensee can print CME summary: [Yes/No]
- System validates accreditation: [Yes/No]
```

---

### SECTION F: CME AUDIT PROCEDURES

**Research Questions:**
1. Does the board conduct CME audits?
2. What type of audits? (Random, for-cause, universal)
3. What percentage of licensees are audited?
4. How are audit subjects selected?
5. What triggers a for-cause audit?
6. What documentation must be submitted during audit?
7. What is the audit response deadline?
8. What are penalties for audit non-compliance?
9. What are penalties for audit non-response?

**Audit System Types:**

| Audit Type | Description | Frequency |
|------------|-------------|-----------|
| **Random Audit** | Board randomly selects X% of renewals for CME verification | Annual or per cycle |
| **For-Cause Audit** | Board audits based on complaint, investigation, or red flags | As needed |
| **Universal Submission** | ALL licensees must submit CME documentation at renewal | Every renewal |
| **Targeted Audit** | Board audits specific populations (e.g., first-time renewals, previously non-compliant) | Varies |
| **No Audit** | Attestation-only, board does not routinely verify CME | Never (unless complaint) |

**Required Documentation:**

```
[ADMIN_CODE] or [BOARD_WEBSITE]
Section: CME Audit Procedures

Audit Type: [Random/For-Cause/Universal/Targeted/None]
Evidence Level: [FACT] or [INFERENCE]

Random Audit Details (if applicable):
- Audit percentage: [X% of renewals]
  Source: [Citation]
  Evidence: [FACT] or [INFERENCE] or [CRITICAL GAP]

- Selection method: [Truly random/stratified/other]
  Source: [Citation]

- Frequency: [Annual/Per cycle/Continuous]
  Source: [Citation]

For-Cause Audit Triggers:
- [List triggers - e.g., "Complaint received", "Previous non-compliance", "Incomplete attestation"]
  Source: [Citation]

Audit Notification:
- Method: [Email/Mail/Portal notification]
- Advance notice: [Days or "None"]
- Source: [Citation]

Required Documentation for Audit:
- [X] CME certificates showing: [Required elements]
- [X] Course completion verification
- [X] Provider accreditation proof
- [X] Transcript from CME tracking system
- [Other requirements]
  Source: [Citation]

Audit Response Timeline:
- Deadline to respond: [X days from notification]
  Source: [Citation]
  Consequence for late response: [Penalty]

Audit Non-Compliance Penalties:
- Failure to respond: [Penalty - e.g., "License suspension", "Fine of $X"]
  Source: [Citation]

- Insufficient CME found: [Penalty - e.g., "Must complete deficit within X days", "Fine", "Probation"]
  Source: [Citation]

- False attestation: [Penalty - e.g., "Disciplinary action", "License revocation possible"]
  Source: [Citation]

CME Documentation Retention Requirement:
- Retention period: [X years from completion OR current cycle + X years]
  Source: [Citation]
  Evidence: [FACT] or [CRITICAL GAP]

- Format: [Paper/Electronic/Either]
  Source: [Citation]
```

---

### SECTION G: EXEMPTIONS & ALTERNATIVES TO CME

**Research Questions:**
1. Does board certification/recertification satisfy CME requirements?
2. If yes, which specialty boards are accepted? (ABMS, AOA, other)
3. How much CME credit is awarded for board certification?
4. Does MOC (Maintenance of Certification) count as CME?
5. Can residency or fellowship training substitute for CME?
6. Are there age-based exemptions? (e.g., physicians over 70)
7. Are there practice-based exemptions? (e.g., non-clinical, retired status)
8. Are there disability or hardship exemptions?
9. Are there military service exemptions?
10. Are there COVID-19 emergency waivers still in effect?

**Required Documentation:**

```
[ADMIN_CODE] or [BOARD_WEBSITE]
Section: CME Exemptions and Alternatives

1. BOARD CERTIFICATION AS CME ALTERNATIVE

Accepted: [Yes/No/Partial]
Source: [Citation]
Evidence: [FACT] or [INFERENCE]

Accepted Specialty Boards:
- ABMS (American Board of Medical Specialties): [Yes/No]
  CME Credit: [Full requirement met OR X hours credited]
  Timing: [Certification obtained during renewal cycle OR active certified status]
  Source: [Citation]

- AOA (American Osteopathic Association) Specialty Boards: [Yes/No]
  CME Credit: [Full requirement met OR X hours credited]
  Source: [Citation]

- Other specialty boards: [List if applicable]

Requirements:
- Must be obtained during current renewal cycle: [Yes/No]
- Ongoing certified status sufficient: [Yes/No]
- Satisfies all topic requirements: [Yes/No - list exceptions]
- Documentation required: [Certificate copy/Board verification letter]
  Source: [Citation]

2. MOC (MAINTENANCE OF CERTIFICATION)

Accepted: [Yes/No/Partial]
Source: [Citation]

MOC Activities Counted as CME:
- Self-assessment modules: [Yes/No - X hours credited]
- Practice improvement modules: [Yes/No - X hours credited]
- Secure examination: [Yes/No - X hours credited]
- All MOC activities combined: [Full requirement OR partial credit]
  Source: [Citation]

3. RESIDENCY & FELLOWSHIP TRAINING

Accepted: [Yes/No]
Source: [Citation]
Evidence: [FACT] or [INFERENCE]

Credit Awarded:
- Per year of completed training: [X hours]
- Maximum credit per cycle: [X hours]
- Applies to: [Preceding X years only OR any timeframe]
- Documentation required: [Program director letter/Certificate]
  Source: [Citation]

4. AGE-BASED EXEMPTIONS

Age exemption exists: [Yes/No]
Source: [Citation]

Details:
- Exemption age: [X years old]
- Requirements: [Full exemption OR reduced hours OR conditions]
- Must be actively practicing: [Yes/No]
- Must be retired/inactive: [Yes/No]
  Source: [Citation]

5. PRACTICE-BASED EXEMPTIONS

Non-Clinical Practice:
- Exemption available: [Yes/No]
- Requirements: [Not seeing patients for X years OR other criteria]
- Status change required: [Inactive/Retired/Other]
  Source: [Citation]

Retired/Inactive Status:
- CME required: [Yes/No/Reduced]
- Hours if reduced: [X hours]
  Source: [Citation]

6. DISABILITY/HARDSHIP EXEMPTIONS

Available: [Yes/No]
Source: [Citation]

Process:
- Application required: [Yes - describe process]
- Board discretion: [Yes/No]
- Temporary vs. permanent: [Details]
- Documentation required: [Medical records/Other]
  Source: [Citation]

7. MILITARY SERVICE EXEMPTIONS

Available: [Yes/No]
Source: [Citation]

Details:
- Active duty exemption: [Yes/No - conditions]
- Deployment exemption: [Yes/No - conditions]
- Credit for military CME: [Yes/No - how much]
- Documentation: [Military orders/Other]
  Source: [Citation]

8. COVID-19 EMERGENCY WAIVERS

Still in effect: [Yes/No]
Last updated: [Date]
Source: [Citation]

Details:
- Waiver period: [Dates]
- Requirements waived: [CME hours/Specific topics/Other]
- Expiration: [Date or "Ongoing"]
  Source: [Citation]

9. OTHER EXEMPTIONS

[List any other exemptions found - e.g., "First renewal after initial licensure", "International medical graduates", etc.]
```

---

### SECTION H: FIRST RENEWAL & NEWLY LICENSED REQUIREMENTS

**Research Questions:**
1. When is first renewal due after initial licensure?
2. Is there a CME grace period for newly licensed physicians?
3. If grace period exists, how long? (Common: 3 years from initial licensure)
4. Do newly licensed physicians have reduced CME requirements for first renewal?
5. When does CME clock start? (Immediately, first full year, other)
6. Are mandatory topics required for first renewal?

**Special Cases to Research:**
- **Mid-cycle initial licensure:** If licensed 1 year into a 2-year cycle, what is required?
- **Pro-rated CME:** Do some states prorate CME based on license issue date?
- **Residency transition:** Physicians leaving residency - do residency years count as CME?

**Required Documentation:**

```
[ADMIN_CODE] or [STATUTE] or [BOARD_WEBSITE]
Section: First Renewal After Initial Licensure

First Renewal Timeline:
- Due: [X years from initial license date OR next regular cycle]
  Source: [Citation]
  Evidence: [FACT] or [INFERENCE] or [CRITICAL GAP]

CME Grace Period:
- Exists: [Yes/No]
  Source: [Citation]
  Evidence: [FACT] or [INFERENCE] or [CRITICAL GAP]

- Duration: [X years from initial licensure]
  Example: "Physician licensed in Year 1 not subject to CME until Year 4 renewal"
  Source: [Citation]

CME Requirements for First Renewal:
- Same as ongoing renewals: [Yes/No]
- Reduced hours: [If yes, X hours instead of regular Y hours]
- Mandatory topics apply: [Yes/No - list exemptions if any]
- Pro-rated based on license date: [Yes/No - calculation method]
  Source: [Citation]

CME Clock Start:
- Starts immediately upon licensure: [Yes/No]
- Starts first full year after licensure: [Yes/No]
- Starts [X months/years] after licensure: [Specify]
  Source: [Citation]

Residency/Fellowship Credit:
- Recent residency graduates: [CME required OR residency counts as CME for first cycle]
- Fellowship completion: [Counts as X hours CME]
  Source: [Citation]

Mid-Cycle Licensure:
- Licensed mid-cycle example: "Licensed in Month 6 of 24-month cycle"
  CME Required: [Pro-rated OR full amount OR none]
  Calculation: [Method]
  Source: [Citation]
```

---

### SECTION I: RENEWAL FEES & LATE PENALTIES

**Research Questions:**
1. What is the standard renewal fee?
2. Are there different fee tiers? (Active, inactive, retired, etc.)
3. What is the late renewal fee/penalty?
4. How long is the late renewal period?
5. After what point does license expire/lapse instead of late renewal?
6. Can a lapsed license be renewed or must it be reinstated?
7. What are reinstatement fees?
8. Are there processing fees for online vs. paper renewal?
9. Are fees statutory or set by board rule?

**Required Documentation:**

```
[STATUTE] or [ADMIN_CODE] or [BOARD_WEBSITE]
Section: Renewal Fees and Penalties

Standard Renewal Fee:
- Amount: $[X]
  Source: [Citation]
  Last updated: [Date fee was set/last changed]
  Evidence: [FACT] or [INFERENCE]

Fee Tiers:
- Active license: $[X]
- Inactive/Non-practicing license: $[X]
- Retired status: $[X]
- Other categories: [List]
  Source: [Citation]

Payment Methods:
- [X] Online (credit card/debit)
- [X] Check
- [X] Money order
- [X] Other: [Specify]
  Processing fees: [Amount if applicable]
  Source: [Citation]

Late Renewal:
- Late renewal period: [X days after expiration]
  Source: [Citation]

- Late fee/penalty: $[X] OR [Percentage increase]
  Source: [Citation]

- License status during late period: [Active/Inactive/Grace period]
  Source: [Citation]

- Can practice during late period: [Yes/No]
  Source: [Citation]

License Expiration/Lapse:
- License lapses after: [X days post-expiration OR immediately]
  Source: [Citation]

- Lapsed license status: [Expired/Inactive/Suspended]
  Source: [Citation]

Reinstatement (vs. Late Renewal):
- Reinstatement required after: [X days/months lapsed]
  Source: [Citation]

- Reinstatement fee: $[X]
  Source: [Citation]

- Additional requirements: [Background check/CME makeup/Re-examination/Other]
  Source: [Citation]

CME Non-Compliance Fees:
- Specific fine for CME non-completion: $[X]
  Source: [Citation]
  Classification: [Disciplinary/Non-disciplinary]

- Additional penalties: [License suspension/Probation/Other]
  Source: [Citation]
```

---

### SECTION J: LAPSED LICENSE REINSTATEMENT CME REQUIREMENTS

**Research Questions:**
1. If license lapses, what CME is required to reinstate?
2. Does lapse duration affect CME requirements?
3. Must licensee complete CME for lapsed period?
4. Are there tiered reinstatement frameworks based on lapse length?
5. Common tiers to research:
   - Lapsed < 1 year
   - Lapsed 1-3 years
   - Lapsed 3-5 years
   - Lapsed > 5 years

**Required Documentation:**

```
[ADMIN_CODE] or [STATUTE] or [BOARD_WEBSITE]
Section: Lapsed License Reinstatement CME

Reinstatement CME Framework:
- Tiered based on lapse duration: [Yes/No]
  Source: [Citation]

TIER 1: Lapsed < 1 Year
- CME Required: [X hours OR current cycle requirements OR makeup for lapsed period]
- Documentation: [Certificates/Attestation/Audit]
- Additional requirements: [Background check/Fees/Other]
  Source: [Citation]

TIER 2: Lapsed 1-3 Years (if applicable)
- CME Required: [X hours OR full cycle amount OR cumulative for lapsed cycles]
- Exemptions: [Any exemptions - e.g., board cert obtained during lapse]
- Additional requirements: [Background check/Re-examination/Interview/Other]
  Source: [Citation]

TIER 3: Lapsed 3-5 Years (if applicable)
- CME Required: [X hours OR special reinstatement amount]
- Must complete before reinstatement: [Yes/No - timing]
- Additional requirements: [Competency evaluation/Practice reentry program/Other]
  Source: [Citation]

TIER 4: Lapsed > 5 Years (if applicable)
- CME Required: [X hours OR treated as new applicant]
- Reinstatement vs. New Application: [Which process applies]
- Additional requirements: [Re-examination/Supervised practice/Other]
  Source: [Citation]

CME for Lapsed Period:
- Must complete CME for each lapsed year: [Yes/No]
- Calculation method: [X hours per year lapsed OR one full cycle OR other]
- Maximum CME required for reinstatement: [Cap if applicable]
  Source: [Citation]

Practice Reentry Programs:
- Required for lapsed > X years: [Duration threshold]
- Board-approved programs: [List or criteria]
- CME credit for reentry program: [Yes/No - amount]
  Source: [Citation]
```

---

### SECTION K: ATTESTATION & RENEWAL PROCESS

**Research Questions:**
1. What questions must be answered at renewal?
2. Is CME completion attested to or documented?
3. What other attestations are required? (Disciplinary actions, malpractice, health status, etc.)
4. Is renewal online, paper, or both?
5. What is the renewal portal URL?
6. What information can be updated at renewal?
7. Is renewal confirmation immediate or delayed?
8. What constitutes proof of renewal?

**Required Documentation:**

```
[BOARD_WEBSITE]
Section: Renewal Process and Attestation

Renewal Portal:
- URL: [Direct link to renewal portal]
- Access method: [License number + PIN/SSN/Email login/Other]
- Available: [Online only/Paper option/Both]
  Source: [Board website]

Renewal Window:
- Opens: [X days before expiration]
- Closes: [Expiration date OR X days after]
- Recommended submission: [Board recommendation]
  Source: [Citation]

Required Attestations at Renewal:
(List ALL questions licensees must answer - common ones below)

1. CME Completion:
   - "I have completed [X] hours of CME including [mandatory topics]"
   - Format: [Checkbox/Signature/Other]
   - Penalty for false attestation: [Disciplinary action/License revocation possible]
     Source: [Citation]

2. Disciplinary Actions:
   - "Any disciplinary actions by medical boards in any jurisdiction"
   - Requires explanation: [Yes/No]
   - Source: [Citation]

3. Criminal Convictions:
   - "Any felony or misdemeanor convictions"
   - Reporting period: [Since last renewal OR ever]
   - Source: [Citation]

4. Malpractice Claims:
   - "Any adverse judgments, settlements, or pending claims"
   - Threshold amount: [$X or all]
   - Source: [Citation]

5. Health Status:
   - "Any physical or mental condition affecting ability to practice"
   - Confidentiality: [How protected]
   - Source: [Citation]

6. Substance Abuse:
   - "Any substance abuse or addiction issues"
   - Self-reporting protection: [Physician health program referral/Other]
   - Source: [Citation]

7. Practice Information:
   - Primary practice address
   - Practice setting (hospital/clinic/telemedicine/other)
   - Specialty
   - Email and contact information
   - Source: [Citation]

8. Board Certification:
   - "Current board certification status"
   - Specialty board and expiration
   - Source: [Citation]

9. Other Licenses:
   - "All states where licensed"
   - Status of each license
   - Source: [Citation]

10. DEA Registration:
    - "Current DEA registration status"
    - Required if prescribing controlled substances
    - Source: [Citation]

[Add any state-specific attestations]

Information Updates Allowed:
- Name changes: [Yes/No - documentation required]
- Address updates: [Yes - can update anytime OR only at renewal]
- Practice setting changes: [Yes/No]
- Email updates: [Yes/No]
  Source: [Citation]

Renewal Confirmation:
- Immediate: [Yes/No]
- Processing time: [X hours/days]
- Proof of renewal: [Email confirmation/Receipt/Printable certificate/Updated license]
- Public verification: [License lookup updated within X hours/days]
  Source: [Citation]

Renewal Completion Requirements:
- Payment processed: [Required before approval]
- All questions answered: [Required/Some optional]
- Incomplete renewal: [Saved as draft OR must complete in one session]
  Source: [Citation]
```

---

### SECTION L: SPECIAL STATE-SPECIFIC REQUIREMENTS

**Research Questions:**
1. Does state have unique CME requirements not found in other states?
2. Does state require CME on state-specific laws or regulations?
3. Does state offer/require state-developed courses?
4. Are there prescribing-related CME requirements? (PDMP training, opioid education, etc.)
5. Does state have medical marijuana program requiring education?
6. Are there telemedicine CME requirements?
7. Does state require jurisprudence examination or course?

**Common State-Specific Areas:**

```
[BOARD_WEBSITE] or [ADMIN_CODE] or [STATE_CME_VENDOR]
Section: State-Specific CME and Education Requirements

1. STATE LAWS & REGULATIONS EDUCATION

Required: [Yes/No]
Source: [Citation]

Details:
- Topic: [e.g., "State Medical Practice Act", "Prescribing Laws", "Professional Boundaries"]
- Hours: [X hours]
- Frequency: [One-time/Every renewal/Every X years]
- Approved courses: [Board-developed course only OR any course covering state laws]
- Course provider: [Board/State medical association/Any]
- Online availability: [Yes/No - URL if applicable]
  Source: [Citation]

2. JURISPRUDENCE EXAMINATION

Required: [Yes/No]
Source: [Citation]

Details:
- When required: [Initial licensure only/Every renewal/Every X years]
- Format: [Online/In-person/Open-book/Closed-book]
- Passing score: [X%]
- Fee: [$X]
- CME credit awarded: [X hours]
- Exam URL: [Link if available]
  Source: [Citation]

3. PRESCRIPTION DRUG MONITORING PROGRAM (PDMP) TRAINING

Required: [Yes/No]
Source: [Citation]

Details:
- Hours: [X hours]
- Frequency: [One-time/Every renewal/Every X years]
- Who must complete: [All prescribers/DEA holders only/Controlled substance prescribers]
- State-specific course: [Yes - URL / No - any accredited course]
- Integration with prescribing authority: [Required before DEA registration/renewal]
  Source: [Citation]

4. MEDICAL MARIJUANA/CANNABIS EDUCATION

State has medical marijuana program: [Yes/No]
CME required to recommend/prescribe: [Yes/No]
Source: [Citation]

Details:
- Hours required: [X hours]
- Frequency: [One-time before certification/Every renewal/Every X years]
- Topics covered: [State law/Clinical use/Dosing/Other]
- State-approved course: [Yes - provider/No - any course]
- Registration required: [Separate cannabis practitioner registry]
  Source: [Citation]

5. TELEMEDICINE STANDARDS EDUCATION

Required: [Yes/No]
Source: [Citation]

Details:
- Hours: [X hours]
- Frequency: [One-time/Recurring]
- Required before: [Engaging in telemedicine/General requirement]
- Topics: [HIPAA/Technology standards/State telemedicine laws]
  Source: [Citation]

6. PRESCRIBING STANDARDS & GUIDELINES

Required: [Yes/No - beyond opioid CME]
Source: [Citation]

Details:
- Hours: [X hours]
- Topics: [Antibiotic stewardship/Appropriate use/Other]
- Frequency: [Per cycle/Annual]
  Source: [Citation]

7. STATE-DEVELOPED COURSES

Board offers own CME courses: [Yes/No]
Source: [Board website]

Available Courses:
- [Course title]: [Hours] - [Required/Optional] - [URL]
- [Course title]: [Hours] - [Required/Optional] - [URL]

Course Catalog URL: [Link if available]

8. OTHER STATE-SPECIFIC REQUIREMENTS

[Document any other unique state requirements not covered above]
Examples:
- Worker's compensation education
- Disability evaluation training
- Healthcare fraud prevention
- Language access/interpreter use
- LGBTQ+ health
- Veteran health
```

---

### SECTION M: CROSS-VALIDATION & CONFLICT RESOLUTION

**Critical Process:**
When you find the same data point from multiple sources, you must:
1. Document ALL sources for that data point
2. Flag any conflicts between sources
3. Establish source hierarchy for conflict resolution

**Source Hierarchy for Conflicts:**
1. **Current Statute** (highest authority)
2. **Current Administrative Code** (implementing regulations)
3. **Board Website Official Guidance** (official interpretation)
4. **Board Policy Documents/FAQs** (clarifications)
5. **Third-party sources** (lowest - use only if no official source)

**Required Documentation Format for Conflicts:**

```
DATA POINT CONFLICT IDENTIFIED

Requirement: [What is the conflicting data point - e.g., "Total CME hours per cycle"]

SOURCE 1: [STATUTE]
Citation: [Full citation]
States: [X hours]
URL: [Link]
Date verified: [Date]

SOURCE 2: [ADMIN_CODE]
Citation: [Full citation]
States: [Y hours]
URL: [Link]
Date verified: [Date]

SOURCE 3: [BOARD_WEBSITE]
Page: [Page title]
States: [Z hours]
URL: [Link]
Date verified: [Date]

CONFLICT ANALYSIS:
- Sources disagree on: [Specific point of disagreement]
- Possible reasons: [Outdated website/Administrative code supersedes statute/Recent change/Other]

RESOLUTION:
Per source hierarchy, authoritative requirement is: [X hours from SOURCE #]
Reasoning: [Explanation]

RECOMMENDATION:
- Verify with board directly: [Yes - this requires clarification]
- Accept hierarchy resolution: [Yes - if confident]
- Flag as CRITICAL GAP: [Yes - if cannot resolve]
```

---

### SECTION N: CRITICAL GAPS & FOLLOW-UP RESEARCH

Throughout your research, you will encounter gaps - information not found in available sources. You must systematically document these.

**Gap Classification:**

| Priority | Definition | Impact |
|----------|------------|--------|
| **CRITICAL** | Information essential for rules engine, no workaround possible | Blocks implementation |
| **HIGH** | Important for compliance accuracy, workaround exists but risky | Major limitation |
| **MEDIUM** | Affects edge cases or small population | Minor limitation |
| **LOW** | Nice-to-have, minimal compliance impact | No blocking issue |

**Required Gap Documentation:**

```
CRITICAL GAPS IDENTIFIED

GAP #[Number]: [Short description]
Priority: [CRITICAL/HIGH/MEDIUM/LOW]

What's Missing:
[Detailed description of missing information]

Why Critical:
[Impact on rules engine or compliance tracking]

Sources Searched:
- [X] State statutes: [Sections searched]
- [X] Administrative code: [Sections searched]
- [X] Board website: [Pages reviewed]
- [X] Board FAQs
- [X] Board contact attempted: [Yes/No]
- [X] FSMB resources checked
- [X] Other: [Specify]

Search Terms Used:
- "[term 1]"
- "[term 2]"
- [etc.]

Possible Reasons for Gap:
- [ ] Information exists but not publicly available
- [ ] Requirement truly doesn't exist (exemption/no rule)
- [ ] Board discretion on case-by-case basis
- [ ] Recent change not yet documented
- [ ] Other: [Specify]

Recommended Follow-Up:
1. [Action - e.g., "Contact Board CME coordinator at [phone]"]
2. [Action - e.g., "Submit public records request for CME audit procedures"]
3. [Action - e.g., "Review Board meeting minutes from [date range]"]

Workaround for Rules Engine:
[If critical gap, propose conservative assumption or default behavior]
Example: "Assume universal audit submission required unless confirmed otherwise"
```

**Mandatory Gap List to Address:**
Create a summary table of ALL gaps found:

| Gap # | Topic | Priority | Status | Follow-Up Action |
|-------|-------|----------|--------|------------------|
| 1 | [e.g., "CME audit percentage"] | CRITICAL | UNRESOLVED | Contact board |
| 2 | [e.g., "First renewal grace period"] | HIGH | UNRESOLVED | Review statutes again |
| [etc.] |

---

## OUTPUT FORMAT SPECIFICATION

Your final deliverable must be a **single markdown (.md) file** with the following structure:

---

### DOCUMENT HEADER

```markdown
# [STATE NAME] [LICENSE TYPE] License Renewal Requirements
## Comprehensive Research Report

**State:** [State name]
**License Type:** [MD/DO/NP]
**Board Name:** [Full official board name]
**Board Website:** [URL]
**Research Date:** [YYYY-MM-DD]
**Researcher:** [Your name/AI identifier]
**Document Version:** 1.0

---

## EXECUTIVE SUMMARY

[2-3 paragraph overview covering:]
- Renewal frequency
- Total CME hours required
- Key mandatory topics
- Unique state requirements
- Critical findings
- Major gaps identified

---
```

### REQUIRED SECTIONS (In Order)

```markdown
## TABLE OF CONTENTS
[Auto-generated list of sections]

---

## 1. BOARD & REGULATORY OVERVIEW

### 1.1 Official Board Information
[Board name, address, contact, website]

### 1.2 Statutory Authority
[Primary statutes governing renewal]

### 1.3 Administrative Code References
[Key OAC/regulatory sections]

### 1.4 Split Board Status
[If MD/DO boards separate, document here]

---

## 2. RENEWAL FREQUENCY & TIMELINE

[Section A content - use tables for clarity]

### 2.1 Renewal Cycle
| Attribute | Requirement | Source | Evidence Level |
|-----------|-------------|--------|----------------|
| Cycle length | [X years] | [Citation] | [FACT/INFERENCE] |
| [etc.] |

### 2.2 Renewal Deadlines
[Details]

### 2.3 Grace Periods
[Details]

---

## 3. CME TOTAL HOUR REQUIREMENTS

[Section B content]

### 3.1 Total Hours Per Cycle
[Table format]

### 3.2 CME Categories
[Table format]

### 3.3 Accreditation Requirements
[Table format]

---

## 4. MANDATORY CME TOPICS

[Section C content - CRITICAL SECTION]

### 4.1 Topic Summary Table
| Topic | Hours | Frequency | Source | Evidence | Notes |
|-------|-------|-----------|--------|----------|-------|
| Pain Management | 1 | Annual | [Citation] | [FACT] | DEA holders only |
| [etc.] |

### 4.2 Detailed Topic Requirements
[Subsection for each mandatory topic with full details]

---

## 5. APPROVED CME PROVIDERS & ACCREDITORS

[Section D content]

---

## 6. CME TRACKING & REPORTING SYSTEMS

[Section E content]

---

## 7. CME AUDIT PROCEDURES

[Section F content - CRITICAL SECTION]

---

## 8. EXEMPTIONS & ALTERNATIVES TO CME

[Section G content]

---

## 9. FIRST RENEWAL & NEWLY LICENSED REQUIREMENTS

[Section H content]

---

## 10. RENEWAL FEES & LATE PENALTIES

[Section I content]

---

## 11. LAPSED LICENSE REINSTATEMENT CME REQUIREMENTS

[Section J content]

---

## 12. ATTESTATION & RENEWAL PROCESS

[Section K content]

---

## 13. STATE-SPECIFIC REQUIREMENTS

[Section L content - VERY IMPORTANT]

---

## 14. SOURCE VALIDATION & CONFLICTS

[Section M content - document any conflicts found]

---

## 15. CRITICAL GAPS & FOLLOW-UP RESEARCH

[Section N content]

### 15.1 Critical Gaps Summary Table
[Table of all gaps]

### 15.2 Detailed Gap Analysis
[Full documentation per gap]

### 15.3 Recommended Follow-Up Actions
[Prioritized list]

---

## 16. APPENDICES

### Appendix A: Full Statutory Citations
[Complete text of key statute sections]

### Appendix B: Administrative Code Citations
[Complete text of key rule sections]

### Appendix C: Source URLs Master List
[All URLs referenced with last verified dates]

### Appendix D: Board Contact Information
[Phone, email, physical address, portal URLs]

### Appendix E: Glossary
[Define CME categories, terms, acronyms]

---

## DOCUMENT REVISION HISTORY

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial research | [Name] |

---
```

### TABLE FORMATTING REQUIREMENTS

All tables must be in markdown format compatible with Excel import:

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data | Data | Data |
```

**Use tables for:**
- Comparison data (renewal cycles, fees, hours)
- Mandatory topics with multiple attributes
- Source citations with evidence levels
- Gap summaries
- Audit procedures
- Fee schedules
- Timeline comparisons

**Use narrative prose for:**
- Detailed analysis
- Statutory interpretation
- Conflict resolution reasoning
- Gap analysis explanations
- Recommendations

---

## EVIDENCE LEVEL NOTATION - MANDATORY

Every factual claim must be tagged with evidence level:

```markdown
**[FACT]** - Explicitly stated in authoritative source (statute/admin code)
Example: "Oklahoma requires 60 hours of Category 1 CME every 3 years [FACT - OAC 435:10-15-1]"

**[INFERENCE - HIGH CONFIDENCE]** - Strongly implied by authoritative source
Example: "Physicians without DEA registration are exempt from pain management CME [INFERENCE - HIGH CONFIDENCE - statute says 'unless licensee does not hold DEA number']"

**[INFERENCE - MEDIUM CONFIDENCE]** - Reasonable interpretation, needs verification
Example: "Board certification may satisfy full CME requirement [INFERENCE - MEDIUM CONFIDENCE - FAQ suggests this but no explicit rule found]"

**[INFERENCE - LOW CONFIDENCE]** - Speculative based on indirect evidence
Example: "Audit rate appears to be ~5% annually [INFERENCE - LOW CONFIDENCE - estimated from board newsletter comment]"

**[CRITICAL GAP]** - Information not found despite thorough search
Example: "Specific documentation retention period not stated [CRITICAL GAP - searched statute, admin code, website, no explicit requirement found]"
```

---

## SOURCE CITATION FORMAT - MANDATORY

Every source must be cited with this format:

**For Statutes:**
```markdown
[STATUTE] Oklahoma Statutes Title 59, Section 495a.1(C)
Source: https://law.justia.com/codes/oklahoma/title-59/section-59-495a-1/
Last Verified: 2026-01-01
Last Amended: November 1, 2019 (per Laws 2019, c. 492, § 3)

Verbatim Text:
"The Board shall require that the licensee receive not less than one (1) hour of education in pain management or one (1) hour of education in opioid use or addiction each year preceding an application for renewal of a license, unless the licensee has demonstrated to the satisfaction of the Board that the licensee does not currently hold a valid federal Drug Enforcement Administration registration number."

Analysis: [Your interpretation]
Evidence Level: [FACT]
```

**For Administrative Code:**
```markdown
[ADMIN_CODE] Oklahoma Administrative Code Title 435, Section 10-15-1
Source: [URL]
Last Verified: 2026-01-01
Effective Date: [Date]

Verbatim Text:
"[Quote]"

Analysis: [Your interpretation]
Evidence Level: [FACT/INFERENCE]
```

**For Board Website:**
```markdown
[BOARD_WEBSITE] Page Title: "CME Requirements for License Renewal"
URL: https://www.okmedicalboard.org/cme-requirements
Last Verified: 2026-01-01
Page Last Updated: [Date per website, if shown]

Content:
[Summary or quote]

Analysis: [Your interpretation]
Evidence Level: [Usually INFERENCE unless quoting official policy]
```

**For Regulatory/Third-Party:**
```markdown
[CME_VENDOR] CE Broker - Oklahoma
URL: https://www.cebroker.com/oklahoma
Last Verified: 2026-01-01

Content:
[Summary]

Evidence Level: [INFERENCE - MEDIUM/LOW depending on source authority]
```

---

## FINAL QUALITY CHECKLIST

Before submitting your research document, verify:

### Completeness Checklist
- [ ] All 15 required sections completed
- [ ] Executive summary written
- [ ] Every mandatory topic searched (pain mgmt, opioid, ethics, etc.)
- [ ] First renewal requirements documented
- [ ] Audit procedures fully researched
- [ ] Fees and penalties documented
- [ ] All gaps identified and prioritized
- [ ] Source validation completed
- [ ] Conflicts resolved or flagged
- [ ] Follow-up recommendations provided

### Source Quality Checklist
- [ ] Primary statute reviewed in full
- [ ] Administrative code searched for all CME sections
- [ ] Board website thoroughly reviewed
- [ ] All sources cited with full URLs
- [ ] Last verified dates included for all sources
- [ ] Evidence levels assigned to all claims
- [ ] Verbatim quotes provided for key requirements
- [ ] No secondary sources used without primary source verification

### Evidence Rigor Checklist
- [ ] No unsupported claims (all have source + evidence level)
- [ ] Conflicts documented with resolution
- [ ] Gaps clearly labeled and prioritized
- [ ] Inferences justified with reasoning
- [ ] Critical gaps have follow-up actions

### Format Checklist
- [ ] Markdown formatting correct
- [ ] Tables properly formatted (Excel-compatible)
- [ ] Headers properly nested (H1, H2, H3)
- [ ] Source codes used consistently
- [ ] Evidence tags used for every claim
- [ ] Document is single .md file
- [ ] File naming: `[STATE]-[LICENSE_TYPE]-renewal-requirements-YYYYMMDD.md`
  Example: `oklahoma-md-renewal-requirements-20260101.md`

---

## SPECIAL INSTRUCTIONS FOR SPECIFIC LICENSE TYPES

### FOR MD RESEARCH:
- Focus on allopathic physician board
- CME typically AMA Category 1/2 or ACCME
- Board certification = ABMS specialty boards
- Check for DO board separation

### FOR DO RESEARCH:
- Focus on osteopathic physician board (if separate) or DO section of unified board
- CME typically AOA Category 1-A, 1-B, 2-A, 2-B OR AMA categories (varies by state)
- Board certification = AOA specialty boards (may also accept ABMS)
- Check for MD board separation
- Document if state requires osteopathic CME or accepts allopathic CME

### FOR NP RESEARCH:
- Focus on Board of Nursing (NOT medical board)
- CME typically called "Contact Hours" or "Continuing Education Units (CEUs)"
- Accreditation typically ANCC or AANP
- May have prescriptive authority requirements separate from renewal
- Document if NP must maintain national certification (ANCC/AANP) for state license
- Check for APRN compact membership (NLC)

---

## RESEARCH WORKFLOW SUMMARY

```
START RESEARCH
    ↓
1. Identify state and license type (MD/DO/NP)
    ↓
2. Check for split MD/DO boards (if MD or DO research)
    ↓
3. PHASE 1: Search statutes
   - Find Medical Practice Act
   - Extract renewal sections
   - Document with [STATUTE] tag
    ↓
4. PHASE 2: Search administrative code
   - Find board rules
   - Extract CME details
   - Document with [ADMIN_CODE] tag
    ↓
5. PHASE 3: Search board website
   - Review all CME/renewal pages
   - Download official documents
   - Document with [BOARD_WEBSITE] tag
    ↓
6. PHASE 4: Search regulatory/third-party
   - FSMB, CE Broker, compacts, etc.
   - Document with appropriate tags
    ↓
7. Cross-validate all sources
   - Flag conflicts
   - Resolve per hierarchy
   - Document resolution
    ↓
8. Identify gaps
   - Classify priority
   - Recommend follow-up
    ↓
9. Compile final document
   - Follow output format
   - Include all sections
   - Apply evidence levels
    ↓
10. Quality check
    - Run through checklist
    - Verify completeness
    ↓
SUBMIT RESEARCH DOCUMENT
```

---

## EXAMPLE OUTPUT SNIPPET

Here's how a completed section should look:

```markdown
## 4. MANDATORY CME TOPICS

### 4.1 Topic Summary Table

| Topic | Hours Required | Frequency | Applies To | Source | Evidence Level |
|-------|----------------|-----------|------------|--------|----------------|
| Pain Management OR Opioid Education | 1 hour | Annual (each year preceding renewal) | DEA holders only | 59 O.S. § 495a.1(C) | [FACT] |
| Medical Marijuana | 2 hours | One-time before registration | Physicians recommending cannabis | OAC 435:10-7-8 | [FACT] |
| Ethics | 3 hours | Per 3-year cycle | All licensees | OAC 435:10-15-1(d) | [FACT] |

### 4.2 Detailed Topic Requirements

#### 4.2.1 Pain Management and Opioid Education

**Requirement:**
[FACT] Oklahoma requires 1 hour of CME in pain management OR 1 hour of CME in opioid use/addiction education annually.

**Source:**
[STATUTE] Oklahoma Statutes Title 59, Section 495a.1(C)
URL: https://law.justia.com/codes/oklahoma/title-59/section-59-495a-1/
Last Verified: 2026-01-01

**Verbatim Statutory Language:**
"The Board shall require that the licensee receive not less than one (1) hour of education in pain management or one (1) hour of education in opioid use or addiction each year preceding an application for renewal of a license, unless the licensee has demonstrated to the satisfaction of the Board that the licensee does not currently hold a valid federal Drug Enforcement Administration registration number."

**Analysis:**
- **Hours:** Minimum 1 hour (statute says "not less than one")
- **Topic Choice:** Pain management OR opioid/addiction (either satisfies)
- **Frequency:** EACH YEAR (not per renewal cycle - this is annual)
- **Timing:** Must be completed in the year PRECEDING renewal application
- **Exemption:** Physicians without valid DEA registration are exempt
- **Evidence:** Exemption requires affirmative demonstration to Board (likely via renewal attestation)

**[INFERENCE - HIGH CONFIDENCE]** Since Oklahoma has a 3-year renewal cycle and this requirement is annual, physicians must complete 3 hours total (1 hour x 3 years) of pain/opioid CME per renewal cycle.

**Approved Providers:**
[CRITICAL GAP] Statute does not specify which CME providers are approved for this topic. Administrative code search revealed no specific approved provider list.

**Recommended Follow-Up:** Check board website for pain management CME course listings or contact board to confirm if any accredited CME on these topics is acceptable.

---

#### 4.2.2 Medical Marijuana Education

[Continue with same detailed format for each topic...]
```

---

## NOTES ON DIFFICULT STATES

Some states have particularly complex or unusual requirements:

**States with Complex Tiered CME:**
- California (risk management hours)
- New York (child abuse, infection control, other mandated topics)
- Texas (ethics, jurisprudence exam)

**States with Unusual Tracking:**
- Florida (CE Broker, universal submission)
- Louisiana (online CME portfolio)

**States with Recent Changes:**
- Check board websites for emergency orders
- COVID-19 waivers (most expired, but verify)
- New opioid education laws (passed 2016-2024)

**For these states:** Spend extra time on board website recent announcements, board meeting minutes, and bulletins.

---

## USER SPECIFICATION CONFIRMATION

Before beginning research, confirm with user:

**Please specify:**
1. **State:** [Which state to research]
2. **License Type:** [MD, DO, or NP]
3. **Special Focus:** [Any particular areas of concern - e.g., "Especially interested in audit procedures"]
4. **Output Filename:** [Preferred filename or use default format]

**Then begin research following the protocol above.**

---

**END OF RESEARCH PROMPT v2.0**
