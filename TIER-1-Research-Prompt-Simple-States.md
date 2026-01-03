# TIER 1 Research Prompt - Simple States
**Version:** 1.0
**Created:** 2026-01-02
**Target Completion Time:** 4-6 hours per state
**License Types:** MD only (or unified MD/DO where applicable)

---

## OVERVIEW

You are researching **one state's MD license renewal requirements** from TIER 1 (Simple States).

**What makes Tier 1 simple:**
- Single unified medical board (no MD/DO split)
- 30-60 hour CME requirement per cycle
- Minimal topic-specific mandates (typically 2-4)
- Standard CME categories (AMA/AOA)
- No major state-specific requirements (medical marijuana, jurisprudence, etc.)

**Eligible States (22 total):**
AL, AK, AR, CO, CT, DE, GA, HI, ID, KS, LA, MA, MS, NE, NH, NJ, NM, ND, OH, OR, UT, WI

---

## CRITICAL INSTRUCTIONS

### Research Scope: MD ONLY
- You are researching **Medical Doctor (MD)** renewals ONLY
- Do NOT research DO (Doctors of Osteopathic Medicine) unless state has UNIFIED requirements
- Do NOT research NP (Nurse Practitioners) - separate research track
- If split-board state found, STOP and report to project manager

### One Document Per Research Session
- **Output:** Single markdown file: `[STATE]-MD-Renewal-Requirements-Narrative-[YYYY-MM-DD].md`
- **Format:** Narrative markdown with regulatory citations
- **Length:** Target 15-25 pages (comprehensive but focused)

### Use the State Research Tracker CSV
- **Before starting:** Open `/Users/tmac/research/state-research-tracker.csv`
- **Mark:** Set status to "IN_PROGRESS" for your state
- **During research:** Update completion % in real-time
- **On completion:** Mark status as "COMPLETE" and update all section completion percentages

---

## RESEARCH PROCESS (4-6 hours)

### Step 1: Identify Board & Statutes (0.5 hours)
**Tasks:**
1. Locate official state medical board website
2. Find governing statute (usually Title XX, Medical Practice Act)
3. Find administrative code (usually Title XX, Chapter X)
4. Note board name, abbreviation, website URL

**Search Pattern:**
- Google: "[STATE] medical board CME requirements"
- Look for: Board renewal page, CME FAQ, licensing information
- Verify: Board website is official .gov domain

**Example:**
```
State: Alabama
Board: Alabama State Board of Medical Examiners
Statute: Ala. Admin. Code r. 540-x-14.02
Admin Code: Ala. Code § 34-24-75
Website: http://www.albme.org
```

---

### Step 2: Extract Core Requirements (1.5 hours)
**Tasks:**
1. Total CME hours and renewal cycle (triennial/biennial/annual)
2. Category requirements (all Category 1? mixed categories?)
3. List mandatory topics (pain management, opioids, cultural competency, etc.)
4. Renewal fees (standard + late)
5. Grace periods for newly licensed physicians

**Source Priority:**
1. State statute (HIGHEST)
2. Admin code (HIGH)
3. Board website/FAQ (MEDIUM-HIGH)
4. FSMB document (VALIDATION ONLY)

**Validation:**
- Does board website match statute?
- Does FSMB match your findings?
- Document any conflicts with explanation

---

### Step 3: Controlled Substance Context (1 hour)
**Tasks:**
1. DEA registration requirement for renewal?
2. Opioid prescribing CME hours mandated?
3. PDMP (Prescription Drug Monitoring Program) training required?
4. Prescribing limits documented in statute or admin code?
5. Any telemedicine opioid restrictions?

**Search Terms:**
- "[STATE] opioid CME requirement"
- "[STATE] controlled substance prescribing"
- "[STATE] PDMP training"
- "[STATE] DEA registration renewal"

---

### Step 4: CME Tracking System (0.5 hours)
**Tasks:**
1. What system does state use? (CE Broker, board-operated portal, other)
2. Are CME providers required to auto-report?
3. Can physicians attest online or must they upload certificates?
4. Audit percentage: how many renewals audited annually?

