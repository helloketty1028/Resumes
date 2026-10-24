# Wilson Zhang — Project Achievement Library

**Version:** v2.1-DRAFT · 2026-10-15 · **PENDING REVIEW — Batch 1 answers applied**
Source codes, status icons and capability tags are defined in `master-career-profile.md` §0.
Each card follows one template: **Context · Architecture & tech · Role & ownership · Challenges · Actions & decisions · Outcomes · Verified metrics · Relevance · Open points.**

**Ownership scale** (rule 3):
**O1** personally built/coded · **O2** designed and led the build · **O3** owned delivery/programme · **O4** governed/oversaw through managers · **O5** contributed/participated

---

## Project Inventory

| ID | Project | Employer | Period | Ownership | Tags | Status |
|---|---|---|---|---|---|---|
| PA-01 | CBPR+ / ISO 20022 MT→MX migration (payment-initiation hub) | UOB | 2022– | O2 + O3 | AR DM GV HC | ✅ |
| PA-02 | Payment-platform resilience, DR and observability | UOB | 2022– | O2 | AR TL GV | ✅ (no MTTR figure) |
| PA-03 | Delivery governance and quality engineering system | UOB | 2022– | O3 + O4 | TL DM GV | ✅ |
| PA-04 | Retail unsecured lending servicing and collections | UOB | 2022– | O3 + O4 | AR DM GV | ✅ |
| PA-05 | C360 regional customer-360 platform (SCV-CCD) | UOB | ❓ | O2 + team lead | AR DM PL | ✅ (dates ❓) |
| PA-06 | VN eTax certificate generation | UOB | ❓ | Team lead | DM PL | ✅ (dates ❓) |
| PA-07 | AI Code Review Service | UOB | ❓ | O1 + O2 | HC AR TL GV | ✅ |
| PA-08 | AI validation of eMemo and quotation documents | UOB | ❓ | O1/O2 ❓ | HC AR | ✅ |
| PA-09 | AI-assisted delivery-risk forecasting | UOB | ❓ | ❓ | DM | 🔶 |
| PA-10 | Multi-tenant online-game business SaaS (KYC, Bonus, AnA, VIP, Payment) | GBD | 2020–22 | O2 + O3, O1 ❓ | AR DM PL HC | ✅ (business nature ❓) |
| PA-11 | VV-Life local-life platform, incl. payment subsystem | VV | 2019–20 | O2 + PL | AR PL DM CV | ✅ |
| PA-12 | VV big-data and real-time analytics platform | VV | 2019–20 | O2 | AR HC | ⚠️ Flink vs Spark |
| PA-13 | GMS group management tool (B2B online office, SEA) | VV | 2019–20 | O2 + O4 | AR CV DM | ✅ [R22] only |
| PA-14 | Customer chatbot | VV | 2019–20 | ❓ | AR | ❓ Anachronism |
| PA-15 | 有声青蛙 audio-content platform (own start-up) | Hengshunyuan | 2017/18–19 | O1 + O2 + co-founder | HC AR DM CV | ⚠️ Dates; cloud provider |
| PA-16 | AI Park smart-parking platform and city rollout | AI Park | 2016–17 | O2 + PL + CV | AR PL CV DM | ⚠️ Pilot dates; 1,000+ lots attribution |
| PA-17 | Baidu Nuomi merchant-side parallel order system | Baidu | 2014 | O2 + project lead | AR HC TL PL DM | ✅ (QPS claim ❓) |
| PA-18 | Sohu CMS v5, OpenAPI messaging platform, SEO | Sohu | 2012–14 | O1 + O2 | HC AR TL | ✅ |
| PA-19 | Renren shopping site, Renren Mall, CRM | Renren | 2008–12 | O1 | HC | ✅ |
| PA-20 | Wealth/quant platform (selective module) | Pureland | 2020– | Advisory ❓ | AR HC | ❓ Disclosure |
| PA-21 | Personal: CamelAcademy and "CAMEL 问答闯关" Android apps | Personal | ❓ | O1 | HC | ❓ Resume use? |
| — | Crypto and key-management infrastructure | — | — | **Knowledge only, not production** | — | Selective fragment |

