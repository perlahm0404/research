# State Medical Board Renewal Requirements Research Prompt

**Version:** 2.1.0
**Created:** 2026-01-01
**Updated:** 2026-01-01 (Added Question 14: Medical Marijuana/Cannabis Education)
**Purpose:** Fourth validator for CME rules engine - validates FSMB data against primary state board sources
**Scope:** Renewal requirements ONLY (not initial licensing)
**Gold Standard Reference:** Oklahoma research (OKLAHOMA_FINDINGS.md - 344KB comprehensive)

---

## CRITICAL: Split-Board State Recognition

**Some states have SEPARATE boards for MD and DO physicians with DIFFERENT CME requirements.**

### Split-Board States (Confirmed)
AZ, CA, FL, ME, MI, NV, **OK**, PA, TN, VT, WA, WV

### Research Protocol for Split-Board States

**When researching a split-board state, you MUST**:

1. **Identify BOTH boards**:
   - MD Board (e.g., Oklahoma State Board of Medical Licensure and Supervision)
   - DO Board (e.g., Oklahoma State Board of Osteopathic Examiners)

2. **Research EACH board separately**:
   - Different governing statutes (e.g., OK: 59 O.S. for MD, 62 O.S. for DO)
   - Different administrative code titles
   - Different renewal portals
   - **Potentially drastically different CME requirements** (e.g., OK: 60h/3yr for MD vs 1h/yr prescribing for DO)

3. **Produce TWO deliverables**:
   - `[STATE]-MD-Renewal-Requirements-YYYY-MM-DD.md`
   - `[STATE]-DO-Renewal-Requirements-YYYY-MM-DD.md`

4. **Create comparison table** showing:
   - Total CME hours (MD vs DO)
   - Renewal cycle frequency
   - Topic requirements
   - Category requirements (AMA Category 1 vs AOA Category 1-A)
   - Exemptions (ABMS board cert vs AOA board cert)
   - Portal URLs

**Example: Oklahoma**

| Factor | MD Board (OBMLS) | DO Board (OSBOE) |
|--------|-----------------|-----------------|
| Governing Statute | 59 O.S. § 480-518.1 | 62 O.S. § 620-642 |
| Total CME | 60 Category 1 hrs/3 yrs | 1h prescribing/yr + [TBD] |
| Renewal Cycle | Triennial (3 years) | [TBD] |
| Portal | pay.apps.ok.gov/medlic/md/ | ok.gov/osboe/ |
| CME Tracking | CE Broker | CE Broker |

---

## Scope Limitation: Initial Licensing EXCLUDED

**DO NOT research initial licensing requirements** unless they directly affect renewal:

### ❌ EXCLUDE (Out of Scope)
- Exam requirements (USMLE, COMLEX, NBME, FLEX)
- Medical school accreditation (LCME, ECFMG)
- Postgraduate training years required for initial license
- Background check procedures for new applicants
- Citizenship/visa requirements for initial application
- Application fees and processing timelines

### ✅ INCLUDE (Affects Renewal)
- First renewal grace periods for newly licensed (e.g., Oklahoma: 3 years)
- Residency/fellowship CME credit (e.g., Oklahoma: 50h/year)
- Training exemptions from CME during active residency
- How "newly licensed" is defined (date of initial license vs date CME tracking begins)

**Why**: CREDMATE already has initial licensing rubric. This prompt focuses on **renewal-specific requirements** only.

---

## Research Objectives

Extract and differentiate renewal requirements across **THREE lifecycle phases**:

### Phase 1: Initial Licensure (Pre-License)
**Skip this phase** - already covered in initial licensing rubric.

### Phase 2: First Renewal Cycle
**Research question:** "What CME or other requirements must be met BEFORE the first license renewal?"

**Extract:**
1. Grace periods for newly licensed physicians (e.g., Oklahoma: 3 years from license date)
2. Reduced requirements for first-time renewers
3. One-time requirements (HIV/AIDS, child abuse, human trafficking)
4. Exemptions for recent graduates or residents/fellows
5. Documentation requirements for first renewal
6. When CME tracking begins vs when license was issued

### Phase 3: Ongoing Renewals (Steady-State)
**Research question:** "What are the recurring CME requirements for SUBSEQUENT renewals after the first?"

**Extract:**
1. Total CME hours per cycle
2. Cycle length (years/months)
3. Category requirements (Category 1, AOA 1-A, etc.)
4. Topic-specific mandates:
   - Pain management/opioid education (check state statutes)
   - Healthcare provider rights/responsibilities
   - Ethics
   - Prescribing standards
   - Child abuse recognition
   - Human trafficking awareness
   - Sexual boundary violations
5. Rollover policies (can excess credits carry forward?)
6. Exemptions and alternatives:
   - Board certification/recertification (ABMS, AOA, RCPSC)
   - Active residency/fellowship (credit amount per year)
   - AMA Physician Recognition Award
   - Military deployment
7. Verification requirements:
   - What documentation must be submitted at renewal?
   - What must be retained for audit?
   - Acceptable proof formats (certificates, transcripts, attestation)
