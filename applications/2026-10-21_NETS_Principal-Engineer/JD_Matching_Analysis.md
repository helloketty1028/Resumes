# JD Matching Analysis — NETS · Principal Engineer (JobStreet 95218038)

- **简历文件：** `drafts/01/out/wilson-2026_ATL_Bank_NETS_V1_0_0_draft.docx`（+ `.pdf`）· 源数据 `drafts/01/resume.json`
- **JD：** `jd/full/01_NETS_JD.md`（全文，2026-10-20 抓取）· 定位卡 `cards/01.md`
- **日期：** 2026-10-21 · 起草依据：Drafting Brief §1–§8、01/02/03/05、skills inventory、fact-check、两份已批准 JSON、Archi_Bank [LIB]
- **Batch match score（卡片数值，用户要求的覆盖率公式 Direct 1 / Transferable 0.5）：87** —— 原样照抄，未重新计算；本文其余部分不打总分、不用百分比。

---

## (a) 分类：Family × Lens

**ATL × BNK**（Architecture / Tech Leader × bank/fintech）。

- **Family = ATL：** JD 的核心是 "senior technical authority" —— 定义目标架构、做 "technical design authority"、审批方案与源代码、在关键生产问题上 "remain hands-on"，并要求 "substantial hands-on software development experience"。这些 Required 项绝大多数落在 ATL。JD 也含 SM/TPM 成分（带团队、组合/资源规划、绩效面谈、跨多条交付线），按 05 §2 "取拥有最多 Required 的 family，其余按 JD 要求借证据" 处理：管理与交付证据放在 UOB 经历后半段（UOB-5、UOB-8、UOB-10、UOB-11），不做主线。
- **Lens = BNK：** NETS 运营新加坡全国借记卡网络（受 MAS 监管的支付网络运营方），客户是 DBS/OCBC/UOB 等银行 —— 属于 FMI / 支付机构，按 05 §2 归 BNK。保留银行术语（MAS TRM、ISO 20022、SWIFT），首次出现时解释。
- **LIB 裁剪指引（Archi_Bank, Principal Engineer 偏 IC）：** "Performance 与 Designed and built 两条置顶，弱化管理类条目，Summary 删掉 100+ engineers" —— 已遵循：Ach-1/Ach-2 为设计与亲手编码，Ach-4 为性能；Summary 不写 140 人组织（只在 VV-1 出现）。

## (b) Fast-reject 与资格

- **Fast-reject（05 §4）：未命中。** JD 不含 C#/.NET 主栈、kdb+/q、Murex/Treasury-FX、equity OMS、制造业、强制 Azure/Databricks、CFO 域 AI、物流 "cross-border"、SAS 公共政策、GPU 推理基础设施。Solace JMS、POS/交换/卡组织对接属于**缺口**，不是 fast-reject 信号。
- **学历：** JD 要 "Bachelor's degree in Computer Science, IT, Software Engineering, or a related technology discipline"。Wilson 本科 Applied Mathematics（相关的定量学科）+ 硕士 Computer Science and Technology —— 满足（硕士直接对口）。
- **年限：** ≥10 年 → 18+ 年 ✅。
- **工作资格：** JD 未写国籍/许可要求；Wilson 为 Singapore PR，工作地 Braddell 无问题。
- **职级信号：** 职位要求 "guide a dynamic technical team"、绩效面谈与教练 —— 与 Wilson 现职（VP2，经 squad lead/EM 带 25 人）相符；薪资未公开，无法判断档位落差。
- **标题风险（需知悉）：** JD 要求 "substantial experience as a Principal Engineer, Solution Architect, Engineering Lead, Engineering Manager, or technical authority"。Wilson 的正式头衔是 Technical Delivery Manager / Project Manager & Architect / Head of Technical Centre / VP of Technical Department —— 没有 "Principal Engineer" 或 "Solution Architect" 头衔。HR 粗筛可能把 UOB 头衔读成"交付经理"。处理：Headline 写目标职位，Summary 第一句与 Ach-1/Ach-2 以架构所有权和亲手编码开头；头衔本身一字不改。

