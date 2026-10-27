# JD 匹配分析 — DBS Bank · SVP, Engineering Lead, Core Banking Technology（JobStreet 95272188）

- **简历草稿：** `out/wilson-2026_ATL_Bank_DBS_V1_0_0_draft.docx`（源 JSON：`resume.json`）· 卡片 04 · 2026-10-21
- **JD：** `jd/full/04_DBS_JD.md`（2026-10-20 经 Claude in Chrome 读取，全文）。JD 只用于分析，不作为 Wilson 经历的证据。
- **事实来源（只读）：** 01 v1.1 · 02 v3.1 · 03 v4.1 · 05 v1.0 · technical-skills-inventory v2.3 · fact-check v2.4 · Drafting Brief §4 会话确认 S1–S9 · approved Talentvis / TEKsystems JSON · TPL · `Archi_Bank_LIB_V5`（仅作定位参考）

**简历位置代号：** HL = Headline · SUM-1/2/3 = Summary 第 1/2/3 段 · CC-1…7 = Core Competencies 行（1 Banking Domains, 2 Engineering Leadership, 3 Architecture & Integration, 4 Hands-On Engineering, 5 Cloud-Native & DevSecOps, 6 Reliability & Performance, 7 AI-Assisted Development）· ACH-1…7 = Selected Achievements（1 Core-banking integration, 2 Legacy modernisation, 3 Hands-on core code, 4 Lending servicing and collections, 5 AI-assisted development, 6 Payment resilience, 7 Multi-squad leadership）· UOB-1…11 = UOB 条目（1 hub 设计, 2 hands-on, 3 延迟, 4 customer-360, 5 ISO 20022 项目交付, 6 MVP 排序, 7 干系人接口, 8 投资/供应商决策权, 9 P1–P3 事件, 10 安全控制, 11 KPI 与标准）· GBD-1/2 · VV-1…4 · AIP-1/2 · EARLY-H/B/S/R（Hengshunyuan / Baidu / Sohu / Renren）

---

## (a) 分类：ATL × BNK（与卡片一致）

- **Family = ATL。** JD 的 7 条 Requirements 里，有 5 条是 ATL 信号：
  - "strong software engineering experience"
  - "leading engineering teams while remaining actively involved in architecture and technical decision-making"
  - 一长串 hands-on 技术栈
  - 分布式 / 性能 / 高可用
  - 平台现代化

  职责里也反复写 architecture / design / code reviews。SM 信号（coach engineering managers、engineering culture、SVP 职级）存在，但不占 Required 多数。按 05 §2 "取拥有最多 Required 的 family"，定为 ATL。
- **Lens = BNK。** 雇主为银行（05 §2）。

## (b) Fast-reject / Eligibility

- **05 §4 fast-reject：无命中。** 以下均不涉及：C#/.NET 主栈、kdb+/q、Murex / Treasury-FX core、equity OMS core、制造业、强制 Azure/Databricks、财务 AI、"cross-border" 物流、SAS 政策撰写、GPU 推理基础设施。
- **ATL×BNK 家族 gap（05 §2.1）：** "Core banking systems (e.g. Temenos, Finacle) … not in sources; do not list"。这不是 fast-reject，作为领域 gap 诚实处理，见 (e)。
- **Eligibility：** JD 未要求证书、银行年限、工作准证或安全审查。Wilson 为 Singapore PR（02 §1），无资格障碍。
- **职级信号：** 招聘 SVP，现职 VP2，属于跨级。这是风险，不是资格问题；简历中不写职级，不做任何暗示。
- **地点：** DBS Asia Hub（East Region），全职，无冲突。

## (c) 证据矩阵（每条 JD 明确要求一行；职责条目按 05 §3 标为 Inferred）

