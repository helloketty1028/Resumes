# Resume Change Log — Card 02 · Private Advertiser · Head of Technology Development

- **File:** `out/wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0_draft.docx`（+ `.pdf`, `.txt`, `.report.md/.json`）· source `resume.json`
- **Date:** 2026-10-21 · draft (red = wording not found verbatim in an approved resume)

## 1. Base and positioning

- **Base:** approved TEKsystems JSON（delivery、stakeholder、GBD/VV/Earlier 句子）+ approved Talentvis JSON（UOB 架构/交付、customer-360、AWS、VV、AI Park 句子）+ `LIB_wilson-2026_Senior_Tech_Bank_LIB_V5_0_0.txt`（SM × BNK 单元；vendor evaluation 措辞）+ TPL（VV 技术中心构成、GBD 跨职能）。
- **Positioning：** SM × BNK。第一印象 = “在强监管金融机构里带跨职能团队、按期交付 BAU 与变更项目的技术负责人”，再用 customer channels（电商网站与支付网关、新闻 CMS、API gateway 后的 B2B SaaS、本地生活平台支付）补足 JD 的渠道域要求；hands-on Java 作为差异点。
- **Headline:** "Head of Technology Development — Payments, Digital Channels & Integration | Regulated Delivery · Hands-On Engineering"（JD 职位名原样引用）。

## 2. 与定位卡的偏差（及原因）

| # | Card 02 计划 | 实际 | 原因 |
|---|---|---|---|
| D1 | Headline "… & Integration **Platforms** \| …" | 删去 "Platforms" | 原句宽度 1.03 行，会折成 2 行；删一个词后 0.95 行 |
| D2 | Ach-1 标签 "Regulatory deadline met" | "Migration ahead of deadline" | SWIFT 2025 年 11 月截止日是行业/网络截止日，不是监管截止日；写 "regulatory" 属夸大 |
| D3 | Ach-2 = X-02（25 人、1:1s、mentoring、performance management） | X-02（两个 onshore/offshore 团队，经 squad lead/EM）+ S3（VV 140 人，total headcount，engineering/DevOps/data） | 第 1 页需要“跨职能 + 规模”证据；"25" 已在 Sum-P2（避免重复）；mentoring/performance management 移到 Comp-1；跨时区协作移到 UOB scope —— 让 Ach-2 保持 2 行 |
| D4 | Ach-3 = S1 + hub 短句（PA-01.2） | 只用 S1 | hub 已在 UOB-5，避免重复；S1 的品牌归属需逐一写清（3 行） |
| D5 | Ach-4 = PA-18.1 + PA-18.2 | 去掉技术括注 "(SSH to Spring MVC; memcached cluster to Redis cluster)" | 对 HR 是术语，且超长；CMS 领域与 publishing workflow 才是 JD 关注点 |
| D6 | Ach-5 = PA-10.1（AWS API Gateway、KYC、payments） | 加 "behind an API gateway"（PA-10 §2），删 "on Spring Cloud and Kubernetes" 与 "analytics" | 2 行限制；技术栈已在 Comp-7 与 GBD-3 |
| D7 | Competencies：Delivery 行含 Agile；单列 Tools 行 | Agile/Scrum、hybrid Waterfall 并入 "Methods & Tools"；Technical 行增加 Apache Camel、Linux (RHEL)、Splunk、Spark、Claude Code；Channels 行的钱包/卡品牌只在 Ach-3 出现 | 行数 7 不变；覆盖 JD 团队职能（systems、data、AI）；避免第 1 页重复列品牌 |
| D8 | UOB 子标题 "Platforms & Integration"（含 S5） | "Platforms, Integration & AI"；S5 移到 Sum-P3，S6 单列 UOB-6；新增 UOB-8（PA-08 + S9 RAG） | Merge, don't stack：S5 只出现一次；JD 团队职能含 AI |
| D9 | Governance 组含 PA-03.1/03.2、PA-03.4、X-01、X-06 | 另并入 PA-02.1（DR 演练、99.9%+）到 UOB-11；PA-03.3（bank-wide standards）删去 | JD 提到 outages/infrastructure；UOB-10 保持 2 行 |
| D10 | VV 3–4 条，含 S3 | 5 条；S3 移到 Ach-2；VV-1 只写平台；新增 VV-3 big-data team（PA-12，R22 版本，已批准句） | JD 团队职能含 data analytics；VV-1 不再出现 "built" 与人数并列 |
| D11 | AI Park 2 条 | 3 条（新增 SaaS model + PA-16.3 AI 识别步骤） | 第 3 页有空间；B2B/B2G 与 AI 相关 |
| D12 | Earlier：Baidu + S1、Renren + S1 | S1 只在 Ach-3 出现；Baidu 行保留团队与提前交付，删 "Dubbo microservices" | 避免重复；Baidu 行压到 2 行 |

