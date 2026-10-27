# Resume Change Log — 06 Airwallex · Engineering Lead/Manager, Growth (SG/SH)

- **Output:** `resume source file (working copy)` → `wilson-2026_SM_Internet_Airwallex_V1_0_0_draft.docx` / `.pdf` / `.report.md`
- **Base:** `base_Talentvis_SM_Internet.json`（结构和大部分已批准句子）+ `base_TEKsystems_TPM_Internet.json`（Agile 治理、MVP 排序、混合交付、AI 代码评审成果句、VV 组织规模句）。没有读 `LIB_wilson-2026_Senior_Tech_Internet_LIB_V5_0_0.txt` —— 03、S1–S9 和已批准的 JSON 已经覆盖了所有需要的事实，而且按优先级 03 高于 [LIB]。
- **Positioning:** SM × INT。定位为亲手做设计和代码评审的工程负责人，面向消费级和 fintech 平台。按 Responsibilities 1–5 排序：带团队 → 和 PM 一起做方案 → hands-on 设计 / 代码评审，然后是消费级平台 / onboarding / 支付的背景。
- **Rendered result:** 3 pages · Layout OK: True · page 1 = header + summary + 7 competencies + 7 achievements · page 2 starts with PROFESSIONAL EXPERIENCE · 31 bullets, 5 at 3 lines · line flags: none · lint hits: 0 · words 1,229 (summary 157) · red runs 47/96 (= wording not verbatim in an approved resume — expected).

## 1. Headline / Summary / Competencies

