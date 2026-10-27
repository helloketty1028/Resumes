# Fact Library Update Review — Interview Bank 回灌（已确认条目）

**日期**：2026-10-26 · **场景**：申请后回灌（Interview Bank → 事实库） · **状态**：✅ 已按你的决定应用（2026-10-26）— 见 `Fact_Library_Change_Log.md`
**材料**：① `Interview Bank\inbox\2026-10-25_old-qa\Fact_Update_Proposal.md`（子批 A/B/C/D + N）② `Interview Bank\prep\_story-build\Fact_Update_Proposal.md`（IB-01 – IB-16）
**实际读取的事实库**：01 v1.1 · 02 v3.1 · 03 v4.2 · fact-check v2.5 · skills inventory v2.3 · 05 v1.0（仅 §6 第 212 行）· `applications\` 下 12 份已投递简历（docx 文本）与审计文件
**本轮范围（你指定）**：SB-04、SB-05、SB-12、SA-01、SA-03、SI-01、SI-02、SI-03、SD-01、SD-02、SD-05、SD-20。其余 ❓ → §B 待问；冲突 → §A13 登记 fact-check。
**已在 03 v4.2 的**：SB-01（= PA-03.5，D-15）——不重复。

---

## 差异识别（本轮 12 条）

| 临时 ID | 来源条目 | 类型 | 关联现有 ID | 现状（03/02） | 图标 | 所有权 | 目标 | 冲突 / 待问 |
|---|---|---|---|---|---|---|---|---|
| A1 | SA-01 | ADD | PA-01 §2/§3/§10, PA-01.2 | 无幂等 / 状态机 / 重试设计记录 | ✅ | O2（PA-01 设计 ✅） | 03 PA-01 + 新 PA-01.8 | MQ / DB 产品未知 → OQ-5.4 |
| A2 | SD-05 | ADD | X-01, PA-01.6 | X-01 只写 "led data migration"，无 entitlement、无流程 | ✅ | O2（X-01 "led" ✅） | 03 PA-01 §6 + 新 PA-01.9；skills Spring Batch 加锚点 | 与 SA-09"周末分批 + 维护窗口切换"冲突 → CF-21 |
| A3 | SI-03 | ADD | PA-01 §6, CF-N4 | 无对账记录；CF-N4：hub 不做对账 | ✅ 事实 / ❓ 归属 | 不定 | 03 PA-01 §6（不出简历措辞） | 谁做、哪一阶段 → OQ-5.2 |
| A4 | SB-04 | ADD | X-06, PA-02（关闭 IB-01） | X-06 面试行写 "generic flow only"，无具体事件 | ✅（永久修复归属 ❓） | O3（协调） | 03 X-06 | 修复归属 → OQ-5.1 |
| A5 | SD-02 | ADD | X-06, §0A | 无事件指挥做法 | ✅ | O3 | 03 X-06 + §0A 新行 | "半天内解决"是目标还是实际 → OQ-5.8 |
| A6 | SB-12 | CLARIFY | X-02, X-05, §0A 第 2 行（解决 SC-01） | "Lead 25 engineers"；未写工程师来自供应商 | ✅ | PL | 03 X-02、X-05、§0A | ⚠ 背调敏感（团队规模归属）；squad lead 是否也是供应商人员、"performance management"含义 → OQ-5.5 |
| A7 | SD-01 | ADD | X-02（关闭 IB-03） | 无冲突处理事件 | ✅ | PL + DM | 03 X-02 | 平台、年份、印度开发是否你的团队 → OQ-5.7 |
| A8 | SA-03 | ADD | PA-07 §5/§6 | §5 "noise and false positives ❓" | ✅（子项需逐项确认） | O1 + O2 | 03 PA-07 + 新 PA-07.7 | 子项内部可能矛盾 → B1 |
| A9 | SI-02 | ADD | PA-11 §6/§7 | 无 MVP / feature toggle 记录 | ✅ | O2 + PL | 03 PA-11 + 新 PA-11.6 | — |
| A10 | SI-01 | ADD | PA-11（关闭 IB-04） | 无人员管理事件 | ✅ | PL | 03 PA-11 + 新 PA-11.7（仅面试） | 与 PA-12"led the big-data team"不冲突（该负责人在你之下） |
| A11 | SB-05 | ADD | 02 §1 | 02 无通知期字段 | ✅ | — | 02 §1 | Singtel 面试说过"约 2 周" → D 组 |
| A12 | SD-20 | RETIRE + CLARIFY | 02 §2 行 2、时间线、§6.2；03 PA-20；fact-check TL-4、OQ-1.8；skills 7 行；05 §6 | Pureland "May 2020 – Present, concurrent" | ✅ 决定 | — | 02、03、fact-check、skills、05 | ⚠ 背调敏感（日期）：结束时间依据 → B3 |
| A13 | 冲突与待问 | REGISTER | fact-check §2/§4/§5 | — | ⚠️ / ❓ | — | fact-check | 见 A13 |

---

## A. 可批准的更新（精确文本）

### A1 — SA-01 支付 hub 设计（03 PA-01）
① **§2 末尾追加**（"Settlement context" 段之后）：
> **Design for integrity and resilience** ✅[CONF 2026-10-26]: (a) every payment carries a unique business reference enforced in the database, plus an explicit state machine, so retries never create duplicates; (b) reference data is replicated locally and managed in the hub, keeping source systems off the critical path (trade-off: data freshness); (c) hand-off to downstream systems is asynchronous, with retry and an exception queue — on a timeout the hub checks downstream status before resending; (d) it runs on Java / Spring Boot with a database and a message queue (MQ). Database and MQ products: ❓ OQ-5.4.

② **§3** 句末追加：`; a message queue (MQ) ✅[CONF 2026-10-26] (product ❓ OQ-5.4)`
③ **§10** 追加一条：`"How do you prevent duplicate payments?" / "What happens when a downstream call times out?" → §2 design (a) and (c); "How do you handle reference data?" → (b), with the freshness trade-off.`
④ **表格新增**：
| PA-01.8 | Safe-retry design | CONF 2026-10-26 | ✅ | Designed the hub for safe retries: a database-enforced unique business reference and an explicit payment state machine prevent duplicates, and downstream hand-off is asynchronous with retry, an exception queue and a status check before any resend. |

### A2 — SD-05 数据迁移含 entitlement（03 PA-01 + skills）
① **§6 Actions 末尾追加**：
> **Payment and entitlement data migration** ✅[CONF 2026-10-26]: the hub supported migration of payment data and entitlement data — users, companies, groups and roles (a user can belong to several groups across companies) — from the legacy platform. Each batch was approved in the old system, exported as JSON, validated record by record on the new side against related applications (user accounts, remittance), then loaded by Spring Batch jobs. (A "migrated over several weekends, switched in a maintenance window" version from one interview-prep document is not confirmed — CF-21.)

② **表格新增**：
| PA-01.9 | Entitlement-data migration | CONF 2026-10-26 | ✅ | Led migration of payment and entitlement data (users, companies, groups, roles) from the legacy platform in approved batches — exported as JSON, validated record by record against related applications, and loaded by Spring Batch jobs. |

③ **03 X-01** 末尾追加：`UOB hub detail: PA-01.9.`
④ **skills inventory Spring Batch 行** "Where used"：`UOB CCD — scheduled-job processing module, personally built` → `UOB CCD — scheduled-job processing module, personally built; UOB payment hub — Spring Batch jobs loading migrated payment and entitlement data (PA-01.9) [CONF 2026-10-26]`。深度保持 P（不推断 hub 迁移作业是你亲手写的）。

### A3 — SI-03 MT/MX 共存期对账（03 PA-01 §6，不出简历措辞）
> **Coexistence reconciliation** ✅[CONF 2026-10-26]: during MT/MX coexistence, both sides (MT and MX) were reconciled — mandatory, since otherwise mismatched records could not be explained in compliance reporting. Which team ran it, and at which stage: ❓ OQ-5.2 (the hub itself does not reconcile — CF-N4). Interview use only until the owner is known.

§10 追加：`"How did you keep MT and MX consistent during coexistence?" → coexistence reconciliation (owner per OQ-5.2).`

### A4 — SB-04 P1 事件（03 X-06）
在 X-06 safe wording 之前插入：
> **Sanitised P1 example** ✅[CONF 2026-10-19; listed as confirmed 2026-10-26] — a payment stuck in "pending in process". Splunk logs and payment records showed the hub had initiated it and sent it downstream, but the hub never received the response; the downstream team confirmed the payment had been processed — the response was blocked in the messaging channel back to the hub. **Containment:** the downstream team cleared the blocked messages and the affected payments recovered. **Permanent fix:** the messaging channel was optimised {— owner: his team or the channel team ❓ OQ-5.1}. No rollback was involved. Interview use only; no internal names or volumes.

Interview 行：`"Walk me through a P1." (specific incident — confidential details stay out; generic flow only)` → `"Walk me through a P1." → the sanitised example above (confidential details stay out).`
**写法说明**：原材料没有说是谁查的 Splunk，所以写"logs showed"，不写"I checked"。

### A5 — SD-02 事件指挥做法（03 X-06 + §0A）
① X-06 追加：
> **Incident-command practice** ✅[CONF 2026-10-26]: one point of coordination in the first 15 minutes; a war-room channel; a hold-or-fail-over decision within 10 minutes; engineers assigned to logs and database, and to messaging and downstream; hourly syncs; first stakeholder update within 30 minutes, then hourly; DevOps or security pulled in if not resolved within an hour; blameless postmortem within 48 hours. These are practice targets, not measured results (§0A). "High-severity issues resolved within half a day": target or actual ❓ OQ-5.8.

② X-06 新增可选 safe wording：
> "Run high-severity incidents with a set command routine — a single coordinator, a war room, a fail-over decision within minutes, regular stakeholder updates and a blameless postmortem within 48 hours."

③ §0A 新行：
| **new** · Incident-command time targets: coordinator in 15 min · hold/fail-over decision in 10 min · first stakeholder update in 30 min, then hourly · escalate at 1 h · postmortem within 48 h | UOB (X-06) | ✅ [CONF 2026-10-26] practice targets, not measured outcomes; "resolved within half a day" ❓ OQ-5.8 |

### A6 — SB-12 工程师来自四家供应商（03 X-02、X-05、§0A）⚠ 背调敏感
① §0A 第 2 行 Attribution：`UOB` → `UOB; the engineers come from the four IT service vendors (X-05) [CONF 2026-10-26]`
② X-02 第 1 条末尾追加：`**The engineers come from the four IT service vendors under his governance (X-05)** ✅[CONF 2026-10-26].`
③ X-02 第 2 条：`covers 1:1s, mentoring and performance management. ✅ / 📄` → `covers 1:1s, mentoring and performance management. ✅ / 📄 — for vendor staff, what "performance management" covers is ❓ OQ-5.5; until answered, new resumes use "1:1s and mentoring" only.`
④ X-05 末尾追加：`The engineers he leads (X-02) come from these vendors ✅[CONF 2026-10-26].`
⑤ X-02 Interview（新增一行）：`"Are they your direct reports? Did you hire them?" → the engineers come from four IT service vendors; he leads their day-to-day work and governs the vendors (X-05). Never "hired".`
⑥ X-02 safe wording 第 1 条**保留不改**（"Lead 25 … engineers" 仍然准确）；新增可选变体：`"Lead 25 onshore and offshore engineers from four IT service vendors in two platform teams serving millions of accounts."`

### A7 — SD-01 需求冲突事件（03 X-02）
① X-02 新增一条：
> **Requirement conflict with offshore developers** ✅[CONF 2026-10-26]: offshore developers in India and Singapore business users clashed because requirements changed often and expectations were unclear. He introduced a requirement-clarification workshop before each sprint (BA, dev lead, QA, business users) to agree acceptance criteria and scope, plus a change-impact assessment for late changes. Escalations fell, trust improved and sprint delivery became more stable (qualitative). Platform and period: ❓ OQ-5.7.

② 新增 safe wording：
> "Introduced pre-sprint requirement-clarification workshops (BA, dev lead, QA, business users) and change-impact assessment for late changes, reducing escalations between offshore developers and business users and stabilising sprint delivery."

### A8 — SA-03 AI 代码评审运行控制（03 PA-07）
① §6 Actions 末尾追加（**按 B1 结果逐项保留**）：
> **Operating controls** ✅[CONF 2026-10-26]: (i) the agent runs in an isolated, read-only environment (ii) with no outbound network access; (iii) code never leaves the bank's network; (iv) the model endpoint is in-region; (v) prompts and outputs are fully logged; (vi) review rules are kept in the repository under normal change approval; (vii) the rejection rate is tracked, (viii) with false-positive suppression.

② §5：`keeping noise and false positives low ❓` → `keeping noise and false positives low (controls: §6 (vii)–(viii))`
③ 表格新增（只用最没有争议的子项）：
| PA-07.7 | Operating controls | CONF 2026-10-26 | ✅ | Ran the review agent in an isolated, read-only environment with an in-region model endpoint and full logging of prompts and outputs, with review rules version-controlled under normal change approval. |

### A9 — SI-02 VV-Life 0-to-1 方法（03 PA-11）
① §6 追加：
> **0-to-1 approach** ✅[CONF 2026-10-26]: product and operations teams ran market research before building; a small MVP, then small steps; every new feature behind a toggle so it could be pulled back in minutes; architecture designed for iteration. Some features missed and were fixed from user feedback. Web, mobile APIs and backend on AWS, with CI/CD and Splunk monitoring.

② §7 追加：`The core model worked and users stayed ✅[CONF 2026-10-26] (qualitative — no retention figure).`
③ 表格新增：
| PA-11.6 | 0-to-1 in small steps | CONF 2026-10-26 | ✅ | Delivered VV-Life from 0 to 1 as a small MVP grounded in the product and operations teams' market research, then iterated in small steps with every new feature behind a toggle that could be pulled back in minutes. |

### A10 — SI-01 管理表现不佳的负责人（03 PA-11，仅面试）
① 新增 §13：
> **13. People-management example** ✅[CONF 2026-10-26] — a lead who ran several teams, including the big-data team, underperformed: gaps in planning and upward reporting, and personal emotion brought into the team. His teams blocked the project (business analysts waited months for technical support); people disengaged and some left. Wilson gave him the facts, agreed clear goals and a review period with real support; when the goals were not met, he let him go. The teams were moving again within weeks.

② §10 追加：`"An underperformer you managed." → §13.`
③ 表格新增：`| PA-11.7 | Managing out an underperforming lead | CONF 2026-10-26 | ✅ | — (interview only; not a resume bullet) |`

### A11 — SB-05 通知期（02 §1）
§1 表格 "Total experience" 行之后新增：
| Notice period | **Two months (contractual).** As of 2026-10-26 the resignation is in progress, so availability ≈ one month after an offer | ✅ [CONF 2026-10-26] (SB-05 / SD-08). Supersedes the "about 2 weeks" said on 2026-10-23 |

### A12 — SD-20 Pureland 从工作经历移除（多文件）⚠ 背调敏感
**02**
- §2 行 2：期间 `May 2020 – Present (concurrent, part-time)` → `May 2020 [LIB] – ended before Oct 2022 [CONF 2026-10-26]`；状态列 → `⛔ **Removed from work history** [CONF 2026-10-26] (D-16). Not on resumes; kept for the record. Start month [LIB] only`
- 时间线：`[Pureland 2020.5 → present, part-time]` → `[Pureland 2020.5 → ended before 2022.10 — removed from work history, D-16]`
- §6.2 标题 → `### 6.2 Pureland Holding (Jewelake) — ⛔ Removed from work history (D-16) · May 2020 – ended before Oct 2022`；正文首句前加：`**Decision [CONF 2026-10-26]:** the advisory arrangement ended before he joined UOB (Oct 2022); no outside work now. Not used in resumes or as current work. Text below kept for the record.`

