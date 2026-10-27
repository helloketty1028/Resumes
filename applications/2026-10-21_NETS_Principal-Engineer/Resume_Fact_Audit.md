# Resume Fact & Quality Audit — 01

**File audited:** `wilson-2026_ATL_Bank_NETS_V1_0_0_draft.txt` (pdftotext), cross-checked against `wilson-2026_ATL_Bank_NETS_V1_0_0_draft.pdf` (3 pages, A4, rendered at 80 dpi and **viewed page by page**) and `wilson-2026_ATL_Bank_NETS_V1_0_0_draft.report.md`.
**Auditor:** independent; the drafting notes, cards, change log, matching analysis and resume.json were **not** read.
**Audit date:** 2026-10-21

**Sources read (versions)**
| Source | Version |
|---|---|
| `01_Resume_Master_Rules.md` | v1.1 · 2026-10-20 |
| `02_Candidate_Profile.md` | v3.1 · 2026-10-17 |
| `03_Achievement_Library.md` | v4.1 · 2026-10-17 |
| `technical-skills-inventory.md` | v2.3 · 2026-10-17 |
| `fact-check-and-open-questions.md` | v2.4 · 2026-10-20 |
| `Session_Confirmations.md` | S1–S9 + hold line (2026-10-20 / 2026-10-21) → tag `[CONF 2026-10-21]` |

**Not read (out of brief scope):** `04_Resume_Layout_Spec.md`, `05_JD_Keyword_and_Matching_Rules.md`, the target JD. So JD fit, "Layout per 04" and 05 §2 lens checks are only partly performed (see §2).

Verdict key: **PASS** = traceable, correct verb, number and qualifier · **REVIEW** = judgement call for Wilson · **FAIL** = must be fixed or deleted.

---

## 1. Claim Table

### Header
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| H1 | "WILSON" | 02 §1, D-11 | Name only, no surname ✓ | PASS | — |
| H2 | "Singapore PR \| +65 8655 9547 \| Skyzhang1028@gmail.com \| Singapore" | 02 §1 | PR since 2024 ✓; phone and email ✓ (the capital S is cosmetic) | PASS | — |
| H3 | "Principal Engineer — Payment & Transaction-Processing Platforms \| Hands-On Java Architecture · Resilience by Design" | 02 §7.2 ATL×BNK "Principal Engineer / Technical Lead … Resilience by Design"; 01 §5 | Target-role headline allowed (01 §5); not a past title ✓; no CTO ✓. JD title match not verifiable (JD not provided) | PASS | — |

### Professional Summary
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| S1 | "Hands-on technical lead for mission-critical payment platforms, with 18+ years of Java engineering and solution architecture across Tier-1 banking, fintech and SaaS products, and consumer e-commerce." | 03 §0A "18+ years = career total since Jul 2008"; 02 §4; 02 §5 | **Number attribution narrowed.** The 18+ figure is the career total. Here it is attached to "Java engineering *and solution architecture*", but 02 §5 shows no [AR] at Renren (2008–12), and Java depth in the 2016–20 head roles is A, not P | **REVIEW (R1)** | Safe default in §4 |
| S2 | "Works across the full lifecycle … architecture and solution design, core code and code review, migration of live systems and production resilience." | X-04, S5, PA-01, PA-02 | Matches X-04 split; no "full-time" or % ✓ | PASS | — |
| S3 | "Since 2022, a Vice President in UOB's Group Technology & Operations, leading 25 onshore and offshore engineers and chairing governance of four IT service vendors for cross-border payment and retail-lending platforms that serve millions of accounts in a MAS-regulated bank." | 02 §2 row 1; X-02 (25 ✓ §0A); X-05 (four vendors ✓ §0A); 02 §6.1 | Title, date, numbers ✓; vendors unnamed ✓; "chair" = X-05 ✓ | PASS | — |
| S4 | "Owns the architecture of the bank's payment-initiation hub and led its move to ISO 20022 messaging." | X-04 / S5 ("own the architecture"); PA-01 O2+O3 | Verb within O2/O3 ✓; no CEW ✓ | PASS | — |
| S5 | "Began as an engineer and technical lead on Renren's e-commerce platform, Sohu's news CMS and Baidu's Nuomi merchant system" | 02 §2 rows 7–9; PA-17–19 | Roles match (engineer / technical leader / project leader) ✓ | PASS | — |
| S6 | "then spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups, delivering microservices platforms, a payment subsystem and a multi-tenant SaaS platform from scratch." | 01 §5 ("head-of-technology roles 2016–2020"); GBD title "Project Manager & Architect" (2020–22); PA-11.1, PA-11.2, PA-10.1 | No CTO or Chief Architect ✓; "architect roles" covers GBD to 2022 ✓ | PASS | — |
| S7 | "Used to explaining technical choices in business terms to senior management and steering committees." | PA-01.5 (senior management + steering committee); PA-01 §6/§9; PA-07 §4 (senior-management briefing) | 🔶 interpretation of documented reporting; no Board or C-suite ✓ | PASS | — |

