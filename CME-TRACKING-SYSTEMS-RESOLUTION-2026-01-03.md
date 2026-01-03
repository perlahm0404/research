# CME Tracking Systems Resolution - 18 States
## Research Initiative to Document CME Tracking and Reporting Methods

**Date:** January 3, 2026
**Researcher:** Claude Code (Sonnet 4.5)
**Project:** Resolve CME tracking system gaps across 18 states with unclear or undocumented tracking systems
**Status:** MANUAL RESEARCH REQUIRED (Web access unavailable)

---

## EXECUTIVE SUMMARY

### Problem Statement

The comprehensive audit identified that **18 states have gaps in CME tracking system documentation** (30% of corpus). This gap prevents full understanding of how physicians report CME compliance, whether automatic reporting exists from CME providers, and whether states use third-party platforms like CE Broker.

**Impact on Rules Engine:** MEDIUM-HIGH
- Cannot build CE Broker API integration without knowing which states use it
- Affects user experience design (manual entry vs automatic sync)
- Influences "CME transcript import" feature prioritization
- Determines audit preparation workflows

### Target States (18 States with Unclear/Undocumented Tracking)

**High Priority (Large Population States):**
1. Maryland (MD)
2. Massachusetts (MA)
3. Ohio (OH)
4. Minnesota (MN)
5. Kentucky (KY)
6. Louisiana (LA)

**Medium Priority:**
7. Connecticut (CT)
8. New Hampshire (NH)
9. New Mexico (NM)
10. Kansas (KS)
11. Mississippi (MS)
12. Nebraska (NE)

**Lower Priority:**
13. Alaska (AK)
14. Arkansas (AR)
15. Delaware (DE)
16. District of Columbia (DC)
17. Iowa (IA)
18. North Dakota (ND)

### Research Deliverable

For each state, document:
- **System name:** CE Broker, board-operated portal, other vendor, or attestation only
- **System URL:** Direct link to CME tracking portal (if applicable)
- **Reporting method:** Automatic provider reporting, manual physician entry, or attestation only
- **Evidence citation:** Board website URL + relevant quote with access date
- **Update needed:** Identify which existing research document needs Section 12 update

---

## METHODOLOGY

### Research Strategy (Manual Process Required)

Since web access tools are unavailable, this document provides a **manual research framework** for each state. Follow this process:

#### Step 1: Check CE Broker State List
- Visit: https://www.cebroker.com/
- Navigate to "States We Serve" or search for each target state
- Document whether state medical board is listed as a CE Broker partner
- **Evidence:** Screenshot or quote from CE Broker website

#### Step 2: Board Website - CME/Renewal Section
- Visit state medical board website (URLs provided below)
- Navigate to: "Continuing Education" or "License Renewal" section
- Search for keywords: "CME tracking," "CME portal," "reporting," "CE Broker"
- Look for:
  - Named tracking system or vendor
  - Portal login links
  - Instructions for CME reporting at renewal
  - FAQs about CME verification

#### Step 3: Board Website - Renewal Instructions
- Find downloadable renewal instructions (PDF or webpage)
- Look for section on "How to Report CME"
- Document: attestation only vs certificate upload vs system integration

#### Step 4: Statute/Regulation Search (If Time Permits)
- Search state administrative code for:
  - "CME tracking"
  - "continuing education documentation"
  - "CME provider reporting"
- Note: Tracking systems usually in board policy, not statute

### Quality Standards

**Minimum Requirements per State:**
- **2+ sources:** Board website + at least one other source (CE Broker, renewal instructions, statute)
- **Exact URLs:** Include full URL and access date for all citations
- **Direct quotes:** Copy relevant text from board website (not paraphrased)
- **Documentation:** If not found after 3 search attempts, mark as "Not Found - Manual Contact Required"

### Evidence Notation

Use standard notation:
- **[FACT - BOARD]** - Information from official state board website
- **[FACT - VENDOR]** - Information from CE Broker or other vendor website
- **[INFERENCE - HIGH]** - Strong inference based on renewal portal features
- **[CRITICAL GAP]** - Not documented after thorough search

---

## KNOWN CME TRACKING SYSTEMS (From Existing Research)

### States Using CE Broker (Confirmed)

#### 1. Alabama - CE Broker (Inferred, Not Mandated)
- **Status:** Voluntary use, not mandated
- **Evidence:** Alabama document notes physician self-management (no automatic reporting)
- **Source:** /Users/tmac/research/AL-MD-Renewal-Requirements-Narrative-2026-01-02.md (line 357)
- **System:** Physicians maintain own documentation; no CE Broker integration confirmed

#### 2. Arizona - CE Broker (Recommended, Not Required)
- **Status:** Free, optional, recommended by board
- **Evidence:** "CE Broker is the board's recommended system for CME tracking and documentation"
- **URL:** https://courses.cebroker.com/search/az
- **Features:** Free account, auto-reporting from ACCME providers, transcript generation
- **Source:** /Users/tmac/research/Arizona-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 336-350)

