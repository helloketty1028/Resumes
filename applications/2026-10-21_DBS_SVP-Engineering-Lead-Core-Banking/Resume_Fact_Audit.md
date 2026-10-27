# Resume Fact & Quality Audit — 04

**File audited:** `wilson-2026_ATL_Bank_DBS_V1_0_0_draft.txt` (pdftotext of the rendered PDF), with `..._draft.pdf` (3 pages, A4) and `..._draft.report.md` / `.report.json`
**Family × lens:** ATL × BNK (from the file name; target DBS). The JD was not given to the auditor, so job fit is not assessed here.
**Auditor:** independent; drafting notes, cards, `JD_Matching_Analysis.md`, `Resume_Change_Log.md` and `resume.json` were **not** read.
**Date:** 2026-10-21

**Sources read (each once):**
| Source | Version |
|---|---|
| `01_Resume_Master_Rules.md` | v1.1 · 2026-10-20 |
| `02_Candidate_Profile.md` | v3.1 · 2026-10-17 |
| `03_Achievement_Library.md` | v4.1 · 2026-10-17 |
| `technical-skills-inventory.md` | v2.3 · 2026-10-17 |
| `fact-check-and-open-questions.md` | v2.4 · 2026-10-20 |
| `session confirmations S1–S9 (Batch_Triage.md §7)` | S1–S9, tagged `[CONF 2026-10-21]` |
| Rendered PDF | Pages rasterised at 70 dpi and inspected visually |

Not read: `04_Resume_Layout_Spec.md` and `05_JD_Keyword_and_Matching_Rules.md`, which are not inputs under the brief. Layout was checked against the brief's document checks and the render report.

---

## 1. Claim-by-claim audit

Checks: **D** dates · **T** titles · **S** scope · **V** ownership verb · **Te** technical depth · **N** numbers & qualifiers · **C** confidentiality. "✓" means checked with no issue.

### Header
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| H1 | "WILSON" | 02 §1 (D-11) | T ✓ | PASS | — |
| H2 | "Singapore PR \| +65 8655 9547 \| Skyzhang1028@gmail.com \| Singapore" | 02 §1 (PR since 2024, phone, email, location) | C ✓ | PASS | Cosmetic: "Singapore" appears twice. Optional: drop the trailing "\| Singapore". |
| H3 | "Hands-On Engineering Lead — Banking Transaction Platforms \| Payments, Lending & Customer Data · Platform Modernisation" | 01 §5 (a headline may name the target role); 02 §6.1; PA-01, PA-04, PA-05 | T ✓ (target-role headline, not a past title) | PASS | — |

