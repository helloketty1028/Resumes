# Resume Fact Audit — NN = 10

**File audited:** `wilson-2026_SM_Internet_CMACGM_V1_0_0_draft.txt` (pdftotext of the PDF; PDF and `.report.md` read too)
**Rendered pages viewed:** yes, all 3 pages of the PDF were rasterised and looked at (70 dpi).
**Sources read:** `01_Resume_Master_Rules.md` v1.1 · `02_Candidate_Profile.md` v3.1 · `03_Achievement_Library.md` v4.1 · `technical-skills-inventory.md` v2.3 · `fact-check-and-open-questions.md` v2.4 · `Session_Confirmations.md` S1–S9 `[CONF 2026-10-21]`. Not read (per brief): `cards/`, change log, matching analysis, resume.json, the JD, 04 and 05.
**Evidence tags:** 02 §, 03 IDs (PA-/X-), Sk = skills inventory, S# = session confirmation.

---

## 1. Claim-by-claim table

| # | Resume text (shortened) | Evidence | Checks | Result | Fix |
|---|---|---|---|---|---|
| H1 | Header: Wilson · Singapore PR · +65 8655 9547 · email | 02 §1 | Name rule D-11, PR since 2024 [CONF], phone, email. No LinkedIn, no legal name | PASS | |
| H2 | Headline: "Technology Leader — Applied AI Adoption & Rapid Prototyping \| Governed AI in Production · Data Teams" | 01 §5, 02 §7 | Names target, not a past title, not "AI engineer". "Technology Leader" fine. "Rapid Prototyping" has no evidence: no prototype stage or speed on record (see R1) | REVIEW | Q-R1 |
| S1 | "takes AI from prototype to governed production … turns it into measurable productivity" | PA-07 §1/§8, S9 | "Governed production" ✅. "Prototype" stage not on record. "Measurable" vs an estimate (PA-07 interview rule: not "measured telemetry") (see R2) | REVIEW | Q-R2 |
| S2 | "with 18+ years of IT leadership across a Tier-1 bank, start-ups and scale-ups, and consumer internet platforms" | 02 §1 (18+ years total experience), 02 §2 | 18+ years is total experience; Renren 2008–12 was Senior R&D Engineer (hands-on, not leadership). "18+ years of IT leadership" overstates | **FAIL** | See Required fix 1 |
| S3 | "Began as an engineer and technical lead at Renren, Sohu and Baidu, then held head-of-technology roles from 2016 to 2020" | 02 §2 rows 7–9, 01 §5 | Wording matches 01 §5 ("head-of-technology roles (2016–2020)"). No CTO | PASS | |
| S4 | "Since 2022, a Vice President in UOB's Group Technology & Operations, leading 25 onshore and offshore engineers on mission-critical payment and lending platforms" | 02 §2 row 1; 03 §0A, X-02 | Oct 2022; 25 in the Metrics Bank; "leading" fits O4/PL; no internal names | PASS | |
| S5 | "designed and built a production AI code-review service and an AI agent for document validation" | PA-07.1 (O1+O2), PA-08 (O1), S9 | Service ✅. Agent: "personally built" ✅ S9. "Designed" on the agent is within the O1 "personally wrote" | PASS | |
| S6 | "and set the human-in-the-loop rules that govern them" | PA-07.2 | The AI-advises / human-approves rule is on record for the code-review service only. "Rules … govern them" extends it to the eMemo agent, with no evidence | **FAIL** | See Required fix 2 |
| S7 | "Combines start-up delivery speed and data-team leadership with the security, privacy and reliability that a large enterprise expects" | PA-12, PA-16, X-01, PA-02 | Data-team leadership ✅ (VV, AI Park). Security, privacy and reliability ✅. "Delivery speed" has no evidence (see R3) | REVIEW | Q-R3 |
| S8 | "explaining technical choices in business terms to senior management and steering committees … taking part in vendor-selection and technology-investment decisions" | PA-01.5, PA-07 §4, X-02 | Senior management and steering committee ✅. Authority understated (safe). No Board or C-suite | PASS | |
| C1 | Applied AI in Production: LLM agents on headless Claude Code · agentic workflow orchestration · prompt A/B evaluation · AgentOps/LLMOps · "taking AI tools through formal approval into production" | Sk §8 (P), PA-07, S9 | Skills at depth P. Formal approval is on record for one service (S9). "AI tools" (plural) implies more (see R4) | REVIEW | Q-R4 |
| C2 | AI Governance & Privacy: HITL governance aligned to MAS FEAT · encryption and role-based access control for sensitive data · secure SDLC · DPIA | PA-07.2, X-01, PA-01.3 (permission matrix), PA-03.4, Sk §10 | All anchored. RBAC comes from the hub's permission matrix and the RAG access controls (O5). "For sensitive data" is a compact reading | PASS | |
| C3 | Prototyping & MVPs: "Rapid 0-to-1 platform builds, MVP scoping and sequencing, production-ready handover through CI/CD quality gates and acceptance-test sign-off" | PA-10, PA-11, X-02, PA-03 | 0-to-1 ✅ (GBD, VV). MVP scope and sequencing ✅ (X-02). Sign-off ✅. "Rapid" is unevidenced (see R5) | REVIEW | Q-R5 |
| C4 | Data & Analytics: "Leading big-data teams on Spark, Hive and HBase; Kafka messaging; customer data models; SQL; data analysis that supports business decisions" | PA-12 (R22 stack), PA-16, Sk §3/§4, PA-05.1, S2 | Teams and stack ✅ (A depth, historical 2016–20, dated in the Experience section). Kafka ✅. Customer data models ✅. SQL ✅ P. "Supports business decisions" is not on record; S2 supports "portfolio analysis" only (see R6) | REVIEW | Q-R6 |
| C5 | Enablement & Change: coaching on AI-assisted engineering · Agile/Scrum from scratch and CI/CD · contributing to bank-wide standards | PA-03 §6, PA-10 §6, PA-11.3, PA-03.3 | "Contributing" is the locked verb ✅ | PASS | |
| C6 | Stakeholders & Commercial: senior management, steering committees, vendor selection and governance, technology-investment decisions, technical bids, cross-time-zone teams | X-02, X-05, PA-16.2, S7 | Bids = AI Park only ✅ S7. No Board or C-suite | PASS | |
| C7 | Platforms & Cloud: Java, Spring Boot, Spring Cloud, Apache Camel, microservices, AWS, Kubernetes, Docker | Sk §1/§2/§5 | All anchored at P or A. Spring Cloud, AWS, K8s and Docker are GBD/VV-era (A). Skills-line use, not a current hands-on claim | PASS | |
| A1 | Prototype to governed production: "Designed and built an AI code-review service … Spring Boot service runs headless Claude Code agents on each pull request … alongside SonarQube — live since May 2026 after formal architecture and risk approval" | PA-07.1, S9, PA-07 §8 | O1+O2 so "designed and built" ✅. Go-live May 2026 and approval ✅. Label "Prototype…" see R2 | PASS | |
| A2 | Measurable productivity: "Cut … code-review time by an estimated ~80%: the AI clears syntax and basic issues, so human review rounds fall to 1–2 per pull request" | PA-07.3 | "Estimated ~80%" qualifier kept ✅. The label says "Measurable". PA-07.3 also states "each about 30% as long"; the draft drops it, so "1–2 rounds" alone doesn't show the 80% logic. The baseline R₀ is still ❓ (C2) | REVIEW | Q-R7 |
| A3 | Responsible AI: AI advises, never approves or merges; MAS FEAT; "contributed to a production RAG knowledge assistant used across departments, with access controls and data masking" | PA-07.2, S9 | Governance ✅. RAG at O5 ("contributed") ✅ S9 | PASS | |
| A4 | Workflow automation agent: "Personally built an AI agent that generates validation prompts … eMemo and quotation documents, removing a recurring manual reconciliation task" | PA-08, S9 | O1 ✅. "eMemo" is a document type, not an internal system name on the §7 list; it is in the PA-08 safe wording | PASS | |
| A5 | Data teams for decisions: "Led the big-data team that built VV Technology's data-analysis platform on Hive and Spark, providing analysis that supported business decisions; earlier led AI Park's big-data team for millions of real-time sensor and transaction events" | PA-12, PA-16 §4, 03 §0A | Team, stack and AI Park events ✅ 📄. "Providing analysis that supported business decisions" is an outcome with no source. PA-12 gives no outcome | **FAIL** | See Required fix 3 |
| A6 | Scale-up 0-to-1 delivery: "led a 140-person technology organisation (total headcount), built its microservices platform from scratch and delivered the first release of its local-life services platform in 2019, including the payment subsystem" | S3, PA-11.1/11.2, 02 §5 | 140 with "(total headcount)" ✅ S3. First release 2019 ✅. "Built" vs O2 (01 §4 lists "built" as not permitted unless O1 also applies; PA-11 O1 is "I built", 📄) (see R8) | REVIEW | Q-R8 |
| A7 | Enablement and change: Agile/Scrum from scratch (GBD); CI/CD, code standards, containerised deployment (VV); "contributed to bank-wide SDLC, coding and code-review standards" (UOB) | PA-10 §6, PA-11.3, PA-03.3 | ✅ locked verb "contributed" | PASS | |
| U0 | UOB header: Oct 2022 – Present · VP (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations | 02 §2 row 1 | Exact match | PASS | |
| U1 | Scope line: two mission-critical platform lines — cross-border payments and retail unsecured lending — millions of accounts | 02 §6.1, X-02 | ✅ | PASS | |
| U2 | Took the AI code-review service into production; briefed senior management on the case and the governance model; prompt A/B testing, AgentOps/LLMOps | PA-07 §4, PA-07.4 | ✅ (13-slide briefing) | PASS | |
| U3 | Coach engineering teams on AI-assisted engineering practices and tooling | PA-03 §6 [LIB] 📄 | ✅ present tense for current scope | PASS | |
| U4 | Led the 10-engineer backend team of a regional customer-360 platform … daily account summaries from core banking … designed its customer data models and personally built its data-analysis module and scheduled batch jobs | PA-05.1/05.2/05.3, S2 | 10 is scope. O1 + team lead ✅. Core banking per S2, not "core-banking systems expertise". No SCV-CCD | PASS | |
| U5 | Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation and status tracking | PA-01.2, Sk §2 | ✅. No claim that it settles or clears (CF-N4) | PASS | |
| U6 | Stay hands-on: review newly submitted core pull requests daily, co-design solutions, own the architecture, write core modules for significant changes, resolve production issues | S5, X-04 | Matches S5 wording; no "~50 / ~20 modules", no coding %, no "full-time engineer" | PASS | |
| U7 | Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration … 15-engineer team … live in May 2025, ahead of SWIFT's November 2025 deadline, with no service interruption | PA-01.1/01.5, 03 §0A | O3 ✅. 15 is scope. Dates ✅. "No service interruption" is 📄 and permitted | PASS | |
| U8 | When the two platform lines' schedules conflict, agree MVP scope … set a sequence all parties accept | X-02 ✅ [CONF 2026-10-16] | Verbatim safe wording | PASS | |
| U9 | Established delivery KPIs … CI/CD quality gates (99% SonarQube coverage gate, automated regression testing) and test sign-off for every release | PA-03.1/03.2, 03 §0A | 📄 safe wording; 99% kept as a gate. "Mean time to recovery" is the expansion of the library's MTTR | PASS | |
| U10 | Coordinate P1–P3 incidents end to end — escalation, communication, RCA, post-incident reports; no separate SRE team, teams own production support and monitoring | X-06, CF-N3, PA-02.3 | The MAS-reporting input is correctly left out | PASS | |
| U11 | Hold decision or joint-decision authority on technology investment, vendor selection, SOW and licence negotiation; chair governance of four IT service vendors | X-02, X-05 | No vendor names | PASS | |
| U12 | Report status, risks and decisions to senior management and steering committees; work closely with teams in India, Thailand and Indonesia | PA-01.5, X-02 | "Collaboration, not line management" kept; no US teams (D-09) | PASS | |
| G0 | GBD header: Nov 2020 – Jul 2022 · Project Manager & Architect | 02 §2 row 3 | Exact match (end date from [LIB] only, ✅ in 02) | PASS | |
| G1 | Architected and delivered, from 0 to 1, a multi-tenant SaaS platform for online-game businesses on AWS — KYC, bonus incentives, VIP tiers, analytics and multi-channel payments — on Spring Cloud and Kubernetes | PA-10.1, S9 | Business described as S9 allows. No "200+ countries" | PASS | |
| G2 | Led a 40-person project team, including outsourced staff; set up CI on Jenkins and Amazon ECR; owned delivery budget, capacity and launch readiness | S4, PA-10.3, 02 §5 | "Led", not "built" ✅. S4 qualifier "(total headcount)" is worded as "including outsourced staff", which is S4's content, so the substance holds. Optional: use "(total headcount)" as at VV for consistency | PASS | |
| G3 | Applied data privacy impact assessments, API and database encryption and credential management to the AWS deployment, and led data migration | X-01, PA-10 §6, Sk §10 | ✅ ("to the AWS deployment" is a mild inference) | PASS | |
| V0 | VV header: Apr 2019 – Jun 2020 · Head of Technical Centre | S8, 02 §2 row 4 | S8 supersedes "Development" | PASS | |
| V1 | VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services — through data | PA-11 §1 | ✅ | PASS | |
| V2 | Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching … response times to the millisecond level | PA-11.4 | Verbatim; no % figure | PASS | |
| V3 | Designed the payment subsystem, which integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation | S1 | Verbatim S1. No direct card-scheme claim | PASS | |
| V4 | Designed the shared back-end platform architecture for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance | PA-13 | "Shared back-end platform" is a plain-English reading of "middle-platform". GMS name not used | PASS | |
| V5 | Defined production-incident priority levels and tiered emergency-response plans | PA-11.5, CF-N8 | ✅ | PASS | |
| P0 | AI Park header: Apr 2016 – Sep 2017 · VP of Technical Department | S8, 02 §2 row 6, CF-06 | Apr start is [CONF] (R22 says May, so low background-check risk) | PASS | |
| P1 | Led architecture, delivery, budget and the technical team for a smart-parking IoT platform … | PA-16.1 | Verbatim | PASS | |
| P2 | Added an AI processing step to licence-plate and portrait recognition … | PA-16.3, Sk §8 | "Added a step", not "trained models" ✅ | PASS | |
| P3 | Led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing; pilots 2016 / 2017 / 2017 | PA-16.2, S7 | Verbatim. No "1,000+ car parks", no "10M DAU" | PASS | |
| E1 | Hengshunyuan — Co-founder (Oct 2017 – Sep 2019): owned product, architecture and technical delivery … peak of ~100k DAU | PA-15.1, D-10, 02 §2 row 5 | "~" kept. Dates per D-10. VV overlap not annotated, as D-10 chose | PASS | |
| E2 | Baidu — Technical Specialist, Nuomi (May – Dec 2014): as project leader, re-architected the merchant-side order system on Dubbo microservices, two months ahead of plan | PA-17.1, 02 §2 row 7 | No "5–10M QPS" | PASS | |
| E3 | Sohu.com — Technical Leader / Project Leader (Mar 2012 – May 2014): led the re-architecture of the fifth-generation CMS, delivered OpenAPI messaging platform | PA-18.1, 02 §2 row 8 | ✅ | PASS | |
| E4 | Renren — Senior R&D Engineer (Jul 2008 – Mar 2012): developed shopping website, Renren Mall and CRM | PA-19, 02 §2 row 9 | ✅. No WeChat Pay, no payment claim (S1) | PASS | |
| D1 | Master's, Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 | Exact | PASS | |
| D2 | Bachelor's, Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 | Exact | PASS | |
| D3 | Software Designer (Intermediate) — Qualification Certificate … (2006) · PMP — in progress · SRE — formal training | 02 §3, S-note on 02 §3 certificate | Verified certificate allowed. No ID or file numbers. PMP "in progress", SRE "training" ✅ | PASS | |
| D4 | Languages: English and Mandarin (professional working proficiency in both) | 02 §1 | ✅ | PASS | |

**Table totals: 59 claims · PASS 48 · REVIEW 8 · FAIL 3**

---

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to 03 / 02; no ❓ / ⚠️ / ⛔ outside permitted parts | **Failed** | A5 outcome ("supported business decisions") and S6 ("govern them") have no source. Otherwise traces. VV stack uses only the R22 version (Hive, Spark), so the Flink ⚠️ is avoided. GBD ❓ business nature is described only as S9 allows |
| Dates and titles match 02 §2 / S8 exactly; no CTO / Chief Architect | Passed | All 8 roles checked. "Head-of-technology roles (2016–2020)" is the approved wording. Low-risk notes: AI Park Apr vs May (CF-06), GBD end date from [LIB] only |
| Every number matches 03 §0A with qualifiers | Passed with note | 18+, 25, 15, 10, 140 (total headcount), 40 (including outsourced), estimated ~80%, ~100k, 99% SonarQube coverage gate, two months ahead, May 2025 / Nov 2025, four vendors. No held numbers used (10M DAU, 200+, 1,000+). Note GBD 40's qualifier wording and the A2 omission of "each ~30%" |
| Verbs match ownership level | Passed with note | One REVIEW: A6 "built its microservices platform" (O2). Everything else OK: "Owned" O3, "Led" O4, "contributed" locked, "Personally built" O1 |
| Skills only if anchored, depth P or A | Passed | Every tool in Summary, bullets and Competencies has an inventory row at P or A. RAG appears only as the S9 "contributed" item, not as a skill. No Flink, Go, GCP, TOGAF, ITIL |
| No CEW / SCV-CCD / CCD / GMS / HCL / vendor names / internal numbers | Passed | Grep for CEW, SCV, CCD, GMS, HCL, Zhang, LinkedIn, CTO, Chief, Board, C-suite: no hits. "eMemo" is a document type (PA-08 safe wording) |
| Headline and Summary fit SM × INT (02 §7, 05 §2) | Passed with note | 05 not read, so not checked against the family × lens rules. Positioning stays "Technology Leader", never "AI engineer", but the page leads heavily with AI (Q-R1, Q-R2) |
| Summary narrative; no stacked repetition | Passed with note | Three short paragraphs (146 words). Summary para 2 echoes A1/A4; Competency 5 repeats U3 and A7; Competency 6 repeats U12. It is within the usual summary echo, and trimmable if space is needed |
| British spelling consistent; JD titles quoted as written | Passed / Not performed | Spelling OK (organisation, licence, containerised, Centre, licence-plate; grep found no American forms). JD title quoting: JD not in my inputs |
| Layout per 04 | Not performed | 04 not in my inputs. Checked against the brief's limits only (section 3) |
| ≤ 3 pages, page numbers, no orphaned headings | Passed | 3 pages, "Page x of 3" on each, no heading orphans (visually verified) |
| Text extractable, renders as PDF | Passed | pdftotext gives clean text; Carlito fonts embedded; no text boxes or images of text visible |
| File name per §10 | Passed | `wilson-2026_SM_Internet_CMACGM_V1_0_0` fits `[Family]_[Lens]_[Target]_V…` (OQ-R3 on the Lens segment is still open) |
| Three-dimension review and change log delivered | Not performed | Out of scope for this audit; the drafter's package was deliberately not read |

---

## 3. Document checks (rendered PDF viewed)

| Check | Result |
|---|---|
| Pages ≤ 3 | 3 (A4). Page 3 is about 35% used |
| Page numbers | Present on all pages ("Page 1 of 3" … "Page 3 of 3") |
| Heading orphans | None. Experience starts p2; Earlier Experience and Education sit mid-page on p3 |
| Page 1 = header + summary + competencies + achievements | Yes (7 achievements, then blank space). Page 2 starts at PROFESSIONAL EXPERIENCE |
| Paragraphs ≤ 4 lines | Yes. Summary paragraphs are 3 / 3 / 3 lines |
| Bullets ≤ 3 lines | Yes, none at 4 |
| ≤ 1 in 5 bullets at 3 lines | **Within limit but no headroom, and the report undercounts.** The render report says 5 of 32. My count from the rendered text is 6 of 32 (18.8%): A1, A3, A5 (p1); U4 customer-360, U7 ISO 20022 (p2); E1 Hengshunyuan (p3). One more 3-line bullet would breach the limit |
| Other layout notes | (a) The third AI Park bullet is stranded alone at the top of p3. (b) The VV scope line leaves "data." alone on a second line. (c) Hengshunyuan (2017–19) sits under "Earlier Experience" after AI Park, so the order is not strictly reverse-chronological, though Summary says head-of-technology roles ran 2016–2020. These are cosmetic. |
| Red change markup | Present (50/94 runs in red), as 01 §10 requires for an unapproved draft |

---

## 4. Summary

**PASS 48 · REVIEW 8 · FAIL 3** (59 claims)

### Required fixes (FAIL)

1. **Summary, sentence 1 (S2).** Replace "with 18+ years of IT leadership across a Tier-1 bank, start-ups and scale-ups, and consumer internet platforms" with **"with 18+ years in IT and leadership roles across a Tier-1 bank, start-ups and scale-ups, and consumer internet platforms"**. Reason: 18+ years is total experience (02 §1); the first four years at Renren were hands-on engineering.
2. **Summary, paragraph 2, last clause (S6).** Replace "and set the human-in-the-loop rules that govern them." with **"and set the human-in-the-loop rule that governs the code-review service."** Reason: the rule is on record only for the code-review service (PA-07.2).
3. **Selected Achievements, "Data teams for decisions" (A5).** Replace the whole bullet with **"Data teams: Led the big-data team that built VV Technology's data-analysis platform on Hive and Spark; earlier led AI Park's big-data team for millions of real-time sensor and transaction events."** Reason: "providing analysis that supported business decisions" has no source (PA-12 records no outcome). It was also removed from the label.

### For Wilson to decide (REVIEW)

| Q | Question | Safe default |
|---|---|---|
| **Q-R1** (H2) | Is there evidence of "rapid prototyping" (a prototype built first, or unusual build speed)? The record shows production services and 0-to-1 platforms, not a prototype stage. | "Technology Leader — Applied AI in Production & 0-to-1 Delivery \| Governed AI · Data Teams" |
| **Q-R2** (S1, plus A1 and A2 labels) | Did the AI code-review service start as a prototype you then productionised? And "measurable productivity" rests on an estimate (~80%, formula-based, baseline R₀ ❓ C2): keep the word? | Summary: "takes AI into governed production in a regulated enterprise and into productivity gains". A1 label: "Governed production". A2 label: "Productivity gain (estimate)" |
| **Q-R3** (S7) | "Start-up delivery speed": any evidence beyond Baidu "two months ahead of plan"? | "start-up 0-to-1 delivery" |
| **Q-R4** (C1) | "Taking AI tools through formal approval": formal approval is on record only for the code-review service. Did the eMemo agent or the RAG assistant also go through formal approval? | "taking an AI service through formal architecture and risk approval into production" |
| **Q-R5** (C3) | "Rapid 0-to-1 platform builds": any basis for "rapid" (timeline, time pressure)? PA-10 §5 says only "0 to 1 under time pressure". | Drop "Rapid" → "0-to-1 platform builds" |
| **Q-R6** (C4) | "Data analysis that supports business decisions": what does it refer to? S2 supports "portfolio analysis" (customer-360); PA-05.1 supports "wealth cross-sell and client management". | "data analysis for portfolio analysis" |
| **Q-R7** (A2) | Add PA-07.3's "each about 30% as long" so the 80% logic holds, or keep the shorter "1–2 rounds" (the baseline R₀ is still ❓ C2)? | Use the full PA-07.3 wording. It adds only about 6 words, but it would push the bullet to 3 lines, and the page is at its 3-line limit (see section 3) |
| **Q-R8** (A6) | "Built its microservices platform from scratch": did you personally build the framework (O1, "I built" in R22) or lead the build (O2)? | "led the build of its microservices platform from scratch" |

### Notes for the main session
- Layout: the render report's "3-line bullets: 5" should read 6; there is no headroom. Any fix that lengthens a bullet needs another bullet shortened.
- Education lines use the corrected degree names from 02 §3 (CF-01/02), which is right.

---

## Resolution (2026-10-26)

**FAIL**
- **F1 (S2): fixed verbatim.** "…with 18+ years in IT and leadership roles across a Tier-1 bank, start-ups and scale-ups, and consumer internet platforms."
- **F2 (S6): fixed verbatim.** "…and set the human-in-the-loop rule that governs the code-review service."
- **F3 (A5): fixed verbatim.** Label and text now read "Data teams: Led the big-data team that built VV Technology's data-analysis platform on Hive and Spark; earlier led AI Park's big-data team for millions of real-time sensor and transaction events." The bullet dropped from 3 lines to 2.

**REVIEW**
- **Q-R1 (H2): default applied.** Headline: "Technology Leader — Applied AI in Production & 0-to-1 Delivery | Governed AI · Data Teams". *For Wilson:* any evidence of a prototype stage or unusual build speed?
- **Q-R2 (S1, A1, A2): default applied.** Summary: "takes AI into governed production … and turns it into productivity gains". A1 label: "Governed production". A2 label: "Productivity gain (estimate)". *For Wilson:* did the code-review service start as a prototype?
- **Q-R3 (S7): default applied.** "Start-up 0-to-1 delivery."
- **Q-R4 (C1): default applied.** "Taking an AI service through formal architecture and risk approval into production". *For Wilson:* did the eMemo agent or the RAG assistant also go through formal approval?
- **Q-R5 (C3): default applied.** "Rapid" dropped. The label changed from "Prototyping & MVPs" to "0-to-1 Builds & MVPs", following Q-R1.
- **Q-R6 (C4): default applied.** "Customer data models for portfolio analysis" (S2).
- **Q-R7 (A2): left for Wilson.** The shorter "1–2 rounds" wording is kept. There is no headroom for another 3-line bullet. *For Wilson:* add "each about 30% as long" (PA-07.3) if space is freed, and confirm the R₀ baseline (C2)?
- **Q-R8 (A6): left for Wilson.** The canonical §2 VV sentence is used ("built its microservices platform from scratch"), because it is Wilson's approved wording. *For Wilson:* did you personally build it (O1), or lead the build (O2, "led the build of")?
- **G2 note:** the GBD bullet now uses the canonical §2 sentence ("including outsourced staff"). "(total headcount)" is removed everywhere, per the coordinator rule.

**Consistency fixes (coordinator rule, 2026-10-26):** "(total headcount)" is removed from A6, which now reads "through its managers". 99.9%+ and the permission matrix are not attached to lending or customer-data platforms anywhere in 10, so no change was needed there. No "Blue/Green", "MX-rich", "middle-platform", "high-traffic", "SSH to" or "RESTful" is present.

**Certificate:** "Software Designer (Intermediate)" is kept unchanged (verified, 02 §3).

**3-line budget (§3 note):** the PDF re-count after the revision is 4 of 32 (A1, A3, A6, ISO 20022). The renderer estimate is 5 of 32. Both are within the one-in-five limit. The AI Park entry no longer splits across pages, and the VV "data." widow is fixed.