| # | JD requirement（JD 原词，缩写） | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| R1 | Strong software engineering + significant exposure to Core Banking **or** large-scale transaction processing | Req | PA-01, PA-01.2, S2, X-02（millions of accounts）, PA-04.1, 02 §1（18+ yrs） | **Direct** on "large-scale transaction processing"（Tier-1 银行的跨境 / RTGS 支付发起中枢，服务数百万账户）。"Core Banking" 本身只有集成侧经验，记为 Transferable，见 R5 | SUM-1, SUM-2, ACH-1, CC-1, UOB-1 | "transaction platforms", "transaction processing", "integrated with core banking" |
| R2 | Leading engineering teams while actively involved in architecture & technical decision-making | Req | X-02, S5 / X-04, S6 / PA-01.3, PA-01.1（phased-coexistence 决策） | **Direct** | SUM-1, ACH-3, ACH-7, CC-2, UOB-2 | "leads teams while staying hands-on in architecture, solution design and code reviews" |
| R3a | Hands-on Java / Spring Boot | Req | skills inv. §1–2（Java P, Spring Boot P）, PA-01.2, S6 | **Direct** | CC-4, UOB-1, ACH-3 | "Java", "Spring Boot" |
| R3b | Angular **or** React | Req | skills inv. §1：React P ✅[CONF]，雇主 / 时期 ❓；Angular P/A ❓[R22] | **Direct**（React 已确认 hands-on），但缺雇主锚点，只放 skills 行；Angular 为 **Unverified**，不列 | CC-4 | "React" |
| R3c | Microservices & API Architecture | Req | PA-01.2（API contracts）, PA-10.1（Spring Cloud + API gateway）, PA-11.4, PA-16.4, PA-17.1（Dubbo） | **Direct** | CC-3, UOB-1, GBD-1, VV-3, AIP-2, EARLY-B | "microservices and API design", "API gateway" |
| R3d | Event-Driven Systems | Req | PA-01 §3（event-driven integration [LIB]）, PA-11.4 / PA-16.4（Kafka 异步） | **Direct** | CC-3, VV-3, AIP-2 | "event-driven integration", "Kafka-based asynchronous processing" |
| R3e | CI/CD and DevSecOps | Req | PA-03.1 / 03.2（Jenkins, Bitbucket, SonarQube gate, automated regression + penetration testing in CI/CD）, PA-03.4（secure SDLC）, PA-10.3, PA-11.3 | **Direct**。"DevSecOps" 一词不在记录中，只用作 CC 行标签；实质证据是管线内安全测试加 secure SDLC | CC-5, ACH-7, GBD-2, VV-4 | "CI/CD", "penetration testing", "secure SDLC", "DevSecOps"（标签） |
| R3f | Linux and Middleware Platforms | Req | CF-N6（RHEL P ✅，雇主锚点 ❓）, Apache Camel P（UOB）, PA-02.1（real-time payment middleware）, PA-17（Dubbo / ZooKeeper / Resin） | **Direct** | CC-5, CC-3, ACH-6, UOB-1 | "Linux (RHEL)", "Apache Camel integration middleware", "payment middleware" |
| R3g | Kubernetes / OpenShift **or equivalent** cloud-native platforms | Req | skills inv. §5（Kubernetes A: GBD, VV, AI Park；Docker A/P；AWS A/P） | **Direct** via Kubernetes：A 级（架构 / 主导），时间为 2016–2022，UOB 侧无记录。OpenShift 为 **Gap**，不写 | CC-5, GBD-1, VV-4 | "Kubernetes", "Cloud-Native" |
| R3h | Exposure to MongoDB（distinct advantage） | Pref | skills inv. §4（MongoDB P: Sohu, Baidu, AI Park）, PA-16 | **Direct**（历史经验，2012–2017） | CC-4, AIP-2 | "MongoDB" |
| R4 | Distributed systems, scalability, resiliency, performance engineering, HA | Req | PA-02.1（DR, 99.9%+）, PA-01.4（latency）, S6（concurrency control）, PA-11.4 / 16.4（millisecond-level）, skills inv. §7 | **Direct** | ACH-6, ACH-3, CC-3, CC-6, UOB-3, VV-3, AIP-2 | "distributed high-concurrency systems", "high availability", "latency tuning", "disaster recovery (DR)" |
| R5 | Core Banking domain expertise: Deposits, Loans, Customer Management, Transaction Processing, Settlement, Accounting flows | Req | PA-01 + S2；PA-04.1；PA-05.1 + S2；S1（VV settlement reconciliation） | 整体 **Transferable**，分项见下 | CC-1, ACH-1, ACH-4, SUM-2, VV-2 | "integration with core banking", "lending servicing and collections", "customer-360"；"Deposits" / "Accounting" 未使用 |

R5 分项：

| 子领域 | Status | 依据 / 桥接 |
|---|---|---|
| Transaction Processing | Direct | 支付发起中枢 |
| Loans | Transferable | 零售无抵押贷款的贷后服务与催收，不是放款或贷款核算 |
| Customer Management | Transferable | customer-360 平台服务 client management 与组合分析，不是 CIF 主数据 |
| Settlement | Transferable | 集成侧：核心银行执行结算，中枢处理回传结果；另有 VV 商户结算对账 |
| Deposits | Gap | 无相关经验 |
| Accounting / GL | Gap | 无相关经验 |

