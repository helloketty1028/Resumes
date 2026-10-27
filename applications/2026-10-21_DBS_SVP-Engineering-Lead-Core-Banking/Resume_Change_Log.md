# Resume Change Log — wilson-2026_ATL_Bank_DBS_V1_0_0（DBS · SVP, Engineering Lead, Core Banking Technology）

- **输出：** `drafts/04/resume.json` → `drafts/04/out/wilson-2026_ATL_Bank_DBS_V1_0_0_draft.docx` / `.pdf` / `.txt` / `.report.md` / `.report.json`
- **日期：** 2026-10-21 · **状态：** 草稿（红字 = 与已批准简历非逐字一致的措辞）。终稿需 Wilson 批准后用 `--final` 重新渲染。

## 1. 底稿与定位

**底稿**（卡片指定：approved Talentvis JSON 的 UOB 架构块 + `Archi_Bank_LIB_V5`）

- **Talentvis JSON（已批准）：** 主要句子来源。UOB scope、hub 设计、延迟、P1–P3 事件、MVP 排序；GBD、VV、AI Park 条目；"Used to explaining technical choices…" 一句。
- **TEKsystems JSON（已批准）：** GBD scope 与架构句、干系人接口句、VV scope（短版）、AI Park 部门领导句。
- **TPL（已批准）：** Payment resilience 一句。
- **`Archi_Bank_LIB_V5`：** 只作定位参考，没有直接取句。原因是 LIB 中的 "Prior CTO"、"10M+ DAU"、Flink、"200+ regions"、"100+" 等均为 ⛔ 或禁用。
- **优先级：** 事实以 Brief §4 S1–S9 和 03 safe wording 为准。

**定位：ATL × BNK**

- 在 Tier-1 银行带交易处理平台团队，同时深度参与架构、设计与代码评审的工程负责人。
- 核心银行只写"集成"（S2），不写"拥有核心系统"。
- Deposits / GL 不写。Loans、Customer Management、Settlement 只用记录里的相邻措辞。

## 2. 逐段内容决定（来源 ID）

### Headline
"Hands-On Engineering Lead — Banking Transaction Platforms  |  Payments, Lending & Customer Data · Platform Modernisation"

- 目标岗位名为 Engineering Lead；不出现 CTO。
- 来源：卡片 headline，因版面原因改写，见 §3-1。

### Professional Summary（3 段，渲染为 3 / 3 / 4 行，共 150 词）

**第 1 段：** 首句回应 JD 核心要求（R1 + R2）："Engineering lead with 18+ years of software engineering experience, who leads teams while staying hands-on in architecture, solution design and code reviews."

- 来源：02 §1（18+）、S5 / X-04。
- 第二句交代 UOB VP 职位与 Tier-1、MAS-regulated 背景（02 §6.1）。

**第 2 段：** 规模与契合点。

- 25 名工程师、数百万账户（X-02）。
- 中枢与 customer-360 "both integrated with core banking"（S2）。
- 零售贷款服务与催收（PA-04.1）。
- ISO 20022 迁移（PA-01）。
- AI 代码评审投产（PA-07）。

**第 3 段：** 更早的职业弧线。

- Renren / Sohu / Baidu（PA-17–19；"high-traffic consumer internet" 取自 02 §4）。
- "head-of-technology and architect roles at start-ups and scale-ups (2016–2022)"（Talentvis 已批准措辞）。
- VV 140（S3，带 "(total headcount)"）。
- 干系人沟通句（Talentvis 已批准）。

### Core Competencies（7 行；行序按 JD Required 优先级）

