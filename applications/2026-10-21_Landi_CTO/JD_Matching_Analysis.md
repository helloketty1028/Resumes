# JD Matching Analysis — Landi International · Chief Technology Officer (JobStreet 95323660)

- **简历文件：** `drafts/07/out/wilson-2026_SM_Bank_Landi_V1_0_0_draft.docx`（+ `.pdf` / `.txt`）· 源数据 `drafts/07/resume.json`
- **JD：** `jd/full/07_Landi_JD.md`（全文，2026-10-20 抓取；JobStreet 标注该广告未经 hirer 验证，外国公司）· 定位卡 `cards/07.md`
- **日期：** 2026-10-21 · 依据：Drafting Brief §1–§8、01/02/03/05、skills inventory、fact-check、两份已批准 JSON（Talentvis 为主）
- **Batch match score（卡片数值，用户要求的覆盖率公式）：75** —— 原样照抄，未重新计算；本文其余部分不打总分、不用百分比。

---

## (a) 分类：Family × Lens

**SM × BNK**（Senior Manager × bank/fintech）。

- **Family = SM：** JD 是公司级技术负责人岗位 —— 技术愿景与路线图、预算/资源/容量、带技术与项目管理团队、向高层汇报、工程实践治理。这些 Required 项落在 SM；架构（cloud-native、microservices、APIs）与交付治理是辅助证据。
- **Lens = BNK：** Landi 是支付硬件 + 软件公司（支付终端、海外市场），JD 要求 "payments, fintech, financial services technology, or a similarly security-sensitive industry" —— 按 05 §2 归 BNK。银行术语（ISO 20022、MAS TRM）首次出现时解释；"MX-rich coexistence" 改写为 "running old and new message formats side by side"（协调方 cold-read 建议）。
- **Headline 不写 "CTO"**（HR-1 与本批规则），用卡片给定的 "Payments Technology Leader — Fintech Platforms, Connected Devices & Multi-Market Delivery | Strategy · Teams · Budgets"（渲染为 1 行）。

## (b) Fast-reject 与资格

- **Fast-reject（05 §4）：未命中。** 无 C#/.NET 主栈、kdb+/q、Murex/Treasury-FX、equity OMS、制造业、强制 Azure/Databricks、CFO 域 AI、物流 "cross-border"、SAS 公共政策、GPU 推理基础设施。**支付终端 / POS** 是领域缺口，不是 fast-reject 信号（JD 写的是 "an understanding of payment terminals, connected devices, **or** integrated hardware and software"）。
- **学历：** JD 要 CS/IT/软件工程/电子工程 "or a related discipline" 本科，研究生为加分。Wilson 本科 Applied Mathematics（相关定量学科）+ 硕士 Computer Science and Technology —— 满足，硕士命中加分项。
- **年限：** "At least 15 years progressive technology experience" —— 18+ 年（2008 起），满足。"including 5 years in senior technology leadership, such as CTO, VP of Engineering, Head of Technology, or equivalent" —— 公司级技术负责人职位为 AI Park VP of Technical Department（2016-04 – 2017-09）、Hengshunyuan Co-founder（2017-10 – 2019-09）、VV Head of Technical Centre（2019-04 – 2020-06），合计约 4 年多（2019 年有重叠）；之后 GBD Project Manager & Architect 与 UOB VP2 是高级但非公司级 "head of technology"。**属 Transferable / 有争议**：简历只写职位与年份（"2016–2022 in head-of-technology and architect roles" 为已批准措辞），不写年数，不写 CTO。
- **工作资格：** Singapore PR —— 无障碍。JD 未写语言要求；英文与普通话均为专业工作水平（Landi 母公司背景下普通话可能是加分，但 JD 未说明，属 Inferred）。

