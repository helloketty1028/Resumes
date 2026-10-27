# Resume Fact & Quality Audit — 02

**File audited:** `wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0_draft.txt` (pdftotext of the rendered PDF), with `..._draft.pdf` (3 pages, A4, viewed as 70 dpi rasters), `..._draft.report.md` and a structural check of `..._draft.docx`.
**Auditor:** independent; drafting notes, change log, matching analysis, resume.json and `Batch_Positioning.md` deliberately **not** read. The JD itself was not among the inputs, so JD fit is not assessed here.
**Date:** 2026-10-21

**Sources read (versions):**
- `01_Resume_Master_Rules.md` v1.1 (2026-10-20)
- `02_Candidate_Profile.md` v3.1 (2026-10-17)
- `03_Achievement_Library.md` v4.1 (2026-10-17)
- `technical-skills-inventory.md` v2.3 (2026-10-17)
- `fact-check-and-open-questions.md` v2.4 (2026-10-20)
- `session confirmations S1–S9 (Batch_Triage.md §7)` S1–S9 + the "Held / not usable" list, tagged `[CONF 2026-10-21]`
- `Audit_Brief.md`

---

## 1. Claim-by-claim audit

Checks: D = dates · T = titles · S = scope · V = ownership verb · TD = technical depth · N = numbers & qualifiers · C = confidentiality.

### Header and Summary

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 1 | "WILSON" | 02 §1, D-11 | T ✓ | PASS | — |
| 2 | "Singapore PR \| +65 8655 9547 \| Skyzhang1028@gmail.com \| Singapore" | 02 §1 (PR since 2024 ✅) | ✓ | PASS | — |
| 3 | Headline "Head of Technology Development — Payments, Digital Channels & Integration \| Regulated Delivery · Hands-On Engineering" | 01 §5 (headline may name the **target** role); 02 §7 SM×BNK | T ✓ (target role, not a past title); no CTO | PASS | — |
| 4 | "Technology leader with 18+ years … leads multi-discipline teams and delivers BAU and change projects to deadline, currently in a MAS-regulated Tier-1 bank." | 03 §0A (18+); PA-01 §9 (multi-discipline); CF-N3/PA-02.3 (BAU); PA-01.1 | N ✓ S ✓ | PASS | — |
| 5 | "Began as a Java engineer and technical lead on high-traffic consumer platforms at Renren, Sohu and Baidu, then spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups." | 02 §4 positioning ("high-traffic consumer internet") and career arc ("Head of Technology (start-ups/scale-ups) 2016–22"); 01 §5; skills Java P | D ✓ T ✓ (no CTO / Chief Architect) | PASS | "High-traffic" stays qualitative. Correct, because the 10M DAU / QPS figures are on hold. |
| 6 | "Since 2022, a Vice President in UOB's GT&O, leading 25 onshore and offshore engineers on two platform lines — cross-border payments and **retail lending** — that serve millions of accounts." | 03 §0A row 2, X-02; 02 §6.1 | N ✓; S: record says **retail *unsecured* lending** | **REVIEW** | See R1. |
| 7 | "Delivers change projects alongside BAU production support, governs IT service vendors and applies MAS TRM (Singapore technology-risk rules) through secure SDLC and data governance." | CF-N3, X-05, PA-03.4, S9 | V ✓ C ✓ (no vendor names) | PASS | — |
| 8 | "Brings customer-channel experience …: e-commerce sites and their payment-gateway integrations, a news CMS, a local-life platform with card and e-wallet payments, and a B2B SaaS platform behind an API gateway." | S1; PA-17/PA-19; PA-18; PA-11; PA-10 | S ✓ | PASS | — |
| 9 | "Remains hands-on in Java — reviewing new core pull requests daily, co-designing solutions with engineers and writing core modules for significant changes." | S5, X-04 | V ✓. No "full-time engineer", no %, no ~50/~20 | PASS | — |

### Core Competencies