| # | JD requirement（JD 原词，缩写） | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| R6 | Platform modernization & legacy transformation | Req | PA-01.1, PA-01.5, PA-17.1, PA-18.1 | **Direct** | HL, ACH-2, SUM-2, UOB-5, CC-3, EARLY-B, EARLY-S | "Platform Modernisation", "Legacy modernisation", "re-architected" |
| R7 | Stakeholder management, communication, problem-solving | Req | X-02, TPL 干系人接口句, X-05, X-06, PA-01.4 | **Direct** | SUM-3, UOB-7, UOB-8, UOB-9 | "steering committees", "senior management", "primary interface" |
| EL | Eligibility（证书 / 银行年限 / 准证 / 审查） | Elig | 02 §1（Singapore PR） | JD 未写，无障碍。SVP 跨级只是风险 | — | — |
| I1 | Lead architecture, design & development of large-scale Core Banking applications | Inferred | PA-01.2, S5, S6, PA-05, S2 | **Transferable**：领导的是与核心银行集成的银行交易平台的架构 / 设计 / 开发，不是核心系统本身 | ACH-1, ACH-3, UOB-1, UOB-2 | "integrated with core banking" |
| I2 | Solution design, system architecture, API strategy, platform modernization | Inferred | PA-01.2, PA-01.1, PA-10.1 | **Direct** | UOB-1, ACH-2, GBD-1, CC-3 | "API contracts", "API gateway" |
| I3 | Drive cloud-native, microservices, event-driven patterns, engineering best practices | Inferred | PA-10.1, PA-11.4, PA-16.4, PA-11.3, PA-03.3 | **Direct**。云原生证据在 GBD / VV（2019–2022）；UOB 的 best practices 为 "contributed to" bank-wide standards | CC-3, CC-5, GBD-1, VV-3, VV-4, UOB-11 | "Cloud-Native", "microservices", "event-driven" |
| I4 | Architecture / design / code reviews & technical governance across multiple delivery teams | Inferred | S5 / X-04, PA-03.3（locked verb） | 本团队为 **Direct**（每日 review 新提交的核心 PR、共同设计、拥有架构）；跨团队治理为 **Transferable**（bank-wide standards 与 architecture-review governance 的贡献者，不是 owner） | UOB-2, UOB-11, CC-2 | "architecture and code reviews", "contributed to … architecture-review governance" |
| I5 | Evaluate emerging technologies incl. AI-assisted software development | Inferred | PA-07.1–07.3, S9, PA-05.1（Cloudera 评估） | **Direct** | ACH-5, CC-7, SUM-2, UOB-4 | "AI-assisted development", "evaluated Cloudera" |
| I6 | Lead multiple engineering squads | Inferred | X-02（25 人，两支团队，经 squad leads / EMs）, PA-01.5（15）, PA-05.3（10）, S3（VV 140 total headcount） | **Direct**。规模：现 25 人；历史 VV 140 人（total headcount） | ACH-7, SUM-2, SUM-3, UOB-4, UOB-5 | "Multi-squad leadership", "squad leads and engineering managers" |
| I7 | Partner with business, product, architecture teams | Inferred | TPL / TEK 干系人句, X-02 MVP | **Direct** | UOB-7, UOB-6 | "primary interface between business stakeholders, product owners … architects" |
| I8 | End-to-end delivery accountability, design → production support | Inferred | PA-01.5, PA-02.3, X-06 | **Direct** | UOB-5, UOB-9 | "owned end-to-end delivery", "own production support" |
| I9 | Engineering quality: automated testing, CI/CD, DevSecOps | Inferred | PA-03.1, PA-03.2 | **Direct** | ACH-7, CC-5, UOB-11 | "CI/CD quality gates", "99% SonarQube coverage gate", "automated regression and penetration testing" |
| I10 | Performance, reliability, observability, stability, operational readiness | Inferred | PA-01.4, PA-02.1, PA-02.3, PA-11.5 | **Direct** | UOB-3, ACH-6, UOB-9, VV-4 | "Splunk-based monitoring", "SLIs/SLOs" |
| I11 | Technical leadership across Core Banking domains（incl. GL integration） | Inferred | 同 R5 | **Transferable**；Deposits、GL integration 为 **Gap** | CC-1, ACH-1, ACH-4 | 同 R5 |
| I12 | Technical roadmaps & modernization strategies aligned to business priorities | Inferred | PA-01.5（roadmap）, PA-01.1（phased-coexistence 决策）, X-02（MVP 排序） | **Direct** | UOB-5, ACH-2, UOB-6 | "roadmap", "phased … coexistence", "MVP scope" |
| I13 | Identify architecture / capacity / performance / resiliency gaps; drive remediation | Inferred | PA-02.1（capacity baselines, DR）, PA-01.4 | **Direct** | ACH-6, UOB-3 | "capacity baselines", "latency" |
| I14 | Support critical production incidents; lead RCA | Inferred | X-06, PA-02 §4（[LIB] led incident response and RCA） | **Direct** | UOB-9, CC-6 | "P1–P3 production incidents", "root-cause analysis (RCA)" |
| I15 | Coach & mentor engineers, tech leads, EMs | Inferred | X-02（1:1s, mentoring, performance management，经 squad leads / EMs） | **Direct** | ACH-7, CC-2 | "1:1s, mentoring and performance management" |
| I16 | Engineering culture: ownership, innovation, technical excellence | Inferred | PA-03（standards, quality gates, coaching）, PA-07 | **Transferable**：有实践证据，没有"文化成效"的度量；简历不写 culture 口号 | CC-2, ACH-5, ACH-7 | —（不写 "culture"） |
| I17 | Trusted technology advisor; influence strategic technology decisions | Inferred | X-02（technology investment / vendor selection 的决策或共同决策权）, PA-01.5, PA-07 §4（向高管汇报） | **Direct** | UOB-8, UOB-7, SUM-3 | "decision or joint-decision authority on technology investment" |