## (c) Evidence matrix

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | Bachelor's in CS/IT/SE/EE or related; postgraduate an advantage | Elig / Pref | 02 §3 | Direct（本科应用数学 = related；硕士 CS） | Education | — |
| 2 | ≥15 years progressive technology experience | Req | 03 §0A "18+ years" | Direct | Sum-P1 | "18+ years" |
| 3 | 5 years senior technology leadership (CTO / VP Eng / Head of Technology or equivalent) | Req | 02 §2, S8, PA-16.1, PA-11.1, PA-15.1, X-02 | Transferable —— 公司级技术负责人约 4 年多 + UOB VP 4 年；不报年数 | Sum-P1（"head-of-technology and architect roles"）, Sum-P2, Experience 职位 | head-of-technology |
| 4 | Define and execute technology strategies and roadmaps for international markets, aligned with local business needs | Req | PA-11.1 技术选型与预算, PA-13 SEA B2B 产品, PA-16.2 城市招投标与试点, PA-10 多辖区 KYC, PA-01.5 roadmap | Transferable —— 桥：多市场平台（新加坡 / 中国 / 东南亚）与技术选型、预算；**没有**"为 N 个海外国家制定技术战略"的记录 | Competencies "Technology Strategy"、"Multi-Market Delivery"; Ach-2, Ach-3, Ach-4; VV-2 | technology roadmaps, multi-market |
| 5 | Payments, fintech, financial services or security-sensitive industry | Req | PA-01, S1, S2, PA-04.1, X-01 | Direct | Headline, Sum-P1/P2, Ach-1, Ach-3, Ach-7, UOB 全部 | payments, fintech, cross-border payments |
| 6 | Understanding of payment terminals, connected devices, or integrated hardware and software | Req | PA-16（车场硬件连云的 IoT 平台）, PA-16.3 识别, 03 §0A 实时传感器事件 | Transferable —— 桥：connected devices（IoT 车场硬件 + 云）；**支付终端 / POS：Gap**，未声称 | Headline "Connected Devices", Competency "Connected Devices & IoT", Ach-2, AI Park | connected devices, IoT |
| 7 | Lead cross-functional customer solution delivery, deployment, localisation, support and maintenance across multiple markets | Req | PA-16.2 三城试点, PA-11.2 VV-Life 首版, PA-10 GBD 上线, X-06 生产支持, PA-02.3 | Transferable —— 交付 / 部署 / 支持为 Direct，"across multiple markets" 为 Transferable（中国多城、新加坡、东南亚产品）；**localisation 无明确记录 → Gap**（只有多辖区 KYC 设计） | Competency "Multi-Market Delivery", Ach-2, UOB "Reliability & Governance", GBD-2 | deployment, production support, rollouts |
| 8 | Strong project management and delivery governance skills | Req | PA-01.5, PA-03.1, X-02 MVP, PA-10 hybrid delivery | Direct | Ach-1, Ach-5, UOB-3, GBD-1/3 | delivery governance, delivery KPIs |
| 9 | Lead, coach and develop geographically distributed technical and PM teams | Req | X-02（25 名 onshore/offshore，经 squad leads；1:1、mentoring、绩效管理；与印度/泰国/印尼团队协作）, S3, S4 | Direct（分布式技术团队）/ Transferable（"PM teams"：带的是交付团队，GBD 40 人项目团队）；印度/泰国/印尼为**协作而非直线管理**，措辞已保留 | Ach-4, Ach-5, Competency "Leadership & Budgets", GBD-1 | onshore and offshore, squad leads |
| 10 | Career development, succession plans for the teams (responsibility) | Inferred（职责项） | X-02 mentoring / performance management | Gap（继任计划无记录）—— 只写 mentoring 与 performance management | Competency "Leadership & Budgets" | mentoring, performance management |
| 11 | Commercial judgement; technology budgets, resource allocation, capacity planning | Req | X-02 预算与投资决策权, X-05, PA-10.3, PA-11.1, PA-16.1, PA-02.1 capacity baselines | Direct（UOB 为**买方**商务权限：供应商选择、SOW/licence 谈判 —— S7） | Sum-P2, Ach-4, Competencies, UOB-1/2, GBD-1 | technology budget, capacity planning |
| 12 | Establish infrastructure, tools, processes and reporting systems for operations and strategic visibility | Req | PA-03.1 KPI, PA-03.2 quality gates, PA-02.2/02.3 Splunk monitoring, PA-11.3/11.5, PA-10.3 Agile 从零引入 | Direct | Ach-5, UOB "Reliability & Governance", VV-4, GBD-1 | delivery KPIs, CI/CD, monitoring |
| 13 | Explain complex technology to executive leadership, Board members and business teams | Req | PA-01.5, X-02（senior management、steering committees）, PA-07 向高管汇报 | Direct（senior management / steering / 业务）；**Board：Gap**，未声称 | Sum-P2, UOB "Reliability & Governance" 第 3 条 | senior management, steering committees |
| 14 | Evaluate emerging technologies, translate into practical applications | Req | PA-07.1–07.3, PA-08, PA-16.3 | Direct | Sum-P3, Ach-6, UOB AI agent 条, AI Park-2 | AI, practical application |
| 15 | Experience delivering AI-enabled products or enterprise AI initiatives | Pref | PA-07（生产 AI code-review，2026-05 上线）, PA-08, RAG 助手（O5） | Direct（RAG 贡献本版未写，见 change log） | Ach-6, Competency "Architecture & AI", UOB AI agent 条 | AI code-review service, AI agent |
| 16 | Enterprise architecture principles; secure, scalable cloud-native, microservices, APIs | Inferred（职责项） | PA-01.2, PA-10.1, PA-11.1/11.4, PA-16.4, X-01 | Direct（"enterprise architecture principles" 作为术语未使用；银行级标准为 "contributed to" —— PA-03.3） | Competency "Architecture & AI", UOB-5, GBD-2, VV-3 | cloud-native microservices, APIs |
| 17 | Interoperability across payment hardware and software | Inferred（职责项） | — | Gap（无支付硬件互通记录） | 未写 | — |
| 18 | Platform modernisation, lifecycle planning, performance, resilience, availability | Inferred（职责项） | PA-01.1, PA-01 "reduced technical debt" 📄, PA-02.1 99.9%+, PA-11.4 | Direct（"technology lifecycle planning" 未作为术语使用） | Ach-1, Ach-7, Competency "Technology Strategy" | platform modernisation, availability |
| 19 | Agile, DevSecOps, CI/CD, automation, code quality, technical debt | Inferred（职责项） | PA-03.2（流水线内回归与渗透测试）, PA-10.3, PA-11.3 | Direct（Agile、CI/CD、代码质量）/ Transferable（"DevSecOps" 术语未用，写为 "security testing in the pipeline, secure SDLC"） | Competency "Engineering Practice", UOB-11, GBD-1, VV-4 | Agile/Scrum, CI/CD, secure SDLC |
| 20 | Work with regional teams to translate local market needs into priorities and product adaptations | Inferred（职责项） | X-02 跨时区协作, X-02 MVP 排序, PA-13 | Transferable —— 桥：跨区域团队协作与优先级排序；产品本地化改造无记录 | Ach-5, UOB-3, VV-2 | — |