#### 3. Florida (MD & DO) - CE Broker (Mandatory)
- **Status:** Mandatory electronic CME tracking through CE Broker
- **Evidence:** "Florida Department of Health verifies licensee compliance...through the electronic tracking system, powered by CE Broker"
- **URL:** https://www.cebroker.com
- **Integration:** FLHealthSource renewal portal pulls CME data from CE Broker automatically
- **Reporting:** Automatic from many CME providers; manual upload for non-integrated providers
- **Source:** /Users/tmac/research/Florida-DO-Renewal-Requirements-Narrative-2026-01-02.md (lines 512-526)

#### 4. Georgia - CE Broker (Voluntary, Partnership)
- **Status:** Voluntary participation, board partnership since August 2023
- **Evidence:** "The Georgia Composite Medical Board has engaged the services of CE Broker...Participation in CE Broker is NOT required"
- **URL:** https://help.cebroker.com/hc/en-us/articles/15226511627540-Georgia-Composite-Medical-Board
- **Features:** Free account available; 55,000+ professionals use the platform
- **Source:** /Users/tmac/research/GA-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 439-471)

#### 5. Oklahoma (MD & DO) - CE Broker (Official Tracking System)
- **Status:** Official CME tracking system for both boards
- **Evidence:** "The Oklahoma State Board of Medical Licensure and Supervision uses CE Broker as the official CME tracking system"
- **URL:** https://cebroker.com/OK/plans
- **Course Search:** https://courses.cebroker.com/search/ok
- **Integration:** Both MD board (OSBMLS) and DO board (OSBOE) use CE Broker with separate portals
- **Features:** Free; automatic reporting from ACCME/AOA providers; manual entry available
- **Source:** /Users/tmac/research/Oklahoma-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 791-848)

#### 6. Tennessee (MD & DO) - CE Broker (Free Basic Account Provided)
- **Status:** Official tracking system; free basic account for all licensees
- **Evidence:** "Tennessee partners with CE Broker to provide free Basic Accounts to all licensees. CE Broker is the primary CME tracking system"
- **URL:** https://www.tn.gov/health/health-program-areas/health-professional-boards/me-board/me-board/continuing-education.html
- **Key Feature:** **Automatic audit pass if current in CE Broker**
- **Renewal Portal:** Health Licensure Regulation System (HLRS) at https://apps.tn.gov/hlrs/
- **Reporting:** Direct provider reporting (ACCME, AAFP, AOA), manual entry, or certificate upload
- **Source:** /Users/tmac/research/Tennessee-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 313-497)

### States Using Board-Operated Portals (No Third-Party System)

#### 7. Hawaii - MyPVL System (No CE Broker Integration)
- **Status:** Board-operated online renewal system without third-party integration
- **Evidence:** "Hawaii does not partner with third-party CME tracking systems such as CE Broker"
- **URL:** MyPVL online renewal system (specific URL in board materials)
- **Method:** Attestation at renewal; certificates submitted only upon audit
- **Source:** /Users/tmac/research/HI-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 270-272)

#### 8. Idaho - Attestation Only (No Mandated Third-Party System)
- **Status:** Attestation at renewal; no third-party system integration
- **Evidence:** "Idaho does not appear to mandate or integrate with third-party CME tracking services (such as CE Broker)"
- **Method:** Physicians attest to CME completion online; upload certificates only if audited
- **Source:** /Users/tmac/research/ID-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 342-344)

#### 9. Kansas - KSBHA Online Renewal System (No Third-Party Partnership)
- **Status:** Board online system; no CE Broker or external integration
- **Evidence:** "Kansas does not partner with third-party CME tracking systems such as CE Broker"
- **Method:** CME tracking and attestation through KSBHA online renewal system
- **Source:** /Users/tmac/research/KS-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 238-240)

#### 10. Pennsylvania - Attestation Only (CE Broker Optional)
- **Status:** No mandate; CE Broker optional at physician's expense
- **Evidence:** "While Pennsylvania does not mandate CE Broker usage, many physicians use CE Broker for voluntary CME tracking"
- **Cost:** CE Broker requires paid subscription (not free for Pennsylvania physicians)
- **Method:** Attestation at renewal; self-maintained records for audit
- **Source:** /Users/tmac/research/Pennsylvania-MD-Renewal-Requirements-Narrative-2026-01-02.md (lines 795-804)

#### 11. Vermont (MD & DO) - No Mandatory Third-Party System
- **Status:** No mandated or provided third-party tracking service
- **Evidence:** "Vermont does not mandate or provide a specific third-party CME tracking service (unlike states that provide free CE Broker accounts)"
- **Method:** Physicians select own tracking methods; documentation retention required
- **Source:** /Users/tmac/research/Vermont-DO-Renewal-Requirements-Narrative-2026-01-02.md (line 407)

### States with Critical Gaps (Marked as Unknown)

The following states have existing research documents that mark CME tracking systems as **critical gaps**:

