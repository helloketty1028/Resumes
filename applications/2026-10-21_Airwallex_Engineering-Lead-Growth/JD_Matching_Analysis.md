# JD Matching Analysis — Airwallex · Engineering Lead/Manager, Growth (SG/SH)

- **JD:** JobStreet 88086261 · https://sg.jobstreet.com/job/88086261 · `JD.md`
- **Resume draft:** `wilson-2026_SM_Internet_Airwallex_V1_0_0_draft.docx` (+ `.pdf`)
- **Batch match score (copied from card 06, coverage formula, user-requested):** 81 · tier B
- **JD 完整性：** JD 不完整 —— 只有 Responsibilities（8 条）和公司 / 团队介绍，**没有 Requirements 段**。下面的矩阵以 8 条职责为主体（按 Req 处理，标 "Req (resp.)"）；"The Opportunity" 和 "Attributes We Value" 中出现的工作内容只标为 **Inferred**，不当作硬性要求，也没有臆造年限、学历或技术栈要求。

---

## (a) 分类：Family × Lens

**SM × INT**（与 card 一致）。

- **Family = SM：** 职责 1、5、7 是带人（目标、反馈、发展计划、招聘培训、代码规范），职责 2、6 是和 PM 一起做方案和 backlog；同时职责 3、4 要求 hands-on 设计和实现。这是"带团队、亲手做设计和代码评审的工程经理"，不是 TPM（没有 RAID、vendor、steering）。05 §2 规定混合型 JD 按承担多数 required 职责的 family 归类 → SM，ATL 的 hands-on 证据按需借用（S5、S6、PA-01.4）。
- **Lens = INT：** Airwallex 是 fintech，但这个岗位在 Growth 团队（获客、onboarding、高流量页面、A/B 实验、营销平台集成），招聘方式和互联网公司一样。按 05 §2 的"fintech scale-up hiring like an internet company → per JD"规则选 INT：前面放 0-to-1、消费级平台、支付集成和工程效能；银行术语只在 UOB 段保留，首次出现时解释（例如 "ISO 20022 (SWIFT MT-to-MX)"）。

## (b) Fast-reject / 资格筛查

- **Fast-reject（05 §4）：** 无命中（不是 C#/.NET、kdb+、Murex、OMS、制造业、Azure/Databricks、GPU 推理等）。
- **工作地点 / 身份：** Singapore PR ✅，可在新加坡工作。JD 写的是 "open for Singapore and Shanghai" —— 简历不对上海做任何表态（card 要求），只写语言行 English and Mandarin。
- **职位状态：** 截至 2026-10-20 已发布 30 天以上 → **投递前先确认职位仍然开放**。
- **薪资 / 职级：** JD 未写，无法核对。

