# Wilson Zhang — Master Career Profile & Achievement Library

**Version:** v1.0 · 2026-10-15 · **Owner:** Wilson Zhang
**Purpose:** Single source of truth for all tailored resumes. Never send this file directly; never overwrite it with a tailored version.
**Built from (6 source libraries, all V5_0_0_1):** Senior_Tech_Bank · Senior_Tech_Internet · Archi_Bank · Archi_Internet · TPM_Bank · TPM_Internet
**Not yet ingested:** Big Data AI library (`wilson-2026_BD_V3_0_0.docx`) — see Q12.

---

## 0. Legend

**Verification status**
- ✅ **Verified** — stated consistently across all source libraries and/or previously confirmed by Wilson.
- 🔶 **Interpretation** — defensible framing of verified facts; wording is a choice, not a new fact.
- ❓ **Needs confirmation** — inconsistent across sources, unattributed, or carries interview-defensibility risk. Do not use in a tailored resume until resolved (see §13).

**Capability tags (Rule 3 — keep these distinct)**
- **[HC]** Hands-on coding · **[AR]** Architecture / design · **[TL]** Technical leadership (direction, reviews, standards) · **[DM]** Delivery / programme management · **[PL]** People leadership / line management · **[CV]** Commercial, vendor, budget · **[GV]** Governance, risk, compliance, security

---

## 1. Identity & Contact ✅

- **Name:** Wilson Zhang
- **Location / status:** Singapore · Singapore PR
- **Phone:** +65 8655 9547 · **Email:** Skyzhang1028@gmail.com
- **Languages:** English and Mandarin (professional working proficiency in both)
- **Total experience:** 18+ years (2008 – present) — use "18+" in every version; never 17 or 20.

---

## 2. Canonical Timeline ✅

| Period | Employer | Title | Location | Notes |
|---|---|---|---|---|
| Oct 2022 – Present | United Overseas Bank (UOB) | Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations | Singapore | Tier-1, MAS-regulated. "TDM" suffix used in TPM variants only. |
| Nov 2020 – Jul 2022 | Golden Bridge Drive (SG) Pte. Ltd. | Project Manager & Architect | Singapore | 0-to-1 multi-tenant gaming-platform SaaS on AWS (see Q8) |
| May 2020 – Present | Pureland Holding (Jewelake) | Technical Consultant (concurrent part-time advisory) | — | Selective module only; conflict-of-interest disclosure needed for bank roles |
| Apr 2019 – Jun 2020 | VV Technology Pte. Ltd. | Head of Technical Centre | Singapore | VV-Life 0-to-1 |
| Oct 2017 – Sep 2019 | Hengshunyuan Information Technology | Founder (own start-up) | China | Audio/media content app (有声青蛙) |
| Apr 2016 – Sep 2017 | AI Park | VP of Technical Department | China | Smart-parking IoT; dates confirmed canonical |
| 2014 – 2014 | Baidu | Technical Specialist — Nuomi.com (group-buying / local-services e-commerce) | China | Earlier experience |
| 2012 – 2014 | Sohu.com | Technical Leader — Sohu News media platform | China | Earlier experience |
| 2008 – 2012 | Renren Network | Senior R&D Engineer — Renren-Mall (e-commerce of Renren social network) | China | Earlier experience |

**Timeline gaps (❓ Q11):** 2015 → Apr 2016 · Jul 2022 → Oct 2022. Prepare a one-line explanation for each; LeMail/Letv is under an editorial lock (omitted from all variants).

**Education & certifications ✅**
- Master of Computer Application — Liaoning University (2005 – 2008)
- Bachelor of Information and Computing Science — Shenyang University of Technology (2000 – 2004)
- Intermediate Software Designer — Qualification Certificate of Computer and Software Technology Proficiency (2006)
- PMP — **in progress** (never write "certified" until passed). No TOGAF, ITIL, PRINCE2, PMI-ACP, AWS or other cloud certifications.

---

## 3. Factual Positioning (master statement) 🔶

> Senior IT technical and management professional with 18+ years across banking payments, fintech SaaS and high-concurrency internet platforms, combining hands-on Java engineering, solution architecture, delivery management and people leadership — with substantial big-data analytics and applied-AI project experience, including a production agentic-AI service inside a Tier-1 regulated bank.