### Core Competencies
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| C1 | Payment Systems: "Payment initiation, validation, enrichment and status tracking; … reconciliation; ISO 20022, SWIFT" | Skills §9; PA-01; S1 / PA-11.2 (reconciliation) | All anchored ✓ | PASS | — |
| C2 | Payment Systems: "settlement integration with core banking" | S2; 02 CF-N4; skills §9 "Never claim: core banking" | S2 supports a downstream hand-off: core banking settles, and the hub processes the returned results. But "settlement integration" can read as settlement-system expertise, which matters for a payment-network (NETS) reader. CF-N4 says the hub does not settle or clear. The skills inventory has no core-banking-integration row | **REVIEW (R2)** | Safe default in §4 |
| C3 | Payment Systems: "card and e-wallet payment integration" | S1 (Renren, Baidu Nuomi, VV-Life) | Merchant-side gateway integration ✓; does not claim direct card-scheme connectivity, POS, card switching or QR acquiring ✓ (S1, hold line). Interview note: frame it as merchant-side integration (bank-card binding, gateways) | PASS | — |
| C4a | Architecture & Integration: "Java, Spring Boot, Apache Camel (enterprise integration patterns), event-driven integration, microservices, distributed systems, multi-tenant SaaS" | Skills §1–2 (P), §7 | All anchored ✓ | PASS | — |
| C4b | Architecture & Integration: "RESTful API design" | PA-01.2 "API contracts"; skills §7 "API gateway" | **REST is not an anchored skill.** Only "API contracts" and API gateway are on record | **REVIEW (R3)** | Safe default in §4 |
| C5 | Performance & Resilience: "Low-latency transaction processing, concurrency control, thread-pool and JVM tuning, high availability, DR and failover drills, capacity baselines" | PA-01.4; S6; skills §1 Java (concurrency) P; PA-02.1 | Anchored ✓ | PASS | — |
| C6 | Security & Risk: "API and database encryption, credential management, role-based access control, secure SDLC, DPIA, data governance, MAS TRM (Singapore technology-risk rules)" | X-01; PA-01.3 (permission matrix); PA-03.4; S9 (MAS TRM gloss) | Anchored ✓ | PASS | — |
| C7 | Engineering Delivery: "DevSecOps practice: CI/CD on Bitbucket and Jenkins, SonarQube quality gates, automated regression and penetration testing; Splunk observability; SIT/UAT release sign-off" | PA-03.1–03.4; skills §5, §6, §10 | Each component is anchored. "DevSecOps" is a 🔶 label for secure SDLC plus penetration testing in CI/CD | PASS | — |
| C8 | Platforms & Middleware: "Linux (RHEL); MySQL, SQL, Redis; Kafka, RocketMQ and AWS SQS/SNS messaging; Docker, Kubernetes; AWS (API Gateway, EC2/ECS, RDS, CloudWatch)" | Skills §3–§5 (RHEL/SQL P CF-N6; MySQL/Redis P; Kafka A/P❓; RocketMQ A; SQS/SNS A/P❓; Docker A/P; K8s A; AWS A) | All anchored, so the skills-line rule is met. **But** Kafka, RocketMQ, SQS/SNS, Docker, Kubernetes and AWS are anchored only in 2016–2022 roles, mostly at depth A, and none at UOB. Under a "Hands-On" Principal Engineer headline this reads as current hands-on proficiency (01 §2) | **REVIEW (R4)** | Safe default in §4 |
| C9 | Technical Leadership: "Design and code reviews, quality gates, engineering standards (contributed bank-wide), mentoring, 1:1s and performance management, steering-committee reporting" | X-04; PA-03.3 (locked "contributed"); X-02; PA-01.5 | Locked verb kept ✓ | PASS | — |