| # | Row | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 10 | Technology Leadership: squad leads/EMs, mentoring, performance management, onshore/offshore, cross-time-zone, 5+ years offshore | X-02; 03 §0A | N ✓ | PASS | Cross-time-zone working is collaboration with India, Thailand and Indonesia, not line management (X-02). The row does not claim line management, so it is fine. |
| 11 | Delivery & Prioritisation: BAU + change, prioritisation across two lines, roadmaps, milestones, RAID, change control, steering-committee reporting | PA-01.5, PA-01 §6, X-02 | ✓ | PASS | — |
| 12 | Channels & Integration: e-commerce, news-portal CMS, API gateway, B2B/B2C, channel and **core-banking integration**, Alipay/WeChat Pay/UnionPay, card and e-wallet payments | S1, S2, PA-10, PA-18 | S ✓ | PASS | Core-banking *integration* is supported by S2. Core-banking *platform* expertise stays on the never-claim list (skills §9; held: Deposits/GL). Be ready to explain this at interview. |
| 13 | Vendor & Commercial: vendor technical evaluation and selection, technology-investment decisions, SOW/licence negotiation, governance of IT service vendors, delivery budget | X-02, X-05, 02 §5 | C ✓ | PASS | Buyer-side authority only (S7). Correctly worded. |
| 14 | Security & Compliance: MAS TRM, secure SDLC, DPIA, API/DB encryption, credential management, pen-testing in CI/CD, incident analysis for regulatory reporting | skills §10; X-01; X-06 | ✓ | PASS | — |
| 15 | Methods & Tools: Agile/Scrum, hybrid Waterfall, Jira, Confluence, MS Project, Miro | skills §11 | ✓ | PASS | — |
| 16 | Technical: Java, **JavaScript (React)**, Spring Boot, Spring Cloud, Apache Camel, **SQL**, **Linux (RHEL)**, AWS, Kubernetes, Splunk, Spark, production AI agents (Claude Code) | skills §1–§8 | TD: all ✅, but React, SQL and RHEL carry "employer anchor ❓" (skills usage rule: anchor = employer + period; OQ-3.8) | **REVIEW** | See R2. |

### Selected Achievements

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 17 | Migration ahead of deadline: phased coexistence, not big-bang; MX-rich live May and Aug 2025 ahead of SWIFT's Nov 2025 deadline; coexistence retired Aug 2026 with no service interruption | PA-01.1 (✅ dates / 📄 no-interruption); 03 §0A | D ✓ N ✓ V ✓ (O2+O3) | PASS | — |
| 18 | Multi-discipline leadership: "Lead two onshore/offshore platform teams through squad leads and engineering managers; earlier led VV's 140-person technology organisation (total headcount) **of engineering, DevOps and data teams**." | X-02; S3 | N ✓ ("total headcount" kept; not paired with "built"). S: **the 140's make-up is not on record** (OQ-2.3 asks which functions were included; S3 does not say). The bullet is scope only with no outcome, and it repeats Summary ¶2, Competencies row 1 and UOB bullets E2/E8 | **REVIEW** | See R3. |
| 19 | Payment-gateway integrations: designed and coded Renren Mall (Alipay, UnionPay) and Baidu Nuomi (Alipay, WeChat Pay, UnionPay); at VV architected a payment subsystem integrating UnionPay, Visa/Mastercard, Google Pay and GrabPay with settlement reconciliation | S1 (O1+O2 for Renren and Baidu; O2 for VV) | V ✓; no WeChat Pay under Renren ✓; no direct card-scheme claim ✓ | PASS | — |
| 20 | Content-management system: at Sohu, led re-architecture of the fifth-generation news CMS; contributed to the publishing-workflow design | PA-18.1 📄, PA-18.2 ✅ (O5) | V ✓ ("contributed to") | PASS | — |
| 21 | Multi-tenant SaaS: at Golden Bridge, architected and delivered 0-to-1 a multi-tenant SaaS for online-game businesses on AWS — KYC, bonus, VIP, multi-channel payments — behind an API gateway | PA-10.1 📄; S9 (approved business wording) | V ✓ (O2+O3); no "200+" ✓ | PASS | OQ-1.9 (casual vs real-money gaming) is still open in the library. S9 approves this exact wording for this batch. |
| 22 | Vendor assessment and governance: "**Assess vendors' architecture, credentials and fit with existing systems**, with decision or joint-decision authority on vendor selection and SOW/licence negotiation; chair governance of four IT service vendors." | X-02, X-05; 02 §5 ("vendor technical evaluation") | N ✓ C ✓. S: the specific criteria ("architecture, credentials, fit with existing systems") are not in 03, 02 or S1–S9. "Credentials" can also be confused with the security sense (credential management) | **REVIEW** | See R4. |
| 23 | AI adopted in production: designed and built an AI code-review service; headless Claude Code agents review each PR alongside SonarQube; live since May 2026 after formal architecture and risk approval; AI advises, never approves or merges; review time fell by **an estimated ~80%** | PA-07.1–07.3, S9 | V ✓ (O1+O2); N ✓ (estimate labelled); D ✓ | PASS | — |