- **Maine:** "Critical gap - official CME tracking system not identified" (lines 350, 435)
- **Michigan:** "Michigan's official CME tracking system (if any) is not identified" (line 299)
- **Montana:** "No CE Broker or board portal for CME logging" (line 316)
- **Nebraska:** "Whether Nebraska uses centralized CME tracking...not documented" (line 316)
- **Nevada:** "Nevada's official CME tracking system (if any) is not identified" (line 394)
- **South Dakota:** "No CE Broker or board portal for CME logging" (line 234)
- **Utah:** "Whether Utah uses centralized CME tracking...not documented" (line 332)
- **Virginia:** "Whether Virginia uses centralized CME tracking...not documented" (line 289)
- **Wisconsin:** "Whether Wisconsin uses centralized CME tracking...not documented" (line 340)
- **Wyoming:** "Whether Wyoming uses centralized CME tracking...not documented" (line 325)

---

## MANUAL RESEARCH FRAMEWORK - 18 TARGET STATES

### TIER 1: HIGH-PRIORITY STATES (Large Populations)

---

#### State 1: Maryland (MD)

**Existing Document:** /Users/tmac/research/Maryland-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** CME tracking system NOT documented in existing research
**Board:** Maryland Board of Physicians (MBP)
**Board Website:** https://www.mbp.state.md.us/

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Visit: https://www.cebroker.com/
   - Search: "Maryland medical board"
   - Document: Is Maryland listed as a CE Broker partner state?

2. **Maryland Board Website - CME Section**
   - Visit: https://www.mbp.state.md.us/
   - Navigate to: "License Renewal" > "CME Requirements"
   - Search for: "CME tracking," "CME portal," "reporting"
   - Look for: Named system, portal login, reporting instructions

3. **Maryland Online Renewal Portal**
   - Look for renewal portal link on board homepage
   - Test: Can physicians log in to view CME compliance?
   - Document: Portal name, URL, features (manual entry vs automatic sync)

4. **Search Maryland Administrative Code**
   - Code: COMAR 10.32.02 (Continuing Medical Education)
   - Search for: "CME reporting," "tracking system," "documentation"
   - URL: (Maryland administrative code online database)

**QUESTIONS TO ANSWER:**
- [ ] What system does Maryland use? (CE Broker, board portal, other)
- [ ] Do CME providers auto-report to Maryland board?
- [ ] Must physicians upload certificates or just attest?
- [ ] Is there a physician CME transcript available online?

**DOCUMENTATION TEMPLATE:**
```markdown
### Maryland - CME Tracking System

[FACT - BOARD/VENDOR] Maryland uses [SYSTEM NAME] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [CE Broker / Board Portal / Other]
- **URL:** [Direct link to physician portal]
- **Reporting Method:** [Automatic provider reporting / Manual physician entry / Attestation only]
- **Features:** [List features: transcript, manual entry, auto-sync, etc.]

**Evidence Citation:**
> "[Exact quote from board website about CME reporting]"
> Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Maryland-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Add Section 12 "CME Tracking Systems" (currently missing)
```

---

#### State 2: Massachusetts (MA)

**Existing Document:** /Users/tmac/research/Massachusetts-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** CME tracking system NOT documented in existing research
**Board:** Massachusetts Board of Registration in Medicine (BORIM)
**Board Website:** https://www.mass.gov/info-details/board-of-registration-in-medicine

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Visit: https://www.cebroker.com/
   - Search: "Massachusetts medical board"
   - Document: Is Massachusetts listed?

2. **Massachusetts Board Website - CME Section**
   - Visit: https://www.mass.gov/info-details/board-of-registration-in-medicine
   - Navigate to: CME requirements or license renewal section
   - Search for: "CME tracking," "renewal portal," "CE Broker"

3. **Massachusetts Online Renewal Portal**
   - Look for online renewal system link
   - Document: Portal name, URL, CME reporting method

4. **Search Massachusetts Regulations**
   - Code: 243 CMR 2.00 (Continuing Medical Education)
   - Search for: "CME documentation," "reporting," "tracking"

**QUESTIONS TO ANSWER:**
- [ ] What system does Massachusetts use?
- [ ] Given 10+ mandatory topics, is there a sophisticated tracking system?
- [ ] Do providers auto-report to Massachusetts board?
- [ ] How do physicians track multiple mandatory topics?

**DOCUMENTATION TEMPLATE:**
```markdown
### Massachusetts - CME Tracking System

[FACT - BOARD/VENDOR] Massachusetts uses [SYSTEM NAME] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [System name]
- **URL:** [Portal URL]
- **Reporting Method:** [Auto/Manual/Attestation]
- **Topic Tracking:** [How does system track 10 hrs risk management, 3 hrs opioid, etc.?]

**Evidence Citation:**
> "[Quote]"
> Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Massachusetts-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Add Section 12 "CME Tracking Systems"
```

---

#### State 3: Ohio (OH)

**Existing Document:** /Users/tmac/research/Ohio-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** CME tracking marked as attestation-based; specific system unclear
**Board:** State Medical Board of Ohio (SMBO)
**Board Website:** https://www.med.ohio.gov
**Renewal Portal:** https://elicense.ohio.gov

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Search: "Ohio medical board CE Broker"

2. **Ohio Board Website - CME Section**
   - Visit: https://www.med.ohio.gov
   - Navigate to: "License Renewal" > "CME Requirements"
   - Search for: CME tracking system details

