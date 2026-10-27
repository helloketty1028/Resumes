# Cold-read 08 — Wilson (TPM_Bank_Income_V1_0_0) vs Head, Technology Transformation (Income Insurance)

Inputs read: the resume text (draft, red markup ignored) and the JD. Nothing else.

## VERDICT: REVISE
Reason: the recruiter can name three matches, but I had to quote three sentences I could not follow or that are too jargon-heavy for HR (limit is two). All three are fixable by wording alone.

---

## (a) HR recruiter, 30 seconds

**1. Who is he?** Senior technology delivery leader, 18+ years. Most recent role: VP2 / Technical Delivery Manager at UOB (a Tier-1 Singapore bank) since Oct 2022, running cross-border payments and retail lending technology with about 25 engineers. Domain is banking and payments technology, with a transformation and AI-adoption slant. Singapore PR. The headline reads "Technology Transformation Leader", which lines up with the JD title, though his actual title is a delivery-manager title.

**2. Three strongest matches to the JD**
1. **Core-platform modernisation in a regulated institution.** Owned the ISO 20022 payments migration with roadmap, governance forums and steering-committee reporting, finished with no service interruption. This matches "modernization of core platforms" and "establish governance, reporting and decision-making forums".
2. **AI taken from idea to governed production.** An AI code-review service has been live since May 2026 after architecture and risk approval. He also contributed to a RAG assistant and coaches teams. This matches "AI adoption" and "AI use cases deployed and adopted".
3. **Vendor and commercial ecosystem.** He chairs governance of four IT vendors and has decision or joint-decision authority on investment, vendor selection and SOW/licence negotiation. This matches "manage system integrators, vendors and delivery partners" and "strategic technology investments".

(Close fourth: delivery KPIs and SIT/UAT sign-off reported to steering committees, matching "effective governance and risk management".)

**3. Biggest doubt.** Level and altitude. "Head, Technology Transformation" reports to the Chief Strategy Officer and has enterprise-wide scope. His evidence is a 25-engineer delivery organisation in one bank division. I see no C-suite engagement, no business case or benefits realisation, and no insurance exposure. PMP is only "in progress".

**4. Sentences I could not understand or that are too technical for HR (quoted exactly)**
1. "Led end-to-end design of the payment-initiation hub, integrating channels, reference data, vendor systems and core banking: the hub sends validated payments on, core banking executes settlement and the hub processes the results."
   The "hub sends validated payments on" is vague, and I could not tell what the hub does.
2. "Personally built an AI agent that generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents, removing a recurring manual reconciliation task."
   "Validation prompts", "schema alignment" and "data-relationship consistency" are engineer language, and "eMemo" is unexplained.
3. "Production AI code review and document-validation agent, human-in-the-loop governance aligned with MAS FEAT, contribution to a RAG knowledge assistant, coaching teams on AI-assisted engineering"
   "MAS FEAT" is left unexplained, while "MAS TRM" two lines below is glossed. "RAG" is unexplained here, though it is spelled out later in the experience section.

Minor, not counted: "it takes daily account summaries from core banking to support portfolio analysis" (customer-360 bullet) and "improved review quality through prompt A/B testing".

---

## (b) Hiring manager, about 3 minutes

**1. Can he do this job?**

Clearly evidenced:
- Modernisation of a core platform in a regulated setting, with dated milestones (go-live May 2025, retirement of the old mode Aug 2026).
- AI adoption beyond pilots: a production service with formal approval, a human-in-the-loop governance model, and the AI-adoption coaching he does.
- Vendor and partner management with real authority (four vendors, SOW/licence, vendor selection).
- Governance and risk: steering committees, KPIs, SIT/UAT sign-off, change control, MAS TRM.
- Programme mechanics: RAID, dependencies, release cadence, phased cut-over.
- 18+ years, a CS master's degree, and 0-to-1 platform building with large teams (VV 140 people, Golden Bridge 40).

Thin or missing:
- **Enterprise-wide scope.** Everything is one bank division, two platform lines.
- **C-suite stakeholder management.** There is "steering committee" and "senior management" but no named executive audience or outcome.
- **Benefits realisation and business cases.** The JD's success measures are benefits against approved business cases, productivity and adoption at scale. The resume gives one number, "~80% estimated" review-time saving. It shows no financial outcomes, adoption figures or budget sizes.
- **Strategy and roadmap ownership.** He owns the ISO 20022 roadmap, but there is no evidence of "translating strategic priorities into initiatives" at enterprise level.
- **Insurance domain.** Absent, though a banking-to-insurance move is plausible.
- **Transformation Office leadership.** He has led engineering teams, not a PMO or transformation office.
- **PMP.** In progress only (preferred, not mandatory).

**2. Hard red flags**
- **Title and altitude.** VP2 / Technical Delivery Manager applying for a Head role that reports to the CSO.
- **Team-size numbers.** "15-engineer team" (ISO migration), "25 onshore and offshore engineers" (UOB) and "10-engineer backend team" (customer-360) are probably nested, but a reader has to work that out. The Summary also frames him as a programme leader while the experience section says "Stay hands-on... write core modules", which pulls toward engineer.
- **Date overlaps and gaps.** Hengshunyuan co-founder (Oct 2017 – Sep 2019) overlaps VV Technology (Apr 2019 – Jun 2020) by about six months. There is a gap from Jun 2020 to Nov 2020 and a short gap from Jul 2022 to Oct 2022. These are minor but would be asked.
- **Estimated figure.** "~80%" is stated as an estimate, which is honest but soft.
- **Education.** The Master's is in Computer Science, which fits the JD. No issue.
- No overstatement that I could prove from the resume alone.

