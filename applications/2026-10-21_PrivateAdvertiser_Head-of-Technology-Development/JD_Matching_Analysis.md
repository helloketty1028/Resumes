# JD Matching Analysis — Card 02 · Private Advertiser (financial services) · Head of Technology Development

- **JD:** JobStreet 95063994 · https://sg.jobstreet.com/job/95063994 · full text `JD.md`（雇主未披露；Central Region；Full time；posted S$8,000–12,000/月）
- **Draft:** `resume source file (working copy)` → `out/wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0_draft.docx/.pdf`
- **Sources read:** Drafting_Brief.md、cards/02.md、01 v1.1、02 v3.1、03 v4.1、04 v1.2、05 v1.0、technical-skills-inventory v2.3、fact-check v2.4、Session_Confirmations S1–S9、base_TEKsystems / base_Talentvis JSON、LIB Senior_Tech_Bank V5、TPL 文本
- **Batch match score（从定位卡照抄，用户要求的 coverage 公式，不是本分析的评分）：95**

---

## (a) 分类：Family × Lens = **SM × BNK**

**理由：** JD 的核心职责是“带一支精简、跨职能的内部技术团队”（direction、hiring、assigning work、performance appraisal），对管理层定义的战略计划负责，同时管 BAU 与项目、供应商尽调、合规 —— 这是 Senior Manager（Head of Technology）职责，不是单纯 TPM 或架构师。雇主是 financial services，强调 “strict regulatory frameworks”，所以用 BNK lens（05 §2：banks / financial institutions / fintech → BNK）。
**混合信号：** “determine timeframes / BAU + projects in parallel / PM tools / Scrum” 属于 TPM 证据，按 05 §2 “borrow evidence where the JD asks” 借用 PA-01.5、X-02 MVP sequencing、PA-03.1、PA-10.3；“customer channels” 一项借用 INT 时期的 e-commerce / CMS / API gateway 证据（S1、PA-18、PA-10）。

## (b) Fast-reject / 资格筛查

**Fast-reject（05 §4）：未命中。** 无 C#/.NET 主栈、kdb+/q、Murex/Treasury-FX、equity OMS、制造业、Azure/Databricks CDAO、CFO 域 AI、物流 “cross-border”、SAS + 公共政策、GPU 推理基础设施。C++ 只作为 “knowledge of software programming” 的示例语言出现，不是主栈要求 → 记为 Gap，不触发 fast-reject。

**Eligibility（JobStreet 筛选题）：**
- **Right to work：** Singapore PR（02 §1，since 2024）→ 满足。
- **Qualifications：** Master's degree in Computer Science and Technology（02 §3）→ 满足 “Degree in Computer Science … or relevant”。PMP 仍为 in progress，不写 certified。
- **Years as Head of Technology：** 有 head-of-technology 头衔/职责的时期为 AI Park（Apr 2016–Sep 2017，VP of Technical Department）、Hengshunyuan（Co-founder，负责全部产品与技术）、VV（Apr 2019–Jun 2020，Head of Technical Centre）→ 合计约 **4 年（2016–2020）**。GBD（Project Manager & Architect）与 UOB（VP2 / TDM）不是 “Head of Technology” 头衔。→ 见 (f) Q3。
- **Salary：** 职位 S$8–12k；05 §9 记录过 “≥ S$12k” 的旧筛选条件（⚠️ 未生效）；卡片注明 “floor negotiable on total package”。非简历事实，由 Wilson 决定，不进入简历。

## (c) Evidence matrix