3. **Ohio eLicense Portal**
   - Visit: https://elicense.ohio.gov
   - Test: Create account or review demo
   - Document: Does portal show CME transcript? Manual entry fields?

4. **Search Ohio Administrative Code**
   - Code: OAC 4731-11-01 (CME Requirements)
   - Search for: "CME verification," "tracking," "documentation"

**QUESTIONS TO ANSWER:**
- [ ] Does Ohio eLicense system include CME tracking module?
- [ ] Do physicians manually enter CME or just attest?
- [ ] Is there provider auto-reporting to Ohio board?
- [ ] Can physicians view CME transcript in eLicense?

**DOCUMENTATION TEMPLATE:**
```markdown
### Ohio - CME Tracking System

[FACT - BOARD] Ohio uses the eLicense system (https://elicense.ohio.gov) for license renewal.

[FACT/INFERENCE] CME reporting method: [Attestation only / Manual entry / Other]
Source: [URL] | Accessed: 2026-01-03

**Evidence Citation:**
> "[Quote from Ohio board website or eLicense portal]"
> Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Ohio-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Update Section 7 "CME Tracking & Compliance Verification" (lines 256-276) with specific system details
```

---

#### State 4: Minnesota (MN)

**Existing Document:** /Users/tmac/research/Minnesota-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** CME tracking system NOT documented
**Board:** Minnesota Board of Medical Practice (MBMP)
**Board Website:** https://mn.gov/boards/medical-practice/

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Search: "Minnesota medical board CE Broker"

2. **Minnesota Board Website - CME Section**
   - Visit: https://mn.gov/boards/medical-practice/
   - Navigate to: License renewal or CME requirements
   - Search for: "CME tracking," "reporting"

3. **Minnesota Online Renewal Portal**
   - Look for online renewal system link
   - Document: Portal name, CME reporting features

4. **Search Minnesota Rules**
   - Code: Minnesota Rules 5600.2100 (Continuing Medical Education)
   - Search for: "CME documentation," "verification"

**QUESTIONS TO ANSWER:**
- [ ] What system does Minnesota use?
- [ ] Given 10+ mandatory topics (like Massachusetts), how are topics tracked?
- [ ] Is there auto-reporting from CME providers?

**DOCUMENTATION TEMPLATE:**
```markdown
### Minnesota - CME Tracking System

[FACT - BOARD/VENDOR] Minnesota uses [SYSTEM NAME] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [System name]
- **URL:** [Portal URL]
- **Reporting Method:** [Auto/Manual/Attestation]

**Evidence Citation:**
> "[Quote]"
> Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Minnesota-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Add Section 12 "CME Tracking Systems"
```

---

#### State 5: Kentucky (KY)

**Existing Document:** /Users/tmac/research/KY-MD-Renewal-Requirements-Narrative-2026-01-02.md (v3.0 Comprehensive)
**Current Status:** CE Broker mentioned as **voluntary** but not mandated
**Board:** Kentucky Board of Medical Licensure (KBML)
**Board Website:** https://kbml.ky.gov/
**Renewal Portal:** https://services.kbml.ky.gov/ebusiness/Login.aspx

**KNOWN INFORMATION:**
- **[FACT - BOARD]** CE Broker offers automated compliance tracking in Kentucky for various healthcare professions (EMS, Dentistry), but **not mandated** for physicians (lines 541-544)
- **[INFERENCE - MEDIUM]** Physicians may voluntarily use CE Broker for personal record-keeping, but state does not require it
- **Source:** https://cebroker.com/ky/plans

**RESEARCH TASKS:**

1. **Verify CE Broker Status for Physicians**
   - Visit: https://cebroker.com/ky/plans
   - Check: Is "Kentucky Board of Medical Licensure" listed as a partner?
   - Compare to: EMS board, dental board (which DO use CE Broker)

2. **Kentucky Board Renewal Portal**
   - Visit: https://services.kbml.ky.gov/ebusiness/Login.aspx
   - Test: Explore CME reporting features (create test account if possible)
   - Document: Manual entry vs attestation? CME transcript available?

3. **Kentucky Board - CME Resources**
   - Visit: https://kyma.org/education-cme/continuing-medical-education/ (Kentucky Medical Association)
   - Search for: Board-approved tracking system, recommended vendor

4. **Search Kentucky Administrative Code**
   - Code: 201 KAR 9:310 (Continuing Medical Education)
   - Search for: "CME tracking," "verification," "reporting"

**QUESTIONS TO ANSWER:**
- [ ] Is CE Broker truly voluntary or is it integrated with board portal?
- [ ] What is the official board CME reporting method?
- [ ] Do physicians attest only or manually enter CME details?
- [ ] Can physicians export CME transcript from board portal?

