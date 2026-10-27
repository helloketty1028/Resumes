# Independent Fact & Quality Audit — Resume 07

**File audited:** `wilson-2026_SM_Bank_Landi_V1_0_0_draft.txt` (pdftotext of the rendered PDF); PDF and render report read alongside. The three PDF pages were viewed as images at 75 dpi.
**Sources read:** 01_Resume_Master_Rules v1.1 · 02_Candidate_Profile v3.1 · 03_Achievement_Library v4.1 · technical-skills-inventory v2.3 · fact-check-and-open-questions v2.4 · Session_Confirmations S1–S9 `[CONF 2026-10-21]`. 04 and 05 were not read. `/cards/`, the change log, the matching analysis and resume.json were not read.
**Method:** every substantive claim was traced to 02 / 03 / skills inventory / S#, and the resume text was never used as evidence for itself. Automated grep on the text found no CEW, CCD, HCL, GMS, CTO, Chief, Board, C-suite, 10M, 1,000, 200+, Flink, Pureland or Alibaba. WeChat Pay appears only under Baidu. There are no US-style spellings.

## 1. Claim table

| # | Resume text (shortened) | Evidence | Checks | Result | Fix |
|---|---|---|---|---|---|
| H1 | Header: Wilson · Singapore PR · +65 8655 9547 · Skyzhang1028@gmail.com | 02 §1 (D-11, PR since 2024) | name form, contact, status | PASS | — |
| H2 | Headline "Payments Technology Leader — Fintech Platforms, Connected Devices & Multi-Market Delivery \| Strategy · Teams · Budgets" | 02 §4/§7; 01 §5 | no CTO or Chief Architect; no AI or big-data identity | PASS | — |
| S1 | Summary: "18+ years across a Tier-1 Singapore bank, payment-enabled SaaS and local-life platforms in Singapore, and consumer internet and IoT in China" | 02 §1 (18+), §2 | scope, geography | PASS | — |
| S2 | "Began as an engineer and technical lead at Renren, Sohu and Baidu, then spent 2016–2022 in head-of-technology and architect roles — heading technology for a smart-parking IoT platform, co-founding an audio-learning platform, leading VV's technology organisation and architecting a multi-tenant SaaS platform" | 02 §2 rows 3–9, §4 arc; 03 PA-16.1, PA-15.1, PA-11.1, PA-10.1; S3 | titles; no "CTO"; 02 gives "head-of-technology roles 2016–2020", and 2020–22 is covered by the GBD "Project Manager & Architect" title | PASS | Note: do not extend "head-of-technology" past 2020 |
| S3 | "Since 2022, a Vice President in UOB's Group Technology & Operations, owning architecture and delivery for mission-critical cross-border payment and retail lending platforms serving millions of accounts" | 02 §2 row 1, §6.1; 03 X-02, X-04, S5 | title, date, scope | PASS | — |
| S4 | "Has decision or joint-decision authority on technology investment and vendor selection, owns the delivery budget and reports to senior management and steering committees" | 03 X-02 ✅; PA-01.5 ("senior management and the steering committee", singular) | authority and budget are ✅. "Steering committees" is plural, but the record has one (the CBPR+ programme). The sentence repeats UOB bullet U1 almost word for word, which is stacking (01 §6 Merging) | REVIEW | See R1 |
| S5 | "Combines regulated-bank discipline with experience of connected hardware, city rollouts, payment integrations across China and Singapore, and architecture for a B2B product serving Southeast Asia" | 03 PA-16, S1, PA-13 | the VV payment integrations and the Baidu/Renren payment integrations are covered. "City rollouts" is in 02 §5 | PASS | — |
| S6 | "Evaluates new technology by putting it to work — most recently a production AI code-review service inside the bank" | 03 PA-07, PA-08 | 🔶 framing, factual anchor ✅ | PASS | — |
| S7 | "Works in English and Mandarin" | 02 §1 | — | PASS | — |
| C1 | Technology Strategy: roadmaps and selection, investment priorities, platform modernisation, capacity planning, reducing technical debt | 03 PA-01 §4/§7 (roadmap, technical debt 📄), X-02, PA-02 (capacity baselines), PA-11 (selection) | no metrics; all anchored | PASS | — |
| C2 | Payments & Fintech: "…core-banking settlement integration, card and wallet payment integrations, settlement reconciliation" | S2, CF-N4, S1, 03 PA-11.2 | The hub integrates with core banking, which executes settlement (S2). Read loosely, "core-banking settlement integration" could imply the hub does settlement (CF-N4 says it does not), and the skills inventory lists "core banking" under Never claim. Card and wallet integrations, and reconciliation, are covered by S1 | REVIEW | See R2 |
| C3 | Connected Devices & IoT: "Car-park hardware connected to the cloud, licence-plate and portrait recognition, real-time sensor and transaction events, SaaS model for business and government customers" | 03 PA-16 §1–§4, §0A (events 📄), skills §8 | Skills §8 records only "added AI processing step, not model training", so listing "licence-plate and portrait recognition" with no qualifier reads as a recognition-engineering competency. Customer wording is covered (PA-16 §2, §9 stakeholders) | REVIEW | See R3 |
| C4 | Multi-Market Delivery: platforms for Singapore, China, SEA; technical bids, city pilots and rollouts; production support; teams in India, Thailand and Indonesia | 02 §5; 03 PA-16.2, X-02 (collaboration, not line management), X-06 | the India/Thailand/Indonesia item is presented as "teams in…", not as line management | PASS | — |
| C5 | Leadership & Budgets: teams led through squad leads, mentoring and performance management, technology budget, vendor selection and governance, SOW/licence negotiation | 03 X-02, X-05; S7 (buyer-side) | O4 verbs; no vendor-side pre-sales | PASS | — |
| C6 | Engineering Practice: Agile/Scrum, CI/CD quality gates (Jenkins, SonarQube), security testing in pipeline, secure SDLC, delivery KPIs, DR drills, P1–P3 | 03 PA-03, PA-02.1, X-06; skills §5 (Jenkins P/A, SonarQube P/A) | skills depth is P or A | PASS | — |
| C7 | Architecture & AI: cloud-native microservices, APIs, event-driven integration (Java, Spring Boot, Spring Cloud, Kafka), AWS, Kubernetes; production AI agents (headless Claude Code) | skills §1–§3, §5, §7, §8: Java P, Spring Boot P, Spring Cloud A/P ❓, Kafka A/P (anchored ✅), AWS A/P, Kubernetes A, Claude Code P | all at depth A or P; Spring Cloud and Kafka are marked "depth ❓" but are at least A | PASS | — |
| A1 | "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration of UOB's cross-border payments, running old and new formats side by side: live in May and August 2025, ahead of SWIFT's November 2025 deadline, transition retired in August 2026 without service interruption" | 03 PA-01.1 (✅ dates / 📄 no interruption), §0A, PA-01 timeline | O3 "owned" ✅; dates ✅; the "no service interruption" qualifier is kept | PASS | — |
| A2 | "Headed technology for AI Park's IoT platform…, led the technical bids that won city projects in Shijiazhuang, Handan and Beijing, and launched pilots in all three (2016–2017)" | 03 PA-16.1, PA-16.2 ✅; S7 (bids = AI Park only), S8 | bids and pilots in the three named cities only; no "and others", no 4+ count; no 1,000+ car parks | PASS | — |
| A3 | "Designed VV's payment subsystem in Singapore, which integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation; earlier designed and coded Baidu Nuomi's payment-gateway integration with Alipay, WeChat Pay and UnionPay in China" | S1 (verbatim) | "Designed" is O2 for VV and "designed and coded" is O1+O2 for Baidu, both as S1 states. No direct card-scheme connectivity claimed. WeChat Pay is under Baidu, not Renren | PASS | — |
| A4 | "Led VV's 140-person technology organisation (total headcount) and built its microservices platform from scratch, owning technology selection and the technology budget" | S3 (verbatim for the first clause); 03 PA-11.1 (📄/✅ safe wording), skills (Spring Cloud A/P ❓) | The "(total headcount)" qualifier is present, and the 140 is scope, not paired with "built". "Built … platform from scratch" is the PA-11.1 library wording (R22 "I built the micro-service framework", 🔶). See the note under the checklist | PASS | — |
| A5 | "Lead 25 onshore and offshore engineers through squad leads, work with teams in India, Thailand and Indonesia, and set delivery KPIs such as deployment frequency, recovery time and change-failure rate" | 03 §0A (25), X-02, PA-03.1/03 §4 (KPIs, O3+O4) | The 25 is ✅. "Work with" keeps the India/Thailand/Indonesia item as collaboration. "Set" applies to KPIs (O3), not to bank-wide standards (the locked "contributed to" is used in U11). "Recovery time" is a fair reading of MTTR; no MTTR improvement is claimed | PASS | — |
| A6 | "Designed and built an AI code-review service in a MAS-regulated bank, live since May 2026 after formal architecture and risk approval; the AI never approves or merges, and senior engineers' review time fell by an estimated ~80%" | 03 PA-07.1–07.3 ✅, S9 | O1+O2 verbs ✅; "estimated ~80%" qualifier kept; no 70–80% defect claim, no 30–40% ramp-up claim, no adoption scope | PASS | — |
| A7 | "Designed security controls — encryption of sensitive data, credential management and role-based permissions — for payment, lending and customer-data platforms; personally led disaster recovery (DR) drills, sustaining 99.9%+ availability under peak load" | 03 X-01 ✅ (API and database encryption, credential-file management, data migration); PA-01.3(b) (permission matrix, personally coded, hub only); PA-02.1 (📄/✅) | Encryption and credentials match X-01. "Role-based permissions" is not in X-01; it is the payment hub's authorisation layer, which Wilson personally coded (O1). Presenting it as a "designed" security control across "payment, lending and customer-data platforms" extends it. DR drills and 99.9%+ are 📄/✅ as worded | REVIEW | See R4 |
| U0 | UOB header: "Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations", Oct 2022 – Present; scope line (two platform lines, MAS-regulated, millions of accounts) | 02 §2 row 1, §6.1 | title and dates match exactly | PASS | — |
| U1 | "Hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and own the delivery budget" | 03 X-02 safe wording (verbatim) | UOB commercial authority is buyer-side (S7). Near-verbatim repeat of S4: see R1 | PASS | — |
| U2 | "Chair vendor governance for four IT service vendors — periodic budget reviews, year-end performance reviews and accountability meetings" | 03 X-05 (verbatim); 01 §7 | no vendor names | PASS | — |
| U3 | "When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept" | 03 X-02 (verbatim) | — | PASS | — |
| U4 | "Own technology for retail unsecured-lending servicing — payment initiation, validation and lifecycle tracking — and post-disbursement collections across credit-card and unsecured-loan portfolios" | 03 PA-04.1 (verbatim) | — | PASS | — |
| U5 | "Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation, enrichment and status tracking — integrated with digital and branch channels, reference data and core banking, which executes settlement" | 03 PA-01.2, S2, CF-N4; skills (Camel P, Spring Boot P) | O2 "led design" ✅. Settlement is correctly attributed to core banking, not the hub. No CEW name | PASS | — |
| U6 | "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results returned by downstream systems" | 03 PA-01.3 ✅; S6 (concurrency control) | O1 "built" ✅ | PASS | — |
| U7 | "Stay hands-on alongside delivery: review newly submitted core pull requests daily, co-design solutions with engineers, own the architecture and resolve production issues" | S5 | no "~50/~20 modules", no "full-time", no coding percentage | PASS | — |
| U8 | "Led the 10-engineer backend team of a regional customer-360 platform in production since 2022, which takes daily account summaries from core banking for portfolio analysis; personally built its data-analysis module" | 03 PA-05.3, PA-05.2 ✅; S2 | The 10 is scope (a sub-total of the 25). Does not claim to have led the 2022 launch (C5 open). The internal name SCV-CCD is not used | PASS | — |
| U9 | "Personally built an AI agent that checks eMemo and quotation documents against each other, removing a recurring manual reconciliation task (April 2026)" | 03 PA-08 ✅ (O1, Apr 2026); S9 | no time-saved figure | PASS | — |
| U10 | "Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, root-cause analysis and post-incident reports; with no separate SRE team, the platform teams own production support and Splunk-based monitoring" | 03 X-06, PA-02.3; 02 CF-N2, CF-N3 | no claim of MAS-reporting ownership; "own production support" matches CF-N3 | PASS | — |
| U11 | "Run CI/CD quality gates — automated regression and penetration testing, SonarQube coverage checks and SIT/UAT sign-off for every release — under MAS TRM (Singapore technology-risk rules); contributed to bank-wide SDLC and code-review standards" | 03 PA-03.2, PA-03.3 (locked "contributed to"), PA-03 §4; S9 (TRM gloss) | the 99% figure is omitted, so no qualifier problem | PASS | — |
| U12 | "Act as the interface between business, product, operations, compliance and engineering managers, and present status, risks and decisions to senior management and steering committees" | 03 PA-01 §9 stakeholders, PA-01 §6 ("executive status reporting"), PA-01.5 (singular steering committee) | The stakeholder list is on record. "Steering committees" is plural, and "present … risks and decisions" is broader than the on-record "reporting to senior management and the steering committee". No Board or C-suite, which is correct | REVIEW | See R1 |
| G0 | Golden Bridge Drive (SG) Pte. Ltd. · Singapore · Nov 2020 – Jul 2022 · Project Manager & Architect; scope "multi-tenant SaaS for online-game businesses, built 0-to-1 on AWS — KYC, bonus incentives, VIP tiers, analytics and multi-channel payments" | 02 §2 row 3; S9; PA-10.1 | title and dates exact; business described only as approved (S9) | PASS | — |
| G1 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness" | S4; 03 PA-10.3 | qualifier kept; 40 is scope and not "built" | PASS | — |
| G2 | "Architected the platform on Spring Cloud and Kubernetes behind an API gateway, with hierarchical KYC identity verification designed for many jurisdictions and multi-channel payments" | 03 PA-10.1, PA-10.2; CF-11 | The "200+ countries" figure is correctly replaced by "many jurisdictions". Spring Cloud and Kubernetes are at depth A | PASS | — |
| G3 | "Ran hybrid delivery — Waterfall for scope, budget, milestones and resource planning; Agile sprints for execution and iterative delivery" | 03 PA-10 §4 (decision: "hybrid delivery (Waterfall for scope and budget, Agile sprints)"); skills §11 | The hybrid model is ✅. The record covers only "scope and budget" for Waterfall and "sprints" for Agile; "milestones", "resource planning", "execution" and "iterative delivery" are not in the files I read | REVIEW | See R5 |
| V0 | VV Technology Pte. Ltd. · Singapore · Apr 2019 – Jun 2020 · Head of Technical Centre; "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services" | 02 §2 row 4; S8; 03 PA-11 §1 | title per S8, dates exact | PASS | — |
| V1 | "Took part in product-strategy planning and delivered the first VV-Life release in 2019, including the payment subsystem's transaction, management and reconciliation modules" | 03 PA-11.2, PA-11 §4 | "Took part" is O5-safe | PASS | — |
| V2 | "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance" | 03 PA-13 (safe wording) | the internal name "GMS" is not used; skills have RocketMQ A and MySQL P | PASS | — |
| V3 | "Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching … millisecond level" | 03 PA-11.4 ✅ (verbatim) | no % figure | PASS | — |
| V4 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans" | 03 PA-11.3, PA-11.5; CF-N8 | — | PASS | — |
| P0 | AI Park · China · Apr 2016 – Sep 2017 · VP of Technical Department; "Smart-parking IoT platform for business and government customers in China" | 02 §2 row 6; S8; 03 PA-16 §2, §9 | title per S8; dates per [CONF] | PASS | — |
| P1 | "Led architecture, delivery, budget and the technical team for the platform — automated car-park management, online payment and recommendations — and introduced its SaaS model" | 03 PA-16.1 ✅ | — | PASS | — |
| P2 | "Added an AI processing step to licence-plate and portrait recognition to improve recognition speed and accuracy" | 03 PA-16.3 (verbatim) | — | PASS | — |
| P3 | "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing" | 03 PA-16.4 ✅ (verbatim) | — | PASS | — |
| P4 | "Led the big-data team on HBase, MongoDB and Spark Streaming, processing millions of real-time sensor and transaction events" | 03 PA-16 §4 ("led the big-data team" [LIB]), §0A (events 📄); skills (HBase A/P, MongoDB P, Spark Streaming A/P ❓) | 📄 only, but stated as worded in the library; no Flink; "millions" is the §0A wording | PASS | — |
| E1 | Hengshunyuan Information Technology — Co-founder (Oct 2017 – Sep 2019, China): "Owned product, architecture and delivery of an audio-learning platform from market research to production, reaching a peak of ~100k daily active users" | 03 PA-15.1; 02 §2 row 5; D-10 | the "~" qualifier is kept; no overlap annotation, as D-10 decided; no 1,500 titles or cloud claimed | PASS | — |
| E2 | Baidu — Technical Specialist, Nuomi group-buying e-commerce platform (May 2014 – Dec 2014): "As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan" | 03 PA-17.1; 02 §2 row 7 | months from R22 📄 and the year is [CONF]; no QPS claim | PASS | — |
| E3 | Sohu.com — Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014): "Led the re-architecture of the fifth-generation news CMS and delivered its OpenAPI messaging platform" | 03 PA-18.1; 02 §2 row 8 | — | PASS | — |
| E4 | Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012): "Developed Renren's shopping website, Renren Mall and CRM, and designed and coded Renren Mall's payment integration with Alipay and UnionPay" | 03 PA-19; S1 | WeChat Pay is not listed under Renren | PASS | — |
| D1 | Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 ✅ | degree type left generic (FU-4) | PASS | — |
| D2 | Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 ✅ | — | PASS | — |
| D3 | Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006) | 02 §3 [CERT-SS] ✅; session note | no ID, date of birth or certificate number | PASS | — |
| D4 | "PMP — in progress" | 02 §3 ✅ | not written as certified | PASS | — |
| D5 | "Site Reliability Engineering (SRE) — formal training" | 02 §3, CF-N5 ✅ | not written as a certification | PASS | — |
| D6 | Languages: English and Mandarin (professional working proficiency in both) | 02 §1 | — | PASS | — |

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to 03 / 02 (no ❓ / ⚠️ / ⛔ outside permitted parts) | **Passed, with 6 REVIEW items** | S4, C2, C3, A7, U12 and G3 are judgement calls and not hold-list content. No held item is used: 10M DAU, 10M HTTP, QPS, 1,000+ car parks, 200+, Flink, GenAI chatbot, forecasting, 70–80%, 30–40%, Pureland and the "~50/~20 modules" figures are all absent |
| Dates and titles match 02 §2 / S8 exactly; no "CTO" or "Chief Architect" | **Passed** | UOB, GBD, VV (Head of Technical Centre), AI Park (VP of Technical Department), Hengshunyuan, Baidu, Sohu and Renren all match. The Pureland role and the Jan 2015 – Mar 2016 and Jul – Oct 2022 gaps are not mentioned, which is acceptable |
| Every number matches 03 §0A / S1–S9 with qualifiers | **Passed** | 18+, 25, 10-engineer, four vendors, 140 and 40 with "(total headcount)", ~100k, estimated ~80%, 99.9%+, "two months ahead" and the dates all have their qualifiers. No number is introduced that is outside §0A or S1–S9 |
| Verbs match ownership level (01 §4) | **Passed** | "Built" is used only for O1 items (U6, U8, U9, A6) and for the PA-11.1 library wording (A4). "Contributed to" is used for bank-wide standards. "Set" is used for KPIs (O3). The 140 and 40 are never paired with "built". Note on A4: "Led the 140-person organisation and built its microservices platform" is exactly the PA-11.1 sentence; ownership of "built" for the platform rests on R22 📄 and 02 §5 marks it 🔶. Acceptable as worded, but the sentence structure invites a reader to link "built" to the team, so keep "(total headcount)" |
| Skills anchored in the skills inventory (P/A for Summary and bullets) | **Passed** | All named technologies are P or A. Spring Cloud and Kafka are "A/P, depth ❓" but anchored. No Go, Flink, Node.js, Netty, RAG, vector databases, GCP or Istio |
| No CEW / SCV-CCD / vendor names / internal numbers | **Passed** | Verified by grep. The hub is "payment-initiation hub" and the C360 platform is "regional customer-360 platform". No GMS, no HCL |
| Headline and Summary fit the chosen family × lens | **Not performed** | The JD and the SM × BNK lens decision are outside the audit scope. The headline is consistent with 02 §4 and 01 §5, with no AI or big-data identity and no CTO wording |
| Summary is narrative; no stacked repetition with Achievements or Experience | **Passed with note** | The Summary is three narrative paragraphs. Stacking: the S4 authority and budget sentence is near-verbatim in U1 (see R1). The Achievements-to-Experience overlaps (A1 vs U-items and A3 vs V1) are expected by the template and are not verbatim |
| British spelling consistent; JD titles as written | **Passed** | organisation, licence, containerised, centre. No US forms found. The JD title cannot be checked |
| Layout per 04; ≤ 3 pages; page numbers; no orphaned headings | **Passed** (04 not read) | Rendered 3 pages, "Page n of 3" footers, no orphans. See section 3 |
| Text extractable; renders as PDF | **Passed** | pdftotext returned the full text; the PDF is tagged; no text boxes visible |
| File name per §10 | **Passed** | `wilson-2026_SM_Bank_Landi_V1_0_0_draft`: [Family] SM, [Lens] Bank, [Target] Landi; the "_draft" suffix is a draft marker |
| Three-dimension review delivered separately | **Not performed** | The matching analysis is outside the audit inputs |
| Change log listing | **Not performed** | The change log is outside the audit inputs |