## 3. 内容决定（逐项，含来源 ID）

**Summary**
- Sum-P1：18+ years（§0A）；"leads multi-discipline teams and delivers BAU and change projects to deadline, currently in a MAS-regulated Tier-1 bank"（X-02、CF-N3 + PA-01 🔶、PA-01.1、02 §4）；"Began as a Java engineer and technical lead … Renren, Sohu and Baidu"（02 §2、skills Java P）；"then spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups"（Talentvis 已批准句）。
- Sum-P2：Talentvis 已批准开头 "Since 2022, a Vice President in UOB's Group Technology & Operations, leading 25 onshore and offshore engineers"（X-02）+ "two platform lines … millions of accounts"（02 §6.1）+ "Delivers change projects alongside BAU production support"（CF-N3 + PA-01，🔶）+ "governs IT service vendors"（X-05）+ "applies MAS TRM (Singapore technology-risk rules) through secure SDLC and data governance"（PA-03.4、S9）。
- Sum-P3：customer channels 叙述（S1、PA-18、PA-10、PA-13、VV S1 卡与钱包支付）；hands-on 句用 S5 措辞（不含 ~50/~20）。

**Core Competencies**（7 行，按 JD Required 优先级）：Technology Leadership（X-02、§0A 5+ years）· Delivery & Prioritisation（X-02、PA-01 §4/§6、PA-01.5、X-01）· Channels & Integration（S1、S2、PA-18、PA-10、PA-13、PA-01.2）· Vendor & Commercial（02 §5、X-02、X-05）· Security & Compliance（PA-03.4、X-01、PA-03.2、X-06；DPIA 首次出现时展开）· Methods & Tools（skills §11）· Technical（skills §1–§8，均有锚点；React 的 employer 锚点 ❓，只放技能行）。

**Selected Achievements**
1. Migration ahead of deadline — PA-01.1 safe wording 改写（"phased coexistence deployment"，加 PA-01 §4 决策 "not a big-bang cutover"，删 "Blue/Green-style" 以减术语）。
2. Multi-discipline leadership — X-02 + S3（"(total headcount)" 保留）+ TPL（engineering, DevOps and data teams）。
3. Payment-gateway integrations — S1 原意逐条：Renren Mall（Alipay, UnionPay）、Baidu Nuomi（Alipay, WeChat Pay, UnionPay）均 "designed and coded"；VV 为 "architected"（O2），"integrating … payments with settlement reconciliation"；无 direct card-scheme 说法；WeChat Pay 不在 Renren 下。
4. Content-management system — PA-18.1 + PA-18.2（"contributed to"，O5）。
5. Multi-tenant SaaS — PA-10.1 + PA-10 §2；业务描述按 S9。
6. Vendor assessment and governance — [LIB] evaluation sessions（📄）+ 02 §5 + X-02（"decision or joint-decision authority"）+ X-05。
7. AI adopted in production — PA-07.1/07.2/07.3 + S9（May 2026、formal architecture and risk approval、"estimated ~80%"）。

**Experience**
- UOB scope：02 §6.1 + X-02（India, Thailand, Indonesia = collaboration，不是直线管理）。
- UOB-1 PA-01.5（加 PA-01 §4 "milestones"；steering 汇报移到 UOB-4）· UOB-2 X-02（TEK 已批准，原句）· UOB-3 PA-04.1（原句）· UOB-4 TEK/TPL 已批准 stakeholder 句（原句）· UOB-5 PA-01.2 + S2（"core banking, which executes settlement"；hub 本身不做 settlement/clearing，CF-N4）· UOB-6 S6 合并措辞 + "in Java" · UOB-7 PA-05.1/05.2/05.3 + S2（daily account summaries → portfolio analysis；现任团队用现在时 "Lead"）· UOB-8 PA-08（"cross-checks"为 schema/data-relationship 校验的通俗说法）+ S9（"contributed to"，RAG 写作 "AI knowledge assistant"）· UOB-9 X-06（"root-cause analysis" 展开 RCA；"support the bank's regulatory reporting to MAS"，不写 "reported to MAS"）· UOB-10 PA-03.1 + PA-03.2 · UOB-11 X-01 + PA-01 §4（designed security controls）+ PA-03.4 + PA-02.1。
- GBD-1 PA-10.3 + S4（Talentvis 已批准，原句）· GBD-2 PA-10 §4 hybrid 决策 + TPL 跨职能 · GBD-3 PA-10 §3 + X-01（Talentvis 已批准，原句）。
- VV scope（TEK 已批准，原句）· VV-1 PA-11.1（平台，不含人数）· VV-2 PA-11.2 + 02 §6.4（Talentvis 原句）· VV-3 PA-12 R22 版本（Talentvis 原句）· VV-4 PA-13（"GMS" 不出现）· VV-5 PA-11.3 + PA-11.5（原句）。
- AIP-1 PA-16.1（Talentvis 原句前半）· AIP-2 PA-16.2 + S7（原句）· AIP-3 02 §6.6 / 03 PA-16 §2 SaaS model + PA-16.3（原句）。
- Earlier：Hengshunyuan PA-15.1/15.2（"~1,500"、"~100k" 保留）· Baidu PA-17.1 · Sohu PA-18.1（TEK 原句）· Renren PA-19（原句）。
- Education：brief §3 四行原文。