**03**
- §1 行 PA-20：状态 `⛔ until disclosure` → `⛔ retired 2026-10-26 (D-16)`；期间 `Pureland · 2020–` → `Pureland · 2020 – before Oct 2022`
- PA-20 标题 → `### PA-20 · Pureland Holding — Wealth / Quant Platform — ⛔ RETIRED 2026-10-26 (D-16)`；正文不删，首加：`Removed from work history; arrangement ended before Oct 2022. Kept for the record only.`
- 新增 §5.5 Retired items：`| PA-20 | 2026-10-26 | Removed from work history by decision D-16 (arrangement ended before Oct 2022) | Card kept in §4 |`
- §5.3 "Selective: Pureland · Crypto" 行 Note：`Pureland retired (D-16)`

**fact-check**
- TL-4 → `✅ Closed 2026-10-26 → D-16`；OQ-1.8 → `✅ Closed 2026-10-26 → D-16`
- 新增 D-16：`Pureland Holding (Jewelake) removed from the work history. The advisory arrangement ended before he joined UOB (Oct 2022); no outside work now. LinkedIn / resume alignment: not now (his decision). Record: in the Cloudera screen (2026-07-10) he said he was "still the consultant" — inconsistent with this decision. Interview answer: "It ended before I joined UOB; my profile is out of date." | 02 §2, §6.2; 03 PA-20, §5.5; skills; 05 §6`