位置代码：HL = headline · Sum-P1/P2/P3 · Comp-1…7（Technology Leadership, Delivery & Prioritisation, Channels & Integration, Vendor & Commercial, Security & Compliance, Methods & Tools, Technical）· Ach-1…7 · UOB-scope, UOB-1…11 · GBD-1…3 · VV-scope, VV-1…5 · AIP-1…3 · Earlier-Heng/Baidu/Sohu/Renren · Edu。

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | Manage a lean internal tech team — software development, applications | Req (duty) | X-02, PA-01.5, PA-05.3, S5, S6 | Direct | Sum-P1/P2, Comp-1, Ach-2, UOB-1/6/7 | "leads multi-discipline teams"; "two onshore/offshore platform teams" |
| 2 | Team scope — systems engineering, infrastructure/cloud | Req (duty) | PA-10 §3, PA-11.1, PA-02.1, CF-N6 (RHEL) | Transferable — 架构并交付过 AWS 部署（GBD、VV），亲自主导 DR/failover 演练，RHEL 熟练；无“管理独立基础设施/系统工程团队”的记录 | Comp-7, GBD-3, VV-1, UOB-11 | "AWS deployment", "Linux (RHEL)", "disaster-recovery and failover drills" |
| 3 | Team scope — UI/UX | Req (duty) | PA-17.1（web front-end team 📄）, skills §1 React（P，employer ❓） | Transferable (weak) — 带过 Baidu web front-end 团队、React 亲手写；无 UI/UX 设计团队管理记录 | Earlier-Baidu, Comp-7 | "web front-end", "JavaScript (React)" |
| 4 | Team scope — payments | Req (duty) | PA-01, PA-04.1, S1, S2 | Direct | HL, Sum-P2/P3, Comp-3, Ach-1/3, UOB-3/5/6 | "Payments", "payment-gateway integrations", "payment-initiation hub" |
| 5 | Team scope — data analytics | Req (duty) | PA-05.2, S2（portfolio analysis）, PA-12（仅 R22 版本）, PA-16 | Direct | UOB-7, VV-3, Comp-7 | "portfolio analysis", "big-data team", "data analysis" |
| 6 | Team scope — cyber security | Req (duty) | X-01, PA-03.2（penetration testing in CI/CD）, PA-03.4 | Transferable — 设计安全控制（加密、凭证管理、权限）、CI/CD 渗透测试、secure SDLC；无独立 cyber-security 团队/SOC 管理记录 | Comp-5, UOB-10/11, GBD-3 | "security controls", "penetration testing" |
| 7 | Team scope — AI | Req (duty) | PA-07.1–07.3, PA-08, S9（RAG，O5） | Direct | Ach-7, UOB-8, Comp-7 | "AI code-review service", "AI agent", "AI knowledge assistant" |
| 8 | Providing direction, assigning of work | Req (duty) | X-02（through squad leads/EMs；MVP sequencing） | Transferable — 通过 squad lead / EM 管理、与各方定 MVP 顺序；“assigning work” 字面无记录 | Comp-1, Ach-2, UOB-2 | "via squad leads and engineering managers"; "set a sequence all parties accept" |
| 9 | Hiring | Req (duty) | 无（HR-9；R22 “built the organisation from scratch” 未使用） | Unverified / Gap — 不写 | — | — |
| 10 | Staff performance appraisal | Req (duty) | X-02（1:1s, mentoring, performance management ✅/📄） | Direct | Comp-1 | "mentoring and performance management" |
| 11 | Drive effectiveness and efficiency by delivering strategic plans defined with Management | Req (duty) | X-02（technology-investment decisions）, PA-01.5（roadmap；向 senior management/steering 汇报）, 02 §6.4（VV product-strategy planning）, PA-03.1, PA-07.3, PA-08 | Transferable — 执行并汇报路线图、参与投资与产品策略、用 AI 去掉手工环节；无“公司级战略规划 owner”记录 | Comp-2/4, UOB-1/4/8/10, VV-2, Ach-7 | "technology-investment decisions", "product-strategy planning", "roadmap" |
| 12 | Execute tech strategies, transformation roadmap and projects by stipulated deadlines | Req (duty) | PA-01.1, PA-01.5 | Direct | Ach-1, UOB-1, Sum-P1 | "ahead of SWIFT's November 2025 deadline"; "roadmap, milestones" |
| 13 | Oversee and determine timeframes — BAU system updates, upgrades, migrations | Req (duty) | PA-01.5 + PA-01 §4（milestones, release planning）, PA-01.1, X-01（data migration） | Direct | UOB-1/11, Ach-1, Comp-2 | "milestones", "upgrades every 2–3 months", "migration" |
| 14 | … outages | Req (duty) | X-06（P1–P3）, PA-02.1（DR/failover drills, 99.9%+） | Transferable — 写成 P1–P3 production incidents 与 DR 演练，未字面写 “outages” | UOB-9/11 | "P1–P3 production incidents", "disaster-recovery and failover drills" |
| 15 | Run BAU tech and developmental projects in parallel; PM and prioritisation | Req (duty) | CF-N3 + PA-01（同一团队承担生产支持与项目交付，🔶 framing）, X-02 MVP sequencing | Direct（🔶 framing） | Sum-P2, Comp-2, UOB-2 | "change projects alongside BAU production support"; "BAU and change projects in parallel" |
| 16 | Vendor/outsourcing — due diligence and assessment from technology perspective | Req (duty) | 02 §5（vendor technical evaluation ✅）, LIB Senior_Tech_Bank（evaluation sessions：architecture, technical credentials, fit 📄）, X-02（vendor selection, SOW/licence） | Direct — 用 “assess vendors' architecture, credentials and fit”，未字面写 “due diligence” | Ach-6, Comp-4 | "Vendor technical evaluation"; "Assess vendors' architecture, credentials and fit with existing systems" |
| 17 | … ongoing effective delivery of outcomes | Req (duty) | X-05（chair vendor governance：budget, year-end performance, accountability） | Direct | Ach-6, Comp-4, Sum-P2 | "chair governance of four IT service vendors" |
| 18 | Technology developments and infrastructures always compliant with regulations | Req (duty) | PA-03.4, X-01, X-06, S9 | Direct | Sum-P2, Comp-5, UOB-9/11 | "MAS TRM (Singapore technology-risk rules)"; "support the bank's regulatory reporting to MAS" |
| 19 | Degree in Computer Science, AI, ML or relevant | Req / Elig | 02 §3 | Direct | Edu | "Master's degree in Computer Science and Technology" |
| 20 | Minimum 8 years of technical and managing experience | Req | 02 §2, 02 §4 | Direct（18+ 年；2012 起 technical/project leader；2016–2020 head-of-technology） | Sum-P1 | "18+ years of engineering and management experience" |
| 21 | Financial services and/or strict regulatory frameworks | Req | 02 §6.1, PA-03.4 | Direct（UOB 2022 至今，约 4 年） | Sum-P1/P2, Comp-5, Ach-1/7 | "MAS-regulated Tier-1 bank" |
| 22 | Technical and business acumen; lead teams with multiple disciplines | Req | X-02, S3, TPL（VV：engineering, DevOps, data；GBD：engineering, QA, DevOps, product, operations）, PA-17.1, X-02 投资/预算 | Direct | Sum-P1, Comp-1, Ach-2, GBD-2, Earlier-Baidu | "multi-discipline teams" |
| 23 | Strong domain knowledge in customer channels / touch points | Req | 汇总 #24–#30 | Direct（部分子项 Gap） | Sum-P3, Comp-3 | "customer-channel experience" |
| 24 | — web portal development | Req | PA-19（Renren shopping website，O1）, PA-18（Sohu news CMS、website SEO）, PA-17.1 | Transferable — 做过电商网站与新闻门户（Sohu.com）CMS；未字面写 “web portal development” | Comp-3, Sum-P3, Earlier-Sohu/Renren | "E-commerce websites", "news-portal CMS" |
| 25 | — mobile application development | Req | skills §1（Swift/Kotlin F；Kotlin 仅个人项目 PA-21 ❓） | Gap — 不写 | — | — |
| 26 | — API gateway management | Req | PA-10 §2/§3 | Direct | Ach-5, GBD-3, Comp-3, Sum-P3 | "behind an API gateway", "API Gateway" |
| 27 | — content management systems | Req | PA-18.1, PA-18.2, PA-17.1 | Direct | Ach-4, Comp-3, Earlier-Sohu/Baidu | "news CMS", "publishing workflow" |
| 28 | — chatbots | Req | PA-14 ⛔；S9 RAG knowledge assistant（O5，非 chatbot） | Gap — 不写；RAG 只作为 contribution，且不称 chatbot | （UOB-8 邻近证据） | — |
| 29 | — B2B / B2C integration platforms | Req | PA-01.2 + S2（channels、third-party banking systems、core banking）, PA-10.1（business tenants）, PA-13（B2B online-office）, VV-Life / Renren Mall（B2C） | Direct | Comp-3, Ach-5, VV-4, UOB-5, Sum-P3 | "B2B and B2C platforms", "B2B SaaS platform", "channel and core-banking integration" |
| 30 | — electronic payment gateways | Req | S1 | Direct | Ach-3, Comp-3, Sum-P3 | "payment-gateway integrations"（Alipay, WeChat Pay, UnionPay；Visa/Mastercard, Google Pay, GrabPay） |
| 31 | PM and collaboration tools — Microsoft Project, Confluence, Jira Software | Req | skills §11 | Direct | Comp-6 | "Jira, Confluence, MS Project, Miro" |
| 32 | — Kanban Boards | Req | 无锚点 | Gap — 不写 | — | — |
| 33 | Coding languages — Java | Req | skills §1（P）, S5, S6 | Direct | Comp-7, Sum-P3, UOB-6 | "Java" |
| 34 | — JavaScript | Req | skills §1 React（P，employer ❓） | Direct（只在 skills 行；employer 锚点 ❓） | Comp-7 | "JavaScript (React)" |
| 35 | — C++ | Req | 无 | Gap — 不写 | — | — |
| 36 | Demonstrated strong ability to meet deadlines | Req | PA-01.1, PA-17.1 | Direct | Ach-1, Earlier-Baidu, Sum-P1 | "ahead of SWIFT's November 2025 deadline"; "two months ahead of plan" |
| 37 | Agile delivery (Scrum) | Req | PA-10.3, PA-01 §6 | Direct | Comp-6, GBD-1/2 | "Agile/Scrum"; "introduced Agile/Scrum from scratch" |
| 38 | Problem solver; multiple points of view; challenging the norm | Req (soft) / Inferred | PA-01 §4 decision（分阶段 coexistence 而非 big-bang）, PA-01 §6 trade-off forums, PA-17 | Transferable — 用决策实例体现，不写形容词 | Ach-1 | "not a big-bang cutover" |
| 39 | Strong stakeholder management | Req | PA-01 §9（TPL/TEK primary-interface 句）, X-02 MVP agreement, PA-01.5 steering | Direct | UOB-4, UOB-2, Comp-2 | "primary interface between business stakeholders…"; "steering committees" |
| 40 | Manage remote or hybrid teams effectively | Req | X-02（25 名 onshore/offshore；与 India/Thailand/Indonesia 团队协作）, §0A 5+ years offshore | Direct | Sum-P2, Comp-1, Ach-2, UOB-scope | "onshore/offshore, cross-time-zone teams; 5+ years managing offshore teams" |
| 41 | Right to work in Singapore | Elig | 02 §1 | Direct | Header | "Singapore PR" |
| 42 | Expected monthly basic salary | Elig | 05 §9（⚠️ 未生效）, card note | Wilson 决定 | — | — |
| 43 | Years' experience as a Head of Technology | Elig | 02 §2 | 约 4 年（2016–2020），见 (f) Q3 | Sum-P1（"2016–2022 in head-of-technology and architect roles"） | — |
| 44 | Qualifications held | Elig | 02 §3 | Master's ✓；PMP in progress；无其他证书 | Edu | — |