### Professional Experience — UOB

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 24 | UOB \| Singapore \| Oct 2022 – Present · "Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | D ✓ T ✓ | PASS | — |
| 25 | Scope line: technology lead for cross-border payments (SWIFT ISO 20022) and retail unsecured lending …; works closely with teams in India, Thailand and Indonesia | 02 §6.1; X-02; D-09 | S ✓ | PASS | — |
| 26 | Led a 15-engineer team; owned end-to-end delivery of the ISO 20022 programme; upgrades every 2–3 months | PA-01.5; 03 §0A | N ✓ V ✓ (O3) | PASS | — |
| 27 | MVP-scope prioritisation when the two lines' schedules conflict | X-02 (verbatim safe wording) | ✓ | PASS | — |
| 28 | Own technology for retail unsecured-lending servicing … and post-disbursement collections | PA-04.1 (verbatim) | V ✓ (O3+O4) | PASS | — |
| 29 | Primary interface between business, product owners, operations, compliance, architects and EMs; presents to senior management and steering committees | 03 §5.3 U29 → PA-01 §9; PA-01.5 | S ✓; no Board or C-suite ✓ | PASS | "Primary" comes from [LIB] U29. 03 has no separate safe wording for it. |
| 30 | Led end-to-end design of a payment-initiation hub … integrating reference data, third-party banking systems and core banking, which executes settlement | PA-01.2 📄; S2; CF-N4 | V ✓ (O2); the hub does not settle ✓; C ✓ (no "CEW") | PASS | — |
| 31 | Personally built the hub's core modules in Java — initiation, **concurrency control**, permission matrix, status-result processing | PA-01.3 ✅; S6 (closes C7 b) | V ✓ (O1) | PASS | — |
| 32 | Lead the 10-engineer backend team of a regional customer-360 platform taking daily account summaries from core banking; designed data models; personally built the analysis module and Spring Batch jobs | PA-05.2/05.3 ✅; S2; skills (Spring Batch P) | N ✓ V ✓; C ✓ (no "SCV-CCD"); no claim to have led the launch (C5) ✓ | PASS | — |
| 33 | Built an AI agent cross-checking eMemo and quotation documents; contributed to a production AI knowledge assistant with access controls and data masking | PA-08 (O1 ✅); S9 (O5) | V ✓ | PASS | — |
| 34 | Coordinate P1–P3 incidents …; produce technical incident analyses that support the bank's regulatory reporting to MAS | X-06 (verbatim) | ✓ (not "reported to MAS") | PASS | — |
| 35 | Established delivery KPIs …; CI/CD quality gates (99% SonarQube coverage gate, regression, pen-testing); SIT/UAT sign-off for every release | PA-03.1 📄, PA-03.2 📄; 03 §0A 99% | N ✓ | PASS | Interview risk: whether the 99% covers new code or all code is still undefined (PA-03 §8). |
| 36 | Designed security controls (API/DB encryption, credential management, role-based permissions) and led data migration … under secure SDLC, DPIA and MAS TRM; personally led DR/failover drills, sustaining 99.9%+ availability | X-01 (O2) ✅; PA-01 §4; PA-02.1; 03 §0A 99.9%+ | V ✓ N ✓ | PASS | Style: two ideas in one 3-line bullet (01 §6 "one idea per bullet"). Optional split. |

