# Fact & Quality Audit — resume 08

**File audited:** `wilson-2026_TPM_Bank_Income_V1_0_0_draft.txt` (pdftotext of the rendered PDF; PDF and `.report.md` also read)
**Fact sources read (once each):** `01_Resume_Master_Rules.md` v1.1 · `02_Candidate_Profile.md` v3.1 · `03_Achievement_Library.md` v4.1 · `technical-skills-inventory.md` v2.3 · `fact-check-and-open-questions.md` v2.4 · `Session_Confirmations.md` S1–S9 `[CONF 2026-10-21]` (incl. the verified PRC Software Designer certificate in 02 §3).
**Not read (per brief):** `/cards/`, change log, matching analysis, resume.json. `04_Resume_Layout_Spec.md` and `05` were not in the audit inputs. No JD was provided, so job-fit was not assessed.
**Rendered pages:** viewed myself (PNG of all 3 pages of the PDF).

**Result: 58 claims audited — PASS 48 · REVIEW 9 · FAIL 1.**

---

## 1. Claim table

| # | Resume text (shortened) | Evidence | Checks | Verdict | Fix / note |
|---|---|---|---|---|---|
| 1 | WILSON · Singapore PR · +65 8655 9547 · email | 02 §1 (D-11, PR since 2024) | name, status, contact | PASS | Header has "Singapore" twice (PR … Singapore); cosmetic. |
| 2 | Headline "Technology Transformation Leader — Regulated Platform Modernisation · AI Adoption · Programme & Vendor Governance" | 01 §5, 02 §7 | no CTO/AI-engineer repackaging; target-style headline | PASS | Not one of the 02 §7 verbatim headlines; allowed by 01 §5 ("headline may name the target role"). |
| 3 | "18+ years across a Tier-1 bank, fintech and SaaS start-ups, and consumer internet platforms" | 02 §1, §4; 03 §0A | years, sectors | PASS | |
| 4 | "Modernises core platforms inside a regulated financial institution" | 03 PA-01; skills §9 "never claim core banking" | scope wording | REVIEW | "Core platforms" can be read as core-banking modernisation (a "never claim" area). See R2. |
| 5 | "takes AI from idea to governed production, with the engineering background to challenge architecture…" | PA-07, X-04; 03 C4 (own initiative ❓) | origin of idea | REVIEW | "from idea" implies he originated it; C4 remainder open. See R1. |
| 6 | "At UOB since 2022, owns the move of cross-border payments to ISO 20022 … roadmap, dependencies, governance forums and steering-committee reporting … without interruption" | PA-01.1, PA-01.5, §0A | O3 "owns"; start date; no-interruption 📄 | PASS | Wording matches PA-01.1 / 01.5. |
| 7 | "built AI tools for code review and document validation and coaches teams to adopt them under human-in-the-loop governance" | PA-07 (O1+O2), PA-08 (O1), PA-03 §6 | "built" ok; "adopt them" | REVIEW | Record says he coached teams on "AI-assisted engineering" (PA-03 §6, 📄); adoption of these two tools (C4: do all 25 use it?) is not on record; the eMemo agent has no team-adoption evidence. See R3. |
| 8 | "From 2016 to 2022, led technology for 0-to-1 digital platforms at start-ups and scale-ups — smart-parking IoT … VV … multi-tenant SaaS — building the teams and delivery processes from scratch" | PA-16, PA-11, PA-10; S8 | 0-to-1 per platform; "led technology" at GBD | REVIEW | 0-to-1 is documented for GBD (PA-10.1) and VV ("from scratch"); AI Park is not recorded as 0-to-1. At GBD he was Project Manager & Architect, not head of technology. "Building the teams" has no number attached, so no HR-9 problem. See R4. |
| 9 | "Brings that pace to vendor-heavy, regulated delivery today" | X-05 (four vendors) | rhetorical | PASS | |
| 10 | "PMP certification in progress" | 02 §3 | not "certified" | PASS | |
| 11 | CC Transformation Programmes: roadmaps, RAID, scope/schedule/delivery budget, phased migration, release cadence | PA-01.5, X-02, §0A | | PASS | |
| 12 | CC Platform Modernisation: ISO 20022 migration, core-banking integration, regional customer-360, 0-to-1 platforms on microservices and AWS | PA-01, PA-05, S2, PA-10/11; skills §2/§5 | "integration" ≠ core banking ownership | PASS | "Core-banking integration" is supported by S2 (hub sends payments; C360 takes daily summaries). Keep as "integration", never "core banking". |
| 13 | CC AI Adoption: "Production AI code review and document-validation agent, human-in-the-loop governance aligned with MAS FEAT, contribution to a RAG knowledge assistant, coaching teams on AI-assisted engineering" | PA-07, PA-08, S9, PA-03 §6 | "Production" scope | REVIEW | "Production" reads as applying to both the code-review service and the eMemo agent; only the code-review service is documented as in production (S9 gives the eMemo agent as "personally built, Apr 2026"). RAG is "contribution" (O5 ✔, S9). See R5. |
| 14 | CC Governance & Risk: steering committees, decision forums, KPIs, SIT/UAT sign-off, change control, secure SDLC, MAS TRM (Singapore technology-risk rules) | PA-01 §6/§9, PA-03, S9 | TRM gloss per S9 ✔ | PASS | "Steering committees" plural: see R6 (minor). |
| 15 | CC Vendors & Commercial: selection, SOW/licence negotiation, investment decisions, delivery budget, vendor reviews, onshore/offshore teams | X-02, X-05, S7 | buyer-side only | PASS | No vendor-side pre-sales claimed. |
| 16 | CC Stakeholders & Change: business, ops, compliance, architects, EMs; Agile adoption from scratch; cross-time-zone teams in India, Thailand, Indonesia | PA-01 §9, PA-10, X-02 | "collaboration, not line management" | PASS | "Cross-time-zone teams" is a collaboration claim, not line management. OK. |
| 17 | CC Methods & Tools: Agile/Scrum, hybrid Waterfall, Jira, Confluence, MS Project; Java, Spring Boot, microservices, AWS, Kubernetes | skills §1, §2, §5, §11 | depth P/A | PASS | Kubernetes = A, AWS = A/P (acceptable for bullets). |
| 18 | ACH1 "Owned the ISO 20022 (SWIFT MT-to-MX) migration … with a 15-engineer team: old and new message formats ran side by side from the May 2025 go-live, ahead of SWIFT's November 2025 deadline, until the old mode was retired in August 2026 with no service interruption" | PA-01 timeline, §7, PA-01.1, PA-01.5 | O3; 15 ✔; dates ✔ | PASS | "Side by side from May 2025" is an inference from the timeline (go-live → coexistence retired Aug 2026). It is consistent with PA-01 but not stated verbatim. Label "Core-platform modernisation": see R2. |
| 19 | ACH2 label "AI from idea to governed production: Designed and built an AI code-review service, live since May 2026 after formal architecture and risk approval: AI agents review each pull request but never approve or merge, cutting senior engineers' review time by an estimated ~80%" | PA-07.1–07.3, S9 | body fully supported; "estimated ~80%" qualifier ✔ | REVIEW | Body PASS. Label "from idea" → C4 (own initiative ❓). See R1. |
| 20 | ACH3 "Personally built an AI agent … eMemo and quotation documents, removing a recurring manual reconciliation task" | PA-08 (O1), S9 | | PASS | "Personally built" = O1 ✔. eMemo is a document type, not on the §7 list. |
| 21 | ACH4 "Chair governance of four IT service vendors — budget, performance and accountability reviews — and hold decision or joint-decision authority…" | X-05, X-02 | no vendor names | PASS | Label "Vendor and partner ecosystem": "partner" is not on record; suggest "Vendor governance" (cosmetic). |
| 22 | ACH5 "Established delivery KPIs — deployment frequency, recovery time, incident trend and change-failure rate — with SIT/UAT sign-off for every release, reported to senior management and steering committees" | PA-03.1; PA-01.5 | KPI wording ✔; reporting clause | REVIEW | PA-03.1 supports KPIs + SIT/UAT sign-off. "Reported to senior management and steering committees" is on record for the CBPR+ programme (PA-01.5, singular "steering committee"), not for the KPIs. See R6. |
| 23 | ACH6 "At VV Technology, headed a 140-person technology organisation through its managers and delivered the first release of the VV-Life local-life platform in 2019, including its payment subsystem" | S3, PA-11.2, §0A | **qualifier "(total headcount)" missing** | **FAIL** | S3 wording is "Led VV's 140-person technology organisation (total headcount)". The number is stated with no basis; "through its managers" does not disclose that 140 is total headcount (direct reports were 15–20). Fix F1. Release/payment-subsystem half is PASS (PA-11.2). |
| 24 | ACH7 "Resolve schedule conflicts between the payments and lending lines by agreeing minimum viable scope with the requirement, project and technical leads, then setting a sequence all parties accept" | X-02 (CONF 2026-10-16) | | PASS | |
| 25 | UOB: "Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations", Oct 2022 – Present | 02 §2 row 1 | exact | PASS | |
| 26 | "Technology delivery owner for two mission-critical platform lines in a MAS-regulated Tier-1 bank … leading 25 onshore and offshore engineers through squad leads and engineering managers" | X-02, §0A (25 = 15 + 10) | O3/O4; number | PASS | C6 (which team covers lending) is not claimed. |
| 27 | "Own end-to-end delivery of the payments modernisation programme … shipping upgrades every 2–3 months" | PA-01.5 | O3 | PASS | |
| 28 | "Led end-to-end design of the payment-initiation hub … the hub sends validated payments on, core banking executes settlement and the hub processes the results" | PA-01.2, S2, CF-N4 | hub does not settle ✔ | PASS | No MEPS+ claim; consistent with CF-N7 caution. |
| 29 | "Led the 10-engineer backend team of a regional customer-360 platform in production since 2022; takes daily account summaries from core banking … serves APIs to multiple business lines" | PA-05.1, PA-05.3, S2 | team size as scope, not "built"; C5 | PASS | Does not claim he led the 2022 launch. |
| 30 | "Own technology for retail unsecured-lending servicing … collections across credit-card and unsecured-loan portfolios" | PA-04.1 | verbatim | PASS | |
| 31 | "Took the AI code-review service from proposal to production: briefed senior management on the case and the governance model, and improved review quality through prompt A/B testing" | PA-07 §4, PA-07.4; C4 | "proposal"; content of the briefing | REVIEW | PA-07 records a 13-slide briefing to senior management, but not that he proposed the service (C4 ❓) or that the deck covered the governance model. Prompt A/B ✔. See R1. |
| 32 | "Coach teams on new delivery practices and AI-assisted engineering, under a governance model in which the AI advises but human reviewers keep approval and merge authority" | PA-03 §6, PA-07.2 | | PASS | |
| 33 | "Contributed to a production RAG knowledge assistant used across departments (2025), with access controls and data masking" | S9 | O5 verb ✔ | PASS | RAG is ❓ in the skills inventory, but S9 overrides it for this wording. |
| 34 | "Coordinate P1–P3 production incidents end to end … produce technical incident analyses that support the bank's regulatory reporting to MAS" | X-06 safe wording, CF-N2 | "input to" ✔ | PASS | |
| 35 | "Contributed to bank-wide SDLC, coding and code-review standards and to architecture-review governance; run secure SDLC, DPIA and data governance in line with MAS TRM" | PA-03.3, PA-03.4, CF-15 | locked verb ✔ | PASS | |
| 36 | "Led API and database encryption of sensitive data, credential management and data migration for the payment, lending and customer-data platforms" | X-01 | | PASS | |
| 37 | "Stay hands-on alongside delivery: review newly submitted core pull requests daily, co-design solutions with engineers, own the architecture, write core modules for significant changes and resolve production issues" | S5, X-04 | no "~50/~20", no full-time, no % | PASS | |
| 38 | Golden Bridge Drive (SG) Pte. Ltd. · Nov 2020 – Jul 2022 · Project Manager & Architect | 02 §2 row 3 | exact | PASS | |
| 39 | "A multi-tenant SaaS platform for online-game businesses, built 0-to-1 on AWS" | S9, PA-10.1 | permitted description only | PASS | |
| 40 | "Led a 40-person project team, including outsourced staff, introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness" | S4, PA-10.3 | "led" not "built"; basis disclosed | PASS | "Including outsourced staff" discloses the basis, which is the content of S4's "(total headcount)". Adding the literal "(total headcount)" would be cleaner but not required. |
| 41 | "Ran hybrid delivery: Waterfall for scope, budget, milestones and resource planning, with Agile sprints for execution, backlog tracking…" | PA-10 §4 (decision) | | PASS | Elaborates on "Waterfall for scope and budget, Agile sprints"; no new fact. |
| 42 | VV Technology Pte. Ltd. · Apr 2019 – Jun 2020 · Head of Technical Centre | 02 §2 row 4, S8 | S8 supersedes the 02 "Development" wording | PASS | |
| 43 | "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services" | PA-11 §1 | | PASS | |
| 44 | "Built VV's microservices platform from scratch on Spring Cloud, Kubernetes, Redis and AWS, owning technology selection and the technology budget" | PA-11.1; 01 §4 (O2 → not "built" unless O1) | verb vs ownership | REVIEW | PA-11.1 safe wording says "Built", but PA-11 ownership is O2 + PL (framework "O1/O2 ('I built')" 🔶) and 01 §4 bars "built" under O2 alone. Sources conflict. See R7. |
| 45 | "Designed the payment subsystem, which integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation" | S1 | O2 "designed" ✔; no direct card-scheme claim | PASS | |
| 46 | "Designed the shared back-end platform architecture for a B2B online-office product serving Southeast Asia, and governed its solution design, cost evaluation, staffing and acceptance" | PA-13 | GMS not named ✔ | PASS | "Shared back-end platform" is a plain-English rendering of "middle-platform". |
| 47 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans" | PA-11.3, PA-11.5, CF-N8 | | PASS | |
| 48 | AI Park · Apr 2016 – Sep 2017 · VP of Technical Department · China | 02 §2 row 6, S8 | | PASS | |
| 49 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform…" | PA-16.1 | | PASS | |
| 50 | "Led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing, and launched pilots … (2016), (2017), (2017)" | PA-16.2, S7 | bids only; no pricing/contract claim | PASS | |
| 51 | Hengshunyuan — Co-founder (Oct 2017 – Sep 2019): "Owned product, architecture and delivery of an audio-learning platform, reaching a peak of ~100k daily active users" | PA-15.1, D-10 | "~" kept; overlap with VV not annotated per D-10 | PASS | Dates are the proposed canonical (CF-05 still unverified against documents). |
| 52 | Baidu — Technical Specialist, Nuomi (May 2014 – Dec 2014): "As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan" | PA-17.1, 02 §2 row 7, CF-12 | 5–10M QPS not used ✔ | PASS | |
| 53 | Sohu.com — Technical Leader / Project Leader (Mar 2012 – May 2014): "Led the CMS re-architecture and contributed to the design of the news publishing workflow and its editorial review" | PA-18.1, PA-18.2 | O5 "contributed" ✔ | PASS | |
| 54 | Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012): "Developed Renren's shopping website, Renren Mall and CRM" | PA-19 | | PASS | |
| 55 | Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 | | PASS | |
| 56 | Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 | | PASS | |
| 57 | Software Designer (Intermediate) — Qualification Certificate … (2006) · PMP — in progress · SRE — formal training | 02 §3, CF-N5, Session note | no ID/DOB/cert numbers ✔; SRE provider/year omitted ✔ | PASS | |
| 58 | Languages: English and Mandarin (professional working proficiency in both) | 02 §1 | | PASS | |