**Page-1 检查（JD 前五项有证据的 Required）：** ① 金融业/强监管 → Sum-P1/P2、Comp-5、Ach-1/7；② 带跨职能团队 → Sum-P1、Comp-1、Ach-2；③ customer channels（API gateway、CMS、B2B/B2C、payment gateways、电商网站）→ Sum-P3、Comp-3、Ach-3/4/5；④ 按期交付 → Sum-P1、Ach-1；⑤ 8+ 年技术与管理 → Sum-P1。Agile、PM 工具、编程、remote/hybrid 也都在第 1 页（Comp-1/6/7、Sum-P2/P3）。

## (d) 三维评审（不打总分、不给 %）

**1. Job fit**
- **强项（Direct）：** 金融业强监管交付（UOB、MAS TRM）；通过 squad lead / EM 带团队、绩效管理、onshore/offshore；按期交付（ISO 20022 在 SWIFT 截止日前上线，Baidu 提前两个月）；payments 与 electronic payment gateways（S1，含 Alipay、WeChat Pay、UnionPay、Visa/Mastercard、Google Pay、GrabPay）；CMS（Sohu）；API gateway 与 B2B SaaS（GBD）；B2B/B2C 平台；供应商技术评估与治理（four IT service vendors）；Agile/Scrum、Jira/Confluence/MS Project；Java。
- **Transferable：** 战略计划执行（有路线图、投资决策、产品策略参与，但无公司级战略 owner 记录）；outages（以 P1–P3 incidents + DR 演练体现）；cyber security、systems engineering/infra、UI/UX 作为团队职能（有相关实践，无独立团队管理记录）；web portal（电商网站、新闻门户 CMS）。
- **Gap：** mobile application development、chatbots、C++、Kanban、hiring（无记录）。均未写入、未包装。
- **规模与级别：** JD 要 “lean internal tech team”，Wilson 现管 25 名工程师（两条平台线），历史上 VV 140 人（total headcount）——规模不是短板。银行年限约 4 年，JD 没有要求金融业年限下限。

