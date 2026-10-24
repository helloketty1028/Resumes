# Wilson Zhang — Technical Skills Inventory

**Version:** v2.2 · 2026-10-16 · **Auxiliary file** (maintained independently [CONF 2026-10-16]) · PA-Q1 and 2026-10-16 confirmations applied
Source codes and status icons: see `01_Resume_Master_Rules.md` §3. Usage in resumes: 01 §9 and 05 §5.

**Depth levels**
- **P** — production use, hands-on (you wrote, configured or operated it)
- **A** — architected or led (you chose it and directed the team; your own coding not established)
- **F** — familiar / working knowledge
- **X** — exposure only, never in production

**Usage rule:** A skill may appear in a resume Skills line once it has an evidence anchor (employer + period). It may appear in a Summary or bullet only at depth P or A. Items marked ❓ stay out of resumes until confirmed.

> **Big change from v1.0:** The 2022 resume anchors many skills that v1.0 listed as "skills-list only" (DynamoDB, RDS, API Gateway, Route 53, Redis, Elasticsearch, Dubbo, Kafka, Alibaba Cloud, MySQL, GitLab, MongoDB …). Depth (P vs A) still needs your confirmation for the 2016–2022 head-of-technology roles.

---

## 1. Languages

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| Java (JVM tuning, concurrency) | UOB payment services; GBD (JDK 11); every role 2008– | P | [R22][LIB] | ✅ |
| Python | Pureland quant/backtesting; agentic tooling | P | [LIB][CONF] | ✅ |
| Shell | Sohu, Renren | P | [R22] | ✅ |
| JavaScript — React | Hands-on front-end | P | [CONF] | ✅ (employer ❓) |
| JavaScript — Angular | Baidu Nuomi, Renren | P/A ❓ | [R22] | ❓ |
| Node.js | Summary skill only, no project | F | [R22][LIB] | ❓ |
| Kotlin / Jetpack Compose | Personal Android apps (CamelAcademy) | P (personal) | [CONF] | ✅ — label "personal projects" |
| Swift | Working familiarity | F | [CONF] | ✅ |
| **Go** | AI Park tech list | ❓ | [R22] | ⚠️ **CF-09** — v1.0 says never claim Go |

## 2. Frameworks and Middleware

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| Spring Boot | UOB; GMS (VV) | P | [LIB][R22] | ✅ |
| Spring Cloud | GBD, VV, Hengshunyuan, AI Park | A/P ❓ | [R22][LIB] | ✅ anchor; depth ❓ |
| Spring MVC / Spring Web | Sohu CMS (replaced SSH) | P | [R22] | ✅ |
| Apache Camel | UOB production | P | [CONF] | ✅ |
| Dubbo | Baidu Nuomi (introduced it), Sohu CMS | P/A | [R22] | ✅ — **moved from un-anchored** |
| ZooKeeper | Baidu Nuomi | P | [R22] | ✅ |
| Resin | Baidu Nuomi (front-end proxy) | P | [R22] | ✅ |
| Netty, ActiveMQ | Summary skill only | F | [R22][LIB] | ❓ no project anchor |
| SSH (Struts/Spring/Hibernate) | Sohu legacy stack (replaced) | P | [R22] | ✅ — Hibernate via SSH |
| Spring Batch | UOB CCD — scheduled-job processing module, personally built | P | [CONF 2026-10-16] | ✅ — **moved from un-anchored** |
| Spring AI, Liquibase | Skills line only | ❓ | [LIB] | ❓ |

## 3. Messaging and Streaming

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| Kafka | Hengshunyuan, AI Park, VV (asynchronous flows) | A/P ❓ | [R22][CONF 2026-10-16] | ✅ — **moved from un-anchored** |
| RocketMQ | VV GMS | A | [R22] | ✅ new |
| AWS SQS / SNS | GBD | A/P ❓ | [R22] | ✅ new |
| Amazon MQ | Skills line only | ❓ | [LIB] | ❓ |
| Flume | VV data platform | A | [R22] | ✅ new |
| Spark Streaming / Spark SQL / Spark Core | VV, AI Park, Pureland | A/P ❓ | [R22][LIB] | ✅ |
| **Flink** | VV ad-order tracking and real-time profiling | ❓ | [LIB] only | ⚠️ **CF-07** — absent from [R22] |