## 3. Document checks

| Check | Result | Note |
|---|---|---|
| Pages ≤ 3 | **Passed** | 3 (pdfinfo and the render report agree) |
| Page numbers | **Passed** | "Page 1 of 3 / 2 of 3 / 3 of 3" |
| Heading orphans | **Passed** | None. The "Professional Experience" heading starts page 2 with its UOB block, and the AI Park heading, title and bullets start page 3 together |
| Bullets ≤ 3 lines; ≤ 1 in 5 at 3 lines | **Passed** | Report: 34 bullets, 4 at three lines (12%). I confirmed the four visually: A1, A3, A7 and U5. None has more than 3 lines |
| Paragraphs ≤ 4 lines | **Passed** | The Summary paragraphs are 4, 3 and 3 lines. The UOB, GBD, VV and AI Park scope lines are 1–2 lines |
| Page 1 = header + summary + competencies + achievements | **Passed** | Confirmed on the image; page 2 begins with Experience |
| Readability | **Passed** (visually inspected at 75 dpi) | Page 3 is about 40% full, so there is room to restore any trimmed item. Page 1 has a small blank band at the bottom |
| Red-marked changes | Note | The draft carries red runs (53/98), as 01 §10 expects until approval; the final must be all black |

## 4. Summary

**Counts (claim rows H1–D6, 60 rows): PASS 54 · REVIEW 6 · FAIL 0.**
The REVIEW rows are S4, C2, C3, A7, U12 and G3.

