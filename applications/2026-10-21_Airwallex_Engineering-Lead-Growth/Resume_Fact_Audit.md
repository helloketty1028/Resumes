# Independent Fact & Quality Audit — Resume 06

**File audited:** `wilson-2026_SM_Internet_Airwallex_V1_0_0_draft.txt` (pdftotext of the rendered PDF; PDF and `.report.md` read alongside)
**Role family / lens (from file name):** SM x INT, target "Airwallex". The JD itself was not supplied to the auditor.
**Sources read:** 01_Resume_Master_Rules v1.1 · 02_Candidate_Profile v3.1 · 03_Achievement_Library v4.1 · technical-skills-inventory v2.3 · fact-check-and-open-questions v2.4 · Session_Confirmations S1–S9 `[CONF 2026-10-21]`. Not read (per brief): cards/, change log, matching analysis, resume.json, 04 and 05.
**Visual check:** all three PDF pages were rendered to PNG and viewed (80 dpi). Red text is the draft change-marking (01 §10) and must turn black at approval.

Result: **PASS 50 · REVIEW 7 · FAIL 0** (57 audited rows).

---

## 1. Claim-by-claim table

Evidence IDs: 02 § = Candidate Profile section; PA/X = 03 ID; INV = skills inventory; S# = session confirmation. "Checks" = dates / titles / scope / ownership verb / technical depth / numbers and qualifiers / confidentiality.