**DOCUMENTATION TEMPLATE:**
```markdown
### Kentucky - CME Tracking System

[FACT - BOARD] Kentucky Board of Medical Licensure uses [SYSTEM NAME] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [KBML Online Renewal Portal / CE Broker / Other]
- **Portal URL:** https://services.kbml.ky.gov/ebusiness/Login.aspx
- **CE Broker Status:** Voluntary (not mandated for physicians) - confirmed
- **Reporting Method:** [Attestation only / Manual entry / Other]
- **Features:** [List portal features]

**Evidence Citation:**
> "[Quote from KBML website or renewal portal]"
> Source: [URL] | Accessed: 2026-01-03

**Clarification on Existing v3.0 Research:**
- Lines 541-544 correctly note CE Broker is NOT mandated for physicians
- Need to document: What IS the official board tracking method?
- Update: Add specific portal features and reporting workflow

**Update Required:**
- Document: /Users/tmac/research/KY-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Expand Section 12 "CME Tracking Systems" (lines 533-558) with official board portal details
```

---

#### State 6: Louisiana (LA)

**Existing Document:** /Users/tmac/research/Louisiana-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** CME tracking system NOT documented
**Board:** Louisiana State Board of Medical Examiners (LSBME)
**Board Website:** https://www.lsbme.la.gov/
**Renewal Portal:** https://www.lsbme.la.gov/ (look for online renewal link)

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Search: "Louisiana medical board CE Broker"

2. **Louisiana Board Website - CME Section**
   - Visit: https://www.lsbme.la.gov/
   - Navigate to: License renewal or CME requirements
   - Search for: "CME tracking," "annual renewal," "reporting"

3. **Louisiana Online Renewal Portal**
   - Look for online renewal system link on board homepage
   - Document: Portal name, CME reporting method

4. **Search Louisiana Administrative Code**
   - Code: LAC 46:XLIII (Board of Medical Examiners)
   - Search for: "CME documentation," "continuing education reporting"

**QUESTIONS TO ANSWER:**
- [ ] What system does Louisiana use?
- [ ] Given annual renewal cycle (20 hrs/year), is tracking more streamlined?
- [ ] Do providers auto-report to Louisiana board?

**DOCUMENTATION TEMPLATE:**
```markdown
### Louisiana - CME Tracking System

[FACT - BOARD/VENDOR] Louisiana uses [SYSTEM NAME] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [System name]
- **URL:** [Portal URL]
- **Reporting Method:** [Auto/Manual/Attestation]
- **Annual Renewal:** Louisiana's annual cycle (20 hrs/year) may influence tracking simplicity

**Evidence Citation:**
> "[Quote]"
> Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Louisiana-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Add Section 12 "CME Tracking Systems" (currently missing)
```

---

### TIER 2: MEDIUM-PRIORITY STATES

---

#### State 7: Connecticut (CT)

**Board:** Connecticut Medical Examining Board
**Board Website:** https://portal.ct.gov/dph/practitioner-licensing--investigations/medical-examining-board
**Target:** Document CME tracking system

**RESEARCH TASKS:**
1. CE Broker state list check
2. Board website CME section review
3. Online renewal portal exploration
4. Connecticut administrative code search

**QUESTIONS:**
- [ ] CE Broker integration?
- [ ] Board portal name and URL?
- [ ] Reporting method?

---

#### State 8: New Hampshire (NH)

**Board:** New Hampshire Board of Medicine
**Board Website:** https://www.oplc.nh.gov/medicine
**Target:** Document CME tracking system

**RESEARCH TASKS:**
1. CE Broker state list check
2. Board website CME section
3. Online renewal portal (OPLC system)
4. NH administrative rules search

**QUESTIONS:**
- [ ] Does OPLC (Office of Professional Licensure and Certification) have CME tracking module?
- [ ] CE Broker used?
- [ ] Reporting method?

---

#### State 9: New Mexico (NM)

**Board:** New Mexico Medical Board
**Board Website:** http://www.nmmb.state.nm.us/
**Target:** Document CME tracking system

**RESEARCH TASKS:**
1. CE Broker state list check
2. Board website CME section
3. Online renewal portal exploration
4. NM administrative code search

**QUESTIONS:**
- [ ] CE Broker integration?
- [ ] Board portal features?
- [ ] Reporting method?

---

#### State 10: Kansas (KS)

**Existing Document:** /Users/tmac/research/KS-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** **NO CE Broker integration confirmed** (line 238)
**Board:** Kansas State Board of Healing Arts (KSBHA)
**Board Website:** https://ksbha.ks.gov/

**KNOWN INFORMATION:**
- **[INFERENCE-HIGH]** Kansas does NOT partner with CE Broker (line 238)
- **[FACT-BOARD]** CME tracking through KSBHA online renewal system (line 240)

**RESEARCH TASKS:**

1. **Verify KSBHA Online Renewal System**
   - Visit: https://ksbha.ks.gov/
   - Navigate to: Online renewal portal
   - Document: Portal name, URL, CME reporting features

2. **Kansas Board - Renewal Instructions**
   - Look for downloadable renewal instructions
   - Document: How physicians report CME compliance

**QUESTIONS TO ANSWER:**
- [ ] What is the exact KSBHA online renewal portal URL?
- [ ] Attestation only or manual entry required?
- [ ] Can physicians view CME transcript in portal?

**DOCUMENTATION TEMPLATE:**
```markdown
### Kansas - CME Tracking System

[FACT - BOARD] Kansas uses the KSBHA online renewal system (NOT CE Broker) for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** KSBHA Online Renewal System
- **URL:** [Specific portal URL]
- **Reporting Method:** [Attestation / Manual entry]
- **CE Broker:** NOT used (confirmed in existing research)

**Update Required:**
- Document: /Users/tmac/research/KS-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Expand CME tracking section with specific portal URL and reporting workflow
```