1. **Banking Domains：** 支付发起与交易处理（ISO 20022、SWIFT、RTGS——RTGS 只作为支付类型，PA-01），零售贷款服务与催收（PA-04.1），customer-360（PA-05），integration with core banking（S2）。
2. **Engineering Leadership：** 经 squad leads / EMs 带队、辅导与 mentoring（X-02）；architecture and code reviews（X-04 / S5；[LIB] 📄）；"contributed to" bank-wide standards（PA-03.3，locked verb）。
3. **Architecture & Integration：** microservices、API、event-driven、high-concurrency、Apache Camel、legacy modernisation（skills inv. §2、§7）。
4. **Hands-On Engineering：** Java（concurrency、JVM）、Spring Boot / Cloud / Batch、React、SQL、MySQL、MongoDB、Redis、Kafka（skills inv. §1–4）。React 缺雇主锚点，所以只在此行出现，见 JD 分析 Q1。
5. **Cloud-Native & DevSecOps：** Kubernetes、Docker、AWS、Linux (RHEL)（skills inv. §5、CF-N6）；CI/CD + 99% SonarQube gate + 自动化回归 + 渗透测试（PA-03.2）；secure SDLC（PA-03.4）。
6. **Reliability & Performance：** disaster recovery (DR) and failover drills（PA-02.1）、high availability、latency tuning（PA-01.4）、Splunk（PA-02）、P1–P3 incident response and root-cause analysis (RCA)（X-06）。
7. **AI-Assisted Development：** headless Claude Code、human-in-the-loop、prompt A/B evaluation（PA-07.1 / 07.2 / 07.4；skills inv. §8）。

### Selected Achievements（7 条，顺序同卡片；3 行的 3 条，2 行的 4 条）

1. **Core-banking integration**（S2 + X-02 + PA-01.2 / PA-05.1）
   - "Lead the teams behind two platforms integrated with core banking"；"core banking executes settlement"；"daily account summaries … to support portfolio analysis"。
   - 3 行，原因：S2 是锁定措辞。
2. **Legacy modernisation**（PA-01.1）
   - 03 safe wording 去掉 "(MT-to-MX)"（Summary 已展开）和 "(TT, RTGS)"；日期、期限和 "no service interruption" 全部保留。
   - 3 行。
3. **Hands-on core code**（S6）
   - 逐字使用 S6 合并措辞，包括 concurrency control。
4. **Lending servicing and collections**（PA-04.1）
   - 逐字（黑字）。
5. **AI-assisted development**（PA-07.1 + S9 + PA-07.3 + PA-07.2）
   - 保留 "live since May 2026 after formal architecture and risk approval"、"estimated ~80%"、"the AI never approves or merges"。
   - 3 行。
6. **Payment resilience**（PA-02.1）
   - TPL 已批准原句（黑字）。
7. **Multi-squad leadership**（X-02 + PA-03.1 / 03.2）
   - "1:1s, mentoring and performance management"；"every release … CI/CD quality gates and SIT/UAT sign-off"。

### UOB（scope 1 行 + 11 条，三个小标题按卡片）

**Scope：** Talentvis 已批准（黑字）。

**Architecture & Engineering**

| # | 内容 | 来源 | 措辞 |
|---|---|---|---|
| UOB-1 | hub 设计 | PA-01.2 | Talentvis 原句，黑字，3 行 |
| UOB-2 | hands-on 做法 | S5 | 逐字，见 §3-5 |
| UOB-3 | 延迟 | PA-01.4 | 原句，黑字 |
| UOB-4 | customer-360 | PA-05.1 / 05.2 / 05.3 | 现职改为现在时 "Lead"；压缩到 2 行，保留 Cloudera 评估 |

**Delivery & Platform Ownership**

| # | 内容 | 来源 | 措辞 |
|---|---|---|---|
| UOB-5 | ISO 20022 项目交付 | PA-01.5 | RAID 改为平实的 "risks and dependencies"；去掉 "CBPR+"（行话，未展开）；steering 汇报移到 UOB-7，避免重复 |
| UOB-6 | MVP 排序 | X-02 | 已批准原句，黑字 |
| UOB-7 | 干系人接口 | TPL / TEK | 已批准原句，黑字；即卡片的 "C-RPT"，见 §3-9 |
| UOB-8 | 技术投资 / 供应商决策权与四家 IT 服务供应商治理 | X-02 + X-05 | 回应 JD "influence strategic technology decisions" |

**Reliability, Security & Governance**

| # | 内容 | 来源 | 措辞 |
|---|---|---|---|
| UOB-9 | P1–P3 事件；无独立 SRE 团队 | X-06 + PA-02.3 | Talentvis 合并原句，黑字 |
| UOB-10 | 安全控制 | X-01 | "MAS Technology Risk Management (TRM) guidelines" 首次展开 |
| UOB-11 | KPI 与 standards | PA-03.1 + PA-03.3 | MTTR 改写为 "mean time to recovery"；standards 用 "contributed to" |