| Item | Decision | Source |
|---|---|---|
| Headline | Card 06 headline used verbatim; estimated 1 line. "User Onboarding" rests on the KYC evidence (🔶; risk noted in the analysis) | Card; PA-10.2; S1 |
| Summary P1 | The first sentence answers the JD's core requirement (product requirements → designs, plans, working software). Career arc reuses TEK/Talentvis phrasing; "2016–2022 leading technology and delivery at start-ups and scale-ups" (no CTO) | 02 §4, §6; TEK summary |
| Summary P2 | 25 engineers + millions of accounts (scale on page 1); work with product owners; "stays close to the code". The AI service is mentioned **without** the ~80% figure, which stays in the achievements (merge, don't stack). "Through squad leads" moved to the UOB bullet | X-02; X-04/S5; PA-07 |
| Summary P3 | Consumer domains + KYC + wallet/card payments + cross-time-zone + languages. **Deviation from card:** "Agile/Scrum from scratch" and "launch to ~100k DAU" removed from the Summary because they appear in Achievements | PA-10.2; S1; X-02; 02 §1 |
| Competencies (7) | Order follows the JD: Leadership → Product Delivery → Hands-On → Consumer → Payments → Cloud & Data → AI-Assisted. **Deviations from card:** (a) React removed — the skills inventory has no employer anchor (01 §9 usage rule) → open question; (b) "goals, feedback and development plans" not used — the record says 1:1s, mentoring and performance management only (X-02) → open question; (c) "user onboarding" not used as a competency term — written as "hierarchical KYC identity verification and rule models" | Skills inventory §1–§5, §8; X-02 |

## 2. Selected Achievements (7)

| # | Label | Content decision | Source |
|---|---|---|---|
| 1 | Hands-on technical leadership | Merged S5 + S6 wording; no ~50/~20 module counts; concurrency control included (S6 closes C7 b) | S5, S6, X-04, PA-01.3 |
| 2 | Faster code review | TEKsystems approved sentence verbatim ("estimated ~80%" kept) | PA-07.1, PA-07.3 |
| 3 | User identity and onboarding rules | PA-10.2 **without "200+ countries"** (banned in this batch); "after benchmarking competitor apps" from PA-10 §4 [R22] 📄; bonus distribution/triggers trimmed (bonus incentives stay in the GBD bullet). **Deviation:** PA-10.1 short moved to the GBD experience bullet to avoid repetition | PA-10.2, PA-10 |
| 4 | Payments across wallets and cards | S1: Baidu Nuomi (O1+O2 "designed and coded") + VV-Life (O2 "architected", "integrating … payments", settlement reconciliation). Renren Mall's integration moved to its Earlier line so the bullet stays within 3 lines; no WeChat Pay under Renren; no card-scheme connectivity | S1 |
| 5 | Consumer product from 0 to 1 | PA-15.1 verbatim. **Deviation:** the card paired it with PA-11.4; kept separate (one idea, one employer) and PA-11.4 stays in VV experience | PA-15.1 |
| 6 | Engineering teams at scale | S3 + S4 + PA-10.3 (Agile/Scrum from scratch, CI on Jenkins and Amazon ECR); "(total headcount)" kept on both. **Deviation:** X-02 mentoring moved to the UOB "Team & Productivity" bullet | S3, S4, PA-10.3 |
| 7 | Mission-critical migration | PA-01.1/01.5: dates, SWIFT deadline, coexistence retired Aug 2026, no service interruption. "15-engineer team" dropped to stay at 3 lines | PA-01.1, PA-01.5 |

## 3. Experience

| Role | Decision | Source |
|---|---|---|
| UOB scope | Talentvis approved scope minus "serving millions of accounts" (already in Summary P2) | 02 §6.1 |
| UOB · Engineering & Design (3) | PA-01.2 (technologies moved into brackets, "digital and branch channels" shortened to "channels" to keep 2 lines); PA-01.4 verbatim; PA-05 shortened (10-engineer team, data models, personally built analysis module + Spring Batch; Cloudera evaluation dropped) | PA-01.2, PA-01.4, PA-05.2/05.3 |
| UOB · Delivery with Product (4) | TEK Agile-governance bullet rewritten to lead with "Work with product owners on backlog prioritisation and sprint planning" (JD resp. 6; product-owner interface is in TEK's approved stakeholder bullet / PA-01 §9); SIT/UAT tail dropped. X-02 MVP sentence verbatim. PA-03.1 + 03.3 (penetration/regression tail dropped). X-06 incident bullet (Talentvis approved). | TEK; X-02; PA-03; X-06, PA-02.3 |
| UOB · Team & Productivity (3) | X-02 leadership through squad leads/EMs + PA-03 §6 coaching; S9 go-live May 2026 + PA-07.2 human-in-the-loop + PA-07.4 prompt A/B; cross-team/cross-time-zone (PA-01 §9 stakeholders + X-02 regions) | X-02, PA-03, S9, PA-07.2/07.4 |
| Golden Bridge (3) | PA-10.1 verbatim; hybrid delivery (TEK approved) + budget/capacity/launch readiness; AWS deployment + X-01, trimmed to four AWS services (≤ 3–4 technologies rule) | PA-10.1, PA-10.3, PA-10, X-01 |
| VV (5) | Scope (Talentvis); PA-11.2 with "took part in product-strategy planning"; PA-11.1 without the 140 figure (already in Achievements) and without AWS (list trimmed); PA-11.4; PA-12 [R22] Spark stack only; PA-11.3 + PA-11.5 | PA-11.x, PA-12 |
| Hengshunyuan (1 + scope) | Full role as the card asked; new scope line "Own start-up: an audio-learning platform for workplace and early-childhood content" (PA-15 §1) so the bullet has context; PA-15.2 + stack (Talentvis) | PA-15, PA-15.2 |
| AI Park (2) | PA-16.1 (title prefix dropped because the title line already shows it; SaaS-model clause dropped for length); PA-16.4 | PA-16.1, PA-16.4 |
| Earlier (3) | Baidu PA-17.1 (Talentvis); Sohu PA-18.1 shortened (OpenAPI platform dropped for length); Renren PA-19 + S1 Renren Mall payment integration (Alipay, UnionPay) | PA-17.1, PA-18.1, PA-19, S1 |
| Education | 4 fixed lines verbatim | Brief §3 |

## 4. Exclusions (with reason)

| Excluded | Reason |
|---|---|
| PA-04.1 lending & collections bullet | Not relevant to Growth; lending is already named in the UOB scope line; length budget |
| X-05 vendor governance; X-02 commercial authority (investment, SOW/licence) | Buyer-side commercial authority is not asked for in an engineering-manager JD |
| PA-02.1 DR / 99.9%+; X-01 UOB security sentence | Bank-resilience emphasis is low priority for a Growth role; reliability is covered by X-06 |
| PA-08 eMemo validation agent; RAG contribution (S9) | Kept to one AI story (code review) so the AI message stays sharp; could be swapped in |
| PA-16.2 bids, PA-16.3 AI recognition | Not relevant; S7 bids are vendor-side pre-sales |
| PA-13 B2B online-office product; PA-18.2 publishing workflow; PA-06 VN eTax | Low relevance; length |
| React | No employer anchor (open question) |
| "200+ countries", 10M DAU, QPS, ~50/~20 modules, Flink, chatbot, ramp-up/defect metrics, hiring numbers, CTO, MEPS+, internal/vendor names, growth A/B frameworks | Banned or held (brief §3, 03 §0A) |
| PA-20 Pureland | Never included |

## 5. Open items carried to the analysis
React anchor · goals/development plans · AI review adoption scope (C4) · GBD business nature (OQ-1.9) · role still open / SG-only.

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/06_Resume_Fact_Audit.md` (PASS 50 · REVIEW 7 · FAIL 0), `coldread/06_Readability_ColdRead.md` (REVISE), `brief/Revision_Brief.md` §2 canonical sentences. No fact added. Pre-revision JSON kept at `drafts/06/tmp/resume.before.json`.

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Summary P1 | "start-ups and scale-ups" | "start-ups and technology companies" | Audit Sum-3 (default) |
| Summary P2 | "a Vice President at UOB" | "a Vice President (VP2) at UOB" | Cold-read (title consistency) |
| Summary P2 | "technical solutions, backlogs and release plans" | "technical solutions, roadmaps and release plans" | Audit Sum-5 (default) |
| Summary P3 | "…across time zones, in English and Mandarin." | "…across time zones; professional working proficiency in English and Mandarin." | Audit Sum-8 (default) |
| Competency · Product Delivery | "backlog prioritisation and sprint planning, Agile/Scrum" | "roadmaps, Agile/Scrum sprints" | Audit Sum-5/E-4 applied consistently (no backlog evidence in 03 or the skills inventory) |
| Ach · Hands-on technical leadership | "the payment hub's core modules — transaction initiation…" | "the payment-initiation hub's core modules — payment-transaction initiation…" | Cold-read (plain antecedent); S6 wording |
| Ach · Faster code review | "a Spring Boot service runs headless Claude Code agents on each pull request alongside SonarQube, cutting…" | "now live in a regulated bank: it reviews each pull request automatically, alongside SonarQube checks, and cut…" (estimated ~80%, 1–2 rounds kept) | Cold-read top-3 #1 (jargon) |
| Ach · Engineering teams at scale | "140-person … (total headcount) … 40-person project team (total headcount)" | "140-person technology organisation through its managers … 40-person project team, including outsourced staff" | Cold-read (readability); brief §2 VV/GBD readable qualifiers |
| Ach · order | Engineering teams 6th | Engineering teams 2nd | Cold-read (JD leads with team leadership) |
| Ach · Mission-critical migration | "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration… phased coexistence… MX-rich… was retired" | Brief §2 canonical ISO 20022 sentence | Cold-read top-3 #2 ("coexistence", "retired" unclear); brief §2 |
| UOB · Delivery with Product (E-4) | "backlog prioritisation and sprint planning … issue escalation and KPI-based progress reporting" | "scope, roadmap and release planning … RAID tracking and KPI-based status reporting" | Audit E-4 (default) |
| UOB · delivery KPIs | "MTTR … CI/CD quality gates (99% SonarQube coverage gate)" | "mean time to recovery … CI/CD quality gates" | Cold-read top-3 #3 (acronym; 99% parenthetical cut as a credibility snag, 03 C-note new-code vs overall still open) |
| UOB · P1–P3 incidents | "stakeholder communication, RCA … SLIs/SLOs and Splunk-based monitoring" | "root-cause analysis (RCA) … service-level indicators/objectives (SLIs/SLOs) and Splunk monitoring"; "stakeholder communication" cut for length | Cold-read #4 (acronyms); brief §1.3 |
| UOB · cross-team bullet (E-10) | "…and closely with teams in India, Thailand and Indonesia across time zones." | "Work with infrastructure, operations, compliance and architecture teams." | Audit X-1 (default; regions stay in Summary P3) |
| Golden Bridge · hybrid delivery (G-2) | "Waterfall for scope, budget and milestones; Agile sprints for execution, backlog tracking and iterative delivery" | "Waterfall for scope and budget, Agile sprints for execution" | Audit G-2 (default) |
| VV · big-data bullet (V-4) | "Led the big-data team on Flume, Hive, MapReduce, Spark Streaming and Spark SQL, providing data analysis that supported business decisions." | Deleted | Audit V-4 (unsupported outcome clause; PA-12 default would name 5 technologies) + cold-read cut (not relevant to Growth) |
| Hengshunyuan bullet | "Spring Cloud microservices stack with a MySQL cluster, Redis, Kafka and ELK" | "Spring Cloud microservices with a MySQL cluster, Redis and Kafka" | Audit §3 minor (≤ 4 technologies) |
| Earlier · Baidu | "…two months ahead of plan, leading the web front-end, CMS development and QA teams." | "…two months ahead of plan." | Cold-read cut; keeps 3-line bullets at 5/30 |
| Earlier · Sohu | "Led the fifth-generation CMS re-architecture (SSH to Spring MVC; memcached to Redis cluster)." | "Led the re-architecture of Sohu's fifth-generation CMS onto Spring MVC and a Redis cluster." | Brief §2 Sohu canonical (first clause only; the OpenAPI clause is not added, as 06 did not carry that fact) |

**Not applied:** cutting the "Software Designer (Intermediate)" certificate (overruled, Revision Brief §1.1); moving "Consumer Platforms" above Payments and Cloud & Data (already above them); any growth, funnel, experimentation, hiring or coding-share wording (would add facts).

**Consistency sweep (batch rule):** the permission matrix appears only with the payment-initiation hub, and no 99.9%+ figure is used. None of "(total headcount)", "Blue/Green", "MX-rich", "middle-platform", "high-traffic", "SSH to" or "RESTful" remains.

**Rendered result:** Layout OK: True · 3 pages · 30 bullets, 5 at 3 lines (17%) · 0 lint hits · 0 line flags · page 1 = summary + competencies + all 7 achievements; page 2 opens with Professional Experience.


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K1 scale-ups | start-ups and technology companies | start-ups and scale-ups | C3 answer K1 (2026-10-26) |
