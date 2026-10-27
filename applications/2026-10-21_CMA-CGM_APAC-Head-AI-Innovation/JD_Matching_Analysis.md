# JD Matching Analysis — CMA CGM · APAC Head of AI and Innovation (JobStreet 95377348)

- **JD 来源:** `JD.md`（https://sg.jobstreet.com/job/95377348，2026-10-20 抓取的全文）
- **简历:** `wilson-2026_SM_Internet_CMACGM_V1_0_0_draft.docx`
- **读过的事实来源:** 01 v1.1 · 02 v3.1 · 03 v4.1 · 05 v1.0 · technical-skills-inventory v2.3 · fact-check v2.4（均在 `master\v2.0-draft\`）· Drafting_Brief §4 S1–S9 · `base_Talentvis_SM_Internet.json` · `base_TEKsystems_TPM_Internet.json`。LIB 文件没有读（不需要）。

## (a) 分类：SM × INT

**Family = SM。** JD 第一句就是 "This senior IT leadership role drives AI and automation across APAC"，Required 项里大多是领导类要求："lead enterprise AI adoption"、"Lead a high-performing AI and data science incubator"、"influence senior stakeholders"、"leading organisational change"。架构（ATL）和交付（TPM）只是辅助。
**Lens = INT。** CMA CGM 是航运物流集团，不是银行或 fintech。JD 看重的是速度（"rapid prototypes and MVPs"、"speed to market"）、产品化和推广，所以银行内部术语在简历里都去掉了或改成白话（MAS TRM 不出现；MAS FEAT 第一次出现时写成 "Singapore's MAS FEAT principles"）。
**定位规则：** 写成 IT 技术 + 管理领导者，applied AI 和大数据是他的两根支柱。全文没有出现 "AI engineer"、"data scientist"、"ML engineer"。

## (b) Fast-reject / 资格

- **Fast-reject（05 §4）：没有命中。** 要特别说一下 "'cross-border' logistics (false-friend keyword)" 这一条：本 JD 确实是物流公司，但 JD 里的 "cross-border" 指的是 "cross-border data requirements"（数据合规），简历里的 "cross-border payments" 也不是在套物流关键词。物流行业经验本身是 Gap（见 e），不属于 fast-reject 的情形。GPU 或模型训练不是这个岗位的核心要求。
- **资格：** "open for local employment only" → Singapore PR（02 §1）✅。"Bachelor's degree in IT, Computer Science, Data Science, or a related field" → 本科 Applied Mathematics（属于 related field），另有 Computer Science and Technology 硕士 ✅。
- **Batch match score（照抄 card，按 coverage 公式算，是用户要求保留的）：71。** 本分析不另外打分。

## (c) Evidence matrix

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | "Lead the APAC rollout, integration, and adoption of global AI platforms … compliance, and commercial ROI" | Req | PA-07.1, S9（May 2026 经正式架构与风险审批上线），PA-07.3 | Transferable：他自己设计并建成一个 AI 服务，走完受监管银行的审批，推到生产，并有估算的效益。但这是一家银行内部的推广，不是把一个 global AI platform 推到多个国家 | Achievements 1–2；Summary P1–P2；Competencies "Applied AI in Production" | "governed production", "formal architecture and risk approval", "AI tools through formal approval into production" |
| 2 | "Identify regional technology opportunities … compelling business cases that shape the global AI and technology roadmap" | Req | PA-07 §4（向 senior management 汇报立项理由和治理模型），PA-16.2 / S7（AI Park 技术投标），X-02（投资决策权） | Transferable（做过立项论证和投标）；影响 *global* roadmap 是 Gap | UOB "Applied AI & Automation" 第 1 条；AI Park 投标条；Competencies "Stakeholders & Commercial" | "briefed senior management on the case", "technology-investment decisions" |
| 3 | "Govern the balance between global platforms and locally developed solutions … scalable, reusable" | Req | X-02（MVP 排序），PA-03.3（参与制定 bank-wide 标准，O5） | Gap（没有 global 与 local 平台治理的记录）；只有团队之间的排序和参与标准制定可以算弱 transferable | UOB MVP 排序条；Achievement 7 | 不用 JD 原词 |
| 4 | "Partner with Global Enterprise Architecture and GRC … data privacy, cross-border data requirements, and responsible AI governance" | Req | PA-07.2，S9（RAG 有 access controls、data masking，O5），X-01，PA-03.4（DPIA、secure SDLC） | Responsible AI 和 data privacy 是 Direct；"cross-border data requirements" 是 Gap；与 EA、GRC 合作只算间接（AI 服务走过 architecture 和 risk approval） | Achievements 1、3；Competencies "AI Governance & Privacy"；GBD 第 3 条 | "responsible-AI principles", "data privacy impact assessments", "access controls and data masking" |
| 5 | "Define and deliver an APAC digital upskilling roadmap with HR and business leaders" | Req | PA-03 §6（带团队学 AI-assisted engineering） | Gap（没有和 HR 一起做过 roadmap）；团队层面的 coaching 可以算 Transferable | UOB "Coach engineering teams…"；Competencies "Enablement & Change" | "coaching engineering teams on AI-assisted engineering" |
| 6 | "practical capability-building across AI, Power BI, low-code/no-code automation, and digital productivity" | Req | PA-03 §6；skills inventory 里 Power BI = F/P（GBD 报表） | AI 部分 Transferable；Power BI、low-code 是 Gap（**按 card 和 brief 不写**） | 同上 | 不写 Power BI / low-code |
| 7 | "Build and scale a governed Citizen Developer community" | Req | — | Gap | — | 不写 |
| 8 | "Lead organisational change initiatives … confidence in automation … data-driven culture" | Req | PA-10.3（从零引入 Agile/Scrum），PA-11.3（CI/CD、代码规范），PA-07（AI 评审服务的推广和治理），PA-12 | Transferable：工程团队层面的变革，不是全组织的文化转型项目 | Achievement 7；Competencies "Enablement & Change" | "Introduced Agile/Scrum from scratch", "Enablement and change" |
| 9 | "Lead a high-performing AI and data science incubator … technical mentorship, and resource prioritisation" | Req | X-02（通过 squad leads 管 25 人，做 mentoring），PA-12 + PA-16（带大数据团队），X-02（MVP 排序） | Transferable：带过工程团队和大数据团队，也做过资源排序；但没有带过 data science 或 incubator 团队 | Summary P2；Achievement 5；UOB MVP 条 | "data-team leadership", "MVP scope … sequence" |
| 10 | "Deliver rapid prototypes and MVPs … validate feasibility before scale-up" | Req | PA-10.1（0-to-1 SaaS），PA-11.2（VV-Life 首版），PA-08（2026 年 4 月亲手做的 AI agent），X-02 MVP | 0-to-1 和 MVP 定范围是 Direct；先验证可行性再放大是 Transferable | Achievements 4、6；GBD 第 1 条；Competencies "Prototyping & MVPs" | "Rapid 0-to-1 platform builds, MVP scoping and sequencing" |
| 11 | "modular, documented, and production-ready for handover to regional, core IT, or global delivery teams" | Req | PA-03.1 / 03.2（CI/CD quality gates、99% SonarQube gate、测试 sign-off），S9（审批上线） | Transferable：生产就绪的把关有记录；把成果交接给其他交付团队的记录没有；"documented" 没有写 | Competencies "Prototyping & MVPs"；UOB KPI 条 | "production-ready handover through CI/CD quality gates" |
| 12 | "fast, commercially focused delivery cadence … measurable business outcomes" | Req | PA-07.3（估算约 80%），PA-08（去掉一项重复的人工任务），PA-01.1（赶在 SWIFT 截止日前上线），PA-17.1（提前两个月） | Direct（效益是估算值，限定语保留） | Achievements 2、4；UOB ISO 20022 条；Earlier Baidu | "Measurable productivity", "ahead of SWIFT's November 2025 deadline" |
| 13 | "Bachelor's degree in IT, Computer Science, Data Science, or a related field" | Elig | 02 §3 | Direct（Applied Mathematics 本科 + CS 硕士） | Education | — |
| 14 | "10+ years of technology leadership … IT transformation, data engineering, digital products, or AI/ML, including delivering production-ready AI/ML solutions" | Req | 02 §1（18+ 年），PA-07、PA-08、S9 RAG，PA-12，PA-16.3 | Direct：生产级 AI 是基于 LLM 的应用交付；ML 模型训练没有声称（见 e） | Summary P1；Achievements 1–5 | "18+ years of IT leadership", "production AI code-review service" |
| 15 | "influence senior stakeholders in complex global matrix organisations and translate regional needs into global technology strategies" | Req | C-RPT（X-02），X-02 跨时区协作（India、Thailand、Indonesia） | 影响高层是 Transferable；global matrix 组织是 Gap（D-09：没有 US 团队协作记录） | UOB C-RPT 条；Summary P3；Competencies "Stakeholders & Commercial" | "senior management and steering committees", "across time zones" |
| 16 | "managing enterprise-scale technology deployments and agile innovation or R&D environments" | Req | PA-01.1 / 01.5，PA-05，PA-10.3，PA-11 | Direct | UOB "Delivery & Governance"；GBD；VV | "mission-critical platform lines … millions of accounts", "Agile/Scrum" |
| 17 | "Practical knowledge of Power BI, low-code automation, citizen development platforms (e.g., Vibe), and generative AI frameworks" | Req | skills inventory §8（headless Claude Code、prompt A/B、AgentOps/LLMOps = P）；Power BI = F/P | GenAI 是 Direct；Power BI、low-code、citizen development 是 Gap | Competencies "Applied AI in Production" | "LLM agents on headless Claude Code" |
| 18 | "Experience leading organisational change, digital-literacy, or culture-shift programmes" | Req | PA-10.3、PA-11.3、PA-03 §6 | Transferable（工程实践变革）；digital literacy 项目是 Gap | Achievement 7 | "Enablement and change" |
| 19 | "Commercially focused and pragmatic … measurable ROI, operational stability, and speed to market" | Req | PA-07.3（估算），PA-08，X-06（P1–P3 事故管理），X-02 / X-05（投资、供应商、SOW），PA-17.1 | Direct（没有以金额计的 ROI） | Achievement 2；UOB 事故条、商务权限条 | "Measurable productivity", "operational stability" 只体现为事故管理，没有用这个词 |
| 20 | "open for local employment only" | Elig | 02 §1 Singapore PR | Direct | Header（renderer 固定） | "Singapore PR" |
| 21 | 区域（APAC）跨国职责 | Inferred | X-02 跨时区团队；PA-05 regional customer-360；PA-13 面向东南亚的 B2B 产品 | Transferable（没有正式的区域负责人职责） | UOB 末条；Platforms & Data；VV 第 3 条 | "regional customer-360 platform", "serving Southeast Asia" |
| 22 | 航运 / 物流行业知识 | Inferred | — | Gap | — | 不写 |

**第 1 页对 JD 前五项 Required 的覆盖：** #14（生产级 AI）在 Summary P1 和 Achievements 1–4；#1（推动 AI 采用和 ROI）在 Achievements 1–2；#4（responsible AI 和隐私）在 Achievement 3 和 Competencies 第 2 行；#10（原型和 MVP）在 Competencies "Prototyping & MVPs" 和 Achievement 6；#9 / #15（带团队、影响高层）在 Summary P2–P3 和 Competencies "Stakeholders & Commercial"。

## (d) 三维评审（不给总分）

**1. Job fit。** 最强的部分是 "delivering production-ready AI/ML solutions"、负责任 AI 治理、0-to-1 原型和 MVP、大数据团队、可量化的效益（估算约 80%）以及技术领导年限。中等的部分是组织变革和高层影响：有证据，但都在工程团队或单一组织内部。最弱的部分是 JD 的 "Digital Literacy & Workforce Enablement" 整块（Power BI、low-code、Citizen Developer、和 HR 一起做 upskilling roadmap），以及 global matrix 组织和物流行业。这几项在 JD 里都写成 Required 或核心职责，HR 初筛时可能被卡。card 定为 tier B，这个判断合理。

**2. 事实可靠性风险。**
- 约 80% 是 **估算**（PA-07.3），简历保留了 "estimated ~80%"，面试时需要讲清楚公式（03 PA-07 §8，R₀ ≈ 3 轮的假设 C2 仍然 open）。
- RAG 助手只写 "contributed to"（O5，S9）；简历里的 "access controls and data masking" 是那个系统本来就有的控制措施，没有说是他设计的。
- "VV Technology's data-analysis platform on Hive and Spark" 用的是 R22 的版本（PA-12 ⚠️ CF-07，Flink 版本没有用）。用的动词是 "Led the big-data team that built…"，符合 O2。
- AI Park "millions of real-time sensor and transaction events" 来自 03 §0A 📄 [LIB] / [TPL]，只出自一个来源。
- 140 人和 40 人都按 S3 / S4 的口径写：140 写成 "(total headcount)"；40 写成 "including outsourced staff"。没有出现招聘数字。
- 职位名称按 S8：VV = Head of Technical Centre，AI Park = VP of Technical Department。CF-16 / FU-3（雇佣信上的英文职位名）仍然是背景调查的风险。
- 没有出现 ⛔ 内容（CTO、10M、Flink、chatbot、MEPS+、~50/~20 modules、defect/ramp-up）。renderer lint 0 hits。

**3. 文档质量。** renderer 结果：3 页，Layout OK: True；第 1 页放下了 header、Summary、Competencies 和全部 7 条 Achievements；第 2 页从 PROFESSIONAL EXPERIENCE 开始；页脚有页码；没有孤立标题；总字数 1,225；32 条 bullet 里 5 条是 3 行（≤ 1/5）；Summary 3 段，每段 3 行。文本可以提取（.txt 和 .pdf 已生成）。**没有做的检查：** 没有在 Word 里人工打开看排版；行数是 renderer 估算的；没有做真人 cold-read。

## (e) Gap 的诚实处理

- **Power BI、low-code / no-code、Citizen Developer 平台（如 Vibe）：** 简历不写。Power BI 在 skills inventory 里只有 F/P（GBD 报表），按 card 的规定省略。面试时如实说"没有带过 citizen developer 项目"，可以拿 AI agent 自动化（PA-08）和 AI 评审服务讲"让一线团队用上自动化"的经验。
- **APAC 级的 digital literacy 和 upskilling 项目（和 HR 合作）：** 不写。简历里只体现团队层面的 coaching，以及从零引入 Agile 和 CI/CD。
- **Global matrix 组织：** 不写。只写 steering committee、senior management 和跨时区团队（India、Thailand、Indonesia）。按 D-09，不写 US 团队。
- **AI / data science incubator：** 不说带过 data science 团队，写的是"大数据团队"和"applied AI delivery"。
- **ML 模型训练和数据科学研究：** 不写（05 §7.2）。AI Park 的识别环节写成 "added an AI processing step"（集成，不是训练模型）。
- **物流和航运行业：** 没有相关经验，不做任何包装。
- **"cross-border data requirements"：** 记录里没有，不写。

## (f) 需要 Wilson 确认的问题（只列会影响事实或定位的；每题都给了默认处理）

1. **AI code-review 服务的推广范围（03 C4 剩余部分）：** 是两个团队的 25 人都在用，还是推广到了其他团队或部门？如果超出了自己的团队，就能直接支撑 JD 的 "enterprise AI adoption"。**默认：** 只写 "on each pull request"，不写采用范围。
2. **AI 赋能和培训：** 除了带自己的团队，有没有面向其他团队或部门做过 AI 工具的分享、workshop 或推广？**默认：** 只写团队层面的 coaching。
3. **Power BI（GBD）：** 是只看过报表，还是亲手做过 dashboard 或数据模型？如果是后者，可以写成 Skills 行。**默认：** 不写（card 规定）。
4. **跨境数据和数据驻留：** regional customer-360 平台或 RAG 助手有没有涉及跨国数据传输、数据驻留合规？**默认：** 不写。
5. **RAG 助手里的 access controls 和 data masking：** 是他参与设计的，还是系统本来就有的？**默认：** 作为系统已有的控制写，动词保持 O5 "contributed to"。