| # | Resume text (shortened) | Evidence | Checks | Result | Fix |
|---|---|---|---|---|---|
| H-1 | Header: Singapore PR · phone · email; headline "Engineering Lead — Consumer & Fintech Platforms \| Hands-On Design and Code Review · User Onboarding & Payments" | 02 §1 (PR since 2024, phone, email); 01 §5 (headline may name the target) | PR ✅. Headline is a target positioning, not a past title; no AI-engineer or CTO repackaging. Whether "Engineering Lead" matches the JD's wording is not verifiable (JD not supplied). | PASS | — |
| Sum-1 | "Hands-on engineering lead with 18+ years of turning product requirements into designs, delivery plans and working software for consumer and fintech platforms." | 03 §0A (18+); X-04; 02 §4 | Number ✅. Hands-on claim anchored (X-04, PA-07). | PASS | — |
| Sum-2 | "Began as an engineer and technical lead on Renren's e-commerce platform, Sohu's news content platform and Baidu's Nuomi group-buying system" | 02 §2 rows 7–9; PA-17/18/19; S1 | Renren Senior R&D Engineer, Sohu Technical Leader, Baidu project leader — all consistent. No titles or dates stated. | PASS | — |
| Sum-3 | "…then spent 2016–2022 leading technology and delivery at start-ups and scale-ups before joining a Tier-1 bank." | 02 §2 rows 3–6; 01 §5 ("head-of-technology roles 2016–2020") | Dates ✅ (AI Park Apr 2016 to GBD Jul 2022). "Scale-ups" is not on record for any of AI Park, Hengshunyuan, VV or GBD. | **REVIEW** | Safe default: "…leading technology and delivery at start-ups and technology companies before joining a Tier-1 bank." |
| Sum-4 | "Since 2022, a Vice President at UOB leading 25 onshore and offshore engineers on payment and lending platforms serving millions of accounts." | 02 §2 row 1; 03 §0A (25), X-02 | Title ✅ ("Vice President (VP2)"). 25 ✅. "Leading" is a scope verb, not "built". "Millions of accounts" ✅. | PASS | — |
| Sum-5 | "Works with product owners and business teams to turn requirements into technical solutions, backlogs and release plans" | PA-01 §9 (stakeholders), PA-01.5 (scope, roadmap, release planning) | Product owners and release planning are on record. "Backlogs" at UOB is not (backlog or sprint planning is recorded only for GBD, PA-10). | **REVIEW** | Safe default: "…turn requirements into technical solutions, roadmaps and release plans" |
| Sum-6 | "…stays close to the code — most recently by building an AI code-review service that is now in production." | PA-07 (O1+O2), X-04, S5 | "Building" fits O1. In production since May 2026 (S9). | PASS | — |
| Sum-7 | "Brings consumer-product experience across e-commerce, group-buying, local-life services and a co-founded consumer app, including user identity verification (KYC) and wallet and card payment integrations." | PA-19, PA-17, PA-11, PA-15, PA-10.2, S1 | Each element is direct experience. Payment wording is "integrations". No direct card-scheme connectivity claimed (S1 ✅). KYC is hierarchical design at GBD (O2). | PASS | — |
| Sum-8 | "Works closely with teams in India, Thailand and Indonesia across time zones, in English and Mandarin." | X-02 [CONF 2026-10-17]; 02 §1 (languages) | Locations and "collaboration, not line management" ✅. The trailing "in English and Mandarin" reads as if he works with the India, Thailand and Indonesia teams in Mandarin. The record gives English and Mandarin only as languages. | **REVIEW** | Safe default: "Works closely with teams in India, Thailand and Indonesia across time zones; professional working proficiency in English and Mandarin." |
| C-1 | Engineering Leadership: leading engineers through squad leads and EMs, 1:1s, mentoring, performance management, code-review and engineering standards, onshore/offshore | X-02; PA-03.3 | O4 wording ✅. Standards are a noun phrase here; the bullets use "contributed to" (CF-15 respected). | PASS | — |
| C-2 | Product Delivery: requirements and solution design with product owners, execution plans, backlog prioritisation and sprint planning, Agile/Scrum, release planning, MVP scoping | PA-10 §4 and §6, PA-01.5, X-02, INV §11 | Career-wide skills row. Backlog and sprint work is anchored at GBD, Agile/Scrum from scratch is ✅, MVP scoping ✅ X-02. See E-4 for the UOB-specific wording. | PASS | — |
| C-3 | Hands-On Engineering: Java, Spring Boot, Spring Cloud, Apache Camel, microservices, API design, high-concurrency systems, JVM and performance tuning, SQL | INV §1/§2/§7 | Java P, Spring Boot P, Camel P, SQL P. Spring Cloud is depth "A/P ❓" (≥ A, so usable). No Go, Flink or 10M-concurrency claims. | PASS | — |
| C-4 | Consumer Platforms: e-commerce, group-buying, local-life, news content platform, audio-learning app; hierarchical KYC and rule models | PA-17/18/19/11/15/10.2 | All direct. "200+ countries" correctly absent (CF-11). | PASS | — |
| C-5 | Payments: Alipay, WeChat Pay, UnionPay, Visa/Mastercard, Google Pay, GrabPay integrations; settlement reconciliation; payment initiation, validation and status tracking | S1; PA-01 (CF-N4) | Row-level list is within S1. Settlement reconciliation is VV and e-commerce, not the UOB hub. The hub is not claimed to settle or clear. | PASS | — |
| C-6 | Cloud & Data: AWS (API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch), Kubernetes, Docker, Kafka, Redis, Elasticsearch, MySQL, Spark | INV §3–§5 | All anchored (GBD/VV), depth ≥ A. No AWS certification implied. | PASS | — |
| C-7 | AI-Assisted Engineering: production AI code review (headless Claude Code), prompt A/B evaluation, human-in-the-loop governance, coaching teams on AI-assisted engineering | PA-07, INV §8, PA-03 §6 | Depth P. Coaching is 📄 (LIB) and usable. | PASS | — |
| A-1 | Hands-on technical leadership: review newly submitted core PRs daily, co-design solutions with engineers, own the architecture; personally built the hub's core modules — transaction initiation, concurrency control, corporate- and user-role permission matrix, status processing | S5, S6, PA-01.3, X-04 | S5 wording used. "~50 / ~20 modules" correctly not used. No "full-time" or coding-time share. Concurrency control closed by S6. "Personally built" is O1 ✅. | PASS | — |
| A-2 | Faster code review: designed and built a production AI code-review service in a regulated bank … Spring Boot … headless Claude Code agents on each PR alongside SonarQube, cutting senior engineers' review time by an estimated ~80% as human review rounds fell to 1–2 per PR | PA-07.1, PA-07.3 | O1+O2 ✅. "Estimated ~80%" qualifier kept. The 1–2 rounds figure ✅. Defect 70–80% and ramp-up 30–40% not used ✅. | PASS | — |
| A-3 | User identity and onboarding rules: designed hierarchical KYC identity verification for Golden Bridge's multi-tenant SaaS platform after benchmarking competitor apps, with rule models for authentication levels and bonus eligibility | PA-10.2, PA-10 §4 | O2 verb ✅. "200+ countries" dropped ✅. Business described only as multi-tenant SaaS (S9) ✅. | PASS | — |
| A-4 | Payments across wallets and cards: designed and coded Baidu Nuomi's payment-gateway integration with Alipay, WeChat Pay and UnionPay; architected VV-Life's payment subsystem, integrating UnionPay, Visa/Mastercard, Google Pay and GrabPay with settlement reconciliation | S1 | Baidu "designed and coded" = O1+O2 ✅. VV "architected" = O2 ✅. WeChat Pay under Baidu, not Renren ✅. No direct card-scheme claim ✅. | PASS | — |
| A-5 | Consumer product from 0 to 1: co-founded an audio-learning platform and owned product, architecture and technical delivery from market research to production, peak ~100k DAU | PA-15.1 | Verbatim safe wording; "~" kept; single source [R22] accepted in the metrics bank. | PASS | — |
| A-6 | Engineering teams at scale: led VV's 140-person technology organisation (total headcount) and, at Golden Bridge, a 40-person project team (total headcount), introducing Agile/Scrum from scratch and CI on Jenkins and Amazon ECR | S3, S4, PA-10.3 | Verb "led", not "built" ✅. Both "(total headcount)" qualifiers present ✅. Agile and CI are GBD facts and are attached to GBD ✅. | PASS | — |
| A-7 | Mission-critical migration: owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration …; phased coexistence took MX-rich messaging live in May and August 2025, ahead of SWIFT's November 2025 deadline, and was retired in August 2026 with no service interruption | PA-01.1, PA-01 §7 | O3 "owned" ✅. Dates ✅. Matches the PA-01.1 safe wording. | PASS | — |
| U-0 | UOB header: Oct 2022 – Present; "Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations"; "Technology leader for two mission-critical platform lines in a MAS-regulated Tier-1 bank…" | 02 §2 row 1, §6.1 | Title and dates exact. No internal system names. | PASS | — |
| E-1 | Led end-to-end design of a payment-initiation hub (Java, Spring Boot, Apache Camel) — API contracts, orchestration, validation, enrichment and status tracking — integrating channels, reference data and vendor and third-party banking systems | PA-01.2 | O2 ✅. Generic "vendor" only, no vendor names. 3 technologies. | PASS | — |
| E-2 | Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking | PA-01.4 | No figure ✅ (none on record). | PASS | — |
| E-3 | Led the 10-engineer backend team of a regional customer-360 platform in production since 2022: designed the customer data models and personally built its data-analysis module and Spring Batch scheduled jobs | PA-05.1/05.2/05.3 | Team of 10 ✅ (sub-total, scope not outcome). "In production since 2022" ✅. The 2022 launch is not claimed as his (C5 open). "SCV-CCD" not used ✅. Spring Batch is P ✅. | PASS | — |
| E-4 | Work with product owners on backlog prioritisation and sprint planning, and run Agile delivery governance — change control, issue escalation and KPI-based progress reporting in Jira and Confluence | PA-01 §3/§6/§9, PA-03.1, PA-10 §4 | Agile governance, change control and Jira/Confluence ✅ (PA-01 §6/§3). "Backlog prioritisation and sprint planning" and "issue escalation" are not recorded for UOB (sprint work is recorded only at GBD). | **REVIEW** | Safe default: "Work with product owners on scope, roadmap and release planning, and run Agile delivery governance — change control, RAID tracking and KPI-based status reporting in Jira and Confluence." |
| E-5 | When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept | X-02 | Verbatim safe wording. | PASS | — |
| E-6 | Established delivery KPIs — deployment frequency, MTTR, incident trend, change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate); contributed to bank-wide SDLC, coding and code-review standards | PA-03.1/03.2/03.3 | "Established" is in the PA-03.1 safe wording. "Contributed to" locked verb ✅. 99% matches the metrics bank. | PASS | — |
| E-7 | Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, RCA and post-incident reports; with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring | X-06, PA-02.3, CF-N2/N3 | No MAS-reporting claim (safer than X-06). SRE framing matches CF-N3. | PASS | — |
| E-8 | Lead two onshore/offshore teams through squad leads and engineering managers, with 1:1s, mentoring and performance management; coach teams on AI-assisted engineering practices and tooling | X-02, PA-03 §6 | O4 wording ✅. | PASS | — |
| E-9 | Took the AI code-review service live in May 2026 after formal architecture and risk approval: the AI advises but never approves or merges, and prompt A/B testing keeps improving review quality | S9, PA-07.2, PA-07.4 | Date ✅ and approval ✅. Governance rule ✅. "Keeps improving" is a mild present-tense extension of the 📄 PA-07.4 "improved review quality". | PASS | — |
| E-10 | Work with infrastructure, operations, compliance and architecture teams, and closely with teams in India, Thailand and Indonesia across time zones | PA-01 §9, PA-02 §9, X-02 | Facts ✅. The India/Thailand/Indonesia clause repeats Sum-8 (see X-1). | PASS | — |
| G-0 | Golden Bridge Drive (SG) Pte. Ltd. · Nov 2020 – Jul 2022 · Project Manager & Architect | 02 §2 row 3 | Exact. | PASS | — |
| G-1 | Architected and delivered, from 0 to 1, a multi-tenant SaaS platform for online-game businesses on AWS — KYC, bonus incentives, VIP tiers, analytics and multi-channel payments — on Spring Cloud and Kubernetes | PA-10.1, S9 | Verbatim safe wording. | PASS | — |
| G-2 | Ran hybrid delivery — Waterfall for scope, budget and milestones; Agile sprints for execution, backlog tracking and iterative delivery — and owned delivery budget, capacity and launch readiness | PA-10 §4 | The record says "Waterfall for scope and budget, Agile sprints". "Milestones", "backlog tracking" and "iterative delivery" are embellishments. Budget, capacity and launch readiness ✅ (CONF). | **REVIEW** | Safe default: "Ran hybrid delivery — Waterfall for scope and budget, Agile sprints for execution — and owned delivery budget, capacity and launch readiness." |
| G-3 | Architected the AWS deployment (API Gateway, EC2/ECS, RDS, DynamoDB) and applied DPIA, API and database encryption and credential management; led data migration | INV §5, X-01 | Depth A ✅. X-01 covers GBD ✅. | PASS | — |
| V-0 | VV Technology Pte. Ltd. · Apr 2019 – Jun 2020 · Head of Technical Centre; "VV-Life: a local-life services platform connecting offline merchants … through data" | 02 §2 row 4, S8, PA-11 §1 | Title per S8 ✅. Dates ✅. Description drops "big data, AI and blockchain" ✅. | PASS | — |
| V-1 | Took part in product-strategy planning and delivered the first VV-Life release in 2019, including the payment subsystem's transaction, management and reconciliation modules | PA-11.2, PA-11 §4 | Verbatim; "took part" is the right level. | PASS | — |
| V-2 | Built the microservices platform (Spring Cloud, Kubernetes, Redis, Elasticsearch) from scratch, owning technology selection and the technology budget | PA-11.1 | "Built" matches the library's own safe wording (framework O1/O2). The 140-person organisation is not repeated here ✅. | PASS | — |
| V-3 | Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching … millisecond level | PA-11.4 | Verbatim; no % figure ✅. | PASS | — |
| V-4 | Led the big-data team on Flume, Hive, MapReduce, Spark Streaming and Spark SQL, providing data analysis that supported business decisions | PA-12 (R22 version only), INV §3 | Stack and "led" ✅; Flink correctly absent (CF-07). The outcome clause "that supported business decisions" is not in 03 PA-12. | **REVIEW** | Safe default (PA-12 wording): "Led the big-data team and built VV's data-analysis platform from scratch on Flume, Hive, MapReduce, Spark Streaming and Spark SQL." |
| V-5 | Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans | PA-11.3, PA-11.5 | Verbatim. | PASS | — |
| Hy-0 | Hengshunyuan Information Technology Co., Ltd. · China · Oct 2017 – Sep 2019 · Co-founder; "Own start-up: an audio-learning platform…" | 02 §2 row 5, D-10 | Dates per D-10 (overlap not annotated) ✅. Title ✅. | PASS | — |
| Hy-1 | Brought ~1,500 licensed audio titles and albums onto the platform at launch, on a Spring Cloud microservices stack with a MySQL cluster, Redis, Kafka and ELK | PA-15.2, PA-15 §3 | "~" kept. Cloud vendor omitted (CF-08 open) ✅. Names 5 technologies (soft limit is 3–4, style only). | PASS | — |
| AP-0 | AI Park · China · Apr 2016 – Sep 2017 · VP of Technical Department | 02 §2 row 6, S8 | Title per S8 ✅. Dates per [CONF] ✅. | PASS | — |
| AP-1 | Led architecture, delivery, budget and the technical team for a smart-parking IoT platform … | PA-16.1 | Verbatim. No 1,000+ lots or 10M DAU ✅. | PASS | — |
| AP-2 | Brought Spring Cloud microservices into the architecture, with Kafka … achieving millisecond-level service processing | PA-16.4 | Verbatim. | PASS | — |
| Er-1 | Baidu — Technical Specialist, Nuomi group-buying e-commerce platform (May 2014 – Dec 2014, China): as project leader, re-architected the merchant-side order system on Dubbo microservices, delivered two months ahead of plan, leading the web front-end, CMS and QA teams | 02 §2 row 7, PA-17.1, S1 | Title ✅. Month precision from [R22] 📄 (CF-12 "2014 only" respected). No 5–10M QPS ✅. | PASS | — |
| Er-2 | Sohu.com — Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014): led the fifth-generation CMS re-architecture (SSH to Spring MVC; memcached to Redis cluster) | 02 §2 row 8, PA-18.1 | Dates and title ✅. | PASS | — |
| Er-3 | Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012): developed Renren's shopping website, Renren Mall and CRM, and designed and coded Renren Mall's payment integration with Alipay and UnionPay | 02 §2 row 9, PA-19, S1 | Alipay and UnionPay only; WeChat Pay correctly absent (S1). | PASS | — |
| Ed-1 | Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 | ✅; no degree type asserted (FU-4). | PASS | — |
| Ed-2 | Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 | ✅. | PASS | — |
| Ed-3 | Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006) · PMP — in progress · SRE — formal training | 02 §3, CF-N5, Session note | Verified PRC certificate allowed; "in progress" and "training" wording correct; no IDs or file numbers. | PASS | — |
| Ed-4 | Languages: English and Mandarin (professional working proficiency in both) | 02 §1 | ✅. | PASS | — |
| X-1 | Cross-cutting repetition (01 §6 Merging) | 01 §6 | The India/Thailand/Indonesia collaboration appears twice (Sum-8 and E-10). AI code review appears in the Summary, a competency row, A-2 and E-9; A-2 carries the result, E-9 the governance and go-live, so these differ in content. | **REVIEW** | Safe default: delete the trailing clause in E-10, leaving "Work with infrastructure, operations, compliance and architecture teams." Keep the other AI-review mentions. |

