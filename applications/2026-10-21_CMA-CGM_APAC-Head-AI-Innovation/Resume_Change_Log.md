# Resume Change Log — CMA CGM · APAC Head of AI and Innovation

- **输出：** `resume source file (working copy)` → `wilson-2026_SM_Internet_CMACGM_V1_0_0_draft.docx`（同目录有 .pdf、.txt、.report.md、.report.json）
- **Base：** `base_Talentvis_SM_Internet.json`（UOB 以 AI 开头的结构，以及 VV、AI Park、Earlier 的句子）。另外借用了 `base_TEKsystems_TPM_Internet.json` 里的 MVP 排序句和 PA-07.3 的简短版。card 列的 `LIB_wilson-2026_Senior_Tech_Internet_LIB_V5_0_0.txt` 没有读：approved JSON 加上 03 已经够用，而且 03 的状态优先于 [LIB]。
- **定位：** SM × INT。IT 技术 + 管理领导者，applied AI 和大数据是两根支柱，不写成 AI engineer 或 data scientist。
- **Headline：** card 原文 "…Rapid Prototyping & Enterprise Delivery | Governed AI in Production · Data Teams" 约 117 个字符，超过一行（≤ 105）。改成 "Technology Leader — Applied AI Adoption & Rapid Prototyping | Governed AI in Production · Data Teams"（96 字符，一行）。删掉的是 "Enterprise Delivery"，这层意思由 Summary P2 和 UOB 的 scope 行承担。

## 1. 主要内容决定（附来源 ID）

**Summary（3 段，各 3 行）**
- P1：第一句对准 JD 的核心要求，即把 AI 从原型带到受治理的生产环境，并转化为可衡量的生产力；接着写 18+ 年（02 §1）和职业弧线（Renren、Sohu、Baidu → "head-of-technology roles from 2016 to 2020"，01 §5 允许这个说法）。
- P2：沿用 Talentvis 已批准的句子（UOB VP、25 名 onshore/offshore 工程师、AI code-review 服务、文档校验 AI agent），加上 "set the human-in-the-loop rules that govern them"（PA-07.2）。没有放约 80%，这个数字只出现在 Achievement 2。
- P3：沿用 Talentvis P3 的结构，把 "enterprise customers" 改成 "a large enterprise"，并加了 "data-team leadership"。删掉了 card 写的跨时区团队（India、Thailand、Indonesia）和 AI 识别环节，因为它们分别已在 UOB C-RPT 条和 AI Park 条出现，避免重复。

**Core Competencies（7 行，按 JD Required 的优先级排）**：Applied AI in Production → AI Governance & Privacy → Prototyping & MVPs → Data & Analytics → Enablement & Change → Stakeholders & Commercial → Platforms & Cloud。
- 和 card 的差别：**删掉了 "data masking"**。它只出现在 RAG 贡献里（O5），skills inventory 没有锚点，所以只留在 Achievement 3 的 RAG 语境里。**删掉了 "AWS" 以外的云服务明细。** Data 行写 "Leading big-data teams on Spark, Hive and HBase"，因为 inventory 里这几项是 A 级，只能写"带团队"，不能写"亲手做"。Kafka 写成 "Kafka messaging"，因为证据是异步处理，不是 event streaming。"SIT/UAT sign-off" 改成 "acceptance-test sign-off"，HR 更容易看懂。"MAS FEAT" 写成 "Singapore's MAS FEAT principles"。
- "Platforms & Cloud" 里的技术都是 P 或 A 级：Java、Spring Boot、Apache Camel 是 P；Spring Cloud、AWS、Kubernetes、Docker 是 A 或 A/P。