### Golden Bridge（scope + 2 条）
- Scope：TEK 已批准，黑字。
- GBD-1：PA-10.1 / 10.2，TEK 架构句，黑字，含 API gateway、Kubernetes。
- GBD-2：PA-10.3 + S4，"Led a 40-person project team (total headcount)"，黑字。

### VV Technology（scope + 4 条；职位 Head of Technical Centre，S8）
- Scope：TEK 短版，黑字。
- VV-1：PA-11.1 + S3。去掉了 140，因为数字已在 Summary 出现（one fact, one place）。
- VV-2：PA-11.2 + S1。用 "integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments"，加 settlement-reconciliation 模块；不写卡组织直连。
- VV-3：PA-11.4，已批准原句。
- VV-4：PA-11.3 + PA-11.5，已批准原句。

### AI Park（2 条；职位 VP of Technical Department，S8）
- AIP-1：PA-16.1，TEK 原句，黑字，去掉 SaaS 分句。
- AIP-2：PA-16.4 + big-data 团队，Talentvis 原句，黑字；含 MongoDB，回应 JD 加分项。
- AI Park 微服务用 "Brought … into the architecture"（O2，Brief §3）。

### Earlier Experience（4 行，lead 文本逐字取自 Brief §3）
- **Hengshunyuan：** PA-15.1，~100k 峰值 DAU。
- **Baidu：** PA-17.1 + S1，"designed and coded Nuomi's payment-gateway integration with Alipay, WeChat Pay and UnionPay"。
- **Sohu：** PA-18.1 短版。
- **Renren：** PA-19 + S1，只写 Alipay 和 UnionPay，没有微信支付（2013 年才上线）。

### Education
4 行，逐字取自 Brief §3（黑字）。

## 3. 偏离卡片之处及理由

1. **Headline。** 卡片原句实测 516–521 pt，超出 510 pt 行宽，渲染为 2 行。改为 "Hands-On Engineering Lead — … · Platform Modernisation"（498.6 pt，1 行）。
   - "Hands-On" 移到岗位名前；"Platform Modernisation" 用 JD 原词。
   - 单列的 "Hands-On Architecture" 删去；"architecture" 在 Summary 首句、CC-3、ACH-2 中可见。
2. **Summary 第 2 段：核心银行集成的范围。** 卡片写的是 hub、贷款服务、customer-360 "all integrated with core banking"。但 S2（以及批次 C1 Q4 / Q4b）只确认了 hub 和 customer-360。所以简历只说这两套 "both integrated with core banking"；贷款平台单独写，不声称与核心银行集成（见 JD 分析 Q3）。
3. **Summary 第 3 段。** 卡片写 "head-of-technology roles (2016–2022)"。实际 GBD 是 Project Manager & Architect（01 §5："head-of-technology roles (2016–2020)"），所以用 Talentvis 已批准的 "head-of-technology and architect roles (2016–2022)"。React / MongoDB 按卡片要求只放 Competencies。
4. **Competencies 行序和标签。** Engineering Leadership 从第 6 行移到第 2 行，因为它对应 JD Required 第 2 条。标签改为 "Architecture & Integration"、"Hands-On Engineering"、"Cloud-Native & DevSecOps"（JD 原词，有证据支撑）、"AI-Assisted Development"（JD 原词）。同时删除与 Achievements 重复的事实："99.9%+ availability"、Blue/Green 细节、"AI never approves or merges"、"JVM tuning" 的第二次出现。
5. **ACH-3 = S6 only。** S5 整句移到 UOB-2，使 ACH-3 保持 2 行，并满足 Achievements "most 2 lines"。S5 的要点在 Summary 首句同样可见。
6. **ACH-6 没有加入 X-06 / RCA。** RCA 已在第 1 页 CC-6 出现，X-06 整句在 UOB-9。再加入会重复，也会让 ACH-6 变成 3 行。
7. **ACH-7 的质量门禁写成短语。** 99% SonarQube gate 放在 CC-5，保证同一事实只出现一次。
8. **VV 第 4 条。** 用 PA-11.3 / 11.5（CI/CD、Kubernetes 回滚、事件分级与应急预案）替代卡片 "if space" 的 PA-12 数据平台。理由：JD 要求 automated testing / CI/CD / operational readiness，未提及大数据。VV 条数仍为卡片的 4 条。
9. **"C-RPT"（卡片代号，未定义）** 理解为汇报与干系人类条目。选用 TPL / TEK 的 "primary interface between business stakeholders, product owners, operations, compliance, architects and engineering managers …"，因为它对应 JD "partner closely with business, product, and architecture teams"；没有用含 India / Thailand / Indonesia 的 Talentvis 版本（JD 未要求跨时区）。
10. **Golden Bridge 未单列 X-01。** X-01 放在 UOB-10，即当前、MAS TRM 场景。GBD 保留 2 条，符合卡片 2–3 条的下限。
11. **Sohu 未加 MongoDB。** 加上会变成 3 行。MongoDB 已由 AIP-2 和 CC-4 支撑；Sohu 行保留已批准句的重构部分。
12. **Renren / Baidu 加入 S1 支付接入。** 卡片未列，但 Brief §4 S1 写明"usable now"。它增加了与"交易处理"相关的亲手编码证据。