**skills inventory**（7 行带 Pureland 锚点：Python、Spark、Hive/MR/YARN/Hadoop、AWS S3、AWS general、Claude agents、quant libraries）：只把 "Pureland" 改成 "Pureland (removed from work history — not citable, D-16)"，**深度不改**（见 B4）。

**05 §6 第 212 行**：`` `on-request` only: Pureland (PA-20 — needs disclosure plan), Crypto… `` → `` `on-request` only: Crypto… ``，并在下面加一行 `- Never: Pureland (PA-20 retired, D-16).` ——这是通用选择规则的变化，符合 05 的修改条件。

### A13 — fact-check 登记（冲突 · 高风险 · 待问 · 决策）
- **D-17**（决策日志）：`Interview Bank back-fill 2026-10-26 — confirmed facts applied: [仅列入最终批准的条目]. Closes Interview Bank IB-01 (SB-04), IB-03 (SD-01), IB-04 (SI-01); resolves SC-01 (SB-12), SD-08, SD-11, SD-16.`
- **§2 冲突 CF-17 – CF-27**（新）：

| ID | 话题 | 版本 A（面试中说过 / 写过） | 版本 B（事实库） | 默认 | 风险 |
|---|---|---|---|---|---|
| CF-17 | CBPR+ 提前量 | "went live 2 months ahead of the deadline"（Singtel 口述） | MX-rich 2025-05 / 08 vs SWIFT 2025-11；"2 months ahead of plan" 属 Baidu PA-17.1 | B | 🟠 |
| CF-18 | C360 / hub 的定位 | C360 = "customer relationship management"、"small & middle merchant clients"；hub 有 "reconciliation" | PA-05 customer-360（wealth cross-sell、client management）；CF-N4 hub 不对账 | B | 🟠 |
| CF-19 | hub 功能范围 | routing（rail / 代理行）、KYC enrichment、compliance validation、duplicate-check 服务、SWIFT gateway 服务 | PA-01：initiation、validation、enrichment、authorisation、pain.002；processing / settlement 在外。注：duplicate prevention 现由 A1(a) 覆盖 | B，等你确认是否有任一项属实 | 🟠 |
| CF-20 | AI 评审 80% | "review quality / efficiency +80%"；"new joiners 30–40% faster" | PA-07.3 senior review **time** −~80% **估算**；C3 未决 | B | 🟠 |
| CF-21 | 迁移方式 | "migrated data in batches over several weekends … switched over in a planned maintenance window" | PA-01.1 分阶段 Blue/Green 共存；PA-01.9 分批审批迁移 | B，等你确认是否有周末分批步骤 | 🟢 |
| CF-22 | UOB 团队规模 | "a team of around 10 engineers"（JPM 2026-10-09、IFS） | 25（15 + 10） | B；问：当时是否只指 CCD | 🔴 背调 |
| CF-23 | 弱项表述 | "no lending product experience"；经验含 "quantitative trading" | PA-04 零售无抵押贷款 + 催收；PA-20 已退役 | B | 🟠 |
| CF-24 | 到新加坡时间 | "moved to Singapore 6 years ago"（2026-07） | VV Technology（Singapore）2019-04 起 | B | 🟢 |
| CF-25 | 职业起点 | "started my career as a (big) data engineer, about two years" | Renren Senior R&D Engineer 2008–12；定位规则 | B | 🟠 |
| CF-26 | 离开 VV 的原因 | "due to Covid the companies moved to China" | 02 §6.4：CEO 把技术团队迁回中国，他因家庭留新 | B | 🟢 |
| CF-27 | 技术栈错配 | Baidu 用 Spring Cloud + Redis + Kafka；AI 评审用 Spring AI | PA-17：Dubbo、Resin、MongoDB…（Spring Cloud 2015 才发布）；PA-07：Spring Boot + headless Claude Code | B | 🟠 |