8. Audit process:
   - Random audits? For-cause audits? Percentage audited?
   - What triggers an audit?
   - Response timeline when audited
   - Retention period for CME certificates
9. Non-compliance penalties:
   - Late fees
   - License suspension timeline
   - Remediation requirements
   - Reinstatement process

---

## Data Extraction Framework

For EACH requirement found, capture:

### Requirement Details
- **Requirement ID**: [STATE]-[BOARD]-RENEWAL-[NUMBER]
- **Requirement Name**: (e.g., "Total CME Hours", "Pain Management Topic")
- **Type**: `total_hours` | `topic_hours` | `one_time` | `exemption` | `verification` | `audit`
- **Value**: (numeric or descriptive)
- **Period**: `annual` | `biennial` | `triennial` | `one_time` | `per_cycle`
- **Applicable Phase**:
  - First renewal only
  - Ongoing renewals
  - Both
  - Conditional (specify condition)

### Source Validation
- **Primary Source Type**:
  - `STATE_BOARD_WEBSITE` (highest authority for operational requirements)
  - `STATE_STATUTE` (legislative mandate)
  - `STATE_ADMIN_CODE` (regulatory implementation)
  - `BOARD_FAQ` (official guidance)
  - `PORTAL_INSTRUCTIONS` (renewal workflow)
- **Specific URL**: Direct link to page containing requirement
- **Quote**: Exact text from source (for verification)
- **Last Verified Date**: YYYY-MM-DD
- **Cross-Source Congruency Count**: Number of sources agreeing (1-5)
- **Source Congruency Detail**: Pipe-delimited list (e.g., `STATE_BOARD|STATUTE|ADMIN_CODE`)

### Lifecycle Context
- **Applies To**:
  - [ ] Newly licensed (before first renewal)
  - [ ] First renewal cycle
  - [ ] All subsequent renewals
  - [ ] Specific conditions (e.g., DEA holders only, pain clinic operators)

- **Exceptions/Exemptions**:
  - Who is exempt?
  - What alternative compliance methods exist?
  - What documentation proves exemption?
  - Are exemptions permanent or per-cycle?

### Compliance Mechanics
- **How Verified**:
  - Portal attestation (honor system)
  - Certificate upload required
  - Board audit (random or for-cause)
  - Automatic (board checks databases)
- **Audit Trigger**:
  - Random (percentage per year)
  - For-cause (complaint, investigation)
  - Every renewal
  - Stratified (high-risk specialties)
- **Retention Requirement**: How long must proof be kept? (years)
- **Response Timeline**: Days to respond to audit request
- **Non-Compliance Penalty**:
  - Late fee amount
  - License suspension (immediate or grace period)
  - Remediation required
  - Board hearing required

---

## Specific Research Questions (Template)

### Question 1: First Renewal Grace Period
"Do newly licensed [STATE] physicians have a grace period before CME requirements begin? If yes, how long?"

**Search terms**: "newly licensed", "first renewal", "grace period", "initial licensure", "CME requirement begins", "reporting period starts"

**Expected answers**:
- "3 years from date of licensure" (Oklahoma pattern)
- "Begins immediately"
- "First renewal cycle exempt"

### Question 2: Residency/Fellowship Credits
"Are physicians actively in residency or fellowship training exempt from CME requirements? Do completed years of training count toward CME hours?"

**Search terms**: "residency", "fellowship", "training", "CME exemption", "graduate medical education", "postgraduate training credit"

**Expected answers**:
- "50 hours per completed year" (Oklahoma pattern)
- "Fully exempt during training"
- "No special credit"

### Question 3: One-Time vs Recurring Topics
For each topic requirement (pain management, healthcare provider rights, HIV/AIDS, child abuse, human trafficking):
- "Is this required every renewal cycle or only once?"
- "Does this apply to first-time renewers or only subsequent renewals?"
- "Does this requirement sunset or remain permanent?"

**Search terms**: "[TOPIC]", "one-time", "initial license", "first renewal only", "recurring requirement"

### Question 4: Verification Methods
"What documentation must physicians submit to prove CME completion?"
"What are acceptable alternatives to CME certificates?"

**Search terms**: "CME verification", "acceptable proof", "documentation required", "AMA Physician Recognition Award", "board certification", "MOC", "maintenance of certification"

**Expected formats**:
- AMA PRA certificate
- ABMS board certification obtained during period
- Individual CME certificates
- CME transcript from provider
- Attestation only

### Question 5: Audit Process
"How does the [STATE] Medical Board audit CME compliance?"
"What percentage of physicians are audited annually?"
"What must physicians retain for potential audit?"

**Search terms**: "audit", "CME verification", "random selection", "compliance review", "record retention"

**Expected elements**:
- Random audit percentage (e.g., "10% annually")
- For-cause triggers (complaint, investigation, pattern)
- Response timeline (e.g., "30 days to submit documentation")
- Retention period (e.g., "3 years", "current cycle + 1 year")