**Search:**
- "[STATE] board CME portal"
- "[STATE] CE Broker"
- Board renewal instructions page

---

### Step 5: Exemptions & Board Certification (0.5 hours)
**Tasks:**
1. Does board certification (ABMS/AOA) satisfy CME requirement?
2. Do resident/fellow physicians get CME credit or exemption?
3. Military service exemption?
4. Hardship exemption?

**Documentation:**
- Cite specific statute section
- Note: "Full exemption OR partial credit (X hours)"
- Effective date if recent change

---

### Step 6: Audit & Reinstatement (1 hour)
**Tasks:**
1. What triggers CME audit? (random? every X% of renewals? for-cause only?)
2. How many days to respond to audit?
3. What documents required? (certificates, transcripts, other?)
4. Penalty for non-compliance: fine? suspension? hearing?
5. What is lapsed license reinstatement process? (Tier 1: simplified)
6. CME makeup required if lapsed < 1 year?

**Critical for Tier 1:**
- Most Tier 1 states have simple reinstatement
- Document all three tiers if they exist (lapsed <1yr, 1-3yr, >3yr)

---

### Step 7: Verify Against FSMB (0.5 hours)
**Task:**
- Open FSMB document for your state
- Compare your findings against FSMB data:
  - CME hours: match?
  - Category requirements: match?
  - Opioid requirement: match?
- Document any conflicts with explanation

**Format:**
```
Cross-Source Validation:
- STATUTE says "60 hours Category 1 every 3 years"
- FSMB says "60 hours every 3 years; all must be Category 1"
- BOARD WEBSITE says "60 hours Category 1 every 3 years"
Congruency: 3/3 sources agree ✅
```

---

## DELIVERABLE STRUCTURE

Follow the **Comprehensive Prompt v3.0** section structure exactly:

1. **Frontmatter (YAML)** - 30 minutes to complete
2. **Executive Summary** - 3-5 bullet points
3. **Board Information & Authority** - 0.5 hours
4. **Lifecycle Phases & Grace Periods** - 0.5 hours
5. **CME Requirements - Total Hours & Categories** - 0.5 hours
6. **CME Topic Requirements** - 1 hour (document each topic separately)
7. **Controlled Substance Context** - 0.5 hours
8. **Audit & Verification Procedures** - 0.5 hours
9. **Exemptions & Alternatives** - 0.5 hours
10. **Renewal Fees & Timeline** - 0.5 hours
11. **Lapsed License Reinstatement** - 0.5 hours
12. **CME Tracking Systems** - 0.25 hours
13. **State-Specific Requirements** - 0.5 hours (if any found)
14. **Research Gaps & Limitations** - 0.5 hours
15. **Sources Cited** - 0.5 hours

**DO NOT include:**
- Appendix (Tier 1 is usually complete)
- NP requirements (separate research)
- DO requirements (single board only)

---

## EVIDENCE CLASSIFICATION REQUIRED

Use inline notation for EVERY factual claim:

**[FACT - STATUTE]** - Directly from state law
- Must include: citation, URL, exact quote
- Example: `[FACT - STATUTE] 60 hours CME every 3 years per 59 O.S. § 495a.1`

**[FACT - ADMIN_CODE]** - From administrative regulations
- Must include: citation, URL, exact quote
- Example: `[FACT - ADMIN_CODE] Board conducts random audits per 435 OAC 10-7-1`

**[FACT - BOARD]** - From official board website
- Must include: URL, date accessed, quote or clear reference
- Example: `[FACT - BOARD] Renewal portal opens 60 days before expiration (accessed 2026-01-02)`

**[INFERENCE - CONFIDENCE]** - Derived from facts
- Must explain reasoning
- Must state confidence: HIGH / MEDIUM / LOW
- Example: `[INFERENCE - HIGH CONFIDENCE] License renewal cycle is triennial (every 3 years) based on CME requirement cycle matching renewal cycle`

**[CRITICAL GAP]** - Extensively searched but NOT found
- Must document search attempts
- Must explain impact on rules engine
- Example: `[CRITICAL GAP] CME record retention period unknown - searched statute, admin code, board FAQ`