**第 1 页可见性：** JD 前五条有记录支撑的 Required（R1、R2、R3、R4、R6）都在第 1 页有可见证据：

- R1：SUM-1/2，ACH-1
- R2：SUM-1，ACH-3/7，CC-2
- R3：CC-3/4/5
- R4：CC-6，ACH-6，ACH-3
- R6：HL，ACH-2

另外，R5 的缺口在 CC-1 和 ACH-1/4 里以"相邻 / 集成"措辞如实呈现；R7 见 SUM-3。

---

## (d) 三维评审（无总分；唯一数字为卡片的批次匹配度）

**批次匹配度（照抄卡片；用户要求的覆盖率口径）：93。**

- 口径 = Required 证据覆盖率：Direct = 1、Transferable = 0.5、Gap = 0，分母为 JD 明写的 7 条 Required。
- 7 条中 6 条 Direct、1 条 Transferable（R5 Core Banking 领域，C1 后由 Gap 改为 Transferable via integration），即 6.5 / 7。
- 本矩阵复核结果一致。该数字不是面试概率，也不包含职级跳跃等风险。

### 1. 岗位匹配（Job fit）

**直接对上的强项**

- **大规模交易处理 + 核心银行集成（R1）：** Tier-1 银行的跨境 / RTGS 支付发起中枢，服务数百万账户。两套平台与核心银行集成（S2）：
  - 中枢把已校验的支付送往下游，由核心银行执行结算，中枢处理回传结果；
  - customer-360 平台每日接收核心银行的账户汇总，用于组合分析。

  这是对 DBS "Core Banking" 诉求最诚实也最有力的回答：集成侧经验，不是"拥有核心系统"。
- **带队且深度参与架构（R2）：**
  - 带 25 人，经 squad leads / EMs 管理；
  - 每日 review 新提交的核心 PR，与工程师共同设计，拥有架构，重大变更时亲自写核心模块（S5）；
  - 亲自实现中枢核心模块：交易发起、并发控制、权限矩阵、状态结果处理（S6）。
- **现代化（R6）：** ISO 20022 MT→MX 采用分阶段 Blue/Green 共存：
  - 2025 年 5 月 / 8 月上线 MX-rich，早于 SWIFT 2025 年 11 月期限；
  - 2026 年 8 月退役共存，无服务中断；
  - 更早还有 Baidu（Dubbo）和 Sohu（CMS）的重构。
- **韧性 / 性能（R4）：** 亲自主导 DR 与 failover 演练，99.9%+ 可用性；延迟调优；并发控制；VV / AI Park 的毫秒级服务。
- **AI 辅助软件开发（I5）：** 亲自设计并构建生产级 AI code review：
  - 2026 年 5 月经正式架构与风险审批后上线；
  - AI 不审批、不合并；
  - 资深工程师审查时间估算下降约 80%。

  这直接回应 JD 的 "AI-assisted software development"。