---

## UOB (Oct 2022 – Present)

### PA-01 · CBPR+ / ISO 20022 MT→MX Migration — Payment-Initiation Hub ✅
- **Context:** A live, mission-critical cross-border payment platform (TT, RTGS) migrating from SWIFT MT to ISO 20022 MX under CBPR+ and regulatory timelines. Scope ran through the coexistence and MX-rich stages, including authorisation procedures (group, account, product) and channel administration.
- **Architecture & tech:** The payment-initiation hub (internal name CEW) takes requests from Internet Banking and branch channels. It uses FX-rate, account and customer reference data; performs validation, enrichment and pain.002 status tracking; and hands off to downstream systems (SWIFT ISO 20022 flow, CASA). Downstream processing and settlement sit in other systems. Built with Java, Spring Boot, Apache Camel and event-driven integration.
- **Role & ownership:** O2 + O3. Led end-to-end system design (API contracts, orchestration, validation, enrichment, status tracking). Owned programme delivery end to end. **Personally wrote core transaction-processing and concurrency-control modules** [LIB] (scope ❓OQ-2.1).
- **Challenges:** Zero tolerance for downtime inside payment cut-off windows. MT/MX coexistence. Many upstream, downstream, vendor and third-party dependencies. Regulatory deadlines.
- **Actions & decisions:**
  - Chose a phased, Blue/Green-style coexistence deployment (parallel traffic management, cutover readiness).
  - Tuned thread pools, reduced synchronous blocking and tuned the JVM to cut end-to-end latency.
  - Designed security controls: API-call encryption/decryption, DB encryption of sensitive data, dedicated credential-file management.
  - Led payment data migration under MAS TRM.
  - Ran Agile governance (sprints, RAID, change control, Jira/Confluence) with executive reporting; coordinated vendors and SLAs.
- **Outcomes:** Cutover with **no service interruption**. Reduced technical debt. Improved scalability, resilience and stability (qualitative).
- **Verified metrics:** "No service interruption" ✅. Latency reduction: no figure ❓.
- **Relevance:** Payments/Solutions Architect · Bank TDM/Programme Manager · Head of Payments Technology · Payments TPM (fintech)
- **Open points:** OQ-2.1 coding share · OQ-2.4 "10+ payment domains" · OQ-3.1 latency figure.

### PA-02 · Payment-Platform Resilience, DR and Observability ✅
- **Context:** Real-time payment middleware must stay available and keep transaction integrity under peak load.
- **Architecture & tech:** Splunk observability and alerting pipeline; SRE practice (SLIs/SLOs, toil reduction, incident management); DR/failover design; capacity baselines.
- **Role & ownership:** O2. **Personally led DR and failover drills** [CONF]. Led incident response and RCA.
- **Actions & decisions:** Defined the DR strategy, failover procedures and capacity-planning baselines. Built the real-time transaction-monitoring pipeline. Coordinated high-severity incidents end to end (investigation, stakeholder communication, workaround tracking, permanent fix) with SLA tracking.
- **Outcomes:** **99.9%+ availability** and transaction integrity under peak load; MTTR reduced (no figure).
- **Verified metrics:** 99.9%+ ✅ · MTTR delta ❓OQ-3.1
- **Relevance:** SRE/Platform lead · Head of Engineering · Service Delivery Manager · Architect

### PA-03 · Delivery Governance and Quality-Engineering System ✅
- **Context:** Releases had to be measurable, governed and audit-ready under MAS TRM.
- **Architecture & tech:** Bitbucket, Jenkins, SonarQube, Aldon, JUnit; automated regression and penetration testing in CI/CD; Jira/Confluence.
- **Role & ownership:** O3 + O4 (governance through squad leads).
- **Actions & decisions:** Set delivery KPIs (deployment frequency, MTTR, incident trend, change-failure rate) and a 99% SonarQube coverage gate. Required SIT/UAT sign-off on all releases. Ran secure SDLC, DPIA and data governance. **Contributed to** bank-wide SDLC, coding, code-review and architecture-review standards [CONF] (locked verb).
- **Outcomes:** Audit-ready releases; SIT/UAT sign-off on all releases.
- **Verified metrics:** 99% coverage gate ✅
- **Relevance:** Engineering Manager · Head of AppDev · TDM · DevOps/Engineering-excellence lead