**Standing rule:** do not package Wilson as an "AI engineer" or "big data engineer" to fit a JD. AI and data are pillars, not the identity.

---

## 4. Capability Evidence Matrix

| Employer | [HC] Hands-on | [AR] Architecture | [TL] Tech leadership | [DM] Delivery | [PL] People | [CV] Commercial |
|---|---|---|---|---|---|---|
| UOB | ✅ Java/Spring Boot/Camel payment services; AI code-review service; code reviews, prod troubleshooting (scope ❓Q7) | ✅ CEW integration, Blue/Green coexistence, DR, security controls | ✅ Standards, architecture/code reviews, vendor tech evaluation | ✅ CBPR+ programme end to end, SIT/UAT, release governance | ✅ 20+ engineers, 2 lines, via squad leads & EMs; offshore | ✅ Investment, vendor selection, SOW/licence (decision or joint-decision); delivery budget |
| Golden Bridge | 🔶 Reusable backend services, CI/CD | ✅ Spring Cloud + K8s microservices, API gateway | ✅ | ✅ Hybrid Waterfall/Agile; Agile from scratch | ✅ Team capacity | ✅ Delivery budget |
| VV Technology | 🔶 Flink systems "built" | ✅ Microservices, data platform, MLOps | ✅ | ✅ VV-Life E2E | ✅ Engineering, DevOps, data teams | ✅ Technology budget |
| Hengshunyuan | ✅ Backend, cloud deployment | ✅ | — | ✅ | 🔶 | ✅ Founder |
| AI Park | 🔶 | ✅ High-concurrency microservices | ✅ | ✅ City rollouts | ✅ Department head; big-data team | ✅ Budget; 4+ bids won |
| Baidu/Sohu/Renren | ✅ Engineer → Technical Leader | 🔶 | 🔶 Sohu Technical Leader | — | — | — |

---

## 5. Experience — Master Bullet Library (deduplicated union of all 6 sources)

### 5.1 UOB — Oct 2022 – Present ✅

**Scope statement:** Lead technology for mission-critical cross-border payments (TT, RTGS, ISO 20022 CBPR+) and retail unsecured lending servicing and collections across regional banking operations — architecture, engineering delivery, production resilience, vendor/investment decisions and people leadership across two platform lines (20+ engineers) serving millions of accounts.

**Programme context — CBPR+ / ISO 20022 (CEW payment-initiation hub)** ✅
CBPR+ covers TT and RTGS payments across the coexistence and ISO-rich/MX-rich stages of the ISO 20022 (MX) migration, including authorisation procedures (group, account, product) and channel administration. CEW takes requests from Internet Banking and branch channels, uses FX-rate, account and customer reference data, performs validation, enrichment and pain.002 status tracking, and hands payments to downstream systems including the SWIFT ISO 20022 flow and CASA. Downstream processing and settlement sit in other systems.
> 🔒 Confidentiality: "CEW" is an internal system name. Use the descriptive phrase "payment-initiation hub" in resumes sent outside UOB unless already public; the internal name is fine in interviews only if you are comfortable.

**A. Architecture & hands-on engineering**
- U1 [HC][AR] ✅ Designed and implemented high-throughput, real-time payment-processing services for CBPR+ and RTGS flows in Java, Spring Boot and Apache Camel, personally authoring core transaction-processing and concurrency-control modules. *(scope ❓Q7)*
- U2 [AR] ✅ Led end-to-end system design — API contracts, service orchestration, validation, enrichment and pain.002 status tracking — and integration with upstream channels, reference data, vendor-delivered and third-party banking systems on Spring Boot and event-driven patterns.
- U3 [HC][AR] ✅ Reduced end-to-end transaction latency by tuning thread pools, minimising synchronous blocking and JVM tuning under high load. *(no figure — ❓Q10)*
- U4 [AR][DM] ✅ Architected and planned the phased, Blue/Green-style coexistence deployment across legacy MT and ISO 20022 MX-rich platforms — parallel traffic management and cutover readiness — with **no service interruption**.
- U5 [AR][GV] ✅ Designed security controls: API-call encryption/decryption, encryption of sensitive data in databases, dedicated credential-file management; led payment data migration under MAS TRM.
- U6 [AR] ✅ Led modernisation of high-volume payment platforms, improving scalability, resilience and operational stability. *(qualitative — avoid "materially" unless a metric exists)*