### Question 6: DEA-Conditional Requirements
"For requirements that only apply to DEA registrants (e.g., pain management CME), how is DEA status verified?"
"When does this requirement begin - immediately upon DEA registration or at next renewal?"
"What if DEA registration is obtained mid-cycle?"

**Search terms**: "DEA registration", "controlled substance", "prescribing authority", "pain management", "opioid education"

### Question 7: Rollover Policy
"Can [STATE] physicians carry forward excess CME credits from one cycle to the next?"
"If yes, what is the maximum rollover amount?"
"Do topic-specific requirements allow rollover?"

**Search terms**: "rollover", "carryover", "excess credits", "surplus CME", "credit banking"

**Expected answers**:
- "No rollover allowed" (most common)
- "Up to [X] hours may carry forward"
- "Total hours rollover allowed, topics cannot roll over"

### Question 8: Topic-Specific Statutory Requirements
"What state statutes mandate specific CME topics beyond the board's general requirements?"

**Search state statute database for**:
- Pain management / opioid prescribing education
- Healthcare provider rights/responsibilities
- Implicit bias / cultural competency
- Domestic violence / human trafficking
- Child abuse recognition / reporting
- Sexual boundary violations / ethics
- Telehealth / telemedicine standards

**For each topic found, extract**:
- Statute citation (e.g., "59 O.S. § 495a.1")
- Required hours
- Frequency (annual, biennial, one-time)
- Applicability (all licensees vs conditional)
- Effective date
- Sunset provision (if any)

### Question 9: Controlled Substance Prescribing Context
"What are the controlled substance prescribing requirements that create the CONTEXT for pain management CME?"

**Extract**:
- Acute pain opioid supply limits (days)
- Chronic pain documentation requirements (treatment plan, agreement, screening)
- Telemedicine restrictions for controlled substances
- Prescription monitoring program (PMP) mandatory use
- Patient-provider agreement requirements
- Urine/serum screening requirements

**Why this matters**: Pain management CME is not just an isolated requirement - it's part of a comprehensive prescribing framework. Rules engine needs this context.

### Question 10: Lapsed License Reinstatement
"What CME requirements apply when reinstating a lapsed license?"

**Search terms**: "reinstatement", "lapsed license", "expired license", "inactive status", "CME makeup"

**Extract lapse timeline with status**:

| Lapse Duration | License Status | Can Practice? | Renewal Path | CME Required | Fee |
|----------------|----------------|---------------|--------------|--------------|-----|
| Before deadline | Active | Yes | Standard renewal | Per cycle | Standard |
| 1-60 days late | Inactive | No | Late renewal | Per cycle | Late fee |
| >60 days | Suspended | No | Reinstatement | Makeup? | Varies |
| >1 year, <3 years | Lapsed | No | Formal reinstatement | Lapsed period? | TBD |
| >3 years | Expired | No | New application | Full requirements | Full fee |

**Oklahoma Pattern (from OKLAHOMA_FINDINGS.md)**:
- **<1 year**: Automatic renewal, CME verification required, no background check
- **1-3 years**: Formal reinstatement, Board discretion on background/reexam, CME makeup for lapsed period
- **>3 years**: New application required, treated as initial applicant

---

### Question 11: DO Board Differences (Split-Board States Only)

**Research question**: "How do DO physician CME requirements differ from MD requirements in this state?"

**When to use**: ONLY for split-board states (AZ, CA, FL, ME, MI, NV, OK, PA, TN, VT, WA, WV)

**Extract**:

1. **Identify DO Board**:
   - Board name (e.g., Oklahoma State Board of Osteopathic Examiners)
   - Governing statute (e.g., 62 O.S. § 620-642)
   - Administrative code title
   - Website URL
   - Renewal portal URL

2. **Compare Requirements** (MD vs DO):
   - Total CME hours per cycle
   - Renewal cycle frequency (annual vs biennial vs triennial)
   - Category requirements (AMA Category 1 vs AOA Category 1-A)
   - Topic-specific mandates (proper prescribing courses common for DOs)
   - Exemptions (ABMS board cert vs AOA board cert)

3. **Document Prescribing-Focused CME**:
   - DO boards often have separate opioid/controlled substance education requirements
   - Example: Oklahoma DO requires 1h/year "Approved Proper Prescribing Courses"
   - May use different terminology than MD boards

4. **Note CME Tracking Systems**:
   - Same system? (e.g., both use CE Broker)
   - Different requirements within same tracking system?

**Expected differences**:
- DO boards may require AOA-approved CME
- Different total hour requirements
- Different renewal cycles
- Prescribing education emphasized more for DOs

---

### Question 12: Renewal Fees and Timelines

**Research question**: "What are the renewal fees, late fees, and renewal timeline?"

**Extract**:

**Fees**:
- Standard renewal fee amount
- Late renewal fee (if different)
- Late renewal grace period (days after expiration)
- Reinstatement fees (by lapse duration)
- Verification letter fee (if applicable)