**Selected Achievements（7 条）**
1. Prototype to governed production：PA-07.1 + S9。删掉了 "MAS-regulated"（INT lens），改为 "regulated Tier-1 bank"。
2. Measurable productivity：PA-07.3。去掉了 "each about 30% as long"，因为每条最多 1–2 个数字，而且 lint 会把 30% 标出来；保留了 "estimated ~80%" 和 "1–2 rounds"。
3. Responsible AI：PA-07.2 + S9 RAG（O5 "contributed to"，RAG 第一次出现时写全称）。
4. Workflow automation agent：PA-08（S9：O1，2026 年 4 月），一字不改沿用 Talentvis。
5. Data teams for decisions：PA-12（只用 R22 的 Spark 版本，动词改成 "Led the big-data team that built…"，符合 O2）+ AI Park 大数据团队（03 §0A "millions of real-time sensor and transaction events" 📄）。
6. Scale-up 0-to-1 delivery：S3（140, total headcount）+ PA-11.1 + PA-11.2。
7. Enablement and change：PA-10.3（从零引入 Agile/Scrum）+ PA-11.3（CI/CD、规范、容器化）+ PA-03.3（"contributed to"，锁定动词）。

**UOB（11 条 + scope 行）**
- scope 行：Talentvis 的版本去掉 "SWIFT ISO 20022 messaging" 括号和 "MAS-regulated"。
- Applied AI & Automation：PA-07.4 加汇报立项（沿用 Talentvis）；团队 coaching（PA-03 §6，沿用 Talentvis）。
- Platforms & Data：PA-05.1/05.2/05.3 + S2，把 "takes daily account summaries from core banking to support portfolio analysis" 并进去。去掉了 Cloudera，因为一条最多 3–4 个技术，而且 "Spring Batch" 改成了 "scheduled batch jobs"，不写版本或框架括号。PA-01.2 是缩短版：去掉了 "enrichment" 和 "vendor"，只保留核心。S5 一字不改。
- Delivery & Governance：
  - PA-01.1 / 01.5 改成白话："running old and new message formats side by side in phases"，代替 "Blue/Green-style coexistence / MX-rich"。只保留 2025 年 5 月上线、赶在 SWIFT 2025 年 11 月截止日之前、无服务中断这几点；2025 年 8 月和 2026 年 8 月两个里程碑为了控制长度删掉了。
  - X-02 MVP 排序：沿用 TEKsystems 的句子，对应 JD 的 MVP 和资源排序。
  - PA-03.1/03.2：MTTR 展开为 "mean time to recovery"；SIT/UAT 写成 "test sign-off"；删掉 penetration testing 以控制长度；把 bank-wide 标准移到了 Achievement 7。
  - X-06 + PA-02.3：RCA 展开写；删掉 "Splunk-based" 和 "SLIs/SLOs"，一般读者不需要。
  - X-02 + X-05：商务权限和四家 IT 服务供应商；SOW 第一次出现时写全称。
  - C-RPT：一字不改。

**Golden Bridge（3 条）：** PA-10.1（S9，只写到 "multi-tenant SaaS for online-game businesses"，不展开）；PA-10.3 + S4，用协调方给的写法 "including outsourced staff"，Agile 移到了 Achievement 7；X-01，DPIA 写全称，AWS 服务清单删掉。

**VV（4 条 + scope 行）：** PA-11.4；S1，支付子系统接入 UnionPay、Visa/Mastercard、Google Pay、GrabPay，并有 settlement reconciliation，动词用 O2 "Designed"，写的是 "integrated … payments"；PA-13，"middle-platform" 改成 "shared back-end platform"，技术括号删掉；PA-11.5。职位按 S8 写 Head of Technical Centre。

**AI Park（3 条）：** PA-16.1（SaaS 子句为了长度删掉了）；PA-16.3（AI 识别环节）；PA-16.2（投标和试点，S7）。职位按 S8 写 VP of Technical Department。

**Earlier（4 行）：** Hengshunyuan（PA-15.1，用 brief 规定的 Earlier 格式）；Baidu PA-17.1（删掉 "leading the web front-end…" 以压到 2 行）；Sohu PA-18.1（去掉 SSH / memcached 技术括号，写成 "news content-management system (CMS)"）；Renren PA-19（Talentvis 原句）。