### Professional Summary
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| S1 | "Engineering lead with 18+ years of software engineering experience, who leads teams while staying hands-on in architecture, solution design and code reviews." | 03 §0A (18+ years); X-04; S5 | N ✓ · V ✓ | PASS | — |
| S2 | "Since 2022, a Vice President in UOB's Group Technology & Operations, accountable for mission-critical payment and lending transaction platforms in a Tier-1, MAS-regulated bank." | 02 §2 row 1; 02 §6.1; PA-04 | D ✓ · T ✓ · S ✓ | PASS | — |
| S3 | "Leads 25 onshore and offshore engineers on platforms serving millions of accounts: a payment-initiation hub for cross-border payments and a customer-360 platform, both integrated with core banking, and the technology for retail lending servicing and collections." | 03 §0A (25, millions of accounts); X-02; S2; PA-04.1 | N ✓ · S ✓ · C ✓ (no CEW/CCD) | PASS | Consistent with X-02, which places the 25 across both platform lines. Which team covers lending is still open (C6), and the sentence does not assign it. See D-1 for the overlap with A1. |
| S4 | "Delivered the ISO 20022 (SWIFT MT-to-MX) migration and put AI-assisted code review into production." | PA-01 (O3); PA-07 (O1+O2) | V ✓ · acronym expanded ✓ | PASS | — |
| S5 | "Before UOB, built and re-architected **high-traffic** consumer internet platforms as an engineer and technical lead at Renren, Sohu and Baidu…" | PA-19 (O1); PA-18.1; PA-17.1 | V ✓ · **S/N: "high-traffic" has no evidence row** | **REVIEW** | The traffic metrics for these roles are held (HR-2 10M DAU; HR-5 5–10M QPS). The systems on record are a merchant-side order system (Baidu), a CMS (Sohu) and Renren's shopping site/Mall/CRM. "High-traffic" leans on the held figures. **Safe default:** "Before UOB, built and re-architected consumer internet platforms as an engineer and technical lead at Renren, Sohu and Baidu, …" |
| S6 | "…then held head-of-technology and architect roles at start-ups and scale-ups (2016–2022)" | 01 §5 / HR-1 ("head-of-technology roles (2016–2020)"); 02 §2 rows 3–6 (GBD Project Manager & Architect to Jul 2022) | T ✓ (no CTO / Chief Architect) · D ✓ | PASS | The extension to 2022 is covered by "architect" (GBD). |
| S7 | "…including leading VV Technology's 140-person technology organisation (total headcount)." | S3 [CONF 2026-10-21] | N ✓ (qualifier kept) · V ✓ ("leading", not "built") | PASS | 03 §0A still shows ❓; S3 is the back-fill. |
| S8 | "Used to explaining technical choices in business terms to senior management and steering committees." | PA-01.5 (reporting to senior management and the steering committee); PA-07 §4 (senior-management briefing) | S ✓ (no Board / C-suite) | PASS | — |

### Core Competencies
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| C1 | Banking Domains: "Payment initiation and **transaction processing** (ISO 20022, SWIFT, RTGS), retail lending servicing and collections, customer-360 data, integration with core banking" | Skills §9; PA-01; PA-04; PA-05; S2; **S6** ("core transaction-processing … modules of the payment hub") vs **03 PA-01 §2 / PA-01.7** ("processing & settlement sit outside the hub") and CF-N4 | S: terminology conflict between sources | **REVIEW** | S6 supports hub "transaction-processing modules". 03 places "processing and settlement" downstream of the hub. As a domain label, "transaction processing" can read as downstream payment processing, which is not on record. The conflict is not resolved here. **Safe default:** "Payment initiation, validation and status tracking (ISO 20022, SWIFT, RTGS), retail lending servicing and collections, customer-360 data, integration with core banking". "Integration with core banking" is fine (S2). It is not a core-banking-product claim (skills §12). |
| C2 | Engineering Leadership: "Leading squads through squad leads and engineering managers, coaching and mentoring, architecture and code reviews, contributed to bank-wide SDLC and code-review standards" | X-02; PA-03 §6 (coached teams); X-04; PA-03.3 (locked "contributed to") | V ✓ | PASS | — |
| C3 | Architecture & Integration: "Microservices and API design, event-driven integration, distributed high-concurrency systems, Apache Camel integration middleware, legacy modernisation and migration" | Skills §7; Apache Camel P; PA-01; X-01 | Te ✓ | PASS | — |
| C4 | **Hands-On Engineering**: "Java (concurrency control, JVM tuning), Spring Boot, Spring Cloud, Spring Batch, React, SQL, MySQL, MongoDB, Redis, Kafka" | Skills: Java P, Spring Boot P, Spring Batch P, React P, SQL P, MySQL P, Redis P, MongoDB P (Sohu/Baidu/AI Park, last used 2017), **Spring Cloud A/P ❓**, **Kafka A/P ❓** (Hengshunyuan/AI Park/VV, last used 2020; none at UOB) | Te: every item is anchored, but the row label claims hands-on depth | **REVIEW** | 01 §2 says a historical technology does not prove current hands-on proficiency. Under a "Hands-On Engineering" label, Kafka and Spring Cloud (depth unconfirmed, last used 2020) and MongoDB (2017) read as current hands-on skills. **Safe default:** "Java (concurrency control, JVM tuning), Spring Boot, Apache Camel, Spring Batch, React, SQL, MySQL, Redis". Move Spring Cloud and Kafka to the Architecture & Integration row (e.g. "…event-driven integration (Kafka), Spring Cloud microservices…") and drop MongoDB. Alternatively, Wilson confirms P depth for Kafka and Spring Cloud. |
| C5 | Cloud-Native & DevSecOps: "Kubernetes, Docker, AWS, Linux (RHEL); CI/CD on Jenkins and Bitbucket with a 99% SonarQube coverage gate, automated regression and penetration testing; secure SDLC" | Skills §5 (Kubernetes A, Docker A/P, AWS A/P, RHEL P, Jenkins/Bitbucket/SonarQube P/A); 03 §0A (99% gate); PA-03.2; PA-03.4 | N ✓ · Te ✓ (skills line; row not labelled hands-on) | PASS | Interview note: whether the 99% gate covers new code or overall code is still open (PA-03 §8). Kubernetes and AWS are anchored at GBD/VV (2019–22), not UOB. |
| C6 | Reliability & Performance: "Disaster recovery (DR) and failover drills, high availability, latency tuning under high load, Splunk monitoring, P1–P3 incident response and root-cause analysis (RCA)" | PA-02.1; PA-01.4; Splunk A/P; X-06 | ✓ | PASS | — |
| C7 | AI-Assisted Development: "Production AI code review on headless Claude Code agents, human-in-the-loop governance, prompt A/B evaluation" | PA-07.1, PA-07.2, PA-07.4; skills §8 (P) | Te ✓ · positioning ✓ (not "AI engineer") | PASS | — |