### Golden Bridge, VV, AI Park

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 37 | Golden Bridge Drive (SG) Pte. Ltd. \| Singapore \| Nov 2020 – Jul 2022 · Project Manager & Architect | 02 §2 row 3 | D ✓ T ✓ | PASS | — |
| 38 | Led a 40-person project team (total headcount); Agile/Scrum from scratch; CI on Jenkins + ECR; delivery budget, capacity, launch readiness | S4; PA-10.3; HR-9 | N ✓ (qualifier kept; "led", not "built") | PASS | — |
| 39 | Hybrid delivery: Waterfall for scope, budget, milestones, resources; Agile sprints for execution | PA-10 §4, §9 | ✓ | PASS | — |
| 40 | Architected the AWS deployment (API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch); DPIA, encryption, credential management; led data migration | PA-10 §3; skills §5 (A); X-01 | V ✓ (O2) TD ✓ (A) | PASS | Style: six named technologies, above the 01 §6 guide of 3–4 per bullet. Optional trim. |
| 41 | VV Technology Pte. Ltd. \| Singapore \| Apr 2019 – Jun 2020 · **Head of Technical Centre** | 02 §2 row 4; S8 (supersedes "Development") | D ✓ T ✓ | PASS | — |
| 42 | Context: VV-Life local-life platform (food, fresh produce, travel, everyday services) | PA-11 §1 | ✓ | PASS | — |
| 43 | Built VV's microservices platform from scratch (Spring Cloud, Kubernetes, Redis, AWS), owning technology selection and budget | PA-11.1 (the 140 slot is dropped, correctly) | V ✓ (03 safe wording uses "Built") | PASS | — |
| 44 | Took part in product-strategy planning; delivered first VV-Life release in 2019 incl. payment subsystem modules | PA-11.2, PA-11 §4 | D ✓ | PASS | — |
| 45 | "Led the big-data team on Flume, Hive, MapReduce, Spark Streaming and Spark SQL, **providing data analysis that supported business decisions**." | PA-12 ([R22] version only; ⚠️ CF-07) | TD ✓ (no Flink). S: the outcome clause is not in 03 (PA-12 records no outcome). Five named technologies | **REVIEW** | See R5. |
| 46 | Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) for a B2B online-office product … | PA-13 (verbatim) | V ✓; C ✓ (no "GMS") | PASS | — |
| 47 | Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined incident priority levels and tiered emergency-response plans | PA-11.3, PA-11.5 | ✓ | PASS | — |
| 48 | AI Park \| China \| Apr 2016 – Sep 2017 · **VP of Technical Department** | 02 §2 row 6; S8; CF-06 default A | D ✓ T ✓ | PASS | — |
| 49 | Led architecture, delivery, budget and the technical team for a smart-parking IoT platform … | PA-16.1 | ✓ | PASS | — |
| 50 | Led technical bids that won city projects in Shijiazhuang, Handan and Beijing; pilots 2016/2017/2017 | PA-16.2 ✅; S7 | D ✓; no "4+" or "1,000+" ✓ | PASS | — |
| 51 | Introduced a SaaS model for business and government customers; added an AI processing step to licence-plate and portrait recognition | 02 §6.6; PA-16.3 | TD ✓ (integration, not model training) | PASS | 02 says "SaaS model for **future** B2B/B2G customers". Avoid implying live SaaS customers at interview. |