---

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to 03/02 ID; no ❓/⚠️/⛔ content outside permitted parts | Passed with exceptions | Partial traces flagged as REVIEW in Sum-5, E-4, G-2 and V-4. No ⛔ content found (no 10M DAU, 200+, Flink, Pureland, chatbot, forecasting, 70–80% defects, 30–40% ramp-up, 1,000+ lots, 5–10M QPS). |
| Dates and titles match 02 §2 / S8 exactly; no "CTO" / "Chief Architect" | Passed | All six employer lines match. VV "Head of Technical Centre" and AI Park "VP of Technical Department" follow S8 (supersedes the 02 §2 "Development" wording, back-fill TU-13 pending). Baidu months are from [R22] (02 §2 note). Grep confirms no CTO or Chief Architect. |
| Every number matches 03 §0A (or S1–S9), qualifiers kept | Passed | 18+, 25, 10, ~80% "estimated", 1–2 rounds, ~100k, ~1,500, 140 and 40 "(total headcount)", 99% gate, two months ahead, May/Aug 2025, Aug 2026, May 2026. |
| Verbs match ownership level | Passed | O1 "built/coded" only where S1, S5, S6 or PA-01.3, 05.2, 07 give O1. 140 and 40 use "led". PA-11.1 "built" is the library's own wording (note on V-2). |
| Skills anchored (P or A for Summary and bullets) | Passed | Spring Cloud depth is "A/P ❓" in the inventory but ≥ A. No Go, Flink, GCP, RAG, LangChain or certifications beyond 02 §3. |
| No CEW / SCV-CCD / vendor names / internal numbers | Passed | Grep clean (only the generic word "vendor"). |
| Headline and Summary fit chosen family × lens (02 §7, 05 §2) | Passed, not fully verified | Headline reads as SM × INT. 05 and the JD were not supplied, so the match to the JD's own title wording is not verified. |
| Summary narrative; no stacked repetition | Passed with exceptions | Narrative, 3 paragraphs. Minor duplication flagged as X-1. |
| British spelling consistent; JD titles quoted as written | Passed (spelling) / Not performed (JD titles) | organisation, prioritisation, containerised, licensed all consistent. JD not supplied. |
| Layout per 04 | Not performed | 04 is outside the audit inputs. The render report says "Layout OK: True" and the pages look consistent with it. |
| ≤ 3 pages; page numbers; no orphaned headings | Passed (visually verified) | 3 pages. Footer "Page n of 3" on every page. "PROFESSIONAL EXPERIENCE" opens page 2. No heading stranded at a page bottom. |
| Text extractable; no text boxes or images of text; PDF renders | Passed | pdftotext returns full text, `pdfimages` lists no images, fonts embedded (Carlito). Docx structure (text boxes) was not inspected; the competency block is a table. |
| File name per §10 | Passed | `wilson-2026_SM_Internet_Airwallex_V1_0_0` matches `[Family]_[Lens]_[Target]_V…` (OQ-R3 on the lens segment is still open). |
| Three-dimension review delivered separately; change log listing every change | Not performed | Out of audit scope (those files were deliberately not read). |