### Selected Achievements
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| A1 | Core-banking integration: "Lead the teams behind two platforms integrated with core banking: a payment-initiation hub that sends validated payments downstream, where core banking executes settlement, and processes the results returned; and a regional customer-360 platform that takes daily account summaries from core banking to support portfolio analysis." | S2 [CONF 2026-10-21]; CF-N4; X-02 (O4 "lead") | S ✓ (hub does not settle) · V ✓ · C ✓ | PASS | Interview note (02 CF-N7): foreign-currency cross-border legs settle through correspondent banks over SWIFT. Be ready to explain "core banking executes settlement" as account posting/booking. Third rendered line has no locked qualifier or metric to justify it (01 §6). See D-1. |
| A2 | Legacy modernisation: "Planned and architected a phased, Blue/Green-style coexistence deployment for the ISO 20022 migration… May and August 2025, ahead of SWIFT's November 2025 deadline… retired coexistence in August 2026 with no service interruption." | PA-01.1 (✅ dates / 📄 no-interruption); 03 §0A | D ✓ · V ✓ (O2+O3) · N ✓ | PASS | — |
| A3 | Hands-on core code: "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results…" | PA-01.3; S6 (closes C7 b) | V ✓ (O1) | PASS | — |
| A4 | Lending servicing and collections: "Own technology for retail unsecured-lending servicing — payment initiation, validation and lifecycle tracking — and post-disbursement collections…" | PA-04.1 (verbatim) | V ✓ | PASS | — |
| A5 | AI-assisted development: "Designed and built a production AI code-review service, live since May 2026 after formal architecture and risk approval… alongside SonarQube, cutting senior engineers' review time by an estimated ~80%; the AI never approves or merges." | PA-07.1; PA-07.2; PA-07.3; S9 | D ✓ · V ✓ (O1+O2) · N ✓ ("estimated ~80%" kept) | PASS | — |
| A6 | Payment resilience: "Defined the DR strategy, failover procedures and capacity baselines… personally led DR and failover drills, sustaining 99.9%+ availability under peak load." | PA-02.1 (verbatim); 03 §0A | N ✓ · V ✓ | PASS | — |
| A7 | Multi-squad leadership: "Lead two onshore/offshore platform teams through squad leads and engineering managers, with 1:1s, mentoring and performance management, and hold every release to CI/CD quality gates and SIT/UAT sign-off." | X-02; PA-03.1; PA-03.2 | V ✓ (O4) · S ✓ (team size not used as an outcome) | PASS | — |