- **§4 高风险说法 HR-11 – HR-15**（新）：HR-11 SA-18 "connection-pool misconfiguration" 事件（像模板，非真实）· HR-12 SD-17 "eliminates 60% of causes"（编造统计）· HR-13 SA-07 "around ten years in large tech companies … millions of users"（§0A 无）· HR-14 SA-08 "millions of payments a day"、SD-15 "UOB IT 3000+ employees"（UOB 数据，规则 12）· HR-15 SD-13 "angel round to Series B & C"（无来源）。
- **已有条目在面试中再次出现**（只在原条目加一句 "also said in interviews, 2026 — Interview Bank traps"，不新开 ID）：HR-1（SI-15、SD-12 "technical architect" 作头衔）、HR-2 / FU-1（SD-12 "ten million daily users"）、HR-3 / HR-9（SI-11、SD-13 "100+"）、HR-10（SI-14）、CF-07（SD-12 Flink）、CF-11（SI-12）、§0A "multi-million daily transactions" ⛔（SI-13）、X-04 编码时间占比规则（SD-14 "half my time"）。
- **§5 新批次 "Batch 5 — Interview Bank back-fill (2026-10-26)"**：登记 §B 全部问题为 OQ-5.1 – OQ-5.30（编号见 §B）。

---

## B. 需要你回答的问题（附默认处理）

