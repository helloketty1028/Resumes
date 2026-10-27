# Resume Change Log — NETS · Principal Engineer (01)

- **输出：** `drafts/01/resume.json` → `drafts/01/out/wilson-2026_ATL_Bank_NETS_V1_0_0_draft.docx` / `.pdf` / `.txt` / `.report.md` / `.report.json`
- **Family × lens：** ATL × BNK · file_stem `wilson-2026_ATL_Bank_NETS_V1_0_0` · 定位卡 `cards/01.md`
- **Base：** 已批准 `base_Talentvis_SM_Internet.json`（UOB 架构块、GBD、VV、AI Park、Earlier）+ `base_TEKsystems_TPM_Internet.json`（GBD scope/要点、VV 组织、MVP、lending、Earlier Hengshunyuan）+ `LIB_wilson-2026_Archi_Bank_LIB_V5_0_0.txt`（ATL × BNK 单元，headline 选项 3、Principal Engineer 裁剪指引）。事实以 03 safe wording 与 Brief §4 S1–S9 为准（优先级：S1–S9 > 03/02 > 已批准原句 > [LIB]）。
- **标记约定：** 「原句」= 与已批准简历逐字一致（渲染为黑字）；「改写」= 基于已批准原句或 03 safe wording 的删改（红字）；「新」= 来自 03/S1–S9 的新组合措辞（红字）。

---

## 1. 定位

- **Headline（卡片原文，1 行）：** "Principal Engineer — Payment & Transaction-Processing Platforms | Hands-On Java Architecture · Resilience by Design"。目标职位名照抄 JD；无 "CTO"；"Resilience by Design" 来自 02 §7.2 ATL × BNK 选项 3（📄）。
- **第 1 页回答三问：** 他是谁（Sum-P1：支付平台的 hands-on 技术负责人，18+ 年 Java 与方案架构）· 规模（Sum-P2：Tier-1 银行 VP、25 名工程师、四家 IT 服务供应商、数百万账户）· 为何匹配（Ach-1 至 Ach-7：hub 设计、亲手核心编码含并发控制、不停机迁移、低延迟、韧性与安全、卡与钱包支付集成、工程治理）。
- **按 LIB Principal Engineer 指引：** 性能与"设计 + 亲手构建"置顶，管理类内容后移到 UOB 后半段；Summary 不写 140 人组织。

## 2. 逐项内容决定（含来源 ID）

### Summary（3 段，全部「新」）
| 位置 | 要点 | 来源 | 说明 |
|---|---|---|---|
| Sum-P1 | 支付平台 hands-on 技术负责人；18+ 年 Java 与方案架构；Tier-1 banking、fintech and SaaS products、consumer e-commerce；覆盖交易系统全生命周期 | 02 §1、§4（🔶 定位）；TEK 已批准用语 "fintech and SaaS products"；PA-01.2、S6、S5、PA-01.1、PA-02.1 | 首句对准 JD 核心（技术权威 + 动手） |
| Sum-P2 | 2022 起 UOB VP；25 名在岸/离岸工程师；主持四家 IT 服务供应商治理；数百万账户；拥有 payment-initiation hub 架构并主导其迁移到 ISO 20022 | X-02、X-05、S5、PA-01.1/01.5 | 加入 X-05 以让 JD #3 的 "vendors" 在第 1 页可见；99.9%+ 与 "no service interruption" 不在此重复（在 Ach-3/Ach-5） |
| Sum-P3 | Renren / Sohu / Baidu 起步（已批准片段）；2016–2022 head-of-technology 与架构师角色，从零交付微服务平台、支付子系统、多租户 SaaS；向高管与指导委员会用业务语言解释技术选择（已批准片段） | Talentvis 已批准 Summary 片段；PA-11.1、PA-11.2、PA-10.1；PA-01.5 | 不重复 S1 支付商清单（只在 Ach-6） |

