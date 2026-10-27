# 05 — JD Keyword and Matching Rules

**Version:** v1.0 · 2026-10-16 · **Status:** ACTIVE DRAFT — ⚠️ / ❓ items await your decisions
**Role of this file:** How a job description is parsed, screened, matched to evidence, keyword-mapped, ordered and compressed into a ≤3-page tailored resume. **It holds no career facts** — it cites IDs from 02 and 03.
**Built from:** `master-career-profile.md` v2.2 §8 (gaps, fast-reject) · Master v1.0 §10 (library → role map) · six [LIB] V5 docx (ATS keyword pools, family gaps, tailoring guides — verbatim) · achievement library v3.1 role ratings · resume-tailor method · decisions of 2026-10-16.
**Decisions applied [CONF 2026-10-16]:** three role families (ATL / SM / TPM) × two industry lenses (BNK / INT) · **three-dimension review, no aggregate score** · skills inventory and fact-check stay auxiliary files.

---

## 1. Workflow per JD (with approval gate)

```
JD ─► §2 classify family × lens ─► §3 parse (required / preferred / inferred / eligibility)
   ─► §4 fast-reject screen ──(hit)──► report and stop unless you override
   ─► §5 evidence matrix (requirement → evidence ID → status → output location)
   ─► positioning recommendation (headline 02 §7.2, lead-with evidence, gaps handling)
   ─► ★ YOUR APPROVAL ★
   ─► draft resume per 01 + 04, ordering/compression per §6
   ─► three-dimension review (01 §8) + QA checklist (01 §9) + change log
```

## 2. Family × Lens Classification

| Signal in JD | Family |
|---|---|
| Owns architecture, system design, hands-on build, principal/staff/lead engineer, solution/payments/platform architect | **ATL** |
| Leads managers/orgs, budget, strategy, Head/Director/VP Engineering or Technology, engineering culture | **SM** |
| Delivery/programme/service ownership, RAID, release/change governance, vendor/SLA, steering reporting | **TPM** |

Mixed JDs: pick the family that owns most **required** criteria; borrow evidence from other families only where the JD asks for it.

| Employer type | Lens |
|---|---|
| Banks, financial institutions, regulators / FMIs (e.g. MAS, SGX), **fintech** | **BNK** [CONF 2026-10-16] |
| Internet platforms, e-commerce, SaaS, consumer tech | **INT** |
| Fintech scale-up hiring like an internet company | ⚠️ decide per JD (OQ-P2 in 02) |

**Lens emphasis** (📄 distilled from [LIB] guides):
- **BNK** — regulated delivery (MAS TRM, secure SDLC), resilience and DR, governance and vendor control, payments domain depth; bank terms kept.
- **INT** — 0-to-1 builds, scale and speed, product sense, engineering culture and developer productivity; bank-internal jargon (MAS TRM, CBPR+ abbreviations) removed or explained on first use.

### 2.1 The six cells

#### ATL × BNK — Architecture / Tech Leader, bank / fintech  (source `Archi_Bank`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** PA-01.2 · PA-01.3 · PA-01.4 · PA-02.1 · PA-07.1 · X-01 · PA-05.1–05.2

**ATS keyword pool (📄 verbatim [LIB]):** solution architecture · technical architecture · enterprise architecture · payments architecture · ISO 20022 · SWIFT · CBPR+ · RTGS · integration architecture · messaging · event-driven architecture (EDA) · microservices · distributed systems · API design · NFRs · low latency · high availability · resilience · disaster recovery · scalability · security architecture · encryption · MAS TRM · PCI-DSS · ISO 27001 · AWS · Kubernetes · Spring Boot · Spring Cloud · Apache Camel · Kafka · Java · architecture governance · architecture review

