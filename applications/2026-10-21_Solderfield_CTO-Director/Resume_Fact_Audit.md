# Resume Fact & Quality Audit — 05

**File audited:** `wilson-2026_SM_Bank_Solderfield_V1_0_0_draft.txt` (pdftotext), with `..._draft.pdf` (3 pages, viewed as rendered images at 70 dpi), `..._draft.report.md` / `.report.json`, and the `.docx` package (comments, footer and text-box check only).
**Auditor:** independent; did not read `Batch_Positioning.md`, `JD_Matching_Analysis.md`, `Resume_Change_Log.md` or `resume.json`. The JD was not provided to the auditor, so job fit is **not assessed**.
**Sources read (v2.0-draft folder):** `01_Resume_Master_Rules.md` v1.1 (2026-10-20) · `02_Candidate_Profile.md` v3.1 (2026-10-17) · `03_Achievement_Library.md` v4.1 (2026-10-17) · `technical-skills-inventory.md` v2.3 (2026-10-17) · `fact-check-and-open-questions.md` v2.4 (2026-10-20) · `session confirmations S1–S9 (Batch_Triage.md §7)` S1–S9 (tagged `[CONF 2026-10-21]`).
**Family × lens (from file name and headline):** SM × BNK.

---

## 1. Claim-by-claim audit

Checks column: D = dates · T = titles · Sc = scope · V = ownership verb · Te = technical depth · N = numbers and qualifiers · C = confidentiality.

### Header and Summary

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| H1 | "WILSON · Singapore PR · +65 8655 9547 · Skyzhang1028@gmail.com · Singapore" | 02 §1; D-11 | Name only, no surname ✓; PR ✓ | PASS | — |
| H2 | Headline "Banking Technology Leader — Payment Middleware & Productised SaaS \| Solution Design to Delivery" | 01 §5 (headline may name target positioning); 02 §7 SM×BNK | No historical title, no CTO ✓ | PASS | — |
| S1 | "Banking technology leader who designs and delivers payment middleware between a Tier-1 bank's channels and its core banking — validation, enrichment and ISO 20022 (SWIFT MT-to-MX) messaging — and has taken a configurable SaaS product from 0 to 1, with 18+ years…" | PA-01.2, PA-01.1, S2, CF-N4; PA-10.1; §0A "18+ years" | V: designs (O2) + delivers (O3) ✓; core banking = integration only (S2) ✓; 0-to-1 SaaS = GBD ✓ | PASS | Note: "core banking" is integration only (S2). Skills inventory §9 says never claim core-banking *platform* expertise (Temenos/Finacle). Be ready to say which core system received the payments. |
| S2 | "Vice President at UOB since 2022, leading 25 onshore and offshore engineers on payment and lending platforms serving millions of accounts." | 02 §2 row 1; §0A row 2; X-02 | T ✓; N 25 ✓ (scope, not outcome) | PASS | Which team covers lending is still open (C6), but X-02 frames the 25 across both platform lines, so this wording is fine. |
| S3 | "Began as an engineer and technical lead on e-commerce and news-content platforms at Renren, Sohu and Baidu" | 02 §4 career arc, §6.7–6.9 | ✓ | PASS | — |
| S4 | "then spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups — heading technology at a smart-parking IoT company, co-founding an audio-learning platform…" | 01 §5 / HR-1 ("head-of-technology roles 2016–2020"); GBD = Project Manager & Architect (02 §2) | No CTO / Chief Architect ✓; 2016–2022 is covered by "and architect roles" ✓ | PASS | — |
| S5 | "…and leading VV Technology's 140-person technology organisation (total headcount)." | S3 | N: wording and qualifier match S3 exactly ✓; no "built" paired with headcount ✓ | PASS | — |
| S6 | "has led winning technical bids as a vendor and, at UOB, helps select vendors and negotiate SOWs and licences as the buyer." | S7, PA-16.2; X-02 | Pre-sales limited to AI Park bids ✓; buyer-side at UOB ✓ | PASS | — |
| S7 | "Delivers end to end — requirements, solution design, testing, release and production support — under banking-grade change, release and access controls." | PA-01 §4/§6, PA-03.1, PA-02.3, X-04, PA-01.3 (permission matrix) | ✓ | PASS | — |