### Core Competencies（7 行，按 JD Required 顺序；全部「新」）
| 行 | 关键内容 | 来源 / 锚点 |
|---|---|---|
| Comp-1 Payment Systems | initiation/validation/enrichment/status tracking；settlement integration with core banking；reconciliation；ISO 20022、SWIFT；card and e-wallet payment integration | PA-01.2、S2、S1、skills inv. §9 |
| Comp-2 Architecture & Integration | Java、Spring Boot、Apache Camel (enterprise integration patterns)、RESTful API design、event-driven、microservices、distributed systems、multi-tenant SaaS | skills inv. §1、§2、§7；REST = [LIB] 📄（OQ-1） |
| Comp-3 Performance & Resilience | low-latency transaction processing、concurrency control、thread-pool/JVM tuning、high availability、disaster recovery (DR) and failover drills、capacity baselines | PA-01.4、S6、PA-02.1 |
| Comp-4 Security & Risk | API/DB encryption、credential management、role-based access control、secure SDLC、DPIA、data governance、MAS TRM (Singapore technology-risk rules) | X-01、PA-01.3、PA-03.4、S9（TRM 解释） |
| Comp-5 Engineering Delivery | DevSecOps practice: CI/CD on Bitbucket and Jenkins、SonarQube gates、automated regression and penetration testing；Splunk observability；SIT/UAT sign-off | PA-03.1/03.2、PA-02.2 |
| Comp-6 Platforms & Middleware | Linux (RHEL)；MySQL、SQL、Redis；Kafka、RocketMQ and AWS SQS/SNS messaging；Docker、Kubernetes；AWS | CF-N6、skills inv. §3–§5（Solace 缺口的诚实桥接） |
| Comp-7 Technical Leadership | design and code reviews、quality gates、engineering standards (contributed bank-wide)、mentoring、1:1s and performance management、steering-committee reporting | S5、PA-03.3（锁定动词）、X-02 |

### Selected Achievements（7 条）
| # | Label（全部「新」） | 正文 | 来源 | 基础 |
|---|---|---|---|---|
| Ach-1 | Payment-hub design | Led end-to-end design of a payment-initiation hub … integrating digital and branch channels, reference data, and vendor and third-party banking systems. | PA-01.2 | 改写：Talentvis 已批准句删去 "on Java, Spring Boot and Apache Camel"（保持 2 行；技术栈在 Comp-2） |
| Ach-2 | Hands-on core engineering | Personally built the hub's core modules — payment-transaction initiation, concurrency control, … | S6（PA-01.3） | 新：S6 合并原句逐字 |
| Ach-3 | Zero-interruption modernisation | Planned and architected a phased, Blue/Green-style coexistence … with no service interruption. | PA-01.1 | 改写：03 safe wording，"(MT-to-MX)" → "(SWIFT MT-to-MX)"，删 "(TT, RTGS)"（避免未解释缩写）；日期全部保留以证明早于 SWIFT 截止（4 个日期超出"每条 1–2 个数字"的建议，理由：已批准原句、可信度依赖日期） |
| Ach-4 | Performance engineering | Reduced end-to-end transaction latency under high load … ; earlier brought VV's services to millisecond-level response times. | PA-01.4 + PA-11.4 | 改写：已批准句 + VV 子句（卡片"如放得下"选项）；VV 经历中原 PA-11.4 要点因此删除，避免同一事实出现两次 |
| Ach-5 | Resilience and security | Designed security controls … sustaining 99.9%+ availability under peak load. | X-01、PA-02.1、PA-03.4 | **原句**（Talentvis "Enterprise-grade trust" 正文逐字；仅换 label） |
| Ach-6 | Payment integrations across markets | Designed and coded Renren Mall's payment integration (Alipay, UnionPay) and Baidu Nuomi's payment-gateway integration (Alipay, WeChat Pay, UnionPay); architected VV-Life's payment subsystem, integrating UnionPay, Visa/Mastercard, Google Pay and GrabPay payments with settlement reconciliation. | S1 | 新：WeChat Pay 只在 Baidu 下；"integrating … payments"；VV 用 O2 动词 "architected" |
| Ach-7 | Engineering governance | Established delivery KPIs and CI/CD quality gates — 99% SonarQube coverage, automated regression and penetration testing, SIT/UAT sign-off for every release — and contributed to bank-wide SDLC and code-review standards. | PA-03.1/03.2/03.3 | 改写：Talentvis 已批准 UOB 句压缩（删去 KPI 明细与 "coding"）以保持 2 行；"contributed to" 锁定 |