### B-1 影响本轮措辞（建议先答）

| ID | 问题 | 默认处理 |
|---|---|---|
| B1（SA-03） | (iii) "code never leaves the bank's network" 与 (iv) "in-region model endpoint"、(ii) "no outbound network access" 放在一起会被追问：diff 要发到模型，端点是在银行网络内（私有链路 / 内部网关），还是银行外的云区域？另：(vii) rejection rate 怎么算、(viii) false-positive suppression 具体怎么做？ | (i)(iv)(v)(vi) 入库；(ii)(iii)(vii)(viii) 先挂 ❓ OQ-5.3，不进 safe wording |
| B2（SB-12） | squad leads / engineering managers 也来自供应商吗？"performance management" 对供应商人员实际指什么（你给供应商年终评审的意见 X-05，还是直接绩效管理）？ | 按 A6 ③：新简历只写 "1:1s and mentoring" |
| B3（SD-20） | "ended before Oct 2022" 的依据（终止邮件、最后一张发票、合同）？能给出年月吗？ | 只写 "ended before Oct 2022"，不写月份 |
| B4（SD-20） | Python、quant libraries 的唯一雇主锚点是 Pureland；移除后，简历里 Python 还能用吗（锚点改为 personal / agentic tooling）？ | 只加 "not citable" 注记，深度不改；简历暂不把 Python 作为雇主技能 |
| B5（SB-04） | 消息通道的永久优化是你的团队做的，还是通道团队做的？ | 保留 `{…}` slot，面试说 "the messaging channel was optimised" |
| B6（SI-03） | MT/MX 双边对账由哪个团队、在什么阶段做？ | 只在面试用，不出简历 |
| B7（SD-02） | "high-severity issues resolved within half a day" 是目标还是实际情况？ | 记为目标，不作结果 |
| B8（SD-01） | 印度的开发是你的供应商离岸团队，还是 X-02 里"协作、非直属"的团队？哪个平台、哪一年？ | 写 "offshore developers in India"，不写平台和年份 |
| B9 | SB-02（P1/P2 后紧急变更）、SB-03（ISO 20022 无 PET / 预生产演练）、SB-06（离开 GBD 的原因：照顾父母健康，对外说 family reasons）、SB-07（PMP 未排考）都标了 [CONF 2026-10-19]，不在你的清单里。本轮一起入库吗？ | 不入库，留到下一轮 |

