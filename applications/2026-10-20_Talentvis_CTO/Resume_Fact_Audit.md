# Resume Fact Audit — wilson-2026_SM_Internet_Talentvis_V1_0_0_draft

**Audit date:** 2026-10-20
**Auditor role:** Independent fact check. I did not write the resume, and the resume is not treated as evidence for its own claims.
**Resume audited:** `draft_text.txt` (72 lines). I also cross-checked it against the rendered `…_draft.pdf`, and every text segment in the draft appears in the PDF.
**Evidence used:** `01_Resume_Master_Rules.md` v1.0 · `02_Candidate_Profile.md` v3.1 · `03_Achievement_Library.md` v4.1 (incl. §0A Metrics Bank) · `technical-skills-inventory.md` v2.3 · `fact-check-and-open-questions.md` v2.3 · the candidate confirmations given with this task, cited as [CONF 2026-10-16], [CONF 2026-10-17] and [CONF 2026-10-20].
**Context only (not evidence):** the target is a CTO role at an enterprise-AI start-up, through Talentvis. Family × lens = SM × INT.

---

## 1. Summary

| Verdict | Count | Meaning |
|---|---|---|
| **PASS** | **59** | Traces to evidence. Verb, number, date, title, skill depth and confidentiality are all within the rules. |
| **REVIEW** | **9** | Needs a candidate decision. The question is stated in each row. |
| **FAIL** | **4** | Must be fixed or deleted. Evidence-safe replacement wording is given in each row. |
| **Total rows** | 72 | |

**FAIL items:** F1 "chief executives" (L7) · F2 "customer … pilots" (L15) · F3 the label "Organisation and platforms from scratch" next to the 140 headcount (L20) · F4 "Built high-concurrency microservices" at AI Park, where ownership is O2 (L63).

**REVIEW items:** R1 "building … teams" and "organisation building" without a headcount (L5 ×2, L9) · R2 build-versus-buy (L7, L15, L23) · R3 scope of the ~50 modules (C6) (L19) · R4 how prominent the O5 RAG contribution should be (L6, L10) · R5 the product name "GMS" (L52).

**Clean areas.** None of the held or retired items appears: 10M DAU, 1,000+ car parks, 200+ countries, Flink, Go, Hengshunyuan cloud, Pureland, VV chatbot, delivery-risk forecasting, 30–40% ramp-up, defect %, "concurrency-control modules", "10+ payment domains". There is no CTO or Chief Architect title. Internal names and vendor names (CEW, SCV-CCD, CCD, HCL) do not appear. Every number matches the Metrics Bank, and the "estimated" qualifier on ~80% is kept.

---

## 2. Claim-by-Claim Audit

Legend for the checks column: **D** dates · **T** title · **S** scope · **V** ownership verb vs O-level · **K** tech depth P/A/F/X · **N** number vs Metrics Bank and qualifier · **C** confidentiality. "—" means the check does not apply.

### Header

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 1 | "WILSON" | 02 §1; D-11 [CONF 2026-10-17] | T: name only, no surname ✅ · C: legal name not shown ✅ | PASS | — |
| 2 | "Singapore PR \| +65 8655 9547 \| Skyzhang1028@gmail.com \| Singapore" | 02 §1 (PR since 2024, CF-04) | S ✅ · C ✅ | PASS | Optional style fix: "Singapore" appears twice. Could read "Singapore PR · Singapore". |
| 3 | "Hands-On Technology Executive — Enterprise Platforms & Production Agentic AI \| Start-up Builder · Regulated-Bank Rigour" | 01 §5 (a headline may name the target role); 02 §7.2 SM headlines; PA-07; PA-15; PA-16 | T: no CTO or Chief Architect ✅ · S 🔶: "Start-up Builder" is a framing of Co-founder plus head-of-technology roles · "Production Agentic AI" is backed by PA-07 (production) | PASS | — |