---

## 3. Document checks (render report + visual)

| Check | Result |
|---|---|
| Pages | 3 (limit 3). Page 3 is about 40% full. |
| Page 1 = header + summary + competencies + achievements | Yes (verified visually). Page 2 starts with Professional Experience. |
| Summary | 3 paragraphs, 157 words. Longest is 4 lines (limit 4). |
| Bullets | 31 bullets. Five at 3 lines (A-1, A-2, A-7, E-9, Baidu line), which is 16%, within 1 in 5. None over 3 lines. |
| Competency rows | All 2 lines. |
| Line-limit flags / lint hits (report) | None. |
| Page numbers | Present ("Page n of 3"). |
| Red runs | 47/97 runs in red (draft change-marking, 01 §10). Must be black at final. |
| Minor | Header shows "Singapore" twice ("Singapore PR … Singapore"). Hengshunyuan bullet names five technologies against the 3–4 style guide. |

---

## 4. Summary

**PASS 50 · REVIEW 7 · FAIL 0**

### Required fixes
None. There are no FAIL rows, and nothing is stated above the record.

### For Wilson to decide (REVIEW)
1. **Sum-3: "start-ups and scale-ups".** Is "scale-ups" defensible for AI Park, VV or GBD? Default: change to "start-ups and technology companies".
2. **Sum-5 and E-4: UOB "backlog prioritisation and sprint planning" / "issue escalation".** Do you personally run backlog prioritisation and sprint planning with product owners at UOB? Backlog and sprint work is on record only for GBD. Default: use the E-4 and Sum-5 replacement text in the table (scope, roadmap, release planning, RAID tracking, KPI status reporting).
3. **Sum-8: "…across time zones, in English and Mandarin."** Does it imply you work with the India, Thailand and Indonesia teams in Mandarin? Default: separate the two statements (replacement text in the table).
4. **G-2: GBD hybrid delivery detail.** Are "milestones", "backlog tracking" and "iterative delivery" true for GBD? The library has only "Waterfall for scope and budget, Agile sprints". Default: trim to the library wording.
5. **V-4: VV big-data outcome "that supported business decisions".** Is there evidence for this outcome? It is not in PA-12. Default: use the PA-12 safe wording ("Led the big-data team and built … from scratch on Flume, Hive, MapReduce, Spark Streaming and Spark SQL").
6. **X-1: duplicated India/Thailand/Indonesia statement** in the Summary and the last UOB bullet. Default: delete the trailing clause in E-10.

