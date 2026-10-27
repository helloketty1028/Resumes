# Cold read 09 — NCS Associate Director, Solution Architect (Technical)

Inputs read: the resume text `wilson-2026_ATL_Internet_NCS_V1_0_0_draft.txt` and `09_NCS_JD.md`. Nothing else was opened. The text file shows no red markup.

## Verdict: REVISE

The recruiter can name three matches. The verdict is REVISE because six sentences are too technical or unclear for HR, and the rule allows at most two.

---

## (a) HR recruiter, 30 seconds

**1. Who is he?**
- He is a senior architect-leader with 18+ years of experience, currently a Vice President at UOB (a Tier-1 bank).
- He has led about 25 engineers on payment and lending platforms since Oct 2022.
- Before UOB he held head-of-technology roles at start-ups, in SaaS and consumer internet.
- The headline calls him a "Solution Architect", but the most recent job title is "Vice President (VP2) / Technical Delivery Manager". On a quick skim the headline and the title disagree.

**2. Three strongest matches to the JD**
1. **Reusable platform and asset design.** This is the JD's core. The resume shows a multi-tenant SaaS platform built "from 0 to 1" and a shared back-end platform for a B2B product, plus the summary line "designed for reuse".
2. **Modern architecture and integration.** The resume shows microservices, cloud-native, API contracts and a payment hub integrating channels and core banking. It matches the "microservices, cloud-native, API-first" requirement.
3. **Governance, sign-off and stakeholder communication.** The resume shows architecture-review governance, SIT/UAT technical sign-off, daily design reviews, mentoring, and steering-committee reporting.

Technical bids and risk and resilience (RAID logs, DR drills, MAS TRM) are also visible, so the count of three is safe.

**3. Biggest doubt or red flag**
- The doubt is "architect or delivery manager?". The current title is Technical Delivery Manager and the bullets lean to delivery and hands-on work ("Personally built…", "review core pull requests daily").
- The JD wants an Associate Director who signs off proposals, supports pre-sales and acts as technical authority with clients.
- Client-facing and pre-sales evidence is thin and old: the only bids are from 2016–17 in China.
- A smaller date point: Hengshunyuan (Oct 2017 – Sep 2019) overlaps VV Technology (Apr 2019 – Jun 2020) by about five months.

**4. Sentences I could not understand or that are too technical for HR (exact quotes)**
1. "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking."
2. "architected a phased, Blue/Green-style rollout that ran old and new message formats side by side"
3. "Led the 10-engineer backend team of a regional customer-360 platform that takes daily account summaries from core banking for portfolio analysis; evaluated Cloudera, designed the customer data models and personally built the Spring Batch jobs."
4. "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution."
5. "Led a 40-person project team (total headcount)" and "Led VV's 140-person technology organisation (total headcount)". It is not clear what "(total headcount)" means here (all staff, or direct reports).
6. "Established delivery KPIs — deployment frequency, MTTR, incident trend and change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing)". This is a wall of acronyms.

The Core Competencies lines are also dense jargon. Examples are "Java, Spring Boot and Apache Camel services" and "Risk and dependency logs (RAID)". I did not count them as separate quotes because they are keyword lists, which are acceptable.

---

## (b) Hiring manager, about 3 minutes

**1. Can he do the job?**

Clearly evidenced:
- **Scalable, reusable platform design.** Multi-tenant SaaS on AWS and a shared B2B back-end. The reuse is stated, but the resume does not show it being reused across several customers or verticals.
- **Microservices, cloud-native and API-first.** Evidence is strong and consistent across UOB, Golden Bridge and VV (Spring Cloud, Kubernetes, Kafka, AWS, API contracts).
- **Enterprise technology environment.** A Tier-1 bank under MAS TRM, with NFRs, resilience and security controls.
- **Delivery oversight and sign-off.** SIT/UAT sign-off on every release, quality gates, and a phased ISO 20022 migration with no service interruption.
- **Governance and mentoring.** Mentoring is stated and daily reviews are listed. Standards are described as "contributed".
- **Seniority.** VP at a bank, a 140-person technology organisation at VV, and a "VP of Technical Department" role at AI Park. The level equivalent to Associate Director is credible.
- **Stakeholder reporting.** Steering committees and senior management.