**Family-specific gaps (📄 verbatim [LIB]):**
- No TOGAF (most acute for EA roles): counter with "designed AND delivered" and architecture-review governance contribution; never claim.
- Core banking systems (e.g. Temenos, Finacle) and Murex — not in sources; do not list.
- PCI-DSS / ISO 27001 — working knowledge of control objectives only; no audit ownership.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 银行 Solution Architect：Headline 选 1；Highlights 以 Payments architecture、Payment-initiation hub、Designed and built、Resilience by design 开头。
- 支付专项架构师：Headline 选 2；UOB 部分保留全部 9 条 Programme 要点，CEW 链路描述（intro）必须保留。
- Tech Lead / Principal Engineer（偏 IC）：Headline 选 3；Performance 与 Designed and built 两条置顶，弱化管理类条目，Summary 删掉 "100+ engineers"。
- EA / Domain Architect：Headline 选 4；Architecture governance 与 Data architecture 前置，TOGAF 缺口按上面的口径处理。
- 数字资产托管 / 密钥管理类 JD：才拼入 Crypto 模块，并保留 knowledge-level 限定语。

#### ATL × INT — Architecture / Tech Leader, internet / tech  (source `Archi_Internet`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** PA-10.1 · PA-11.4 / PA-16.4 · PA-07.1 · X-04 · PA-12 ([R22] Spark version only) · PA-17.1

**ATS keyword pool (📄 verbatim [LIB]):** principal architect · solutions architect · platform architect · staff engineer · distributed systems · high concurrency · scalability · microservices · event-driven · Kafka · Flink · Spark · streaming · real-time data · multi-tenant SaaS · cloud-native · Kubernetes · AWS · API gateway · system design · performance · JVM · reliability · SRE · observability · security · MLOps · recommendation · GenAI · LLM · RAG · agentic AI · Java · Spring Cloud

**Family-specific gaps (📄 verbatim [LIB]):**
- Service mesh, GCP, Go/Rust — not in sources; do not list.
- Large-scale ML model training / GPU inference infrastructure — not claimed; position as data/MLOps and applied-AI architecture.
- Recent internet-company tenure — last internet role ended 2022; lead with architecture depth and the production AI system built at UOB to show currency.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 平台 / 分布式系统架构师：Headline 选 1；Highlights 以 High-concurrency、Event streaming、Hands-on depth 开头。
- SaaS 平台架构师：Headline 选 2；Golden Bridge 全部 9 条保留并前置 arch / build / core / global。
- Fintech 架构师：Headline 选 3；UOB Real-Time Payment Platform 全部 7 条保留，并补 Golden Bridge 的 KYC/支付。
- AI / 数据平台架构师：Headline 选 4；VV 的 adorder / causal / pipelines / genai 前置，UOB AI Code Review 整块上提。
- Staff / Principal Engineer（IC 岗）：去掉 Architecture leadership 一条和 Summary 中的管理头衔，突出动手条目。

#### SM × BNK — Senior Manager, bank / fintech  (source `Senior_Tech_Bank`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** X-02 · PA-01.1 · PA-03.1–03.3 · PA-07.1–07.3 · X-05 · PA-02.1

**ATS keyword pool (📄 verbatim [LIB]):** technology strategy · engineering leadership · Head of Engineering · Head of Technology · CTO · Technical Director · VP Engineering · multi-squad delivery · organisation design · platform modernisation · digital transformation · mission-critical systems · operational resilience · MAS TRM · regulatory compliance · stakeholder management · vendor management · technology roadmap · budget · SOW · engineering excellence · SDLC · DevOps · SRE · cloud · microservices · event-driven · ISO 20022 · CBPR+ · RTGS · payments · GenAI adoption · Responsible AI · MAS FEAT