### Professional Summary

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 4 | "18+ years of building platforms **and the teams behind them**" | Metrics Bank "18+ years" ✅; HR-9; [CONF 2026-10-20] team-size verb rule | N ✅ · V: "building … teams" is close to HR-9 ("built a 40/140-person team"). There is no number here, so the 2026-10-20 rule is not breached outright | REVIEW (R1) | **Question:** are you happy for "building … teams" to stand without a number? **Safe default:** "18+ years of building platforms and leading the teams behind them". |
| 5 | "Began as an engineer and technical lead on Renren's e-commerce platform, Sohu's news CMS and Baidu's Nuomi merchant system" | 02 §2 rows 7–9; PA-17, PA-18, PA-19 | T ✅ (Senior R&D Engineer; Technical Leader; Technical Specialist / project leader) · S 🔶: Renren shopping site and Mall described as "e-commerce" | PASS | — |
| 6 | "spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups" | 01 §5 / HR-1 ("head-of-technology roles (2016–2020)"); 02 §2 row 3 (GBD Project Manager & Architect) | D ✅: 2020–22 is covered by "and architect" (GBD) · T: no CTO ✅ | PASS | — |
| 7 | "heading technology for a smart-parking IoT platform through its city pilots" | PA-16.1, PA-16.2 | S ✅ · V ✅ (led as department head) | PASS | — |
| 8 | "co-founding an audio-learning platform" | PA-15; 02 §2 row 5 | T ✅ Co-founder | PASS | — |
| 9 | "**building** VV Technology's technology organisation and platforms from scratch" | PA-11.1 📄 ("Built VV's technology organisation …"); [CONF 2026-10-20] ("led", never "built", for the 140) | V: the organisation half sits close to the headcount rule (the 140 appears in L20) · the platform half ✅ PA-11.1 | REVIEW (R1) | **Safe default:** "leading VV Technology's technology organisation and building its platforms from scratch". |
| 10 | "architecting a 0-to-1 multi-tenant SaaS platform on AWS" | PA-10.1 📄 | V ✅ (O2 → architected) | PASS | — |
| 11 | "Since 2022, a Vice President in UOB's Group Technology & Operations" | 02 §2 row 1 | D ✅ Oct 2022 · T ✅ | PASS | — |
| 12 | "leading 25 onshore and offshore engineers on mission-critical payment and lending platforms" | X-02; Metrics Bank (25, two platform lines) | N ✅ · S ✅ X-02 ("25 … across two platform lines"). C6 (which team runs lending) is still open, but this wording does not depend on the answer | PASS | — |
| 13 | "staying close to the code — reviewing daily, designing solutions and writing core modules" | X-04 | V ✅ · no coding-time % and no "full-time engineer" ✅ | PASS | — |
| 14 | "designed and built a production AI code-review service on headless Claude Code agents" | PA-07 (O1 + O2); inventory §8 (P) | V ✅ · K ✅ P | PASS | — |
| 15 | "and an AI agent for document validation" | PA-08 (O1, Apr 2026) | V ✅ (O1 → built) | PASS | — |
| 16 | "and contributed to a RAG knowledge assistant used across departments" | [CONF 2026-10-20] (O5, in production, cross-department); inventory §8 RAG ❓ (not yet updated) | V ✅ ("contributed to", O5) · K: RAG is not established as a P/A skill. The contribution was loading content | REVIEW (R4) | **Question:** should a content-loading contribution sit in the Summary of a CTO / enterprise-AI resume, where interviewers will probe RAG engineering? **Recommended:** keep it in the UOB bullet (L30) only and drop it from the Summary. If you keep it, the wording is factually acceptable as it stands. |
| 17 | "start-up speed together with the security, privacy, access control, auditability and reliability that enterprise customers expect" | X-01; PA-01.3 (permission matrix); PA-03 (audit-ready, DPIA); PA-02 | S 🔶 framing of confirmed controls | PASS | — |
| 18 | "explaining technical choices in business terms to **chief executives**, senior management and steering committees" | PA-07 §4 (senior management) ✅; PA-01.5 (steering committee) ✅; PA-11 §9 lists VV's CEO only as a stakeholder | S ✗: nothing records you explaining technical choices to chief executives (plural). At UOB it reads as C-suite access | **FAIL (F1)** | **Replace with:** "Used to explaining technical choices in business terms to senior management and steering committees, …". You could add "and start-up CEOs" back only after confirming you briefed the CEO at VV and/or AI Park. |
| 19 | "and to making vendor-selection and **build-versus-buy** decisions" | X-02 ("decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation"); PA-05 (Cloudera evaluated) | S: build-vs-buy is not on record · V: "making … decisions" is stronger than "decision or joint-decision authority" | REVIEW (R2) | **Question:** do you have a real build-vs-buy decision you can defend at interview (what, where, outcome)? **Safe default:** "…and to taking part in vendor-selection and technology-investment decisions." |