### Required fixes (FAIL)
None. No claim is unsupported, over-owned, un-qualified or confidential to the point that it must be deleted. No item from the held list appears.

### For Wilson to decide (REVIEW)

- **R1 — "steering committees" and the Summary/U1 repeat (S4, U12).** The record (03 PA-01.5) has one steering committee, and the Summary sentence repeats UOB bullet U1.
  Q: do you report to more than one steering committee, and do you present "decisions" to them, or is it status and risks to the CBPR+ steering committee?
  Safe default: change both to "senior management and the steering committee" in S4 and U12, and in S4 cut the authority sentence so it reads "…owns the delivery budget" only once (keep it in U1).
- **R2 — "core-banking settlement integration" (C2).**
  Q: do you want the row to say the hub integrates with core banking (which executes settlement), so it cannot be read as the hub doing settlement?
  Safe default: replace with "core-banking integration".
- **R3 — "licence-plate and portrait recognition" with no qualifier (C3).** Your record is that you added an AI processing step; it is not recognition-model work.
  Safe default: replace with "AI processing step in licence-plate and portrait recognition".
- **R4 — "role-based permissions" in the security achievement (A7).** It is the hub's permission matrix that you personally built, not a control listed under X-01 across payment, lending and customer-data platforms.
  Q: do you want to keep it as a designed control across platforms, or limit it to the hub?
  Safe default: delete "and role-based permissions" (the permission matrix is already in U6).