### Earlier Experience and Education

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 52 | Hengshunyuan — Co-founder (Oct 2017 – Sep 2019): audio-learning platform, ~1,500 licensed titles, peak ~100k DAU | 02 §2 row 5; D-10; PA-15.1/15.2; 03 §0A | D ✓ T ✓ N ✓ ("~" kept) | PASS | — |
| 53 | Baidu — Technical Specialist (May – Dec 2014): led web front-end, CMS and QA teams as project leader; re-architecture two months ahead of plan | 02 §2 row 7; PA-17.1 | D ✓ T ✓ N ✓; no "5–10M QPS" ✓ | PASS | — |
| 54 | Sohu.com — Technical Leader / Project Leader (Mar 2012 – May 2014): CMS OpenAPI messaging platform; website SEO | 02 §2 row 8; PA-18.1 | D ✓ T ✓ | PASS | — |
| 55 | Renren — Senior R&D Engineer (Jul 2008 – Mar 2012): shopping website, Renren Mall, CRM | 02 §2 row 9; PA-19 | D ✓ T ✓ | PASS | — |
| 56 | Master's degree in Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 (FU-4 fallback wording) | ✓ | PASS | — |
| 57 | Bachelor's degree in Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 | ✓ | PASS | — |
| 58 | "**Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006)**", under the heading "EDUCATION, **CERTIFICATIONS** & LANGUAGES" | 02 §3 marks it ✅ [CERT-SS], **but** Session_Confirmations "Held / not usable" lists "any certification other than 'PMP — in progress' and SRE formal training" | Breaks the batch hold on certifications | **FAIL** | See Required fix F1. (If Wilson wants the certificate back, he must lift the hold; it is a verified document in 02 §3.) |
| 59 | PMP — in progress · Site Reliability Engineering (SRE) — formal training | 02 §3; CF-N5 | ✓ (not "certified") | PASS | — |
| 60 | Languages: English and Mandarin (professional working proficiency) | 02 §1 | ✓ | PASS | — |

---

## 2. 01 §9 Pre-Delivery QA Checklist