## 4. 排除项及理由

| 排除项 | 理由 |
|---|---|
| CTO / Chief Architect、CEW、SCV-CCD、MEPS+、vendor 名称 | Brief §3 禁写 / 01 §7 保密 |
| PA-01.7 hub 上下文句（含 MEPS+、CASA） | MEPS+ 禁写；CASA 不单独提（避免暗示 Deposits，见 JD 分析 Q4） |
| "~50 / ~20 core modules"（X-04 数字） | 本批不用（S5） |
| PA-07.5 ramp-up、PA-07.6 defects | ⛔ / ❓（C1、C3） |
| PA-08 eMemo 校验 agent、RAG 知识助手贡献（S9） | 与 JD 的核心银行 / 工程主线关联弱；篇幅优先给 AI code review |
| PA-06 VN eTax | 证据薄（📄，无日期与规模） |
| PA-02.2 MTTR 降幅 | 无数字（{…} 槽位不填） |
| X-06 中 "regulatory reporting to MAS" 分句 | UOB-9 采用 Talentvis 已批准的合并句（事件 + 无 SRE 团队），保持 2 行 |
| PA-10.2 "200+ countries"、10M DAU、"1,000+"、GBD "200+" | 禁写或 ⛔ |
| PA-12 VV 数据平台（Spark） | 卡片的 "if space" 项；被更贴合 JD 的 PA-11.3 / 11.5 替代 |
| PA-13 GMS | "GMS" 禁写；B2B 办公产品与 JD 无关 |
| PA-16.2 城市投标、PA-16.3 AI 识别 | 与 DBS 岗位无关（S7：投标只限 AI Park，且本岗不需要） |
| Hengshunyuan ~1,500 版权内容 | 与岗位无关，压缩为一行 |
| MAS FEAT、DPIA、CBPR+、TT、pain.002 | 行话，未必能展开；保留可读性（human-in-the-loop、secure SDLC 已覆盖实质） |
| 跨时区团队（India / Thailand / Indonesia）、5+ 年离岸管理 | JD 未要求；篇幅 |
| "Coach engineering teams on AI-assisted engineering" | 篇幅；辅导事实已由 ACH-7 / CC-2 覆盖 |
| Angular、OpenShift、Deposits / GL | 无证据或禁写（见 JD 分析 (e)） |
| Pureland（PA-20）、Crypto（X-03）、个人 App（PA-21） | 永不 / 按需 |

## 5. 渲染结果

**最终渲染**

- Layout OK: **True**。
- 页数 3；第 1 页含全部 Achievements；第 2 页以 PROFESSIONAL EXPERIENCE 开头；第 3 页以 EARLIER EXPERIENCE 开头；页脚有页码；无孤立标题。

**行数（`.report.json` 估算 + PDF 实测核对）**

- Headline 1 行；Summary 3 / 3 / 4 行；Competencies 每格 ≤ 2 行、标签单行。
- 30 条 bullet，其中 3 行的 5 条：ACH-1、ACH-2、ACH-5、UOB-1、EARLY-B。