**2. Factual-reliability risks（需 Wilson 知悉）**
- **UOB 团队的 “multi-discipline”：** Sum-P1 写 "leads multi-discipline teams … currently in a MAS-regulated Tier-1 bank"。UOB 团队含 QA/BA 的说法只来自 [LIB]（📄 "developers, QA and business analysts"），03 未记录。跨职能的直接证据在 VV（engineering, DevOps, data，TPL 📄）、GBD（engineering, QA, DevOps, product, operations，TPL 📄）、Baidu（web front-end, CMS, QA，PA-17.1）。→ (f) Q4。
- **"BAU and change projects in parallel"：** 🔶 框定 —— 依据 CF-N3（无独立 SRE/生产支持团队，他的团队负责生产支持）+ PA-01（同一团队交付项目）。面试时可直接解释。
- **React：** 技能清单为 P ✅，但 employer 锚点 ❓ → 只放在 Comp-7 技能行，不进 Summary/bullet。→ (f) Q5。
- **"news-portal CMS"：** Sohu.com 是新闻门户，Wilson 负责其 news CMS（PA-18）；"portal" 是对雇主网站的描述，不是新增事实。若审计认为不妥，回退为 "news CMS"。
- **Vendor 评估措辞：** "architecture, credentials and fit with existing systems" 来自 [LIB] Senior_Tech_Bank（📄），与 02 §5 "vendor technical evaluation ✅" 一致；未使用 “due diligence” 字面。
- **AI Park SaaS model：** 02 §6.6 写 "for **future** B2B/B2G customers"；03 PA-16 §2/§4 与已批准的 Talentvis 句子都没有 "future"。沿用已批准写法 "for business and government customers"；如需更保守可加 "future"。
- **GBD 业务性质（OQ-1.9 未决）：** 只写 "multi-tenant SaaS platform for online-game businesses"（S9），未展开。金融业雇主可能追问是否涉及 real-money gaming。
- **头衔：** VV = Head of Technical Centre、AI Park = VP of Technical Department（S8；02 §2 的 "Development" 写法待回填 TU-13；背景调查需与雇佣文件一致，CF-16）。
- **数字与限定语全部保留：** "estimated ~80%"（估算，非遥测）、"99.9%+"、"99% SonarQube coverage gate"（coverage 定义 ❓，面试可能追问 new-code vs overall）、"(total headcount)"（VV 140）、"~1,500"、"~100k"、"every 2–3 months"、"15-engineer"、"10-engineer"、"25"。"no service interruption" 为 📄（按 03 safe wording 使用）。
- **SWIFT 截止日：** 是行业/网络截止日，不是监管截止日 → 标签写 "Migration ahead of deadline"，不写 "regulatory deadline"。
- **Hengshunyuan 与 VV 重叠（Apr–Sep 2019）：** 按 D-10 不标注，面试解释（公司已基本停业，VV 为主职）。