### Professional Experience — UOB
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| E0 | "United Overseas Bank (UOB) \| Singapore — Oct 2022 – Present · Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | D ✓ · T ✓ (exact) | PASS | — |
| E1 | Scope: "Technology leader for two mission-critical platform lines in a MAS-regulated Tier-1 bank — cross-border payments (SWIFT ISO 20022 messaging) and retail unsecured lending — serving millions of accounts." | 02 §6.1; 03 §0A | S ✓ | PASS | — |
| E2 | "Led end-to-end design of a payment-initiation hub on Java, Spring Boot and Apache Camel — API contracts, orchestration, validation, enrichment and status tracking — integrating digital and branch channels, reference data, and vendor and third-party banking systems." | PA-01.2; PA-01 §3 | V ✓ (O2) · Te ✓ (3 technologies) | PASS | — |
| E3 | "Stay hands-on alongside delivery: review newly submitted core pull requests daily, co-design solutions with engineers, own the architecture, write core modules for significant changes and resolve production issues." | S5 (batch wording); X-04 | V ✓ · no %, no "full-time engineer" ✓ | PASS | — |
| E4 | "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking." | PA-01.4 (📄, no figure) | N ✓ (no invented figure) | PASS | — |
| E5 | "Lead the 10-engineer backend team of a regional customer-360 platform, in production since 2022: evaluated Cloudera as the processing framework, designed the data models and personally built the data-analysis module and Spring Batch jobs." | PA-05.1, PA-05.2, PA-05.3; skills (Cloudera A "evaluated"; Spring Batch P) | N ✓ · V ✓ · C ✓ (no SCV-CCD) | PASS | Does not claim he led the 2022 launch (C5 open). |
| E6 | "Led a 15-engineer onshore/offshore team and owned end-to-end delivery of the ISO 20022 programme — scope, roadmap, risks and dependencies, release planning and production rollout — shipping upgrades every 2–3 months after go-live." | PA-01.5; 03 §0A | N ✓ · V ✓ (O3) | PASS | — |
| E7 | "When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept." | X-02 (verbatim safe wording) | ✓ | PASS | — |
| E8 | "Act as the primary interface between business stakeholders, product owners, operations, compliance, architects and engineering managers; present status, risks and decisions to senior management and steering committees." | PA-01 §9 (stakeholder list); PA-01.5; 03 §5.3 U29 → PA-01 §9 / X-02 | S ✓ (no Board / C-suite) | PASS | "Primary interface" is 🔶 framing from [LIB] U29 with no verbatim safe wording, but it is consistent with the TDM role. |
| E9 | "Hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and chair governance of four IT service vendors — periodic budget reviews, year-end performance reviews and accountability meetings." | X-02; X-05; CF-N1; S7 (buyer-side) | N ✓ · C ✓ (no HCL) | PASS | — |
| E10 | "Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, RCA and post-incident reports; with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring." | X-06; PA-02.3; CF-N3 | S ✓ (no "reported to MAS") | PASS | — |
| E11 | "Led API encryption, database encryption of sensitive data, credential management and data migration for the payment, lending and customer-data platforms under MAS Technology Risk Management (TRM) guidelines." | X-01 | V ✓ · acronym expanded ✓ | PASS | — |
| E12 | "Established delivery KPIs — deployment frequency, mean time to recovery, incident trend and change-failure rate — and contributed to bank-wide SDLC, coding and code-review standards and to architecture-review governance." | PA-03.1 (03 safe wording uses "Established"); PA-03.3 (locked "contributed to") | V ✓ | PASS | — |