**B. Production resilience & engineering excellence**
- U7 [AR][GV] ✅ Defined DR strategy, failover procedures and capacity-planning baselines for real-time payment middleware; **personally led** DR and failover drills — sustaining **99.9%+ availability** and transaction integrity under peak load.
- U8 [AR][TL] ✅ Built a Splunk-based observability and alerting pipeline for real-time transaction monitoring; integrated SRE practice (SLIs/SLOs, toil reduction, incident management).
- U9 [TL][DM] ✅ Established delivery KPIs — deployment frequency, MTTR, incident trend, change-failure rate — with CI/CD release governance and the DevOps operating model.
- U10 [TL][GV] ✅ Governed quality gates on Bitbucket, Jenkins, SonarQube and Aldon: JUnit, **99% SonarQube coverage**, automated regression and penetration testing in CI/CD; SIT/UAT sign-off for all releases.
- U11 [TL][DM] ✅ Led incident response, RCA and resilience improvements, reducing MTTR; coordinated high-severity issues end to end — investigation, stakeholder communication, workaround tracking, permanent-fix closure; SLA tracking.

**C. Delivery management (CBPR+ programme)**
- U12 [DM] ✅ Owned end-to-end delivery of the CBPR+ / RTGS / ISO 20022 transformation — scope, delivery plan, roadmap, milestones, risks, dependencies, release planning and production rollout.
- U13 [DM] ❓ Managed delivery across **10+ interconnected payment domains** and multiple concurrent workstreams. *(origin: Stripe-tailored version — ❓Q4)*
- U14 [DM] ✅ Ran Agile delivery governance — sprint planning, backlog prioritisation, escalation, change control, RAID, KPI-driven reporting in Jira/Confluence — with executive-level status reporting and decision making.
- U15 [DM] ✅ Managed delivery risk across ISO 20022 migration, payment data transformation, system integration, regulatory timelines, production stability and release readiness.
- U16 [DM][AR] ✅ Facilitated architecture and solution trade-off discussions across legacy and modern platforms (integration approach, scalability, feasibility).
- U17 [DM][CV] ✅ Vendor coordination, dependency tracking and SLA governance across legacy and MX-rich payment systems.
- U18 [DM] ✅ Led cross-functional, cross-time-zone teams spanning development, system analysis, QA, DevOps, infrastructure, operations, compliance and external vendors.

**D. Retail unsecured lending servicing & collections** ✅
- U19 [AR][DM] Own the technology for payment initiation, validation and lifecycle tracking in retail unsecured lending servicing.
- U20 [AR][DM] Own post-disbursement credit collections across credit-card and unsecured-loan portfolios, drawing account and balance data from the card account system.
- U21 [GV] Led data migration and data-protection controls (sensitive-data encryption, credential management) across lending and customer-data platforms.

**E. People leadership & culture**
- U22 [PL] ✅ Lead both platform lines through squad leads and engineering managers (incl. dotted-line) — onshore/offshore developers, QA and BAs — with 1:1s, technical mentoring, career development and performance management.
- U23 [TL][HC] ✅ Stay hands-on across design, code review and complex production troubleshooting; architecture and code reviews and PR guidance across teams.
- U24 [TL] ✅ Coach delivery teams and drive adoption of new delivery practices and tooling, including AI-assisted engineering.
- U25 [PL] ✅ 5+ years managing offshore teams alongside onshore squads, in English and Mandarin.

**F. Standards, governance & risk**
- U26 [TL][GV] ✅ **Contributed to** bank-wide SDLC, coding, code-review standards and architecture-review governance beyond own squads. *(lock this verb — ❓Q6)*
- U27 [GV] ✅ Run secure SDLC, data governance and DPIA under MAS TRM; communicate designs, risks and trade-offs to senior technology, compliance and steering-committee audiences.

**G. Commercial, vendor & stakeholder**
- U28 [CV][TL] ✅ Lead evaluation of external vendors, start-ups and internal teams — architectural design, technical credentials, fit with existing systems — with **decision or joint-decision authority** on technology investment planning, vendor selection and SOW/licence negotiation; own delivery budget.
- U29 [DM] ✅ Primary interface between business, product owners, operations, compliance, architects and engineering managers; translate business needs into executable technical roadmaps; present to senior management and steering committees.
- U30 [DM] 🔶 Introduced AI-assisted delivery-risk forecasting from historical sprint data, improving programme predictability. *(method/outcome — ❓Q10)*