Thin or missing:
- **Systems-integrator or consulting context.** Everything is in-house product or bank platforms. I see no vendor-side delivery to external clients.
- **Pre-sales and sign-off of architectures for project proposals.** The only evidence is the AI Park bids from 2016–17. There is nothing recent.
- **"Establish" architectural standards.** The resume says he "contributed" to standards and to architecture-review governance, which reads as participation rather than ownership.
- **Multiple verticals and client engagements.** No client-facing work is shown, and the JD stresses "client-facing and internal leadership roles".
- **AI consulting (additional information in the JD).** There is an AI code-review service, but no consulting programmes.

**2. Hard red flags**
- **Title versus headline.** The headline says Solution Architect, while the current title is Technical Delivery Manager. Expect questions on how much of his time is architecture.
- **Date overlap.** Hengshunyuan (Co-founder, Oct 2017 – Sep 2019) overlaps VV Technology (Head of Technical Centre, Apr 2019 – Jun 2020).
- **Possible scope overstatement.** The summary says he "leads 25 engineers", while the experience section gives a 15-engineer team and a 10-engineer backend team. The two add up, but a reader has to do the sum.
- **Hands-on versus Associate Director level.** "Personally built the hub's core modules" and "personally built the Spring Batch jobs" read more like a senior engineer than an Associate Director.
- **AI Park bids are not in the role entry.** The Selected Achievements say he "led technical bids that won city parking projects", but the AI Park experience entry does not mention bids.
- **Summary-narrative gap.** The summary says "2016–2022 in head-of-technology and architect roles", but the next listed job after 2016 is Hengshunyuan, which is "Earlier Experience" and out of the main flow.
- Overstatement concerns are otherwise minor. The "no service interruption" and "99.9%+ availability" claims are specific rather than inflated.

**3. Interview questions**
1. Walk me through a time you reviewed and signed off a solution architecture before delivery. What did you reject or send back, and why?
2. In the multi-tenant SaaS and the shared B2B back-end, what exactly was reused, and how was reuse governed? Did a second customer or vertical adopt it?
3. Your current title is Technical Delivery Manager. How is your time split between architecture, delivery management and hands-on coding, and who owns architecture decisions at UOB?
4. Describe your client-facing and pre-sales work since the 2016–17 bids: how do you shape a technical narrative and test feasibility with a sales team?
5. How did you establish standards and review mechanisms, and what changed as a result?
6. (Clarification) How did Hengshunyuan and VV Technology overlap in 2019?

**4. Would I interview him?**
**Yes**, for a screening interview. The platform, integration and governance evidence is strong and the level fits. What remains to be tested is how much of him is architect versus delivery manager, and how deep his client-facing and pre-sales experience goes.

---

## Suggestions (wording, order, cuts only)

**S1. Latency bullet.**
Quote: "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking."
Rewrite: "Cut end-to-end transaction latency under high load by tuning the Java runtime and removing steps where one system waited idle for another."

**S2. ISO 20022 bullet.**
Quote: "architected a phased, Blue/Green-style rollout that ran old and new message formats side by side"
Rewrite: "architected a phased rollout that ran the old (MT) and new (MX) payment-message formats in parallel, so customers saw no interruption; live May 2025, parallel running ended August 2026".
This also lets "ISO 20022 (SWIFT MT-to-MX)" be glossed once as "the new SWIFT payment-message standard".

**S3. KYC bullet.**
Quote: "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution."
Rewrite: "Designed the tiered identity-verification (KYC) levels and the rules that decide bonus eligibility, triggers and payout."

**S4. Customer-360 bullet.**
Quote: "evaluated Cloudera, designed the customer data models and personally built the Spring Batch jobs."
Rewrite: "led the vendor evaluation (Cloudera), designed the customer data models and built the nightly batch jobs that load account summaries."
The word "nightly" is not in the resume, so use "daily batch jobs", which matches "takes daily account summaries".

**S5. Headcount parentheses.**
Quote: "Led a 40-person project team (total headcount)" and "Led VV's 140-person technology organisation (total headcount)".
Rewrite: "Led a 40-person project team, including…" or simply "Led a 40-person project team" and "Led VV's 140-person technology organisation".
Cut the parentheses unless the headcount definition matters.

**S6. KPI bullet.**
Quote: "Established delivery KPIs — deployment frequency, MTTR, incident trend and change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing) and SIT/UAT sign-off for every release."
Rewrite: "Set delivery KPIs (release frequency, recovery time, incident trend, change-failure rate) and automated quality gates, including a 99% code-coverage gate, regression and penetration testing, with SIT/UAT sign-off on every release."