- **R5 — hybrid-delivery detail (G3).** The record says Waterfall for scope and budget, Agile sprints.
  Q: did you also run Waterfall for milestones and resource planning, and Agile for iterative delivery?
  Safe default: "Ran hybrid delivery — Waterfall for scope and budget; Agile sprints for execution."

## Resolution (2026-10-26)

**FAIL:** none.

| REVIEW | Resolution |
|---|---|
| R1 · S4 (Summary) | Default applied: singular "the steering committee"; "owns the delivery budget" removed from the Summary (kept once, in UOB bullet 1). Left for Wilson: do you report to more than one steering committee? |
| R1 · U12 | Default applied and narrowed to the record: "report delivery status to senior management and the steering committee". Left for Wilson: do you present risks and decisions, beyond status, to them? |
| R2 · C2 | Applied as "hand-off to core banking for settlement" (the batch canonical competency phrase). It makes clear that core banking settles, as the default intended. |
| R3 · C3 | Default applied: "AI processing step in licence-plate and portrait recognition". |
| R4 · A7 | Default applied: "and role-based permissions" deleted. The permission matrix remains in the hub-modules bullet. Left for Wilson: should it be presented as a control across platforms? |
| R5 · G3 | Default applied: "Waterfall for scope and budget, Agile sprints for execution". Left for Wilson: did Waterfall also cover milestones and resource planning? |

**Consistency fix (batch rule):** in A7, the 99.9%+ availability figure and the DR drills are now scoped to "the payment hub and real-time payment middleware" (PA-02.1). The encryption and credential controls stay across payment, lending and customer-data platforms (X-01).

**Certificate:** the "Software Designer (Intermediate)" line is unchanged (verified, 02 §3).

Re-render: Layout OK: True, 3 pages, 5/34 bullets at 3 lines, 0 lint hits.