**Timeline**:
- Renewal notice sent (days before expiration)
- Online portal opens (days before expiration)
- Renewal deadline (relative to license expiration)
- Late renewal deadline (days after expiration)
- License status during each period (active, inactive, suspended)

**Oklahoma Example**:
| Fee Type | Amount | Notes |
|----------|--------|-------|
| Standard Renewal | $200 | On-time renewal |
| Late Renewal | $350 | Within 60 days of expiration |
| Verification Letter | $25 | Official verification |

**Timeline**: Portal opens 60 days before expiration, license becomes inactive immediately after deadline, suspended if >60 days past deadline.

---

### Question 13: CME Tracking Systems

**Research question**: "What CME tracking systems does the board use or integrate with?"

**Extract**:
- Official CME tracking system (CE Broker, ACCME, other)
- Integration URL
- Mandatory vs optional use
- Auto-reports to board? (or physician must attest separately)
- Portal instructions for accessing CME transcript

**Oklahoma Example**:
- **System**: CE Broker
- **URL**: https://cebroker.com/OK/plans
- **Usage**: Both MD and DO boards use CE Broker
- **Integration**: Official tracking system

**Why this matters**: If board uses automated CME tracking, renewal may be simplified. If not, physicians must retain paper certificates.

---

### Question 14: Medical Marijuana/Cannabis Education (State-Specific)

**When to research**: States with medical/recreational cannabis programs (AK, AZ, AR, CA, CO, CT, DE, FL, HI, IL, MA, MD, ME, MI, MN, MO, MT, ND, NH, NJ, NM, NV, NY, OH, **OK**, OR, PA, RI, SD, UT, VT, VA, WA, WV)

**Research question**: "Does the state require CME on medical marijuana, cannabis therapeutics, or cannabis recommendation before physicians can provide medical marijuana recommendations?"

**Extract**:
- Mandatory cannabis/medical marijuana CME requirement (yes/no)
- Required hours (if applicable)
- Frequency (one-time, annual, triennial)
- When required (before first recommendation, at every renewal, other)
- Exemptions (if any)
- Effective date of requirement
- Source statute/regulation (critical - cannabis laws change frequently)

**Oklahoma Example (2026)**:
- **Requirement**: Medical marijuana education required before providing recommendations
- **Status**: NEW requirement (implemented 2026)
- **Hours**: Research specific hour requirement from board website
- **Timing**: Before issuing medical marijuana recommendations
- **Authority**: Oklahoma State Board of Medical Licensure and Supervision

**Why this matters**:
- Cannabis education requirements are **emerging** (many states added 2020-2026)
- NOT consistently in FSMB documents (too new/state-specific)
- Non-compliance can result in loss of authority to recommend medical marijuana
- Requirements vary significantly: some states require initial education only, others require ongoing CME

**Search locations**:
- State board Medical Marijuana section
- State cannabis/marijuana program regulations (often separate from medical board)
- Recent legislative updates (2020-2026 timeframe)
- Controlled substance prescribing guidelines

---

## Output Format

Produce a **structured YAML document** for each state:

```yaml
state: "[STATE CODE]"
board_code: "[BOARD CODE]" # e.g., OK-M, OK-O, CA-M
board_name: "[FULL BOARD NAME]"
research_date: "YYYY-MM-DD"
researcher: "[NAME/AGENT]"

# ===== LIFECYCLE PHASES =====
lifecycle_phases:
  first_renewal:
    grace_period_enabled: true/false
    grace_period_years: [NUMBER or null]
    grace_period_description: "[e.g., CME begins 3 years from license date]"
    one_time_requirements:
      - topic: "[e.g., HIV/AIDS]"
        hours: [NUMBER]
        statute: "[CITATION]"
        source_url: "[URL]"
        quote: "[EXACT TEXT]"

  ongoing_renewals:
    renewal_period_years: [NUMBER]
    renewal_frequency: "[annual|biennial|triennial]"

# ===== CME REQUIREMENTS =====
cme_requirements:
  total_hours:
    value: [NUMBER]
    period_years: [NUMBER]
    category_requirements:
      ama_category_1_required: true/false
      ama_category_1_minimum_hours: [NUMBER or null]
      aoa_category_1a_accepted: true/false
      exclusive: true/false # true = ALL must be Category 1

  topic_requirements:
    - topic_id: "pain_management_opioid"
      topic_name: "Pain Management and Opioid Education"
      hours: [NUMBER]
      period_years: [NUMBER]
      lifecycle_phase: "[first_renewal_only|ongoing|both]"
      condition: "[DEA_holder|all_licensees|pain_clinic_operator]"
      statute: "[CITATION]"
      admin_code: "[CITATION]"
      source_url: "[URL]"
      quote: "[EXACT STATUTE TEXT]"
      primary_source_type: "[STATE_STATUTE|STATE_ADMIN_CODE|STATE_BOARD_WEBSITE]"
      cross_source_congruency_count: [1-5]
      source_congruency_detail: "[SOURCE1|SOURCE2|SOURCE3]"

    - topic_id: "health_care_provider_rights"
      topic_name: "Healthcare Provider Rights and Responsibilities"
      hours: [NUMBER]
      period_years: [NUMBER]
      statute: "[CITATION]"
      source_url: "[URL]"
      quote: "[EXACT TEXT]"
      primary_source_type: "[TYPE]"
      cross_source_congruency_count: [NUMBER]
      source_congruency_detail: "[SOURCES]"

# ===== EXEMPTIONS & ALTERNATIVES =====
exemptions:
  board_certification:
    accepted: true/false
    boards_accepted: ["ABMS", "AOA", "RCPSC"]
    exemption_scope: "[full_cme|partial|none]"
    exemption_period: "[during_certification_year|entire_cycle]"
    documentation_required: "[certificate|transcript|attestation]"
    notes: "[e.g., Current certification/MOC satisfies entire CME requirement]"

  residency_fellowship:
    accepted: true/false
    credit_hours_per_year: [NUMBER or null]
    exemption_type: "[full_exemption|credit_award]"
    documentation_required: "[program_verification|completion_certificate]"

  ama_physician_recognition_award:
    accepted: true/false
    exemption_scope: "[full_cme|partial]"
    validity_period: "[current|during_award_year]"

# ===== VERIFICATION & AUDIT =====
verification:
  at_renewal:
    method: "[attestation|certificate_upload|automatic|none]"
    documentation_required: "[yes|no|conditional]"
    portal_upload_required: true/false

  audit_process:
    audit_type: "[random|for_cause|both|stratified]"
    random_audit_percentage: [NUMBER or null]
    random_audit_frequency: "[annual|biennial|per_cycle]"
    for_cause_triggers:
      - "[complaint]"
      - "[investigation]"
      - "[pattern_of_violations]"
    audit_response_timeline_days: [NUMBER]
    audit_documentation_required:
      - "[CME certificates]"
      - "[transcripts]"
      - "[board_certification_proof]"

  retention_requirements:
    retention_period_years: [NUMBER]
    retention_period_description: "[e.g., Current cycle plus 1 year]"
    acceptable_formats: ["paper", "electronic"]
    storage_location: "[physician_responsibility|board_database|portal]"

# ===== ROLLOVER POLICY =====
rollover:
  total_hours_rollover:
    allowed: true/false
    maximum_hours: [NUMBER or null]
    rollover_period: "[to_next_cycle|indefinite]"

  topic_hours_rollover:
    allowed: true/false
    restrictions: "[topic_hours_do_not_rollover|same_as_total]"

# ===== NON-COMPLIANCE =====
non_compliance:
  late_renewal:
    grace_period_days: [NUMBER or null]
    late_fee_amount: "[AMOUNT or varies]"
    license_status_during_grace: "[active|inactive|suspended]"

  failure_to_complete_cme:
    penalty: "[suspension|remediation|board_hearing]"
    remediation_options:
      - "[complete_outstanding_hours]"
      - "[attend_board_approved_course]"
      - "[probation_with_monitoring]"
    automatic_suspension: true/false
    hearing_required: true/false

# ===== REINSTATEMENT (LAPSED LICENSE) =====
reinstatement:
  lapsed_less_than_1_year:
    process: "[automatic_renewal|simple_reinstatement]"
    cme_required: true/false
    cme_makeup_period: "[lapsed_period|current_cycle_only]"
    background_check_required: false
    reexamination_required: false

  lapsed_1_to_3_years:
    process: "[formal_reinstatement|board_discretion]"
    cme_required: true/false
    cme_makeup_period: "[lapsed_period|proportional]"
    background_check_required: "[may_be_required|required|not_required]"
    reexamination_required: "[may_be_required|required|not_required]"

  lapsed_more_than_3_years:
    process: "[new_application|full_reapplication]"
    cme_required: true/false
    background_check_required: true
    reexamination_required: true
    treated_as_initial_applicant: true/false

# ===== CONTROLLED SUBSTANCE CONTEXT =====
controlled_substance_context:
  prescribing_limits:
    acute_pain_opioid_supply_limit_days: [NUMBER or null]
    chronic_pain_documentation_required: true/false

  prescribing_requirements:
    patient_provider_agreement_required: true/false
    urine_screening_required_high_risk: true/false
    treatment_plan_required: true/false
    prescription_monitoring_program_mandatory: true/false

  telemedicine_restrictions:
    opioid_prescribing_allowed: true/false
    benzodiazepine_prescribing_allowed: true/false
    controlled_substance_general_restrictions: "[description]"

  context_notes: |
    [Explain how controlled substance prescribing requirements create the
    context for pain management/opioid CME. Why does this CME exist? What
    prescribing behaviors is it meant to inform?]

# ===== SOURCE CITATIONS =====
sources:
  primary_sources:
    - source_type: "STATE_BOARD_WEBSITE"
      url: "[URL]"
      section: "[Section name/page]"
      last_verified: "YYYY-MM-DD"

    - source_type: "STATE_STATUTE"
      citation: "[Full citation]"
      url: "[URL to statute database]"
      last_verified: "YYYY-MM-DD"

    - source_type: "STATE_ADMIN_CODE"
      citation: "[Full citation]"
      url: "[URL]"
      last_verified: "YYYY-MM-DD"

  secondary_sources:
    - source_type: "BOARD_FAQ"
      url: "[URL]"
      last_verified: "YYYY-MM-DD"

    - source_type: "PORTAL_INSTRUCTIONS"
      url: "[URL]"
      last_verified: "YYYY-MM-DD"

# ===== FSMB COMPARISON =====
fsmb_comparison:
  fsmb_total_hours_match: true/false
  fsmb_period_years_match: true/false
  discrepancies:
    - field: "[FIELD_NAME]"
      fsmb_value: "[VALUE]"
      state_board_value: "[VALUE]"
      correct_value: "[VALUE]"
      severity: "[CRITICAL|HIGH|MEDIUM|LOW]"

  missing_in_fsmb:
    - requirement: "[e.g., First renewal grace period]"
      state_board_value: "[VALUE]"
      impact: "[Description of rules engine impact]"

# ===== GAPS & AMBIGUITIES =====
research_gaps:
  - gap: "[Description of unanswered question]"
    attempted_sources: ["[SOURCE1]", "[SOURCE2]"]
    recommendation: "[How to resolve - contact board, FOIA request, etc.]"
    priority: "[CRITICAL|HIGH|MEDIUM|LOW]"

# ===== RENEWAL FEES & TIMELINES =====
renewal_fees:
  standard_renewal_fee: "[AMOUNT]"
  late_renewal_fee: "[AMOUNT]"
  late_renewal_grace_period_days: [NUMBER or null]
  reinstatement_fee: "[varies_by_duration|fixed_amount]"
  verification_letter_fee: "[AMOUNT or null]"

  timeline:
    renewal_notice_sent_days_before: [NUMBER]
    portal_opens_days_before: [NUMBER]
    license_status_after_deadline: "[inactive|suspended]"
    late_renewal_cutoff_days: [NUMBER or null]

# ===== CME TRACKING SYSTEM =====
cme_tracking_system:
  system_name: "[CE Broker|ACCME|Board-Specific|None]"
  system_url: "[URL or null]"
  integration_type: "[mandatory|optional|recommended]"
  auto_reports_to_board: true/false
  portal_instructions: "[URL or description]"

# ===== RESEARCH STATUS & COMPLETENESS =====
research_status:
  completion_percentage: [0-100]
  completion_criteria:
    lifecycle_phases: "[complete|partial|missing]"
    total_cme_hours: "[complete|partial|missing]"
    topic_requirements: "[complete|partial|missing]"
    audit_process: "[complete|partial|missing]"
    exemptions: "[complete|partial|missing]"
    rollover: "[complete|partial|missing]"
    non_compliance: "[complete|partial|missing]"
    reinstatement: "[complete|partial|missing]"
    controlled_substance_context: "[complete|partial|missing]"
    fees_timeline: "[complete|partial|missing]"

  next_steps:
    - "[Specific research action needed]"
    - "[Source to access]"
    - "[Contact if needed]"

# ===== NOTES =====
notes: |
  [Any additional context, state-specific quirks, historical changes,
  pending legislation, or implementation nuances that don't fit above categories]
```