## (c) Evidence matrix（JD Requirements 逐条；复合要求拆分为子行）

位置代码：Sum-P1–P3 = Summary 段落 · Comp-1–7 = Core Competencies 行 · Ach-1–7 = Selected Achievements · UOB-1–11 / GBD-1–3 / VV-1–4 / AIP-1–2 = 经历要点（scope = 角色说明行）· Earl-H/B/S/R = Earlier Experience（Hengshunyuan/Baidu/Sohu/Renren）· Edu = 学历。

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | Bachelor's in CS / IT / SE or related discipline | Elig | 02 §3 | Direct — Master's in Computer Science and Technology; Bachelor's in Applied Mathematics (related) | Edu | "Master's degree in Computer Science and Technology" |
| 2 | ≥10 yrs progressive tech experience, substantial experience as Principal Engineer / Solution Architect / Eng Lead / EM / technical authority in a medium–large org | Req | 02 §1–§2 (18+ yrs); S5; PA-01.2; X-02; S3; 02 §6.3–6.6 | Direct for scope (architecture ownership + team leadership in a Tier-1 bank; heads of technology 2016–2022); no formal "Principal Engineer" title (see (b)) | Headline; Sum-P1/P2/P3; titles | "Hands-on technical lead", "solution architecture", "18+ years", "head-of-technology and architect roles" |
| 3 | Leading large-scale development / modernisation / migration programmes across multiple teams, vendors and concurrent delivery tracks | Req | PA-01.1, PA-01.5, X-02, X-05 | Direct | Ach-3; UOB-5; UOB-8; Sum-P2 | "ISO 20022 (SWIFT MT-to-MX) migration", "coexistence", "four IT service vendors", "two platform lines" |
| 4a | Enterprise application architecture — Java and Spring Boot | Req | skills inv. §1–§2 (P); PA-01 §3; S6 | Direct | Sum-P1; Comp-2; UOB-4; VV-3 | "Java", "Spring Boot" |
| 4b | RESTful APIs | Req | PA-01.2 ("API contracts"); [LIB] Archi_Bank "API-first and REST design" 📄 | Direct (📄 — REST not in skills inventory; see OQ-1) | Comp-2; Ach-1 | "RESTful API design", "API contracts" |
| 4c | Distributed systems | Req | skills inv. §7 (high-concurrency distributed systems ✅); PA-11.1; PA-10.1; PA-16.4 | Direct | Comp-2; VV-1; GBD-2; AIP-2 | "distributed systems", "microservices" |
| 4d | Solace JMS | Req | — (no anchor); bridge: Kafka A/P, RocketMQ A, AWS SQS/SNS A/P, Apache Camel P | **Gap** — bridge shown (messaging middleware), Solace itself not claimed | Comp-6 (bridge only) | — |
| 4e | Databases | Req | skills inv. §4 (MySQL P, SQL P, Redis P) | Direct | Comp-6; VV-3; Earl-R | "MySQL, SQL, Redis", "MySQL cluster" |
| 4f | Linux or RHEL platforms | Req | CF-N6 (RHEL P ✅) | Direct (employer anchor still ❓ in skills inventory) | Comp-6 | "Linux (RHEL)" |
| 4g | Containers | Req | skills inv. §5 (Docker A/P, Kubernetes A); PA-11.3 | Direct (architected/led level) | Comp-6; VV-4; GBD-2 | "Docker, Kubernetes", "containerised deployment with rollback" |
| 4h | Cloud technologies | Req | skills inv. §5 (AWS A/P); PA-10.1 | Direct (AWS only) | Comp-6; GBD-scope; GBD-3 | "AWS" |
| 4i | Enterprise integration patterns | Req | Apache Camel P (skills inv. §2; 03 PA-01 §3) | Direct via Camel (bridge: Camel is an EIP framework used in UOB production) | Comp-2 | "Apache Camel (enterprise integration patterns)" |
| 5 | Designing, delivering and modernising secure, low-latency, high-throughput, highly available, business-critical transaction-processing systems | Req | PA-01.2; S6; PA-01.4; PA-02.1; X-01; PA-01.1; PA-11.4 | Direct ("high-throughput" shown only as "high load" — no volume figures, 01 §7) | Sum-P1; Ach-1–Ach-5; Comp-3 | "transaction-processing systems", "concurrency control", "latency under high load", "99.9%+ availability" |
| 6a | Digital-payment ecosystems — transaction switching | Req | — | **Gap** | — | — |
| 6b | — retail POS | Req | — | **Gap** | — | — |
| 6c | — e-commerce | Req | S1; PA-19; PA-17.1; PA-11.2 | Direct | Ach-6; Sum-P1/P3; Earl-B/R | "e-commerce", "payment-gateway integration" |
| 6d | — QR payments | Req | — (e-wallet payments integrated, S1) | **Gap** — QR acceptance/acquiring not claimed | — | — |
| 6e | — credit and debit cards | Req | S1 (UnionPay, Visa/Mastercard payments integrated at platform level); PA-04.1 (credit-card collections) | Transferable — card payments integrated on the merchant/platform side; collections across credit-card portfolios; no card issuing/acquiring/processing | Ach-6; Comp-1; UOB-9 | "card and e-wallet payment integration", "credit-card and unsecured-loan portfolios" |
| 6f | — payment authorisation | Req | PA-01.3 / S6 (corporate- and user-role permission matrix = the hub's authorisation layer) | Transferable — authorisation of payment requests by role/account/product, **not** card authorisation; resume says "permission matrix" only | Ach-2; Comp-4 | "permission matrix", "role-based access control" |
| 6g | — clearing and settlement | Req | S2; CF-N4; S1 (settlement reconciliation) | Transferable — hub hands validated payments to core banking, which settles; settlement reconciliation at VV-Life; the hub itself does not clear or settle | UOB-3; Comp-1; Ach-6 | "settlement integration with core banking", "settlement reconciliation" |
| 6h | — digital banking platforms | Req | PA-01.2 | Direct | Ach-1 | "digital and branch channels" |
| 6i | — international card-scheme integration | Req | S1 (Visa/Mastercard payments integrated via the payment subsystem) | **Gap** — adjacent evidence only; never "scheme connectivity" | Ach-6 (adjacent) | — |
| 7 | Mobile applications and SDK development (advantageous) | Pref | profile: React P; Swift/Kotlin F; PA-21 ❓ | **Gap** | — | — |
| 8 | Integration architecture across AWS/Azure/GCP, API management platforms, middleware, enterprise systems, infrastructure, databases, external providers | Req | PA-10.1 / GBD (AWS API Gateway, API-gateway model); PA-01.2 (vendor and third-party banking systems); S2 (core banking); S1 (payment providers); Camel/Kafka/RocketMQ | Direct (AWS only; API management = API gateway on AWS) | GBD-2/3; Ach-1; UOB-3; Ach-6; Comp-2/6 | "API gateway", "vendor and third-party banking systems", "core banking" |
| 9a | Payment & cybersecurity — PCI-DSS | Req | skills inv. §10 (working knowledge of control objectives only) | **Gap** — not claimed | — | — |
| 9b | — secure software engineering | Req | PA-03.4; PA-03.2 | Direct | Comp-4; Ach-5 | "secure SDLC" |
| 9c | — data encryption | Req | X-01 | Direct | Ach-5; Comp-4; GBD-3 | "API and database encryption" |
| 9d | — tokenisation | Req | — | **Gap** | — | — |
| 9e | — access control | Req | PA-01.3; X-01 | Direct | Ach-2; Ach-5; Comp-4 | "role-based permissions", "role-based access control" |
| 9f | — technology risk | Req | PA-03.4 (MAS TRM) | Direct | Comp-4; Ach-5 | "MAS TRM (Singapore technology-risk rules)" |
| 9g | — audit controls | Req | PA-03.1 (SIT/UAT sign-off on every release); PA-03 §7 "audit-ready releases" 📄 | Transferable — release controls; no audit ownership | Ach-7 | "SIT/UAT sign-off for every release" |
| 9h | — DR, operational resilience, risk mitigation | Req | PA-02.1; PA-02.3; X-06 | Direct | Ach-5; UOB-6/7; Comp-3 | "DR and failover drills", "99.9%+ availability" |
| 10a | DevSecOps, CI/CD pipelines, automated testing | Req | PA-03.1; PA-03.2 | Direct (DevSecOps = penetration testing and quality gates inside CI/CD, as evidenced) | Comp-5; Ach-7 | "DevSecOps practice", "CI/CD", "automated regression and penetration testing" |
| 10b | Infrastructure automation | Req | skills inv. §5 (IaC = exposure X); PA-11.3; PA-10.3 | Transferable — deployment automation only (containerised rollback, CI on Jenkins + ECR); IaC not claimed | VV-4; GBD-1 | "containerised deployment with rollback" |
| 10c | Application observability | Req | PA-02.2; PA-02.3 | Direct | UOB-7; Comp-5 | "Splunk-based monitoring and alerting", "SLIs/SLOs" |
| 10d | Vulnerability management, secure deployment | Req | PA-03.2 (penetration testing in CI/CD); PA-03.1 (release governance) | Transferable — security testing in the pipeline and release gates; no vulnerability-management programme ownership | Ach-7; Comp-5 | "penetration testing", "quality gates" |
| 11 | Java/Spring Boot, Solace JMS, PostgreSQL or MySQL, RHEL, containers, AWS (highly desirable) | Pref | as 4a–4h | Direct except Solace (Gap); PostgreSQL not in sources → MySQL used | Comp-2; Comp-6 | as 4a–4h |
| 12 | Establish architecture principles, engineering standards, technical guardrails and governance across multiple development teams | Req | PA-03.1/03.2 (own teams); PA-03.3 (bank-wide = contributed); PA-07.2 (AI governance rule); PA-11.3/11.5 | Direct for own teams/organisations; bank-wide = "contributed" | Ach-7; Comp-7; UOB-4; VV-4 | "quality gates", "engineering standards (contributed bank-wide)", "code standards" |
| 13 | Manage competing priorities, technical dependencies, delivery risks and concurrent tracks in a regulated, business-critical environment | Req | X-02 (MVP sequencing); PA-01.5 (RAID) | Direct | UOB-8; UOB-5 | "MVP scope", "dependencies", "RAID" |
| 14 | Systems thinking; balance strategic direction with hands-on technical leadership and accountable delivery | Req | S5; S6; PA-01.5 | Direct | UOB-1; Ach-2; Sum-P1 | "Stay hands-on alongside delivery" |
| 15 | Collaborative relationships with business, cross-functional tech teams, senior management, vendors, banks and payment schemes | Req | PA-01 §9; X-05; X-02; S1 | Direct (business, tech teams, senior management, vendors) · Transferable (banks — works inside a Tier-1 bank and integrates third-party banking systems) · **Gap** (payment schemes — no direct scheme relationship on record) | Sum-P2/P3; UOB-8/10/11 | "senior management and steering committees", "vendor governance" |
| 16 | Excellent written, verbal, presentation, influencing and executive communication | Req | PA-01.5 (steering reporting); PA-07 §4 (briefed senior management) | Direct (evidence = reporting and briefings) | Sum-P3 | "explaining technical choices in business terms to senior management and steering committees" |
| 17 | Lead, mentor, coach and develop senior engineers and technical leads | Req | X-02 | Direct (through squad leads and EMs) | UOB-10; Comp-7 | "1:1s, mentoring and performance management" |
| I-1 | Lead resolution of critical production issues and major incidents; validate root causes (Key Responsibilities) | Inferred | X-06; S5 | Direct | UOB-6; UOB-1 | "P1–P3 production incidents", "RCA", "resolve production issues" |
| I-2 | Review and approve designs and source code | Inferred | S5 | Direct for review; formal approval authority not claimed | UOB-1; Comp-7 | "review newly submitted core pull requests daily", "Design and code reviews" |
| I-3 | Represent the portfolio in senior-management / governance forums; investment recommendations | Inferred | X-02; PA-01.5 | Direct | Sum-P3; UOB-11 | "technology investment", "steering committees" |
| I-4 | Coaching and performance feedback (1:1s, structured reviews) | Inferred | X-02 | Direct | UOB-10 | "1:1s … performance management" |
| E-1 | Work authorisation / location (not stated in JD) | Elig | 02 §1 | Direct — Singapore PR, Singapore-based | Header | "Singapore PR" |

**JD 前五项 Required（按 JD 强调程度）在第 1 页的可见证据：** #2 技术权威与年限 → Headline、Sum-P1/P2 · #5 安全低延迟高可用交易系统 → Ach-1/2/4/5、Comp-3 · #4 应用与集成架构 → Comp-2/6、Ach-1 · #6 数字支付生态 → Ach-6、Comp-1（缺口不掩饰）· #3 跨团队/供应商/多线迁移 → Ach-3、Sum-P2。✅

## (d) 三维评审（无总分、无百分比）

### 1. Job fit
- **强项（Direct）：** 支付交易处理系统的设计与亲手编码（payment-initiation hub：设计 + 核心模块含 concurrency control + 状态结果处理）；不停机的 ISO 20022 迁移（日期齐全、早于 SWIFT 截止）；低延迟调优与 99.9%+ 可用性、亲自主导 DR 演练；安全控制（加密、凭证管理、基于角色的权限）与 MAS TRM 下的 secure SDLC；工程治理（质量门禁、交付 KPI、bank-wide 标准"contributed"）；多条交付线与四家 IT 服务供应商；Java/Spring Boot/Camel、RHEL、MySQL、容器、AWS。
- **Transferable：** 卡与钱包支付（平台/商户侧集成，非发卡/收单/处理）；支付授权（请求级角色/账户/产品授权，非卡授权）；清算结算（与核心银行结算对接 + VV-Life 结算对账，hub 本身不清算）；基础设施自动化（部署自动化，非 IaC）；漏洞管理（CI/CD 内渗透测试）；与银行的关系（行内 + 第三方银行系统集成）。
- **Gap：** transaction switching、retail POS、QR、国际卡组织对接、Solace JMS、PCI-DSS（仅工作知识，未写）、tokenisation、mobile/SDK（Preferred）、与支付卡组织的直接关系。JD 没有解释 "UPOS & DA"；从 JD 对 POS、QR、卡与卡组织对接的反复强调推断（**属推断，非 JD 明文**），该组合偏卡受理与交换 —— **这是本次申请最大的实质差距**，面试会被直接追问。
- **判断：** 架构/动手/韧性/治理/迁移维度高度对口；"卡受理与交换"领域知识是硬缺口。简历不掩饰，用相邻证据（交易处理、结算对接、卡与钱包集成、对账）展示可迁移性。

### 2. Factual-reliability risks（逐项对照 02/03/S1–S9）
- 标题与日期：与 Brief §3 固定文本逐字一致（VV = Head of Technical Centre、AI Park = VP of Technical Department，S8）；无 CTO/Chief Architect；教育 4 行逐字。
- 数字：25 engineers、四家供应商、15/10 人团队、MX-rich 2025-05/08、2026-08 退役、每 2–3 个月发版、99.9%+、99% SonarQube、estimated ~80%、May 2026、40-person / 140-person（均带 "total headcount"）、~100k DAU —— 全部在 03 §0A 或 S1–S9 中，限定语保留。
- 所有权动词：Ach-2/UOB-1 用 S6/S5 原句；AI Park "Brought Spring Cloud microservices into the architecture"（O2）；VV-Life 支付子系统 "architected"（S1, O2）；Renren/Baidu "Designed and coded"（S1, O1+O2）；bank-wide 标准一律 "contributed"。
- **需要留意的措辞（低–中风险）：**
  - "RESTful API design"（Comp-2）只有 [LIB] 📄 "API-first and REST design" 与 PA-01.2 "API contracts" 支撑，skills inventory 无 REST 行 → OQ-1。
  - "Apache Camel (enterprise integration patterns)" 属合理推断（Camel 即 EIP 框架，P 级生产使用）。面试准备：能举出用过的 Camel EIP（如 content-based router、splitter、aggregator）。
  - "DevSecOps practice" 是对已证实做法（CI/CD 内渗透测试 + 质量门禁 + secure SDLC）的概括，不暗示独立 DevSecOps 平台。
  - Sum-P2 "leading 25 onshore and offshore engineers" 同句未带 "through squad leads"（限定语在 UOB-10；与已批准 Talentvis Summary 写法一致）。
  - Sum-P1 "fintech and SaaS products" 为 02 §4 定位用语（🔶）且已见于已批准 TEK Summary。
  - Ach-6：WeChat Pay 只挂在 Baidu Nuomi 下（S1 规则）；统一写 "integrating … payments"，不写卡组织直连。
  - Ach-4 VV 子句 "brought VV's services to millisecond-level response times" —— PA-11.4 ✅，无数字。
  - 未写 "design authority"（JD 用语）：正式的设计权威/架构评审委员会角色不在记录内（PA-03.3 = contributed），简历用 "Led end-to-end design" + "own the architecture"（S5）。
- 保密：无 CEW/SCV-CCD/CCD/GMS/HCL/MEPS+、无 UOB 交易量、无客户名；lint 0 命中。

### 3. Document quality
- 渲染：3 页（第 3 页约 1/3 篇幅：Earlier Experience + Education）；第 1 页 = 页眉 + Summary + Competencies + 全部 7 条 Achievements；第 2 页以 PROFESSIONAL EXPERIENCE 开头，AI Park 整段在第 2 页；页脚 "Page X of 3" ✅；无孤立标题；Layout OK: **True**。
- 行数：Headline 1 行；Summary 3/3/4 行；Competencies 全部 ≤ 2 行；31 条要点中 4 条为 3 行（Ach-3、Ach-5、Ach-6、UOB-4），其余 2 行；Achievements 7 条中 4 条 2 行。
- 字数 1,269（Summary 164）—— 低于 1,350–1,550 的"通常可容纳"区间：Principal Engineer 偏 IC，按 LIB 指引精简管理类内容，不为凑字数加料。
- 红字 47/93 runs（非已批准原句，草稿预期）；lint 0；英式拼写已检查（organisation、modernisation、programme、licence、centre）；DR、ISO 20022 (SWIFT MT-to-MX)、MAS TRM 首次出现时已解释；CI/CD、SDLC、SIT/UAT、RCA、RAID 等通用交付缩写沿用已批准简历做法，未展开。
- 已执行检查：render 报告；pdftotext 文本可提取；PDF 光栅化目视检查三页。**未执行：** Microsoft Word（Calibri）实机渲染（本环境为 LibreOffice + Carlito，度量兼容但可能有细微换行差异）；ATS 解析测试。

## (e) 缺口的诚实处理

| 缺口 | 简历处理 | 面试口径（建议） |
|---|---|---|
| Transaction switching / retail POS / QR / 卡授权 / 国际卡组织对接 | 不写；只展示相邻证据：支付请求的发起、校验、增补与状态跟踪（Ach-1/Ach-2）、与核心银行结算对接（UOB-3）、卡与钱包支付集成和结算对账（Ach-6） | "我的卡/钱包经验在平台和商户集成侧；没有运营过交换或收单主机。但交易处理、并发控制、状态回执处理、结算对接这些核心问题，我在银行支付 hub 上亲手设计并编码过。" |
| Solace JMS | 不写；Comp-6 列出已有锚点的消息中间件（Kafka、RocketMQ、AWS SQS/SNS）与 Apache Camel 作为桥接 | 坦承未用过 Solace；讲清楚消息语义（持久化、顺序、重放、背压）在 Kafka/RocketMQ/Camel 上的实践 |
| PCI-DSS | 不写（仅工作知识；lint 也禁止） | 讲加密、凭证管理、访问控制、secure SDLC、MAS TRM —— 与 PCI-DSS 控制目标重合的部分；不声称合规负责人 |
| Tokenisation | 不写 | 如被问，说明未做过 tokenisation 实施 |
| Infrastructure automation（IaC） | 不写；展示容器化部署回滚（VV-4）与 CI 流水线（GBD-1） | IaC 仅接触级 |
| Vulnerability management | 只写 "penetration testing" 于 CI/CD（Ach-7、Comp-5） | 不声称负责漏洞管理流程 |
| Mobile / SDK（Preferred） | 不写 | React 动手、Swift/Kotlin 熟悉；不声称移动端领导经验 |
| 与支付卡组织 / 外部银行的直接关系 | 不写 | 行内与第三方银行系统集成、支付服务商集成（S1）为相邻经验 |
| PostgreSQL | 不写；用 MySQL（JD 写 "PostgreSQL or MySQL"） | — |
| "Technical design authority" 正式角色 | 不写该头衔；用 "Led end-to-end design"、"own the architecture" | 讲架构所有权与设计评审的实际做法；bank-wide 架构评审治理为 "contributed" |
| 继任计划、技术社区 | 不写（无记录） | — |

## (f) 需要 Wilson 确认的问题（只列会改变事实或定位的；每条附默认处理）

1. **OQ-1 REST：** UOB payment-initiation hub（及其他系统）的 API 是否为 RESTful？[LIB] 写有 "API-first and REST design"，skills inventory 无 REST 行。**默认：** 保留 Comp-2 "RESTful API design"；若不准确则改为 "API design (API contracts, API gateway)"。
2. **OQ-2 Bank-card binding 的归属：** S1 的 "the e-commerce integrations included bank-card binding payment interfaces and settlement reconciliation" 指 Renren/Baidu 的电商集成，还是 VV-Life 的电商部分？确认后可在 Ach-6 加一个"借记/信用卡绑卡"证据点（对 JD 的 cards 要求有用）。**默认：** 不写 bank-card binding；"settlement reconciliation" 只挂 VV-Life（S1 明确部分）。
3. **OQ-3 JMS / 消息中间件：** 在 UOB 是否用过任何 JMS 类中间件（IBM MQ、ActiveMQ 等）？ActiveMQ 在 skills inventory 中无项目锚点。**默认：** 不写；Solace JMS 保持为缺口，只用 Kafka/RocketMQ/SQS-SNS/Camel 作桥接。
4. **OQ-4 PCI-DSS / tokenisation：** 是否有任何项目处在 PCI-DSS 范围内，或做过卡号/账户 tokenisation（例如 VV-Life 卡支付、UOB 信用卡催收数据）？**默认：** 两者均不写。
5. **OQ-5 正式设计权威：** 是否在 UOB 的设计评审/设计权威论坛中拥有正式签批权（而不仅是本平台的架构所有者）？若有，可在 Ach-1 用 "design authority"。**默认：** 不用该说法。
6. **OQ-6 基础设施自动化：** 是否亲手用过 Terraform / CloudFormation / Ansible 等 IaC？**默认：** 不写（skills inventory 为 exposure）。
7. **OQ-7 卡组织 / 外部银行协作：** 是否与 SWIFT、代理行、UnionPay/Visa 等直接打过交道（接入认证、联调、事件沟通）？**默认：** 不写。
