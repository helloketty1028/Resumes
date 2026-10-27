# Independent Fact & Quality Audit — Resume 09

**File audited:** `wilson-2026_ATL_Internet_NCS_V1_0_0_draft.txt` (pdftotext of the rendered PDF). I also viewed the PDF pages (3 pages rendered to PNG and looked at) and read the render report.
**Fact sources read (once each):** 01_Resume_Master_Rules v1.1 · 02_Candidate_Profile v3.1 · 03_Achievement_Library v4.1 · technical-skills-inventory v2.3 · fact-check-and-open-questions v2.4 · `Session_Confirmations.md` S1–S9 (`[CONF 2026-10-21]`). Not read, as instructed: cards, matching analysis, change log, resume.json, 04/05 files.
**Not verifiable:** the target JD (so JD-title spelling, JD keyword fit and 05 §2 lens fit are not checked).

Legend: PASS = traced to evidence with correct verb, scope and qualifier. REVIEW = judgement call for Wilson. FAIL = must be fixed or deleted.

---

## 1. Claim-by-claim table

| # | Resume text (shortened) | Evidence | Checks | Result | Fix / note |
|---|---|---|---|---|---|
| 1 | Header: "Wilson", Singapore PR, +65 8655 9547, email | 02 §1 (D-11, PR since 2024) | name, status, contact | PASS | None |
| 2 | Headline: "Solution Architect — Reusable Platforms & Integration Architecture \| Designed and Delivered in a Tier-1 Bank" | 02 §7.2 ATL; 01 §5 (headline may name the target role) | no CTO; "Reusable" see #12 | PASS | Target-role title only; "reusable" judged in #12 |
| 3 | Summary P1: "18+ years … designing scalable, reusable platforms and staying accountable … through delivery and production, across a Tier-1 bank, SaaS products and consumer internet" | 02 §4, §1 (18+); 03 §0A | number, framing | PASS | "Reusable" judged in #12 |
| 4 | "Began as an engineer and technical lead at Renren, Sohu and Baidu" | 02 §2 rows 7–9 (Senior R&D Engineer; Technical/Project Leader; Technical Specialist and project leader) | titles, sequence | PASS | None |
| 5 | "then spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups, building platforms from 0 to 1" | 02 §2, 03 §0A row "5 years as CTO", HR-1 ("head-of-technology roles (2016–2020)") | date range, titles, "scale-ups" | **REVIEW** | See Q1 |
| 6 | "Joined UOB in 2022 as a Vice President and leads 25 onshore and offshore engineers on payment and lending platforms" | 02 §2 row 1; 03 §0A (25), X-02 | title, number | PASS | None |
| 7 | "Designed the integration architecture of a payment-initiation hub that connects channels, reference data, vendor systems and core banking" | PA-01.2; S2 (hub sends validated payments to core banking) | O2 verb "Designed"; core banking = downstream, hub does not settle (CF-N4) | PASS | None |
| 8 | "reviews designs and code daily" | S5 / X-04 (daily review of core pull requests; co-designs solutions) | "reviews designs" not on record | **REVIEW** | See Q2 |
| 9 | "designs the security and resilience controls" | PA-01 §4 (designed the security controls); PA-02.1 (defined DR/failover) | O2 | PASS | None |
| 10 | "contributes to the bank's architecture-review governance" | PA-03.3, CF-15 locked verb | verb O5 | PASS | None |
| 11 | "Earlier platforms were built for reuse: a customisable multi-tenant SaaS platform on AWS at Golden Bridge" | PA-10.1; 02 §6.3; S9 | scope; "built for reuse" is interpretation | **REVIEW** | See Q3 |
| 12 | "…a shared back-end platform for a B2B product serving Southeast Asia at VV Technology" | PA-13 ("middle-platform architecture", 📄, outcome ❓) | "shared back-end platform" is a plain-English rendering of "middle platform"; reuse not documented | **REVIEW** | See Q3 |
| 13 | "At AI Park, led technical bids that won city projects" | PA-16.2 ✅; S7 | O2 verb; no pre-sales claim | PASS | None |
| 14 | "Explains technical choices in business terms to senior management and steering committees, and mentors engineers" | PA-01.5, PA-01 §9 (steering committee), X-02 (mentoring) | "in business terms" is not on record | **REVIEW** | See Q4 |
| 15 | Summary P3 repeats the multi-tenant SaaS, VV shared platform and AI Park bids that Selected Achievements 2, 3 and 5 state again | 01 §6 Merging, §9 | stacked repetition | **REVIEW** | See Q5 |
| 16 | CC "Solution Architecture": scalable, reusable platform design, multi-tenant SaaS, integration patterns, NFRs (latency, availability, security), technical sign-off through SIT/UAT and release | Skills §7; PA-01.4; PA-02.1; X-01; PA-03 §4 (required SIT/UAT sign-off) | depth A; "reusable" see #12 | PASS | Keyword-level; "sign-off" matches PA-03 §4 |
| 17 | CC "Integration & APIs": Java, Spring Boot and Apache Camel, API contracts and orchestration, event-driven, channel/vendor/third-party/core-banking integration | Skills §1–2 (P), PA-01.2, S2 | depth P | PASS | None |
| 18 | CC "Cloud-Native Architecture": Spring Cloud, Kubernetes, API gateway, AWS (ECS, RDS, DynamoDB, SQS/SNS), Kafka, Redis, CI/CD on Jenkins | Skills §2–5 (A or A/P; Kafka A/P) | depth ≥ A; GBD/VV/AI Park era, not UOB | PASS | Interview risk only: these are 2016–22 architecture-level skills, not UOB's stack |
| 19 | CC "Governance & Standards": … (contributed), "daily design and code reviews", quality gates, secure SDLC, MAS TRM (Singapore technology-risk rules) | PA-03.3, PA-03.2, PA-03.4; S9 (TRM wording approved) | "daily design … reviews" as #8 | **REVIEW** | See Q2 |
| 20 | CC "Risk & Resilience": RAID, API/database encryption, credential management, role-based permissions, DR and failover drills, 99.9%+, incident RCA | PA-01.5; X-01; PA-01.3(b); PA-02.1; X-06 | numbers, depth | PASS | "Risk and dependency logs (RAID)" is a shortened expansion; acceptable |
| 21 | CC "Stakeholders & Bids": technical bids, "explaining technical choices to business and senior stakeholders", steering-committee reporting, mentoring, cross-time-zone teams | PA-16.2; X-02; PA-01.5 | "business" wording as #14 | **REVIEW** | See Q4 |
| 22 | CC "Applied AI": production AI code-review service on headless Claude Code agents, AI document-validation agent, human-in-the-loop governance | PA-07.1/07.2, PA-08 (O1, Apr 2026), S9; skills §8 (P) | AI as pillar, not identity | PASS | None |
| 23 | SA1: "Led end-to-end design of a payment-initiation hub — API contracts, orchestration, validation, enrichment and status tracking — … handing payments to core banking for settlement" | PA-01.2; S2 | hub does not settle; wording says "handing … for settlement" | PASS | None |
| 24 | SA2: "Architected and delivered, from 0 to 1, a customisable multi-tenant SaaS platform on AWS for online-game businesses — KYC, bonus incentives, VIP tiers and multi-channel payments — on Spring Cloud and Kubernetes" | PA-10.1; S9 (approved GBD description) | O2+O3; no 200+; no real-money claim | PASS | None |
| 25 | SA3: "Designed the shared back-end platform architecture for VV's B2B online-office product serving Southeast Asia, and governed its solution design, cost evaluation, staffing and acceptance" | PA-13 | O2+O4; "middle platform" reworded | **REVIEW** | See Q3 |
| 26 | SA4: "Contributed to bank-wide SDLC, coding and code-review standards and to architecture-review governance; review core pull requests daily and co-design solutions with engineers" | PA-03.3; S5 | locked verb; S5 wording | PASS | Minor tense mix (past, then present) |
| 27 | SA5: "At AI Park, led technical bids that won city parking projects in Shijiazhuang, Handan and Beijing, and launched pilots … (2016) … (2017) … (2017)" | PA-16.2 ✅ verbatim; S7 | cities, dates | PASS | None |
| 28 | SA6: "Designed API and database encryption, credential management and **role-based permissions for payment, lending and customer-data platforms** under MAS TRM; personally led DR and failover drills, sustaining 99.9%+ availability" | X-01 (encryption, credential management, data migration across payment, lending, customer data); PA-01.3(b) (permission matrix is the payment hub only); PA-02.1 | scope: role-based permissions are evidenced only for the hub | **FAIL** | See Required fix 1 |
| 29 | SA7: "Designed and built an AI code-review service in a MAS-regulated bank that runs headless Claude Code agents on each pull request; live since May 2026 after formal architecture and risk approval, it advises but never approves or merges" | PA-07.1, 07.2; S9 | O1+O2; no ~80% figure; "each pull request" is the library wording (adoption scope C4 open) | PASS | None |
| 30 | UOB header: "United Overseas Bank (UOB) \| Singapore, Oct 2022 – Present; Vice President (VP2) / Technical Delivery Manager — Real-Time & Payment Data Services, Group Technology & Operations" | 02 §2 row 1 | exact title and dates | PASS | None |
| 31 | UOB scope: "two mission-critical platform lines in a Tier-1 bank operating under MAS TRM — cross-border payments and retail unsecured lending — serving millions of accounts" | 02 §6.1; 03 X-02 | no volumes, no names | PASS | None |
| 32 | "Personally built the hub's core modules — payment-transaction initiation, concurrency control, the corporate- and user-role permission matrix and processing of payment status results returned by downstream systems" | PA-01.3 ✅; S6 (concurrency control, closes C7b) | O1 verb "built" | PASS | `[CONF 2026-10-21]` |
| 33 | "Reduced end-to-end transaction latency under high load through thread-pool and JVM tuning and removal of synchronous blocking" | PA-01.4 📄 (no figure) | no invented number | PASS | None |
| 34 | "Led the 10-engineer backend team of a regional customer-360 platform that takes daily account summaries from core banking for portfolio analysis; evaluated Cloudera, designed the customer data models and personally built the Spring Batch jobs" | PA-05.1–05.3 ✅; S2; skills (Cloudera A "evaluated"; Spring Batch P) | 10 is a sub-total of 25; "Led", not "built", pairs with team size; no SCV-CCD name; launch ownership (C5) not claimed | PASS | None |
| 35 | "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration … architected a phased, Blue/Green-style rollout … went live in May 2025 and ended the parallel running in August 2026 with no service interruption" | PA-01.1; 03 §0A | dates, O3+O2 verbs, acronym expanded | PASS | None |
| 36 | "Own scope, roadmap, risks and dependencies, release planning and production rollout with a 15-engineer team, shipping upgrades every 2–3 months" | PA-01.5 | 15 = hub sub-total; cadence | PASS | None |
| 37 | "Established delivery KPIs … with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing) and SIT/UAT sign-off for every release" | PA-03.1, PA-03.2 📄 | 99% definition ❓ (new-code vs overall); qualifier not in library | PASS | Interview risk only |
| 38 | "Report status, risks and decisions to senior management and steering committees, and work closely with teams in India, Thailand and Indonesia across time zones" | PA-01.5; X-02 ✅ 2026-10-17 | no Board/C-suite; no US teams | PASS | None |
| 39 | "When the two platform lines' schedules conflict, agree MVP scope …" | X-02 safe wording, verbatim | — | PASS | None |
| 40 | "Coordinate P1–P3 production incidents end to end … with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring" | X-06; PA-02.3; CF-N3 | does not claim MAS reporting | PASS | None |
| 41 | "Lead two platform teams through squad leads and engineering managers, including mentoring; hold decision or joint-decision authority on vendor selection and chair governance of four IT service vendors" | X-02, X-05; S7 (buyer-side only) | "four" ✅; no vendor names | PASS | None |
| 42 | GBD header: Golden Bridge Drive (SG) Pte. Ltd., Nov 2020 – Jul 2022, Project Manager & Architect | 02 §2 row 3 | exact | PASS | None |
| 43 | "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution" | PA-10.2 (200+ countries correctly omitted, CF-11) | O2 | PASS | None |
| 44 | "Architected the AWS deployment (API Gateway, ECS, RDS, DynamoDB) and applied DPIA, API and database encryption and credential management; led data migration" | PA-10 §3, §6; X-01; skills §4–5 (A) | O2; DPIA ✅ GBD | PASS | None |
| 45 | "Led a 40-person project team (total headcount) with hybrid delivery … introduced Agile/Scrum and CI on Jenkins and Amazon ECR from scratch" | S4; PA-10.3 | "(total headcount)" kept; not "built" | PASS | None |
| 46 | VV header: Head of Technical Centre, Apr 2019 – Jun 2020 | S8 (supersedes 02 §2 "Development"); 02 §2 row 4 | title, dates | PASS | None |
| 47 | VV scope line: "VV-Life: a local-life services platform connecting offline merchants … through data" | PA-11 §1 | no blockchain/AI/10M DAU | PASS | Last word "data." sits alone on line 2 (cosmetic) |
| 48 | "Led VV's 140-person technology organisation (total headcount), running technology selection and the technology budget, and designed its microservices platform from scratch" | S3; PA-11.1 | qualifier kept; "Led", not "built"; 15–20 direct not claimed | PASS | None |
| 49 | "Designed for performance with Spring Cloud microservices, Kafka-based asynchronous processing and caching … millisecond level" | PA-11.4 ✅ verbatim | no % | PASS | None |
| 50 | "Delivered the first VV-Life release in 2019, including a payment subsystem that integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation" | PA-11.2; S1 | no direct card-scheme connectivity claimed | PASS | None |
| 51 | "Introduced CI/CD, code standards and containerised deployment with rollback on Kubernetes; defined production-incident priority levels and tiered emergency-response plans" | PA-11.3, PA-11.5, CF-N8 | — | PASS | None |
| 52 | AI Park header: VP of Technical Department, Apr 2016 – Sep 2017 | S8; 02 §2 row 6 | title, dates | PASS | None |
| 53 | "Led architecture, delivery, budget and the technical team for a smart-parking IoT platform connecting car parks to the cloud; introduced a SaaS model for business and government customers" | PA-16.1; 02 §6.6 ("future B2B/B2G customers") | "future" dropped | **REVIEW** | See Q6 |
| 54 | "Brought Spring Cloud microservices into the architecture, with Kafka … millisecond-level service processing" | PA-16.4 ✅ verbatim | no 10M DAU, no 1,000+ | PASS | None |
| 55 | Hengshunyuan — Co-founder (Oct 2017 – Sep 2019): "Owned product, architecture and delivery … ~1,500 licensed audio titles … ~100k daily active users" | 02 §2 row 5, D-10; PA-15.1/15.2 | "~" and "peak" kept; single-source [R22] | PASS | Overlap with VV deliberately unannotated (D-10) |
| 56 | Baidu — Technical Specialist (May 2014 – Dec 2014): project leader, Dubbo re-architecture, "two months ahead of plan"; "designed and coded payment-gateway integration with Alipay, WeChat Pay and UnionPay" | 02 §2 row 7, PA-17.1; S1 | months 📄 (year ✅); S1 O1+O2 | PASS | None |
| 57 | Sohu.com — Technical Leader / Project Leader (Mar 2012 – May 2014): CMS re-architecture to Spring MVC and Redis cluster; OpenAPI messaging platform | 02 §2 row 8; PA-18.1 | title, dates | PASS | None |
| 58 | Renren — Senior R&D Engineer (Jul 2008 – Mar 2012): shopping site, Renren Mall, CRM; "designed and coded Renren Mall's payment integration with Alipay and UnionPay" | 02 §2 row 9; PA-19; S1 | no WeChat Pay under Renren (correct) | PASS | None |
| 59 | Master's, Computer Science and Technology — Liaoning University (2005 – 2008) | 02 §3 | exact | PASS | None |
| 60 | Bachelor's, Applied Mathematics — Shenyang University of Technology (2000 – 2004) | 02 §3 | exact | PASS | None |
| 61 | Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006) | 02 §3 [CERT-SS]; session note says allowed | no ID numbers or DOB | PASS | None |
| 62 | "PMP — in progress · Site Reliability Engineering (SRE) — formal training" | 02 §3; CF-N5 | not "certified"; training not certification | PASS | Grouped on the same bullet as the certificate; clear labels, acceptable |
| 63 | Languages: English and Mandarin (professional working proficiency) | 02 §1 | — | PASS | None |