### Selected Achievements
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| A1 | "Payment-hub design: Led end-to-end design of a payment-initiation hub — API contracts, orchestration, validation, enrichment and status tracking — integrating digital and branch channels, reference data, and vendor and third-party banking systems." | PA-01.2 📄 | Near-verbatim safe wording; O2 ✓ | PASS | — |
| A2 | "Hands-on core engineering: Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results returned by downstream systems." | PA-01.3 ✅; **S6** (concurrency control; closes C7 b) | O1 "built" ✓. Note: 03 still shows C7(b) as open, so S6 back-fill is pending | PASS | — |
| A3 | "Zero-interruption modernisation: Planned and architected a phased, Blue/Green-style coexistence deployment for the ISO 20022 (SWIFT MT-to-MX) migration …: took MX-rich messaging live in May and August 2025, ahead of SWIFT's November 2025 deadline, and retired coexistence in August 2026 with no service interruption." | PA-01.1 ✅/📄; §0A row 3 and row 5 | Dates ✓; "no service interruption" 📄 used as worded ✓; O2+O3 verbs ✓ | PASS | — |
| A4 | "Performance engineering: Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking; earlier brought VV's services to millisecond-level response times." | PA-01.4 📄 (no figure); PA-11.4 ✅ (no % figure) | No invented figure ✓; VV attributed ✓ | PASS | — |
| A5 | "Resilience and security: Designed security controls — API and database encryption of sensitive data, credential management **and role-based permissions** — for payment, lending and customer-data platforms under secure SDLC, DPIA and MAS TRM; personally led DR and failover drills, sustaining 99.9%+ availability under peak load." | X-01 ✅ (encryption, credential management, data migration for payment/lending/customer-data platforms); PA-01.3 (permission matrix = **hub only**); PA-02.1 (99.9%+ = **real-time payment middleware**) | **Scope inflation.** Role-based permissions are on record only for the payment-initiation hub (PA-01.3), not for the lending or customer-data platforms. The 99.9%+ figure (PA-02.1) belongs to the real-time payment middleware, but here it follows a clause naming all three platforms, so it can be read as applying to all of them | **FAIL (F1)** | See Required fixes |
| A6 | "Payment integrations across markets: Designed and coded Renren Mall's payment integration (Alipay, UnionPay) and Baidu Nuomi's payment-gateway integration (Alipay, WeChat Pay, UnionPay); architected VV-Life's payment subsystem, integrating UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation." | **S1** | O1+O2 "designed and coded" ✓; VV O2 "architected" ✓; no WeChat Pay under Renren ✓; no direct card-scheme claim ✓ | PASS | — |
| A7 | "Engineering governance: Established delivery KPIs and CI/CD quality gates — 99% SonarQube coverage, automated regression and penetration testing, SIT/UAT sign-off for every release — and contributed to bank-wide SDLC and code-review standards." | PA-03.1–03.3; §0A "99% SonarQube coverage gate" | "Established" = 03 safe wording; "contributed to" locked ✓; 99% reads as a gate ✓. Interview note: new-code vs overall coverage is still ❓ (PA-03 §8) | PASS | — |