### Core Competencies

| # | Row | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| C1 | Banking Solutions: "Payment initiation, validation, enrichment and status tracking; **ISO 20022 (MT-to-MX) message transformation**; core-banking integration; retail lending servicing and collections" | PA-01, skills §9 (ISO 20022 MT→MX ✓), S2, PA-04 | Te: "message transformation" (converting MT messages into MX) is not on record. The record has the hub validating, enriching and handing payments to the SWIFT MX flow, and a migration of the programme from MT to MX. | **REVIEW** | See R-1. Safe default: "ISO 20022 (MT-to-MX) messaging migration". |
| C2 | Solution Architecture: payment middleware, API design, microservices, Apache Camel, event-driven integration, service orchestration, AI workflow automation, legacy modernisation with phased cut-over | PA-01.2, PA-01.1, skills §2 (Camel P), §7; PA-07/PA-08 | ✓ | PASS | — |
| C3 | Productisation: configurable multi-tenant SaaS from 0 to 1, reusable backend services, a SaaS model for business and public-sector customers, release planning and governance | PA-10.1; PA-16 §4 (SaaS model for *future* B2B/B2G); PA-03 | ✓ ("future" is kept in the AI Park bullet) | PASS | — |
| C4 | Bids & Commercial: technical bids and tender responses; buyer-side vendor evaluation and selection, SOW/licence negotiation, vendor performance reviews; delivery and technology budgets | S7, PA-16.2; X-02, X-05; 02 §5 (budget at UOB, GBD, VV, AI Park) | ✓ | PASS | — |
| C5 | Governance & Quality: secure SDLC, role-based access control, change control, release governance, SIT/UAT sign-off, DR and failover, MAS TRM (Singapore technology-risk rules) | PA-03.1, PA-03.4, PA-01.3 (permission matrix), PA-02.1; S9 (MAS TRM gloss) | ✓ | PASS | — |
| C6 | End-to-End Delivery: requirements to production support; Agile/Scrum and hybrid Waterfall; RAID, dependencies and scope trade-offs; data migration; steering-committee reporting | PA-01.5, PA-10 §4, X-02 (MVP scope), X-01 | ✓ | PASS | — |
| C7 | Technical: Java, Spring Boot, Spring Cloud, Apache Camel, Kafka, Kubernetes, Docker, AWS, Linux (RHEL), SQL, Jenkins, SonarQube, Splunk | Skills inventory §1–§6 (all anchored) | Skills line needs only an anchor ✓ | PASS | Kafka, Kubernetes and AWS are anchored at 2016–2022 employers, not UOB. This is fine in an undated skills line. |

### Selected Achievements

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| A1 | "Led end-to-end design of a payment-initiation hub — API contracts, validation, enrichment and status tracking — integrating channels, vendor systems and core banking, which executes settlement." | PA-01.2 📄; S2; CF-N4 | V: "Led … design" (O2) ✓; the hub is not described as settling ✓; no internal name ✓ | PASS | — |
| A2 | "Planned and architected the phased, Blue/Green-style coexistence… live from May 2025, ahead of SWIFT's November 2025 deadline, with coexistence retired in August 2026 and no service interruption." | PA-01.1; §0A rows 3, 5 | D ✓; N ✓; "no service interruption" is 📄 and permitted as worded in 03 | PASS | — |
| A3 | "Architected and delivered, from 0 to 1, a multi-tenant SaaS platform for online-game businesses — reusable services for KYC, bonuses, VIP tiers, analytics and payments — on Spring Cloud, Kubernetes and AWS." | PA-10.1 📄; S9 (GBD wording) | V: O2 + O3 ✓; no "200+" ✓ | PASS | OQ-1.9 (business nature) is still open, but S9 approves this exact framing. |
| A4 | "At AI Park, led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing, and launched pilots in Shijiazhuang (2016), Handan (2017) and Beijing Chaoyang (2017)." | PA-16.2 ✅; CF-14 | Matches 03 word for word; no "4+" or "1,000+" ✓ | PASS | — |
| A5 | "At UOB, hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and chair budget and performance reviews for four IT service vendors." | X-02, X-05; §0A "four IT service vendors" | No vendor names ✓ | PASS | — |
| A6 | "Established release governance with SIT/UAT sign-off for every release, designed role-based permissions and encryption under MAS TRM, and personally led DR and failover drills, sustaining 99.9%+ availability." | PA-03.1 📄 ("Established…" is 03 safe wording); PA-01 §4 "Designed the security controls" ✅; PA-01.3; PA-02.1; §0A 99.9%+ | V: matches 03 ✓; N ✓ | PASS | Three ideas in one bullet, all on the governance theme. Acceptable. |
| A7 | "Co-founded an audio-learning platform and owned product, architecture and technical delivery from market research to production, reaching a peak of ~100k daily active users." | PA-15.1 📄; §0A | N: "~" kept ✓ | PASS | Single source ([R22]). |