### Core Competencies

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 20 | Technology Leadership: "Technology strategy and roadmap, **organisation building from scratch**, leading through squad leads and engineering managers, engineering standards and delivery KPIs, onshore/offshore teams" | PA-01.5 (roadmap); PA-13 (phased technical strategy); X-02; PA-03.1; PA-03.3 (standards are "contributed to"); PA-11 📄 | Every item anchored · "organisation building" is the same R1 issue | REVIEW (R1) | **Safe default:** replace "organisation building from scratch" with "leading technology organisations at start-ups and scale-ups". |
| 21 | Applied & Agentic AI: "Production LLM agents (headless Claude Code), agentic workflow orchestration, prompt A/B evaluation, AgentOps/LLMOps practice, human-in-the-loop governance aligned with MAS FEAT, **RAG knowledge-assistant contribution**" | Inventory §8: Claude Code P, prompt A/B P, AgentOps/LLMOps P, MAS FEAT P; PA-07 (orchestrator); [CONF 2026-10-20] RAG O5 | K ✅ for all except RAG. RAG is honestly labelled as a "contribution", but the competency row reads as a skill list | REVIEW (R4) | Same decision as row 16. **Recommended:** delete "RAG knowledge-assistant contribution" from this row and keep L30. |
| 22 | Architecture & Engineering: "Java, Spring Boot, Spring Cloud, Apache Camel, microservices, event-driven integration, API design, high-concurrency systems, JVM tuning, multi-tenant SaaS" | Inventory §1, §2, §7 | K ✅ (all P or A/P, all anchored) | PASS | — |
| 23 | Cloud & Data: "AWS (EC2/ECS, API Gateway, Lambda, RDS, DynamoDB, S3, IAM, CloudWatch), Kubernetes, Docker, Kafka, Redis, Elasticsearch, Spark, Hive, MySQL, SQL" | Inventory §3–§5 (AWS services A, GBD; Elasticsearch A/P GBD/VV; Kubernetes A; others P or A) | K ✅. A skills line only needs an anchor, and every item has one. Note: the AWS, Lambda and Elasticsearch anchors are 2019–2022 (GBD, VV), so they are not proof of current hands-on use | PASS | Interview note: present AWS as architect-level (A) experience from 2020–22. |
| 24 | Security & Compliance: "API and database encryption, credential management, role-based permission design, secure SDLC, DPIA, data governance, MAS TRM" | Inventory §10; X-01; PA-01.3; PA-03.4 | K ✅ | PASS | — |
| 25 | Reliability & Operations: "DR and failover drills, SLIs/SLOs, Splunk monitoring, P1–P3 incident response and RCA, CI/CD quality gates (Jenkins, SonarQube)" | PA-02.1–02.3; X-06; PA-03.2 | K ✅ | PASS | — |
| 26 | Commercial & Stakeholders: "Vendor selection and governance, **build-vs-buy evaluation**, SOW/licence negotiation, technology budget, **customer** and city pilots, executive communication" | X-02, X-05 ✅; budget at UOB, VV and AI Park ✅ [CONF]; PA-16.2 (city pilots) ✅ | S ✗: no customer pilots are on record (only city pilots and technical bids, PA-16.2) · build-vs-buy is the R2 issue | **FAIL (F2)** | **Replace with:** "Vendor selection and governance, technology-investment decisions, SOW/licence negotiation, technology budget, technical bids and city pilots, executive communication" (if R2 is confirmed, keep "build-vs-buy evaluation"). |