**H. UOB projects**
- **AI-Powered Code Review Service** (designed, built, in production) [HC][AR][TL] ✅ — see Achievement A3.
- **AI Validation of eMemo & Quotation Documents** [HC][AR] ✅ — AI agent auto-generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents; removed a recurring manual cross-document reconciliation task.
- **C360 Regional Customer 360 Platform (SCV-CCD)** [AR][DM][PL] ✅ — Led the SCV-CCD (Customer Centric Database) backend team under Waterfall governance; evaluated Cloudera as the data-processing framework; designed and optimised 360° customer data models (transactions, accounts, balances) with KYC-relevant data handling; APIs consumed by multiple business lines for Wealth cross-sell and client management; led related data migration.
- **VN eTax** [DM][PL] ✅ — Led the backend team delivering tax-certificate generation for completed transactions, enabling 24/7 tax payments.

### 5.2 Golden Bridge Drive (SG) — Nov 2020 – Jul 2022 ✅
**Context:** New gaming-platform SaaS built 0-to-1 on AWS — multi-tenant platform providing KYC, bonus, analytics (AnA), member VIP and payment-SaaS services to users across **200+ regions**. *(business-nature wording — ❓Q8)*
- G1 [AR] Designed the microservices architecture on Spring Cloud and Kubernetes with an API-gateway model, cloud deployment framework and integration patterns for payment, identity, KYC and user-management modules.
- G2 [AR][DM] Built and scaled the multi-tenant SaaS on AWS from 0 to 1 — payments, identity, KYC, user lifecycle.
- G3 [HC][AR] Built reusable backend services, CI/CD pipelines, AWS cloud-native infrastructure, deployment governance and the production support model.
- G4 [DM] Delivered KYC and payment modules for users across 200+ regions; managed cross-functional dependencies; kept the roadmap aligned with business development.
- G5 [DM][CV][PL] Managed team capacity, delivery budget, module priorities, technical risks, stakeholder alignment and launch readiness across engineering, QA, DevOps, product and operations.
- G6 [DM] Hybrid delivery: Waterfall scope/budget/timeline/milestone planning with Agile sprint execution.
- G7 [DM][TL] Implemented Agile/Scrum from scratch for lean engineering teams; led squads on tight iteration cycles.
- G8 [GV] Applied DPIA, API-call encryption/decryption, sensitive-data encryption, credential management; led data migration.
- G9 [DM] Business and operational reporting on Power BI and Splunk.

### 5.3 VV Technology — Apr 2019 – Jun 2020 ✅
**Context:** VV-Life (0-to-1) — "change life through data": connecting offline businesses with big data, real-time analytics and blockchain to build a local-life services ecosystem (food, groceries, travel, everyday services).
- V1 [PL][CV][TL] Led the technical centre — engineering, DevOps and data teams — and owned the technology budget; built engineering organisations and delivery models supporting expansion across multiple regions. *(which regions? 🔶)*
- V2 [TL] Partnered with product and business on roadmap, architecture planning and technology strategy.
- V3 [DM] Managed end-to-end VV-Life delivery — roadmap, requirements, architecture, testing, release, production support; hybrid Agile/Waterfall.
- V4 [AR] Designed and implemented distributed microservices on Spring Cloud and Kubernetes, with API platforms on AWS (CloudWatch).
- V5 [AR] ❓ Supported platforms processing multi-million daily transactions across payments and digital-services ecosystems. *(attribution — ❓Q3)*
- V6 [AR][GV] Improved production stability and reduced critical incidents through resilience engineering; introduced Splunk-based SLOs, alerting and dashboards.
- V7 [HC][AR] Built the Flink-based real-time/offline ad-order tracking system.
- V8 [HC][AR] Built a Flink-based real-time customer-profiling system using causal inference.
- V9 [AR] Built real-time and offline data pipelines and MLOps architecture for recommendation algorithms, analytics and monitoring.
- V10 [AR] ❓ "Delivered a GenAI customer chatbot using self-attention models, RAG, LLM integration and function calling." **Anachronism risk** — LLM "function calling" did not exist before mid-2023 and RAG was only published in May 2020; VV ended Jun 2020. Reword before use (❓Q5).
- V11 [TL][DM] Established CI/CD pipelines, release governance and containerised deployments, tracking deployment frequency, MTTR, incident trend and change-failure rate.
- V12 [AR][CV] Reduced infrastructure cost through AWS optimisation and CI/CD automation. *(no figure — ❓Q10)*
- V13 [TL] End-to-end test strategy — JUnit, integration, SIT, UAT — with 99% SonarQube coverage enforced.
- V14 [GV] API-call encryption/decryption, database encryption of sensitive data, credential-file management; platform data migration.
- V15 [AR] Managed containerised workloads on Kubernetes with deployment readiness and rollback.
- V16 [DM] Business analytics on Tableau and Splunk; aligned product, business, engineering, DevOps and data teams on priorities and go-live readiness.