### B-2 其余 ❓ 条目 → OQ-5.x（不回答时一律不入库，只登记）

| OQ | 来源 | 问题 |
|---|---|---|
| OQ-5.1 – 5.3 | SB-04、SI-03、SA-03 | 见 B5、B6、B1 |
| OQ-5.4 | SA-01(d)、SB-10 / SA-10、SA-12、SI-07、SD-18 | UOB 实际技术栈：MQ 产品？数据库是 Oracle 吗？Kafka / Redis 在 UOB 是否用于你的平台（"有单独团队管 Kafka"）？SFTP / Axway API gateway + JWT / SSL 硬件网关？ |
| OQ-5.5 | SB-12 | 见 B2 |
| OQ-5.6 | SC-03 | 除你的团队外，是否另有运维 / L1 desk？ |
| OQ-5.7 – 5.8 | SD-01、SD-02 | 见 B8、B7 |
| OQ-5.9 | SB-08 | MVP 排序僵持时，提交给更高层决策——真实做法吗？ |
| OQ-5.10 | SB-09 | "在互联网公司带技术和基础设施团队搭网站环境"——哪家公司？ |
| OQ-5.11 | SB-11 | 发布做法：先部署到 standby 环境验证、向生产支持讲变更、准备上线与回滚计划、上线后 Splunk 监控——真实吗？ |
| OQ-5.12 | SA-04（= C4） | AI 评审推广：先一个 squad，调 prompt 降噪，再推广，其他 squad 主动要求——真实吗？是否 25 人都在用？ |
| OQ-5.13 | SA-11 | UOB 主要是私有环境、无公有云；AWS 实操来自 GBD / VV？ |
| OQ-5.14 | SA-13 | 有带类生产数据的 "BAU" 环境；用 GenAI 生成测试数据？ |
| OQ-5.15 | SA-14 | 工作外在本地和 AWS 搭过 Spring AI 架构？（关联 PA-21） |
| OQ-5.16 | SA-17 | 遗留应用几乎每月出生产事件？ |
| OQ-5.17 | SI-04 | 用人做法：按缺口招人、目标 / 期限 / 边界、1:1、争取公平薪酬、技术辅导、"帮 squad lead 成长为经理"——哪些属实？ |
| OQ-5.18 | SI-05（关联 IB-02） | 供应商做法：像招聘一样面试驻场人员、客户数据不出行、合同含源码归属 / 文档 / 退出 / 审计条款、缺陷与稳定性跟踪、每日站会 + 周会——哪些属实？有没有具体的供应商绩效问题案例？ |
| OQ-5.19 | SI-06 | BAU 与项目 backlog 每两周和业务复盘？ |
| OQ-5.20 | SI-09 | "AI 先写代码和测试初稿，工程师审"——是团队做法吗？ |
| OQ-5.21 | SD-03 | 用 AI 重构遗留中间件代码（抽可复用 API）；从 user story 生成测试原型？ |
| OQ-5.22 | SD-04 | 研究 ISO 20022 进出报文与报表、2025 年向经理提 AI agent 想法；2026-05 起部门 AI 团队，你是成员并写代码？ |
| OQ-5.23 | SD-06 | 两个 squad 各有 squad lead；站会 20–30 分钟；两周 sprint；回顾会？ |
| OQ-5.24 | SD-07 + IB-11 | JUnit 覆盖率 ≥ 90%？第三方出渗透测试报告？Jenkins 部署 JAR、Aldon（Rocket）管包？"SonarQube 100%" 是覆盖到 100% 的流水线，还是覆盖率门槛？99% 门槛是新代码还是全量？ |
| OQ-5.25 | IB-12 | "CEW 50+ code components"：§0A "~50" 改 "50+"？范围只是 hub（关闭 C6 的模块部分）？"~20 个核心模块深审"不变？ |
| OQ-5.26 | IB-05 | 延迟改进的数字、根因、你的部分 O1 还是 O2（含 C7 并发控制模块） |
| OQ-5.27 | IB-06 | DR 演练频率、范围、RTO / RPO；MTTR 前后 |
| OQ-5.28 | IB-07 | Cloudera 选型：比较过哪些方案、标准；C5 你是否主导 2022 上线 |
| OQ-5.29 | IB-08 | PA-04 技术、挑战、结果；哪个团队负责贷款 / 催收（C6）；两条线排期冲突的一个具体例子 |
| OQ-5.30 | IB-13、IB-14、IB-15、IB-16 | Baidu 接手时的问题；VV 对账设计（频率、异常处理）；C1 – C4 剩余部分及降噪；上线就绪门的标准与 CBPR+ 关键路径上的险情 |