**第 1 页可见性（01 §6A）：** JD 前五个有证据支撑的 Required —— (2) 15+ 年 → Sum-P1；(5) 支付 / fintech → Headline、Sum-P1、Ach-1、Ach-3；(6) connected devices → Headline、Competency、Ach-2；(9) 分布式团队 → Ach-5、Competency；(11) 预算 / 资源 / 容量 → Sum-P2、Ach-4、Competency。(4) 国际市场战略以 Competency "Technology Strategy" + "Multi-Market Delivery" 与 Ach-2/3 的方式呈现为 Transferable，没有伪装成 Direct。

## (d) 三维评审（不打总分）

**1. Job fit**
- 强项：支付领域深度（Tier-1 银行跨境支付 ISO 20022 迁移 + 中国与新加坡的卡 / 钱包支付集成）、公司级技术负责人经历（AI Park、VV、联合创始）、预算与供应商权限、分布式团队、生产 AI —— 覆盖 JD 大部分 Required。
- IoT 车场平台是对 "connected devices / integrated hardware and software" 的真实桥梁，且带有招投标 → 试点 → 城市落地的过程，与 JD 的 "deliver, deploy, support" 吻合。
- 弱项：没有支付终端 / POS 经验；没有 "海外市场技术战略" 的明确所有权；无 Board 汇报；公司级技术负责人年限约 4 年多，略低于 "5 years"；无本地化（localisation）记录。CTO 岗位的层级（公司级、全海外市场）高于其当前 VP2 带 25 人的范围 —— HM 可能视为跨级申请。