### Golden Bridge Drive
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| G0 | "Golden Bridge Drive (SG) Pte. Ltd. \| Singapore — Nov 2020 – Jul 2022 · Project Manager & Architect" | 02 §2 row 3 | D ✓ · T ✓ | PASS | — |
| G1 | Scope: "A multi-tenant SaaS platform for online-game businesses, built 0-to-1 on AWS — KYC, bonus incentives, VIP tiers, analytics and multi-channel payments." | PA-10.1; S9 (approved description) | S ✓ (no 200+, no iGaming wording) | PASS | — |
| G2 | "Architected and delivered the platform on Spring Cloud and Kubernetes behind an API gateway, including hierarchical KYC identity verification and rule models for authentication levels and bonus eligibility, triggers and distribution." | PA-10.1; PA-10.2 (200+ correctly dropped) | V ✓ (O2+O3; no "built"/"coded", OQ-2.2 respected) | PASS | — |
| G3 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness." | S4; PA-10.3 | N ✓ (qualifier kept; "led", not "built", per HR-9) | PASS | — |

### VV Technology
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| V0 | "VV Technology Pte. Ltd. \| Singapore — Apr 2019 – Jun 2020 · Head of Technical Centre" | 02 §2 row 4 (dates); **S8** supersedes the 02 §2 "Development" wording (TU-13 back-fill pending) | D ✓ · T ✓ per S8 | PASS | The CF-16 background-check note still applies: the title must match the employment letter. |
| V1 | Scope: "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services." | PA-11 §1 | ✓ | PASS | — |
| V2 | "Led VV's technology organisation and built its microservices platform from scratch, owning technology selection and budget." | PA-11.1 (03 safe wording "Built … from scratch"); PA-11 §4 (budget ✅) | V ✓ (as worded in 03) | PASS | — |
| V3 | "Delivered the first VV-Life release in 2019, including the payment subsystem — transaction, management and settlement-reconciliation modules — which integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments." | PA-11.2; S1 | D ✓ · S ✓ (no direct card-scheme connectivity claim) | PASS | — |
| V4 | "Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching that kept load off the database, bringing service response times to the millisecond level." | PA-11.4 (verbatim) | V ✓ · N ✓ (no % figure) | PASS | — |
| V5 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans." | PA-11.3; PA-11.5; CF-N8 | ✓ | PASS | — |

### AI Park
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| P0 | "AI Park \| China — Apr 2016 – Sep 2017 · VP of Technical Department" | 02 §2 row 6 (Apr 2016 = confirmed default; fact-check §6); **S8** (title) | D ✓ · T ✓ per S8 | PASS | Same CF-16 background-check note. |
| P1 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform connecting car parks to the cloud for automated management, online payment and recommendations." | PA-16.1 | V ✓ · no 1,000+ / 10M DAU ✓ | PASS | — |
| P2 | "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing; led the big-data team on HBase, MongoDB and Spark Streaming." | PA-16.4; PA-16 §3–§4 (big-data team [LIB]); skills (HBase A/P, MongoDB P, Spark Streaming A/P) | Facts ✓ | PASS | Style issue logged as D-2. |