**Family-specific gaps (📄 verbatim [LIB]):**
- Bank tenure ~4 years vs JDs asking 6–10 years in banking: counter with Tier-1 regulated delivery depth plus 18+ years total and payments-heavy fintech platforms.
- Largest current team is 20+ (two lines) vs JDs expecting 50–200: lead with the historic 100+ organisation and "leader of leaders" structure; do not inflate the UOB number.
- Treasury / FX / Murex / wealth core systems: not your domain — bridge via payments only when the JD lists them as adjacent; fast-reject if core.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 大型银行 Head of / Director 岗：Headline 选 1 或 2；Summary 用 A 版；Highlights 前 4 条固定用 Executive scope、Leader of leaders、Payments modernisation、Governance beyond own teams。
- AppDevMgr / VP Tech Lead 岗：Headline 选 3；保留 UOB 的 "hands-on" 与延迟调优相关条目（可从 Architect 素材库借）。
- AI 方向技术高管岗：Headline 选 4；把 AI Code Review 整块上提到 UOB 第一位，Highlights 第 1 条换成 Production AI。
- VV Technology 和 AI Park 在投递版各保留 6–8 条：优先 lead / delivery / arch / scale / data / genai（VV），lead / bids / rollout / arch / data（AI Park）。
- 控制长度：投递版 UOB 用 10–12 条，Golden Bridge 用 4–5 条，Hengshunyuan 用 1 条，更早经历 3 行。

#### SM × INT — Senior Manager, internet / tech  (source `Senior_Tech_Internet`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** PA-11.1 · PA-10.1 · PA-16.1–16.2 · PA-07.1–07.3 · PA-15.1 · X-02

**ATS keyword pool (📄 verbatim [LIB]):** Head of Engineering · VP Engineering · CTO · engineering leadership · scale-up · 0-to-1 · product engineering · platform engineering · high-scale distributed systems · microservices · event-driven · real-time data · Flink · Kafka · AWS · Kubernetes · CI/CD · SRE · developer productivity · DORA metrics · engineering culture · hiring and team building · GenAI · agentic AI · LLM · RAG · MLOps · recommendation · payments · fintech · marketplace · SaaS · multi-tenant · cost optimisation

**Family-specific gaps (📄 verbatim [LIB]):**
- Last 4 years in a bank may read as "slow corporate" to scale-ups: lead with 0-to-1 builds and the AI tool shipped inside the bank as proof of speed.
- Hiring at scale — not quantified in sources: describe as "built a 100+ person organisation"; do not invent hiring numbers.
- Consumer growth metrics (retention, conversion, GMV) — none in sources; do not invent. Use DAU, transaction volume and launch scope instead.
- Mobile apps: working familiarity with Swift/Kotlin only — do not claim native mobile leadership.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 投 scale-up CTO / VP Eng：Headline 选 2；Summary 用 A 版；Highlights 以 0-to-1、Scale、Organisation building、Engineering culture 开头。
- 投 fintech Head of Technology：Headline 选 3；把 Fintech depth 一条提到第 2 位，UOB 保留迁移与可靠性两条。
- 投平台工程 / 开发者效能负责人：Headline 选 4；AI Code Review 整块上提到 UOB 第一位，Highlights 加入 Engineering Productivity 能力行。
- VV Technology 是互联网版的主战场：投递版保留 8–10 条，Flink 广告订单与因果推断两条必须保留。
- UOB 部分投递版压到 8–10 条，去掉银行内部术语（MAS TRM、CBPR+ 缩写）或在首次出现时解释。

#### TPM × BNK — Technical Project Manager, bank / fintech  (source `TPM_Bank`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** PA-01.5 · PA-01.1 · X-06 · PA-02.3 · X-05 · PA-03.1–03.2

**ATS keyword pool (📄 verbatim [LIB]):** technical programme management · technical delivery manager · IT programme manager · project manager · multi-squad delivery · Agile · Scrum · Waterfall · hybrid · SDLC · scope · schedule · budget · RAID · risk management · dependency management · change control · release management · steering committee · executive reporting · stakeholder management · vendor management · SLA · SOW · UAT · SIT · cutover · migration · ISO 20022 · CBPR+ · SWIFT · RTGS · payments · MAS TRM · regulated delivery · incident management · RCA · service management · Jira · Confluence · MS Project