### Professional Experience
| 位置 | 内容（简） | 来源 | 基础 / 说明 |
|---|---|---|---|
| UOB-scope | Two mission-critical platform lines: cross-border payments on SWIFT ISO 20022 and retail unsecured lending and collections. | 02 §6.1 | 新：缩为 1 行，不重复 Summary 的 "millions of accounts / MAS-regulated" |
| 小标题 | "Architecture & Hands-On Engineering"（原句）/ "Delivery, Production & Leadership"（新） | 卡片 | 卡片的三组合并为两组（Reliability 只剩 2 条，并入第二组） |
| UOB-1 | Stay hands-on alongside delivery: review newly submitted core pull requests daily … | S5（X-04） | 新：S5 本批次原句逐字；未用 "~50/~20 modules" |
| UOB-2 | Lead the 10-engineer backend team of a regional customer-360 platform live since 2022 … | PA-05.1/05.2/05.3 | 改写：Talentvis 句改现在时、压到 2 行；不声称主导 2022 上线（C5 未决） |
| UOB-3 | Integrated both platforms with core banking … for core banking to settle … daily account summaries for portfolio analysis. | S2、CF-N4 | 新：明确 hub 不清算/结算；"integrated with core banking" 措辞 |
| UOB-4 | Designed and built a production AI code-review service … estimated ~80%; the AI never approves or merges. | PA-07.1/07.2/07.3、S9 | 改写：Talentvis 成就句压到 3 行（卡片：作为工程效能工具放经历） |
| UOB-5 | Led a 15-engineer onshore/offshore team and owned end-to-end delivery of the ISO 20022 programme … every 2–3 months after go-live. | PA-01.5 | 改写：03 safe wording 删去汇报子句（汇报在 Sum-P3） |
| UOB-6 | Coordinate P1–P3 production incidents end to end … technical incident analyses that support the bank's regulatory reporting to MAS. | X-06 | 新：恢复 X-06 的 MAS 报告"输入"措辞（NETS 同受 MAS 监管）；不写 "reported to MAS" |
| UOB-7 | With no separate SRE function, own production support … Splunk-based monitoring and alerting, and capacity baselines. | PA-02.3、CF-N3 | 新：03 safe wording 逐字（从原 Talentvis 事件句拆出） |
| UOB-8 | When the two platform lines' schedules conflict, agree MVP scope … | X-02 | **原句**（TEK） |
| UOB-9 | Own technology for retail unsecured-lending servicing … | PA-04.1 | **原句**（TEK） |
| UOB-10 | Lead both platform teams through squad leads and engineering managers — 1:1s, mentoring and performance management — and work closely with teams in India, Thailand and Indonesia across time zones. | X-02 | 新：由已批准片段组合；mentoring 的唯一位置 |
| UOB-11 | Hold decision or joint-decision authority on technology investment, vendor selection and SOW/licence negotiation, and run vendors' periodic budget reviews, year-end performance reviews and accountability meetings. | X-02、X-05 | 新：供应商数量在 Sum-P2，这里给治理细节，不重复 |
| GBD-scope | Multi-tenant SaaS for online-game businesses, built 0-to-1 on AWS — KYC, bonus incentives, VIP tiers and multi-channel payments. | PA-10.1、S9 | 改写：TEK scope 删 "analytics" 缩为 1 行（让 AI Park 整段留在第 2 页）；不展开业务性质（S9） |
| GBD-1/2/3 | 40-person (total headcount)；Spring Cloud + Kubernetes + API gateway + KYC；AWS deployment + DPIA + encryption | PA-10.3/S4、PA-10.1/10.2、X-01 | **原句**（TEK ×2、Talentvis ×1） |
| VV-scope | VV-Life: a local-life services platform connecting offline merchants — food, fresh produce, travel and everyday services. | PA-11 | **原句**（TEK；1 行，去掉 Talentvis 版的 "through data" 孤字行） |
| VV-1/2/4 | 140-person (total headcount)；first VV-Life release in 2019 incl. payment subsystem；CI/CD + incident priority plans | S3/PA-11.1、PA-11.2、PA-11.3/11.5 | **原句** |
| VV-3 | Designed the middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS) … | PA-13 | **原句**（Talentvis；不写 "GMS"）—— 替代被并入 Ach-4 的 PA-11.4；补充架构治理与消息中间件证据 |
| AIP-1/2 | IoT 平台技术负责；Spring Cloud + Kafka + 缓存 → 毫秒级 | PA-16.1/S8、PA-16.4 | **原句**（TEK 短版、Talentvis） |
| Earl-H | Hengshunyuan — Co-founder (Oct 2017 – Sep 2019, China): Owned product, architecture and delivery of an audio-learning platform, reaching a peak of ~100k daily active users. | PA-15.1 | 改写：TEK 句删去 ~1,500 授权内容（与 JD 无关，保持 2 行） |
| Earl-B | As project leader, re-architected the merchant-side order system on Dubbo microservices and delivered two months ahead of plan. | PA-17.1 | 改写：删 "leading the web front-end, CMS development and QA teams"（保持 2 行） |
| Earl-S | Led the re-architecture of the fifth-generation CMS (SSH to Spring MVC; memcached cluster to Redis cluster). | PA-18.1 | 改写：删 "and delivered its OpenAPI messaging platform"（保持 2 行） |
| Earl-R | Developed Renren's shopping website, Renren Mall and CRM on Spring, Solr, Redis, MySQL and Nginx. | PA-19 | 新：03 safe wording 逐字（补 MySQL 证据，消除孤字行） |
| Education | 4 行 | Brief §3 | **原句**逐字 |