(Items 2 and 6 each cover more than one row: Sum-5 + E-4, and X-1 alone. Seven REVIEW rows in total: Sum-3, Sum-5, Sum-8, E-4, G-2, V-4, X-1.)

## Resolution (2026-10-26)

**FAIL:** none.

| REVIEW | Resolution |
|---|---|
| Sum-3 "start-ups and scale-ups" | Default applied: "start-ups and technology companies". |
| Sum-5 "backlogs" | Default applied: "technical solutions, roadmaps and release plans". The same change was carried into the Product Delivery competency row ("roadmaps, Agile/Scrum sprints"), because 03 and the skills inventory hold no backlog evidence. |
| Sum-8 languages | Default applied: "…across time zones; professional working proficiency in English and Mandarin." |
| E-4 UOB backlog/sprint planning, issue escalation | Default applied verbatim. Left for Wilson: do you personally run backlog prioritisation and sprint planning with product owners at UOB? If yes, the JD-responsibility-6 keyword can be restored. |
| G-2 GBD hybrid delivery | Default applied: "Waterfall for scope and budget, Agile sprints for execution". |
| V-4 VV big-data outcome | Default (PA-12 wording) considered, then the bullet was deleted: the cold-read recommended cutting it for this Growth role, and the PA-12 wording names five technologies. Nothing unsupported remains. |
| X-1 India/Thailand/Indonesia repeat | Default applied: E-10 now reads "Work with infrastructure, operations, compliance and architecture teams." |

**Other audit notes:** Hengshunyuan bullet trimmed to four technologies (§3 minor). The header "Singapore" duplication is fixed by the renderer (brief §3) and was not changed. The "Software Designer (Intermediate)" certificate stays exactly as written: it is a verified document in 02 §3, and the cold-read's suggestion to cut it is overruled by Revision Brief §1.1.

Re-render: Layout OK: True, 3 pages, 5/30 bullets at 3 lines, 0 lint hits.
