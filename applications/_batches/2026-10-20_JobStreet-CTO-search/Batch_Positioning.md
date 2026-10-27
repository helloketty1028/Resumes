# Batch Positioning — 定位卡（10 份 A/B 档 JD）

- 批次：2026-10-20_JobStreet-CTO-search · 工具 C 阶段二 · 2026-10-21
- 审批方式：Wilson 选择“定位卡 + 红字草稿一起出，C3 一并审”（2026-10-21 10:4x）——本文件与草稿、审计、冷读一起在 C3 审阅
- 依据：Batch_Triage.md 分诊结论、C1 三轮答复（S1–S9，见 Batch_Fact_Update_Proposal.md）、事实库 master\v2.0-draft（只读）

# Card 01 — NETS — Principal Engineer (JobStreet 95218038)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95218038
- **Triage:** tier **A** · batch match score **87** (Required coverage: Direct 1 / Transferable 0.5)
- **Family × lens:** **ATL × BNK** (owns target architecture, design authority, hands-on engineering for mission-critical payment platforms; NETS = payment scheme operator → bank/fintech lens)
- **file_stem:** `wilson-2026_ATL_Bank_NETS_V1_0_0` · application folder `2026-10-21_NETS_Principal-Engineer`
- **Base:** approved Talentvis JSON (UOB architecture block, VV, GBD, AI Park, Earlier) + `LIB_wilson-2026_Archi_Bank_LIB_V5_0_0.txt` (ATL × BNK cell, headline option 3).

## Headline (one line)
`Principal Engineer — Payment & Transaction-Processing Platforms | Hands-On Java Architecture · Resilience by Design`

## Summary storyline (3 paragraphs, ≤ 4 lines each)
1. First sentence = JD core: hands-on technical authority for mission-critical payment platforms — 18+ years, Java engineering and solution architecture across a Tier-1 bank and high-traffic e-commerce/local-life platforms.
2. At UOB (since 2022): design authority and hands-on builder of the payment-initiation hub (design + core modules incl. concurrency control), integrated with core banking (S2); ISO 20022 migration with no service interruption; DR/99.9%+; leads 25 engineers through squad leads.
3. Earlier: payment integrations across Alipay, WeChat Pay, UnionPay (Renren Mall, Baidu Nuomi) and UnionPay, Visa/Mastercard, Google Pay, GrabPay with settlement reconciliation (VV-Life) (S1); head-of-technology roles 2016–2022; mentoring engineers; works with vendors, banks' internal stakeholders, steering committees.

## Core Competencies (6–7 rows, JD order)
Payment & Transaction Systems (payment initiation, validation, enrichment, status tracking, settlement integration with core banking, reconciliation, ISO 20022, SWIFT, card and wallet payment integrations) · Architecture & Integration (Java, Spring Boot, Apache Camel, RESTful APIs, enterprise integration patterns, event-driven, microservices, distributed systems) · Performance & Resilience (low latency, concurrency control, JVM/thread-pool tuning, DR and failover drills, high availability, capacity baselines) · Security & Risk (API and database encryption, credential management, role-based access control, secure SDLC, DPIA, MAS TRM) · Engineering Delivery (CI/CD, DevSecOps practices as evidenced: SonarQube gates, automated regression and penetration testing in CI/CD; Splunk observability) · Platforms (Linux (RHEL), SQL, MySQL, Docker, Kubernetes, AWS) · Leadership (design/code reviews, standards (contributed), mentoring, vendor governance, steering-committee reporting).

## Selected Achievements (6–7)
1. **Payment-hub design authority** — PA-01.2 (+ S2 core-banking integration in short form).
2. **Hands-on core engineering** — S6 (core modules incl. concurrency control) + S5 (daily review of new core PRs).
3. **Zero-interruption modernisation** — PA-01.1 (ISO 20022 coexistence; May/Aug 2025; retired Aug 2026).
4. **Low latency under load** — PA-01.4 (+ PA-11.4 millisecond-level at VV only if it fits).
5. **Resilience & security** — PA-02.1 + X-01 (99.9%+; encryption, credential management, access control).
6. **Payments across markets** — S1 (Renren/Nuomi/VV integrations + settlement reconciliation).
7. **Engineering governance** — PA-03.1/03.2 + PA-03.3 ("contributed to" bank-wide standards) + mentoring (X-02).

## Experience plan
- **UOB** scope line (two platform lines, MAS-regulated, millions of accounts). Sub-headings: *Architecture & Hands-On Engineering* (PA-01.2 or S2 bullet, PA-05 customer-360 + S2 daily summaries, PA-07 AI code review as engineering-productivity tool) → *Reliability, Security & Production* (X-06 incidents, PA-02.2/02.3 SLOs & Splunk, X-01 data migration) → *Delivery & Leadership* (PA-01.5 15-engineer team + releases every 2–3 months, X-02 25 engineers + cross-time-zone, X-05 vendors). 9–11 bullets, complementary to achievements.
- **Golden Bridge** 2–3: PA-10.1 (multi-tenant SaaS on AWS incl. multi-channel payments, API gateway), PA-10.3 (40-person, total headcount), X-01.
- **VV** 3–4: S3 140-person org + platform; S1 VV-Life payment subsystem (transaction, management, reconciliation; UnionPay, Visa/Mastercard, Google Pay, GrabPay) — combine with PA-11.2; PA-11.4 performance; PA-11.3 + PA-11.5.
- **Hengshunyuan** → one Earlier Experience line (space).
- **AI Park** 2: PA-16.1 (IoT platform with online payment), PA-16.4 (Spring Cloud + Kafka + caching → millisecond-level).
- **Earlier**: Baidu (PA-17.1 + S1 "designed and coded payment-gateway integration with Alipay, WeChat Pay and UnionPay"), Sohu (PA-18.1), Renren (PA-19 + S1 "designed and coded Renren Mall's payment integration with Alipay and UnionPay").

## Gaps → honest handling (do not claim)
Transaction switching, retail POS, QR, card-scheme integration, payment authorisation in the card sense → not claimed; show adjacent evidence only (payment initiation, settlement integration, wallet/card payment integration, reconciliation). Solace JMS → omit. PCI-DSS → omit (only working knowledge). Mobile/SDK → omit. Note: the hub's "authorisation" is group/account/product authorisation of payment requests — do not call it card payment authorisation.