### PA-04 · Retail Unsecured Lending Servicing and Collections ✅
- **Context:** The second platform line. Covers payment initiation, validation and lifecycle tracking for retail unsecured lending, plus post-disbursement collections across credit-card and unsecured-loan portfolios. Collections uses account and balance data from the card account system.
- **Role & ownership:** O3 + O4 ("own the technology") [CONF]. Led data migration and data-protection controls.
- **Outcomes:** No metrics on record ❓
- **Relevance:** Lending/consumer-banking tech lead · Head of Technology (retail bank)
- **Open points:** OQ-3.2 any outcome (collection-cycle time, automation, incident reduction)?

### PA-05 · C360 Regional Customer-360 Platform (SCV-CCD) ✅
- **Context:** The region needed a single customer view across channels for Wealth cross-sell and client management.
- **Architecture & tech:** Cloudera evaluated as the data-processing framework. 360° data models (transactions, accounts, balances) with KYC-relevant data handling. APIs consumed by several business lines. Waterfall governance.
- **Role & ownership:** Led the SCV-CCD backend team; designed and optimised the data models; led data migration.
- **Outcomes:** APIs in use across multiple business lines.
- **Relevance:** Data/Platform Architect · Customer-data platform lead · Big Data AI family
- **Open points:** OQ-3.3 dates, team size, number of countries/business lines.

### PA-06 · VN eTax ✅
- **Context:** Tax-certificate generation for completed transactions, enabling 24/7 tax payments (Vietnam).
- **Role & ownership:** Led the backend team.
- **Open points:** OQ-3.3 dates, scale, outcome.

### PA-07 · AI Code Review Service ✅ (strongest differentiator)
- **Context:** As the team grew, code review became a bottleneck. Senior engineers spent time on repeat reviews, and review quality was inconsistent.
- **Architecture & tech:** A Spring Boot service orchestrates headless Claude Code via ProcessBuilder. Uses three-dot diffs; integrates with Bitbucket/GitHub; runs SonarQube on every PR. Reviews on four dimensions: security, performance, correctness, maintainability. Prompt A/B testing; AgentOps/LLMOps practice; Responsible AI aligned with MAS FEAT.
- **Role & ownership:** **O1 + O2 — designed and built it; in production** [CONF].
- **Key decision:** Governance rule — **the AI never approves or merges; human reviewers decide.**
- **Outcomes:** Review efficiency up ~80%; new-joiner ramp-up 30–40% faster (internal measures). Briefed senior management with a 13-slide deck.
- **Verified metrics:** ✅ [CONF]. Measurement method ❓OQ-3.1
- **Relevance:** Head of Engineering · Developer-productivity/Platform lead · AI Delivery/Programme Manager · Head of AI Projects · Architect
- **Note:** Removed from Big Data variants by an earlier editorial lock [CONF].

### PA-08 · AI Validation of eMemo and Quotation Documents ✅
- **Context:** Operations reconciled eMemo and quotation documents by hand on a recurring basis.
- **Tech:** An AI agent auto-generates validation prompts to check schema alignment and data-relationship consistency between the documents.
- **Role & ownership:** Built [LIB] (O1/O2 ❓).
- **Outcomes:** Removed a recurring manual reconciliation task. Volume/time saved ❓OQ-3.1

### PA-09 · AI-Assisted Delivery-Risk Forecasting 🔶
- **Claim [LIB]:** Forecasting from historical sprint data improved programme predictability.
- **Open points:** OQ-3.1 — method (tool/model), who built it, and a measurable outcome. **Do not use in resumes until answered.**

---

## Golden Bridge Drive (Nov 2020 – Jul 2022)