---

#### State 11: Mississippi (MS)

**Board:** Mississippi State Board of Medical Licensure
**Board Website:** https://www.msbml.ms.gov/
**Target:** Document CME tracking system

**RESEARCH TASKS:**
1. CE Broker state list check
2. Board website CME section
3. Online renewal portal
4. MS administrative code search

**QUESTIONS:**
- [ ] CE Broker used?
- [ ] Board portal name?
- [ ] Reporting method?

---

#### State 12: Nebraska (NE)

**Existing Document:** /Users/tmac/research/Nebraska-MD-Renewal-Requirements-Narrative-2026-01-02.md
**Current Status:** **CRITICAL GAP** - tracking system not documented (line 316)
**Board:** Nebraska Department of Health and Human Services - Division of Public Health - Licensure Unit
**Board Website:** http://dhhs.ne.gov/licensure/Pages/licensure.aspx

**RESEARCH TASKS:**

1. **Check CE Broker State List**
   - Search: "Nebraska medical board CE Broker"

2. **Nebraska Board Website - CME Section**
   - Visit: http://dhhs.ne.gov/licensure/Pages/licensure.aspx
   - Navigate to: Physician licensure > CME requirements
   - Search for: CME tracking system details

3. **Nebraska Online Renewal Portal**
   - Look for online renewal link
   - Document: Portal name, URL, CME reporting method

**QUESTIONS:**
- [ ] What system does Nebraska use?
- [ ] Attestation-based (as inferred in line 318)?
- [ ] Manual entry required?

**DOCUMENTATION TEMPLATE:**
```markdown
### Nebraska - CME Tracking System

[FACT - BOARD/INFERENCE] Nebraska uses [SYSTEM NAME / attestation-based system] for CME tracking.
Source: [URL] | Accessed: 2026-01-03

**Update Required:**
- Document: /Users/tmac/research/Nebraska-MD-Renewal-Requirements-Narrative-2026-01-02.md
- Section: Update lines 316-318 with specific system details (currently marked as critical gap)
```

---

### TIER 3: LOWER-PRIORITY STATES

For brevity, Tier 3 states follow the same research framework:

#### State 13: Alaska (AK)
- **Board:** Alaska State Medical Board
- **Website:** https://www.commerce.alaska.gov/web/cbpl/ProfessionalLicensing/StateMedicalBoard.aspx
- **Known:** No CE Broker (line 234 in existing doc)

#### State 14: Arkansas (AR)
- **Board:** Arkansas State Medical Board
- **Website:** https://www.armedicalboard.org/
- **Research:** CE Broker check, board portal