### Selected Achievements

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 27 | "Production agentic AI: Designed and built an AI code-review service … headless Claude Code agents on each pull request … alongside SonarQube. Live since May 2026 after formal architecture and risk approval; the AI advises but never approves or merges, and senior engineers' review time fell by an **estimated ~80%**." | PA-07.1, PA-07.2, PA-07.3; PA-07 §8 (May 2026, approval; C4 partly answered); Metrics Bank | V ✅ O1 + O2 · N ✅ with the "estimated" qualifier kept · adoption scope (C4 remainder) is not claimed ✅ | PASS | Interview: explain the ~80% formula (PA-07 §8); R₀ (C2) is still open. |
| 28 | "AI agent for document validation: Personally built an AI agent that generates validation prompts … eMemo and quotation documents, removing a recurring manual reconciliation task." | PA-08 (O1, personally wrote it ✅ [CONF 2026-10-16]) | V ✅ (O1 → "built"; "personally" is accurate) · C: "eMemo" is a generic document type, not a system name | PASS | — |
| 29 | "Review code daily across **the platform's ~50 modules** (deep review of ~20 core modules)" | X-04; Metrics Bank (~50 / ~20) ✅; **C6 open** (are the ~50 CEW only, or CEW + CCD?) | N ✅ · S: "the platform's" (singular) is only correct if the ~50 are CEW only | REVIEW (R3) | **Question (C6):** are the ~50 modules the payment hub only, or the hub plus customer-360? **Safe default:** "Review code daily across ~50 code modules (deep review of ~20 core modules)", which drops "the platform's". |
| 30 | "co-design solutions with engineers and write core modules for significant changes — including a payment hub's transaction initiation, corporate- and user-role permission matrix and downstream status processing" | X-04; PA-01.3 ✅ | V ✅ O1 · C ✅ (no CEW) | PASS | — |
| 31 | "**Organisation and platforms from scratch:** At VV Technology, led a 140-person technology organisation (total headcount) and built its microservices platform (Spring Cloud, Kubernetes, Redis, Elasticsearch, AWS) and data-analysis platform from scratch, owning technology selection and the technology budget." | [CONF 2026-10-20] (approved wording; direct reports ≤ 15–20); PA-11.1; PA-12 safe wording; inventory (Elasticsearch A/P, Kubernetes A) | N ✅ "(total headcount)" kept · V ✅ in the body ("led" the 140; "built" the platform per PA-11.1 and PA-12 📄) · **the bold label "Organisation … from scratch", placed next to the 140, signals "built a 140-person organisation"**, which the 2026-10-20 rule forbids | **FAIL (F3)** | **Replace the label with:** "Scale-up technology leadership:". Keep the body unchanged. |
| 32 | "0-to-1 multi-tenant SaaS: Architected and delivered, from 0 to 1, a multi-tenant SaaS platform for online-game businesses on AWS — KYC, bonus incentives, VIP tiers, analytics and multi-channel payments — on Spring Cloud and Kubernetes." | PA-10.1 📄 (verbatim) | V ✅ O2 + O3 · 200+ countries is correctly omitted (CF-11) | PASS | Note OQ-1.9 (casual vs real-money gaming) is still open. It matters less for this target. |
| 33 | "Enterprise-grade trust: Designed security controls — API and database encryption …, credential management and role-based permissions — for payment, lending and customer-data platforms under secure SDLC, DPIA and MAS TRM; personally led DR and failover drills, sustaining 99.9%+ availability under peak load." | X-01 (O2); PA-01 §4 ("Designed the security controls" ✅); PA-01.3; PA-02.1; Metrics Bank 99.9%+ | V ✅ (O2 → designed; drills "personally led" ✅ [CONF]) · N ✅ | PASS | — |
| 34 | "**Leadership and build-vs-buy:** Lead 25 onshore and offshore engineers in two platform teams through squad leads and engineering managers; hold decision or joint-decision authority on …; chair governance of four IT service vendors." | X-02; X-05; Metrics Bank (25; four vendors) | N ✅ · C ✅ (no vendor names) · V ✅ · the label depends on R2 | REVIEW (R2) | If R2 is not confirmed, **change the label to:** "Leadership and commercial authority:". Also see style S1: "25 engineers" repeats L6. |

### Professional Experience — UOB

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 35 | "United Overseas Bank (UOB) \| Singapore — Oct 2022 – Present · Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | D ✅ · T ✅ exact | PASS | — |
| 36 | "Technology leader for two mission-critical platform lines … cross-border payments (SWIFT ISO 20022 messaging) and retail unsecured lending — serving millions of accounts." | 02 §6.1; X-02; Metrics Bank ("millions of accounts") | S ✅ · N ✅ | PASS | — |
| 37 | "Took the AI code-review service into production: briefed senior management on the case and the governance model, passed formal architecture and risk approval, and improved review quality through prompt A/B testing and AgentOps/LLMOps practices." | PA-07 §4 (briefed senior management, 13-slide deck); PA-07 §8 (approval); PA-07.4 📄 | V ✅ · K ✅ P · S 🔶: the deck's content ("case and governance model") is not recorded | PASS | Style S1: "formal architecture and risk approval" repeats L17. Keep it in one place. |
| 38 | "Contributed to a production RAG knowledge assistant used across departments (2025), loading internal intranet documentation into its vector database, with access controls and data masking in place." | [CONF 2026-10-20] | V ✅ O5 · S ✅ (access controls and masking are attributed to the system, not to you) · D ✅ 2025 · C ✅ (no system or vendor names) | PASS | Optional: "uploading" (as confirmed) instead of "loading", which might suggest you built an ingestion pipeline. Library sync L2 (§5). |
| 39 | "Coach engineering teams on AI-assisted engineering practices and tooling." | PA-03 §6 📄 | V ✅ | PASS | — |
| 40 | "Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation, enrichment and status tracking — integrating digital and branch channels, reference data, and vendor and third-party banking systems." | PA-01.2 📄; PA-01 §3; inventory (Camel P) | V ✅ O2 · C ✅ (no CEW) | PASS | — |
| 41 | "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking." | PA-01.4 📄 | N: no figure is claimed ✅ | PASS | — |
| 42 | "Led the 10-engineer backend team of a regional customer-360 platform in production since 2022 — evaluated Cloudera as the processing framework, designed the customer data models and personally built the platform's data-analysis module and Spring Batch scheduled jobs." | PA-05.1–05.3; inventory (Cloudera A "evaluated"; Spring Batch P) | N ✅ 10 · V ✅ · C ✅ (no SCV-CCD) · S: "in production since 2022" does not claim the launch (C5 open) ✅ | PASS | Interview: be ready on C5 (whether you led the 2022 launch or took over). |
| 43 | "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration … 15-engineer team: phased, Blue/Green-style coexistence … May and August 2025, ahead of SWIFT's November 2025 deadline, … retired … August 2026 with no service interruption; upgrades ship every 2–3 months." | PA-01.1, PA-01.5; Metrics Bank | D ✅ · N ✅ (15; 2–3 months; no interruption) · V ✅ O3 | PASS | — |
| 44 | "Coordinate P1–P3 production incidents end to end … with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring." | X-06; PA-02.3; 02 CF-N3 | V ✅ · no "reported to MAS" claim ✅ | PASS | — |
| 45 | "Established delivery KPIs … with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing) and SIT/UAT sign-off for every release; contributed to bank-wide SDLC, coding and code-review standards." | PA-03.1, PA-03.2 📄; PA-03.3 (locked "contributed to", CF-15) | V ✅ ("Established" is the PA-03.1 safe wording; "contributed to" for standards ✅) · N ✅ 99% | PASS | Interview: is the 99% on new code or overall? (PA-03 §8) |
| 46 | "Report status, risks and decisions to senior management and steering committees, and work closely with teams in India, Thailand and Indonesia across time zones." | PA-01.5; X-02 [CONF 2026-10-17]; D-09 | S ✅ (collaboration, not line management; no US claim) | PASS | — |