---

## Research Gap Documentation & Tracking

### Using Markdown Checkboxes

Flag incomplete sections with markdown checkboxes in your narrative sections:

```markdown
### Topic Requirements

- [x] Total hours confirmed: 60h/3yr (STATE_BOARD + STATUTE)
- [ ] Pain management CME (59 O.S. 495a.1) - **CRITICAL GAP** - Need statute text
- [ ] Healthcare provider rights (63 O.S. 3162) - **HIGH GAP** - Need hours/frequency
- [x] Rollover policy confirmed: Not allowed (STATE_BOARD)
- [ ] Audit retention period - **MEDIUM GAP** - Need admin code section
```

### Gap Priority Levels

- **CRITICAL GAP**: Affects core CME calculation (total hours, topic hours, exemptions)
  - *Blocks rules engine deployment*
  - *Must resolve before implementation*

- **HIGH GAP**: Affects compliance validation (audit procedures, verification methods, penalties)
  - *Impacts user experience*
  - *Should resolve before production*

- **MEDIUM GAP**: Affects edge cases (rollover, reinstatement, special licenses)
  - *Document workaround*
  - *Can resolve post-launch*

- **LOW GAP**: Nice-to-have context (board statistics, historical changes)
  - *Optional*
  - *No impact on rules engine*

---

## Two-File Research Workflow

### Master Findings File (Narrative)

**Purpose**: Capture ALL research in narrative format, including context and out-of-scope details

**File**: `[STATE]_FINDINGS.md`
**Example**: `OKLAHOMA_FINDINGS.md` (344KB comprehensive)

**Contents**:
- Initial licensing requirements (for context)
- Renewal requirements (comprehensive)
- Controlled substance prescribing framework (full detail)
- Lapsed license reinstatement (all tiers)
- Narrative explanations with full quotes
- Research notes and ambiguities