## 2. 排除项及原因

| 排除项 | 原因 |
|---|---|
| Power BI、low-code / no-code、Citizen Developer | card 和协调方都规定不写；Power BI 在 inventory 里只有 F/P |
| digital-literacy 和 upskilling 项目、global matrix、物流行业 | 记录里没有，属于 Gap（见 Analysis e） |
| 跨境数据合规（"cross-border data requirements"） | 记录里没有 |
| S6 亲手写的核心模块清单（并发控制、权限矩阵等） | 和 AI 创新岗关系弱，篇幅优先给 AI 和数据；S5 已经说明他保持动手 |
| PA-01.4 延迟调优、PA-02.1 DR / 99.9%+、PA-04.1 lending 与 collections、PA-06 VN eTax | 和本 JD 相关性低（INT lens，AI 岗）；lending 已在 scope 行出现 |
| GBD 的 KYC 规则模型（PA-10.2） | 篇幅原因；200+ 国家的说法有 CF-11 风险 |
| VV 的 GMS 技术栈、AI Park 的微服务条（PA-16.4） | 每条技术数量受限；篇幅原因 |
| VV 和 AI Park 经历里的大数据 bullet | **偏离 card：** card 写 AI Park 经历要有 big-data team 条，但它已经并进 Achievement 5。按"同一事实只出现一次"的原则，没有在经历里重复 |
| UOB 的 coaching 同时出现在 Summary | 只留在 UOB 经历条里，避免重复 |
| ⛔ / ⚠️ 项：CTO、10M DAU、Flink、chatbot、delivery-risk forecasting、defect、ramp-up、~50 / ~20 modules、MEPS+、供应商名、CEW / SCV-CCD | brief §3 和 03 状态规定不能用 |
| Pureland（PA-20）、个人 App（PA-21）、Crypto（X-03） | brief 规定不写，或只在对方要求时提供 |

## 3. 渲染结果

- 页数 **3**（上限 3）· **Layout OK: True** · 第 1 页放下全部 Achievements：True · 第 2 页从 Experience 开始：True · 页脚有页码 · 没有孤立标题
- 总字数 1,225（Summary 146）· bullet 32 条，3 行的 5 条（Achievements "Prototype to governed production"、"Responsible AI"、"Data teams for decisions"；UOB customer-360、ISO 20022）
- Red runs 50 / 94。红色表示不是 approved 原句，这是 INT 白话改写和新的 AI 岗位组合带来的，属于预期情况。
- **Lint hits：0**
- 迭代过程：第一版有 9/32 条 bullet 是 3 行，超过 1/5 的上限。缩短了 Baidu、Sohu、AI Park PA-16.1、payment hub 和 Data achievement 后降到 5 条；之后又做了几处可读性微调（MAS FEAT 说明、SOW 全称、acceptance-test、Kafka messaging）。

## Post-audit and cold-read revisions (2026-10-26)