- **技术栈（R3）：**
  - Java / Spring Boot / Apache Camel（P）
  - 微服务与 API、事件驱动
  - CI/CD + 管线内渗透测试
  - RHEL（P）
  - Kubernetes（A，2016–2022）
  - MongoDB（P，2012–2017）
  - React（P，缺雇主锚点）

**弱项 / 风险**

- **核心银行领域（R5，最大实质缺口）：** Deposits、Accounting / GL 没有经验；Loans、Customer Management、Settlement 只有相邻或集成侧经验。JD 把 "Strong Core Banking domain expertise" 列为 Required，面试官很可能就此深挖。
- **职级与规模：** VP2 → SVP 跨级。现团队 25 人，可能小于 DBS SVP 的多 squad 组织；历史上 VV 140 人（total headcount）能部分对冲。
- **云原生近况：** Kubernetes 证据在 2016–2022、深度为 A；UOB 平台侧没有记录；OpenShift 无。
- **前端：** React 已确认但缺雇主 / 时期；Angular 未列。
- **银行年限：** 约 4 年，简历日期明示，不掩饰。

### 2. 事实可靠性风险（Factual reliability）

1. **📄 级来源：** "99.9%+ availability" 和 "no service interruption" 来自 [LIB]（📄），不是独立证据。面试需准备统计窗口与计算口径。
2. **"estimated ~80%" 是估算：** 依据 03 PA-07 §8 公式；改造前审查轮数 R₀ 仍 ❓（C2）。简历已保留 "estimated"，面试按公式解释，不要说成遥测数据。
3. **并发控制模块：** S6 / B-09 于 2026-10-21 确认可写，但具体机制未入库，面试必问。请提前准备实现细节，例如锁 / 幂等 / 乐观并发中实际用了哪种。
4. **团队人数，背调敏感：**
   - VV 140 为 total headcount，分层管理，直接共事 15–20 人（S3）；
   - GBD 40 为 total headcount，含外包（S4）。

   简历两处都带 "(total headcount)"。
5. **职位英文名：** 按 S8 使用 Head of Technical Centre / VP of Technical Department；02 v3.1 仍记 "…Development"（CF-16 / FU-3，TU-13 未入库）。背调时须与雇佣信一致。
6. **customer-360：** 写的是 "in production since 2022"，没有写成"主导了 2022 年上线"（C5 未决）。
7. **99% SonarQube coverage gate：** 是新代码覆盖率还是整体覆盖率，仍 ❓（03 PA-03 §8）。面试可能被问。
8. **雇主锚点缺失：** RHEL、SQL、React 只出现在 Competencies，没有进入任何描述性句子（skills inventory 规则）。
9. **Kubernetes 深度为 A：** 记录是架构 / 主导，不是亲手运维。若被追问实操，请如实说明。
10. **结算口径：** 简历只写 "where core banking executes settlement"（S2 / CF-N4），未写中枢做清算或结算；"RTGS" 只作为支付类型出现在 CC-1。
11. **其他已知口径：**
    - Hengshunyuan 日期 Oct 2017 – Sep 2019（D-10），与 VV 的重叠不在简历注释，面试时解释（业务休眠）；
    - GBD 业务性质未决（OQ-1.9），只用默认措辞 "online-game businesses"。

### 3. 文档质量（Document quality）

**已通过（render.py 报告 + 人工检查 PDF）**

- **版面：** Layout OK: True；3 页；第 1 页 = 页眉 + Summary + Competencies + 全部 7 条 Achievements；第 2 页以 PROFESSIONAL EXPERIENCE 开头，第 3 页以 EARLIER EXPERIENCE 开头；页脚 "Page X of Y"；无孤立标题。
- **行数：**
  - Headline 1 行（实测宽 498.6 pt，行宽 510.3 pt）；
  - Summary 渲染为 3 / 3 / 4 行；
  - Competencies 7 行，每格 ≤ 2 行，标签 ≤ 3 词、单行；
  - 30 条 bullet 中 3 行的 5 条（ACH-1、ACH-2、ACH-5、UOB-1、EARLY-B），未超过 1/5；无行数超限标记。