### Professional Experience — UOB

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| U0 | "United Overseas Bank (UOB) \| Singapore · Oct 2022 – Present · Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | D, T exact ✓ | PASS | — |
| U1 | Scope line: two platform lines in a MAS-regulated Tier-1 bank, serving millions of accounts: cross-border payments (SWIFT ISO 20022 messaging) and retail unsecured lending… | 02 §6.1; PA-04.1 | ✓ | PASS | — |
| U2 | "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results…" | PA-01.3 ✅; S6 (closes C7 b) | V: O1 ✓ | PASS | Polish P-1: "the hub" has not been introduced in this section. |
| U3 | "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking." | PA-01.4 📄 | No invented figure ✓ | PASS | — |
| U4 | "Led the 10-engineer backend team of a regional customer-360 platform (in production since 2022) that takes daily account summaries from core banking for portfolio analysis; personally built its data-analysis module and Spring Batch jobs." | PA-05.2, PA-05.3 ✅; S2; skills (Spring Batch P) | N ✓; does not claim he led the 2022 launch (C5 open) ✓; no internal name ✓ | PASS | Polish P-2 (tense). |
| U5 | "Designed and built two AI workflow automations: a code-review service — live since May 2026 after formal architecture and risk approval, with humans keeping merge authority — and an agent that removed a manual document-reconciliation task." | PA-07.1, PA-07.2 (O1+O2); PA-08 (O1, Apr 2026); S9 | V ✓; no unqualified "80%" ✓ | PASS | — |
| U6 | "Own end-to-end delivery of the ISO 20022 programme with a 15-engineer onshore/offshore team — scope, roadmap, RAID, dependencies…, release planning and production rollout — shipping upgrades every 2–3 months." | PA-01.5; §0A rows 3, 15 | V: O3 ✓; team size is scope, not paired with "built" ✓ | PASS | — |
| U7 | "Led data migration for the payment-initiation hub, the retail-lending platform and the customer-360 platform, with sensitive-data encryption and credential management." | X-01 ✅; PA-04 §4 | ✓ | PASS | — |
| U8 | "Enforce CI/CD quality gates — JUnit, a 99% SonarQube coverage gate, automated regression and penetration testing — and run secure SDLC, DPIA and data governance in line with MAS TRM." | PA-03.2 📄, PA-03.4 ✅; §0A 99% | N ✓ | PASS | Interview risk: whether 99% is new-code or overall coverage is still open (03 PA-03 §8). |
| U9 | "Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, RCA and post-incident reports; with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring." | X-06, CF-N2, CF-N3, PA-02.3 | No "reported to MAS" ✓ | PASS | — |
| U10 | "Lead technical evaluation of vendors **and start-ups — architectural design, technical credentials and fit with existing systems —** as input to vendor-selection and SOW/licence decisions." | 02 §5 ("vendor technical evaluation"); X-02 | Sc: "start-ups" as evaluated parties, and the three evaluation criteria, are on no record (02, 03, S1–S9) | **FAIL** | Replace with: "Lead technical evaluation of vendors as input to vendor-selection and SOW/licence decisions." (The removed detail can come back only if Wilson confirms it with a [CONF] date.) |
| U11 | "When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies and set a sequence all parties accept." | X-02 ✅ (word for word) | ✓ | PASS | — |
| U12 | "Act as the primary interface between business stakeholders, product owners, operations, compliance, architects and engineering managers; present status, risks and decisions to senior management and steering committees." | PA-01 §9; §5.3 U29; PA-01.5 | No Board or C-suite ✓ | PASS | — |