**3. Interview questions**
1. Walk me through the ISO 20022 programme: what was your own decision-making role versus your team's? What was the budget, who sat on the steering committee, and what was the hardest dependency?
2. Which executives did you report to or brief, and what did you need from them that you did not already have?
3. How did you measure the AI code-review service's benefit (the ~80% is an estimate)? What adoption and productivity numbers would you take into an Income business case?
4. This role is strategy-led and cross-functional, reporting to the CSO. How is the work you do today different from a Transformation Office role, and what would you do differently?
5. How would you build a roadmap in an insurer, a domain you have not worked in, with business, operations and compliance partners? And where do you stand on the PMP?

**4. Would I interview him?** **Yes.** Strong, recent modernisation, AI-to-production and vendor-governance evidence from a regulated Tier-1 institution at 18+ years' seniority. The level jump, thin executive and benefits evidence, and the insurance gap are things to probe in interview, not reasons to reject.

---

## Wording, order and cuts (no new facts)

1. **Payment-hub bullet (Transformation Programme Delivery).**
   Quote: "Led end-to-end design of the payment-initiation hub, integrating channels, reference data, vendor systems and core banking: the hub sends validated payments on, core banking executes settlement and the hub processes the results."
   Rewrite: "Led end-to-end design of the payment-initiation hub that connects channels, reference data and vendor systems to core banking: it validates each payment, passes it to core banking for settlement, then processes the result."

2. **eMemo bullet (Selected Achievements).**
   Quote: "Personally built an AI agent that generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents, removing a recurring manual reconciliation task."
   Rewrite: "Personally built an AI agent that automatically checks that eMemo and quotation documents are consistent with each other, removing a recurring manual reconciliation task."
   Also consider moving this bullet below the vendor and governance bullets. It is the weakest-scoped achievement for a Head-level role, and the strongest JD matches should come first.

3. **AI Adoption row (Core Competencies).**
   Quote: "human-in-the-loop governance aligned with MAS FEAT, contribution to a RAG knowledge assistant"
   Rewrite: "human-in-the-loop AI governance aligned with MAS FEAT (fairness, ethics, accountability, transparency) principles, contribution to a retrieval-augmented generation (RAG) knowledge assistant". If space is tight, cut "MAS FEAT" and write "aligned with MAS AI-governance principles". This matches how "MAS TRM (Singapore technology-risk rules)" is already glossed.

4. **Team-size clarity (Selected Achievements, first bullet).**
   Quote: "with a 15-engineer team"
   Rewrite: "with a 15-engineer team (within the 25-engineer organisation below)". This preempts the apparent inconsistency with "leading 25 onshore and offshore engineers".

5. **Weakest bullet (Selected Achievements, last).**
   Quote: "Resolve schedule conflicts between the payments and lending lines by agreeing minimum viable scope with the requirement, project and technical leads, then setting a sequence all parties accept."
   Suggestion: cut it, or shorten to "Resolve cross-line schedule conflicts by agreeing minimum viable scope and sequence with requirement, project and technical leads." It has no outcome and is the most generic line on page 1.

6. **Customer-360 bullet.**
   Quote: "it takes daily account summaries from core banking to support portfolio analysis and serves APIs to multiple business lines"
   Rewrite: "it feeds daily account summaries from core banking into portfolio analysis and serves data to multiple business lines" ("APIs" is acceptable; the main fix is the plainer verb).

7. **Prompt A/B testing.**
   Quote: "improved review quality through prompt A/B testing"
   Rewrite: "improved review quality by testing alternative AI instructions (prompt A/B testing)".

8. **Order.** Page 1 Selected Achievements currently reads modernisation, AI, automation, vendors, governance, VV, priorities. For this JD, swap the automation bullet (3) with the vendor bullet (4) and the governance bullet (5), as noted under item 2.

## Facts the resume does not show (questions only, not text to add)
- What is the size of the ISO 20022 programme's budget, and who sat on its steering committee?
- Which senior executives (C-suite) does he brief or report to at UOB?
- Is there any measured adoption or business outcome for the AI code-review service beyond the ~80% estimate?
- What does "eMemo" refer to, in a form a non-banker would understand?
- Is any of his work at UOB enterprise-wide rather than limited to his two platform lines?
- Any exposure to insurance, or to business-case and benefits-tracking processes?

## Resolution (2026-10-26)

**Applied**
- #1 Hub: canonical S2 wording, "it hands validated payments to core banking, which executes settlement, and processes the results returned".
- #2 eMemo: "checks eMemo and quotation documents against each other"; moved below the vendor and governance achievements.
- #3 AI Adoption row: "MAS FEAT AI principles" and "retrieval-augmented generation (RAG)". The full four-word FEAT expansion did not fit the 2-line limit, so the cold-read's space fallback was used.
- #4 Team size: the 15-engineer figure moved to UOB bullet 1 as "a 15-engineer onshore/offshore team (part of the 25)". The ISO 20022 achievement now uses the batch canonical sentence.
- #5 Priorities: tightened to the batch canonical MVP sentence instead of being cut.
- #6 Customer-360: "for portfolio analysis" (canonical).
- #7 "improved review quality by testing alternative prompts (prompt A/B testing)".
- #8 Order: vendor and governance now precede the automation bullet.

**Not applied, with reasons**
- Defining "eMemo": the record does not describe what an eMemo is, so no definition was added.
- C-suite audience, benefits realisation, adoption figures, insurance exposure and enterprise-wide scope: not on record. These remain interview questions.