### 5.4 Hengshunyuan — Oct 2017 – Sep 2019 ✅
- H1 [HC][AR][DM] Founded the company and built an audio and media content distribution app (有声青蛙) from 0 to 1; led product design, backend architecture and AWS cloud deployment.

### 5.5 AI Park — Apr 2016 – Sep 2017 ✅
**Context:** Intelligent-parking IoT platform connecting parking facilities to the cloud — automated site management, online payment, personalised recommendations.
- P1 [PL][CV][TL] Headed the technical department — technology direction, architecture, delivery, team leadership and budget.
- P2 [CV] Coordinated technical bidding for urban AI-parking projects; won **4+ city projects**.
- P3 [DM] Oversaw deployment across **1,000+ public parking lots**; pilots in Shijiazhuang (2016), Handan (2017), Beijing Chaoyang (2017).
- P4 [AR] Built high-concurrency microservices and distributed systems connecting sites to the cloud.
- P5 [AR][DM] Delivered automated site management, online payment and personalised recommendations.
- P6 [AR][PL] Led the big-data team building offline + online analytics on HBase, MongoDB, MapReduce, Spark Streaming and ETL, processing millions of real-time sensor and transaction events.
- P7 [GV] API-call encryption/decryption, sensitive-data encryption, credential management; data migration.

### 5.6 Earlier experience ✅
- Baidu — Technical Specialist, Nuomi.com (group-buying / local-services e-commerce) (2014 – 2015)
- Sohu.com — Technical Leader, Sohu News media platform (2012 – 2014)
- Renren Network — Senior R&D Engineer, Renren-Mall e-commerce platform (2008 – 2012)
- Wilson regards the Baidu, Sohu, Renren, own start-up and VV Technology work as e-commerce / consumer-platform experience.

### 5.7 Selective modules (splice in only when the JD calls for it)
- **Pureland Holding (Jewelake)** — Technical Consultant, concurrent part-time, May 2020 – Present ✅. Wealth quant platform (VWAP execution, portfolio management, risk analytics) on Spark/Hadoop; Spring services on AWS, S3 tick data, Spark Streaming + Spark SQL, Bloomberg and Yahoo Finance data; Claude agent comparing daily trading patterns against 10-day and 6-month baselines for risk-scored recommendations and alert narratives (traders execute); Python quant/backtesting (pandas, NumPy, backtrader, statsmodels). ⚠️ Disclosure plan required for bank roles.
- **Crypto & key-management infrastructure** — knowledge/exposure only, **not production**: HSM, MPC/TSS, TEE/confidential compute, PKI, post-quantum migration awareness. Only for digital-asset custody / key-management JDs; keep the qualifier.

---

## 6. Achievement Library (STAR cards — interview-ready)