### PA-10 · Multi-Tenant Online-Game Business SaaS (KYC · Bonus · AnA · VIP · Payment) ✅ / ❓ business nature
- **Context:** A customisable, multi-tenant public platform for online-game businesses, built 0 to 1. Services: event operations management, bonus incentives, VIP user upgrade, KYC and multi-channel payments [R22].
- **Architecture & tech [R22]:** JDK 11, Spring Cloud, Kubernetes, Elasticsearch, code standards. AWS: Route 53, API Gateway, EC2/ECS, SQS/SNS, S3, RDS, load balancing, Cognito, DynamoDB, ElastiCache, Lambda, CloudWatch, IAM. CI on Jenkins + Amazon ECR. [LIB] adds Power BI/Splunk reporting, DPIA and encryption controls.
- **Role & ownership:** O2 + O3. **Built a 40-person project team** [R22]. Designed the rules at each level of the authentication service. Designed bonus-activity management (eligibility, trigger conditions, distribution rules). Designed hierarchical KYC by benchmarking competitor apps. [R22] says "Implement the core modules: KYC, Bonus, AnA, Payment" — ❓ personally coded, or led the team that did? (OQ-2.2)
- **Challenges:** 0-to-1 under time pressure; multi-tenancy; KYC across many jurisdictions.
- **Actions & decisions:** Hybrid delivery (Waterfall for scope, budget and milestones; Agile sprints). Set up Agile/Scrum from scratch. Owned team capacity, delivery budget and launch readiness [LIB][CONF].
- **Outcomes:** Platform launched. KYC supports 200+ countries [R22].
- **Verified metrics:** 40-person team ✅[R22] · 200+ countries ⚠️ capability vs live users (CF-11)
- **Relevance:** Scale-up CTO/Head of Tech · Platform/Cloud Architect · fintech/payments SaaS
- **Open points:** OQ-1.9 casual/social vs real-money gaming · OQ-2.2 hands-on share.

---

## VV Technology (Apr 2019 – Jun 2020)

### PA-11 · VV-Life Local-Life Platform (0 to 1), incl. Payment Subsystem ✅
- **Context:** VV-Life aimed to "change life through data": connecting offline merchants through big data, AI and blockchain into a transparent local-life platform (food, fresh produce, travel, local services).
- **Architecture & tech [R22]:** CI/CD, Spring Cloud, Redis cluster, Kubernetes, Elasticsearch, AWS, code standards. [LIB] adds AWS CloudWatch, Splunk SLOs/alerting/dashboards, Tableau, Docker.
- **Role & ownership:** Head of Technical Development [CONF] ("Head of Technical Centre" in [R22][LIB] — FU-3). Built the organisation and technical framework from scratch; ran technology selection; took part in product-strategy planning. "I built the micro-service framework" [R22] (O1/O2).
- **Actions & decisions:** Built a **140-person technical team** [R22]. Implemented CI/CD. Delivered the first VV-Life version's closed loop in 2019, including the payment subsystem's **transaction, management and reconciliation** modules [R22]. [LIB] adds resilience engineering, 99% coverage, Kubernetes rollback, encryption/migration controls and AWS cost optimisation.
- **Outcomes:** VV-Life v1 launched (2019). Fewer critical incidents; lower cloud cost [LIB] (no figures).
- **Verified metrics:** 140 people ❓ (direct vs indirect) · "framework supporting 10M concurrent HTTP requests" ❓ **high risk** (OQ-2.3) · platform ~10M DAU [CONF] — measure ❓ FU-1
- **Relevance:** Head of Tech · Engineering org builder · Platform Architect · e-commerce/local services
- **Open points:** OQ-2.3 · FU-1.

### PA-12 · VV Big-Data and Real-Time Analytics Platform ⚠️
- **Context:** Data-driven profiling, recommendation and advertising analytics for VV-Life.
- **Architecture & tech — CONFLICT:**
  - [R22]: built the data-analysis platform from scratch with **Flume, Hive, MapReduce, Spark Streaming, Spark SQL, YARN, ETL**. **No Flink.**
  - [LIB]: **Flink-based** real-time/offline ad-order tracking system; Flink-based real-time customer profiling using causal inference; MLOps architecture for recommendation.