## (c) Evidence Matrix

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | Lead a team of engineers, set goals and development targets, support with feedback and development plans | Req (resp.) | X-02 (25 engineers via squad leads / EMs; 1:1s, mentoring, performance management); S3, S4 (140 / 40 total headcount) | **Direct**（带团队、1:1、mentoring、绩效管理）· "goals / development plans" 字面上 **Transferable**：绩效管理一般包含目标和反馈，但记录里没有单独写"为工程师定发展计划"，所以没有使用这个说法 | Summary P2; Competencies "Engineering Leadership"; Achievement "Engineering teams at scale"; UOB "Team & Productivity" b1 | "leading engineers", "1:1s, mentoring and performance management" |
| 2 | Work with PMs to analyse product requirements, produce technical solutions & execution plan | Req (resp.) | X-04 (co-design technical solutions with engineers for new requirements); PA-01 §9 (product owners); X-02 MVP sequencing; PA-01.5 (release planning) | **Direct** | Summary P1 first sentence + P2; Competencies "Product Delivery"; UOB "Delivery with Product" b1–b2 | "product requirements", "technical solutions", "execution plans", "product owners" |
| 3 | Hands-on design, implement and deliver software functions | Req (resp.) | S6 / PA-01.3 (personally built hub core modules incl. concurrency control); S5 / X-04; PA-05.2; PA-07.1 (O1+O2); PA-01.4 | **Direct** | Achievement "Hands-on technical leadership", "Faster code review"; UOB "Engineering & Design" | "hands-on", "design", "personally built" |
| 4 | Analyse and validate the technical design from the team | Req (resp.) | S5 / X-04（与工程师共同设计方案、负责架构）; PA-01.2 (led end-to-end design) | **Direct** | Achievement "Hands-on technical leadership"; UOB "Engineering & Design" b1 | "co-design solutions with engineers and own the architecture" |
| 5 | Review code from team members and ensure the standards | Req (resp.) | S5（每天评审新提交的核心 PR）; PA-07.1/07.3 (AI review service); PA-03.1–03.3 (quality gates; contributed to bank-wide code-review standards, locked verb) | **Direct** | Headline; Achievements "Hands-on technical leadership", "Faster code review"; Competencies "Engineering Leadership"; UOB "Delivery with Product" b3 | "review newly submitted core pull requests daily", "code-review standards" |
| 6 | Engage with PM to build a backlog that contributes to the roadmap | Req (resp.) | TEKsystems approved Agile-governance bullet (sprint planning, backlog prioritisation, Jira/Confluence); PA-01.5 (roadmap); PA-10 hybrid delivery (backlog tracking) | **Direct** | Competencies "Product Delivery"; UOB "Delivery with Product" b1; Golden Bridge b2 | "backlog prioritisation", "sprint planning" |
| 7 | Contribute to hiring, training and development of engineers | Req (resp.) | X-02 (mentoring, performance management); PA-03 §6 (coach teams on AI-assisted engineering) | **Training / development: Direct** · **Hiring: Gap**（没有可用的招聘数据；HR-9 禁止写招聘人数） | UOB "Team & Productivity" b1; Competencies "AI-Assisted Engineering" | "mentoring", "coach teams" —— 未用 "hiring" |
| 8 | Collaboration with local/global engineering, infrastructure and PM teams | Req (resp.) | X-02 (India, Thailand, Indonesia across time zones; collaboration, not line management); PA-01 §9 (infrastructure, operations, compliance, architects, product owners) | **Direct**（区域范围）· 没有和美国团队合作的记录（D-09） | Summary P3; UOB "Team & Productivity" b3 | "infrastructure, operations, compliance and architecture teams", "across time zones" |
| 9 | Onboarding optimisations / new-user funnels | Inferred (team context) | PA-10.2 (hierarchical KYC identity verification after benchmarking competitor apps; authentication-level rules) | **Transferable** —— 桥接：KYC / 分级身份认证是用户 onboarding 的环节；**没有** funnel 或转化率优化的证据 | Headline "User Onboarding"; Achievement "User identity and onboarding rules"; Competencies "Consumer Platforms" | "KYC identity verification" —— 未用 "funnel" |
| 10 | Scalable architectures for high-traffic pages | Inferred | PA-11.4, PA-16.4 (millisecond-level services); PA-01.4 (latency under high load); PA-17.1, PA-19 (consumer e-commerce platforms) | **Transferable** —— 是高并发后端和消费级平台经验，不是前端页面性能；没有可用的流量数字（10M DAU / QPS 被 hold） | UOB "Engineering & Design" b2; VV b3; AI Park b2; Competencies "Hands-On Engineering" | "high-concurrency systems", "millisecond level" |
| 11 | Robust A/B testing frameworks | Inferred | — | **Gap** —— 只有 prompt A/B 评估（PA-07.4），这和增长实验不是一回事，保留在 AI 语境里 | 未声称 | — |
| 12 | Integrating global marketing platforms | Inferred | — | **Gap** | 未声称 | — |
| 13 | Leverage data to craft experiences | Inferred | PA-12 (big-data team, data analysis supporting business decisions); PA-05.2 | **Transferable**（是数据分析平台，不是增长分析） | VV b4; UOB "Engineering & Design" b3; Competencies "Cloud & Data" | "data analysis that supported business decisions" |
| 14 | Turn zero-to-one ideas into real products; get stuff done end to end | Inferred (attributes) | PA-15.1 (co-founded, ~100k DAU); PA-10.1 (0-to-1 SaaS); PA-11.1/11.2 (from scratch, first release) | **Direct** | Achievement "Consumer product from 0 to 1"; Golden Bridge b1; VV b1–b2 | "0 to 1", "from scratch" |
| 15 | Use AI to work smarter and solve problems faster | Inferred (attributes) | PA-07.1/07.3, S9 (live since May 2026, human-in-the-loop) | **Direct** | Achievement "Faster code review"; UOB "Team & Productivity" b2; Competencies "AI-Assisted Engineering" | "AI-assisted engineering" |
| 16 | Payments / financial platform domain (company context) | Inferred | S1 (Alipay, WeChat Pay, UnionPay, Visa/Mastercard, Google Pay, GrabPay; settlement reconciliation); PA-01; S2 | **Direct**（作为领域背景）—— 所有措辞都是 "integrated … payments"，没有写 card-scheme 直连 | Achievement "Payments across wallets and cards"; Competencies "Payments"; Earlier (Renren) | "payment integrations", "settlement reconciliation" |
| 17 | Location: Singapore or Shanghai | Elig | 02 §1 (Singapore PR) | **Direct** for Singapore · Shanghai：不表态 | Header | — |