### Golden Bridge Drive · VV Technology · Hengshunyuan · AI Park

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| G0 | "Golden Bridge Drive (SG) Pte. Ltd. \| Singapore · Nov 2020 – Jul 2022 · Project Manager & Architect" | 02 §2 row 3 | D, T ✓ | PASS | — |
| G1 | "Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR, and owned delivery budget, capacity and launch readiness…" | S4; PA-10.3 | N: S4 wording ✓; "Led", not "Built" (HR-9) ✓ | PASS | — |
| G2 | "Ran hybrid delivery — Waterfall for scope, budget, milestones and resource planning; Agile sprints for execution, backlog tracking and iterative delivery." | PA-10 §4 decision [LIB] | ✓ | PASS | — |
| G3 | "Designed hierarchical KYC identity verification and configurable rule models for authentication levels and for bonus eligibility, triggers and distribution." | PA-10.2 📄 (without "200+") | No "200+" ✓ (CF-11) | PASS | — |
| V0 | "VV Technology Pte. Ltd. \| Singapore · Apr 2019 – Jun 2020 · Head of Technical Centre" | 02 §2 row 4 (dates); S8 (title, supersedes 02 "Development") | D ✓; T per S8 ✓ | PASS | Back-fill TU-13 is still pending in 02/03. |
| V-ctx | "VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services — through data." | PA-11 §1 [R22] | ✓ | PASS | The rendered line ends with "data." alone on a second line (cosmetic). |
| V1 | "Built VV's technology organisation and its microservices platform (Spring Cloud, Kubernetes, Redis cluster, Elasticsearch, AWS) from scratch, owning technology selection and the technology budget." | PA-11.1 (03 wording, 140 slot dropped) | V: 03 wording ✓; Te: all anchored ✓ | PASS | Style: 5 named technologies, over the 01 §6 cap of 3–4 (P-3). |
| V2 | "Delivered the first VV-Life release in 2019 and architected its payment subsystem, integrating UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation." | PA-11.2; S1 (O2) | V: "architected" (O2) ✓; no direct card-scheme connectivity claim ✓ | PASS | — |
| V3 | "Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product serving Southeast Asia, governing solution design, cost evaluation, staffing and acceptance." | PA-13 📄 | Internal name "GMS" not used ✓ | PASS | Style: 5 named technologies (P-3). |
| V4 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans." | PA-11.3, PA-11.5 / CF-N8 | ✓ | PASS | — |
| HS0 | "Hengshunyuan Information Technology Co., Ltd. \| China · Oct 2017 – Sep 2019 · Co-founder" | 02 §2 row 5; D-10 | D per D-10 ✓; T ✓ | PASS | — |
| HS1 | "Ran business development for content licensing with rights holders, bringing ~1,500 licensed audio titles and albums onto the audio-learning platform at launch." | PA-15 §4; PA-15.2; §0A | N: "~" kept ✓ | PASS | — |
| AP0 | "AI Park \| China · Apr 2016 – Sep 2017 · VP of Technical Department" | 02 §2 row 6 (Apr per CF-06 default A, confirmed earlier); S8 (title) | D ✓; T per S8 ✓ | PASS | — |
| AP1 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform connecting car parks to the cloud…" | PA-16.1 | ✓ | PASS | — |
| AP2 | "Introduced a SaaS model for future business and government customers." | PA-16 §4 [R22] | ✓ | PASS | — |
| AP3 | "Brought Spring Cloud microservices into the architecture, with Kafka for asynchronous flows and caching to shield the database, achieving millisecond-level service processing." | PA-16.4 ✅ (word for word) | No % figure ✓ | PASS | — |