IB-09（= CF-11）、IB-10（= OQ-2.3）：已有登记，不新开。

---

## C. 只能记为推断 / 不入库

- A1(b) 的"freshness 取舍"按你确认的原文写，不扩展成同步频率或缓存策略。
- A4：不写"我查了 Splunk"——材料没说是谁查的。
- A5 的时间数字只作"做法目标"，不作"结果"；不推断 MTTR 改善。
- A6：不推断"这些工程师不是 UOB 员工"之外的雇佣细节（合同形式、计费方式）；不推断你参与招聘。
- A10：不推断 VV 被辞退的人数、职位名称或时间。
- 不入库（按设计）：薪资、入籍、对他国 / 年龄的评论、Pureland 背后的私人关系、IFS 公司细节与面试官姓名、SA-15 "预算每年削减 / 项目结束后供应商团队归零"的说法（敏感框架，不作事实）。
- SC-01、SD-08、SD-11、SD-16 已被本轮条目解决，不单独入库。
- 观察（不在本轮范围）：DBS、NCS、Solderfield 简历中的 "payment-gateway integration with Alipay…" 来自 `_batches\2026-10-20_JobStreet-CTO-search` 的 S1 批次事实，**尚未进 03**；SA-16 的"payment gateway"说法与之相关。建议另开一轮处理 Batch_Fact_Update_Proposal。

---

## D. 可能影响已投递简历 / 面试的更正

| 优先级 | 影响 | 位置 | 原句 | 说明 |
|---|---|---|---|---|
| 🔴 高 | A6（SB-12） | Talentvis、Airwallex、Landi、NETS、PrivateAdvertiser、Stripe（6 份） | "…through squad leads and engineering managers, with 1:1s, mentoring and performance management" | 工程师来自供应商；若被问"绩效怎么管"，须按 B2 的真实情况回答。不自动改旧简历 |
| 🟢 无影响 | A6 | 全部 12 份 | "Lead 25 onshore and offshore engineers"、"chair governance of four IT service vendors" | 仍然准确 |
| 🟢 无影响 | A12（SD-20） | 全部 12 份 | — | 已核对 docx 文本：没有一份写 Pureland |
| 🟠 中 | A12 | LinkedIn | 仍显示 Pureland 在职 | 你决定暂不改；面试答法见 D-16 |
| 🟠 中 | A11（SB-05） | Singtel（面试，2026-10-23） | "about 2 weeks" | 下次联系时更正为"约一个月" |
| 🟢 无影响 | CF-17 | 全部 12 份 | "…May and August 2025, ahead of SWIFT's November 2025 deadline" | 简历与 03 一致；冲突只在口述 |
| 🟢 | A1、A2、A5、A8、A9 | — | — | 新增可用证据，旧简历不受影响 |

Interview Bank 侧：入库后可启用 A-Q0029 / 0036（SA-01）、A-Q0030 / 0032（SA-03）、A-Q0052（SI-01）、A-Q0048（SI-02）、A-Q0037 / 0051（SI-03）、A-Q0014（SD-01）、A-Q0017（SB-04、SD-02）、A-Q0073（SD-05）的 parked 块，以及 A-Q0001 / 0008 / 0020（SB-12）。

---

## 决定（待填）

| ID | 决定（Y / E / Q / N） | 日期 |
|---|---|---|
| A1 – A10 | Y（A8 按默认只入 (i)(iv)(v)(vi)） | 2026-10-26 |
| A11 | E — 通知期统一写"一个月"，不写"合同两个月 / 辞职进行中" | 2026-10-26 |
| A12、A13 | Y | 2026-10-26 |
| B1 – B9 | 未回答 → 按默认处理（已登记为 OQ-5.x） | 2026-10-26 |

## 未采纳

| ID | 决定 | 日期 | 备注 |
|---|---|---|---|
| A8 子项 (ii)(iii)(vii)(viii) | Q（B1 默认） | 2026-10-26 | 记入 03 PA-07 §6 "held"，OQ-5.3 |
| A11 原文"Two months (contractual) … resignation in progress" | 被 E 替代 | 2026-10-26 | 02 只记"One month"；早先说法列为 superseded |
| SB-02、SB-03、SB-06、SB-07 | 不在本轮（B9 默认） | 2026-10-26 | OQ-5.31 |
| 其余 ❓ 条目 | Q | 2026-10-26 | OQ-5.9 – 5.30 |