## 4. 排除项（及原因）

| 排除 | 原因 |
|---|---|
| CTO / Chief Architect；CEW、SCV-CCD、CCD、GMS、HCL 等内部/供应商名；MEPS+（含 PA-01.7 context 句） | HR-1、01 §7、brief §3 |
| 10M DAU、10M concurrent、5–10M QPS、1,000+ car parks、10+ payment domains、100+ org、GBD 200+ countries | ⛔ / ⚠️ held metrics |
| Flink、GenAI chatbot（PA-14）、delivery-risk forecasting（PA-09）、defect 70–80%、ramp-up 30–40% | ⛔ / ❓ held |
| X-04 "~50 / ~20 modules" | 本批次不用（S5） |
| PA-02.2 "cutting MTTR by X%" | 槽位未填 |
| PA-01.4 latency、PA-11.4 / PA-16.4 millisecond-level、PA-07.4 prompt A/B、PA-06 VN eTax、PA-10.2 KYC rule models | 与本 JD 关联较弱；控制篇幅 |
| PA-03.3 bank-wide standards（"contributed to"） | 为让 UOB-10 保持 2 行而删；可在需要时恢复 |
| [LIB] UOB "developers, QA and business analysts" | 03 未记录；与 "25 engineers" 口径可能冲突 |
| R22 VV "built the organisation from scratch" | 不与 140 人并列（brief/HR-9），避免暗示招聘 |
| Pureland（PA-20）、个人 Android 应用（PA-21）、Crypto（X-03） | ⛔ / ❓ / 无关 |
| Kanban、C++、hiring、mobile app、chatbot、"due diligence"/"outages"/"web portal development" 字面 | 无证据或不能字面支撑；见 Analysis (e) |
| TT / RTGS 缩写 | 对 HR 读者是术语，ISO 20022 已足够说明 |

## 5. 渲染结果与迭代