| Item | Result | Note |
|---|---|---|
| Every bullet traces to an ID in 03 / a section of 02; no ❓/⚠️/⛔ content outside permitted parts | **Failed** (1 item) | #58 Software Designer certificate is on the batch hold list. The elaborations in #18, #22 and #45 have no evidence ID (REVIEW). |
| Dates and titles match 02 §2 exactly; no "CTO" / "Chief Architect" | Passed | VV and AI Park titles follow S8 ("Centre" / "Department"), which supersedes 02 §2 "Development". No CTO or Chief Architect anywhere. |
| Every number matches 03 Metrics Bank, with qualifiers kept | Passed | 18+, 25, 15, 10, 2–3 months, 2025/2026 milestones, estimated ~80%, 99%, 99.9%+, four vendors, 5+ years, 140 and 40 (both "total headcount"), ~1,500, ~100k, two months ahead. None of the held figures appear. |
| Verbs match ownership level (§4) | Passed | Designed and coded = O1+O2 (S1); architected = O2; contributed to = O5 (PA-18.2, S9); hands-on wording per S5. |
| Skills appear only if anchored (P/A for Summary/bullets) | Passed with REVIEW | Summary and bullets use only P/A skills (Java P, Spring Batch P, Spark A, AWS A). React, SQL and RHEL have no employer anchor (R2). |
| No CEW / SCV-CCD / vendor names / internal numbers (§7) | Passed | Not present: CEW, CCD, SCV, GMS, HCL, Zhang Heng. |
| Headline and Summary fit the family × lens (SM × BNK) | Passed (not checked against the JD) | Leader-of-leaders framing, regulated bank, hands-on. JD not in auditor inputs. |
| Summary is narrative; no stacked repetition | **Partly failed** | The Summary is three narrative paragraphs (167 words). Team leadership appears four times: Summary ¶2, Competencies row 1, A2, and UOB E2/E8. The customer-channel list repeats across Summary ¶3, Competencies row 3 and A3–A5 (acceptable as summary → detail). → R3 |
| British spelling consistent; JD titles quoted as written | Passed | Spelling checked with a regex scan (organisation, programme, prioritisation, licence, containerised, Centre). No American forms found. |
| Layout per 04; ≤ 3 pages; page numbers; no orphaned headings | Passed (04 not in auditor inputs) | 3 pages; "Page X of 3" footer; no orphans (render report and visual check); 17 keep-with-next paragraphs in the DOCX. |
| Text extractable; renders correctly as PDF | Passed | pdftotext extracts all text. The DOCX has no text boxes, drawings or VML shapes, and one table (Core Competencies). Carlito fonts are embedded. |
| File name per §10 | Passed | `wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0` matches the `[Family]_[Lens]_[Target]_V` pattern; "_draft" suffix marks the draft (OQ-R3 still open). |
| Three-dimension review delivered separately | Not performed | Out of auditor scope (drafter's analysis deliberately not read). |
| Change log | Not performed | Out of auditor scope (deliberately not read). |

---

## 3. Document checks (render report + PDF)

| Check | Result | Note |
|---|---|---|
| Page count ≤ 3 | ✅ 3 | Report and pdfinfo agree. |
| Page numbers | ✅ | "Page 1 of 3" … "Page 3 of 3" footer, seen on every page. |
| Heading orphans | ✅ none | Page 2 opens with PROFESSIONAL EXPERIENCE; page 3 opens with the AI Park block plus its bullets. |
| Bullets ≤ 3 lines | ✅ | No bullet exceeds 3 lines. |
| ≤ 1 in 5 bullets at 3 lines | ✅ 4 / 33 (12%) | 3-line bullets seen visually: Migration (A1), AI adopted (A7), UOB security/DR (E12), plus one more counted by the report. |
| Paragraphs ≤ 4 lines | ✅ (at limit) | Summary: three paragraphs of exactly 4 lines each. UOB scope line: 2 lines. |
| Page 1 = header + summary + competencies + achievements | ✅ | Seen on page 1; the report agrees ("page 1 holds all achievements: True"). |
| Line flags / lint | ✅ none | Per report. |
| Draft markup | ℹ️ 44 / 95 red runs (FF0000) | Expected for a draft (01 §10). The final file must be all black. |
| Visual verification | Performed at 70 dpi | All three pages viewed. Fine typography (exact wraps, kerning) was not checked at high resolution. |

---

## 4. Summary

**Counts (60 claims):** PASS **54** · REVIEW **5** · FAIL **1**

### Required fixes

**F1 (#58): certification on the batch hold list.**
- Delete "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006) · ".
- The line becomes: "PMP — in progress · Site Reliability Engineering (SRE) — formal training".
- Rename the heading "EDUCATION, CERTIFICATIONS & LANGUAGES" to "EDUCATION, TRAINING & LANGUAGES". Once the certificate is removed, no certification is held.

### For Wilson to decide

**R1 (#6): "retail lending" in Summary ¶2.**
- **Issue:** the record (02 §6.1, X-02, PA-04) and the UOB scope line say "retail *unsecured* lending". The shorter form could read as mortgages or secured lending.
- **Question:** keep "retail lending" for brevity?
- **Safe default:** "cross-border payments and retail unsecured lending".

**R2 (#16): Technical row includes "JavaScript (React)", "SQL" and "Linux (RHEL)".**
- **Issue:** all three are ✅ by your confirmation, but the skills inventory has no employer anchor for them (OQ-3.8; React "employer ❓").
- **Question:** where did you use React, and with which employer and period? Do SQL and RHEL apply to UOB?
- **Safe default:** keep SQL and Linux (RHEL), since CF-N6 is an explicit confirmation and [TPL] uses "Linux (RHEL)". Drop "JavaScript (React)" until you give an employer anchor.

**R3 (#18): "Multi-discipline leadership" achievement.**
- **Issue 1:** the make-up of VV's 140 ("of engineering, DevOps and data teams") is not on record. OQ-2.3 asks which functions it included; S3 confirms only the total headcount and the layered management.
- **Issue 2:** the bullet is scope only, with no outcome, and repeats the 25-engineer / squad-lead framing already in Summary ¶2, Competencies row 1 and UOB E2/E8.
- **Questions:** (a) which functions made up the 140? (b) keep this bullet, or free the space?
- **Safe default:** cut the clause, giving "…earlier led VV's 140-person technology organisation (total headcount), managed in layers through managers." Alternatively, delete the bullet and move the VV 140 fact into the VV role as "Led VV's 140-person technology organisation (total headcount) through managers;" (S3).

**R4 (#22): "Assess vendors' architecture, credentials and fit with existing systems".**
- **Issue:** the record supports "vendor technical evaluation" (02 §5) but not these specific criteria. "Credentials" is also ambiguous next to credential management.
- **Question:** are these the criteria you actually use when evaluating vendors?
- **Safe default:** "Lead technical evaluation of vendors, with decision or joint-decision authority on vendor selection and SOW/licence negotiation; chair governance of four IT service vendors."

**R5 (#45): VV big-data bullet.**
- **Issue:** the outcome clause "providing data analysis that supported business decisions" is not recorded in PA-12.
- **Question:** can you name what the analysis supported (e.g., merchant or operations decisions)?
- **Safe default:** use the 03 PA-12 safe wording: "Led the big-data team and built VV's data-analysis platform from scratch on Flume, Hive, MapReduce, Spark Streaming and Spark SQL."

### Non-blocking notes (no change required)

- **#12:** core-banking *integration* (S2) ≠ core-banking platform expertise. Keep that distinction at interview.
- **#35:** the 99% SonarQube gate's scope (new code vs all code) is undefined.
- **#36:** two ideas in one 3-line bullet. **#40:** six named technologies. Both are optional style trims.
- **#51:** 02 says the SaaS model was for *future* B2B/B2G customers.
- **#21:** OQ-1.9 (gaming type) is still open in the library; S9 wording is used.

---

## Resolution (2026-10-26)

| Item | Resolution |
|---|---|
| **F1** (#58 Software Designer certificate) | **Overruled** per Revision Brief §1.1 — verified document in 02 §3 [CERT-SS]; Session_Confirmations lists it as fine. Certificate line and section heading unchanged. |
| R1 (#6 retail lending) | Default applied — "cross-border payments and retail unsecured lending". |
| R2 (#16 React / SQL / RHEL) | Left for Wilson — React is a confirmed skill (✅), so the default (drop it) would remove a confirmed fact. Question: which employer and period for React; do SQL and RHEL apply to UOB? SQL and RHEL kept per the auditor's default. |
| R3 (#18 Multi-discipline leadership) | Default applied — functions clause removed; now "earlier led VV Technology's 140-person technology organisation through its managers" (canonical form). Left for Wilson: which functions made up the 140? |
| R4 (#22 vendor criteria) | Default applied — "Lead technical evaluation of vendors, with decision or joint-decision authority on vendor selection and SOW/licence negotiation; chair governance of four IT service vendors." Question kept for Wilson (actual criteria). |
| R5 (#45 VV big data) | Default applied — 03 PA-12 safe wording, trimmed to four technologies: "Led the big-data team and built VV's data-analysis platform from scratch on Flume, Hive, MapReduce and Spark." Question kept for Wilson (what the analysis supported). |
| Non-blocking #36 | Same claim was a FAIL in audit 01 (F1): role-based permissions removed and 99.9%+ scoped to "the real-time payment middleware" (X-01, PA-02.1). Bullet kept as one item. |
| Non-blocking #40 | AWS list trimmed to four services. |
| Non-blocking #35 | 99% gate scope listed for Wilson; no text change. |
| Non-blocking #51 | No change — 03 PA-16 §2 supports "SaaS model for B2B/B2G customers". |