### Professional Experience — Golden Bridge Drive

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 47 | "Golden Bridge Drive (SG) Pte. Ltd. \| Singapore — Nov 2020 – Jul 2022 · Project Manager & Architect" | 02 §2 row 3 | D ✅ · T ✅ | PASS | — |
| 48 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness …" | [CONF 2026-10-20]; PA-10.3 | N ✅ with qualifier · V ✅ "led" (not "built") · O3 "owned" ✅ | PASS | — |
| 49 | "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution." | PA-10.2 📄 (200+ correctly dropped) | V ✅ O2 | PASS | — |
| 50 | "Architected the AWS deployment — Route 53, API Gateway, EC2/ECS, Lambda, Cognito, RDS, DynamoDB, ElastiCache, SQS/SNS, S3 and CloudWatch — and applied DPIA, API and database encryption and credential management; led data migration." | PA-10 §3; inventory §5 (all A, GBD); X-01 | K ✅ (A is allowed in bullets) · V ✅ O2 | PASS | Style S2: 11 services in one bullet reads as a technology dump (01 §6). Consider "Architected the AWS deployment (API Gateway, EC2/ECS, Lambda, RDS, DynamoDB, SQS/SNS) …". |

### Professional Experience — VV Technology

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 51 | "VV Technology Pte. Ltd. \| Singapore — Apr 2019 – Jun 2020 · **Head of Technical Centre**" | 02 §2 row 4 (dates ✅); [CONF 2026-10-17] FU-3 decision (supersedes "Development" in 02) | D ✅ · T ✅ per FU-3 decision · British spelling ✅ | PASS | Library sync L1 (§5). |
| 52 | "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services — through data." | PA-11 §1 📄 | S ✅ (blockchain/AI wording correctly left out) | PASS | — |
| 53 | "Took part in product-strategy planning and delivered the first VV-Life release in 2019, including the payment subsystem's transaction, management and reconciliation modules." | PA-11 §4; PA-11.2 📄 | D ✅ · V ✅ | PASS | — |
| 54 | "Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching …, bringing service response times to the millisecond level." | PA-11.4 ✅ (verbatim) | N: no % ✅ · K ✅ Kafka anchored | PASS | — |
| 55 | "Led the big-data team on Flume, Hive, MapReduce, Spark Streaming and Spark SQL, providing data analysis that supported business decisions." | PA-12 ([R22] version, the only permitted one); [CONF 2026-10-16] | K ✅ (A) · **no Flink** ✅ (CF-07 respected) | PASS | — |
| 56 | "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for **GMS**, a B2B online-office product for Southeast Asia, governing solution design, cost evaluation, staffing and acceptance." | PA-13 📄 | V ✅ O2 + O4 · K ✅ RocketMQ A · C: the PA-13 safe wording deliberately leaves out the name "GMS". It is not on the 01 §7 list, but it is an employer product name with no public anchor | REVIEW (R5) | **Question:** was "GMS" a public product name? If not, or if unsure, **replace** "for GMS, a B2B online-office product" with "for a B2B online-office product". |
| 57 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans." | PA-11.3 📄; PA-11.5 ✅ (02 CF-N8) | V ✅ | PASS | — |