### Earlier Experience and Education

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| E1 | "Baidu — Technical Specialist, Nuomi… (May 2014 – Dec 2014, China): As project leader, re-architected… on Dubbo microservices and delivered two months ahead of plan; designed and coded Nuomi's payment-gateway integration with Alipay, WeChat Pay and UnionPay." | 02 §2 row 7 (CF-12); PA-17.1; S1 | D, T ✓; N ✓; no "5–10M QPS" ✓ | PASS | — |
| E2 | "Sohu.com — Technical Leader / Project Leader, Sohu News content platform (Mar 2012 – May 2014, China): Re-architected the fifth-generation CMS (SSH to Spring MVC, memcached to Redis) and delivered its OpenAPI messaging platform." | 02 §2 row 8; PA-18.1 (O1+O2) | ✓ | PASS | — |
| E3 | "Renren Network — Senior R&D Engineer (Jul 2008 – Mar 2012, China): Developed Renren's shopping website, Renren Mall and CRM, and designed and coded Renren Mall's payment integration with Alipay and UnionPay." | 02 §2 row 9; PA-19; S1 | No WeChat Pay under Renren ✓ | PASS | — |
| Ed1 | "Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008)" | 02 §3; CF-02; FU-4 fallback wording | ✓ | PASS | — |
| Ed2 | "Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004)" | 02 §3; CF-01 | ✓ | PASS | — |
| Ed3 | "Software Designer (Intermediate) — Qualification Certificate… (2006) · PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3 [CERT-SS]; CF-N5; S9 | No other certifications claimed ✓; PMP not "certified" ✓ | PASS | — |
| Ed4 | "Languages: English and Mandarin (professional working proficiency in both)" | 02 §1 | ✓ | PASS | — |

---

## 2. 01 §9 QA checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to an ID in 03 / 02; no ❓/⚠️/⛔ content | **Failed** (1 item) | U10 adds "start-ups" and evaluation criteria that are on no record. No ⛔ items appear (10M DAU, 200+, 1,000+, 10M HTTP, 5–10M QPS, Flink, chatbot, forecasting, defects 70–80%, ramp-up 30–40% are all absent). |
| Dates and titles match 02 §2 exactly; no CTO / Chief Architect | Passed | VV and AI Park titles follow S8 (which supersedes the 02 §2 "Development" wording). Hengshunyuan dates per D-10; AI Park start per CF-06 default. |
| Every number matches the Metrics Bank, with qualifiers kept | Passed | 18+, 25, 15, 10, four vendors, 99.9%+, 99%, ~100k, ~1,500, 2–3 months, milestone dates, and 140 / 40 "(total headcount)" (S3/S4). |
| Verbs match ownership level (01 §4) | Passed | "Personally built" is used only for O1 items (PA-01.3 + S6, PA-05.2). "Architected" is used for O2 (VV payments, GBD). Headcount is never paired with "built". |
| Skills anchored in the inventory (P/A for Summary/bullets) | Passed | Every named technology in bullets is P, A or A/P. The Technical line is anchored. |
| Confidentiality: no CEW / SCV-CCD / CCD / GMS / HCL / internal numbers | Passed | Confirmed by grep of the text and by checking the docx package (no comments, no text boxes). |
| Headline and Summary fit family × lens | Partly performed | It reads as a coherent SM × BNK positioning. JD-specific fit was **not assessed** because the JD was not provided to the auditor. |
| Summary is narrative; no stacked repetition | Passed (minor note) | Three short paragraphs (162 words). Some overlap on page 1: "validation, enrichment" appears in the Summary, Competencies and A1; commercial authority appears in Summary P3 and A5. Acceptable, but these are candidates to trim. |
| British spelling consistent; JD titles as written | Passed | Organisation, programme, licence(s), containerised, Productised, Centre. No American forms found. |
| Layout per 04; ≤ 3 pages; page numbers; no orphaned headings | Passed | 3 pages; footer reads "Page X of 3"; no orphaned headings. 04 was not re-read; checked against the render report and the rendered pages. |
| Text extractable; renders correctly as PDF | Passed | pdftotext extraction is complete; tagged PDF; no text boxes or drawings in the docx. |
| File name per 01 §10 | Passed (provisional) | `wilson-2026_SM_Bank_Solderfield_V1_0_0` matches the pattern (OQ-R3 still open). "_draft" is a working suffix. |
| Three-dimension review delivered separately | Not performed | `JD_Matching_Analysis.md` exists in `drafts/05/` but was not read, per the brief. |
| Change log | Not performed | `Resume_Change_Log.md` exists but was not read, per the brief. |

## 3. Document checks (render report + PDF viewed at 70 dpi)