---

## 2. 01 §9 QA checklist

| Item | Status | Note |
|---|---|---|
| Every bullet traces to 03/02; no ❓/⚠️/⛔ outside permitted parts | **Failed** | One scope extension (#28). Other ❓ items (GBD business nature, 99% gate definition, Spring Cloud depth) are used only in approved or qualifier-safe wording. |
| Dates and titles match 02 §2 / S8 exactly; no CTO / Chief Architect | Passed | VV and AI Park per S8; Baidu months 📄. "Solution Architect" appears only as the target headline. |
| Every number matches 03 §0A (or S1–S9) with qualifiers | Passed | 18+, 25, 15, 10, 40 and 140 with "(total headcount)", 99.9%+, 99%, 2–3 months, four vendors, ~1,500, ~100k, 2 months ahead. No ~50/~20 modules, no ~80%. |
| Verbs match ownership level | Passed | O1 "built" used only where coded. "Led end-to-end design" and "Established KPIs" are the library's own wording. |
| Skills anchored at depth P/A | Passed | Spring Cloud/Kafka/SQS are A/P ❓, so depth is at least A. Cloudera stays "evaluated". No Flink, Go, RAG, Istio. |
| No CEW / SCV-CCD / CCD / GMS / HCL / vendor names / internal numbers | Passed | Checked the whole text. |
| Headline and Summary fit chosen family × lens (02 §7) | Passed (partly) | ATL framing is consistent with 02 §7. Fit to the INT lens and 05 §2 not verified (05 and JD not read). |
| Summary narrative; no stacked repetition with Achievements/Experience | **Failed (minor)** | Summary P3 restates SA2, SA3 and SA5; daily review appears in Summary, a competency and SA4. See Q5. |
| British spelling consistent; JD titles quoted as written | Passed / Not performed | Spelling consistent (customisable, organisation, containerised, centre). JD title spelling not checked (no JD). |
| Layout per 04; ≤ 3 pages; page numbers; no orphaned headings | Passed (partly) | 3 pages, "Page n of 3" footer, no orphan headings. 04 itself not read. |
| Text extractable; renders as PDF | Passed | pdftotext returns clean text; Carlito fonts embedded; all 3 pages viewed. The DOCX was not opened, so text-box use is not verified. |
| File name per 01 §10 | Passed | `wilson-2026_ATL_Internet_NCS_V1_0_0_draft`. OQ-R3 on the Lens segment is still open. |
| Three-dimension review and change log delivered | Not performed | Outside this audit's inputs. |

---

## 3. Document checks (render report + PDF viewed)

- **Pages:** 3 (limit 3). Page 1 holds header, Summary, Core Competencies and all 7 Selected Achievements. Page 2 starts with Professional Experience. Page 3 holds Earlier Experience and Education and is about one third full.
- **Footer page numbers:** present on all pages. **Orphan headings:** none. **Line-limit flags:** none.
- **Bullets:** 30 bullets, 5 at three lines (SA1, SA7, UOB ISO 20022, Hengshunyuan, Baidu), about 1 in 6, which is within the "about one in five" limit. None exceed 3 lines. Paragraphs are at most 4 lines (Summary P2 has 4).
- **Cosmetic widows:** Summary P1's last line is the single token "1." ("from 0 to / 1."). The VV scope line wraps the single word "data." (non-blocking polish).
- **Red text:** 52 of 92 runs are red, which is correct for an unapproved draft (01 §10). The final must be all black.
- **Presentation note:** Hengshunyuan (Oct 2017 – Sep 2019) sits under "Earlier Experience" after AI Park (2016–2017) and VV (2019–2020), so the main list is not in strict reverse-chronological order. This is not a fact error.

---

## 4. Summary

**Counts (63 claim rows): PASS 52 · REVIEW 10 · FAIL 1**
QA checklist: 2 Failed (one fact, one style), 2 Not performed or partial (JD/05/04/DOCX not in scope).

### Required fixes
1. **SA6 "Secure by design" (claim #28): FAIL, scope extension.** Role-based permissions are evidenced only for the payment hub (PA-01.3b). The sentence extends them to lending and customer-data platforms. Replace with:
   "Designed API and database encryption and credential management for payment, lending and customer-data platforms under MAS TRM; personally led DR and failover drills, sustaining 99.9%+ availability."
   If Wilson wants to keep permissions, use instead: "…credential management for payment, lending and customer-data platforms, and the payment hub's role-based permission matrix, under MAS TRM; personally led DR and failover drills, sustaining 99.9%+ availability." This may push the bullet to three lines, which makes 6 of 30. The Core Competencies "role-based permissions" keyword stays valid.
2. QA failure on stacked repetition is carried as a REVIEW (Q5), not a FAIL, because it is a style rule.

### For Wilson to decide (REVIEW)
- **Q1 (#5): "2016–2022 in head-of-technology and architect roles at start-ups and scale-ups".** The locked wording is "head-of-technology roles (2016–2020)". GBD (2020–22) was Project Manager & Architect, and "scale-ups" is not on record. Is the range defensible as written? *Safe default:* "then held head-of-technology roles (2016–2020) and a project-manager-and-architect role (2020–2022) at start-ups, building platforms from 0 to 1."
- **Q2 (#8, #19): "reviews designs and code daily" and "daily design and code reviews".** S5 supports daily review of core pull requests and co-designing solutions, not daily design review. Do you review designs daily? *Safe default:* "reviews core pull requests daily and co-designs solutions with engineers" (Summary), and "daily code review and solution co-design" (competency row).
- **Q3 (#11, #12, #25): "built for reuse", "Reusable Platforms" and "shared back-end platform" for the VV 中台 (middle-platform) design.** Reuse is an interpretation, not a documented fact, and GMS has no recorded outcome. Are you comfortable defending "reusable" in interview, and is "shared back-end platform" a fair plain-English rendering of "middle platform"? *Safe default:* keep "reusable" only for the multi-tenant SaaS and the hub (one hub serving several channels), and write the VV item as "Designed the middle-platform architecture (shared services layer) for VV's B2B online-office product…".
- **Q4 (#14, #21): "explains technical choices in business terms".** Steering-committee reporting and mentoring are documented. "In business terms" is not. *Safe default:* "Reports status, risks and decisions to senior management and steering committees, and mentors engineers."
- **Q5 (#15): Summary P3 repeats SA2, SA3 and SA5.** Rule 01 §6 asks to merge, not stack. Do you want P3 condensed? *Safe default:* "Earlier platforms, from multi-tenant SaaS to a shared B2B back-end, were designed for reuse, and technical bids at AI Park won city projects. Reports technical choices to senior management and steering committees, and mentors engineers." Or drop the platform sentence and keep only the bids and stakeholder sentences.
- **Q6 (#53): AI Park "introduced a SaaS model for business and government customers".** 02 §6.6 says "future B2B/B2G customers". Were there actual customers on the SaaS model before Sep 2017? *Safe default:* "introduced a SaaS model aimed at business and government customers."

### Non-blocking polish
- Fix the "1." widow in Summary P1, for example "building platforms from 0 to 1" becomes "building 0-to-1 platforms".
- Fix the single-word "data." wrap in the VV scope line.
- Consider moving Hengshunyuan into the main Experience list, or renaming "Earlier Experience", so the chronology reads cleanly.
- Fix the tense mix in SA4 ("Contributed … ; review …").
- Interview risks, not resume errors: the 99% SonarQube gate's definition (new-code vs overall) is open, and the cloud-native competency row reflects 2016–22 architecture work rather than UOB's current stack.

---

## Resolution (2026-10-26)

**FAIL**
- **F1 / claim #28 (SA6 "Secure by design"): fixed.** Applied the auditor's first replacement, without the permission matrix. The permission-matrix variant was not used: UOB bullet 1 already states the permission matrix, so it would repeat a fact and add a 3-line bullet. Coordinator consistency rule also applied: 99.9%+ is now attached only to the payment hub and middleware. Final text: "Designed API and database encryption and credential management for payment, lending and customer-data platforms under MAS TRM; personally led DR and failover drills keeping the payment hub and middleware at 99.9%+ availability."

**REVIEW**
- **Q1 (#5): default applied.** Summary P1 now reads "held head-of-technology roles (2016–2020) and a project-manager-and-architect role (2020–2022) at start-ups, building 0-to-1 platforms". "Scale-ups" is removed. *For Wilson:* is "start-ups" a fair label for all of AI Park, Hengshunyuan, VV and Golden Bridge?
- **Q2 (#8, #19): default applied.** "Reviews designs and code daily" is removed from the Summary. The daily review now appears only in SA4 ("reviews core pull requests daily and co-designs solutions with engineers"). The competency row reads "daily code review and solution co-design". *For Wilson:* if you do review designs daily, the original wording can come back.
- **Q3 (#11, #12, #25): partly applied, rest left for Wilson.** "Built for reuse" is removed. "Reuse" is now claimed only for the multi-tenant SaaS and the payment hub ("a payment hub that serves several channels"). The VV item keeps "shared back-end platform", because that is the canonical §2 sentence Wilson approved; "middle-platform" is not used. *For Wilson:* are you comfortable defending "reusable" for the SaaS platform and the hub in interview?
- **Q4 (#14, #21): default applied.** Summary and competency row now say "reports status, risks and decisions to senior management and steering committees". *For Wilson:* resume 10 still says "explaining technical choices in business terms" (it passed audit 10). Should all resumes use one wording?
- **Q5 (#15): default applied (variant).** P3 is condensed and no longer repeats SA2 or SA3. Daily review and architecture governance are removed from the Summary (they stay in SA4).
- **Q6 (#53): default applied.** "Introduced a SaaS model aimed at business and government customers." *For Wilson:* were there paying business or government customers on the SaaS model before Sep 2017?
- **Claim #48 (VV): note.** The canonical §2 VV sentence replaces "designed its microservices platform", and the text now reads "built its microservices platform from scratch" (Wilson-approved wording). *For Wilson:* did you personally build it (O1), or lead the build (O2)?

**Certificate:** "Software Designer (Intermediate)" is kept unchanged (verified, 02 §3). No item asked to remove it.

**Non-blocking polish:** the "1." widow is fixed (Summary P1), and so is the "data." widow (the VV scope line is now one line). The SA4 tense mix is fixed. Hengshunyuan placement is unchanged (D-10 and the brief's order). The interview risks still stand (99% gate definition; the cloud-native row reflects 2016–22 work).