### UOB — Oct 2022 – Present
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| U0a | "United Overseas Bank (UOB) \| Singapore · Oct 2022 – Present · Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | Exact ✓ | PASS | — |
| U0b | "Two mission-critical platform lines: cross-border payments on SWIFT ISO 20022 and retail unsecured lending and collections." | 02 §6.1 | ✓ | PASS | — |
| U1 | "Stay hands-on alongside delivery: review newly submitted core pull requests daily, co-design solutions with engineers, own the architecture, write core modules for significant changes and resolve production issues." | **S5**; X-04 | Batch wording exact; no ~50/~20, no "full-time" or % ✓ | PASS | — |
| U2 | "Lead the 10-engineer backend team of a regional customer-360 platform live since 2022: evaluated Cloudera as its processing framework, designed the customer data models and built its data-analysis module and Spring Batch jobs." | PA-05.1 📄, PA-05.2 ✅ (O1), PA-05.3 ✅; §0A 10-engineer | No SCV-CCD ✓; "live since 2022" does not claim the launch (C5 open) ✓; "built" refers to O1 modules, not the team ✓ | PASS | — |
| U3 | "Integrated both platforms with core banking: the payment-initiation hub hands validated payments downstream for core banking to settle, and the customer-360 platform takes daily account summaries for portfolio analysis." | **S2**; CF-N4 | Facts match S2 ✓; hub does not settle ✓. **But** S2 does not record Wilson's ownership level for the core-banking interfaces, so the verb "Integrated" implies he built them (O1/O2) without evidence. Also, "both platforms" sits right under the scope line naming the two platform *lines* (payments and lending), but here it means hub + customer-360 | **REVIEW (R5)** | Safe default in §4 |
| U4 | "Designed and built a production AI code-review service: headless Claude Code agents, orchestrated by Spring Boot, review each pull request alongside SonarQube. Live since May 2026 after formal architecture and risk approval, it cut senior engineers' review time by an estimated ~80%; the AI never approves or merges." | PA-07.1 (O1+O2), PA-07.2, PA-07.3; **S9** | "estimated ~80%" qualifier kept ✓; May 2026 ✓; human-in-the-loop ✓ | PASS | — |
| U5 | "Led a 15-engineer onshore/offshore team and owned end-to-end delivery of the ISO 20022 programme — scope, roadmap, RAID, release planning and production rollout — shipping upgrades every 2–3 months after go-live." | PA-01.5; §0A rows 3, 15 | Team size given as scope, not as an outcome ✓ | PASS | — |
| U6 | "Coordinate P1–P3 production incidents end to end — … — and produce technical incident analyses that support the bank's regulatory reporting to MAS." | X-06; CF-N2 | "Support" wording kept; never "reported to MAS" ✓ | PASS | — |
| U7 | "With no separate SRE function, own production support for the payment platforms — SLA tracking, SLIs/SLOs, Splunk-based monitoring and alerting, and capacity baselines." | PA-02.3; CF-N3 | Verbatim ✓ | PASS | — |
| U8 | "When the two platform lines' schedules conflict, agree MVP scope … and set a sequence all parties accept." | X-02 | Verbatim ✓ | PASS | — |
| U9 | "Own technology for retail unsecured-lending servicing — payment initiation, validation and lifecycle tracking — and post-disbursement collections across credit-card and unsecured-loan portfolios." | PA-04.1 | Verbatim ✓ | PASS | — |
| U10 | "Lead both platform teams through squad leads and engineering managers — 1:1s, mentoring and performance management — and work closely with teams in India, Thailand and Indonesia across time zones." | X-02; D-09 | O4 ✓; collaboration, not line management ✓; no US claim ✓ | PASS | — |
| U11 | "Hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and run vendors' periodic budget reviews, year-end performance reviews and accountability meetings." | X-02; X-05; S7 (buyer-side) | ✓; no vendor names ✓ | PASS | — |