**3. Document quality**
- **渲染结果（render.py 报告 + PDF 实测）：** 3 页 · Layout OK: **True** · 第 1 页 = header + headline + summary + competencies + 全部 7 条 achievements · 第 2 页以 PROFESSIONAL EXPERIENCE 开头 · 页脚 "Page X of 3" ✓ · 无孤立标题 ✓ · AI Park 整段落在第 3 页顶部（未被拆页）。
- **可读性限制：** headline 1 行 · Summary 3 段，各 4 行（56–57 词）· Competencies 7 行，标签 1 行、内容 ≤ 2 行 · 33 条 bullet/achievement/earlier 中 4 条为 3 行（12%，上限 1/5）· 全文 1,341 词 · lint 0。
- **3 行条目及理由：** Ach-1（日期里程碑 + "no service interruption"）、Ach-3（S1 的品牌归属必须逐一准确，不能合并以免把 WeChat Pay 放到 Renren 下）、Ach-7（"after formal architecture and risk approval"、"estimated ~80%" 限定语）、UOB-11（"99.9%+" 指标与 MAS TRM 合规内容）。
- **ATS：** pdftotext 可完整抽取文字；competency 表为简单两列，无合并单元格。
- **视觉检查：** 已将 PDF 三页以 80 dpi 渲染为图片逐页查看（版式、表格、页码、分页正常）。
- **未执行的检查：** 未在 Microsoft Word 中打开核对（仅 LibreOffice 渲染）；未生成去红的 final 版。