**Why**: Preserves research context, allows discovery of edge cases, reference for future updates

---

### Structured YAML Deliverable (Rules Engine Input)

**Purpose**: Extract ONLY renewal requirements in structured format for rules engine

**File**: `[STATE]-[BOARD]-Renewal-Requirements-Comprehensive-YYYY-MM-DD.md`
**Example**: `Oklahoma-MD-Renewal-Requirements-Comprehensive-2026-01-01.md`

**Contents**:
- YAML data block (structured, machine-readable)
- Renewal-focused sections only
- Gap flags with checkboxes
- Completion percentage tracking
- FSMB comparison

**Why**: Direct rules engine import, version control, completeness tracking

---

### Optional Quick Reference (Summary)

**Purpose**: Quick-lookup table for developers/users

**File**: `[STATE]-physician-license-renewal.md`
**Example**: `oklahoma-physician-license-renewal.md` (4.9KB)

**Contents**:
- Summary tables (fees, hours, timeline)
- Checklist format
- No detailed sourcing
- Links to full research

**Why**: Fast reference without reading full research

---

## Workflow: Narrative → Structured → Summary

1. **Gather everything** → Create `[STATE]_FINDINGS.md`
   - Don't filter, capture all details
   - Include initial licensing for context
   - Full prescribing framework
   - Narrative format, quotes embedded

2. **Extract renewal requirements** → Populate `[STATE]-[BOARD]-Renewal-Requirements-YYYY-MM-DD.md`
   - Use YAML template from this prompt
   - Only renewal-specific content
   - Flag gaps with checkboxes
   - Calculate completion percentage

3. **Create quick reference** (optional) → `[STATE]-physician-license-renewal.md`
   - Table format
   - Core facts only (hours, fees, timeline)
   - Link to full structured deliverable

---

## Research Sources (State-Specific)

### Primary Sources (REQUIRED - Minimum 2 per requirement)

1. **State Medical Board Website**
   - URL: [State board official website]
   - Focus: Renewal section, CME requirements, FAQs, licensee resources
   - **Highest authority** for operational requirements

2. **Board Online Portal Instructions**
   - Look for: Renewal workflow, attestation questions, upload requirements
   - Screenshots if needed to document portal requirements

3. **State Administrative Code**
   - Title/Chapter governing medical licensure
   - Specific sections on CME, renewal, reinstatement
   - URL: State's administrative code database

4. **State Statutes**
   - Legislative mandates for CME topics (pain management, etc.)
   - Professional regulation chapter
   - URL: State legislature website

5. **Board FAQs / Guidance Documents**
   - Official interpretations of regulations
   - Common questions about CME compliance

### Secondary Sources (CORROBORATION)

6. **State Medical Association Resources**
   - Member guidance on CME compliance
   - Advocacy updates on legislation

7. **FSMB State CME Comparison**
   - For validation only - NOT primary source
   - Use to identify discrepancies

8. **Board Meeting Minutes**
   - Policy changes, new interpretations
   - Available on board website

---

## Quality Standards

### Minimum Requirements
- ✅ Minimum **2 sources** per requirement (primary + corroboration)
- ✅ Direct **quotes** for all regulatory language
- ✅ **URL verification** (ensure links are current, not broken)
- ✅ **Date stamp** all research (YYYY-MM-DD)
- ✅ Flag **any conflicting information** across sources
- ✅ Note if requirement is **IMPLIED vs EXPLICIT** in source text

### Cross-Source Congruency Validation
For each requirement, track which sources agree:

```yaml
cross_source_congruency_count: 3
source_congruency_detail: "STATE_BOARD|STATUTE|ADMIN_CODE"
```

**Congruency scoring**:
- **5 sources agree** = Highest confidence
- **3-4 sources agree** = High confidence
- **2 sources agree** = Medium confidence
- **1 source only** = Low confidence - flag for follow-up
- **0 sources (inferred)** = Assumption - must validate

### Conflict Resolution
When sources disagree:

```yaml
conflicts:
  - field: "total_hours"
    sources:
      - source: "STATE_BOARD_WEBSITE"
        value: 60
        url: "[URL]"
      - source: "FSMB"
        value: 50
        url: "[URL]"
    resolution:
      correct_value: 60
      authority: "STATE_BOARD_WEBSITE"
      rationale: "State board website is primary authority for operational requirements"
```

---

## Deliverable

Produce a **structured markdown document** titled:
```
[STATE]-[BOARD_CODE]-Renewal-Requirements-Comprehensive-YYYY-MM-DD.md
```

**Example**: `Oklahoma-MD-Renewal-Requirements-Comprehensive-2026-01-01.md`

### Document Structure