### Earlier Experience
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| L1 | "Hengshunyuan Information Technology — Co-founder (Oct 2017 – Sep 2019, China): Owned product, architecture and delivery of an audio-learning platform, reaching a peak of ~100k daily active users." | 02 §2 row 5; D-10; PA-15.1; 03 §0A | D ✓ · T ✓ · N ✓ ("~" kept) | PASS | — |
| L2 | "Baidu — Technical Specialist, Nuomi group-buying e-commerce platform (May 2014 – Dec 2014, China): As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan; designed and coded Nuomi's payment-gateway integration with Alipay, WeChat Pay and UnionPay." | 02 §2 row 7; PA-17.1; S1 | D ✓ · T ✓ · N ✓ · no QPS ✓ | PASS | Three rendered lines with two ideas. Within the 1-in-5 allowance. |
| L3 | "Sohu.com — Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014, China): Led the re-architecture of the fifth-generation CMS (SSH to Spring MVC; memcached cluster to Redis cluster)." | 02 §2 row 8; PA-18.1 | D ✓ · T ✓ | PASS | — |
| L4 | "Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012, China): Developed Renren's shopping website, Renren Mall and CRM, and designed and coded Renren Mall's payment integration with Alipay and UnionPay." | 02 §2 row 9; PA-19; S1 (no WeChat Pay) | D ✓ · T ✓ · V ✓ (O1) | PASS | — |

### Education, Certifications & Languages
| # | Resume text | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| ED1 | "Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008)" | 02 §3; CF-02 | D ✓ · generic degree type (FU-4 open) ✓ | PASS | — |
| ED2 | "Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004)" | 02 §3; CF-01 | ✓ | PASS | — |
| ED3 | "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006) · PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3 [CERT-SS]; PMP in progress; CF-N5; S9 | ✓ (no "certified" PMP; SRE described as training) · C ✓ (no certificate numbers) | PASS | — |
| ED4 | "Languages: English and Mandarin (professional working proficiency in both)" | 02 §1 | ✓ | PASS | — |

### Style and structure findings
| # | Finding | Rule | Result | Question / safe default |
|---|---|---|---|---|
| D-1 | The hub + customer-360 + "integrated with core banking" pairing appears in both Summary P2 and Achievement A1, and core banking appears a third time in Competencies. Team scope also repeats: Summary (25), A7 (two teams), E5 (10), E6 (15). | 01 §6 Merging; §9 "no stacked repetition" | **REVIEW** | Keep the full core-banking story only in A1. **Safe default for Summary P2:** "Leads 25 onshore and offshore engineers across payment, customer-data and retail-lending platforms serving millions of accounts. Delivered the ISO 20022 (SWIFT MT-to-MX) migration and put AI-assisted code review into production." |
| D-2 | AI Park P2 names five technologies (Spring Cloud, Kafka, HBase, MongoDB, Spark Streaming) and holds two ideas (performance design; big-data team). | 01 §6 (one idea per bullet; at most 3–4 named technologies) | **REVIEW** | **Safe default:** "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing, and led the big-data team." Alternative: split the big-data team (HBase, Spark Streaming) into its own bullet, since page 3 has room. |

---

## 2. 01 §9 Pre-Delivery QA Checklist