### Professional Experience — Hengshunyuan

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 58 | "Hengshunyuan Information Technology Co., Ltd. \| China — Oct 2017 – Sep 2019 · Co-founder" | 02 §2 row 5; D-10 [CONF 2026-10-17]; CF-05 (title resolved) | D ✅ per D-10, no overlap note · T ✅ | PASS | Interview: be ready to explain the overlap with VV and the dormancy (D-10). CF-05 date basis is still not checked against documents. |
| 59 | "Owned product, architecture and technical delivery of an audio-learning platform … reaching a peak of ~100k daily active users." | PA-15.1 📄; Metrics Bank (~100k, single source) | N ✅ "~" kept · V ✅ | PASS | — |
| 60 | "Brought ~1,500 licensed audio titles and albums onto the platform at launch, on a Spring Cloud microservices stack with a MySQL cluster, Redis, Kafka and ELK." | PA-15.2 📄; PA-15 §3; inventory (Kafka, ELK anchored at Hengshunyuan) | N ✅ · **cloud provider omitted** ✅ (CF-08 respected) | PASS | — |

### Professional Experience — AI Park

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 61 | "AI Park \| China — Apr 2016 – Sep 2017 · **VP of Technical Department**" | 02 §2 row 6; CF-06 (Apr confirmed earlier, fact-check §6); [CONF 2026-10-17] FU-3 | D ✅ · T ✅ per FU-3 decision | PASS | Library sync L1 (§5). |
| 62 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform …; introduced a SaaS model for business and government customers." | PA-16.1; PA-16 §4 | V ✅ | PASS | — |
| 63 | "Led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing, and launched pilots in Shijiazhuang (2016), Handan (2017) and Beijing Chaoyang (2017)." | PA-16.2 ✅ (CF-14 resolved) | D ✅ · N: no "4+" or "1,000+" ✅ | PASS | — |
| 64 | "Added an AI processing step to licence-plate and portrait recognition to improve recognition speed and accuracy." | PA-16.3 📄; inventory §8 (pipeline integration, not model training) | K ✅ | PASS | — |
| 65 | "**Built** high-concurrency microservices on Spring Cloud with Kafka and caching for millisecond-level service processing, and led the big-data team on HBase, MongoDB and Spark Streaming." | PA-16 ownership **O2** + PL; PA-16.4 safe wording ("Brought Spring Cloud microservices into the architecture …"); inventory (HBase A/P, MongoDB P, Spark Streaming A/P) | V ✗: "Built" is not allowed for O2 (01 §4) · the big-data half ✅ | **FAIL (F4)** | **Replace with:** "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing; led the big-data team on HBase, MongoDB and Spark Streaming." |

### Earlier Experience

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 66 | "Baidu — Technical Specialist, Nuomi group-buying e-commerce platform (May 2014 – Dec 2014, China): As project leader, re-architected … Dubbo … two months ahead of plan, leading the web front-end, CMS development and QA teams." | 02 §2 row 7 (CF-12 resolved; months from [R22] 📄); PA-17.1 📄; Metrics Bank (2 months ahead) | D ✅ · T ✅ · N ✅ · "5–10M QPS" correctly omitted | PASS | — |
| 67 | "Sohu.com — Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014, China): Led the re-architecture of the fifth-generation CMS … OpenAPI messaging platform." | 02 §2 row 8 (CF-13: either title); PA-18.1 📄 | D ✅ · T ✅ | PASS | — |
| 68 | "Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012, China): Developed Renren's shopping website, Renren Mall and CRM." | 02 §2 row 9; PA-19 | D ✅ · T ✅ · V ✅ O1 | PASS | — |

### Education, Certifications and Languages

| # | Resume sentence (short quote) | Evidence ID(s) | Checks | Verdict | Action |
|---|---|---|---|---|---|
| 69 | "Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008)" | 02 §3 (CF-02 resolved; FU-4 degree type open, so generic "Master's degree" ✅) | D ✅ · T ✅ | PASS | — |
| 70 | "Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004)" | 02 §3 (CF-01 resolved) | D ✅ | PASS | — |
| 71 | "Software Designer (Intermediate) — Qualification Certificate … (2006) · PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3 [CERT-SS]; PMP [CONF]; SRE [CONF 2026-10-16] | D ✅ 2006 · no "certified" for PMP or SRE ✅ · C: no certificate number, ID or legal name ✅ | PASS | OQ-P1 (SRE provider and year) is still open. Not needed here. |
| 72 | "Languages: English and Mandarin (professional working proficiency in both)" | 02 §1 | S ✅ | PASS | — |

---

## 3. 01 §9 Pre-Delivery QA Checklist