**Family-specific gaps (📄 verbatim [LIB]):**
- PMP / PMI-ACP / PRINCE2 — not yet held (PMP in progress). Lead with delivered programme outcomes; state "PMP — in progress" honestly.
- ITIL certification — none. Show service-management practice (SLA, incident, RCA, KPIs) instead; do not claim ITIL.
- "10+ interconnected payment domains" originates from the Stripe-tailored version — confirm it is not inflated before relying on it in interviews.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 银行 TDM / Delivery Lead：Headline 选 1；Highlights 以 Programme scale、Regulated migration、Production ownership、Commercial control 开头。
- 纯 IT Programme Manager（偏治理、偏 Waterfall）：Headline 选 2；把 C360（Waterfall 治理）和预算/SOW 相关条目前置。
- Run + Change 的服务交付岗：Headline 选 3；把 UOB 的 Production & Service Management 整块提到 Programme 之前。
- AI PM / Technical AI Manager：Headline 选 4；AI Code Review 与 AI-Enabled Delivery 合并上提到 UOB 第一位，Highlights 第 1 条换成 AI-enabled delivery。
- VV Technology 投递版保留 delivery / hybrid / lead / coord / devops / quality / arch / scale 等 8 条；AI Park 保留 lead / bids / rollout / features / data 5 条。

#### TPM × INT — Technical Project Manager, internet / tech  (source `TPM_Internet`)

**Lead-with evidence (🔶 proposal, from 03 ratings):** PA-10.3 · PA-11.2 · PA-16.2 · PA-07.1 · PA-03.1 · PA-01.5

**ATS keyword pool (📄 verbatim [LIB]):** technical program manager · TPM · program lead · cross-functional · roadmap · planning · dependencies · launch · release · Agile at scale · Scrum · risk management · stakeholder management · executive communication · engineering productivity · developer experience · CI/CD · DORA metrics · reliability · incident management · platform · payments · fintech · multi-region · 0-to-1 · AI program · LLM · agentic AI · data pipelines · Jira · Confluence

**Family-specific gaps (📄 verbatim [LIB]):**
- OKR practice — not in sources. Do not claim OKR ownership; keep the keyword as "planning" language only if the JD insists.
- Product-metric ownership (conversion, retention) — none in sources; frame outcomes as launch scope, scale, reliability and delivery metrics.
- PMP — in progress only.

**Tailoring guide (📄 verbatim [LIB]; "Headline 选 N" = Nth option in 02 §7.2):**
- 大厂 / 平台型公司 TPM：Headline 选 1 或 2；Highlights 以 Multi-team execution、Data-driven delivery、Launch quality 开头。
- 支付公司 TPM（Stripe、Adyen、Grab Financial 类）：Headline 选 3；把 UOB 迁移、Golden Bridge 200+ 地区 KYC/支付两条前置。
- AI Program Manager：Headline 选 4；UOB 的 AI 程序整块上提，VV GenAI chatbot 与 MLOps 条目前置。
- UOB 投递版保留 8 条左右，删除 MAS 等银行内部术语；VV 与 Golden Bridge 合计不少于 12 条，体现互联网交付节奏。

> ⚠️ The [LIB] guides predate the 2026-10-16 decisions. Where a guide points to material now ⛔ in 03 (e.g. "Programme scale / 10+ payment domains", "10M+ DAU", "Prior CTO" headlines, Flink items, the GenAI chatbot, "100+ engineers"), skip it — 03 status wins.

## 3. JD Parsing Rules