### Golden Bridge Drive — Nov 2020 – Jul 2022
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| G0 | "Golden Bridge Drive (SG) Pte. Ltd. \| Singapore · Nov 2020 – Jul 2022 · Project Manager & Architect" | 02 §2 row 3 | Exact ✓ | PASS | — |
| G1 | "Multi-tenant SaaS for online-game businesses, built 0-to-1 on AWS — KYC, bonus incentives, VIP tiers and multi-channel payments." | **S9** (approved description); 02 §6.3 | Approved wording ✓; "200+" dropped ✓ | PASS | — |
| G2 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness." | **S4**; PA-10.3; §0A | "Led", not "built" a team ✓ (HR-9); qualifier kept ✓ | PASS | — |
| G3 | "Architected and delivered the platform on Spring Cloud and Kubernetes behind an API gateway, including hierarchical KYC identity verification and rule models for authentication levels and bonus eligibility, triggers and distribution." | PA-10.1, PA-10.2 📄 | O2+O3 ✓; not claimed as own code (OQ-2.2) ✓ | PASS | — |
| G4 | "Architected the AWS deployment (API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch) and applied DPIA, API and database encryption and credential management; led data migration." | Skills §5 (GBD AWS = A); X-01 (GBD) ✅; skills §10 DPIA (GBD) | Facts ✓. Style: six named technologies vs the 3–4 limit in 01 §6 (see §3 notes) | PASS | — |

### VV Technology — Apr 2019 – Jun 2020
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| V0 | "VV Technology Pte. Ltd. \| Singapore · Apr 2019 – Jun 2020 · Head of Technical Centre" | 02 §2 row 4 (dates); **S8** (title supersedes 02 "Development" wording; TU-13 back-fill pending) | ✓ | PASS | — |
| V1 | "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services." | PA-11 §1 | ✓ | PASS | — |
| V2 | "Led VV's 140-person technology organisation (total headcount) and built its microservices platform from scratch, owning technology selection and the technology budget." | **S3**; PA-11.1 | S3 wording exact; "built" applies to the platform (PA-11.1 📄), not the team ✓ | PASS | — |
| V3 | "Took part in product-strategy planning and delivered the first VV-Life release in 2019, including the payment subsystem's transaction, management and reconciliation modules." | PA-11 §4; PA-11.2 | ✓ | PASS | — |
| V4 | "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance." | PA-13 | Safe wording verbatim; "GMS" not used ✓ | PASS | — |
| V5 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans." | PA-11.3; PA-11.5 / CF-N8 | ✓ | PASS | — |

### AI Park — Apr 2016 – Sep 2017
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| P0 | "AI Park \| China · Apr 2016 – Sep 2017 · VP of Technical Department" | 02 §2 row 6 (Apr 2016 = proposed canonical [CONF]; fact-check §6); **S8** (title) | ✓. Residual: CF-06 (Apr vs May) uses the confirmed default | PASS | — |
| P1 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform connecting car parks to the cloud for automated management, online payment and recommendations." | PA-16.1 | ✓; no 1,000+ or 10M DAU ✓ | PASS | — |
| P2 | "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing; led the big-data team on HBase, MongoDB and Spark Streaming." | PA-16.4 ✅; PA-16 §3–§4 [LIB] 📄; skills §3–§4 | ✓ | PASS | — |

### Earlier Experience
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| E1 | "Hengshunyuan Information Technology — Co-founder (Oct 2017 – Sep 2019, China): Owned product, architecture and delivery of an audio-learning platform, reaching a peak of ~100k daily active users." | 02 §2 row 5; D-10; PA-15.1; §0A | Dates per D-10 ✓; "~" kept ✓ | PASS | — |
| E2 | "Baidu — Technical Specialist, Nuomi … (May 2014 – Dec 2014, China): As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan." | 02 §2 row 7; PA-17.1; §0A | ✓; no 5–10M QPS ✓ | PASS | — |
| E3 | "Sohu.com — Technical Leader / Project Leader … (Mar 2012 – May 2014, China): Led the re-architecture of the fifth-generation CMS (SSH to Spring MVC; memcached cluster to Redis cluster)." | 02 §2 row 8; PA-18.1 | ✓ | PASS | — |
| E4 | "Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012, China): Developed Renren's shopping website, Renren Mall and CRM on Spring, Solr, Redis, MySQL and Nginx." | 02 §2 row 9; PA-19 | ✓ | PASS | — |