### Facts
| Item | Result | Notes |
|---|---|---|
| Every bullet traces to an ID in 03 (or a section in 02); no ❓ / ⚠️ / ⛔ content outside permitted parts | **PASS with exceptions** | Every bullet traces to 03 or 02, except the RAG bullet, which traces to [CONF 2026-10-20] and is not yet in 03 (sync L2). The unsupported fragments are F1 ("chief executives") and F2 ("customer pilots"). No held or retired item appears (see §1). The ⚠️ items used (CF-16 titles, CF-05 Hengshunyuan dates, CF-06 AI Park start) are covered by the confirmations of 2026-10-17 and earlier. Open items the wording depends on: C6 (R3), OQ-1.9 (online-game wording, 📄 safe wording used). |
| Dates and titles match 02 §2 exactly; no "CTO" / "Chief Architect" | **PASS** | All dates match 02's proposed canonical values. VV and AI Park titles follow the FU-3 decision [CONF 2026-10-17], not 02's "Development" wording (sync L1). There is no CTO or Chief Architect anywhere in the resume text. The PDF metadata title reads "Wilson — Resume — CTO (Enterprise AI), Talentvis". That names the *target* role, which 01 §5 / 02 §7.2 allows for a CTO JD. It is noted here because ATS tools may parse it. |
| Every number matches the 03 Metrics Bank, with qualifiers kept | **PASS** | 18+; 25; 15; 10; ~50 / ~20; estimated ~80%; 99.9%+; 99%; four vendors; millions of accounts; May/Aug 2025, Nov 2025, Aug 2026, May 2026, 2–3 months; 140 and 40 with "(total headcount)"; ~100k; ~1,500; pilot years; 2 months ahead; 2006. |
| Verbs match ownership level (§4) | **FAIL** | F4 ("Built", O2, L63) and F3 (label implying "built" the 140). R1 is borderline (unquantified "building teams / organisation"). Everything else complies, including O5 "contributed to" for RAG and bank-wide standards. |
| Skills appear only if anchored in the inventory (P or A for Summary and bullets) | **PASS with one exception** | Every skill is anchored. Lambda, Cognito and Elasticsearch are A, which is allowed in bullets. The exception is RAG and vector DB, which are still ❓ in the inventory and are anchored only by [CONF 2026-10-20] at O5. The wording is "contributed" or descriptive, not a skill claim (R4, sync L2). |