## 4. Data Stores and Search

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| MySQL (incl. clusters) | Renren, Sohu, Hengshunyuan, GMS | P | [R22] | ✅ — **moved from un-anchored** |
| SQL (general) | Proficient | P | [CONF 2026-10-16] | ✅ — employer anchor ❓ (assumed career-wide) |
| Oracle / PL-SQL | Skills line only | ❓ | [LIB] | ❓ (UOB?) |
| Redis (incl. cluster) | Renren, Sohu (memcache→Redis), Baidu, VV, Hengshunyuan, GMS | P | [R22] | ✅ — **moved from un-anchored** |
| AWS ElastiCache | GBD | A | [R22] | ✅ new |
| memcached | Sohu (replaced) | P | [R22] | ✅ |
| MongoDB | Sohu, Baidu, AI Park | P | [R22][LIB] | ✅ |
| HBase | AI Park | A/P | [R22][LIB] | ✅ |
| Hive, MapReduce, YARN, Hadoop | VV, AI Park, Pureland | A | [R22][LIB] | ✅ |
| Elasticsearch | GBD, VV | A/P | [R22] | ✅ — **moved from un-anchored** |
| Solr | Renren, Sohu, Baidu | P | [R22] | ✅ new |
| AWS DynamoDB / RDS | GBD | A | [R22] | ✅ — **moved from un-anchored** |
| AWS S3 | GBD, Pureland (tick data) | P/A | [R22][LIB] | ✅ |
| Cloudera | UOB C360 (evaluated as framework) | A | [LIB] | ✅ — "evaluated/selected", not operated ❓ |
| Vector databases | Skills line only | ❓ | [LIB] | ❓ |

## 5. Cloud, Containers, DevOps

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| AWS (general cloud-native) | GBD, VV, GMS, Pureland | A/P | [R22][LIB] | ✅ |
| AWS Route 53, API Gateway, EC2/ECS, Lambda, Cognito, IAM, ELB, CloudWatch, ECR | GBD (all); VV (CloudWatch) | A | [R22] | ✅ — **moved from un-anchored** |
| **Alibaba Cloud (aliyun)** | Hengshunyuan | A/P | [R22] | ✅ anchor · ⚠️ **CF-08** vs [LIB] "AWS" |
| Azure | Exposure | X | [LIB] | ✅ keep "exposure" |
| GCP | — | — | — | Never claim depth |
| Kubernetes | GBD, VV, AI Park | A | [R22][LIB] | ✅ |
| Docker | VV, career | A/P | [R22][LIB] | ✅ |
| Jenkins | UOB; GBD (Jenkins + ECR) | P/A | [R22][LIB] | ✅ |
| Bitbucket, SonarQube, Aldon, JUnit | UOB; VV (SonarQube 99%) | P/A | [LIB] | ✅ |
| GitLab, Gradle | Baidu | P | [R22] | ✅ — **moved from un-anchored** |
| Maven | Skills line only | ❓ | [LIB] | ❓ (very likely; confirm) |
| Nginx, SLB, NFS, DNS | Sohu, Renren | P | [R22] | ✅ new |
| RHEL (Linux) | Proficient [CONF 2026-10-16]; [TPL] lists "Linux (RHEL)" | P | [CONF][LIB] | ✅ — employer anchor ❓ |
| IaC | Exposure | X | [LIB] | ✅ keep "exposure" |
| CI/CD (DevOps model) | UOB, GBD, VV | A | [R22][LIB] | ✅ |

## 6. Observability and BI

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| Splunk | UOB (pipeline); GBD; VV | A/P | [LIB] | ✅ |
| ELK | Hengshunyuan, AI Park | A | [R22] | ✅ new |
| Rollbar | Hengshunyuan | A | [R22] | ✅ new |
| Ruxit (Dynatrace APM) | AI Park | A | [R22] | ✅ new |
| Power BI | GBD | F/P | [LIB] | ✅ |
| Tableau | VV | F/P | [LIB] | ✅ |

## 7. Architecture Patterns

Microservices (Dubbo era → Spring Cloud → Spring Boot/Camel) ✅ · API gateway ✅ · event-driven integration ✅ · multi-tenant SaaS ✅ (GBD, AI Park SaaS model) · high-concurrency distributed systems ✅ · middle-platform design (GMS) ✅ · Blue/Green coexistence deployment ✅ · DR/failover design ✅ · SOA ❓ (skills line only)