---

## QUALITY CHECKLIST

Before marking complete, verify:

- [ ] Frontmatter YAML is 100% complete
- [ ] All factual statements have evidence classification ([FACT], [INFERENCE], [GAP])
- [ ] All [FACT] statements include source citation AND URL AND quote
- [ ] All [INFERENCE] statements explain reasoning AND state confidence
- [ ] All [CRITICAL GAP] statements document search attempts
- [ ] Cross-source congruency tracked for all major requirements
- [ ] Sections follow v3.0 structure in exact order
- [ ] Research Gaps section complete (all gaps prioritized)
- [ ] Sources Cited section includes all URLs and access dates
- [ ] Completion percentage calculated in frontmatter
- [ ] Document tagged with research date and last_verified date
- [ ] No NP requirements included
- [ ] No DO requirements included (unless state unified)

---

## TIME ALLOCATION (4-6 hours total)

| Task | Time |
|------|------|
| Step 1: Identify Board & Statutes | 0.5 hr |
| Step 2: Core Requirements | 1.5 hrs |
| Step 3: Controlled Substance Context | 1 hr |
| Step 4: CME Tracking System | 0.5 hr |
| Step 5: Exemptions & Board Cert | 0.5 hr |
| Step 6: Audit & Reinstatement | 1 hr |
| Step 7: FSMB Verification | 0.5 hr |
| Frontmatter & Documentation | 1 hr |
| **TOTAL** | **6.5 hrs** |

**Target Completion: 4 hours minimum, 6-7 hours for comprehensive research**

---

## HELPFUL TIPS FOR TIER 1 RESEARCH

1. **Start with FSMB data** - Use it as a starting point, verify everything
2. **Board websites are often better than statutes** - More user-friendly, current
3. **Admin code has implementation details** - Statutes are high-level; OAC/OAR has specifics
4. **Search for "CME FAQ" or "Renewal FAQ"** - Often consolidates all requirements
5. **If you find a board manual** - Gold mine of implementation details
6. **Controlled substance requirements** - Usually in separate section of statute
7. **Contact info for board** - Include in sources for future verification
8. **Reinstatement info** - Often buried in disciplinary code, not licensing code

---

## COMPLETION CRITERIA

**Minimum (50% completion):**
- Core CME hours, cycle, categories documented
- Renewal fees documented
- Controlled substance requirements (if any) documented
- Board contact info and portal documented

**Standard (70% completion):**
- All sections 1-12 completed
- Evidence classification applied to all major claims
- Sources cited with URLs
- 1-3 gaps identified

**Comprehensive (85%+ completion):**
- All sections 1-14 completed
- Cross-source congruency verified
- All gaps documented with search attempts
- Ready for validation with board contact

---

## UPDATING THE TRACKER

After completion:

1. Open `/Users/tmac/research/state-research-tracker.csv`
2. Find your state row
3. Update fields:
   - `status`: "COMPLETE"
   - `md_completion_%`: Your actual completion percentage
   - `md_document`: Name of your output file
   - `last_updated`: Today's date
   - `notes`: Any critical gaps or findings

4. Commit the CSV update to git

---

## WHEN STUCK

**Q: Can't find CME statute?**
A: Check board website for "Statutes & Rules" link. Often links directly to statute sections.

**Q: State has multiple codes (title 43, 49, etc.)?**
A: Medical licensing is usually in one title (e.g., Title 4 = licensing in many states). Check board website for official citation.

**Q: FSMB data conflicts with statute?**
A: Trust the statute. FSMB is accurate but may be outdated. Note conflict in document.

**Q: Can't find information on a topic?**
A: That's a GAP. Document what you searched, where you looked, and mark as [CRITICAL GAP] if it blocks rules engine.

**Q: Reinstatement info doesn't exist in statute?**
A: Common for Tier 1 states. Document what you found. Mark gap if needed.

---

*This research prompt supports CREDMATE's CME accuracy framework for Tier 1 (Simple) states.*