### Confidentiality
| Item | Result | Notes |
|---|---|---|
| No CEW / SCV-CCD / CCD / vendor names (incl. HCL) / internal numbers (§7) | **PASS** | Descriptive names are used: "payment-initiation hub", "regional customer-360 platform", "four IT service vendors". No UOB volumes, customer names, ticket numbers, legal name or certificate identifiers. "GMS" (a former employer's product name) is R5. "eMemo" is a generic document type. |

### Positioning and style
| Item | Result | Notes |
|---|---|---|
| Headline and Summary fit the chosen family × lens (SM × INT) | **PASS** | It reads as a hands-on technology executive and leader, with AI as one pillar. It does not repackage the candidate as an AI engineer or big-data engineer (01 §5). |
| Summary is narrative; no stacked repetition with Achievements or Experience | **REVIEW (style S1)** | The Summary is a three-paragraph career narrative ✅. Repeated content: "25 engineers" appears in L6 and L23. "Formal architecture and risk approval" appears in L17 and L29. The VV organisation appears in L5, L20 and the VV section. The 0-to-1 SaaS appears in L5, L21 and the GBD section. RAG appears in L6, L10 and L30 (R4). Suggest keeping each fact in one primary place. |
| British spelling consistent (pending OQ-R1) | **PASS** | organisation, licence, Centre, containerised, programme-style wording. No American spellings found. |
| Other style | **REVIEW (style S2, S3)** | S2: the L45 AWS list is a technology dump. S3: "Singapore" appears twice in the header line. |

### Document
| Item | Result | Notes |
|---|---|---|
| ≤ 3 pages; page numbers present; no orphaned headings | **PASS (PDF text check only)** | PDF = 3 A4 pages. Footer shows "Page X of 3" (PAGE field in footer1.xml). Page 2 starts with the "PROFESSIONAL EXPERIENCE" heading and page 3 with the Hengshunyuan employer line, so there is no orphaned heading at either page end. The DOCX has only one `keepNext` property, so pagination may break after edits. Re-check after fixes. |
| Layout per 04 | **NOT PERFORMED** | `04_Resume_Layout_Spec.md` was not in the supplied fact-library folder. |
| Text extractable (no text boxes, no images of text); renders as PDF | **PASS (partial)** | `document.xml` has 0 text boxes. Every draft text segment was found in `pdftotext` output. A visual render (fonts, spacing, bullets, table look) was not inspected. |
| File name per §10 | **PASS (provisional)** | `wilson-2026_SM_Internet_Talentvis_V1_0_0_draft` follows `[Family]_[Lens]_[Target]_V…`, with a "_draft" suffix. OQ-R3 is still open. "Talentvis" is the recruiter, not the employer. Your call whether the target segment should name the employer. |
| Draft marking | **Note** | The DOCX has 74 red (`FF0000`) runs, which fits the draft convention (01 §10). The final version must be all black. `comments.xml` exists but holds no comment text. |

### Review package
| Item | Result | Notes |
|---|---|---|
| Three-dimension review (§8) delivered separately; change log | **NOT PERFORMED** | Outside this audit's scope (fact reliability only). Not supplied for review. |

---

## 4. Checks Not Performed

- **Layout against 04:** fonts, sizes, margins, heading styles, spacing and section order. 04 was not supplied.
- **Visual rendering:** I did not rasterise or view the PDF or DOCX pages. Only text extraction, page count, footer and page-boundary text were checked.
- **Job fit (01 §8 dimension 1):** the JD was given as context only and was not audited.
- **Primary documents:** employment letters (FU-3 title wording, CF-05 / CF-06 dates), diplomas (FU-4) and SRE training records (OQ-P1) were not available. Titles and dates were checked against 02 and the confirmations only.
- **Library facts themselves:** 📄 items (e.g. 99.9%+, "no service interruption", ~100k DAU, ~1,500 titles, latency reduction) were accepted as worded in 03. Their underlying evidence was not re-verified.
- **Change log and three-dimension review package:** not supplied.

---

## 5. Library Sync Items (not resume defects — for the candidate to approve; source files were not modified)

| ID | File(s) | Item |
|---|---|---|
| L1 | 02 §2 rows 4 and 6, §6.4, §6.6; fact-check CF-16 / FU-3; 03 PA-11, PA-16 | Record the [CONF 2026-10-17] FU-3 decision (AI Park "VP of Technical Department"; VV "Head of Technical Centre") as a decision-log entry. 02 and 03 still show "Development". |
| L2 | 03 (new card, e.g. X-07); inventory §8 RAG and vector-DB rows | Add the [CONF 2026-10-20] RAG knowledge-assistant contribution: UOB, 2025, O5, uploading intranet materials, cross-department production use, access controls and masking. Set the RAG depth for the contribution (not P/A). |
| L3 | 03 Metrics Bank (140 ❓, 40 📄), PA-10.3, PA-11.1; fact-check OQ-2.3, HR-3, HR-9; inventory §12 | Record [CONF 2026-10-20]: 140 and 40 are total headcount; direct reports ≤ 15–20; verb "led", never "built" or "hired". |
| L4 | 03 PA-12 | Add [CONF 2026-10-16]: "data analysis that supported business decisions". |

---
## Post-audit fixes applied by the drafter (2026-10-20)
| Item | Applied | Status |
|---|---|---|
| F1 "chief executives" | → "senior management and steering committees" | fixed |
| F2 "customer … pilots" | → "technical bids and city pilots" | fixed |
| F3 label next to 140 headcount | → "Scale-up technology leadership:" | fixed |
| F4 AI Park "Built high-concurrency…" | → PA-16.4 safe wording ("Brought Spring Cloud microservices into the architecture…") | fixed |
| R1 "building … teams / organisation" | safe defaults applied ("leading the teams", "leading VV's technology organisation and building its platforms", "leading technology organisations") | default applied — candidate to confirm |
| R2 build-vs-buy | removed; "taking part in vendor-selection and technology-investment decisions"; label "Leadership and commercial authority" | default applied — candidate to confirm |
| R3 "the platform's ~50 modules" | → "~50 code modules" | default applied |
| R4 RAG prominence | removed from Summary and competency row; kept only the UOB bullet; "loading" → "uploading" | default applied |
| R5 "GMS" name | → "a B2B online-office product serving Southeast Asia" | default applied |
| Style: duplicate "25 engineers" | Achievement 7 no longer repeats the number | fixed |
| Style: duplicate "formal approval" | removed from UOB AI bullet | fixed |
| Style: AWS list (11 services) | trimmed to 6 | fixed |
| Doc: keep-with-next | verified on all headings, employer, title and sub-heading lines (auditor counted one) | verified |
| Doc: re-render | LibreOffice PDF re-rendered after fixes — 3 pages, "Page X of 3", no orphaned headings, text extractable; pages viewed visually | verified |

## Candidate decisions on REVIEW items (2026-10-20 16:46)
| Item | Decision | Applied |
|---|---|---|
| R1 "building … teams / organisation" | safe defaults kept | no change |
| R2 build-vs-buy | **No build-vs-buy experience** — not claimed; JD requirement stays a gap | no change |
| R3 ~50 modules | ~50 modules = the payment platform (payment-initiation hub app) only | "across the payment platform's ~50 code modules" |
| R4 RAG prominence | agreed — UOB bullet only | no change |
| R5 GMS | not a public product name — stays unnamed | no change |
Re-rendered: 3 pages.