## 8. Data, ML and AI

| Skill | Evidence anchor | Depth | Source | Status |
|---|---|---|---|---|
| Data warehouse / ETL | VV, AI Park | A | [R22][LIB] | ✅ |
| User profiling, recommendation, risk-control platforms | Career summary; VV | A | [R22][LIB] | 🔶 per-platform anchors partial |
| Causal inference (profiling) | VV | ❓ | [LIB] | ❓ tied to CF-07 |
| MLOps (recommendation) | VV | A | [LIB] | 🔶 |
| Computer-vision pipeline integration (licence-plate/portrait recognition) | AI Park | A | [R22] | ✅ new — "added AI processing step"; not model training |
| Headless Claude Code agents; Anthropic Messages API | UOB AI Code Review; personal apps; Pureland agent | P | [CONF][LIB] | ✅ |
| Prompt engineering, A/B evaluation; AgentOps/LLMOps | UOB | P | [CONF] | ✅ |
| LLM evaluation concepts (LLM-as-judge, trajectory eval, RAGAS) | Interview prep only | F | [CONF] | ✅ — **knowledge, not a production claim** |
| Responsible AI — MAS FEAT | UOB | P | [CONF] | ✅ |
| RAG, LangChain, vector DBs | Skills line only | ❓ | [LIB] | ❓ — where in production? |
| Quant libraries: pandas, NumPy, backtrader, statsmodels | Pureland / personal | P | [LIB][CONF] | ✅ |
| Large-scale model training / GPU inference infrastructure | — | — | — | Never claim |

## 9. Payments and Banking Domain

ISO 20022 (MT→MX) ✅ · CBPR+ ✅ · RTGS ✅ · TT ✅ · SWIFT ✅ · pain.002 ✅ · payment initiation/validation/enrichment/status tracking ✅ · CASA integration ✅ · retail unsecured lending servicing and collections ✅ · customer-360 / KYC-relevant data ✅ · KYC (hierarchical, multi-country) ✅ GBD · payment subsystem incl. **reconciliation** ✅ VV [R22] · online payment ✅ AI Park · VWAP / portfolio and risk analytics 🔶 Pureland (selective)
**Never claim:** core banking (Temenos, Finacle) · Murex · kdb+/q · Treasury/FX core · equity OMS core

## 10. Security, Risk and Governance

MAS TRM ✅ · secure SDLC ✅ · DPIA ✅ (UOB, GBD) · API-call encryption/decryption, DB encryption of sensitive data, credential-file management ✅ [CONF] (UOB, GBD, VV, AI Park) · penetration testing in CI/CD ✅ · "security defence" / network security ✅ AI Park, career [R22] (generic; specifics ❓) · PCI-DSS / ISO 27001 — working knowledge of control objectives only ✅ · infrastructure/security/compliance from founder roles — confirmed exists, specifics not yet given ❓ [CONF]

**Reliability practice [CONF 2026-10-16]:** completed formal SRE training (not a certification); UOB teams own production support with no separate SRE team (03 PA-02.3, X-06).

## 11. Delivery and Management Tooling

Jira ✅ · Confluence ✅ · MS Project ✅ [LIB] · Agile/Scrum ✅ (set up from scratch at GBD) · hybrid Waterfall/Agile ✅ · RAID / change control ✅ · DORA-style KPIs ✅

## 12. Never Claim (carried from v1.0 + [CONF])

TOGAF · ITIL · service mesh (Istio/Envoy) · GCP depth · Go/Rust (**unless CF-09 resolves otherwise**) · core banking · Murex · kdb+/q · large-scale model training · OKR ownership · consumer growth metrics (GMV, retention, conversion) · native mobile leadership · quantified hiring numbers (**note:** [R22] contains "built 40/140-person teams" — see OQ-2.3)

## 13. Change Log
| Version | Date | Change |
|---|---|---|
| v2.1-DRAFT | 2026-10-16 | PA-Q1 answers applied (Spring Batch, Kafka anchored). |
| v2.2 | 2026-10-16 | Kept as an auxiliary file. Icon reference → 01 §3. RHEL ❓→✅ P and new "SQL (general)" row per your confirmation; SRE-training note in §10. Nothing removed. |