**第 1 页覆盖情况：** JD 前五条有证据支持的职责（1、2、3、4、5）在第 1 页都能看到 —— Summary P1–P2（2、3）、Competencies "Engineering Leadership" / "Product Delivery"（1、2、5、6）、Achievements "Hands-on technical leadership" / "Faster code review" / "Engineering teams at scale"（1、3、4、5）。

## (d) 三个维度的评审（不打总分）

**1. 岗位匹配**
- 强项：JD 核心是"带人 + 亲手设计 / 评审代码 + 和 PM 做方案和 backlog"，三项都有直接证据：现在 UOB 每天评审核心 PR、亲手写核心模块（S5/S6）、AI 代码评审服务（PA-07），之前有 140 人 / 40 人团队（S3/S4），也和 PM 一起做 backlog。消费级平台背景（Renren、Sohu、Baidu Nuomi、VV-Life、自己联合创办的 app 达到 ~100k DAU）和钱包 / 银行卡支付集成（S1）对 fintech 增长团队很有用。
- 弱项：Growth 团队的专业内容（funnel、A/B 实验框架、营销平台集成、转化 / 留存指标）**没有证据** —— 这是这份 JD 最大的差距。最近 4 年在银行，最后一段互联网经历在 2022 年结束；简历用 0-to-1 经历和银行里交付上线的 AI 服务来说明速度。上海选项和招聘职责也没有证据。

**2. 事实可靠性风险**
- 头衔、日期、学历都按 brief 的固定写法照抄；VV = Head of Technical Centre，AI Park = VP of Technical Department（S8）。
- 数字都来自 Metrics Bank / S 项：18+、25、millions of accounts、estimated ~80%（保留 "estimated"）、1–2 rounds、140 / 40（total headcount）、~100k、~1,500、15 → 简历终稿没用、10、99% SonarQube、May/Aug 2025、Nov 2025、Aug 2026、May 2026、two months ahead。每条最多 2 个数字。
- 动词和归属层级：hub 核心模块 "personally built"（O1，S6）；hub 设计 "Led end-to-end design"（O2）；VV 支付子系统 "architected"（O2，S1）；Baidu / Renren 支付集成 "designed and coded"（O1+O2，S1）；140 / 40 写 "led … (total headcount)"，没有用 "built"；全行标准写 "contributed to"。
- **需要注意的点：** ① 标题里的 "User Onboarding" 是根据 KYC 证据做的 🔶 解读 —— 面试时会讲成"分级身份认证和认证规则"，不讲成 funnel 优化。② GBD 业务写法是 "online-game businesses"（S9）—— Airwallex 是持牌支付公司，可能会追问业务性质（OQ-1.9 仍未关闭）。③ VV-Life 支付集成写的是 "integrating … payments"，没有写卡组织直连（S1）。④ "~80%" 是估算，面试时要讲计算方法（PA-07 §8）。
- 刻意没有使用：10M DAU、QPS、200+、"~50 / ~20 modules"、Flink、chatbot、ramp-up / defect 指标、招聘人数、CTO。