| # | Achievement | Situation / Problem | Action (Wilson's role) | Result / Evidence | Tags | Status |
|---|---|---|---|---|---|---|
| A1 | CBPR+ ISO 20022 migration | MT→MX migration under SWIFT/regulatory timelines on a live mission-critical payment platform | Planned and architected phased Blue/Green-style coexistence (coexistence → MX-rich), parallel traffic, cutover readiness; owned delivery E2E | No service interruption; reduced technical debt | AR DM GV | ✅ |
| A2 | Payment platform resilience | Real-time payments must stay available inside cut-off windows | DR/failover strategy; personally led drills; capacity baselines; Splunk monitoring; SRE SLIs/SLOs | 99.9%+ availability, transaction integrity under peak load; MTTR reduced | AR TL GV | ✅ (MTTR figure ❓) |
| A3 | AI Code Review Service | Team growth → review bottleneck; seniors on repeat reviews; inconsistent quality | Designed and built: Spring Boot orchestrates headless Claude Code via ProcessBuilder; three-dot diff; Bitbucket/GitHub; SonarQube on every PR; four dimensions (security, performance, correctness, maintainability); prompt A/B testing; AgentOps/LLMOps; MAS FEAT; AI never approves/merges | Review efficiency ~80% higher; new-joiner ramp-up 30–40% faster (internal measures); senior-management briefing (13-slide deck) | HC AR TL GV | ✅ (metric definition ❓Q10) |
| A4 | Payment-service performance | Latency under high load | Thread-pool tuning, less synchronous blocking, JVM tuning; core concurrency-control code | Reduced end-to-end latency | HC AR | ✅ (no figure) |
| A5 | Engineering excellence system | Need for measurable, governed delivery | Delivery KPIs (DORA-style), CI/CD release governance, DevOps model, 99% coverage gate, regression + pen testing in pipeline | Audit-ready releases; SIT/UAT sign-off on all releases | TL DM GV | ✅ |
| A6 | C360 / SCV-CCD | Regional need for a single customer view across channels | Led backend team; Cloudera evaluation; 360° data models; APIs | Served Wealth cross-sell and client management across multiple business lines | AR DM PL | ✅ |
| A7 | eMemo/quotation AI validation | Manual cross-document reconciliation in operations | Built agent that auto-generates validation prompts for schema and relationship checks | Recurring manual task removed | HC AR | ✅ |
| A8 | Golden Bridge 0-to-1 SaaS | New multi-tenant platform needed fast | Architecture (Spring Cloud, K8s, API gateway); Agile from scratch; budget | Live for users in 200+ regions | AR DM PL CV | ✅ |
| A9 | VV-Life 0-to-1 + real-time data | Data-driven local-life platform | Led technical centre; microservices; Flink ad-order and causal-inference profiling; MLOps | Platform launched; reduced critical incidents; lower cloud cost | AR HC PL CV | ✅ (cost figure ❓) |
| A10 | AI Park city rollout | Win and deliver city smart-parking projects | Headed tech dept; led bids; high-concurrency architecture; big-data team | 4+ city bids won; 1,000+ lots; 3 pilots | PL CV AR DM | ✅ |
| A11 | Security & data-migration controls | Sensitive payment/customer data under MAS TRM | Led API encryption, DB encryption, credential management, data migration — repeated across UOB, Golden Bridge, VV, AI Park | Controls in production across four employers | GV AR | ✅ |
| A12 | AI-assisted delivery-risk forecasting | Programme predictability | Forecasting from historical sprint data | "Improved predictability" | DM | 🔶 (method/outcome ❓Q10) |

---

## 7. Metrics Bank (must match between resume and interview)

| Metric | Attribution | Status |
|---|---|---|
| 18+ years | Total career (2008 –) | ✅ |
| ~4 years at UOB | Oct 2022 – present | ✅ (soft gap vs 6+ yr banking JDs) |
| 20+ engineers, 2 platform lines | UOB, via squad leads and EMs | ✅ — do not inflate |
| millions of accounts | UOB two lines | ✅ |
| 99.9%+ availability | UOB payment platforms | ✅ |
| no service interruption | ISO 20022 phased cutover | ✅ |
| ~80% review efficiency / 30–40% faster onboarding | AI Code Review, internal measures | ✅ (definition ❓) |
| 99% SonarQube coverage gate | UOB and VV | ✅ |
| 5+ years offshore management | Career | ✅ |
| 200+ regions | Golden Bridge SaaS users | ✅ |
| 1,000+ lots · 4+ city bids · 3 pilots | AI Park | ✅ |
| **100+ person technology organisation** | **Unattributed** | ❓ Q2 |
| **10M+ DAU / multi-million daily transactions** | **Unattributed** ("payments, marketplaces, SaaS") | ❓ Q3 |
| **10+ interconnected payment domains** | UOB — originated in Stripe-tailored version | ❓ Q4 |

---

## 8. Skills Inventory with Evidence Anchors