## (e) Gap 的诚实处理

- **Mobile application development：** 未写。Swift/Kotlin 只是熟悉；个人 Android 应用（PA-21）的简历用途仍 ❓，也不能代表“管理移动开发项目”。面试口径：hub 接收 Internet Banking 等数字渠道请求，属于渠道集成，不是 app 开发。
- **Chatbots：** 未写（PA-14 ⛔）。S9 的 RAG knowledge assistant 只以 "contributed to a production AI knowledge assistant" 出现，不称 chatbot。
- **C++、Kanban：** 未写（无锚点，且 brief 禁止）。
- **Hiring：** 未写；只写 "mentoring and performance management"。不使用 R22 的 “built the organisation from scratch”（避免与 140 人并列造成招聘暗示，HR-9）。
- **UI/UX、cyber security、systems engineering 团队：** 只写已有实践（web front-end 团队、React；安全控制与渗透测试；AWS 部署、DR 演练、RHEL），不声称管理过这些独立团队。
- **"due diligence"、"outages"、"web portal development"：** 均未字面使用，改用有证据支撑的说法（vendor technical evaluation / P1–P3 incidents + DR drills / e-commerce websites + news-portal CMS）。

## (f) 给 Wilson 的问题（只列会改变事实或定位的；每条附默认做法）

1. **Hiring：** 你在 UOB、GBD 或 VV 是否亲自负责过招聘（面试、发 offer）？如是，可加 "hiring"（不写人数）。**默认：** 不写。
2. **Mobile app：** 你带过的团队是否交付过移动 App（例如 VV-Life App、AI Park 停车 App）？你的角色是什么？**默认：** 记为 Gap，不写。
3. **筛选题 “years as Head of Technology”：** **默认回答 4 年**（2016–2020：AI Park、Hengshunyuan、VV）。若你认为 GBD 也算 head-of-technology 职责，可答 6 年，但 GBD 头衔是 Project Manager & Architect，需能解释。
4. **UOB 两个团队的组成：** 除工程师外是否包含 QA、BA 等其他职能？**默认：** 保留 Sum-P1 "leads multi-discipline teams"（以 VV/GBD/Baidu 为直接证据）；若 UOB 仅为工程师，改为 "who has led multi-discipline teams"。
5. **React 的雇主锚点：** 在哪家公司/项目亲手写过 React？**默认：** 只放在 Technical 技能行。
6. **GBD 业务性质（OQ-1.9）：** casual/social gaming 还是 real-money gaming？对金融业雇主影响面试口径。**默认：** 维持 S9 写法，不展开。
7. **"Outages"：** 你处理过的 P1 事件中是否有系统停机（outage）？可否写 "outages"？**默认：** 保持 "P1–P3 production incidents"。