### Education, Certifications & Languages
| # | Resume text | Evidence ID | Checks | Verdict | Fix |
|---|---|---|---|---|---|
| Ed1 | "Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008)" | 02 §3; CF-02; FU-4 default | ✓ | PASS | — |
| Ed2 | "Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004)" | 02 §3; CF-01 | ✓ | PASS | — |
| Ed3 | "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006)" | 02 §3 ✅ [CERT-SS] **vs** Session_Confirmations hold line: "any certification other than 'PMP — in progress' and SRE formal training" is held | **Sources conflict.** A verified primary document vs an explicit 2026-10-21 hold. Not resolved by guessing | **REVIEW (R6)** | Safe default in §4 |
| Ed4 | "PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3; CF-N5; hold line | Not "certified" ✓; training, not a certification ✓ | PASS | — |
| Ed5 | "Languages: English and Mandarin (professional working proficiency in both)" | 02 §1 | ✓ | PASS | — |

---

## 2. 01 §9 QA Checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to an ID in 03 / 02 / S#; no ❓/⚠️/⛔ content | **Failed** | F1 (A5 role-based-permissions scope and 99.9%+ scope). R6 is a possible ⛔ (certification hold). Everything else traces. No 10M DAU, 10M HTTP, QPS, 1,000+, 200+, Flink, chatbot, Pureland, ~50/~20 modules, "10+ payment domains", or 30–40% / 70–80% figures |
| Dates and titles match 02 §2 exactly; no CTO / Chief Architect | Passed | VV "Head of Technical Centre" and AI Park "VP of Technical Department" follow **S8**, which supersedes the 02 §2 wording (TU-13 back-fill pending). AI Park Apr 2016 and Hengshunyuan Oct 2017 – Sep 2019 are the confirmed defaults (CF-06, D-10). Baidu months 📄 [R22]. No CTO or Chief Architect |
| Every number matches the Metrics Bank, qualifiers kept | Passed (1 REVIEW) | 25, four, 15, 10, 2–3 months, May/Aug 2025, Aug 2026, May 2026, "estimated ~80%", 99.9%+, 99% gate, 40 and 140 "(total headcount)", ~100k, two months ahead — all ✓. R1: 18+ years attached to a narrower attribution |
| Verbs match ownership level (01 §4) | Passed (1 REVIEW) | O1 "built/coded" only where O1 is on record (PA-01.3, S6, PA-05.2, PA-07, S1). "Contributed to" kept for bank-wide standards. R5: "Integrated" lacks an ownership record |
| Skills anchored (P/A for Summary and bullets) | Passed (2 REVIEW) | All Summary and bullet technologies are P or A. R3: "RESTful" not in the inventory. R4: 2016–22 stack in Competencies reads as current |
| No CEW / SCV-CCD / vendor names / internal numbers (01 §7) | Passed | grep: no CEW, SCV, CCD, GMS or HCL; no volumes or customer names |
| Headline and Summary fit family × lens | Passed (partial) | Fits ATL × BNK against 02 §7.2 "Principal Engineer / Technical Lead … Resilience by Design". 05 §2 and the JD were not read, so JD fit was **not performed** |
| Summary narrative; no stacked repetition | Passed with note | Three narrative paragraphs, not one bullet per role. Note: the Competencies "Security & Risk" and "Engineering Delivery" rows repeat almost word for word the lists in Achievements A5 and A7 (see §3) |
| British spelling consistent; JD titles quoted as written | Passed / not performed | grep found no -ize/-yze, "center", "program", "license" (noun) or "behavior"; "organisation", "programme", "licence", "modernisation" ✓. JD-title quoting not performed (no JD) |
| Layout per 04; ≤ 3 pages; page numbers; no orphan headings | Passed (04 not read) | Checked against the brief's enumerated checks (§3), not against the 04 text itself |
| Text extractable; renders correctly as PDF | Passed | Tagged PDF; pdftotext gives the full text in reading order; the Competencies table extracts row by row |
| File name per 01 §10 | Passed with note | `wilson-2026_ATL_Bank_NETS_V1_0_0` matches `[Family]_[Lens]_[Target]_V…`; the "_draft" suffix is for the draft stage only; OQ-R3 is still open |
| Three-dimension review delivered separately | Not performed | Outside auditor scope (the drafter's analysis was deliberately not read) |
| Change log | Not performed | Not read by design |

---

## 3. Document Checks (render report + own view of PDF pages 1–3)

**Visually verified:** I rasterised all three pages and looked at each one.

| Check | Result | Note |
|---|---|---|
| Page count ≤ 3 | ✓ 3 | pdfinfo + visual |
| Page numbers | ✓ | Footer "Page N of 3" on every page |
| Heading orphans | ✓ none | Page 2 opens with PROFESSIONAL EXPERIENCE; page 3 opens with EARLIER EXPERIENCE; the "Delivery, Production & Leadership" sub-heading has content after it |
| Bullets ≤ 3 lines | ✓ | None above 3 |
| ≤ 1 in 5 bullets at 3 lines | ✓ 4/31 (13%) | 3-line bullets: A3, A5, A6 (page 1) and U4 (page 2). Note: 3 of the 7 Selected Achievements run to 3 lines, so page 1 looks dense. Fixing F1 may bring A5 down to 2–3 lines |
| Paragraphs ≤ 4 lines | ✓ | Each Summary paragraph is 3 lines; role context lines are 1 line each |
| Page 1 = header + Summary + Competencies + Achievements | ✓ | About 15% white space left at the bottom of page 1; Experience starts on page 2 |
| Render report lint / line flags | none | Report: Layout OK = True; 47/93 runs red (draft markup, expected per 01 §10) |

**Style observations (not counted as claims)**
- **Tech count above 3–4 per bullet (01 §6):** G4 (6 AWS services), P2 (5), V4 (5, 03 verbatim) and E4 (5, 03 verbatim). G4 is the clearest case: trim to e.g. "(API Gateway, EC2/ECS, RDS, DynamoDB)".
- **Acronyms not expanded at first use (01 §6A):** MT/MX, RAID, SOW, SLI/SLO, RCA, DPIA. ISO 20022 and DR are explained.
- **Chronology:** Hengshunyuan (Oct 2017 – Sep 2019) appears under Earlier Experience, below AI Park (2016–17), which sits in the main section. This is consistent with D-10 (overlap not annotated), but a careful reader may notice the order break.
- **Repetition:** the Competencies rows "Security & Risk" and "Engineering Delivery" repeat the A5 and A7 lists. The ISO 20022 programme appears in S4, A3 and U5, but each from a different angle, which is acceptable.

---

## 4. Summary

**Counts:** 63 claims audited · **PASS 56 · REVIEW 6 · FAIL 1**

### Required fixes
**F1 — Selected Achievements, "Resilience and security" (A5).** Role-based permissions are on record only for the payment-initiation hub (PA-01.3). The 99.9%+ figure belongs to the real-time payment middleware (PA-02.1), not to the lending and customer-data platforms. Replace the whole bullet with:

> **Resilience and security:** Designed security controls — API and database encryption of sensitive data and credential management — for payment, lending and customer-data platforms under secure SDLC, DPIA and MAS TRM; personally led DR and failover drills for the real-time payment middleware, sustaining 99.9%+ availability under peak load.

(Role-based access control stays visible in Achievement A2 (permission matrix) and the Security & Risk competency row.)

### For Wilson to decide
| ID | Where | Question | Safe default |
|---|---|---|---|
| R1 | Summary, sentence 1 | "18+ years of Java engineering *and solution architecture*" attaches the career-total number to architecture, which isn't on record for Renren 2008–12. Keep it? | "Hands-on technical lead for mission-critical payment platforms, with 18+ years across Tier-1 banking, fintech and SaaS products, and consumer e-commerce, combining Java engineering with solution architecture." |
| R2 | Competencies, Payment Systems | Is "settlement integration with core banking" acceptable for a payment-network reader? The hub does not settle (CF-N4), and the inventory says never claim core banking | Replace with "hand-off to core banking for settlement" |
| R3 | Competencies, Architecture & Integration | Were the hub's API contracts REST? "RESTful" is not anchored in the skills inventory | Replace "RESTful API design" with "API design" (and add REST to the inventory if confirmed) |
| R4 | Competencies, Platforms & Middleware | Kafka, RocketMQ, SQS/SNS, Docker, Kubernetes and AWS are anchored only in 2016–22 roles, mostly at depth A. Under a "Hands-On" Principal Engineer headline they read as current proficiency. Keep as is, or qualify? | Keep (the skills-line rule is met) and prepare the interview line "architected/led 2016–22; current hands-on stack is Java, Spring Boot, Camel, Splunk" |
| R5 | UOB bullet "Integrated both platforms with core banking" | Did your teams design or build the core-banking interfaces (O1/O2), or consume existing ones? "Both platforms" can also be misread as the two platform lines | "Both platforms connect to core banking: the payment-initiation hub hands validated payments downstream for core banking to settle and processes the results returned, and the customer-360 platform takes daily account summaries for portfolio analysis." |
| R6 | Education, certifications | Does the 2026-10-21 hold on "any certification other than PMP in progress and SRE training" cover the verified PRC Software Designer (Intermediate) qualification (02 §3 ✅ CERT-SS)? | Remove until confirmed: "• PMP — in progress · Site Reliability Engineering (SRE) — formal training" |

**Library back-fill reminders (no action on the resume):** S6 closes 03 C7(b) (concurrency control); S8 titles still differ from the 02 §2 wording (TU-13); S3/S4 headcount qualifiers resolve OQ-2.3 for resume use.

---

## Resolution (2026-10-26)

| Item | Resolution |
|---|---|
| **F1** (A5 Resilience and security) | Fixed — auditor's replacement text applied verbatim: role-based permissions removed from the multi-platform clause; DR/failover drills and 99.9%+ now scoped to "the real-time payment middleware". |
| R1 (Summary 18+ years) | Default applied — "18+ years across Tier-1 banking, fintech and SaaS products, and consumer e-commerce, combining Java engineering with solution architecture." |
| R2 (settlement integration) | Default applied — "hand-off to core banking for settlement" (canonical S2 competency phrase). |
| R3 (RESTful) | Default applied — "API design". Left for Wilson: were the hub's API contracts REST? (if yes, restore and add REST to the skills inventory). |
| R4 (2016–22 stack in Platforms row) | Default applied — row kept as is (skills-line rule met); interview line: "architected/led 2016–22; current hands-on stack is Java, Spring Boot, Camel, Splunk". |
| R5 (Integrated both platforms) | Default applied, merged with canonical S2: "The payment-initiation hub hands validated payments to core banking, which executes settlement, and processes the results returned; the customer-360 platform takes daily account summaries from core banking for portfolio analysis." Left for Wilson: did your teams build the core-banking interfaces or consume existing ones? |
| R6 (Software Designer certificate) | **Overruled** per Revision Brief §1.1 — verified document in 02 §3 [CERT-SS]; Session_Confirmations explicitly lists it as fine. Education lines unchanged. |
| §3 style notes | G4 trimmed to four AWS services; V4 now four technologies (canonical); RAID, RCA, SOW, DPIA, SRE, SLIs/SLOs expanded or replaced. P2 (AI Park) and E4 (Renren, 03 verbatim) left at five technologies. |