## 3. 与定位卡的偏离（及理由）

1. **S1 支付商清单只出现在 Ach-6**，不再放进 Summary P3 和 Earlier（Baidu/Renren）行 —— Brief §6 "merge, don't stack"（同一事实只出现一次）。Earlier 两行保留 PA-17.1/PA-19 的其他事实。
2. **Ach-7 不含 mentoring**；mentoring 放 UOB-10（带 1:1s 与绩效管理）—— 避免重复，并让 Ach-7 保持 2 行。
3. **S2 核心银行对接放 UOB-3**，不并入 Ach-1 —— Ach-1 保持 2 行，且避免与 Ach-2 的"处理下游返回的支付状态结果"重叠。
4. **Summary P2 不写 DR/99.9%+ 与 "no service interruption"**（在 Ach-3/Ach-5），改加四家 IT 服务供应商（X-05），让 JD #3 的 "vendors" 在第 1 页有证据。
5. **Comp-6 改名 "Platforms & Middleware"**，加入 RocketMQ、AWS SQS/SNS（skills inventory 有锚点）作为 Solace JMS 缺口的诚实桥接；Comp-1 去掉 RTGS（非 JD 用语、避免未解释缩写）。
6. **VV：PA-11.4 并入 Ach-4**，VV 经历改用 PA-13 中台架构要点；**X-06 与 PA-02.3 拆为两条**以恢复 MAS 报告输入措辞（UOB 共 11 条，在 9–11 预算内）。
7. **UOB 三组小标题合并为两组**（Reliability 组只剩两条）。
8. **Hengshunyuan 以 Earlier 一行呈现**（与卡片一致）。

## 4. 排除项（及理由）

| 排除内容 | 理由 |
|---|---|
| PA-08 eMemo AI 校验 agent | 与 NETS JD 关联弱；篇幅给 JD 必需项 |
| S9 RAG 知识助手（O5） | 与 JD 无关 |
| PA-06 VN eTax | 03 记为 📄 thin（日期、规模、结果未定） |
| PA-12 VV 大数据平台、PA-16.3 AI 识别 | 与 JD 无关 |
| PA-16.2 城市投标与试点 | 与 JD 无关（S7：投标只限 AI Park，非本岗位重点） |
| PA-15.2 ~1,500 授权音频 | 与 JD 无关 |
| PA-01.7 hub 背景句 | 含 MEPS+（Brief §3 禁用），且与 Ach-1 重叠 |
| X-04 "~50 / ~20 core modules" | Brief S5：本批次不用 |
| PA-07.5 ramp-up 30–40%、PA-07.6 defects | C1/C3 未决，Brief 禁用 |
| PA-09、PA-14、PA-20 Pureland、10M DAU、10M concurrent、5–10M QPS、1,000+ lots、GBD 200+、"10+ payment domains" | ⛔ / ⚠️ 或 Brief §3 禁用 |
| "high-throughput" 字样 | 无数字；03 用 "under high load"，UOB 交易量保密 |
| "design authority" 字样 | 正式设计权威角色无记录（PA-03.3 = contributed）→ OQ-5 |
| Solace、PCI-DSS、tokenisation、POS、QR、交换、卡组织直连、PostgreSQL、IaC、mobile/SDK | 无证据或仅工作知识 → 缺口，见分析 (e) |
| 美国团队协作 | D-09 |
| "Prior CTO"、Chief Architect | HR-1 |

