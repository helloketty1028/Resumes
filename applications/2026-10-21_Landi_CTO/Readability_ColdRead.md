# 07 Cold Read: Wilson, SM_Bank_Landi_V1_0_0 vs Landi International CTO

Inputs used: the resume draft text and the JD only. Red markup is not visible in the text file and was ignored.

## VERDICT: REVISE

Reason: the recruiter can name three matches, but I quote more than two sentences that an HR reader could not follow (four are listed below). Under the verdict rule, that makes it REVISE. The content is strong; the fix is wording only.

---

## (a) HR recruiter, 30 seconds

**1. Who is he?**
A senior payments and fintech technology leader. He has 18+ years of experience and is currently a Vice President (VP2) / Technical Delivery Manager at UOB, a Tier-1 Singapore bank. He has led technology at start-ups and mid-size companies in Singapore and China. The headline says "Payments Technology Leader" and the title says "Delivery Manager", so he reads as a very senior delivery and technology head. He does not read as a title-holding CTO.

**2. Three strongest matches to the JD**
1. **Payments and fintech in a security-sensitive industry.** He owns a MAS-regulated bank's cross-border payments (ISO 20022) and lending platforms, and has built payment integrations in Singapore and China. This is the JD's core industry requirement.
2. **Senior technology leadership with budgets and teams.** He was VP of Technical Department at AI Park, led VV's 140-person technology organisation, and leads 25 engineers today. He owns the technology budget, vendor selection, and SOW/licence negotiation. This matches the "5 years in senior technology leadership", "budgets" and "distributed teams" requirements.
3. **Connected devices and hardware with AI.** At AI Park he headed technology for an IoT platform connecting car-park hardware to the cloud, with city rollouts. He has also built an AI code-review service that is live in production. This maps to "connected devices or integrated hardware and software" and "AI-enabled products".

**3. Biggest doubt or red flag**
The JD is a company-wide CTO role for overseas markets, reporting to the Board. His current title is "Technical Delivery Manager". The resume shows no Board exposure, no strategy ownership at a company-wide level, and no payment terminals. Several bullets are "personally built / reviews pull requests daily", which reads as senior engineer or delivery manager rather than CTO. The last true head-of-technology role ended in 2020.

**4. Sentences I could not follow, or that are too technical for HR (exact quotes)**
- "running old and new message formats side by side: live in May and August 2025, ahead of SWIFT's November 2025 deadline, with the transition retired in August 2026 without service interruption." (What was "retired"? Is "live in May and August" two launches? Reads as unclear.)
- "Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation, enrichment and status tracking — integrated with digital and branch channels, reference data and core banking, which executes settlement." (A long list of tools and terms; an HR reader cannot tell the point.)
- "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results returned by downstream systems."
- "Led the big-data team on HBase, MongoDB and Spark Streaming, processing millions of real-time sensor and transaction events."

Smaller items that also snag: "production AI agents (headless Claude Code)" in the competencies table; "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS)"; "re-architected the merchant-side order system on Dubbo microservices". I do not count these among the four above.

---

## (b) Hiring manager, about 3 minutes

**1. Can he do this job?**

Clearly evidenced:
- Payments and fintech domain, with regulatory discipline (MAS TRM, approvals, SIT/UAT, P1–P3).
- Technology budget, vendor governance, and SOW/licence negotiation (UOB, VV, AI Park, Golden Bridge).
- Leading large and distributed teams: 140-person technology organisation, 40-person project team, 25 engineers on and offshore, India/Thailand/Indonesia.
- Cloud-native architecture, microservices, APIs, Kubernetes, CI/CD, DevSecOps-style quality gates (Jenkins, SonarQube, security testing).
- Connected hardware and IoT (AI Park), including city bids and rollouts.
- AI: a production code-review service with governance (the AI never approves or merges), plus an agent that checks documents against each other.
- Platform modernisation (ISO 20022 migration, reducing technical debt).