**3. 文档质量**
- 渲染器报告：3 页 · 第 1 页包含页眉 + Summary + Competencies + 全部 7 条 Achievements · 第 2 页以 PROFESSIONAL EXPERIENCE 开头 · 有页码 · 没有孤立标题 · 没有超行标记 · **Layout OK: True** · lint 命中 0 · 31 条中有 5 条是 3 行（都在规定的 1/5 以内）。
- Summary 3 段，估算 4 / 3 / 3 行（157 词）。标题估算 1 行。
- 总字数 1,229，比通常的 1,350–1,550 少；第 3 页还有空间。这是有意为之（第 1 页已经排满；合并重复内容而不是叠加），需要的话可以在 UOB 段再加一条（例如 PA-04.1 贷款与催收）。
- 已检查：用 pdftotext 抽取文字（文字可正常抽取，内容不在文本框里）、英式拼写（organisation、prioritisation、containerised）、所有 3 行条目。**没做的检查：** 没有在 Microsoft Word 里打开核对分页（只看了 LibreOffice 生成的 PDF），也没有做 ATS 解析测试。

## (e) 差距的诚实处理

| 差距 | 处理方式 |
|---|---|
| A/B 实验框架、增长 funnel、营销平台集成 | 不声称，不写这些关键词；prompt A/B 只出现在 AI 代码评审的语境里。面试时可以说明：有消费级平台的工程经验，但没有专门做过增长实验平台。 |
| 消费级增长指标（转化、留存、GMV） | 简历里没有；规模用 ~100k DAU、140 人组织、数百万账户来体现。 |
| 招聘 | 只写 mentoring / coaching / 绩效管理，不写招聘人数，也不用 "hiring" 这个词（HR-9）。 |
| 高流量页面（前端） | 用高并发后端和毫秒级服务证据做桥接；React 有动手经验但没有雇主锚点 → 没写（见 OQ-1）。 |
| 上海 | 不表态。 |
| 最近的互联网公司经历在 2022 年结束 | 用 0-to-1 经历和 2026 年在银行里上线的 AI 服务来说明速度。 |

## (f) 需要 Wilson 确认的问题（只列会改变事实或定位的；每个都给了默认处理）

1. **React：** 你的 React 前端动手经验是在哪家公司、哪段时间？（技能清单 employer ❓）—— *默认：* 不写。
2. **工程师的目标和发展计划：** 在 UOB，你是否亲自（或通过 squad lead）为工程师设定目标、写发展计划？—— *默认：* 只写 "1:1s, mentoring and performance management"。
3. **AI 代码评审的覆盖范围（C4 剩余部分）：** 25 名工程师是不是都在用？—— *默认：* 不写覆盖范围。
4. **GBD 的业务性质（OQ-1.9）：** 是休闲 / 社交游戏，还是真钱游戏？面对持牌支付公司，这个影响很大。—— *默认：* 保持 "online-game businesses"，不展开。
5. **职位是否仍开放，以及工作地点（只考虑新加坡，还是也接受上海）：** —— *默认：* 只投新加坡，简历不提上海。