## 5. 渲染结果与迭代

| 轮次 | 改动 | 结果 |
|---|---|---|
| v1 | 首稿 | Layout OK True；3 页；但发现：VV 毫秒级事实在 Ach-4 与 VV 要点重复；VV scope、Renren 行出现孤字行；UOB scope 2 行；AI Park 跨第 2/3 页 |
| v2 | VV PA-11.4 → PA-13；X-06/PA-02.3 拆分；Comp-6 加消息中间件；Renren 用 03 safe wording；VV scope 用 TEK 1 行版；UOB-3 写明 "payment-initiation hub" | Layout OK True；AI Park 仍跨页 |
| v3（终稿） | UOB scope、GBD scope 各缩为 1 行 | Layout OK True；AI Park 整段在第 2 页 |

**终稿报告（`out/wilson-2026_ATL_Bank_NETS_V1_0_0_draft.report.md`）：**
- Pages **3**（第 3 页约 1/3：Earlier Experience + Education）· 第 1 页含全部 7 条 Achievements ✅ · 第 2 页以 PROFESSIONAL EXPERIENCE 开头 ✅ · 页码 "Page X of 3" ✅ · 孤立标题：无 · **Layout OK: True**
- Words 1,269（Summary 164）· 要点 31 条，3 行 **4** 条（Ach-3、Ach-5、Ach-6、UOB-4）· line flags：无
- Red runs **47/93**（新措辞，草稿预期）· **Lint hits: 0**
- 目视检查：三页 PDF 光栅化后逐页检查（LibreOffice + Carlito）。未在 Microsoft Word（Calibri）中实机检查；未做 ATS 解析测试。

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/01_Resume_Fact_Audit.md` (F1, R1–R6), `coldread/01_Readability_ColdRead.md`, `brief/Revision_Brief.md` §2 canonical sentences. Helper scripts and the pre-revision JSON: `drafts/01/tmp/` (`resume.before.json`, `edits*.py`).

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Headline | "… Hands-On Java Architecture · Resilience by Design" | "… Hands-On Java Architecture & Resilience" | Cold-read §4/§5: tagline unclear |
| Summary P1, sentence 1 | "18+ years of Java engineering and solution architecture across …" | "18+ years across Tier-1 banking, fintech and SaaS products, and consumer e-commerce, combining Java engineering with solution architecture" | R1 safe default (career-total number no longer attached to architecture) |
| Comp · Payment Systems | "settlement integration with core banking" | "hand-off to core banking for settlement" | R2 safe default; canonical S2 phrase |
| Comp · Architecture & Integration | "RESTful API design" | "API design" | R3 safe default (REST not anchored) |
| Comp · Security & Risk | "DPIA" | "data protection impact assessments (DPIA)" | Audit §3 acronym note |
| Achievements order | Payment-hub design first, hands-on second | "Hands-on core engineering" first; "Payment-hub design" second, now "Led end-to-end design of the hub …" | Cold-read suggestion 4 (Principal Engineer headline); hub defined in Summary P2 |
| Ach · Zero-interruption modernisation | "phased, Blue/Green-style coexistence deployment … MX-rich messaging … retired coexistence" | Canonical ISO 20022 sentence ("running old and new message formats side by side … old path was retired in August 2026 …") | Cold-read 4.1 / suggestion 1; Revision Brief §2 |
| Ach · Resilience and security | "… credential management and role-based permissions — for payment, lending and customer-data platforms …; personally led DR and failover drills, sustaining 99.9%+ …" | Auditor's replacement: role-based permissions removed; "DR and failover drills for the real-time payment middleware, sustaining 99.9%+ …" | **F1** |
| UOB · customer-360 | "evaluated Cloudera as its processing framework" | "evaluated Cloudera as its big-data processing framework" | Cold-read 4.3 / suggestion 2 (no new fact; "chose" not used) |
| UOB · core banking | "Integrated both platforms with core banking: … for core banking to settle …" | "The payment-initiation hub hands validated payments to core banking, which executes settlement, and processes the results returned; the customer-360 platform takes daily account summaries from core banking for portfolio analysis." | R5 safe default + canonical S2 (no ownership verb; no "both platforms" ambiguity) |
| UOB · ISO 20022 delivery | "scope, roadmap, RAID, …" | "scope, roadmap, risk and issue tracking, …" | Audit §3 acronym note (RAID) |
| UOB · P1–P3 incidents | "RCA" | "root-cause analysis (RCA)" | Revision Brief §1.3 acronym list |
| UOB · production support | "With no separate SRE function, own … SLIs/SLOs, Splunk-based monitoring …" | "Own production support for the payment platforms, with no separate site reliability engineering (SRE) team: SLA tracking, service-level indicators/objectives (SLIs/SLOs), Splunk monitoring …" | Cold-read 4.2 / suggestion 2; acronyms expanded (SLIs/SLOs kept — JD observability) |
| UOB · MVP sequencing | "When the two platform lines' schedules conflict, agree MVP scope …" | Canonical MVP sentence ("Resolve schedule conflicts … by agreeing MVP scope …") | Revision Brief §2 (subject/verb order) |
| UOB · commercial authority | "SOW/licence negotiation" | "statement-of-work (SOW) and licence negotiation" | Acronym expansion; vendor-authority wording unchanged |
| GBD · team | "Led a 40-person project team (total headcount), …" | "Led a 40-person project team, including outsourced staff, …" | Canonical GBD sentence (readable qualifier, S4) |
| GBD · AWS | "(API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch)" | "(API Gateway, EC2/ECS, RDS, DynamoDB)" | Audit §3: ≤ 4 named technologies |
| VV · organisation | "140-person technology organisation (total headcount)" | "140-person technology organisation through its managers" | Canonical VV sentence (readable qualifier, S3) |
| VV · B2B product | "middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS)" | "shared back-end platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ)" | Canonical VV B2B sentence (jargon; ≤ 4 technologies) |
| Earlier · Sohu | "(SSH to Spring MVC; memcached cluster to Redis cluster)" | "Led the re-architecture of the fifth-generation CMS onto Spring MVC and a Redis cluster, and delivered its OpenAPI messaging platform." | Cold-read 4.4 ("SSH" misread); canonical Sohu sentence (PA-18.1); "Sohu's" dropped because the line's lead already names Sohu (keeps it at 2 lines) |

**Not changed:** Education certificate line (R6 overruled — verified 02 §3 document); "Technical Leadership" competency row (kept as the page-1 evidence for the JD's mentoring / standards requirements); "estimated ~80%"; 140 / 40 qualifiers kept in readable form.

**Rendered result (after revision):** 3 pages · Layout OK **True** · bullets 31, at 3 lines **4** (Ach ISO 20022, Ach Resilience and security, Ach Payment integrations, UOB AI code review) · words 1,304 (summary 164) · line flags none · lint hits 0 · all three pages rasterised and viewed (`drafts/01/tmp/pg-*.png`).

**For Wilson:** (1) Were the hub's API contracts REST? If yes, "RESTful API design" can return (JD keyword). (2) Did your teams design/build the core-banking interfaces, or consume existing ones? If built, "Integrated … with core banking" can return. (3) Is the 99% SonarQube gate on new code or overall coverage (PA-03 §8)?


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K3 business team | Used to explaining technical choices in business terms to senior management and steering c | Reports status, risks and decisions to senior management, the steering committee and the business team. | C3 answer K3 (2026-10-26) |
| K5 SonarQube scope | 99% SonarQube coverage, | 99% SonarQube coverage on all code, | C3 answer K5 (2026-10-26) |
| PA-03.5 CRQ/CAB | — | Personally prepare the change request for every production release on both platform lines and present the go-l | C3: add PA-03.5 (03 v4.2, CONF 2026-10-26) — approved by Wilson |
| PA-03.5 competency | Splunk observability; SIT/UAT release sign-off | Splunk observability; SIT/UAT and Change Advisory Board (CAB) release approval | C3: add PA-03.5 (03 v4.2, CONF 2026-10-26) — approved by Wilson |

**Independent C3 edit review (2026-10-26) — fixes applied:**

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| C3 review fix #1 | Reports status, risks and decisions to senior management, the steering committee and the b | At UOB, reports status, risks and decisions to senior management, the steering committee and the business team | Independent C3 review: sentence closes a pre-UOB paragraph |