**Evidence-backed (appears in an experience bullet)** ✅
- **Languages/frameworks:** Java (deep, JVM tuning) · Spring Boot / Spring Cloud · Apache Camel (UOB production) · Python (Pureland quant; agentic tooling) · React (hands-on front-end) · Swift, Kotlin (working familiarity only)
- **Architecture:** microservices · API gateway · event-driven patterns · multi-tenant SaaS · high-concurrency distributed systems
- **Data:** Flink · Spark Streaming / Spark SQL · Hadoop · HBase · MapReduce · MongoDB · Cloudera · ETL
- **Cloud/DevOps:** AWS (CloudWatch, S3 and general cloud-native) · Kubernetes · Docker · Bitbucket · Jenkins · SonarQube · Aldon · JUnit
- **Observability/BI:** Splunk · Power BI · Tableau
- **AI:** headless Claude Code agents · prompt engineering & A/B evaluation · AgentOps/LLMOps · Responsible AI (MAS FEAT) · MLOps (recommendation)
- **Payments:** ISO 20022 (MT→MX) · CBPR+ · RTGS · TT · SWIFT · pain.002 · payment initiation/validation/enrichment · CASA integration
- **Governance:** MAS TRM · secure SDLC · DPIA · pen testing in CI/CD
- **Delivery tools:** Jira · Confluence · MS Project

**Skills-list only — no anchoring bullet yet** ❓ Q9
Kafka · Dubbo · ActiveMQ · Netty · SOA · Redis · Elasticsearch · DynamoDB · RDS · API Gateway (AWS) · Route 53 · Amazon MQ · Alibaba Cloud · Azure (exposure) · Informatica · Liquibase · Hibernate · Spring Batch · Spring AI · LangChain · RAG · vector databases · Node.js · Oracle / MySQL / PL-SQL · RHEL · GitLab · Maven · PCI-DSS / ISO 27001 (working knowledge of control objectives only) · IaC (exposure)
> Rule: an un-anchored skill may appear in a Skills line, but must not be claimed in a Summary or bullet until its "where/when/what" is confirmed.

**Never claim:** TOGAF · ITIL · service mesh (Istio/Envoy) · GCP depth · Go/Rust · core banking (Temenos, Finacle) · Murex · kdb+/q · large-scale model training / GPU inference infra · OKR ownership · consumer growth metrics (GMV, retention, conversion) · native mobile leadership · quantified hiring numbers.

---

## 9. Known Gaps & Honest Handling (consolidated)

| Gap | Handling |
|---|---|
| Banking tenure ~4 yrs vs 6–10 yr asks | Tier-1 regulated depth + payments specialism + 18+ yrs total |
| Current team 20+ vs 50–200 asks | "Leader of leaders" structure; historic 100+ org (once Q2 is resolved) |
| No TOGAF / architecture certification | "Designed AND delivered in a Tier-1 regulated bank"; architecture-review governance contribution |
| No cloud certification | Hands-on AWS production delivery; open to certifying |
| PMP not yet held | "PMP — in progress" |
| No ITIL | Show SLA, incident, RCA and service-KPI practice |
| Internet tenure ended 2022 | Lead with 0-to-1 builds + production AI built inside the bank |
| Treasury / FX / Murex / wealth core | Not his domain; bridge only when adjacent |
| Deep ML research | Position AI as applied delivery; the shipped production service is the proof |

**Fast-reject signals:** C#/.NET primary stack · kdb+/q · Murex / Treasury-FX core · equity OMS core · manufacturing (AGV/AMR/FlexSim) · mandatory Azure/Databricks CDAO track · finance/CFO-domain AI · "cross-border" logistics (false-friend keyword) · SAS + public-sector policy-authorship scope · GPU/model-inference infrastructure as a core requirement.

---

## 10. Source Library → Role Map

| Library | Target roles | Lead with |
|---|---|---|
| Senior_Tech_Bank | Bank CTO / Head of Technology / Head of Engineering / AppDev Manager / VP Tech Lead | Executive scope, leader of leaders, payments modernisation, governance |
| Senior_Tech_Internet | Scale-up CTO / VP Eng / fintech Head of Tech / platform & dev-productivity lead | 0-to-1, scale, org building, engineering culture, AI dev productivity |
| Archi_Bank | Solutions / Payments / Domain Architect, Principal Engineer (bank) | Payment-initiation hub, hands-on build, resilience, security |
| Archi_Internet | Principal / Platform / Data & AI Architect, Staff Engineer | High concurrency, streaming, multi-tenant SaaS, hands-on depth |
| TPM_Bank | TDM / IT Programme Manager / Service Delivery Lead / AI Delivery Manager (bank) | Programme scale, regulated migration, production ownership, vendor control |
| TPM_Internet | Senior TPM / TPM Lead / Payments TPM / AI Program Manager | Multi-team execution, data-driven delivery, launch quality |