**Lint：0 命中。** 不需要逐条说明。

**字数：1,262（Summary 150）。** 低于 1,350–1,550 的参考区间，没有凑字数。

**红字：43 / 93 runs 为红色。**

- 黑字（已批准原句）：UOB scope、UOB-1 / 3 / 6 / 7 / 9；ACH-4 正文、ACH-6；GBD 全部；VV scope、VV-3 / 4；AI Park 全部；Earlier 的 lead 文本；Education。
- 红字：Headline、Summary、Competencies、其余 Achievements 和 UOB 条目、VV-1 / 2、Earlier 正文。

**人工检查：** PDF 三页已栅格化后逐页查看。只看过 LibreOffice + Carlito 的渲染效果，没有在 Microsoft Word 中实测。

## 6. 渲染迭代记录

| 轮次 | 发现 | 处理 |
|---|---|---|
| v1（仅估算） | Headline 2 行；10 / 30 条为 3 行（上限 6） | 改写 headline；压缩 A7、UOB-4、UOB-10、AIP-1、Sohu；去掉 Competencies 中的重复事实 |
| v2（完整渲染） | Layout OK；Summary 第 2 段末尾单词孤行；AI Park 跨第 2 / 3 页 | Summary 第 2 段删 "regional"、"brought" 改 "put"；VV scope 换成已批准短版；VV-1 压到 1 行 |
| v3（终版） | CC-1 加入 "RTGS" 支付类型 | 重新渲染，各项检查不变，Layout OK: True |

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/04_Resume_Fact_Audit.md` (S5, C1, C4, D-1, D-2), `coldread/04_Readability_ColdRead.md`, `brief/Revision_Brief.md` §2. Helper scripts and the pre-revision JSON: `drafts/04/tmp/`.

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Summary P2 | "… on platforms serving millions of accounts: a payment-initiation hub … and a customer-360 platform, both integrated with core banking, and the technology for retail lending servicing and collections." | "Leads 25 onshore and offshore engineers across payment, customer-data and retail-lending platforms serving millions of accounts." | D-1 safe default (core-banking detail kept once, in Achievement 1) |
| Summary P3 | "built and re-architected high-traffic consumer internet platforms" | "built and re-architected consumer internet platforms" | S5 safe default |
| Summary P3 | "… 140-person technology organisation (total headcount). Used to explaining …" | "… 140-person technology organisation through its managers. Experienced in explaining …" | Cold-read 4.3 / suggestion 3; canonical VV summary form; cold-read "smaller wording" |
| Comp · Banking Domains | "Payment initiation and transaction processing (ISO 20022, SWIFT, RTGS)" | "Payment initiation, validation and status tracking (ISO 20022, SWIFT, RTGS)" | C1 safe default |
| Comp · Architecture & Integration | "Microservices and API design, event-driven integration, …" | "Spring Cloud microservices and API design, event-driven integration (Kafka), …" | C4 safe default (lead-level skills moved out of the Hands-On row) |
| Comp · Hands-On Engineering | "Java (…), Spring Boot, Spring Cloud, Spring Batch, React, SQL, MySQL, MongoDB, Redis, Kafka" | "Java (…), Spring Boot, Apache Camel, Spring Batch, React, SQL, MySQL, Redis" | C4 safe default (MongoDB dropped) |
| Ach · Core-banking integration | "a payment-initiation hub that sends validated payments downstream, where core banking executes settlement, and processes the results returned; … to support portfolio analysis" | "a payment-initiation hub that hands validated payments to core banking, which executes settlement, and processes the results returned; … for portfolio analysis" | Cold-read 4.1 / suggestion 2; canonical S2 sentences |
| Achievements order | Hands-on core code 3rd | Hands-on core code 2nd (after Core-banking integration) | Cold-read "Order" (JD's main requirement) |
| Ach · Legacy modernisation | "phased, Blue/Green-style coexistence deployment … MX-rich messaging … retired coexistence" | Canonical ISO 20022 sentence | Cold-read 4.2 / suggestion 1; Revision Brief §2 |
| Ach · Multi-squad leadership | "Lead two onshore/offshore platform teams through squad leads … and hold every release to CI/CD quality gates and SIT/UAT sign-off." | Cut | Cold-read "Cuts" (repeats Summary and UOB scope); audit D-1 team-scope repetition. Squad-lead leadership, mentoring and the quality gates stay in Competencies |
| UOB · MVP sequencing | "When the two platform lines' schedules conflict, agree MVP scope …" | Canonical MVP sentence | Cold-read 4.4 / suggestion 3 (tense, no subject); Revision Brief §2 |
| UOB · P1–P3 incidents | "Coordinate P1–P3 production incidents … SLIs/SLOs and Splunk-based monitoring" | "Coordinate P1–P3 incidents … service-level indicators/objectives and Splunk monitoring" | Revision Brief §1.3 acronyms ("production" dropped to keep the bullet at 2 lines; RCA is expanded on page 1) |
| GBD · scope line | "A multi-tenant SaaS platform for online-game businesses … VIP tiers, analytics and multi-channel payments." | "Multi-tenant SaaS for online-game businesses … VIP tiers and multi-channel payments." | Cut (approved S9 wording); one line saved so AI Park no longer splits across pages 2–3 |
| GBD · team | "Led a 40-person project team (total headcount), …" | "Led a 40-person project team, including outsourced staff, …" | Cold-read 4.3 / suggestion 3; canonical GBD sentence |
| VV · organisation | "Led VV's technology organisation and built its microservices platform from scratch, owning technology selection and budget." | Canonical VV sentence ("Led VV's 140-person technology organisation through its managers and built …, owning technology selection and the technology budget.") | Revision Brief §2 (same fact, same wording batch-wide) |
| AI Park · bullet 2 | "… achieving millisecond-level service processing; led the big-data team on HBase, MongoDB and Spark Streaming." | "… achieving millisecond-level service processing, and led the big-data team." | D-2 safe default |
| Earlier · Sohu | "(SSH to Spring MVC; memcached cluster to Redis cluster)" | "Led the re-architecture of the fifth-generation CMS onto Spring MVC and a Redis cluster, and delivered its OpenAPI messaging platform." | Canonical Sohu sentence ("Sohu's" dropped; the lead names Sohu) |

**Not changed:** Education certificate line; "integration with core banking" in the Banking Domains row (audit C1 confirms it is fine under S2); "Lending servicing and collections" achievement (only place with the lending detail; the JD lists Loans); "estimated ~80%".

**Rendered result (after revision):** 3 pages · Layout OK **True** · bullets 29, at 3 lines **5** (Ach Core-banking integration, Ach Legacy modernisation, Ach AI-assisted development, UOB hub design, Earlier Baidu) · words 1,228 (summary 130) · line flags none · lint hits 0 · pages rasterised and viewed; AI Park now wholly on page 2 (`drafts/04/tmp/pg-*.png`).

**For Wilson:** (1) Kafka / Spring Cloud: can you confirm current hands-on (P) depth (C4)? If yes they can return to the Hands-On row. (2) For "transaction processing", which reading applies: the hub's own transaction-processing modules (S6), or downstream processing outside the hub (CF-N4) (C1)? (3) Is the 99% SonarQube gate on new code or all code?


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K3 business team | Experienced in explaining technical choices in business terms to senior management and ste | Reports status, risks and decisions to senior management, the steering committee and the business team. | C3 answer K3 (2026-10-26) |
| K3 de-duplicate | engineering managers; present status, risks and decisions to senior management and steerin | engineering managers. | Merged into Summary K3 sentence (no stacking) |
| K5 SonarQube scope | 99% SonarQube coverage gate | 99% SonarQube coverage gate on all code | C3 answer K5 (2026-10-26) |
| PA-03.5 CRQ/CAB | — | Personally prepare the change request for every production release on both platform lines and present the go-l | C3: add PA-03.5 (03 v4.2, CONF 2026-10-26) — approved by Wilson |

**Independent C3 edit review (2026-10-26) — fixes applied:**

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| C3 review fix #9 | Reports status, risks and decisions to senior management, the steering committee and the b | At UOB, reports status, risks and decisions to senior management, the steering committee and the business team | Independent C3 review: paragraph opens "Before UOB" |