## Keyword map (JD term → record term → ID)
technical design authority → led end-to-end design (PA-01.2) · low-latency, high-throughput → latency under high load (PA-01.4), concurrency control (S6) · highly available, DR, operational resilience → PA-02.1 · settlement, reconciliation → S2, S1 · legacy modernisation, migration → PA-01.1 · Java/Spring Boot, RESTful APIs, EIP → PA-01.2/01.3, Camel · RHEL, containers, AWS → skills inventory · DevSecOps, CI/CD, automated testing, observability → PA-03.2, PA-02.2 · architecture/design/code reviews, guardrails → X-04 (S5), PA-03.3 · multiple concurrent tracks, vendors → X-02, X-05 · mentor senior engineers → X-02.

---

# Card 02 — Private Advertiser (financial services) — Head of Technology Development (JobStreet 95063994)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95063994
- **Triage:** tier **A** · batch match score **95** · note: posted salary band S$8–12k (Wilson: floor negotiable on total package)
- **Family × lens:** **SM × BNK** (heads a lean multi-discipline tech team in a regulated financial-services employer; owns strategy execution, BAU + projects, vendors, compliance)
- **file_stem:** `wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0` · folder `2026-10-21_PrivateAdvertiser_Head-of-Technology-Development`
- **Base:** approved TEKsystems JSON (delivery, BAU + change, stakeholders) + Talentvis JSON + `LIB_wilson-2026_Senior_Tech_Bank_LIB_V5_0_0.txt` (SM × BNK, headline option 3 AppDev Manager).

## Headline (one line)
`Head of Technology Development — Payments, Digital Channels & Integration Platforms | Regulated Delivery · Hands-On Engineering`