依据：`audit/10_Resume_Fact_Audit.md`（3 FAIL、8 REVIEW）、`coldread/10_Readability_ColdRead.md`、`brief/Revision_Brief.md` §2 canonical sentences，以及 coordinator 的一致性规则：清除 "(total headcount)"；99.9%+ 和 permission matrix 只用于 hub / middleware（本简历没有挂到 lending 或 customer-data 平台上，不需要改）。修改前的 JSON 已备份到 `drafts/10/tmp/resume_before_rev.json`。

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| 1. Summary P1 years | "18+ years of IT leadership across…" | "18+ years in IT and leadership roles across…" | Audit F1（逐字照用） |
| 2. Summary P2 HITL | "set the human-in-the-loop rules that govern them" | "set the human-in-the-loop rule that governs the code-review service" | Audit F2（逐字照用） |
| 3. A5 Data teams | "Data teams for decisions: … providing analysis that supported business decisions; …" | "Data teams: Led the big-data team that built VV Technology's data-analysis platform on Hive and Spark; earlier led AI Park's big-data team…" | Audit F3（逐字照用，3 行 → 2 行） |
| 4. Headline | "Applied AI Adoption & Rapid Prototyping \| Governed AI in Production · Data Teams" | "Applied AI in Production & 0-to-1 Delivery \| Governed AI · Data Teams" | Audit R-Q1 safe default |
| 5. Summary P1 opening | "takes AI from prototype to governed production … turns it into measurable productivity" | "takes AI into governed production … turns it into productivity gains" | Audit R-Q2 |
| 6. A1 label | "Prototype to governed production" | "Governed production" | Audit R-Q2 |
| 7. A2 label | "Measurable productivity" | "Productivity gain (estimate)" | Audit R-Q2；正文保留 "estimated ~80%" |
| 8. Summary P3 | "start-up delivery speed" | "start-up 0-to-1 delivery" | Audit R-Q3 |
| 9. Summary P3 authority | "Used to explaining … and to taking part in vendor-selection and technology-investment decisions" | "Experienced in explaining … with decision or joint-decision authority on vendor selection and technology investment" | Brief §1.3：vendor authority 的说法要统一强度（与 UOB bullet 一致）+ cold-read #6 |
| 10. CC Applied AI | "LLM agents on headless Claude Code, agentic workflow orchestration, prompt A/B evaluation, … taking AI tools through formal approval…" | "AI agents on headless Claude Code, comparing prompt versions (A/B evaluation), AgentOps/LLMOps practice, taking an AI service through formal architecture and risk approval into production" | Audit R-Q4 + cold-read #2（删掉重复的 "agentic workflow orchestration"） |
| 11. CC 第 3 行 | "Prototyping & MVPs: Rapid 0-to-1 platform builds…" | "0-to-1 Builds & MVPs: 0-to-1 platform builds…" | Audit R-Q5；label 跟随 R-Q1（没有 prototyping 的证据） |
| 12. CC Data & Analytics | "customer data models; SQL; data analysis that supports business decisions" | "customer data models for portfolio analysis; SQL" | Audit R-Q6 safe default（S2） |
| 13. A4 eMemo agent | "generates validation prompts to check schema alignment and data-relationship consistency between eMemo and quotation documents" | "generates validation prompts to check that eMemo and quotation documents are consistent in structure and data relationships" | Cold-read #1（白话化；保留 "generates validation prompts" 这个事实，没有简化成 "checks documents"） |
| 14. A6 VV | "led a 140-person technology organisation (total headcount), built its microservices platform from scratch and delivered…" | Brief §2 canonical VV 句 + "; delivered the first release of its local-life services platform in 2019, including the payment subsystem" | Brief §2 + coordinator 规则；"built" 保留（R-Q8 留给 Wilson） |
| 15. A6 label | "Scale-up 0-to-1 delivery" | "0-to-1 delivery" | 一致性（09 audit Q1："scale-ups" 没有记录支持）；减少歧义 |
| 16. UOB AI bullet 1 | "Took the AI code-review service into production: …" | "Designed, built and took the AI code-review service into production: …" | Cold-read #7（ownership 说法与 A1、Summary 一致） |
| 17. UOB customer-360 | "…from core banking to support portfolio analysis…" | "…from core banking for portfolio analysis…" | Brief §2 core-banking canonical；3 行 → 2 行 |
| 18. Delivery & Governance 顺序 | ISO → MVP → KPI → incidents → authority → report | authority → report → ISO → MVP → KPI → incidents | Cold-read #5（JD 强调影响 senior stakeholders） |
| 19. UOB ISO 20022 | "Owned delivery … with a 15-engineer team, running old and new message formats side by side in phases: live in May 2025…" | Brief §2 canonical ISO 20022 句 | Brief §2；cold-read #4 的缩短版没有采用，因为 canonical 优先。"15-engineer team" 随之删除（Summary 写的是 25 人） |
| 20. UOB MVP | "When the two platform lines' schedules conflict, agree MVP scope…" | Brief §2 canonical MVP 句 | Brief §2 + cold-read HR quote 3 / #3 |
| 21. UOB KPIs | "— deployment frequency, mean time to recovery, … — with CI/CD quality gates (99% SonarQube coverage gate, automated regression testing) and test sign-off…" | "(deployment frequency, mean time to recovery, incident trend, change-failure rate), CI/CD quality gates and test sign-off for every release" | Cold-read #4（删减行话；99% 门槛和这个 JD 无关） |
| 22. UOB incidents | "— escalation, stakeholder communication, root-cause analysis and post-incident reports; with no separate SRE team, the platform teams own…" | "…end to end, from escalation and stakeholder communication to root-cause analysis and post-incident reports" | Cold-read #4（删减）；因此 page 3 的分页刚好落在两段工作之间，AI Park 完整留在第 2 页 |
| 23. GBD team | "Led a 40-person project team, including outsourced staff, set up CI on Jenkins and Amazon ECR, and owned…" | Brief §2 canonical GBD 句（"introduced Agile/Scrum from scratch and CI on Jenkins and Amazon ECR"） | Brief §2。A7 也写了 GBD 的 Agile/Scrum：A7 是跨雇主的 change 总结，这一处重复是有意接受的 |
| 24. VV scope | "…connecting offline merchants — food, … everyday services — through data." | "VV-Life: a data-driven local-life services platform connecting offline merchants in food, fresh produce, travel and everyday services." | 修掉孤立的 "data."（audit §3 b），与 09 一致 |
| 25. VV B2B | "Designed the shared back-end platform architecture for a B2B online-office product…" | Brief §2 canonical VV B2B 句（加了 Spring Boot、MySQL cluster、Redis、RocketMQ） | Brief §2 |
| 26. Sohu | "…fifth-generation news content-management system (CMS) and delivered…" | Brief §2 canonical Sohu 句（"of Sohu's fifth-generation CMS onto Spring MVC and a Redis cluster, and delivered its OpenAPI messaging platform"） | Brief §2 |
| 27. Hengshunyuan | "Owned product, architecture and technical delivery…" | "Owned product, architecture and delivery…" | 行数预算：PDF 中从 3 行减到 2 行（与 09 用词一致） |

