# 03 Cold Read — Stripe, Engineering Manager, Disputes Foundations (Singapore)

Resume read: `wilson-2026_SM_Internet_Stripe_V1_0_0_draft.txt` (3 pages). JD read: `03_Stripe_JD.md`. No other file opened.

## Verdict: REVISE

Reason: the recruiter can name three matches, but I quote more than two sentences a non-technical recruiter would not follow (six listed below; the rule's limit is two).

---

## (a) HR recruiter, 30 seconds

**1. Who is he.** Senior engineering leader, 18+ years. Currently Vice President (VP2) / Technical Delivery Manager at UOB, a Tier-1 Singapore bank, since Oct 2022. He leads about 25 onshore and offshore engineers in two platform teams (payments and lending). Earlier he held CTO/VP/Head-of-Tech roles at start-ups, and engineering roles at Renren, Sohu and Baidu. Level: senior manager to director. Domain: payments and platform engineering.

**2. Three strongest matches to the JD.**
1. **People leadership across time zones.** 25 engineers, onshore and offshore, with teams in India, Thailand and Indonesia; 1:1s, mentoring and performance management. This matches "support a team of senior engineers", "cross-timezone" and "3+ years managing".
2. **Platform built for other teams, in payments.** A payment-initiation hub used by the bank's digital and branch channels, plus ISO 20022 and card and wallet integrations. This matches "extensible software", "platforms to serve other product teams" and "familiarity with payments".
3. **Hands-on plus production rigour.** Daily pull-request review, personally coded core modules, P1–P3 incident ownership, SLOs, DR drills and 99.9%+ availability. This matches "lead by example" and "high operational rigor".

**3. Biggest doubt.** The title "Technical Delivery Manager" and the programme-management language (steering committees, vendor governance, SOW negotiation) read as delivery or programme management rather than product-engineering management. The JD stresses product strategy and partnering with product management. A close second: nothing on the page shows hiring, which is a stated minimum requirement ("track record of successfully hiring"). The same page also shows career-history gaps (Dec 2014 to Apr 2016, Jun to Nov 2020).

**4. Sentences I could not follow, or that are too jargon-heavy for HR (exact quotes).**
1. "Designs and delivers extensible platforms that other teams and businesses depend on — payment initiation, customer data and multi-tenant SaaS — and has led VV Technology's 140-person technology organisation (total headcount)." The "(total headcount)" parenthetical is odd, and the VV section lower down never mentions 140.
2. "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution."
3. "Personally built an AI agent (April 2026) that generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents, removing a recurring manual reconciliation task."
4. "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance." ("Middle-platform" is not common English.)
5. "When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept." ("The requirement lead" is unclear, and the sentence has no subject.)
6. "Production AI code review on headless Claude Code agents, prompt A/B evaluation, AgentOps/LLMOps practice, human-in-the-loop governance, delivery KPIs" (Core Competencies row). It is a wall of tool and practice names.

Borderline, not counted: the "Production Rigour" and "Hands-On Engineering" rows are acronym-dense (SLIs/SLOs, RCA, JVM tuning), but a recruiter can skim past them, and the abbreviations are expanded in the Summary.

---

## (b) Hiring manager, about 3 minutes

**1. Can he do this job?**

Clearly evidenced:
- 3+ years in an engineering management role: UOB since Oct 2022, leading 10 plus 15 engineers, and earlier technology-head roles.
- 8+ years of software development: Renren, Sohu and Baidu (2008–2014), and the hands-on coding claims at UOB.
- Operational rigour: P1–P3 incidents, RCA, SLIs/SLOs, DR drills, change-failure rate and MTTR.
- Extensible platforms for other teams: the payment-initiation hub, the customer-360 platform that serves APIs to several business lines, and the multi-tenant SaaS.
- Cross-region collaboration: India, Thailand and Indonesia.
- Payments: strong, though it is bank-side (initiation, ISO 20022, reconciliation, collections) rather than card-acquiring or disputes.

Thin or missing:
- **Hiring.** There is no sentence about recruiting, interviewing or closing candidates. The JD lists hiring as a minimum requirement and as a responsibility.
- **Career development with stretch assignments.** "1:1s, mentoring and performance management" appears, but no outcome (a promotion, someone growing) is shown.
- **Product and strategy involvement.** The resume shows delivery and governance, not shaping product direction. The AI Park and VV entries mention product-strategy planning only briefly.
- **Disputes, chargebacks, issuer or scheme relationships.** Not shown. The JD says "familiarity with payment processing", so this is a domain gap, not a disqualifier.
- **Fast-paced, ambiguous environments.** Implied by the start-up history, but the recent seven years are in a regulated bank.

**2. Hard red flags and inconsistencies.**
- **Headcount claims.** The Summary says "140-person technology organisation (total headcount)" at VV, but the VV section has no team size. Golden Bridge says "40-person project team (total headcount)". A reader will ask whether these are direct teams or organisation totals.
- **Reporting structure.** "Lead both platform teams through squad leads and engineering managers" implies two management layers under him for 25 engineers. Elsewhere he "leads the 10-engineer backend team" and the "15-engineer hub team" directly. Which is it?
- **Overlapping dates.** Hengshunyuan co-founder (Oct 2017 – Sep 2019, China) overlaps VV Technology (from Apr 2019, Singapore). It is plausible but unexplained.
- **Gaps.** Dec 2014 to Apr 2016, about 5 months in 2020, and 3 months in 2022. The Summary's "(2008–2014)" and "(2016–2022)" make the first gap visible.
- **Metrics that read as soft.** "Cut senior engineers' review time by an estimated ~80%" is flagged as an estimate, which is honest. "Personally led DR drills, sustaining 99.9%+ availability" implies the drills caused the availability.
- **Level mismatch risk.** VP and "Head of Technical Centre" titles against a manager-of-a-single-team role. Not a flag in itself, but Stripe may ask why he is stepping down.
- **Title mix.** "Vice President (VP2) / Technical Delivery Manager" gives two titles on one line.

**3. Questions I would ask.**
1. Tell me about the last engineer you hired: how you sourced, assessed and closed them. How many have you hired at UOB?
2. How many direct reports do you have? Who are your squad leads and engineering managers, and how do you split your time between management and code?
3. Give me an example of an engineer you grew through a stretch assignment, and what happened.
4. In the payment hub, how do you handle a payment that ends in an unexpected status, or a dispute-like exception later? What would you design differently now?
5. Describe a product decision you drove, not just delivered. What did you push back on with product management?
6. What is the basis for the ~80% review-time reduction, and how did you measure 99.9%+ availability?

**4. Would I interview him?** **Yes**, for a screen. The management, payments, platform and operational evidence fits the minimum requirements. I would use the screen to test hiring track record and product-side involvement, which the resume does not show.

---

## Suggestions (wording, order and cuts only)

**W1. Fix the headcount parentheticals.**
- "has led VV Technology's 140-person technology organisation (total headcount)" → "has led VV Technology's technology organisation of 140 people".
- "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch…" → "Led a 40-person team, introduced Agile/Scrum from scratch…".

**W2. Rewrite the six hard-to-read sentences in plain English.**
- KYC: "Designed hierarchical KYC identity verification and rule models…" → "Designed the identity-verification (KYC) levels and the rules that decide bonus eligibility, triggers and payout."
- eMemo: cut the bullet. It is low relevance to this JD, the terms are unexplained, and cutting it frees a line. If kept: "Built an AI agent (April 2026) that checks eMemo and quotation documents for consistency, removing a recurring manual task."
- Middle-platform: "Designed the middle-platform architecture (…)" → "Designed the shared platform architecture (…)".
- MVP: "When the two platform lines' schedules conflict, agree MVP scope…" → "Resolve schedule conflicts between the two platform lines by agreeing minimum-viable scope with the requirement, project and technical leads and setting a sequence all parties accept."
- Competencies row: "Production AI code review on headless Claude Code agents, prompt A/B evaluation, AgentOps/LLMOps practice, human-in-the-loop governance, delivery KPIs" → "AI-assisted code review in production, prompt testing, human-in-the-loop governance, delivery KPIs".

**W3. Order and trims on page 1.**
- Move the "Leading and developing engineers" bullet to the top of Selected Achievements. The JD's first hard requirements are people leadership, and the current first bullet is platform design.
- Shorten the Summary's first paragraph, which spends two lines on Renren, Sohu and Baidu: "Started as a software engineer and technical lead on Renren's e-commerce platform, Sohu's news CMS and Baidu's Nuomi group-buying system (2008–2014), then led…" → "Started as a software engineer and technical lead at Renren, Sohu and Baidu (2008–2014), then led…".
- Remove the repeated "Singapore" in the contact line ("Singapore PR | … | Singapore").
- In the title line, keep only one title in the UOB heading, or put "Technical Delivery Manager" in brackets, to reduce the delivery-manager first impression.

## Facts the resume does not show (questions, not text to add)
- Has he personally hired or interviewed engineers, and how many? (JD minimum requirement.)
- How many direct reports does he have, and does the squad-lead and engineering-manager layer actually exist under him?
- Was the 140-person VV figure his own organisation, and when? Is there a way to describe the 2014–2016 and 2020 gaps?
- Any exposure to disputes, chargebacks, refunds or scheme and issuer relationships?
- Did he shape product direction with product management at UOB, as opposed to delivering to it?
- What is the basis of the ~80% review-time estimate?

---

## Resolution (2026-10-26)

**Applied**
- W1 — "(total headcount)" replaced by the batch readable qualifiers: VV "through its managers" (Summary and, now, the VV section, so the figure can be checked there); GBD "including outsourced staff". The GBD "40-person" figure is kept (required qualifier form, not cut).
- W2 — KYC bullet rewritten in plain English (same facts); eMemo agent bullet cut; "middle-platform" replaced by "shared back-end platform architecture"; MVP bullet uses the batch canonical sentence (subject-first; "MVP" and "requirement lead" kept for batch consistency); AI competency row simplified as suggested.
- W3 — "Leading and developing engineers" moved to the top of Selected Achievements; Summary paragraph 1 shortened as suggested.
- Also: hub achievement no longer ends in an ambiguous "which executes settlement"; DR/99.9%+ clause scoped to the real-time payment middleware (addresses the "drills caused availability" reading); SLIs/SLOs, MTTR, SIT/UAT written out.

**Not applied, and why**
- Remove the repeated "Singapore" in the contact line, and show one title only in the UOB heading — both are fixed by the renderer and the Drafting Brief (exact title).
- Hiring track record, direct-report counts, career-development outcomes, product-direction examples, disputes/chargebacks exposure, gap explanations — would add facts not on record (hiring claims are on the "never write" list).