**S7. Header and headline.**
Quote: "Singapore PR | +65 8655 9547 | Skyzhang1028@gmail.com | Singapore".
Cut the duplicate "Singapore" (keep "Singapore PR").
Reconcile headline and title. Either let the headline read "Solution Architect and Technology Leader — Reusable Platforms…", or put the architecture role first in the UOB line: "Vice President (VP2) / Technical Delivery Manager" is the real title and must stay, so soften the headline rather than the title.

**S8. Order: move the bids evidence into the AI Park role.**
The AI Park experience entry has no mention of bids, yet Selected Achievements features them. Move the sentence "led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing" into the AI Park entry and cut the pilot years from Selected Achievements, so the bullet is one line.

**S9. Governance wording.**
Quote: "Contributed to bank-wide SDLC, coding and code-review standards and to architecture-review governance".
"Contributed" undersells the JD requirement "Establish architectural standards". If the resume's own facts allow it, state what he personally defined or approved. If they do not, keep the wording and expect the interview question.

**S10. Order: Earlier Experience.**
Hengshunyuan (2017–2019) sits first and overlaps VV. Either move it below the dated roles or state the overlap as "part-time alongside" only if the facts support that (see questions below).

**Top three for the revision:** S1 plus S2 (plain-language rewrites of the two jargon-heavy bullets), S3 plus S4 (unclear KYC and customer-360 bullets), S7 (headline versus title).

## Facts the resume does not show (questions only, not text to add)
- What share of his UOB role is architecture decisions versus delivery management?
- Has he signed off architectures for proposals or supported pre-sales since 2017?
- Was the multi-tenant SaaS or the shared B2B back-end reused by more than one customer, vertical or product?
- Did he work with a systems integrator or consulting firm, or with external clients, at any stage?
- How did Hengshunyuan (Oct 2017 – Sep 2019) and VV Technology (Apr 2019 – Jun 2020) overlap?
- What happened between Baidu (Dec 2014) and AI Park (Apr 2016)?
- Does "contributed" to standards and governance mean he authored or approved them?

---

## Resolution (2026-10-26)

**Applied**
- **HR quote 1 / S1 (latency):** now reads "by tuning thread pools and the Java runtime (JVM) and removing blocking synchronous calls". "Waited idle for another system" was not used, because it reinterprets the fact.
- **HR quote 2 / S2 (ISO 20022):** replaced by the canonical brief §2 sentence. "Blue/Green-style" is gone, and the text says plainly that old and new message formats ran side by side.
- **HR quote 4 / S3 (KYC):** now reads "Designed tiered know-your-customer (KYC) identity verification and rule models for…". The original "distribution" was kept instead of "payout".
- **HR quote 5 / S5 (headcount parentheses):** "(total headcount)" is removed. The canonical readable forms are used: "Led a 40-person project team, including outsourced staff" and "Led VV's 140-person technology organisation through its managers".
- **HR quote 6 / S6 (KPI bullet):** MTTR is expanded to "mean time to recovery", and the list is restructured with parentheses and dashes. The 99% SonarQube gate is kept (a Metrics Bank figure).
- **S7 (headline vs title):** the headline now reads "Solution Architect & Technology Leader — Reusable Platforms and Integration Architecture in a Tier-1 Bank". The UOB title is unchanged.
- **Acronyms (brief §1.3):** DR, SIT/UAT, RCA and MTTR are expanded at first use. SLIs/SLOs became "service-level objectives". "The hub" in Experience now reads "the payment-initiation hub" at first mention.
- **Summary duplication:** P3 no longer restates SA2 or SA3. Daily review and governance appear in SA4 only.

**Not applied**
- **HR quote 3 / S4 (customer-360):** the wording is unchanged. "Led the vendor evaluation" would raise the ownership level (the record says "evaluated Cloudera"), and "batch jobs that load account summaries" is not on record.
- **S7 header "Singapore" duplicate:** the header is fixed by the renderer (Drafting Brief §3).
- **S8 (move the bids into the AI Park entry):** this would state the same fact twice (SA5). Page 1 must keep the only pre-sales evidence.
- **S9 ("contributed" to standards):** "contributed to" is the locked verb for bank-wide standards (01 §4, CF-15). Claiming ownership would overstate.
- **S10 (Hengshunyuan order / overlap):** the order follows the Drafting Brief and decision D-10. Explaining the overlap would add a fact. It is listed as a question for Wilson.
- **"Facts the resume does not show":** these are questions, not text. Pre-sales since 2017, systems-integrator or client work, and the share of architecture versus delivery were not added.