**没有改的：** A2 保留较短的 "1–2 rounds" 说法，没有加 "each about 30% as long"（R-Q7，没有剩余的 3 行配额）· education 和 "Software Designer (Intermediate)" 证书保持原样 · F1 里的 "start-ups and scale-ups" 是逐字照用的（问题留给 Wilson）· Cold-read 列的 Power BI、low-code、upskilling、global HQ 都是 gap 或问题，不会写进简历。

**渲染结果（2026-10-26）：** Layout OK **True** · 3 页 · page 1 = summary + competencies + 全部 7 条 achievements · 32 条 bullet，renderer 估算 3 行的 **5** 条，用 PDF 核对是 **4** 条（A1、A3、A6、ISO 20022；Sohu 在 PDF 中是 2 行）→ 12.5%，低于 1/5 · Lint **0** · 1,233 词（Summary 150）· red runs 53/94 · AI Park 不再跨页。


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K3 business team | Experienced in explaining technical choices in business terms to senior management and ste | Reports status, risks and decisions to senior management, the steering committee and the business team, and ho | C3 answer K3 (2026-10-26) |
| K3 de-duplicate | Report status, risks and decisions to senior management and steering committees, and work  | Work closely with teams in India, Thailand and Indonesia across time zones. | Merged into Summary K3 sentence (no stacking) |
| K2 steering committee (singular) | Senior management and steering committees | Senior management and the steering committee | C3 answer K2 (2026-10-26) |