```markdown
# [STATE] [BOARD TYPE] Renewal Requirements - Comprehensive Research

**Board Code**: [CODE]
**Board Name**: [FULL NAME]
**Research Date**: YYYY-MM-DD
**Researcher**: [NAME]
**Last Verified**: YYYY-MM-DD

---

## Executive Summary

[3-5 bullet summary of key findings, unique requirements, FSMB discrepancies]

---

## YAML Data Block

[Full YAML output as specified in Output Format section above]

---

## Detailed Findings

### Section 1: Lifecycle Phases
[Narrative explanation of first renewal vs ongoing, with quotes from sources]

### Section 2: CME Requirements
[Detailed breakdown of total hours, categories, topics with source citations]

### Section 3: Verification & Audit
[How compliance is verified, audit process, retention requirements]

### Section 4: Exemptions & Alternatives
[Board certification, residency, AMA PRA details]

### Section 5: Controlled Substance Context
[How prescribing requirements inform CME mandates]

### Section 6: Non-Compliance & Reinstatement
[Penalties, remediation, lapsed license pathways]

---

## Source Comparison Matrix

| Requirement | STATE_BOARD | STATUTE | ADMIN_CODE | FSMB | Congruency |
|-------------|-------------|---------|------------|------|------------|
| Total Hours | 60 | 60 | 60 | 60 | 4/4 ✅ |
| Grace Period | 3 years | Not mentioned | Not mentioned | Not mentioned | 1/4 ⚠️ |
| Pain CME | 1h/yr DEA | 1h/yr DEA | 1h/yr DEA | Not mentioned | 3/4 ⚠️ |

---

## FSMB Discrepancies

[List all differences between FSMB document and state board sources, with severity ratings]

---

## Research Gaps

[Questions that remain unanswered, with recommended follow-up actions]

---

## Recommendations for Rules Engine

[Specific guidance on how to implement these requirements in the rules engine, including edge cases and decision trees]

---

## Appendix: Source Documents

[Full citations, URLs, access dates, screenshots if needed]
```

---

## State-Specific Research Notes

### Oklahoma (Example - Already Researched)
- **Statutes to verify**: 59 O.S. § 495a.1 (pain CME), 63 O.S. § 3162 (healthcare rights)
- **Admin code**: OAC 435:10-15-1 (CME requirements), OAC 435:10-7-11 (controlled substances)
- **Unique features**: 3-year grace for newly licensed, 50h/year residency credit, random annual audits
- **FSMB gaps**: Grace period, residency credit, audit process not in FSMB document

### Pennsylvania (Complex State - Pending Research)
- **Known complexity**: Act 53 requirements, detailed licensing guide
- **Bureau**: PA DOS Bureau of Professional and Occupational Affairs
- **Focus**: Split-board MD/DO requirements, any unique reciprocity rules

### Louisiana (Complex State - Pending Research)
- **Known complexity**: Unique reciprocity rules, split licensing requirements
- **Board**: Louisiana State Board of Medical Examiners
- **Focus**: Any special CME topic mandates, Hurricane Katrina legacy exemptions

---

## Implementation Workflow

### Step 1: Select Target State
- Prioritize based on: CREDMATE user concentration, FSMB discrepancies, split-board states

### Step 2: Gather Primary Sources
- Access state board website renewal section
- Download all CME guidance PDFs
- Bookmark statute/admin code sections
- Screenshot portal if no public documentation

### Step 3: Extract Requirements
- Use YAML template above
- Document every field with source citation
- Flag any ambiguities or conflicts

### Step 4: Cross-Validate
- Compare at least 2 sources per requirement
- Note congruency count and detail
- Resolve conflicts with hierarchy (statute > admin code > board website > FSMB)

### Step 5: Compare to FSMB
- Load FSMB CME overview for state
- Identify discrepancies
- Rate severity (CRITICAL for hours/periods, HIGH for topics, MEDIUM for process)

### Step 6: Document Gaps
- List unanswered questions
- Recommend follow-up research method
- Prioritize by rules engine impact

### Step 7: Generate Deliverable
- Produce markdown document per template
- Include YAML data block
- Add narrative explanations with quotes
- Provide rules engine recommendations

---

## Success Criteria

A research deliverable is **complete** when:

✅ All YAML fields populated or marked `null` with explanation
✅ Minimum 2 sources per requirement
✅ Direct quotes for all regulatory requirements
✅ Cross-source congruency calculated for all fields
✅ FSMB comparison completed with discrepancies documented
✅ Research gaps identified with follow-up recommendations
✅ Rules engine implementation guidance provided
✅ All URLs verified as current and accessible
✅ Document dated and researcher identified

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-01 | Initial prompt created based on Oklahoma research findings and FSMB gap analysis |
| 2.0.0 | 2026-01-01 | **Oklahoma Gold Standard Integration**: Split-board recognition (CRITICAL), scope exclusion (initial licensing), DO-specific Question 11, fees & timeline Question 12, CME tracking Question 13, completion percentage tracking in YAML, gap flagging with markdown checkboxes, two-file workflow documentation (narrative + structured + summary), lapsed license 3-tier table (Question 10 enhanced), renewal fees YAML section, CME tracking system YAML section, research status tracking YAML section |

---

*This prompt serves as the fourth validator in the CREDMATE CME accuracy framework, validating FSMB data against primary state sources to achieve 100% rules engine accuracy.*