Targeted scans of the text: no CEW / SCV / CCD / GMS / HCL, no "CTO" / "Chief Architect", no Board / C-suite / executive, no Pureland, Flink, 10M, "full-time". Numbers present (18+, 15, 10, 25, 2–3 months, ~80%, four vendors, 140, 40, ~100k, "two months ahead") all trace to 03 §0A or S1–S9. Only 140 lacks its qualifier (FAIL #23).

---

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to 03 / 02; no ❓/⚠️/⛔ outside permitted parts | **Failed (pending decision)** | "Idea" / "proposal" origin of the AI review service touches C4 (❓) — rows 5, 19, 31 (R1). |
| Dates and titles match 02 §2 exactly (as updated by S8); no CTO / Chief Architect | Passed | VV and AI Park titles follow S8. Hengshunyuan dates are the D-10 canonical dates. |
| Every number matches 03 Metrics Bank with qualifiers | **Failed** | 140 without "(total headcount)" — FAIL #23 (F1). |
| Verbs match ownership level | **Failed (pending decision)** | VV "Built" under O2 — row 44 (R7). All other verbs checked and acceptable. |
| Skills anchored in the inventory (P/A for Summary/bullets) | Passed | RAG is allowed by S9 (O5). |
| No CEW / SCV-CCD / vendor names / internal numbers | Passed | |
| Headline and Summary fit family × lens (02 §7, 05 §2) | Passed, not verified against a JD | TPM × BNK tone is plausible. 05 and the JD were not available to me. |
| Summary is narrative; no stacked repetition with Achievements / Experience | **Failed (minor)** | The ISO 20022 programme (roadmap, dependencies, steering) appears in Summary P2, ACH1 and UOB bullet 1. The AI code-review service appears in Summary, ACH2 and UOB AI bullet 1 (R8). |
| British spelling consistent; JD titles as written | Passed | |
| Layout per 04 | Not performed | 04 was not in my inputs. The render report says "Layout OK: True". |
| ≤ 3 pages; page numbers; no orphaned headings | Passed | 3 pages, "Page n of 3" footer, headings keep with their content (viewed). |
| Text extractable; renders as PDF | Passed | pdftotext is clean; the PDF was viewed. |
| File name per §10 | Passed (OQ-R3 still open) | `wilson-2026_TPM_Bank_Income_V1_0_0_draft`. I cannot verify the "Income" target segment. |
| Three-dimension review and change log delivered | Not performed | Out of scope for this audit (excluded by the brief). |

## 3. Document checks (render report + PDF viewed)

- **Pages:** 3 (limit 3), A4. Page 1 = header, headline, Summary, Core Competencies, Selected Achievements (7). Page 2 starts with Professional Experience. Page 3 holds Earlier Experience and Education only (about 30% of the page), so there is spare room for F1 and the R-fixes.
- **Page numbers:** "Page 1 of 3" to "Page 3 of 3" present.
- **Heading orphans:** none (report: `[]`; confirmed visually).
- **Bullets:** 30 bullets, 2 at three lines (ACH1, ACH2) = 7%, within 1 in 5. None above 3 lines. F1 may push ACH6 to 3 lines (3 of 30 = 10%, still fine).
- **Paragraphs:** Summary paragraphs 3 / 4 / 3 lines (≤ 4). UOB scope line 2 lines.
- **Summary:** about three short paragraphs, 155 words (01 §6).
- **Red text:** 52 of 93 runs are red. This is the "changes in red until approved" convention (01 §10); the final must be all black.
- **Lint hits / line flags:** none.

---

## 4. Summary

**PASS 48 · REVIEW 9 · FAIL 1** (58 claims).

### Required fixes

**F1 — Row 23 (ACH6, VV 140), qualifier missing.** Replace the bullet text with:

> Scale-up transformation: At VV Technology, led a 140-person technology organisation (total headcount) through its managers and delivered the first release of the VV-Life local-life platform in 2019, including its payment subsystem.

(S3 wording, "Led VV's 140-person technology organisation (total headcount)"; keeps "through its managers". Do not add "built" or a direct-reports figure other than S3's "15–20" if Wilson wants one.)

### For Wilson to decide (REVIEW)

- **R1 (rows 5, 19, 31): Did you originate the AI code-review service, or was it a team or management initiative?** Also, did the senior-management deck cover the governance model? (03 C4 remainder and PA-07 §4 are silent on both.) *Safe default:* Summary "takes AI into governed production"; ACH2 label "AI into governed production"; UOB bullet "Took the AI code-review service through formal architecture and risk approval into production: briefed senior management on the case, and improved review quality through prompt A/B testing."
- **R2 (row 4, also ACH1 label "Core-platform modernisation"): Is "core platforms" acceptable, given that a recruiter may read it as core-banking modernisation (skills inventory: never claim core banking)?** *Safe default:* "Modernises mission-critical payment platforms inside a regulated financial institution", and label ACH1 "Payments modernisation".
- **R3 (row 7): Do teams actually use the code-review service (C4: all 25?), and did you coach anyone on the eMemo agent?** *Safe default:* "…built AI tools for code review and document validation and coaches teams on AI-assisted engineering under human-in-the-loop governance."
- **R4 (row 8): Was the AI Park platform a 0-to-1 build, and is "led technology" fair for Golden Bridge, where your title was Project Manager & Architect?** *Safe default:* "From 2016 to 2022, led technology and delivery for digital platforms at start-ups and scale-ups — a smart-parking IoT platform through its city pilots, VV Technology's local-life platform and a multi-tenant SaaS platform — building teams and delivery processes from scratch at VV and Golden Bridge."
- **R5 (row 13): Is the eMemo validation agent in production use?** The record says built (Apr 2026) and "removed a recurring manual task", not "production". *Safe default:* "Production AI code review; a document-validation agent; human-in-the-loop governance aligned with MAS FEAT; …".
- **R6 (rows 14, 22): Were the delivery KPIs reported to senior management and steering committees? Is the plural "steering committees" correct, or is it one steering committee (PA-01.5)?** *Safe default:* end ACH5 at "…with SIT/UAT sign-off for every release." and use the singular "steering committee" in the competency row.
- **R7 (row 44): For the VV microservices platform, did you personally write the framework (R22: "I built the micro-service framework")?** 01 §4 allows "built" only with O1, while 03 PA-11.1 uses "Built". *Safe default:* "Led the build of VV's microservices platform from scratch on Spring Cloud, Kubernetes, Redis and AWS, owning technology selection and the technology budget." Keep "Built" only if you confirm you wrote the framework code.
- **R8 (QA, advisory): Stacked repetition.** The ISO 20022 programme and the AI code-review service are each described in the Summary, in Selected Achievements and in the UOB experience section. *Safe default:* trim Summary P2 to one sentence on outcome ("…owns the move of cross-border payments to ISO 20022 through a phased migration that kept payments running without interruption") and drop the "roadmap, dependencies, governance forums and steering-committee reporting" list, which UOB bullet 1 already carries.

## Resolution (2026-10-26)

**F1 (row 23, VV 140): fixed.** The text now reads "Technology organisation: Led VV's 140-person technology organisation through its managers and delivered the first release of the VV-Life local-life platform in 2019, including its payment subsystem." Per Revision Brief §1.4/§2, the batch uses the readable canonical qualifier "through its managers" for the 140 total, not the parenthetical "(total headcount)". The "Scale-up transformation" label was replaced because "scale-up" is not on record (audit 06 Sum-3).

| REVIEW | Resolution |
|---|---|
| R1 (rows 5, 19, 31) idea/proposal origin | Default applied: Summary "takes AI into governed production"; label "AI into governed production"; UOB bullet "Took the AI code-review service through formal architecture and risk approval into production: briefed senior management on the case, …". Left for Wilson: did you originate the service, and did the senior-management deck cover the governance model? |
| R2 (row 4, ACH1 label) "core platforms" | Default applied: "mission-critical payment platforms"; label "Payments modernisation". The competency row now uses "hand-off to core banking for settlement". |
| R3 (row 7) team adoption | Default applied: "coaches teams on AI-assisted engineering under human-in-the-loop governance". Left for Wilson: do all 25 engineers use the review service? |
| R4 (row 8) 0-to-1 / "led technology" | Default applied, with "scale-ups" changed to "technology companies" for batch consistency. Left for Wilson: was AI Park a 0-to-1 build? |
| R5 (row 13) "Production" scope | Default applied: "Production AI code review; a document-validation agent; …". Left for Wilson: is the eMemo agent in production use? |
| R6 (rows 14, 22) KPI reporting / plural | Default applied: ACH5 ends at "…for every release."; competency row uses the singular "Steering committee". Left for Wilson: are the delivery KPIs reported to the steering committee? |
| R7 (row 44) "Built" VV microservices | **Not changed.** "Built its microservices platform from scratch" is the brief §2 canonical VV wording used in Wilson's approved resumes. Left for Wilson: did you personally write the framework code (R22 "I built the micro-service framework")? If not, change to "Led the build of". |
| R8 stacking | Default applied: Summary P2 trimmed to one outcome sentence on ISO 20022; the roadmap, dependencies and steering list remains only in UOB bullet 1. |

**Certificate:** the "Software Designer (Intermediate)" line is unchanged (verified, 02 §3).

Re-render: Layout OK: True, 3 pages, 4/30 bullets at 3 lines, 0 lint hits.