1. Split every JD statement into **Required**, **Preferred**, or **Inferred** (your own inference — always labelled as such).
2. Pull out **eligibility items** separately: work-pass / PR, security clearance, mandatory certifications (e.g. AWS, PMP, TOGAF), years in banking, language. Eligibility gaps stay visible — never worded around.
3. Record the JD's own terms for each requirement (for §5 keyword mapping).
4. Note seniority signals (band, reporting line, team size) to check against 02 (e.g. VP2 → ED band jump; current team 25).
5. If the JD URL cannot be read, say so and work only from text you were given; never pretend it was read.

## 4. Fast-Reject Screen (run before any tailoring)

Verbatim union of [LIB] and profile v2.2 §8 [CONF]:
C#/.NET primary stack · kdb+/q · Murex / Treasury-FX core · equity OMS core · manufacturing (AGV/AMR/FlexSim) · mandatory Azure/Databricks CDAO track · finance/CFO-domain AI · "cross-border" logistics (false-friend keyword) · SAS + public-sector policy authorship · GPU/model-inference infrastructure as a core requirement.

A hit is reported with the reason; you decide whether to continue.

## 5. Evidence Matrix and Keyword Mapping

**Matrix columns (one row per JD requirement):**

| # | JD requirement (JD wording) | Type (Req / Pref / Inferred / Eligibility) | Evidence ID (02 / 03 / skills inventory) | Status | Output location | Keyword used |
|---|---|---|---|---|---|---|

**Status values:** Direct · Transferable (state the bridge) · Gap · Unverified (❓ in 03 — cannot be used until confirmed).

**Keyword rules**
- Use the JD's own term only when the evidence truly supports it; otherwise keep it as a gap.
- No mention quotas, no keyword ceilings, no hidden or repeated keyword lists (01 §2 rule 10).
- Skills appear only if anchored in the skills inventory; depth P or A for Summary/bullets (01 §9).
- Synonyms: map JD terms to the record's terms (e.g. "production support" ↔ X-06/PA-02.3; "vendor management" ↔ X-05/X-02; "DORA metrics" ↔ PA-03.1) — the mapping lives in the matrix, not in the resume.
- A missing qualification and missing wording are different problems: fix wording only when the fact exists in 03.

## 6. Ordering and Compression

**Ordering**
1. Section order per 04 §4.
2. Experience reverse-chronological; within each role, bullets ordered by relevance to the JD's **required** criteria, then preferred.
3. Selected Achievements: 6–8 items taken from the cell's lead-with evidence (§2.1), each traceable to an ID.
4. Summary: narrative across the whole career (01 §6), framed by family × lens; must not repeat Selected Achievements word for word.

**Page budget (📄 from [LIB] tailoring guides; ≤ 3 pages total [CONF])**

| Block | Guide budget |
|---|---|
| UOB | 10–12 bullets (8–10 for INT versions) |
| Golden Bridge | 4–5 bullets |
| VV Technology | 6–8 bullets (8–10 for INT / data-heavy roles) |
| AI Park | 5–8 bullets |
| Hengshunyuan | 1 bullet / one line in Earlier Experience |
| Baidu, Sohu, Renren | 1 line each |

**Compression ladder (apply in order; never shrink fonts or margins below 04)**
1. Drop items rated ● for the family.
2. Merge duplicates across Summary / Selected Achievements / Experience (one fact, one place).
3. Shorten context/scope paragraphs to one line.
4. Move the oldest roles to Earlier Experience one-liners.
5. Trim the Core Competencies table to the rows the JD needs.

**Visibility of selective content**
- `on-request` only: Pureland (PA-20 — needs disclosure plan), Crypto/key-management (X-03 — knowledge-level qualifier mandatory), personal Android apps (PA-21).
- Every exclusion is listed in the review package with its reason (not in the resume).

## 7. Gaps and Honest Handling

### 7.1 General gaps (verbatim from `master-career-profile.md` v2.2 §8)