**Tailored-resume constraints:** ≤ 3 pages; Summary ≈ page 1; merge/condense, no stacked repeats; red-font (FF0000) markup for changes; file naming `wilson-2026_[family]_[Target]_V[x]_[y]_[z].docx`.

---

## 11. Inconsistencies Found Across the 6 Sources

| # | Issue | Where | Recommendation |
|---|---|---|---|
| I1 | "Prior CTO … Chief Architect" in Summaries/headlines, but no CTO or Chief Architect title appears in the timeline | Senior_Tech_*, Archi_*, TPM_Bank | ❓ Q1 — high risk at background check |
| I2 | Standards: "contributed to bank-wide…" (Bank) vs "set … standards adopted company-wide" (Senior_Tech_Internet highlight) and "adopted company-wide" (Archi_Internet highlight) | Internet variants | Lock to "contributed to", matching your earlier confirmation |
| I3 | VV GenAI chatbot claims 2023-era terms (LLM function calling) for 2019–2020 work | All 6 | ❓ Q5 — reword |
| I4 | 100+ org and 10M+ DAU unattributed, yet read as personal achievements | All 6 | ❓ Q2, Q3 |
| I5 | Lending: "Own the technology" (Bank) vs "Architecture oversight" (Archi_Internet) | Archi_Internet | Both defensible; keep "own" as master wording |
| I6 | "Materially improving scalability…" without a metric | Senior_Tech_Bank, Senior_Tech_Internet | Drop "materially" unless a metric is supplied |

---

## 12. Confidentiality Guardrails (Rule 12)
- No customer names, volumes, internal ticket numbers, architecture diagrams or vendor commercial terms from UOB in any resume.
- Internal system names (CEW, SCV-CCD) — prefer descriptive wording in external resumes unless publicly known.
- AI Code Review metrics are labelled "internal measures"; do not cite internal job references (e.g. JR numbers).

---

## 13. Confirmation Queue (open)

**Priority 1 — blocks interview defensibility**
- **Q1** CTO / Chief Architect: which employer and period held these titles (formal or de facto)? If none was formal, change to "CTO-level scope" or drop.
- **Q2** 100+ person organisation: which company and period? Was it direct + indirect headcount?
- **Q3** 10M+ DAU / multi-million daily transactions: which platform(s) — Renren-Mall, Sohu News, Baidu Nuomi, VV? Were you directly responsible?
- **Q4** "10+ interconnected payment domains": what are the domains and the real count?
- **Q5** VV chatbot (2019–2020): what was actually built (e.g. Transformer/BERT-based intent + retrieval over a knowledge base, API calls to business services)? I will reword without "LLM function calling".

**Priority 2 — positioning**
- **Q6** Confirm the locked verb "contributed to" for bank-wide standards.
- **Q7** UOB hands-on coding: which modules and in which period did you personally write core code at VP2 level? (Defensible ratio of coding vs leading.)
- **Q8** Golden Bridge "gaming platform": casual/social gaming or iGaming/real-money? This affects wording for bank and regulated-employer applications.

**Priority 3 — strengthening**
- **Q9** For the un-anchored skills (§8), which did you use in production, where?
- **Q10** Missing numbers: latency reduction (%/ms), MTTR improvement, cloud-cost saving (%), definition of "~80% review efficiency", delivery-risk forecasting method and outcome.
- **Q11** Timeline gaps 2015 → Apr 2016 and Jul → Oct 2022: one-line explanations.
- **Q12** Should the Big Data AI library (`BD_V3_0_0`) be ingested into this master profile?

---

## 14. Change Log
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-15 | Initial master profile built from 6 V5_0_0_1 libraries; deduplicated union of bullets; added status and capability tags, STAR achievement library, evidence-anchored skills inventory, inconsistency register and confirmation queue. |