- **Role & ownership:** Led the big-data team [R22]; [LIB] says "built" (O1/O2 ❓).
- **Outcomes:** No metrics.
- **Relevance:** Big Data AI family · Data Platform Architect
- **Open points:** CF-07 — which stack was used, and were both used (e.g. Spark batch + Flink real-time)?

### PA-13 · GMS Group Management Tool ✅ [R22] — **new, not in v1.0**
- **Context:** An intelligent online-office product: a general-purpose B2B office tool covering Southeast Asia and other regions.
- **Architecture & tech:** Middle-platform design on Spring Boot, MySQL cluster, Redis, RocketMQ and AWS.
- **Role & ownership:** O2 + O4. Controlled solution soundness, cost evaluation, staffing structure and acceptance. Set the phased technical strategy. Designed the middle-platform architecture.
- **Outcomes:** Not stated ❓ (launched? number of client companies?)
- **Relevance:** SaaS/B2B Architect · Head of Tech

### PA-14 · VV Customer Chatbot ❓ (do not use)
- **Claim [LIB]:** "GenAI customer chatbot using self-attention models, RAG, LLM integration and function calling."
- **Problem:** [R22], written closer to the time, does not mention any chatbot. LLM function calling dates from 2023, and RAG was published in May 2020, a month before VV ended. Very likely to fail interview scrutiny.
- **Open point:** OQ-1.10 — what was actually built, if anything? It will be reworded or removed.

---

## Hengshunyuan (own start-up)

### PA-15 · 有声青蛙 — Vertical Audio-Content Platform ⚠️
- **Context:** A vertical platform for displaying and delivering audio content, focused on copyrighted workplace and early-childhood education content, with precise targeting of consumer users [R22].
- **Architecture & tech:**
  - [R22]: Spring Cloud, big data, MySQL cluster, Redis, Kafka, **Alibaba Cloud (aliyun)**, ELK, Rollbar.
  - [LIB]: "**AWS** cloud deployment". ⚠️ CF-08
- **Role & ownership:** **Co-founder** ✅ [CONF][R22]. Largely dormant from Apr 2019, when Wilson joined VV [CONF]. Responsible for all products, architecture and technical implementation; big-data architecture; from market research to production operations (O1 + O2).
- **Actions:** Licensed about **1,500 audio titles/albums** early on (business development). Introduced Spring Cloud microservices for extensibility.
- **Outcomes:** Peak **DAU about 100k**; single-node concurrency **above 1,500**. The company closed after fundraising failed [R22].
- **Relevance:** Founder/0-to-1 evidence · consumer/media platforms · CTO-level scope
- **Open points:** CF-05 dates (FU-5) · CF-08 cloud provider · team size.

---

## AI Park

### PA-16 · Smart-Parking IoT Platform and City Rollout ⚠️
- **Context:** Combined parking-lot and user scenarios to connect different types of car parks automatically to the cloud: automatic management, online charging, precise recommendations.
- **Architecture & tech [R22]:** Data analysis, Go ❓, Spark Core, HBase, ELK, IoT, Spring Cloud, SaaS, Ruxit, Kafka, security defence, Kubernetes. [LIB] adds MongoDB, MapReduce, Spark Streaming, ETL and encryption/migration controls.
- **Role & ownership:** VP of Technical Development [CONF] (PL + AR + CV). Led the big-data team [LIB].
- **Actions & decisions:**
  - Coordinated city bids and won Shijiazhuang, Handan, Beijing and other cities [R22] (CF-10: 3+ vs 4+).
  - Added an AI processing step to licence-plate and portrait recognition to improve speed and accuracy [R22] — **new, not in v1.0**.
  - Introduced a SaaS model for future B2B/B2G customers [R22].