| Gap | Handling |
|---|---|
| Banking tenure ~4 years vs 6–10-year asks | Tier-1 regulated depth + payments specialism + 18+ years total |
| Current team 20+ vs 50–200 asks | Leader-of-leaders structure; historic 140-person team at VV (once confirmed) |
| No TOGAF / ITIL / cloud certification; PMP in progress | Show the practice (architecture governance, SLA/incident/RCA, AWS production delivery) |
| Internet tenure ended 2022 | Lead with 0-to-1 builds plus production AI built inside the bank |
| Treasury / FX / Murex / wealth core | Not his domain |
| Deep ML research | AI is positioned as applied delivery |

**Fast-reject signals [CONF]:** C#/.NET primary stack · kdb+/q · Murex / Treasury-FX core · equity OMS core · manufacturing (AGV/AMR/FlexSim) · mandatory Azure/Databricks CDAO track · finance/CFO-domain AI · "cross-border" logistics (a false-friend keyword) · SAS + public-sector policy authorship · GPU/model-inference infrastructure as a core requirement.

### 7.2 Gaps common to all six [LIB] families (📄 verbatim)
- AWS / cloud certifications — none. Anchor on hands-on AWS production delivery; open to certifying if a role requires it.
- Deep ML research / model training — not claimed. Position AI as applied delivery (agentic systems, LLMOps); the shipped production service is the proof.
- Fast-reject signals: C#/.NET primary stack · kdb+/q · Murex / Treasury-FX core · equity OMS core · manufacturing (AGV/AMR/FlexSim) · mandatory Azure/Databricks CDAO track · finance/CFO-domain AI · "cross-border" logistics (false-friend keyword).
- GCP — no depth; Azure — exposure only. Lead with AWS + cloud-agnostic patterns (Kubernetes, microservices).
- Service mesh (Istio/Envoy) — no hands-on experience. Do not list.
- TOGAF / formal architecture certification — none. Never claim; counter with "designed AND delivered in a Tier-1 regulated bank". Do not write "in progress" unless actually enrolled.

Family-specific gaps are listed per cell in §2.1.

## 8. Review Package per JD

1. Classification (family × lens) and fast-reject result.
2. Evidence matrix (§5).
3. Positioning recommendation → **approval gate**.
4. Tailored `.docx` (+ PDF check) per 04.
5. Three-dimension review (01 §8) — no total score.
6. Change log of material wording choices and exclusions.

## 9. Job-Search Filters ⚠️ (recorded, not enforced)

Your 2026-10-16 answer did not settle this, so the earlier filter is recorded **verbatim and not applied**:

> "Current job-search filter criteria: monthly salary S$12,000 and above, no contract roles (permanent/full-time only), targeting 'Head of Technical' / 'Head of Technical Development'-type tech leadership titles, excluding banks, preferring fintech companies or government employers." — [CONF, earlier session]

**Conflicts:** the MAS System Manager application is a contract role; the BNK lens and bank libraries exist; fintech is now grouped with banks. → **OQ-J1**

## 10. Retired Practices (history)

| Practice | Status |
|---|---|
| JD-fit percentage / scorecard score (e.g. "~78%") | Retired [CONF 2026-10-16] → three-dimension review |
| 40-keyword JD-to-asset mapping | Kept as the §5 matrix, without a fixed count |
| Seven resume families (banking-resume-optimizer) / four folders | Replaced by 3 families × 2 lenses [CONF 2026-10-16]; Big Data AI is a pillar, not a family |

## 11. Open Questions

| ID | Question |
|---|---|
| OQ-J1 | Job-search filters (§9): keep, change or drop? |
| OQ-J2 | Accept the proposed lead-with evidence per cell (§2.1)? |

## 12. Change Log
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-16 | Created. Workflow with approval gate; family × lens classification; six cells with verbatim [LIB] keyword pools, gaps and tailoring guides; parsing, fast-reject, matrix, keyword, ordering and compression rules; gaps (verbatim from v2.2 §8 + common [LIB] gaps); filters recorded as ⚠️; % scoring retired. |