- **Lint：** 0 命中。
- **拼写与用语：** 全文英式拼写，已用正则扫过 -ize / center / program / license 等美式写法；业内缩写首次出现即展开（ISO 20022 (SWIFT MT-to-MX)、disaster recovery (DR)、root-cause analysis (RCA)、MAS Technology Risk Management (TRM)），MTTR 改写为 "mean time to recovery"。
- **事实一致性：** 职位、日期、教育四行与 Brief §3 完全一致；无 CTO、内部系统名、供应商名、UOB 业务量。
- **长度与可读性：** 1,262 词，低于 1,350–1,550 的参考区间，但没有为凑字数加料。第 3 页内容约占三分之一页，属正常。
- **红字：** 43 / 93 个 run 为红色（草稿标记，表示与已批准简历非逐字一致），符合预期。

**发现并已修复的问题（3 轮渲染）**

- 卡片 headline 实测 516–521 pt，渲染为 2 行 → 改写为 1 行。
- 首稿 10 / 30 条为 3 行 → 压缩到 5 条。
- Summary 第 2 段末尾单词孤行 → 精简。
- AI Park 被分页拆开 → 两处省行后整段回到第 2 页。

**未执行的检查**

- Microsoft Word 实机渲染：只用 LibreOffice + Carlito（与 Calibri 度量兼容）检查过。
- ATS 解析器实测。
- 红字转黑后的终稿渲染（需 Wilson 批准后用 `--final` 生成）。

---

## (e) Gap 诚实处理

| Gap | 简历中的处理 | 面试桥接建议 |
|---|---|---|
| Deposits | 不写（lint 亦拦截） | 说明经验在支付发起与核心银行集成一侧；不把支付经验说成存款系统专长（另见 Q4） |
| Accounting / GL integration | 不写 | 如实说明未做过总账；可谈下游状态结果的回传处理（S6）和 VV 的结算对账（S1），定性为相邻经验 |
| Loans | 用记录原词 "retail unsecured-lending servicing … and post-disbursement collections"（ACH-4） | 强调是贷后服务与催收，不是放款或贷款核算 |
| Customer Management | "customer-360 data"、"customer-360 platform … daily account summaries … portfolio analysis"（CC-1、ACH-1） | 说明是 360 视图 / 分析平台，不是 CIF 主数据系统 |
| Settlement | "integrated with core banking … where core banking executes settlement"（ACH-1） | 中枢不做清算或结算（CF-N4）；可谈结果回传处理与时间窗口压力 |
| OpenShift | 不写；以 Kubernetes 作为 JD 允许的 "or equivalent" | 视 Q2 答复决定能否补充 |
| Angular | 不列；React 只列在 Competencies | 视 Q1 答复 |
| SVP 职级 / 团队规模 | 不写职级；用真实数字：25 名工程师（经 squad leads / EMs），VV 140（total headcount） | 用 leader-of-leaders 结构和 SVP 职责里的决策权（X-02）回应；不夸大 UOB 人数 |
| 云原生近况 | Kubernetes 只出现在 CC-5 与 GBD / VV 条目，没有写到 UOB | 如实说明 UOB 平台环境；强调可迁移的架构模式 |
| 银行年限约 4 年 | 不掩饰（UOB 日期明示） | 用 Tier-1 受监管交付深度加 18+ 年总经验对冲（05 §7.1） |

## (f) 待 Wilson 确认的问题（只列会改变事实或定位的；每条附默认做法）

1. **React 的雇主 / 时期：** 是哪段经历（或个人项目）？另外，Renren / Baidu 时期是否亲手写过 Angular？
   - **默认：** React 只列在 CC-4，Angular 不列。
2. **Kubernetes 深度与 OpenShift：** GBD / VV / AI Park 时期是亲手配置 / 运维 Kubernetes（P），还是只负责架构 / 主导（A）？UOB 是否接触 OpenShift 或其他容器平台？
   - **默认：** Kubernetes 按架构级写在 CC-5 与 GBD / VV 条目；OpenShift 不写。
3. **零售贷款服务平台是否也与核心银行集成**（例如贷款账户、还款入账）？
   - **默认：** 不写。只按 S2 的范围写中枢和 customer-360 两套平台与核心银行集成。若确认，"Loans" 证据会更强。
4. **CASA 交接：** 03 PA-01 图中中枢下游包含 CASA（活期 / 储蓄账户），这是否就是 S2 所说的核心银行交接？
   - **默认：** 简历不提 CASA，Deposits 仍记 Gap。若确认，只作为面试中的 Deposits 相邻话题，简历仍不写 Deposits 专长。
5. **25 人以外的扩展团队：** 是否有可如实计入的 dotted-line 成员或供应商人员（四家 IT 服务供应商），可用于 SVP 规模定位？
   - **默认：** 只写 25 名工程师，供应商人员不计入。