- **Outcomes:** Running in 1,000+ public car parks in the target cities ❓ (during or after your tenure?). Pilots: Shijiazhuang 2016, Handan 2017, Beijing Chaoyang 2017 [CONF]. [R22] said 2017/2018/2019 — already corrected by you.
- **Relevance:** IoT/smart-city · Head of Tech · B2G bidding · big data
- **Open points:** CF-06 start month · CF-09 Go · OQ-3.4 1,000+ attribution and team size · FU-1: platform ~10M DAU [CONF] — define the measure.

---

## Early Career (China internet)

### PA-17 · Baidu Nuomi Merchant-Side Parallel Order System ✅ (metric ❓)
- **Context:** The group-buy information-publishing and management system: merchant contracts, Nuomi group orders, coupons. [R22] calls it the "core of core" at Baidu Nuomi.
- **Architecture & tech:** Dubbo microservices, Resin front-end proxy, MongoDB, Redis, ZooKeeper, GitLab, Gradle, Angular, Solr, data security.
- **Role & ownership:** **Project leader.** Re-structured the technical architecture after taking over. Led the web front-end, CMS development team and QA. Worked with product on requirements; controlled project and testing progress.
- **Outcomes:** **Delivered two months ahead of plan.** Improved fault tolerance. The system became central to Nuomi's merchant side.
- **Metrics:** "Serves 5–10 million QPS" ❓ **high risk** — implausible for a merchant-side system (OQ-2.3).
- **Relevance:** Early leadership evidence · e-commerce · distributed systems.

### PA-18 · Sohu CMS v5, OpenAPI Messaging Platform, Website SEO ✅
- **Architecture & tech:** Spring MVC, Dubbo, DNS, DevOps, MongoDB, Redis, Solr, MySQL, NFS, SLB, Nginx, shell.
- **Role & ownership:** Technical Leader / Project Leader (O1 + O2).
- **Actions:** Upgraded the CMS architecture: replaced SSH with Spring Web, and the memcache cluster with a Redis cluster.
- **Relevance:** Media/content platforms · hands-on depth

### PA-19 · Renren Shopping Website, Renren Mall, CRM ✅
- **Tech:** Spring, Solr, Redis, MySQL, Nginx, Angular, shell.
- **Role & ownership:** Senior R&D Engineer (O1).
- **Open points:** OQ-3.6 advertising team?

---

## Selective and Personal

### PA-20 · Pureland Holding — Wealth/Quant Platform ❓
[LIB]: VWAP execution, portfolio management, risk analytics on Spark/Hadoop; Spring services on AWS; S3 tick data; Spark Streaming + Spark SQL; Bloomberg and Yahoo Finance data. A Claude agent compares daily trading patterns with 10-day and 6-month baselines to produce risk-scored recommendations and alert narratives (traders execute). Python quant/backtesting (pandas, NumPy, backtrader, statsmodels). **Disclosure plan needed for bank roles** (OQ-1.8).

### PA-21 · Personal Android Apps ❓
Stated earlier [CONF]: **CamelAcademy** (an Apache Camel learning game, Kotlin/Jetpack Compose, nine levels + boss stage) and **"CAMEL 问答闯关"** (a multi-agent AI quiz on the Anthropic Messages API), published on Google Play. Evidence for Kotlin and LLM-API hands-on work. ❓ Include in the resume library? (OQ-3.7)

---

## Role-Relevance Map (where each project earns its place)

| Target family | Lead projects | Supporting |
|---|---|---|
| Senior Tech / Head of Tech (bank) | PA-01, PA-03, PA-07, PA-04 | PA-02, PA-05 |
| Senior Tech / Head of Tech (fintech/internet) | PA-07, PA-10, PA-11, PA-15 | PA-16, PA-17 |
| Architect (bank) | PA-01, PA-02, PA-05 | PA-07 |
| Architect (internet/platform/data) | PA-10, PA-11, PA-12, PA-07 | PA-13, PA-16 |
| TPM / TDM / Programme | PA-01, PA-03, PA-02 | PA-10, PA-16 |
| Big Data / AI delivery | PA-05, PA-12, PA-07, PA-08 | PA-16, PA-20 |