| Item | Status | Note |
|---|---|---|
| **Facts:** every bullet traces to an ID in 03 / a section in 02; no ❓/⚠️/⛔ content | **Passed** | Every line traces (table above). Items that were ❓/⚠️ in the library are covered by session confirmations: VV/AI Park titles (CF-16 → S8), VV 140 (S3), GBD 40 (S4), concurrency control (C7 b → S6), GBD description (OQ-1.9 → S9). No held items appear: 10M DAU, QPS, 200+, 1,000+, Flink, chatbot, forecasting, Pureland, defect %, ramp-up %. |
| Dates and titles match 02 §2; no "CTO" / "Chief Architect" | **Passed** | UOB, GBD, Hengshunyuan, Baidu, Sohu and Renren are exact. VV and AI Park titles follow S8, which supersedes 02 §2 (back-fill TU-13 pending). AI Park Apr 2016 is the confirmed default. No CTO or Chief Architect anywhere (grep). |
| Every number matches the 03 Metrics Bank, with qualifiers | **Passed** | 18+, 25, 140 (total headcount, S3), 10, 15, 2–3 months, four vendors, 99.9%+, estimated ~80%, 99% gate, 40 (total headcount, S4), ~100k, two months ahead. Each bullet carries no more than 2 numbers. |
| Verbs match ownership level (01 §4) | **Passed** | "Built" only where O1 applies (A3, A5, E5) or where 03 safe wording uses it (V2). "Contributed to" is kept for bank-wide standards. "Established" (E12) follows the PA-03.1 safe wording. |
| Skills anchored in the inventory (P/A for Summary and bullets) | **Passed, with REVIEW** | All anchored. C4 groups depth-❓ and historical skills under "Hands-On Engineering" (REVIEW C4). |
| **Confidentiality:** no CEW / SCV-CCD / vendor names / internal numbers | **Passed** | Grep found no CEW, SCV, CCD, GMS, HCL, MEPS or customer names. |
| **Positioning:** headline and Summary fit the family × lens | **Passed (family/lens) · Not performed (JD fit)** | ATL × BNK framing is consistent: hands-on lead with architecture and delivery, not repackaged as an AI or big-data engineer. JD-specific fit was not assessed because the JD was not provided to the auditor. |
| Summary is narrative; no stacked repetition | **Failed (minor)** | Three short narrative paragraphs ✓. The core-banking pairing is repeated between Summary P2 and A1 (D-1, REVIEW). |
| British spelling consistent | **Passed** | Grep found no -ize/-yze/"program"/"center"/"license" forms. "Organisation", "programme", "licence", "containerised" and "modernisation" are used throughout. |
| **Document:** layout; ≤ 3 pages; page numbers; no orphaned headings | **Passed** | See §3. 04 spec not read (not an input). |
| Text extractable; renders as PDF | **Passed** | pdftotext returns all content in reading order. Competency table text extracts cleanly. |
| File name per 01 §10 | **Passed (provisional)** | `wilson-2026_ATL_Bank_DBS_V1_0_0` matches the pattern. OQ-R3 (the [Lens] segment) is still open. The `_draft` suffix and red markup (43/93 runs red) are correct for a draft; the final must be all black. |
| **Review package:** three-dimension review; change log | **Not performed** | Outside the auditor's scope; those files were deliberately not read. |

## 3. Document checks (render report + visual inspection of the PDF at 70 dpi)

| Check | Result | Note |
|---|---|---|
| Page count ≤ 3 | ✅ 3 pages, A4 | Confirmed by pdfinfo and visually |
| Page numbers | ✅ "Page 1 of 3" … "Page 3 of 3" in the footer | Visual |
| Heading orphans | ✅ None | Professional Experience starts at the top of p.2; Earlier Experience starts at the top of p.3 |
| Bullets ≤ 3 lines | ✅ | No bullet exceeds 3 lines (render report; visual) |
| ≤ 1 bullet in 5 at 3 lines | ✅ 5 of 30 (limit 6) | 3-line bullets: A1, A2, A5, UOB E2, Baidu L2. A1's third line has no locked qualifier or metric to justify it (01 §6). Minor. |
| Paragraphs ≤ 4 lines | ✅ | Summary paragraphs are 3 / 3 / 4 lines (P3 at the limit). Scope lines are 1–2 lines. |
| Page 1 = header + summary + competencies + achievements | ✅ | All 7 achievements are on p.1 (visual + report `page1_has_all_achievements: true`) |
| Page 2 starts with Experience | ✅ | — |
| Lint / line flags | ✅ none | Render report |
| Other | ℹ️ | Page 3 is about 60% blank, so D-2 can be split without a page risk. Contact line repeats "Singapore". Low-resolution check only: fine typography and kerning were not verified. |

---

## 4. Summary

**Counts (59 claim rows + 2 style rows):**
- Claims: **PASS 56 · REVIEW 3 · FAIL 0**
- Style/structure: **REVIEW 2** (D-1, D-2)
- Total: **PASS 56 · REVIEW 5 · FAIL 0**