## Summary storyline
1. First sentence = JD core: technology leader who runs multi-discipline teams and delivers BAU and change projects on deadline in a regulated financial-services environment — 18+ years across a Tier-1 bank, fintech/SaaS and consumer internet.
2. UOB: leads 25 engineers across two platform lines; delivery on regulatory deadlines (ISO 20022 before SWIFT's deadline); vendors (four IT service vendors), investment/vendor selection; MAS TRM compliance; production ownership.
3. Customer channels and touchpoints across his career: e-commerce and payment-gateway integrations (S1), news CMS and publishing workflow (Sohu), API-gateway-based multi-tenant SaaS (GBD), local-life platform with payments (VV); Agile/Scrum set up from scratch; hands-on Java.

## Core Competencies
Technology Leadership (lean multi-discipline teams, squad leads/EMs, performance management, onshore/offshore and cross-time-zone teams) · Delivery & Prioritisation (BAU and project portfolio in parallel, deadlines, RAID, change control, MVP sequencing across two lines; Agile/Scrum, hybrid Waterfall) · Channels & Integration (web portals and e-commerce sites, CMS, API gateway, B2B/B2C integration, payment gateways — Alipay, WeChat Pay, UnionPay, Visa/Mastercard, Google Pay, GrabPay) · Vendor & Commercial (vendor due diligence/selection, SOW/licence, vendor performance governance, budget) · Security & Compliance (MAS TRM, secure SDLC, DPIA, encryption, credential management) · Tools (Jira, Confluence, MS Project, Miro) · Technical (Java, JavaScript (React), Spring Boot, Spring Cloud, AWS, Kubernetes, SQL).

## Selected Achievements
1. **Regulatory deadline met** — PA-01.1.
2. **Multi-discipline leadership** — X-02 (25 engineers, two teams through squad leads/EMs, 1:1s, mentoring, performance management).
3. **Payment gateways & channel integration** — S1 (+ hub integrates digital and branch channels PA-01.2 short form).
4. **Content-management platform** — PA-18.1 + PA-18.2 (Sohu CMS re-architecture + publishing workflow contribution).
5. **API-gateway SaaS platform** — PA-10.1 (multi-tenant SaaS on AWS API Gateway, KYC, payments).
6. **Vendor due diligence & accountability** — X-05 + X-02 commercial authority.
7. **AI adoption in production** — PA-07.1/07.3 (short) — JD lists AI in the team scope.

## Experience plan
- **UOB** scope line. Sub-headings: *Technology Leadership & Delivery* (PA-01.5, PA-04.1 lending line, X-02 MVP sequencing, C-RPT steering/cross-time-zone) → *Platforms & Integration* (PA-01.2 hub + S2 core banking, PA-05 customer-360 with S2 daily summaries, S5 hands-on) → *Governance, Security & Production* (X-06 incidents incl. outages, PA-03.1/03.2, PA-03.4 MAS TRM, X-01 data migration). 9–11 bullets.
- **Golden Bridge** 3: PA-10.3 (40-person, Agile from scratch, budget), hybrid delivery, PA-10.1/API gateway + X-01.
- **VV** 3–4: S3 org; S1 VV payments + PA-11.2; PA-11.3/11.5; PA-13 B2B product (unnamed).
- **Hengshunyuan**: Earlier line.
- **AI Park** 2: PA-16.1, PA-16.2.
- **Earlier**: Baidu + S1; Sohu (CMS + publishing workflow if not in achievements — avoid duplicate); Renren + S1.

## Gaps → honest handling
Chatbots → not claimed (PA-14 ⛔). Mobile app development → not claimed (Swift/Kotlin familiarity only). C++ → not listed. Kanban → not listed. "Head of Technology" title → historical titles stay as in 02; head-of-technology roles 2016–2022 may be described as such.

## Keyword map
lean multi-discipline team → X-02 · strategic plans / transformation roadmap → PA-01.5 roadmap, VV technology selection (PA-11.1) · BAU + projects in parallel, prioritisation → X-02 MVP sequencing, PA-04.1 · upgrades, migrations, outages → PA-01.1, X-01 data migration, X-06 · vendor due diligence → X-02 vendor selection, X-05 · regulatory compliance → PA-03.4 MAS TRM · web portal, CMS → PA-18, PA-19 · API gateway, B2B/B2C integration → PA-10.1, PA-01.2 · electronic payment gateways → S1 · Scrum → PA-10.3 · Jira/Confluence/MS Project → skills §tools · remote/hybrid teams → X-02 offshore 5+ years.

---

# Card 03 — Stripe — Engineering Manager, Disputes Foundation (JobStreet 88429529)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/88429529
- **Triage:** tier **A** · batch match score **93** · posted 30d+ → Wilson to confirm still open
- **Family × lens:** **SM × INT** (engineering manager for a platform team at a fintech that hires like an internet company — OQ-P2 decided per JD → INT; remove bank jargon or explain it)
- **file_stem:** `wilson-2026_SM_Internet_Stripe_V1_0_0` · folder `2026-10-21_Stripe_EM-Disputes-Foundation`
- **Base:** approved Talentvis JSON (SM × INT) — closest approved base.

## Headline (one line)
`Engineering Manager — Payment Platforms & Production Systems | Hands-On Java · Platform Teams · Cross-Time-Zone Delivery`

## Summary storyline
1. First sentence = JD core: hands-on engineering manager for payment platforms — began as a software engineer and technical lead at Renren, Sohu and Baidu (2008–2014), then led engineering teams and organisations (no "8+ years" claim; no derived year counts).
2. UOB: manages 25 engineers in two platform teams through squad leads and EMs; still reviews new core PRs daily and writes core modules; production rigour (P1–P3, SLOs, DR drills, zero-interruption ISO 20022 cutover).
3. Builder of extensible platforms that serve other teams (payment-initiation hub used by digital and branch channels; customer-360 APIs used by several business lines; multi-tenant SaaS) and of the teams behind them (VV 140-person org, GBD 40-person team, both total headcount); payment integrations across wallets and cards (S1); cross-time-zone teams in India, Thailand and Indonesia.

## Core Competencies
Engineering Management (squad leads/EMs, 1:1s, mentoring, performance management, standards, onshore/offshore) · Platform Engineering (extensible platforms for other teams, API design, microservices, event-driven integration, multi-tenant SaaS) · Payments (payment initiation, status tracking, settlement integration and reconciliation, ISO 20022, card and wallet payment integrations) · Production Rigour (P1–P3 incidents and RCA, SLIs/SLOs, DR drills, Splunk, CI/CD quality gates) · Hands-On Engineering (Java, Spring Boot, Spring Cloud, Apache Camel, concurrency control, JVM tuning, SQL) · Cloud & Data (AWS, Kubernetes, Docker, Kafka, Redis, MySQL) · Developer Productivity & AI (production AI code review, AgentOps/LLMOps practice, human-in-the-loop governance).

## Selected Achievements
1. **Platform used by other teams** — PA-01.2 (+ S2 short).
2. **Production rigour** — PA-01.1 (no service interruption) + X-06 (short).
3. **Hands-on manager** — S6 + S5.
4. **Developer productivity** — PA-07.1/07.2/07.3 (AI code review).
5. **Payments across wallets and cards** — S1 + PA-11.2 (VV reconciliation).
6. **0-to-1 extensible platforms** — PA-10.1 + PA-11.4.
7. **Developing engineers** — X-02 (1:1s, mentoring, performance management; leading through squad leads/EMs) + cross-time-zone.

## Experience plan
- **UOB** scope line in plain English ("cross-border payments and retail lending platforms in a regulated bank"). Sub-headings: *Platform Engineering* (PA-01.2/S2, PA-05 + S2, PA-01.4) → *Production & Delivery* (PA-01.5 releases every 2–3 months, X-06, PA-03.1/03.2) → *Team & Productivity* (X-02, AI review productionisation PA-07.4 + approval S9, coaching on AI-assisted engineering, RAG contribution optional). 9–10 bullets.
- **Golden Bridge** 3 (Talentvis): PA-10.3, PA-10.2 (no 200+), AWS stack + X-01.
- **VV** 4: S3 org; S1 payments + PA-11.2; PA-11.4; PA-11.3 + 11.5.
- **Hengshunyuan** 1–2 (0 to ~100k DAU; consumer product) — full role or Earlier line depending on space.
- **AI Park** 2: PA-16.1, PA-16.4.
- **Earlier**: Baidu + S1, Sohu, Renren + S1.

## Gaps → honest handling
"8+ years full-time software development": do not claim a year count; show the engineering path (Renren 2008–2012 engineer; Sohu/Baidu technical/project leader with hands-on re-architecture) plus current hands-on work (S5/S6). Hiring track record: not quantified — do not claim hiring numbers; use "led", "mentoring and performance management". Disputes domain: not claimed (adjacent: payment status tracking, reconciliation, collections PA-04).

## Keyword map
engineering management → X-02 · developing & mentoring → X-02 (1:1s, mentoring) · ambiguous, fast-paced → 0-to-1 builds PA-10.1, PA-15.1 · operational rigor, production systems → X-06, PA-02.1, PA-01.1 · extensible software that scales → PA-10.1, PA-01.2 · cross-functional, cross-timezone → X-02 India/Thailand/Indonesia · platforms serving other product teams → PA-01.2 (channels), PA-05 (APIs for several business lines) · payment processing → PA-01, S1, S2.

---

# Card 04 — DBS Bank — SVP, Engineering Lead, Core Banking Technology (JobStreet 95272188)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95272188
- **Triage:** tier **B** · batch match score **93** (after C1: core-banking domain = Transferable via integration) · band jump VP2 → SVP
- **Family × lens:** **ATL × BNK** (engineering lead who stays in architecture, design and code reviews for transaction platforms in a bank)
- **file_stem:** `wilson-2026_ATL_Bank_DBS_V1_0_0` · folder `2026-10-21_DBS_SVP-Engineering-Lead-Core-Banking`
- **Base:** approved Talentvis JSON (UOB architecture block) + `LIB_wilson-2026_Archi_Bank_LIB_V5_0_0.txt`.

## Headline (one line)
`Engineering Lead — Banking Transaction Platforms | Payments, Lending & Customer Data · Hands-On Architecture · Modernisation`

## Summary storyline
1. First sentence = JD core: engineering lead for transaction-processing platforms in a Tier-1 bank who leads squads while staying in architecture, design and code reviews — 18+ years.
2. UOB: payment-initiation hub, retail-lending servicing and collections, and a regional customer-360 platform, all integrated with core banking (S2: core banking executes settlement; daily account summaries feed portfolio analysis); ISO 20022 modernisation with coexistence and no interruption; AI-assisted software development in production (AI code review).
3. Earlier: high-concurrency internet platforms (Renren, Sohu, Baidu) and head-of-technology roles (2016–2022) building microservices platforms; hands-on Java/Spring, React, MongoDB exposure (historical — keep it in competencies only).

## Core Competencies
Banking Domains (payments and transaction processing, retail lending servicing and collections, customer data/customer-360, settlement integration with core banking, ISO 20022) · Architecture (microservices, API design, event-driven integration, distributed systems, Apache Camel, legacy modernisation, coexistence/Blue-Green deployment) · Engineering (Java, Spring Boot, Spring Batch, React, SQL, MySQL, MongoDB) · Platforms & DevSecOps (Linux (RHEL), Docker, Kubernetes, AWS; CI/CD with SonarQube gates, automated regression and penetration testing) · Reliability & Performance (DR and failover drills, 99.9%+ availability, latency tuning, concurrency control, P1–P3 incidents and RCA, Splunk) · Leadership (multiple squads through squad leads/EMs, coaching, architecture and code reviews, standards — contributed) · AI-Assisted Engineering (production AI code review, human-in-the-loop governance).

## Selected Achievements
1. **Core-banking-integrated platforms** — S2 + PA-05.1 (customer-360: daily account summaries for portfolio analysis).
2. **Legacy modernisation** — PA-01.1.
3. **Hands-on architecture & code** — S6 + S5 (+ PA-01.2 short if it fits).
4. **Lending servicing & collections** — PA-04.1.
5. **AI-assisted software development** — PA-07.1/07.2/07.3.
6. **Reliability** — PA-02.1 + X-06 (RCA).
7. **Multi-squad leadership** — X-02 + PA-03.1/03.2 (CI/CD quality).

## Experience plan
- **UOB** scope line. Sub-headings: *Architecture & Engineering* (PA-01.2, PA-01.4, PA-05.2/05.3, S2 where not already in achievements) → *Delivery & Platform Ownership* (PA-01.5, X-02 MVP sequencing, C-RPT) → *Reliability, Security & Governance* (X-06, PA-02.2/02.3, X-01, PA-03.3 contributed standards). 9–11 bullets, no repeats of achievements.
- **Golden Bridge** 2–3: PA-10.1 (microservices on Spring Cloud/Kubernetes, API gateway), PA-10.3, X-01.
- **VV** 3–4: S3 org; PA-11.4; S1 payments + PA-11.2; PA-12 [R22] data platform (Spark) if space.
- **Hengshunyuan**: Earlier line.
- **AI Park** 2: PA-16.1, PA-16.4 (+ MongoDB via big-data team line if useful).
- **Earlier**: Baidu (PA-17.1 Dubbo re-architecture, delivered two months ahead of plan), Sohu (PA-18.1 MongoDB/Redis CMS re-architecture), Renren.

## Gaps → honest handling
Deposits and General Ledger → not claimed; Customer Management ↔ customer-360 (adjacent), Loans ↔ lending servicing & collections (adjacent), Transaction Processing ↔ payments (direct), Settlement ↔ integration only (S2). OpenShift → not claimed (Kubernetes). Angular → not listed (React only). SVP band → nothing to write; mention in analysis only.

## Keyword map
core banking / large-scale transaction processing → PA-01, S2 · leading teams while active in architecture → X-04/S5, S6 · Java/Spring Boot, React, microservices & API, event-driven, CI/CD & DevSecOps, Linux & middleware, Kubernetes, MongoDB → skills inventory · distributed systems, resiliency, performance, HA → PA-02.1, PA-01.4, S6 · platform modernisation & legacy transformation → PA-01.1 · architecture/design/code reviews → S5, PA-03.3 · AI-assisted software development → PA-07 · critical incidents & RCA → X-06 · coach engineers, TLs, EMs → X-02.

---

# Card 05 — Solderfield — Chief Technology Officer/Director (Business Partner) (JobStreet 95022480)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95022480
- **Triage:** tier **B** · batch match score **83** · ⚠ employment form unclear ("business partner") — Wilson does not accept non-salaried roles; confirm before applying
- **Family × lens:** **SM × BNK** (technical + commercial leadership of a banking-solutions software business)
- **file_stem:** `wilson-2026_SM_Bank_Solderfield_V1_0_0` · folder `2026-10-21_Solderfield_CTO-Director`
- **Base:** Talentvis JSON + `LIB_wilson-2026_Senior_Tech_Bank_LIB_V5_0_0.txt` + `LIB_wilson-2026_Archi_Bank_LIB_V5_0_0.txt`.

## Headline (one line; no "CTO")
`Banking Technology Leader — Payment Middleware, Message Transformation & Productised SaaS | Solution Design to Delivery`

## Summary storyline
1. First sentence = JD core: banking technology leader who designs and delivers payment middleware in a Tier-1 bank — validation, enrichment, ISO 20022 message transformation, integration with core banking — and who has turned platforms into configurable products.
2. Productisation and entrepreneurship: architected a customisable multi-tenant SaaS from 0 to 1 (GBD); built VV's platforms from scratch; co-founded an audio-learning start-up (entrepreneurial ownership; fundraising failure is not mentioned).
3. Commercial and delivery: led technical bids that won city projects (AI Park — the only vendor-side pre-sales on record, S7); buyer-side vendor selection and SOW/licence negotiation and vendor governance at UOB; end-to-end delivery from requirements to production support under banking governance (change control, release governance, access control, audit-ready releases).

## Core Competencies
Banking Solutions (payment initiation, validation, enrichment, status tracking, ISO 20022 message transformation, core-banking integration, retail lending servicing) · Solution Architecture (middleware, APIs, microservices, Apache Camel, workflow orchestration, legacy modernisation, coexistence cut-over) · Productisation (multi-tenant, configurable SaaS; reusable backend services; version and release management) · Commercial (technical bids and proposals, vendor selection, SOW/licence negotiation, budgets, vendor performance reviews) · Banking Governance (secure SDLC, role-based access control, change control, release governance, audit-ready SIT/UAT sign-off, DR, MAS TRM) · Delivery (requirements to production and support; Agile/Scrum, hybrid Waterfall; RAID; steering committees) · Technical (Java, Spring Boot, Spring Cloud, Kubernetes, AWS, Linux (RHEL), SQL).

## Selected Achievements
1. **Payment middleware in a Tier-1 bank** — PA-01.2 + S2 (short).
2. **Modernisation without disruption** — PA-01.1.
3. **Configurable product from 0 to 1** — PA-10.1 (customisable multi-tenant SaaS).
4. **Technical bids won** — PA-16.2.
5. **Commercial authority** — X-02 commercial + X-05.
6. **Banking-grade governance** — PA-03.1 (release governance, SIT/UAT sign-off) + X-01 (access control via role-permission design, encryption).
7. **Entrepreneurial ownership** — PA-15.1 (co-founder; 0 to ~100k DAU).

## Experience plan
- **UOB** scope line. Sub-headings: *Solution Architecture & Engineering* (S6, PA-01.4, PA-05 + S2) → *Delivery & Governance* (PA-01.5, X-06, PA-03.2/03.4, data migration X-01) → *Commercial & Stakeholders* (C-RPT, X-02 MVP, PA-04.1). 9–10 bullets.
- **Golden Bridge** 3: PA-10.3 (budget, launch readiness), hybrid delivery, PA-10.2 rule models (configurable rules — no 200+).
- **VV** 3–4: S3; S1 payments + PA-11.2; PA-13 B2B middle platform (cost evaluation, acceptance — unnamed); PA-11.3/11.5.
- **Hengshunyuan** full role 1–2 bullets (PA-15.2 licensing = commercial content deals).
- **AI Park** 2: PA-16.1 (SaaS model for B2B/B2G), PA-16.3 or PA-16.4.
- **Earlier**: Baidu, Sohu, Renren (+ S1 short only if space).

## Gaps → honest handling
IBM iSeries/AS400, Silverlake → none; not mentioned. Vendor-side pricing, costing, contract negotiation, invoicing → none beyond AI Park bids; buyer-side commercial experience shown as such. IP-ownership practices → not claimed. CTO title → never.

## Keyword map
banking technology and transaction processing → PA-01, S2 · middleware, APIs, microservices, message transformation → PA-01.2 (Camel, ISO 20022) · legacy modernisation → PA-01.1 · productisation, configurable products → PA-10.1, PA-10.2 · proposals, tenders → PA-16.2 · commercial, negotiation → X-02 (SOW/licence, buyer side), X-05 · end-to-end delivery → PA-01.5 · access controls, change management, release governance, resilience → X-01, PA-03.1, PA-02.1 · entrepreneurial mindset → PA-15.

---

# Card 06 — Airwallex — Engineering Lead/Manager, Growth (SG/SH) (JobStreet 88086261)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/88086261
- **Triage:** tier **B** · batch match score **81** · JD incomplete (no requirements section) · posted 30d+ → confirm still open
- **Family × lens:** **SM × INT** (hands-on engineering lead of a product team at a fintech that hires like an internet company)
- **file_stem:** `wilson-2026_SM_Internet_Airwallex_V1_0_0` · folder `2026-10-21_Airwallex_Engineering-Lead-Growth`
- **Base:** Talentvis JSON + `LIB_wilson-2026_Senior_Tech_Internet_LIB_V5_0_0.txt`.

## Headline (one line)
`Engineering Lead — Consumer & Fintech Platforms | Hands-On Design and Code Review · User Onboarding & Payments`

## Summary storyline
1. First sentence = JD core: hands-on engineering lead who turns product requirements into designs, delivery plans and working software for consumer and fintech platforms — 18+ years from Renren e-commerce, Sohu News and Baidu Nuomi to start-up platforms and a Tier-1 bank.
2. UOB: leads 25 engineers through squad leads, works with product owners and business on requirements and backlog, reviews new core PRs daily, co-designs solutions and writes core modules; AI code-review service raised review throughput (estimated ~80% senior review time).
3. Consumer onboarding and payments: hierarchical KYC identity verification (GBD); payment integrations across wallets and cards (S1); consumer product from launch to ~100k DAU (Hengshunyuan); Agile/Scrum set up from scratch; cross-time-zone collaboration; Mandarin + English (useful for SG/Shanghai — state only as language line, no claim about Shanghai).

## Core Competencies
Engineering Leadership (goals, feedback and development plans, 1:1s, mentoring, code-review standards, squad leads/EMs) · Product Delivery (requirements analysis with product owners, solution design, execution plans, backlog and roadmap, Agile/Scrum, releases) · Consumer Platforms (e-commerce, group-buying, local-life services, content platform; user onboarding and KYC) · Payments (wallet and card payment integrations, settlement reconciliation, payment status tracking) · Hands-On Engineering (Java, Spring Boot, Spring Cloud, React, SQL; concurrency and performance tuning) · Cloud & Data (AWS, Kubernetes, Docker, Kafka, Redis, Elasticsearch, MySQL) · AI-Assisted Engineering (production AI code review, prompt A/B evaluation, human-in-the-loop governance).

## Selected Achievements
1. **Hands-on lead** — S6 + S5.
2. **Faster code review** — PA-07.1/07.3.
3. **User onboarding at scale** — PA-10.2 (hierarchical KYC; rule models) + PA-10.1 short.
4. **Payments across wallets and cards** — S1.
5. **Consumer product growth** — PA-15.1 (0 to ~100k DAU) + PA-11.4 (millisecond-level services) — keep factual.
6. **Teams and ways of working** — PA-10.3 (40-person team, total headcount; Agile/Scrum from scratch) + X-02 mentoring.
7. **Production ownership** — PA-01.1 or X-06 (short).

## Experience plan
- **UOB** scope line (plain English). Sub-headings: *Engineering & Design* (PA-01.2 short, PA-01.4, PA-05 short) → *Delivery with Product* (PA-01.5, X-02 MVP sequencing with requirement/project/tech leads, TEKsystems "Agile delivery governance" bullet) → *Team & Productivity* (X-02, PA-07.4 + S9, coaching on AI-assisted engineering, C-RPT cross-time-zone). 9–10 bullets.
- **Golden Bridge** 3: PA-10.1 (if not in achievements), PA-10.2 (if not), AWS stack + X-01 — avoid repeats.
- **VV** 4: S3; S1 + PA-11.2; PA-11.4 (if not in achievements); PA-11.3/11.5; PA-12 big-data (data-driven decisions) optional.
- **Hengshunyuan** full role 1–2 bullets (consumer product).
- **AI Park** 2: PA-16.1, PA-16.4.
- **Earlier**: Baidu + S1, Sohu, Renren + S1.

## Gaps → honest handling
Growth engineering (funnels, A/B-testing frameworks, marketing-platform integration) → none; do not claim (prompt A/B testing is not growth experimentation — keep it in the AI context). Hiring: no numbers. Shanghai option: no claim.

## Keyword map
lead a team, goals, feedback, development plans → X-02 · analyse requirements with PMs, technical solutions & execution plans → PA-01.2, X-02 MVP sequencing, TEKsystems Agile governance · hands-on design and implementation → S6, S5 · validate team designs, review code, standards → S5, PA-03.3 · backlog → TEKsystems bullet · hiring & training → mentoring only · cross-team collaboration → C-RPT · onboarding → PA-10.2 · high-traffic pages → Renren/Nuomi/VV (no numbers) · uses AI to work smarter → PA-07.

---

# Card 07 — Landi International — Chief Technology Officer (JobStreet 95323660)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95323660
- **Triage:** tier **B** · batch match score **75** · foreign company, ad not hirer-verified
- **Family × lens:** **SM × BNK** (technology executive for a payments-hardware/software company's overseas markets)
- **file_stem:** `wilson-2026_SM_Bank_Landi_V1_0_0` · folder `2026-10-21_Landi_CTO`
- **Base:** Talentvis JSON + `LIB_wilson-2026_Senior_Tech_Bank_LIB_V5_0_0.txt`.

## Headline (one line; no "CTO")
`Payments Technology Leader — Fintech Platforms, Connected Devices & Multi-Market Delivery | Strategy · Teams · Budgets`

## Summary storyline
1. First sentence = JD core: payments technology leader with 18+ years across a Tier-1 bank in Singapore, fintech and SaaS platforms in Singapore and Southeast Asia, and consumer internet in China; head-of-technology roles 2016–2022 (never "CTO").
2. UOB: owns architecture and delivery for mission-critical cross-border payments; technology investment, vendor selection and budgets; leads teams onshore/offshore and works with teams in India, Thailand and Indonesia; reports to senior management and steering committees (not "Board").
3. Connected devices and markets: headed technology for a smart-parking IoT platform connecting car-park hardware to the cloud, with city bids and pilots; payment integrations across China (Alipay, WeChat Pay, UnionPay) and Singapore (UnionPay, Visa/Mastercard, Google Pay, GrabPay) (S1); B2B product for Southeast Asia (PA-13); production AI service; bilingual English/Mandarin.

## Core Competencies
Technology Strategy (roadmaps, technology selection, investment priorities, platform modernisation, capacity planning) · Payments & Fintech (cross-border payments, ISO 20022, payment initiation and settlement integration, card and wallet payment integrations, reconciliation) · Connected Devices & IoT (car-park hardware connected to the cloud, recognition pipeline, real-time events) · Multi-Market Delivery (Singapore, China and Southeast Asia platforms; city rollouts; cross-time-zone teams in India, Thailand and Indonesia) · Leadership & Budgets (technical and delivery teams through squad leads, technology budget, vendor selection and governance, SOW/licence) · Engineering Practice (Agile/Scrum, CI/CD, code-quality gates, secure SDLC, DR, incident management) · Architecture & AI (cloud-native microservices, APIs, AWS, Kubernetes; production AI code review).

## Selected Achievements
1. **Payments platform modernisation** — PA-01.1 (+ PA-01.2 short).
2. **Connected-device platform and city rollouts** — PA-16.1 + PA-16.2.
3. **Payments across two markets** — S1.
4. **Technology strategy and budget** — PA-11.1 short + S3 (140-person org, total headcount; technology selection; budget).
5. **Distributed teams and governance** — X-02 cross-time-zone + PA-03.1 KPIs.
6. **AI-enabled delivery** — PA-07.1/07.3 (+ PA-16.3 AI recognition step if it fits).
7. **Security-sensitive operations** — PA-02.1 + X-01.

## Experience plan
- **UOB** scope line. Sub-headings: *Technology Leadership & Strategy* (X-02 commercial authority, X-05 vendors, X-02 MVP sequencing, PA-04.1) → *Architecture & Delivery* (PA-01.2 or S6, PA-01.5, PA-05 + S2) → *Reliability & Governance* (X-06, PA-03.2, C-RPT). 9–10 bullets.
- **Golden Bridge** 2–3: PA-10.1 (multi-tenant SaaS, multi-channel payments, KYC across jurisdictions — no 200+), PA-10.3, hybrid delivery.
- **VV** 3–4: S1 + PA-11.2; PA-13 SEA B2B product; PA-11.3/11.5; (S3 if not in achievements).
- **Hengshunyuan**: Earlier line.
- **AI Park** 3: PA-16.1/16.2 (if not in achievements → PA-16.3, PA-16.4, big-data team), introduced SaaS model for business and government customers.
- **Earlier**: Baidu + S1, Sohu, Renren + S1.

## Gaps → honest handling
Payment terminals / POS → not claimed; bridge = connected IoT devices (AI Park) + payment integrations. International market strategy → shown as multi-market platforms (SG/China/SEA), not "overseas strategy for N countries". Board reporting → not claimed (senior management and steering committees). "5 years in senior technology leadership" → head-of-technology roles 2016–2022 + current VP role (state roles, no year count).

## Keyword map
technology vision and roadmap → PA-11.1 technology selection, PA-01.5 roadmap · overseas/international markets → SEA product (PA-13), SG/China payment integrations (S1), city rollouts (PA-16.2) · payments/fintech → PA-01, S1, S2 · payment terminals, connected devices, integrated hardware and software → PA-16 (car-park hardware to cloud) · deploy, localise, support, maintain → PA-16.2 pilots, X-06 production support · distributed technical and PM teams → X-02 · budgets, resources, capacity → X-02, PA-02.1 capacity baselines · executive communication → C-RPT · emerging tech, AI → PA-07, PA-16.3 · Agile, CI/CD, code quality, technical debt → PA-03.1/03.2, PA-01 "reduced technical debt" (📄).

---

# Card 08 — Income Insurance — Head, Technology Transformation (JobStreet 95105986)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95105986
- **Triage:** tier **B** · batch match score **75**
- **Family × lens:** **TPM × BNK** (transformation programme leadership in a regulated financial-services firm; reports to the Chief Strategy Officer)
- **file_stem:** `wilson-2026_TPM_Bank_Income_V1_0_0` · folder `2026-10-21_Income_Head-Technology-Transformation`
- **Base:** approved TEKsystems JSON (TPM) + `TPL_TPM_Bank_template.txt` + `LIB_wilson-2026_TPM_Bank_LIB_V5_0_0.txt`.

## Headline (one line)
`Technology Transformation Leader — Regulated Platform Modernisation & AI Adoption | Programme Governance · Vendor Ecosystems`

## Summary storyline
1. First sentence = JD core: technology transformation and programme leader who modernises core platforms in a regulated financial institution and takes AI from idea to governed production — 18+ years across a Tier-1 bank, fintech/SaaS and consumer internet.
2. UOB: owns the cross-border payments modernisation (ISO 20022) through coexistence to retirement of the old mode — roadmap, dependencies, governance forums, steering-committee reporting — and two AI tools taken into production after formal architecture and risk approval; drives adoption by coaching teams.
3. Earlier: led technology organisations through 0-to-1 digital platforms (VV 140-person organisation, GBD 40-person project team — total headcount), city rollouts, vendor ecosystems (four IT service vendors today); PMP in progress.

## Core Competencies
Transformation Programmes (roadmap, initiatives, interdependencies, RAID, scope/schedule/budget, release cadence, value-focused delivery) · Platform Modernisation (legacy-to-ISO 20022 migration, coexistence and cut-over, core-banking integration, customer-360 data platform) · AI Adoption (production AI code review and document-validation agent, human-in-the-loop governance aligned with MAS FEAT, RAG contribution, coaching teams) · Governance & Reporting (steering committees, decision forums, delivery KPIs, SIT/UAT sign-off, change control, risk and regulatory compliance — MAS TRM) · Vendors & Partners (vendor selection, SOW/licence negotiation, vendor performance and accountability reviews, onshore/offshore delivery partners) · Stakeholders & Change (business, operations, compliance, architects, engineering managers; Agile adoption from scratch; cross-time-zone teams) · Methods & Tools (Agile/Scrum, hybrid Waterfall, Jira, Confluence, MS Project).

## Selected Achievements
1. **Core-platform modernisation** — PA-01.1 + PA-01.5 (merged, ≤ 3 lines).
2. **AI from idea to governed production** — PA-07.1/07.2 + S9 (approval) + PA-07.3 estimate.
3. **Automation of a manual process** — PA-08.
4. **Vendor and partner ecosystem** — X-05 + X-02 commercial.
5. **Governance that holds** — PA-03.1 (KPIs, release governance, SIT/UAT sign-off) + C-RPT.
6. **Scale-up transformation** — S3 (140-person org, total headcount) + PA-11.2 (first release 2019) — or PA-16.2 city rollouts.
7. **Priorities across two lines** — X-02 MVP sequencing (+ PA-04.1 short).

## Experience plan
- **UOB** scope line. Sub-headings: *Transformation Programme Delivery* (TEKsystems "Own end-to-end delivery…", "Run Agile delivery governance…", S2 core-banking integration, PA-05 customer-360) → *AI Adoption & Change* (RAG contribution O5, coaching on AI-assisted engineering, AI governance model) → *Governance, Risk & Production* (X-06, PA-03.3 contributed standards, PA-03.4, X-01 data migration). 9–11 bullets.
- **Golden Bridge** 3: context line (scope), PA-10.3, hybrid delivery.
- **VV** 3–4: S3, PA-11.2 (+ S1 short), PA-13, PA-11.3/11.5.
- **Hengshunyuan**: Earlier line.
- **AI Park** 2: PA-16.1, PA-16.2.
- **Earlier**: Baidu (two months ahead of plan), Sohu (PA-18.2 publishing workflow — contributed), Renren.

## Gaps → honest handling
"15+ years leading large-scale transformation" → do not claim a year count; show 18+ years in total and the leadership roles. "Enterprise-wide" portfolio → not claimed (platform-line programmes). C-suite → "senior management and steering committees". Benefits realisation against business cases → not claimed. Insurance domain → none (not mentioned). PMP → "in progress" only.

## Keyword map
enterprise technology transformation roadmap → PA-01.5 roadmap · programmes from initiation to value → PA-01.1 dated milestones · interdependencies, risks, priorities → RAID, X-02 MVP · scope, timelines, budget → PA-10.3, PA-01.5 · compliance with architecture, risk, regulation → architecture and risk approval (S9), MAS TRM · AI, automation → PA-07, PA-08 · adoption, change → coaching, Agile from scratch · vendors, system integrators, delivery partners → X-05, X-02 · governance, reporting, decision forums → steering committee, KPIs.

---

# Card 09 — NCS — #EG Associate Director – Solution Architect (Technical) (JobStreet 94992125)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/94992125
- **Triage:** tier **B** · batch match score **75** · same group as Wilson's Singtel Delivery Manager application → keep facts identical
- **Family × lens:** **ATL × INT** (solution architect for reusable assets at a systems integrator serving enterprise and public-sector clients)
- **file_stem:** `wilson-2026_ATL_Internet_NCS_V1_0_0` · folder `2026-10-21_NCS_AD-Solution-Architect`
- **Base:** Talentvis JSON + `LIB_wilson-2026_Archi_Internet_LIB_V5_0_0.txt` (ATL × INT, Platform Architect / SaaS headline).

## Headline (one line)
`Solution Architect — Reusable Platforms, Integration Architecture & Cloud-Native Delivery | Designed and Delivered in a Tier-1 Bank`

## Summary storyline
1. First sentence = JD core: solution architect who designs scalable, reusable platforms and stays accountable through delivery and production sign-off — 18+ years across banking, SaaS and consumer internet.
2. UOB (enterprise environment): designed the payment-initiation hub's integration architecture (API contracts, orchestration, channel, reference-data, vendor and core-banking integration), contributes to architecture-review governance and engineering standards, reviews designs and code, and owns security and resilience controls.
3. Reusable assets: multi-tenant, customisable SaaS platform from 0 to 1 (GBD); middle-platform architecture for a B2B product serving Southeast Asia (VV); technical bids that won city projects (AI Park); mentoring engineers; explains technical choices to business stakeholders and steering committees.

## Core Competencies
Solution Architecture (scalable platform design, reusable services and blueprints, integration patterns, NFRs, technical sign-off through delivery) · Integration & APIs (API-first design, Apache Camel, event-driven integration, enterprise systems, vendor and third-party integration, core-banking integration) · Cloud-Native (microservices on Spring Cloud and Kubernetes, AWS — API Gateway, ECS, RDS, DynamoDB, SQS/SNS) · Multi-Tenant SaaS (tenant configuration, rule models, KYC, payments) · Governance & Standards (architecture-review governance and engineering standards — contributed; design and code reviews; secure SDLC; MAS TRM) · Risk & Resilience (encryption, credential management, access control, DR drills, 99.9%+ availability) · Stakeholders & Bids (technical bids, business-facing communication, mentoring, cross-time-zone teams).

## Selected Achievements
1. **Integration architecture** — PA-01.2 + S2.
2. **Reusable multi-tenant platform** — PA-10.1 (+ PA-10.2 rule models short).
3. **Middle platform for a regional product** — PA-13 (unnamed).
4. **Architecture governance** — PA-03.3 (contributed) + S5 (design/code reviews).
5. **Technical bids** — PA-16.2.
6. **Secure, resilient by design** — X-01 + PA-02.1.
7. **Reusable AI service** — PA-07.1 (production AI code-review service; no adoption numbers).

## Experience plan
- **UOB** scope line (plain English; explain MAS TRM at first use). Sub-headings: *Architecture & Design* (S6, PA-01.4, PA-05 + S2) → *Delivery Oversight* (PA-01.1/01.5 — no repeat of achievements, PA-03.1/03.2 quality gates) → *Stakeholders & Production* (C-RPT, X-06, X-02). 9–10 bullets.
- **Golden Bridge** 3: PA-10.3, AWS deployment + X-01, hybrid delivery.
- **VV** 3–4: S3, PA-11.4, S1 + PA-11.2, PA-11.3/11.5.
- **Hengshunyuan**: Earlier line.
- **AI Park** 2–3: PA-16.1 (+ SaaS model for business and government customers), PA-16.4.
- **Earlier**: Baidu (Dubbo re-architecture), Sohu (CMS re-architecture), Renren.

## Gaps → honest handling
Systems-integrator / client-facing architecture → not claimed as SI experience; show internal enterprise + vendor/third-party integration + AI Park bids. Associate Director level → nothing to write. TOGAF → not mentioned. Public-sector (IM8) → not claimed.

## Keyword map
solution architecture in an enterprise environment → PA-01.2 · scalable platform design, reusable assets → PA-10.1, PA-13 · blueprints, integration patterns → PA-01.2 · microservices, cloud-native, API-first → PA-10.1, skills · technical sign-off, delivery oversight → PA-01.1, PA-03.1 (SIT/UAT sign-off) · architectural standards, review mechanisms → PA-03.3 (contributed), S5 · mentor engineering teams → X-02 · pre-sales narratives → PA-16.2 · risk management → RAID (PA-01.5), X-01.

---

# Card 10 — CMA CGM — APAC Head of AI and Innovation (JobStreet 95377348)

- **JD:** `JD.md（各申请文件夹）` · https://sg.jobstreet.com/job/95377348
- **Triage:** tier **B** · batch match score **71** · local employment only (Singapore PR — fine)
- **Family × lens:** **SM × INT** (senior IT leader for applied AI adoption, prototyping and enablement in a global logistics group)
- **file_stem:** `wilson-2026_SM_Internet_CMACGM_V1_0_0` · folder `2026-10-21_CMA-CGM_APAC-Head-AI-Innovation`
- **Base:** Talentvis JSON (AI-first UOB block) + `LIB_wilson-2026_Senior_Tech_Internet_LIB_V5_0_0.txt`.
- **Positioning rule (01 §5):** an IT technical + management leader with applied AI and big-data pillars — **not** an "AI engineer" or "data scientist".

## Headline (one line)
`Technology Leader — Applied AI Adoption, Rapid Prototyping & Enterprise Delivery | Governed AI in Production · Data Teams`

## Summary storyline
1. First sentence = JD core: technology leader who takes AI from prototype to governed production inside a regulated enterprise and turns it into measurable productivity — 18+ years of IT leadership across a Tier-1 bank, fintech/SaaS and consumer internet.
2. UOB: designed and built an AI code-review service (live May 2026 after formal architecture and risk approval; estimated ~80% less senior review time) and an AI document-validation agent; set human-in-the-loop governance; contributed to a production RAG assistant with access controls and data masking; coaches teams on AI-assisted engineering.
3. Data and delivery: led big-data teams whose analysis supported business decisions (VV, AI Park); added an AI recognition step to an IoT platform; 0-to-1 platforms delivered fast; works across time zones with teams in India, Thailand and Indonesia; explains technology in business terms.

## Core Competencies
Applied AI in Production (LLM agents with headless Claude Code, agentic workflow orchestration, prompt A/B evaluation, AgentOps/LLMOps practice) · Responsible AI & Data Protection (human-in-the-loop governance aligned with MAS FEAT, access controls, data masking, encryption, secure SDLC, DPIA) · Prototyping & Delivery (rapid 0-to-1 builds, MVP scoping and sequencing, production-ready handover, CI/CD and quality gates) · Data & Analytics (big-data teams; Spark, Hive, HBase, Kafka; SQL; analytics for business decisions) · Enablement & Change (coaching teams on AI-assisted engineering and new practices, Agile adoption from scratch, standards — contributed) · Stakeholders (business translation, senior management and steering committees, vendor and investment decisions, cross-time-zone teams) · Platforms (Java, Spring Boot, Spring Cloud, AWS, Kubernetes).

## Selected Achievements
1. **Prototype to governed production** — PA-07.1 + S9 approval.
2. **Responsible AI** — PA-07.2 + RAG contribution (access controls, data masking) — O5 verb for RAG.
3. **Automation with measurable effect** — PA-07.3 (estimate) or PA-08 (removed recurring manual task) — use both across achievements and UOB bullets without repetition.
4. **Workflow automation agent** — PA-08.
5. **Data teams for decisions** — PA-12 [R22 Spark version] + AI Park big-data team.
6. **Fast 0-to-1 delivery** — PA-10.1 or PA-11.2 + S3.
7. **Engineering enablement** — coaching on AI-assisted engineering (PA-03 §6) + Agile from scratch (PA-10.3).

## Experience plan
- **UOB** scope line. Sub-headings: *Applied AI & Automation* (prompt A/B + AgentOps PA-07.4, RAG bullet, coaching bullet — avoid repeating achievements) → *Platforms & Data* (PA-01.2 short, PA-05 customer-360 + S2 portfolio analysis, S5 hands-on) → *Delivery & Governance* (PA-01.1 short, X-06, PA-03.1, C-RPT). 9–10 bullets.
- **Golden Bridge** 2–3: PA-10.3, PA-10.1 (if not in achievements), X-01.
- **VV** 3–4: S3; PA-12 big-data team (if not in achievements); S1 + PA-11.2; PA-11.3/11.5.
- **Hengshunyuan**: Earlier line.
- **AI Park** 3: PA-16.1, PA-16.3 AI recognition step, big-data team (HBase, MongoDB, Spark Streaming).
- **Earlier**: Baidu, Sohu, Renren.

## Gaps → honest handling
Power BI, low-code/no-code, citizen-developer platforms → not claimed (Power BI is F/P only — omit). Organisation-wide digital-literacy programmes → not claimed; show team-level coaching. Global matrix organisation → show cross-time-zone teams and steering committees only. Logistics domain → none. Data science / ML model training → not claimed (applied AI delivery).

## Keyword map
production-ready AI/ML solutions → PA-07, PA-08 · enterprise AI adoption → PA-07 approval path, coaching · responsible AI governance, data privacy → PA-07.2, RAG access controls/data masking, X-01 · rapid prototypes and MVPs → PA-10.1, PA-11.2, X-02 MVP sequencing · production-ready handover → CI/CD quality gates PA-03.2 · data engineering → PA-12, AI Park big data · change and culture → coaching, Agile from scratch · ROI → estimated ~80% review time; removal of a recurring manual task · influence senior stakeholders → C-RPT, X-02.

---