---

# 补充轮 — 2026-10-27（回答 OQ-5.5、OQ-5.3、CF-22、B3、通知期）

**来源**：Wilson 2026-10-27 原话 [CONF 2026-10-27]。**状态**：✅ 已应用（2026-10-27）。

**决定**：R1 Y · R2 方案 a · R3 Y · R4 (a) 维持现状 · R5 Y（2026-10-27）。未采纳：R2 方案 b（挂起项仍为 OQ-5.3）；R4 (b)(c)。

| 临时 ID | 回答 | 类型 | 目标 |
|---|---|---|---|
| R1 | squad lead 来自供应商；对供应商人员，"performance management" 指在需求开发、项目进度、结果交付、最终上线和事件处理全过程中的表现 | CLARIFY（部分关闭 OQ-5.5；EM 是否来自供应商仍 ❓） | 03 X-02 |
| R2 | 模型端点：经 AWS 专网专线访问 | CLARIFY（部分关闭 OQ-5.3） | 03 PA-07 §6、PA-07.7 |
| R3 | CCD 10 人，CEW 15 人 | 关闭 CF-22 | fact-check CF-22 |
| R4 | "去掉 Pureland 的工作经历"；不提供结束年月 | 关闭 B3；处理方式待定（见问题） | 02 / 03 / skills |
| R5 | 通知期：ok | 仅记录确认，不改 02 | fact-check D-18 |

### R1 — 03 X-02 第 2 条
**前**：`… covers 1:1s, mentoring and performance management. ✅ / 📄 — for vendor staff, what "performance management" covers is ❓ OQ-5.5; until answered, new resumes use "1:1s and mentoring" only.`
**后**：`… covers 1:1s, mentoring and performance management. ✅ / 📄 — Squad leads also come from the vendors ✅[CONF 2026-10-27]; whether the engineering managers do: ❓ OQ-5.5. For vendor staff, "performance management" means assessing each person's performance across the whole cycle — requirement development, project progress, delivery, go-live and incident handling ✅[CONF 2026-10-27].`
X-02 Interview 行追加：`· "How do you manage the performance of vendor staff?" → each person is assessed across requirement development, progress, delivery, go-live and incident handling.`
**影响**：解除"新简历只写 1:1s and mentoring"的限制；6 份已投递简历的 "performance management" 从 🔴 降为 🟢（面试按上面的口径回答）。

### R2 — 03 PA-07
**§6 前**：`… the model endpoint is in-region; … Also stated, held until OQ-5.3 is answered: no outbound network access; code never leaves the bank's network; rejection-rate tracking; false-positive suppression.`
**§6 后（方案 a，只写你说的）**：`… the model endpoint is in-region on AWS, reached over a private dedicated connection ✅[CONF 2026-10-27]; … Also stated, held (OQ-5.3 remainder): no outbound network access; code never leaves the bank's network — as worded, this does not fit an AWS endpoint, since diffs travel to AWS over the private connection; rejection-rate tracking; false-positive suppression.`
**方案 b（另加，需你确认事实）**：把两项挂起子项改写入库为 `the agent environment has no public-internet access — its only outbound path is the private connection to the model endpoint, so code never travels over the public internet.`
**PA-07.7 safe wording**：`with an in-region model endpoint` → `with an in-region model endpoint reached over a private dedicated connection`（方案 b 再加 `and no public-internet access`）。
**说明**：只写"AWS"和"专网专线"，不推断具体 AWS 服务名。

### R3 — fact-check CF-22
"Proposed default" 列 → `✅ Resolved 2026-10-27: CCD 10 + CEW 15 = 25 [CONF 2026-10-27]. External answer: 25 (15 + 10), or name the team; never "~10" for the whole team.`

### R4 — Pureland
B3 关闭：不记录结束年月。现状：02、03、skills 已把 Pureland 标为"已从工作经历移除"，但按 01 §2 规则 5 保留原文作为档案记录。**需要你选**：(a) 维持现状（推荐）；(b) 把 02 §2 第 2 行和时间线中的 Pureland 移出，挪到 02 新增的 "Retired" 表，§6.2 正文也挪进去；skills 的 8 处锚点删除 Pureland 字样（Python、quant libraries 只剩 personal / agentic tooling）；(c) 从全部主文件物理删除（违反 01 §2 规则 5，需要你明确批准，快照仍保留旧版）。

### R5 — fact-check D-18
`2026-10-27 — OQ-5.5 partly answered (squad leads from vendors; vendor-staff performance-management scope); OQ-5.3 partly answered (AWS endpoint over a private dedicated connection); CF-22 resolved; B3 closed without an end date; notice period one month acknowledged.`