The draft is factually clean. Every number, date and title traces to 02/03 or S1–S9, with qualifiers kept. No confidential names appear and no held claims are used.

### Required fixes
None. No claim fails the fact rules.

### For Wilson to decide
1. **S5, "high-traffic consumer internet platforms" (Summary P3).** Keep "high-traffic"? Nothing on record quantifies it: the traffic metrics are held (HR-2, HR-5), and the systems were merchant-side, CMS and shopping/Mall. **Safe default:** delete "high-traffic", giving "built and re-architected consumer internet platforms as an engineer and technical lead at Renren, Sohu and Baidu".
2. **C1, "Payment initiation and transaction processing" (Core Competencies).** S6 says the hub has core transaction-processing modules. 03 PA-01 says "processing and settlement sit outside the hub" (CF-N4). Which reading should the resume use? **Safe default:** "Payment initiation, validation and status tracking (ISO 20022, SWIFT, RTGS), …"
3. **C4, "Hands-On Engineering" row.** Kafka and Spring Cloud are depth A/P ❓ and last used in 2020 (not at UOB); MongoDB was last used in 2017. Can you confirm current hands-on (P) depth? If not, **safe default:** "Java (concurrency control, JVM tuning), Spring Boot, Apache Camel, Spring Batch, React, SQL, MySQL, Redis". Move Kafka and Spring Cloud to Architecture & Integration and drop MongoDB.
4. **D-1, repetition between Summary P2 and Achievement A1.** Keep the core-banking integration detail only in A1? **Safe default for Summary P2:** "Leads 25 onshore and offshore engineers across payment, customer-data and retail-lending platforms serving millions of accounts. Delivered the ISO 20022 (SWIFT MT-to-MX) migration and put AI-assisted code review into production."
5. **D-2, AI Park bullet 2 (five technologies, two ideas).** Trim or split? **Safe default:** "…achieving millisecond-level service processing, and led the big-data team." (Drop "on HBase, MongoDB and Spark Streaming", or move them to a separate bullet; page 3 has room.)

### Interview-defensibility notes (no change required)
- A1 "core banking executes settlement": be ready to distinguish account posting from interbank settlement (MEPS+ / correspondent banks), per 02 CF-N7.
- C5 "99% SonarQube coverage gate": whether it covers new code or overall code is still open (PA-03 §8).
- V0/P0 titles: S8 wording must match the employment letters at background check (CF-16).
- S3/E1: which team covers lending and collections is still open (C6). Be ready to explain how the 25 engineers map to the two platform lines.

---

## Resolution (2026-10-26)

No FAIL items.

| Item | Resolution |
|---|---|
| S5 ("high-traffic") | Default applied — "built and re-architected consumer internet platforms …". |
| C1 ("transaction processing") | Default applied — "Payment initiation, validation and status tracking (ISO 20022, SWIFT, RTGS), …". Left for Wilson: which reading (S6 hub modules vs CF-N4 downstream) should the resume use? |
| C4 (Hands-On row) | Default applied — Hands-On row now "Java (concurrency control, JVM tuning), Spring Boot, Apache Camel, Spring Batch, React, SQL, MySQL, Redis"; Spring Cloud and Kafka moved to Architecture & Integration; MongoDB dropped. Left for Wilson: confirm current P depth for Kafka / Spring Cloud. |
| D-1 (repetition) | Default applied — Summary P2 replaced with the auditor's text; the "Multi-squad leadership" achievement was also cut (cold-read), removing the team-scope repeat. |
| D-2 (AI Park five technologies) | Default applied — "…achieving millisecond-level service processing, and led the big-data team." |
| Software Designer certificate | Not raised in this audit; education lines unchanged (Revision Brief §1.1). |
| Interview notes | No text change. A1 now uses the canonical S2 wording ("hands validated payments to core banking, which executes settlement"); be ready to distinguish account posting from interbank settlement (CF-N7). 99% gate basis listed for Wilson. |
