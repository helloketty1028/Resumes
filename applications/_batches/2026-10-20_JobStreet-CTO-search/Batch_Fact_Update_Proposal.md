# Batch Fact Update Proposal — 2026-10-20 JobStreet CTO search（滚动草稿，2026-10-26 更新：新增 B-11 至 B-22；B-12、B-15、B-16、B-17、B-22 已在 C3 答复）

> **回灌候选** = 本批求职中你新确认、可写回事实库 `master\v2.0-draft\` 供以后复用的事实。
> 本文件只是候选清单：阶段六统一整理去重，在审批门 C4 由你逐条选 **Y 入库 / E 改后入库 / Q 只登记待确认 / L 仅限本次 / N 不入库**。**未选中的一律 N。** 只有 Y / E / Q 交给工具 B；工具 C 不写事实库。

| 临时 ID | 类型 | 关联现有 ID | 现有表述 | 建议表述 | 来源 | 建议图标 | 目标文件 §章节 | 风险标记 | 建议 | 我的决定 |
|---|---|---|---|---|---|---|---|---|---|---|
| B-01 | ADD | PA-19 Renren, PA-17 Baidu | 无支付接入记录 | 作为技术专家亲自设计并编码支付接入：Renren Mall — Alipay、银联；百度糯米 — Alipay、微信支付、银联（O1 + O2） | [CONF 2026-10-21] | ✅ 分配已确认 | 03 PA-19, PA-17 | 时间线已核对（Renren 不含微信支付） | Y | 默认 N |
| B-02 | ADD | PA-11.2 | "payment subsystem's transaction, management and reconciliation modules" | 作为技术负责人兼架构师（O2），支付子系统接入银联、Visa/Mastercard、Google Pay、GrabPay，并负责结算对账；措辞为经收单 / 网关接入。另：技术团队做过卡组织直连，你本人未直接做（O4）；接入形式与卡组织待补 | [CONF 2026-10-20 / 10-21] | ✅（直连部分 ❓） | 03 PA-11 | — | Y（直连部分 Q） | 默认 N |
| B-03 | CLARIFY | PA-01 §2, PA-05, 02 §8 CF-N4 | hub 不做清结算 | CBPR+ 与 C360 均与核心银行系统集成：结算由核心系统执行，你的系统发送并接收结果；C360 使用核心系统的每日账户汇总并支持组合分析 | [CONF 2026-10-20] | ✅ | 03 PA-01, PA-05；02 §8 | — | Y | 默认 N |
| B-04 | CLARIFY | OQ-2.3（GBD 部分）, PA-10.3, §0A | {40-person — OQ-2.3} | 40 人项目团队为总人数，含外包人员；措辞 "Led a 40-person project team (total headcount)" | [CONF 2026-10-20] | ✅ | 03 PA-10.3, §0A；fact-check OQ-2.3 | ⚠ 背调敏感（团队规模） | Y | 默认 N |
| B-05 | CLARIFY | OQ-2.3（VV 部分）, PA-11.1, §0A, HR-3 | {of 140 — OQ-2.3}，§0A 为 ❓ | 140 人均在你负责的技术中心之下，由下级经理分层管理；你直接对接 15–20 人 → "Led VV's 140-person technology organisation (total headcount)"（与两份终稿一致） | [CONF 2026-10-21] | ✅ | 03 PA-11.1, §0A；fact-check OQ-2.3、HR-3 | ⚠ 背调敏感（团队规模） | Y | 默认 N |
| B-06 | CLARIFY | X-04, §0A "~50 modules / ~20 core" | "review code daily across ~50 modules (deep review of ~20 core modules)" | 新增安全措辞 "review newly submitted core PRs daily"；本批不用 50 / 20，但不退役（未说其不实） | [CONF 2026-10-21] | ✅ | 03 X-04 | 与 Talentvis 终稿为口径收窄，不矛盾 | Y | 默认 N |
| B-07 | CORRECT | 05 §9, OQ-J1, D-07 | "S$12k+、无合同岗、排除银行、偏好 fintech / 政府"（早期记录） | 月薪底线看总包可谈；不接受非受薪安排（合伙 / 分成类）；从不排除银行。合同岗是否接受：未答复 | [CONF 2026-10-20] | ✅ | 05 §9；fact-check OQ-J1, D-07 | — | Y | 默认 N |
| B-08 | RESTRICT | PA-16.2, X-02 | — | 乙方售前经验仅 AI Park（投标、写标书）；无其他乙方售前、报价或合同谈判经验 | [CONF 2026-10-20] | ✅ | 03 PA-16；05 §7 | — | Y | 默认 N |
| B-09 | CLARIFY（关闭 C7 b） | PA-01.3, 03 §5.2, v1.0 U1 | [LIB] "concurrency-control modules" 不在你的亲自编码清单中 → ❓ keep or drop | 保留并作为技术优势写入，用 [LIB] 原句："personally authoring core transaction-processing and concurrency-control modules" | [CONF 2026-10-21] | ✅（具体机制 ❓） | 03 PA-01.3, §5.2 | 面试必问具体机制 | Y | 默认 N |
| B-10 | RESTRICT（保留不退役） | OQ-2.3 第三项, HR-4, HR-5, 03 §0A, §5.2 | VV "10M concurrent HTTP requests"、Baidu "5–10 million QPS"：⛔ / ❓，曾提议退役 | 保留在事实库，不退役；口径（生产峰值 / 每日总量 / 压测或设计目标）确认前不用于简历 | [CONF 2026-10-21] | ❓（维持） | 03 §0A, §5.2；fact-check HR-4 / HR-5 | ⚠ 面试高风险 | Q | 默认 N |
| B-11 | Q | 技能清单 React | 有 React 前端开发经验（雇主 / 时期未记录） | 补雇主、时期、深度 | 02 草稿审计 | ❓ | skills inventory | — | Q | 默认 N |
| B-12 | CLARIFY | PA-03 / §0A 99% SonarQube | “99% SonarQube coverage gate” | 门禁针对**全部代码**（all code），不只是新代码 | [CONF 2026-10-26] C3 K5 | ✅ | 03 §0A, PA-03 | 面试可能追问 | Y | 默认 N |
| B-13 | Q | 技能清单 Spring Cloud / Kafka | A/P ❓ | 补当前 hands-on 深度（亲手写还是选型 + 指导） | 03、04 审计 | ❓ | skills inventory | — | Q | 默认 N |
| B-14 | Q | PA-01 API | hub API 设计 | 补：hub 的 API 契约是否 REST；核心系统接口是新建还是复用 | 01 审计 | ❓ | 03 PA-01 | — | Q | 默认 N |
| B-15 | CLARIFY | PA-01.5 | 向 steering committee 汇报（CBPR+ 项目） | 只有**一个** steering committee（单数）。是否也汇报风险 / 决策、交付 KPI 是否上报：仍未答 | [CONF 2026-10-26] C3 K2 | ✅（后半 ❓） | 03 PA-01.5 | — | Y（后半 Q） | 默认 N |
| B-16 | ADD | 02 §1 / Talentvis 终稿 | “start-ups and scale-ups”（无依据） | VV Technology 与 Golden Bridge 可称 **scale-ups**，“start-ups and scale-ups” 可用 | [CONF 2026-10-26] C3 K1 | ✅ | 02 §1 | — | Y | 默认 N |
| B-17 | CLARIFY | PA-11.1 | “built its microservices platform from scratch” | 微服务**框架代码由你亲手编写**（O1），“built” 成立 | [CONF 2026-10-26] C3 K4 | ✅ | 03 PA-11.1 | 面试会追问框架设计细节 | Y | 默认 N |
| B-18 | Q | PA-07 / C4 | AI code-review 服务、eMemo agent | 补：code-review 是否你发起；25 人是否都在用；eMemo agent 是否投产、是否经正式审批；RAG 助手审批情况 | 08、10 审计 | ❓ | 03 PA-07 | — | Q | 默认 N |
| B-19 | Q | PA-01 ISO 20022 | MT-to-MX 迁移 | 补：MT↔MX 报文转换是否由你或 hub 团队实现 | 05 审计 | ❓ | 03 PA-01 | — | Q | 默认 N |
| B-20 | Q | X-03 | 交付治理 | 补：在 UOB 是否亲自与 PO 做 backlog 优先级排序和 sprint 规划 | 06 审计 | ❓ | 03 X-03 | — | Q | 默认 N |
| B-21 | Q | PA-16 AI Park | SaaS 模式面向 B2B / B2G | 补：2017-09 前是否有真实付费客户；是否算 0-to-1 建设 | 08、09 审计 | ❓ | 03 PA-16；02 §6.6 | — | Q | 默认 N |
| B-22 | ADD | PA-01.5 / X-02 | 向高管和 steering committee 汇报 | 也向**业务团队（business team）**汇报状态、风险和决策；“explains technical choices in business terms” 无依据，不再使用 | [CONF 2026-10-26] C3 K3 | ✅ | 03 PA-01.5, X-02 | — | Y | 默认 N |

相关但不在本批重复登记：TEKsystems 提案 TU-13（VV / AI Park 职位英文名）尚未入库（2026-10-21 你再次确认这两个名称），见 `applications\2026-10-17_TEKsystems_Program-Manager\Fact_Update_Proposal.md`。