**2. Factual-reliability risks**
- 所有数字来自 03 §0A / S1–S9：18+ 年、25 名工程师、140 人（total headcount）、40 人（total headcount）、四家 IT 服务供应商、10 人团队、May/Aug 2025 与 Aug 2026、November 2025、estimated ~80%、99.9%+、~100k DAU、2016–2017 试点、"millions of real-time sensor and transaction events"（📄）。
- 措辞风险点（已控制）："car-park hardware"（03 正文为 "car parks"，"varied car-park hardware" 出现在挑战栏；卡片指定此措辞）；VV 支付子系统用 "Designed … which integrated … payments"（S1 O2，未写直连卡组织）；WeChat Pay 只出现在 Baidu Nuomi 下；UOB hub "integrated with … core banking, which executes settlement"（S2，hub 本身不结算）；"Has decision or joint-decision authority"（买方权限，S7）；印度 / 泰国 / 印尼为协作。
- 无 CTO / Chief Architect、无 Board、无 CEW/SCV/CCD/vendor 名称、无 MEPS+、无 held 指标；lint 0 命中。

**3. Document quality**
- 渲染：3 页，Layout OK: True；第 1 页 = header + summary + competencies + 全部 7 条 achievements；第 2 页以 PROFESSIONAL EXPERIENCE 开始；无孤立标题；页脚页码在。
- 34 条 bullet 中 4 条为 3 行（Ach-1、Ach-3、Ach-7、UOB hub 设计），在 1/5 上限内；Summary 三段分别为 4 / 3 / 3 行（pdftotext 核对）。总字数 1,316。
- 可读性：首次出现的缩写已展开（ISO 20022 (SWIFT MT-to-MX)、disaster recovery (DR)、MAS TRM (Singapore technology-risk rules)、root-cause analysis）；"MTTR" 改为 "recovery time"；去掉 "SSH to Spring MVC" 这类括号；英式拼写。
- 未执行的检查：未在 Word 中打开核对视觉效果（只检查了 renderer 的 PDF/文本输出与行数估计）。

## (e) 缺口的诚实处理

| 缺口 | 处理 |
|---|---|
| 支付终端 / POS / 支付硬件互通 | 不声称；以 IoT 车场硬件连云（PA-16）+ 两地支付集成（S1）作桥梁；面试时如实说明 "没有终端产品经验，但有设备连云平台与支付集成经验" |
| 海外市场技术战略 | 呈现为多市场平台（新加坡、中国、东南亚）与技术选型 / 预算，不写 "overseas strategy for N countries" |
| 5 年公司级技术负责人 | 只写职位与年份段，不写年数 |
| Board 汇报 | 写 senior management 与 steering committees，不写 Board |
| Localisation、succession planning | 不声称；mentoring 与 performance management 保留 |
| DevSecOps 术语 | 写实际做法（流水线中的渗透测试、secure SDLC），不用该术语 |

## (f) 给 Wilson 的问题（只列会改变事实或定位的；均附默认值）

1. **VV 的东南亚 B2B 产品**是否实际交付给新加坡以外的东南亚客户 / 国家？如有，是哪些国家、你是否参与了当地需求适配？—— 默认：保持 "a B2B online-office product serving Southeast Asia"，不写国家名、不写 localisation。
2. **AI Park 硬件侧**：你是否直接参与过车场设备（道闸、摄像头、车场控制器、网关）的接入协议或设备集成设计？—— 默认：只写 "connecting car-park hardware to the cloud"，不写设备协议或硬件设计。
3. **本地化（localisation）**：VV-Life 为新加坡市场接入本地支付方式（GrabPay 等）是否可表述为 "localised payments for the Singapore market"？—— 默认：不使用 "localise" 一词。
4. **Headline 中 "Fintech Platforms"**：02 §4 定位陈述写作 "fintech/SaaS platforms"，02 §7.2 也有 "Fintech & Payments Platforms" 的 headline 选项；正文中 Summary 用了更具体的 "payment-enabled SaaS and local-life platforms in Singapore"。是否接受 headline 这样写？—— 默认：保留（卡片指定）。