#### State 15: Delaware (DE)
- **Board:** Delaware Board of Medical Licensure and Discipline
- **Website:** https://delpros.delaware.gov/
- **Portal:** DelPROS (https://delpros.delaware.gov/)
- **Research:** Document DelPROS CME features

#### State 16: District of Columbia (DC)
- **Board:** DC Board of Medicine
- **Website:** https://dchealth.dc.gov/service/board-medicine
- **Research:** CE Broker check, board portal

#### State 17: Iowa (IA)
- **Board:** Iowa Board of Medicine
- **Website:** https://medicalboard.iowa.gov/
- **Research:** CE Broker check, online renewal portal

#### State 18: North Dakota (ND)
- **Board:** North Dakota Board of Medicine
- **Website:** https://www.ndbom.org/
- **Research:** CE Broker check, board portal

---

## RESEARCH OUTPUT TEMPLATE

For each state researched, create an entry in this format:

```markdown
---

## [STATE NAME] - CME Tracking System Resolution

**Research Date:** 2026-01-03
**Researcher:** [Your name]
**Board:** [Board name]
**Board Website:** [URL]

### FINDINGS

#### System Identification

[FACT - BOARD/VENDOR] [State] uses [SYSTEM NAME] for CME tracking and reporting.

**System Details:**
- **Official Name:** [CE Broker / Board Portal Name / Other]
- **System URL:** [Direct link to CME portal or renewal system]
- **Vendor:** [CE Broker / State-operated / Other vendor name]
- **Cost to Physicians:** [Free / Paid / Not applicable]

#### Reporting Method

**How physicians report CME:**
- [ ] Automatic provider reporting (from ACCME/AOA accredited providers)
- [ ] Manual physician entry (physicians enter course details)
- [ ] Attestation only (physicians certify completion without details)
- [ ] Certificate upload required
- [ ] Other: [Describe]

**Integration Details:**
- Auto-sync from CME providers: [Yes/No/Partial]
- CME transcript available to physician: [Yes/No]
- Topic-specific tracking (for mandatory topics): [Yes/No]
- Manual entry fields: [Yes/No - describe]

### EVIDENCE CITATIONS

**Source 1: [Board Website / CE Broker / Other]**
- **URL:** [Full URL]
- **Access Date:** 2026-01-03
- **Relevant Quote:**
  > "[Exact text from source about CME tracking system]"

**Source 2: [Secondary Source]**
- **URL:** [Full URL]
- **Access Date:** 2026-01-03
- **Relevant Quote:**
  > "[Exact text]"

**Source 3 (if applicable):**
- **URL:** [Full URL]
- **Access Date:** 2026-01-03
- **Relevant Quote:**
  > "[Exact text]"

### VERIFICATION STATUS

- [ ] Minimum 2 sources verified
- [ ] Direct quote from board website obtained
- [ ] System URL confirmed functional
- [ ] Reporting method clearly documented
- [ ] Screenshots captured (if applicable)

**Confidence Level:** [HIGH / MEDIUM / LOW]

**Notes:**
- [Any additional observations]
- [Clarifications needed]
- [Alternative sources explored]

### UPDATE REQUIRED

**Target Document:** /Users/tmac/research/[STATE]-MD-Renewal-Requirements-Narrative-2026-01-02.md

**Section to Add/Update:**
- **Section Number:** 12 (CME Tracking Systems) or Section 8 (Audit & Verification) subsection
- **Lines:** [Specific line numbers if updating existing section]
- **Action:** [Add new section / Update existing gap / Expand existing content]

**Recommended Content:**
```markdown
## 12. CME TRACKING SYSTEMS

### Official Tracking System - [System Name]

[FACT - BOARD] [State] uses [SYSTEM NAME] for CME compliance tracking and verification.
Source: [URL] | Accessed: 2026-01-03

**System Details:**
- **Name:** [System name]
- **URL:** [Portal URL]
- **Vendor:** [CE Broker / State-operated / Other]
- **Cost:** [Free / Paid]

**Reporting Method:**
[FACT - BOARD] Physicians report CME compliance through [automatic provider reporting / manual entry / attestation only].

[Describe specific workflow: How physician completes CME > How it's reported > How board verifies]

**Features:**
- [Feature 1: e.g., CME transcript generation]
- [Feature 2: e.g., Course search and registration]
- [Feature 3: e.g., Automatic audit pass if current]

**Evidence:**
> "[Direct quote from board website]"
> Source: [URL] | Accessed: 2026-01-03
```

---
```

---

## CONTACT INFORMATION FOR MANUAL VERIFICATION

If tracking system cannot be identified through web research, contact boards directly:

### Email Template

```
Subject: CME Tracking System Inquiry - [State] Physician License Renewal

Dear [Board Name] Staff,

I am conducting research on CME compliance tracking systems for physician license renewal across all states. Could you please clarify the following for [State]:

1. What system do physicians use to track and report CME compliance for license renewal?
   - Do you use CE Broker or another third-party vendor?
   - Do you operate an internal board portal for CME tracking?
   - Do physicians attest to completion without submitting details?

2. Do CME providers automatically report course completion to your board, or must physicians manually enter credits?

3. Can physicians access a CME transcript or compliance report through your renewal system?

4. Is there a specific portal URL where physicians can view their CME records?

Thank you for your assistance.

Sincerely,
[Your name]
[Title/Organization]
```

### Phone Script

```
"Hello, I'm researching CME compliance tracking systems for physician licensure. Could you help me understand:

1. What system does [State] use for physicians to track CME? Is it CE Broker, a board-operated portal, or another system?

2. Do physicians manually enter CME courses, or do providers report automatically?

3. Is there a physician portal where doctors can view their CME compliance status?

Thank you for your help."
```

### Board Contact Information (18 Target States)

1. **Maryland:** (410) 764-4777 | mdh.mdbp@maryland.gov
2. **Massachusetts:** (617) 654-9800 | board.medicine@mass.gov
3. **Ohio:** (614) 466-3934 | [Contact form on website]
4. **Minnesota:** (612) 617-2130 | medical.board@state.mn.us
5. **Kentucky:** (502) 429-7150 | beverlyl.collier@ky.gov
6. **Louisiana:** (504) 568-6820 | [Contact form on website]
7. **Connecticut:** (860) 509-7648 | [DPH contact]
8. **New Hampshire:** (603) 271-1203 | [OPLC contact]
9. **New Mexico:** (505) 476-7220 | [Board contact]
10. **Kansas:** (785) 296-7413 | [KSBHA contact]
11. **Mississippi:** (601) 987-3079 | [Board contact]
12. **Nebraska:** (402) 471-2115 | [DHHS contact]
13. **Alaska:** (907) 269-8163 | [Board contact]
14. **Arkansas:** (501) 296-1802 | [Board contact]
15. **Delaware:** (302) 744-4500 | [DelPROS contact]
16. **DC:** (202) 724-4900 | [DOH contact]
17. **Iowa:** (515) 281-5171 | [Board contact]
18. **North Dakota:** (701) 328-6500 | [Board contact]

---

## RESEARCH TIMELINE & EFFORT ESTIMATE

### Estimated Time per State

**High-Quality Research (Recommended):**
- CE Broker check: 5 minutes
- Board website CME section review: 15 minutes
- Online renewal portal exploration: 20 minutes
- Administrative code search: 15 minutes (if needed)
- Documentation write-up: 15 minutes
- **Total:** ~70 minutes (1.2 hours) per state

**Quick Research (Minimum):**
- CE Broker check: 5 minutes
- Board website review: 10 minutes
- Documentation: 10 minutes
- **Total:** ~25 minutes per state

### Total Project Effort

**High-Quality Approach:**
- 18 states × 1.2 hours = **21.6 hours (2.7 days)**

**Quick Approach:**
- 18 states × 0.4 hours = **7.2 hours (1 day)**

**Phased Approach (Recommended):**
- **Phase 1 (High Priority):** 6 states × 1.2 hours = **7.2 hours**
- **Phase 2 (Medium Priority):** 6 states × 1.2 hours = **7.2 hours**
- **Phase 3 (Lower Priority):** 6 states × 0.4 hours = **2.4 hours**
- **Total:** **16.8 hours (2.1 days)**

---

## DELIVERABLE CHECKLIST

Upon completion of research for all 18 states:

- [ ] **Summary table created** listing all 18 states with tracking system identified
- [ ] **Evidence citations collected** (minimum 2 sources per state, URLs + quotes)
- [ ] **Existing documents updated** (Section 12 added or updated for each state)
- [ ] **CE Broker master list** compiled (which states use it, which don't)
- [ ] **Reporting method categorized** (Automatic/Manual/Attestation for each state)
- [ ] **Contact log maintained** (if boards were contacted for clarification)
- [ ] **Screenshots archived** (if portal explorations were conducted)

---

## SUMMARY TABLE - CME TRACKING SYSTEMS (18 Target States)

| State | Board | System Name | Type | Reporting Method | Status | Sources |
|-------|-------|-------------|------|------------------|--------|---------|
| **Alaska** | Alaska State Medical Board | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Arkansas** | Arkansas State Medical Board | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Connecticut** | CT Medical Examining Board | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Delaware** | DE Board of Medical Licensure | DelPROS (inferred) | Board Portal | [TBD] | PARTIAL | 0 |
| **DC** | DC Board of Medicine | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Iowa** | Iowa Board of Medicine | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Kansas** | Kansas State Board of Healing Arts | KSBHA Online System | Board Portal | [TBD] | PARTIAL | 1 |
| **Kentucky** | Kentucky Board of Medical Licensure | KBML Portal (CE Broker voluntary) | Board Portal | [TBD] | PARTIAL | 2 |
| **Louisiana** | Louisiana State Board of Medical Examiners | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Maryland** | Maryland Board of Physicians | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Massachusetts** | MA Board of Registration in Medicine | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Minnesota** | Minnesota Board of Medical Practice | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Mississippi** | Mississippi State Board of Medical Licensure | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Nebraska** | NE DHHS - Licensure Unit | [TBD] | [CE Broker/Portal/Attestation] | Attestation (inferred) | PARTIAL | 0 |
| **New Hampshire** | New Hampshire Board of Medicine | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **New Mexico** | New Mexico Medical Board | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **North Dakota** | North Dakota Board of Medicine | [TBD] | [CE Broker/Portal/Attestation] | [Auto/Manual/Attestation] | PENDING | 0 |
| **Ohio** | State Medical Board of Ohio | Ohio eLicense | Board Portal | Attestation (inferred) | PARTIAL | 1 |

**Legend:**
- **Status:** PENDING (not researched), PARTIAL (some info documented), COMPLETE (2+ sources verified)
- **Type:** CE Broker (third-party vendor), Board Portal (state-operated), Attestation (no tracking system), Other
- **Reporting Method:** Auto (provider auto-reporting), Manual (physician entry), Attestation (certify only)

---

## CONCLUSION & NEXT STEPS

### Manual Research Required

This document provides a comprehensive framework for resolving CME tracking system gaps across 18 target states. **Web access tools are unavailable**, therefore manual research is required following the structured approach outlined above.

### Recommended Workflow

1. **Prioritize High-Priority States (6 states):** Maryland, Massachusetts, Ohio, Minnesota, Kentucky, Louisiana
2. **Use phased approach:** Complete Tier 1 first, then Tier 2, then Tier 3
3. **Document as you go:** Fill in the summary table after each state is researched
4. **Contact boards if needed:** Use email/phone templates for states with unclear information
5. **Update existing documents:** Add Section 12 to each state's research document

### Impact on Rules Engine Development

Once complete, this research will:
- Enable CE Broker API integration planning (knowing which 18 states to target)
- Inform user experience design (manual vs automatic CME tracking)
- Support accurate audit preparation workflows
- Allow "import CME transcript" feature scoping

### Quality Assurance

- Minimum 2 sources per state
- Direct quotes from board websites required
- Exact URLs with access dates
- Verification status tracked for each state

---

**Document Status:** FRAMEWORK COMPLETE - AWAITING MANUAL RESEARCH
**Next Action:** Begin research with Tier 1 High-Priority States (MD, MA, OH, MN, KY, LA)
**Estimated Completion:** 16-22 hours of manual research across 18 states

---

*This research framework was created January 3, 2026, by Claude Code to resolve systematic CME tracking system documentation gaps identified in the comprehensive audit report.*
