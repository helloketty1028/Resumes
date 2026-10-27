# Resume Fact & Quality Audit — 03 (SM × Internet · Stripe)

**File audited:** `wilson-2026_SM_Internet_Stripe_V1_0_0_draft.txt` (pdftotext of the rendered PDF), cross-checked against `…_draft.pdf` (3 pages, A4, viewed page by page as images), `…_draft.report.md` / `.report.json` and the unpacked `…_draft.docx` (structure only).
**Auditor:** independent; did not write the draft and was not given the drafting notes. The resume was not used as evidence for its own claims.
**Date:** 2026-10-21

**Sources read (version):**
- `01_Resume_Master_Rules.md` v1.1 · 2026-10-20
- `02_Candidate_Profile.md` v3.1 · 2026-10-17
- `03_Achievement_Library.md` v4.1 · 2026-10-17
- `technical-skills-inventory.md` v2.3 · 2026-10-17
- `fact-check-and-open-questions.md` v2.4 · 2026-10-20
- `Session_Confirmations.md` S1–S9 (2026-10-20 / 2026-10-21) → cited as `[CONF 2026-10-21]`
- `Audit_Brief.md`

**Not read (by instruction or outside the brief's input list):** `Batch_Positioning.md`, the draft's JD_Matching_Analysis / Resume_Change_Log / resume.json, `Drafting_Brief.md`, the LIB/TPL/approved files in `brief/`, `04_Resume_Layout_Spec.md`, `05_JD_Keyword_and_Matching_Rules.md`, and the Stripe JD. As a result, **JD fit was not assessed** and layout was checked against the brief's document checks, not against 04 directly.

---

## 1. Claim-by-claim audit

Abbreviations: S# = Session_Confirmations item; 📄/✅/🔶 = status in the cited source; O1–O5 = ownership level (01 §4).

### Header and Professional Summary

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 1 | "WILSON" | 02 §1 (D-11) | Name only, no surname ✅ | PASS | — |
| 2 | "Singapore PR \| +65 8655 9547 \| Skyzhang1028@gmail.com \| Singapore" | 02 §1 | PR since 2024 ✅ · phone ✅ · email ✅ | PASS | Cosmetic: 02 records the address in lower case (`skyzhang1028@…`); the capital S does no harm. |
| 3 | Headline "Engineering Manager — Payment Platforms & Production Systems \| Hands-On Java · Platform Teams · Cross-Time-Zone Delivery" | 01 §5 (headline may name the target role); skills Java = P; 03 X-02 (India/Thailand/Indonesia; onshore/offshore) | Target-role naming, not a past title ✅ · no CTO ✅ | PASS | — |
| 4 | "Hands-on engineering manager for payment platforms, with 18+ years in technology." | 03 §0A "18+ years"; X-04 / S5 (hands-on); X-02 (leads through squad leads/EMs) | Number ✅ · descriptor, not a title claim 🔶 | PASS | — |
| 5 | "Started as a software engineer and technical lead on Renren's e-commerce platform, Sohu's news CMS and Baidu's Nuomi group-buying system (2008–2014)" | 02 §2 rows 7–9; PA-17, PA-18, PA-19 | Titles (Senior R&D Engineer / Technical Leader / Technical Specialist + project leader) fairly summarised ✅ · dates ✅ | PASS | — |
| 6 | "then led engineering teams and technology organisations through 0-to-1 platform builds at start-ups and scale-ups (2016–2022)" | 02 §4 career arc ("Head of Technology (start-ups/scale-ups) 2016–22"); PA-10.1, PA-11.1, PA-15.1, PA-16.1 | Dates ✅ · no CTO title ✅ | PASS | — |
| 7 | "Since 2022, a Vice President at UOB, a Tier-1 bank, leading 25 onshore and offshore engineers in two platform teams on payment and lending platforms that serve millions of accounts." | 02 §2 row 1; 03 §0A row 2; X-02 bullet 1 | 25 ✅ (team size as scope, not outcome; not paired with "built") ✅ · millions of accounts ✅ | PASS | Team-to-line mapping (C6) is still open, but X-02 itself places the two teams "across two platform lines (cross-border payments, retail unsecured lending)". |
| 8 | "Stays hands-on in code review, solution design and core-module coding" | X-04; S5 | No coding-time %, no "full-time engineer" ✅ | PASS | — |
| 9 | "works closely with product, operations and compliance partners, and leads production operations, from incident response to service-level objectives (SLOs)" | PA-01 §9; X-06; PA-02.3; CF-N3 | Stakeholders on record ✅ · no SRE team claimed ✅ | PASS | — |
| 10 | "Designs and delivers extensible platforms that other teams and businesses depend on — payment initiation, customer data and multi-tenant SaaS" | PA-01.2 (O2) + PA-01.5 (O3); PA-05.1; PA-10.1 | Verbs O2+O3 ✅ · "extensible … depend on" is interpretation 🔶 (channels, business lines and SaaS tenants do consume them) | PASS | C5 (who led the 2022 customer-360 launch) is not claimed here ✅. |
| 11 | "and has led VV Technology's 140-person technology organisation (total headcount)" | S3 | Safe wording and qualifier kept ✅ · not "built" ✅ | PASS | — |
| 12 | "Payments experience spans cross-border bank payments, lending collections and wallet and card integrations on consumer platforms." | PA-01; PA-04.1; S1 | No direct card-scheme connectivity claimed ✅ | PASS | — |

### Core Competencies

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 13 | Engineering Management — "Leading through squad leads and engineering managers, 1:1s, mentoring, performance management, coaching, engineering standards, onshore/offshore teams" | X-02; PA-03 §6 (coaching); PA-03.3 (contributed, O5) + PA-11.3 (VV code standards) | ✅ | PASS | — |
| 14 | Hands-On Engineering — "Java, Spring Boot, **Spring Cloud**, Apache Camel, concurrency control, JVM tuning, SQL, code review, solution design, production troubleshooting" | Skills §1 Java P; §2 Spring Boot P, Camel P, **Spring Cloud A/P ❓**; SQL P (CF-N6); S6; X-04 | All anchored, but Spring Cloud's hands-on depth is unconfirmed, and the row label claims hands-on | **REVIEW** | See R1. |
| 15 | Production Rigour — "P1–P3 incident response and root-cause analysis (RCA), SLIs/SLOs, disaster-recovery (DR) and failover drills, Splunk monitoring, CI/CD quality gates" | X-06; PA-02.1–02.3; PA-03.2; skills Splunk A/P | ✅ | PASS | — |
| 16 | Platform Engineering — "Extensible platforms used by other teams, API design, microservices, event-driven integration, multi-tenant SaaS, high-concurrency systems" | Skills §7; PA-01.2 (API contracts) | ✅ | PASS | — |
| 17 | Payments — "Payment initiation and status tracking, **integration with core-banking settlement**, reconciliation, lending collections, ISO 20022 messaging, wallet and card payment integrations" | S2; CF-N4 (hub does **not** settle or clear); skills §9 (reconciliation VV; never claim core banking); S1; PA-04 | Every item anchored. The compressed phrase "core-banking settlement" can read as settlement-system expertise, which CF-N4 and the skills "never claim core banking" rule bound | **REVIEW** | See R2. |
| 18 | Developer Productivity & AI — "Production AI code review on headless Claude Code agents, prompt A/B evaluation, AgentOps/LLMOps practice, human-in-the-loop governance, delivery KPIs" | PA-07.1–07.4; skills §8 (P); PA-03.1 | ✅ · not positioned as an "AI engineer" ✅ | PASS | — |
| 19 | Cloud & Data — "AWS, Kubernetes, Docker, Kafka, Redis, Elasticsearch, MySQL, Spark" | Skills §3–§5 (all anchored, depth A to P) | Skills line, so the anchor is enough ✅ | PASS | All of these are 2016–2022 evidence (GBD, VV, AI Park, Hengshunyuan), not UOB. Be ready to say so at interview. |

### Selected Achievements

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 20 | Platform for other teams: "Led end-to-end design of a payment-initiation hub that the bank's digital and branch channels use — API contracts, orchestration, validation and status tracking — integrated with core banking, which executes settlement, and with vendor and third-party banking systems." | PA-01.2 📄; S2; CF-N4 | Verb O2 ✅ · hub does not settle (wording correct) ✅ · no internal name ✅ | PASS | — |
| 21 | Leading and developing engineers: "Lead both platform teams through squad leads and engineering managers — 1:1s, mentoring and performance management — and work closely with teams in India, Thailand and Indonesia across time zones." | X-02 bullets 2 and 5; D-09 | Collaboration, not line management ✅ · no US teams ✅ | PASS | — |
| 22 | Hands-on technical leadership: "Review newly submitted core pull requests daily, co-design solutions with engineers and resolve production issues; personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results…" | S5; S6 (closes C7 b); PA-01.3 ✅ | O1 "personally built" ✅ · "~50/~20 modules" not used ✅ · no coding % ✅ | PASS | — |
| 23 | Operational rigour: "Planned a phased ISO 20022 (SWIFT MT-to-MX) migration of cross-border payments, running old and new formats in parallel until August 2026 with no service interruption; personally led DR drills, sustaining 99.9%+ availability." | PA-01.1 (Aug 2026 ✅, no interruption 📄); PA-02.1; §0A rows 3 and 5 | "Planned" is an O3 verb ✅ · numbers match §0A ✅ · 2 numbers ✅ | PASS | Readability: "MT-to-MX" is not explained (01 §6A names ISO 20022 MT→MX as an acronym to expand). |
| 24 | 0-to-1 extensible platforms: "Architected and delivered a 0-to-1 multi-tenant SaaS platform for online-game businesses on AWS; at VV, designed Spring Cloud microservices with Kafka and caching that brought service response times to the millisecond level." | PA-10.1 📄; S9 (GBD wording); PA-11.4 ✅ | Verbs O2/O3 ✅ · business described only as approved ✅ · no % figure ✅ | PASS | Clarity: the first clause does not name the employer (Golden Bridge), unlike "at VV" in the second. |
| 25 | Developer productivity with AI: "Designed and built a production AI code-review service in which headless Claude Code agents review each pull request. Live since May 2026 after formal architecture and risk approval, it advises but never approves or merges, and has cut senior engineers' review time by an estimated ~80%." | PA-07.1 (O1+O2); S9; PA-07.2; PA-07.3 | Estimate labelled ("an estimated ~80%") ✅ · go-live date ✅ | PASS | — |
| 26 | Cards and wallets: "Designed and coded payment integrations at Baidu Nuomi (Alipay, WeChat Pay, UnionPay) and Renren Mall (Alipay, UnionPay); at VV, designed a subsystem that integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments." | S1 | O1+O2 at Renren/Baidu ✅ · O2 "designed" at VV ✅ · no WeChat Pay under Renren ✅ · no direct card-scheme claim ✅ | PASS | — |

### Professional Experience — UOB

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 27 | "United Overseas Bank (UOB) \| Singapore · Oct 2022 – Present · Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | Title and dates exact ✅ | PASS | — |
| 28 | "Technology leader for two mission-critical platform lines in a MAS-regulated Tier-1 bank — cross-border payments (SWIFT ISO 20022 messaging) and retail unsecured lending." | 02 §6.1 | ✅ | PASS | — |
| 29 | "Lead the 10-engineer backend team of a regional customer-360 platform (live since 2022) that takes daily account summaries from core banking for portfolio analysis and serves APIs to several business lines." | PA-05.3; PA-05.1; S2; §0A | 10 ✅ · "live since 2022" does not claim the launch (C5) ✅ · internal name not used ✅ | PASS | — |
| 30 | "Own technology for retail unsecured-lending servicing — payment initiation, validation and lifecycle tracking — and post-disbursement collections across credit-card and unsecured-loan portfolios." | PA-04.1 (verbatim) | ✅ | PASS | — |
| 31 | "Reduced the payment hub's end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking." | PA-01.4 📄 (no figure) | No invented figure ✅ | PASS | — |
| 32 | "Owned end-to-end delivery of the ISO 20022 programme with the 15-engineer hub team — scope, roadmap, risks and dependencies, release planning and production rollout; upgrades now ship every 2–3 months." | PA-01.5; §0A rows 3 and 13 | O3 verb ✅ · 15 is scope ✅ · cadence ✅ | PASS | — |
| 33 | "Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, RCA and post-incident reports; with no separate reliability team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring." | X-06; PA-02.3; CF-N3 | No MAS-reporting overclaim ✅ | PASS | — |
| 34 | "Established delivery KPIs — deployment frequency, MTTR, incident trend and change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing) and SIT/UAT sign-off for every release; contributed to bank-wide SDLC, coding and code-review standards." | PA-03.1 📄 ("Established" is the library's own wording); PA-03.2; PA-03.3 (locked "contributed to"); §0A | Locked verb kept ✅ · 99% matches §0A ✅ | PASS | Interview risk: PA-03 §8 asks whether 99% is new-code or overall coverage. Be ready to answer. |
| 35 | "When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept." | X-02 (verbatim) | ✅ | PASS | — |
| 36 | "Act as the primary interface between business stakeholders, product owners, operations, compliance, architects and engineering managers; present status, risks and decisions to senior management and steering committees." | PA-01 §9; PA-01.5; 03 §5.3 U29 → PA-01 §9, X-02 | Stakeholder levels on record ✅ · no Board/C-suite ✅ | PASS | 03 has no safe-wording row for "primary interface" (it comes from [LIB] U29). Acceptable, but the wording is not library-verbatim. |
| 37 | "Hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and chair governance of four IT service vendors." | X-02; X-05; CF-N1 | No vendor names ✅ · buyer-side authority only (S7) ✅ | PASS | — |
| 38 | "Took the AI code-review service into production: briefed senior management on the case and the governance model, and improved review quality through prompt A/B testing and AgentOps/LLMOps practices; coach teams on AI-assisted engineering." | PA-07 §4 (briefing); PA-07.2; PA-07.4 📄; PA-03 §6; S9 | ✅ | PASS | Complements row 25 without repeating it. |
| 39 | "Personally built an AI agent (April 2026) that generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents, removing a recurring manual reconciliation task." | PA-08 (O1, Apr 2026); S9 | ✅ · no time-saved figure invented ✅ | PASS | — |

### Professional Experience — earlier roles

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 40 | "Golden Bridge Drive (SG) Pte. Ltd. \| Singapore · Nov 2020 – Jul 2022 · Project Manager & Architect" | 02 §2 row 3 | ✅ | PASS | — |
| 41 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness for the multi-tenant SaaS platform." | S4; PA-10.3 | Qualifier kept ✅ · "Led", not "built" (HR-9) ✅ | PASS | — |
| 42 | "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution." | PA-10.2 (without "200+") | CF-11 avoided ✅ | PASS | — |
| 43 | "Architected the AWS deployment (API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch) and applied DPIA, API and database encryption and credential management; led data migration." | Skills §5 (GBD AWS services, depth A); skills §10 DPIA; X-01 | Facts ✅ · "Architected" matches depth A ✅ · **six named AWS services**, above the 01 §6 guideline of 3–4 technologies per bullet (a 🔶 limit) | **REVIEW** | See R3. |
| 44 | "VV Technology Pte. Ltd. \| Singapore · Apr 2019 – Jun 2020 · Head of Technical Centre" | 02 §2 row 4 (dates); **S8** (title, supersedes the 02 "Development" wording) | Dates ✅ · title per S8 ✅ | PASS | CF-16 risk remains: the title must match the employment letter at background check. |
| 45 | "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services — through data." | PA-11 §1 | Drops "AI and blockchain" (conservative) ✅ | PASS | — |
| 46 | "Built VV's microservices platform from scratch, owning technology selection and the technology budget." | PA-11.1 (the {140} slot correctly dropped) | "Built" matches the library wording ✅ | PASS | — |
| 47 | "Took part in product-strategy planning and delivered the first VV-Life release in 2019, including the payment subsystem's transaction, management and reconciliation modules." | PA-11 §4; PA-11.2 | ✅ | PASS | — |
| 48 | "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance." | PA-13 (verbatim) | Facts ✅ · internal name "GMS" not used ✅ · **five named technologies**, above the 3–4 guideline | **REVIEW** | See R3 (same question). |
| 49 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans." | PA-11.3; PA-11.5; CF-N8 | ✅ | PASS | — |
| 50 | "Hengshunyuan Information Technology Co., Ltd. \| China · Oct 2017 – Sep 2019 · Co-founder" | 02 §2 row 5; D-10 | ✅ (overlap with VV not annotated, per D-10) | PASS | — |
| 51 | "Owned product, architecture and technical delivery of an audio-learning platform for workplace and early-childhood content, from market research to production, reaching a peak of ~100k daily active users." | PA-15.1; §0A | "~" kept ✅ | PASS | — |
| 52 | "AI Park \| China · Apr 2016 – Sep 2017 · VP of Technical Department" | 02 §2 row 6 (Apr 2016 [CONF], CF-06); **S8** (title) | ✅ | PASS | Same CF-16 background-check note as row 44. |
| 53 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform connecting car parks to the cloud for automated management, online payment and recommendations." | PA-16.1 | No "1,000+ car parks" and no "10M DAU" ✅ | PASS | — |
| 54 | "Led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing, and launched pilots in Shijiazhuang (2016), Handan (2017) and Beijing Chaoyang (2017)." | PA-16.2 (verbatim); S7 | ✅ | PASS | — |
| 55 | Baidu — "Technical Specialist, Nuomi group-buying e-commerce platform (May 2014 – Dec 2014, China): As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan, leading the web front-end, CMS development and QA teams." | 02 §2 row 7 (CF-12; months 📄 R22); PA-17.1 | No "5–10M QPS" ✅ | PASS | — |
| 56 | Sohu — "Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014, China): Led the CMS re-architecture (SSH to Spring MVC; memcached to Redis cluster) and delivered its OpenAPI messaging platform." | 02 §2 row 8; PA-18.1 | ✅ | PASS | — |
| 57 | Renren — "Senior R&D Engineer (Jul 2008 – Mar 2012, China): Developed Renren's shopping website, Renren Mall and CRM." | 02 §2 row 9; PA-19 | ✅ | PASS | — |

### Education, Certifications and Languages

| # | Resume text | Evidence | Checks | Verdict | Note / fix |
|---|---|---|---|---|---|
| 58 | "Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008)" | 02 §3; CF-02 | Discipline ✅ · generic "Master's degree" is the FU-4 fallback ✅ | PASS | — |
| 59 | "Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004)" | 02 §3; CF-01 | ✅ | PASS | — |
| 60 | "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006)" | 02 §3 ✅ [CERT-SS] (issued 2006-09-30) **vs** Session_Confirmations "Held / not usable: … any certification other than 'PMP — in progress' and SRE formal training" | The two sources conflict. Not resolved by the auditor | **REVIEW** | See R4. |
| 61 | "PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3; CF-N5; S-held line | Not "certified" ✅ · training, not certification ✅ | PASS | — |
| 62 | "Languages: English and Mandarin (professional working proficiency in both)" | 02 §1 | ✅ | PASS | — |

---

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to an ID in 03 (or a 02 section); no ❓/⚠️/⛔ content | **Passed** | All 62 claims trace to 02/03/skills/S1–S9. The VV and AI Park titles are ⚠️ in 02 (CF-16) but were superseded by S8. Held items are absent: 10M DAU, 10M HTTP, 5–10M QPS, 1,000+ car parks, 10+ domains, 100+ org, 200+, Flink, chatbot, forecasting, defect %, ramp-up %, Pureland, MEPS+, Board/C-suite. |
| Dates and titles match 02 §2 exactly; no "CTO"/"Chief Architect" | **Passed** | UOB, GBD, Hengshunyuan, Baidu, Sohu and Renren match 02 §2. VV and AI Park titles follow S8 [CONF 2026-10-21], with back-fill to 02 pending (TU-13). No CTO or Chief Architect (grep: 0 hits). |
| Every number matches the 03 Metrics Bank with qualifiers | **Passed** | 18+ · 25 · 10 · 15 · 140 (total headcount, S3) · 40 (total headcount, S4) · 99.9%+ · estimated ~80% · 99% · every 2–3 months · ~100k · two months ahead · dates Aug 2026, May 2026, Apr 2026 (all [CONF]). No orphan numbers. |
| Verbs match ownership level (01 §4) | **Passed** | O1 "personally built/coded" only where S1/S6/PA-01.3/PA-07/PA-08 support it; O2 "designed/architected" for VV and GBD; team sizes are paired with "led", never "built"; standards use "contributed to". "Established" (row 34) is the library's own PA-03.1 wording. |
| Skills anchored in the inventory (P/A for Summary/bullets) | **Passed with 1 REVIEW** | Everything is anchored. Spring Cloud (A/P ❓) sits under a "Hands-On" label (R1). No never-claim items (Go, TOGAF, ITIL, core-banking product, Istio). |
| No CEW / SCV-CCD / vendor names / internal numbers | **Passed** | grep CEW/SCV/CCD/GMS/HCL/MEPS: 0 hits. "eMemo" is a document type, not a system name, and is used in 03's safe wording. |
| Headline and Summary fit the chosen family × lens | **Not performed (partly)** | SM framing is consistent (leader of leaders, platform teams, hands-on). Fit to the Stripe JD was **not assessed**: the JD was outside the auditor's inputs. Lens: Stripe is a fintech, and the BNK-vs-INT default for fintech is still open (02 §7, OQ-P2). The file uses INT. |
| Summary is narrative; no stacked repetition | **Passed with note** | The Summary is narrative (3/4/3 lines). The idea "extensible platforms other teams depend on" appears four times: Summary ¶3, the Platform Engineering competency row, and the A1 and A5 labels. Consider cutting one or two of these (01 §6 Merging). |
| British spelling consistent; JD titles as written | **Passed** | Uses rigour, organisation, programme, licence, centre, containerised. grep for American -ize/-yze/center/program/organization/license forms: 0 hits. |
| Layout per 04; ≤ 3 pages; page numbers; no orphaned headings | **Passed (04 not read)** | 3 pages (pdfinfo). Footer "Page n of 3" on every page. 19 keep-with-next settings in the DOCX. No orphan headings, checked visually. |
| Text extractable; renders correctly as PDF | **Passed** | No text boxes, drawings or images (0 `txbxContent`/`drawing`/`pict`; `pdfimages`: none). Two tables (header/competencies) extract cleanly. Fonts are embedded (Carlito, the metric-compatible Calibri substitute, so Word rendering may differ slightly). |
| File name per 01 §10 | **Passed with note** | `wilson-2026_SM_Internet_Stripe_V1_0_0` follows the `[Family]_[Lens]_[Target]_V…` pattern. OQ-R3 is still open. Drop the `_draft` suffix on the final file. |
| Three-dimension review delivered separately | **Not performed** | Outside this audit. The auditor was instructed not to read the drafter's matching analysis. |
| Change log listing every material change | **Not performed** | Same reason. |

## 3. Document checks (render report + my own look at the PDF)

**Visually verified:** I rasterised all three pages and inspected them.

| Check | Result | Evidence |
|---|---|---|
| Page count ≤ 3 | ✅ 3 | pdfinfo; report "Pages: 3 (limit 3)" |
| Page numbers | ✅ | "Page 1 of 3" … "Page 3 of 3" in the footer |
| Heading orphans | ✅ none | Page 2 ends with the complete Hengshunyuan entry; page 3 opens with the AI Park employer line and its bullets; report `orphan headings: []` |
| Bullets ≤ 3 lines | ✅ | Longest bullet is 3 lines; report `line_flags: none` |
| ≤ 1 bullet in 5 at 3 lines | ✅ 5 / 31 = 16% | 3-line bullets: A1 (hub design), A3 (hands-on), A6 (AI service), UOB KPIs/quality gates, Baidu. Counted from the text; matches the report. |
| Paragraphs ≤ 4 lines | ✅ | Summary 3 / 4 / 3 lines; UOB scope line 2; VV-Life context 2 |
| Page 1 = header + summary + competencies + achievements | ✅ | All 7 achievements on page 1; page 2 starts with PROFESSIONAL EXPERIENCE (report: True/True; confirmed visually) |
| Draft markup | ℹ️ | 43 of 96 runs are red, which is expected for a draft (01 §10). The final file must be all black. |
| DOCX hygiene | ✅ | `comments.xml` contains 0 comments; 0 tracked insertions/deletions |

## 4. Summary

**Counts (62 claims):** **PASS 57 · REVIEW 5 · FAIL 0**

### Required fixes
None. No claim failed.

### For Wilson to decide
- **R1 — Spring Cloud under "Hands-On Engineering" (row 14).** The skills inventory rates Spring Cloud "A/P ❓": it is anchored at GBD, VV, Hengshunyuan and AI Park, but your own coding with it is not established, and the row label claims hands-on.
  *Question:* Did you personally write Spring Cloud code, or did you choose it and direct the team?
  *Safe default:* Move it out of the hands-on row. Hands-On Engineering → "Java, Spring Boot, Apache Camel, concurrency control, JVM tuning, SQL, code review, solution design, production troubleshooting". Platform Engineering → "Extensible platforms used by other teams, API design, microservices (Spring Cloud), event-driven integration, multi-tenant SaaS, high-concurrency systems".
- **R2 — "integration with core-banking settlement" (row 17).** S2 confirms that core banking executes settlement. CF-N4, however, says the hub does no settlement or clearing, and the skills inventory says never to claim core banking. The compressed phrase can read as settlement expertise. Row 20 words the same fact precisely.
  *Question:* Keep the compressed phrase?
  *Safe default:* Replace it with "hand-off to core banking, which executes settlement".
- **R3 — Too many named technologies in one bullet (rows 43 and 48).** GBD AWS lists 6 services and VV middle platform lists 5. 01 §6 says "at most 3–4 named technologies per bullet" (a 🔶 limit). Row 48 is the verbatim PA-13 wording.
  *Question:* Trim the lists, or accept them as ATS keywords for an internet-lens resume?
  *Safe default:* Trim GBD to "Architected the AWS deployment (API Gateway, ECS, RDS, DynamoDB) and applied DPIA, API and database encryption and credential management; led data migration." Keep VV's library-verbatim wording.
- **R4 — Software Designer (Intermediate) certificate, 2006 (row 60).** 02 §3 records it as ✅ from a verified primary document. The session evidence's "Held / not usable" line, however, blocks "any certification other than 'PMP — in progress' and SRE formal training". The auditor did not resolve this conflict.
  *Question:* Was that hold meant to cover this verified PRC qualification, or only unearned certifications such as TOGAF, ITIL or AWS?
  *Safe default:* Remove it until you confirm. The line becomes "PMP — in progress · Site Reliability Engineering (SRE) — formal training".

### Also worth a look (not counted; no fact at risk)
- Lens: Stripe is a fintech. The BNK-vs-INT default for fintech is still open (OQ-P2). This draft uses the Internet lens.
- Readability (01 §6A): MT/MX, MTTR, SIT/UAT and MAS are not expanded at first use. A5 does not name Golden Bridge for the SaaS clause.
- Interview readiness: the 99% SonarQube gate (new-code or overall? PA-03 §8). The ~80% figure is an estimate (PA-07 §8 formula). The VV and AI Park titles must match the employment letters at background check (CF-16).
- Repetition: "extensible platforms other teams depend on" appears four times on page 1 (see the QA checklist).

---

## Resolution (2026-10-26)

No FAIL items.

| Item | Resolution |
|---|---|
| R1 (Spring Cloud under Hands-On) | Default applied — removed from Hands-On Engineering; Platform Engineering now reads "microservices (Spring Cloud)". Left for Wilson: did you personally code with Spring Cloud? |
| R2 (core-banking settlement) | Default applied in the batch canonical form — "hand-off to core banking for settlement". Achievement A1 also reworded to "handing payments to core banking for settlement". |
| R3 (technology count) | Default applied — GBD AWS trimmed to "(API Gateway, ECS, RDS, DynamoDB)". VV B2B now uses the batch canonical sentence (four technologies; AWS dropped, "middle-platform" replaced). |
| R4 (Software Designer certificate) | **Overruled** per Revision Brief §1.1 — verified document in 02 §3 [CERT-SS]; education lines unchanged. |
| "Also worth a look" | MT/MX now explained by the canonical ISO wording; MTTR and SIT/UAT written out; A5 now names Golden Bridge; "extensible" repetition reduced (Summary ¶3 and A5 label). DR/99.9%+ in A4 now scoped to the real-time payment middleware (PA-02.1; same issue as audit 01 F1). 99% gate basis and OQ-P2 lens listed for Wilson. |