- **v1：** 3 页，但 Layout OK = False —— 14/31 条为 3 行（上限 1/5）、Comp-1 内容 3 行、Ach-1 4 行。
- **v2：** 用 render.py 的 Measurer 逐条测宽度，把大多数条目压到 ≤ ~1.85 行宽（2 行），只保留需要限定语/日期的 3 行条目 → Layout OK = True，31 条中 5 条 3 行（Baidu 行 1.97 意外折到 3 行）。
- **v3（最终）：** 修 Baidu 行；Ach-1、Ach-7 去掉句中第二个冒号；UOB scope 改写；第 3 页有空间，加回 VV-3（big-data）与 AIP-3（SaaS + AI 识别）；Comp-5 展开 DPIA。
- **最终报告：** Pages **3** · Layout OK **True** · page 1 holds all achievements True · page 2 starts with Experience True · page numbers True · orphan headings none · words 1,341（summary 167）· items 33，3 行 **4**（Ach-1、Ach-3、Ach-7、UOB-11）· line flags none · **lint hits 0** · **red runs 44/95**（headline、summary、6/7 competency 内容、全部 achievements、UOB scope 与 8/11 bullets、GBD-2、VV-1、AIP-3、Hengshunyuan、Baidu 为新/改写措辞；titles、dates、education、其余已批准句为黑色）。
- **视觉检查：** PDF 三页已渲染为 PNG 逐页查看。未在 Microsoft Word 中核对。

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/02_Resume_Fact_Audit.md` (F1, R1–R5, non-blocking notes), `coldread/02_Readability_ColdRead.md`, `brief/Revision_Brief.md` §2. Helper scripts and the pre-revision JSON: `drafts/02/tmp/`.

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Summary P1 | "technical lead on high-traffic consumer platforms at Renren, Sohu and Baidu" | "technical lead on consumer platforms at Renren, Sohu and Baidu" | Revision Brief §1.2 (drop unquantified "high-traffic") |
| Summary P2 | "cross-border payments and retail lending" | "cross-border payments and retail unsecured lending" | R1 safe default |
| Comp · Delivery & Prioritisation | "RAID" | "risk and issue tracking" | Cold-read suggestion 11 (jargon) |
| Ach · Migration ahead of deadline | "phased coexistence deployment, not a big-bang cutover … MX-rich messaging … retiring coexistence" | Canonical ISO 20022 sentence | Cold-read 4.1 / suggestion 1; Revision Brief §2 |
| Ach · Multi-discipline leadership | "earlier led VV's 140-person technology organisation (total headcount) of engineering, DevOps and data teams" | "earlier led VV Technology's 140-person technology organisation through its managers" | R3 safe default (unrecorded make-up removed); canonical VV summary form |
| Ach · Vendor assessment and governance (text) | "Assess vendors' architecture, credentials and fit with existing systems, with …" | "Lead technical evaluation of vendors, with decision or joint-decision authority on vendor selection and SOW/licence negotiation; chair governance of four IT service vendors." | R4 safe default |
| Achievements order | Vendor item 6th | Vendor item 3rd (after Multi-discipline leadership, before Payment-gateway integrations) | Cold-read suggestion 10 (JD responsibilities 1 and 6) |
| UOB · ISO 20022 delivery | "milestones, RAID, release planning" | "milestones, risk and issue tracking, release planning" | Cold-read suggestion 11 |
| UOB · MVP sequencing | "When the two platform lines' schedules conflict, agree MVP scope …" | Canonical MVP sentence | Cold-read 4.2 / suggestion 2 (no subject); Revision Brief §2 |
| UOB · hub design | "… integrating reference data, third-party banking systems and core banking, which executes settlement." | "… integrates reference data and third-party banking systems, and hands payments to core banking for settlement." | Cold-read 4.3 / suggestion 3 (ambiguous "which"); canonical S2 hand-off phrase (result processing stays in the next bullet) |
| UOB · delivery KPIs | "MTTR … SIT/UAT sign-off" | "mean time to recovery … system and user-acceptance test sign-off" | Cold-read 4.5 / suggestion 4 (acronyms written out; kept at 3 lines) |
| UOB · security controls | "… credential management and role-based permissions — … personally led disaster-recovery and failover drills, sustaining 99.9%+ availability." | "… API and database encryption and credential management — … personally led disaster recovery (DR) and failover drills for the real-time payment middleware, sustaining 99.9%+ availability." | Same claim failed in audit 01 (F1): role-based permissions are outside X-01; 99.9%+ belongs to the real-time payment middleware (PA-02.1). Applied for accuracy and batch consistency |
| GBD · team | "Led a 40-person project team (total headcount), …" | "Led a 40-person project team, including outsourced staff, …" | Canonical GBD sentence; cold-read suggestion 8 |
| GBD · AWS | "(API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch)" | "(API Gateway, EC2/ECS, RDS, DynamoDB)" | Audit note #40 (≤ 4 technologies) |
| VV · big data | "Led the big-data team on Flume, Hive, MapReduce, Spark Streaming and Spark SQL, providing data analysis that supported business decisions." | "Led the big-data team and built VV's data-analysis platform from scratch on Flume, Hive, MapReduce and Spark." | R5 safe default (03 PA-12 safe wording; Spark Streaming/SQL folded into "Spark", ≤ 4 technologies; cold-read 6) |
| VV · B2B product | "middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS)" | "shared back-end platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ)" | Cold-read 4.4 / suggestion 5; canonical VV B2B sentence |

**Not changed:** Education certificate line and heading (F1 overruled — verified 02 §3 document); "JavaScript (React)" in the Technical row (R2 — confirmed skill; left for Wilson); "estimated ~80%".

**Rendered result (after revision):** 3 pages · Layout OK **True** · bullets 33, at 3 lines **5** (Ach ISO 20022, Ach Payment-gateway integrations, Ach AI adopted in production, UOB delivery KPIs, UOB security controls) · words 1,358 (summary 167) · line flags none · lint hits 0 · pages rasterised and viewed (`drafts/02/tmp/pg-*.png`).

**For Wilson:** (1) React: which employer and period (R2)? Do SQL and RHEL apply to UOB? (2) Which functions made up VV's 140 (R3)? (3) Are "architecture, credentials and fit with existing systems" your actual vendor-evaluation criteria (R4)? (4) What did VV's data analysis support (R5)? (5) Is the 99% SonarQube gate on new code or all code?


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K2 steering committee (singular) | senior management and steering committees | senior management and the steering committee | C3 answer K2 (2026-10-26) |
| K5 SonarQube scope | 99% SonarQube coverage gate | 99% SonarQube coverage gate on all code | C3 answer K5 (2026-10-26) |