Thin or missing:
- **Overseas market strategy for one company.** "Multi-market" is shown as platforms built at different times in China and Singapore, not as one company localising and supporting one product line across several countries at once.
- **Board and executive presentation.** Only "senior management and steering committees" appear.
- **Payment terminals** specifically. The hardware is car-park equipment, not payment devices.
- **Localisation and customer solution deployment** (the JD's central phrase): not shown directly.
- **Succession planning, career development** of the team: "mentoring and performance management" only.
- **Recent CTO-level scope.** The last role is a delivery-manager title within one bank division.

**2. Hard red flags**
- Level: the jump from "Technical Delivery Manager" to company CTO. The pitch is credible only if the earlier head-of-technology roles carry the story.
- Overlapping dates: Hengshunyuan co-founder (Oct 2017 – Sep 2019) overlaps VV Technology (Apr 2019 – Jun 2020), and there is a gap from Jul 2020 to Nov 2020. Minor, but a reader will notice.
- Headcount qualifiers: "140-person technology organisation (total headcount)" and "40-person project team (total headcount)" sit awkwardly beside the "Head of Technical Centre" title. Possible query on actual span of control.
- "Estimated ~80%" review-time reduction: estimate basis not explained.
- Repetition: the decision/joint-decision authority sentence appears three times (Summary, Core Competencies, UOB experience); the AI code review appears in the Summary, Achievements and Skills. This reads as padding.
- Bachelor's in Applied Mathematics is not on the JD's list, though "related discipline" probably covers it, and the Master's in Computer Science helps.
- Tagline "Strategy · Teams · Budgets" is vague next to the very specific rest.

**3. Interview questions**
1. You run delivery for two platform lines at UOB. What technology strategy or roadmap did you set yourself, and what did you present to the most senior audience (Board, executive committee)?
2. At AI Park and VV you worked across hardware, payments and cloud. How would you localise and support one product across, say, three new overseas markets at once? What did you do in China versus Singapore?
3. What was the real span of control behind "140-person technology organisation" at VV, and how many reported to you directly?
4. Which payment terminals or devices have you worked with, if any, and where did your hardware experience stop (AI Park only)?
5. Why move from a hands-on delivery role at a bank to a CTO role at a hardware and software company? How would you handle a lower-governance environment?

**4. Would I interview him?**
**Maybe, leaning yes.** The payments, connected-device, budget and AI evidence is broad and well matched. The level step to full CTO and the missing Board and overseas-strategy evidence need a conversation.

---

## Suggestions (wording, order, cuts only)

1. **ISO 20022 bullet (Selected Achievements).**
   Quote: "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration of UOB's cross-border payments, running old and new message formats side by side: live in May and August 2025, ahead of SWIFT's November 2025 deadline, with the transition retired in August 2026 without service interruption."
   Rewrite: "Owned delivery of UOB's cross-border payments migration to the new SWIFT ISO 20022 message standard. Went live in two phases (May and August 2025), ahead of SWIFT's November 2025 deadline, ran old and new formats in parallel, and switched off the old format in August 2026 with no service interruption."

2. **Payment-initiation hub (two UOB bullets).** Merge and cut tool lists.
   Quote: "Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation, enrichment and status tracking — integrated with digital and branch channels, reference data and core banking, which executes settlement." + "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results returned by downstream systems."
   Rewrite: "Led end-to-end design of UOB's payment-initiation hub (Java, Spring Boot, Apache Camel), which takes payments from digital and branch channels through validation and status tracking to core banking, where settlement is executed. Personally built its core modules: payment initiation, concurrency control, role-based permissions for corporate and individual users, and processing of status results from downstream systems."

3. **Repeated authority claim.** Keep it once in the UOB section (first bullet). Delete "Has decision or joint-decision authority on technology investment and vendor selection, owns the delivery budget and reports to senior management and steering committees." from the Summary, and delete "technology budget, vendor selection and governance, SOW/licence negotiation" duplication in the Leadership & Budgets row; shorten that row to "Technical and delivery teams led through squad leads; mentoring and performance management; technology budget; vendor governance."

4. **Big-data bullet at AI Park.**
   Quote: "Led the big-data team on HBase, MongoDB and Spark Streaming, processing millions of real-time sensor and transaction events."
   Rewrite: "Led the big-data team that processed millions of real-time sensor and transaction events (HBase, MongoDB, Spark Streaming)." Putting the result first and the tools in brackets lets an HR reader stop at the useful part.

5. **Competencies row.**
   Quote: "production AI agents (headless Claude Code)"
   Rewrite: "production AI agents (built with Claude Code)", or simply "production AI tools". The AI code-review achievement already carries the evidence.

6. **Order.** Move "Technology organisation and budget" (VV 140-person) up to second place in Selected Achievements, directly after the ISO 20022 bullet. For a CTO JD it is the strongest proof of scale and ownership, and currently sits fourth. Move "Distributed teams and governance" third.

7. **Cut.** The "Security-sensitive operations" achievement duplicates the Engineering Practice row and the UOB Reliability bullets. Cut it or merge it into one line under UOB.

8. **Wording.** In both the VV and Golden Bridge bullets, the parenthetical "(total headcount)" is read as defensive. Replace with "(all functions)" only if that is what it means; otherwise cut the parenthetical and keep the number in context.

## Facts the resume does not show (questions only, not text to add)

- Has he presented to a Board, an executive committee, or the C-suite, and on what? (JD asks for Board-level presentation.)
- Has he worked with payment terminals, POS or other payment hardware?
- Has he taken one product into several countries and localised it, at one company?
- What was the direct reporting line of the 140 people at VV?
- What is the basis of the "~80%" review-time estimate?
- What happened between Jul 2020 and Nov 2020, and how did the Hengshunyuan co-founder role overlap with VV in 2019?

## Resolution (2026-10-26)

**Applied**
- #1 ISO 20022: replaced with the batch canonical sentence. It names the two go-lives and says the old path was retired in August 2026.
- #2 Hub, first half: tools moved into brackets, "enrichment" cut, and the flow restated as "it hands validated payments to core banking, which executes settlement, and processes the results returned".
- #3 Repetition: authority now appears once in the Summary (no budget clause) and in full in UOB bullet 1. Competency row shortened to "technology budget; vendor governance".
- #4 AI Park big data: result first, tools in brackets.
- #5 "headless Claude Code" changed to "production AI code-review agents (Claude Code)".
- #6 Order: VV organisation second, Distributed teams third.
- #8 "(total headcount)": replaced with the batch's readable qualifiers ("through its managers"; "including outsourced staff"). The numbers stay, so the 140 and 40 qualifiers are kept.
- Minor: "middle-platform" became "shared back-end platform" (canonical).

**Not applied, with reasons**
- #2 Second half ("role-based permissions for corporate and individual users"): conflicts with audit R4. The canonical S6 "corporate- and user-role permission matrix" is kept.
- #7 Cut the security achievement: kept, with "role-based permissions" removed (R4), because the JD requires a "security-sensitive industry".
- #3 Remove authority from the Summary entirely: one clause is kept so the JD's investment, budget and vendor requirement is visible on page 1.
- "(all functions)": would add a fact.
- Board, payment terminals, multi-country localisation: not on record or held. Nothing added; these remain interview questions.