| Check | Result | Note |
|---|---|---|
| Page count ≤ 3 | Passed | 3 pages (pdfinfo and the render report agree). |
| Page numbers | Passed | "Page 1 of 3" … "Page 3 of 3" in the footer. |
| Heading orphans | Passed | None in the report; seen on the rendered pages. The Hengshunyuan heading at the foot of page 2 keeps its bullet. |
| Bullets ≤ 3 lines; ≤ 1 in 5 at 3 lines | Passed | 2 of 32 bullets are 3 lines (A2 Modernisation and E1 Baidu), about 1 in 16. |
| Paragraphs ≤ 4 lines | Passed | Summary paragraphs are 4 / 3 / 3 lines (estimated) and the UOB scope line is 3. |
| Page 1 = header + Summary + Competencies + Achievements | Passed | Page 2 starts with Professional Experience. Page 1 has about 15% free space at the bottom. |
| Draft markup | Note | 51 of 97 runs are red (expected for a draft, 01 §10). The final file must be all black. |
| Cosmetic | Note | The VV-Life context line leaves "data." alone on its second line. Fine typographic detail was not checked at higher resolution. |

---

## 4. Summary

**Counts:** 59 claims audited. **PASS 57 · REVIEW 1 · FAIL 1.**

### Required fixes
1. **U10 (UOB, Commercial & Stakeholders):** replace "Lead technical evaluation of vendors and start-ups — architectural design, technical credentials and fit with existing systems — as input to vendor-selection and SOW/licence decisions." with **"Lead technical evaluation of vendors as input to vendor-selection and SOW/licence decisions."** The record has vendor technical evaluation only (02 §5; X-02). Start-ups and the evaluation criteria are on no record.

### For Wilson to decide
- **R-1 (Core Competencies → Banking Solutions, "ISO 20022 (MT-to-MX) message transformation"):** Did you or your hub team build MT-to-MX message transformation or mapping, or does the hub produce MX natively, with the migration being a change of message standard? **Safe default:** change to "ISO 20022 (MT-to-MX) messaging migration".

### Recommended polish (optional, not counted)
- **P-1:** U2 "Personally built the hub's core modules" → "Personally built the payment-initiation hub's core modules". "The hub" is not introduced on page 2, and recruiters may read page 2 on its own.
- **P-2:** U4 "Led the 10-engineer backend team" is past tense, but the team is part of the 25 he currently leads (S2/X-02). Present tense "Lead…" would be consistent with 01 §6. Past tense matches the 03 PA-05.3 wording, so this is not an error.
- **P-3:** V1 and V3 each name 5 technologies (01 §6 cap: 3–4). Trim one each, for example drop "Elasticsearch" in V1 and "AWS" in V3, if space or style requires.
- **P-4:** 01 §6A asks for industry acronyms to be expanded at first use, citing "ISO 20022 MT→MX" as the example. Summary S1 does not expand MT/MX. Consider "ISO 20022 payment messaging (SWIFT's move from legacy MT to MX)".
- **Interview-risk reminders (no change needed):** the 99% SonarQube gate (new-code or overall coverage?); "core banking" (be ready to name the integration point, never claim platform expertise); "no service interruption" and the 99.9%+ availability are 📄 single-library claims.

---

## Resolution (2026-10-26)

| Item | Resolution |
|---|---|
| **F1** (U10 vendor evaluation) | Fixed — auditor's replacement applied verbatim: "Lead technical evaluation of vendors as input to vendor-selection and SOW/licence decisions." Start-ups and evaluation criteria removed; they return only with a dated confirmation from Wilson. |
| R-1 (MT-to-MX message transformation) | Default applied — "ISO 20022 (MT-to-MX) messaging migration". Left for Wilson: did you or the hub team build MT→MX transformation/mapping? |
| P-1 | Applied — "Personally built the payment-initiation hub's core modules". |
| P-2 | Applied — "Lead the 10-engineer backend team …". |
| P-3 | Applied — V1 replaced by the batch canonical VV sentence (no technology list); V3 replaced by the canonical VV B2B sentence (four technologies). |
| P-4 | Applied — Summary now "ISO 20022 messaging (SWIFT's MT-to-MX migration)"; the achievement uses the canonical ISO 20022 sentence. |
| Interview-risk reminders | 99.9%+ in A6 now scoped to "the real-time payment middleware" (PA-02.1; same issue as audit 01 F1). 99% gate basis listed for Wilson. |
| Software Designer certificate | Not raised in this audit; education lines unchanged (Revision Brief §1.1). |
