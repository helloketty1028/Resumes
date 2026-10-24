# Fact Library Update Review — TEKsystems 申请后回灌

**日期：** 2026-10-17 · **场景：** 申请后回灌 · **材料：** `applications\2026-10-17_TEKsystems_Program-Manager\Fact_Update_Proposal.md`（TU-01 – TU-15）
**基线（已实际读取）：** 本地 `master\v2.0-draft\` — 01 v1.0 · 02 v3.0 · 03 v4.0 · 04 v1.0 · 05 v1.0 · skills inventory v2.2 · fact-check v2.2（文件时间 2026-10-16 08:57，本次比对前无变化）
**处理口径：** 按你的说明，全部 15 条视为"未决定"（没有 5A 结果），先与事实库逐条比对，已在库内的内容不再提。
**状态：★ 审批门 — 尚未修改任何源文件。** 默认 N：没有被你明确选中的条目一律不入库。

## 0. 比对结果总览

| TU | 结论 | 去向 |
|---|---|---|
| TU-01 Sohu 发布流程 | 库中没有 → 新增 | A1 |
| TU-02 Miro | 库中没有 → 新增锚点；用途未确认 | A7 + B4 |
| TU-03 跨区域协作 / 美国 | 库中都没有 → 新增亚太协作，并登记"不写美国"的限制 | A2 + A3 |
| TU-04 40 / 140 总编制 | 库中仍为 ❓（OQ-2.3）；确认来自 10-16 的另一个会话，属背调敏感项 | B1 |
| TU-05 MVP 排序做法 | 库中没有 → 新增 | A4 |
| TU-06 PA-08 所有权与日期 | 库中仍为 ❓ → 澄清 | A5 |
| TU-07 PA-07 上线与审批 | 上线月份和审批库中没有 → 澄清；"25 = 两队合计"**已在 X-02，重复，不再提** | A6 |
| TU-08 姓名 "Wilson" | 事实已在 02 §1；只需关闭 FU-6 | A9 |
| TU-09 早期经历月份 | **月份已在 02 §2，事实重复，不再提**；只剩一条通用版式规则 | A10 |
| TU-10 HR-9 措辞 | 库中仍写 "Built and led {40}" / "Built … {of 140}" → 依赖 B1 | A8（以 B1 为前提） |
| TU-11 200+ 国家 | 库内自相矛盾（§0A 标 ⚠️，PA-10 §8 标 📄 可用） | B5 |
| TU-12 SQL / RHEL 锚点 | 库中熟练度 ✅，但没有雇主锚点 | B6 |
| TU-13 VV / AI Park 职称 | 与 10-15 的确认冲突（CF-16 ⚠️），属背调敏感项 | B2 |
| TU-14 AI Park 2016 年 4 月起 | 默认值已是 4 月；关闭 CF-06 需要原始依据 | B3 |
| TU-15 恒顺源日期写法 | "简历用选项 (a)"是写法决定 → 可直接定；日期本身的依据并入 B3 | A11 + B3 |

---

## A. 可批准的更新（证据为你的明确确认）

| # | 类型 | 目标文件 § | 修改前（原文） | 修改后（拟写入文本） | 来源 | 图标 / 所有权 | 影响面 |
|---|---|---|---|---|---|---|---|
| **A1** | ADD | 03 §3 PA-18 表格，新增一行 | （无） | `\| PA-18.2 \| Publishing-workflow design \| CONF \| ✅ \| Contributed to the design of Sohu News' publishing workflow — story flow, editorial review and scheduled publishing. \|`；PA-18 文字段加：`Publishing workflow: contributed to its design ✅[CONF 2026-10-17] (O5). TPM ●● for INT publishing/content JDs.` | [CONF 2026-10-17] | ✅ · O5 | TEKsystems 简历 Achievement 5 已使用 |
| **A2** | ADD | 03 X-02，新增一条 bullet | （无） | `- Work closely with teams in India, Thailand and Indonesia across time zones (collaboration, not line management) ✅[CONF 2026-10-17].` 安全措辞：*"Work closely with teams in India, Thailand and Indonesia across time zones."* | [CONF 2026-10-17] | ✅ · 协作 | TEKsystems 简历 Summary、能力表、UOB 段已使用 |
| **A3** | RESTRICT | fact-check §0 决策日志，新增 D-09 | （无） | `D-09 \| 2026-10-17 \| No direct collaboration with US-based teams at UOB; no other US-team collaboration on record. Do not claim US-team experience; JDs asking for it show it as a gap. \| 05 §5 matrix use` | [CONF 2026-10-17] | — | 防止日后的简历把"和美国团队协作"写进去 |
| **A4** | ADD | 03 X-02，新增一条 bullet | （无） | `- When the two platform lines' schedules conflict, agree MVP scope with the requirement, project and technical leads, confirm dependencies, then set a sequence all parties accept ✅[CONF 2026-10-16].` | [CONF 2026-10-16]（另一会话的确认，本次请你复核） | ✅ · O3 | TEKsystems 简历 UOB 段已使用 |
| **A5** | CLARIFY | 03 §2 PA-08 | `Ownership O1/O2 ❓ · Time saved ❓` | `Ownership O1 — personally wrote the agent ✅[CONF 2026-10-16] · Built Apr 2026 ✅[CONF 2026-10-16] · Time saved ❓` | [CONF 2026-10-16] | ✅ · O1 | 措辞不变（本来就写 "Built"） |
| **A6** | CLARIFY | 03 PA-07 §8；§6.2 C4 | `Adoption and go-live ❓ (C4)` | `Go-live May 2026, after formal architecture and risk approval ✅[CONF 2026-10-16] · Adoption scope (all 25?) and own-initiative ❓ (C4 remainder)` | [CONF 2026-10-16] | ✅ | C4 只关闭一半 |
| **A7** | ADD | skills inventory §11 | `Jira ✅ · Confluence ✅ · MS Project ✅ [LIB] · …` | `… · Miro ✅ — used at VV Technology (2019–20), Golden Bridge (2020–22) and UOB (2022– ) [CONF 2026-10-17]; use case ❓ (B4)` | [CONF 2026-10-17] | ✅ · P（工具使用） | 能力表可以合规列出 Miro |
| **A8** | CORRECT（**须 B1 = Y**） | 03 PA-10.3、PA-11.1 safe wording；§0A 两行 | PA-10.3：`Built and led a {40-person — OQ-2.3} project team, …`；PA-11.1：`Built VV's technology organisation{ of 140 — OQ-2.3} and its microservices platform …` | PA-10.3：`Led a 40-person project team (total headcount), introduced Agile/Scrum from scratch …`；PA-11.1：`Led VV's 140-person technology organisation (total headcount) and built its microservices platform (…) from scratch, owning technology selection and the technology budget.`；§0A：两行改为 `✅ total headcount; direct reports ≤ 15–20 [CONF]`；HR-3 / HR-9 / OQ-2.3 关闭 | HR-9 规则 + B1 | ✅ | 与 TEKsystems 简历一致 |
| **A9** | CLARIFY（关闭 FU-6） | 02 §1 姓名行；04 §5；fact-check FU-6 | `… ⚠️ — surname question FU-6 still open` | `✅ "Wilson" only, no surname, on resume headers [CONF 2026-10-17]; legal name Zhang Heng on forms. FU-6 closed.` | [CONF 2026-10-17] | ✅ | 今后的模板抬头统一用 "WILSON" |
| **A10** | 通用版式规则 | 04 §4 | （Earlier Experience 只写年份，沿用 [TPL]） | `Earlier Experience entries show Mmm YYYY – Mmm YYYY from 02 §2 (ATS date parsing; style review §4).` | Resume_Style_Review §4 | — | 只改版式规则，不涉及事实 |
| **A11** | 决策（关闭 FU-5 的写法部分） | fact-check FU-5 → D-10 | FU-5：三种写法待选 | `D-10: resumes show Hengshunyuan as Oct 2017 – Sep 2019 (option a), overlap with VV not annotated; dormancy explained at interview.` | [CONF 2026-10-17] | — | 日期本身的依据见 B3 |

---

## B. 需要你回答的问题（⚠ = 背调敏感，需要原始依据）

| # | 问题 | 不回答时的默认处理 |
|---|---|---|
| **B1 ⚠** | GBD 40 人、VV 140 人都是**总编制**、你的直接下属最多 15–20 人，这是 10-16 在另一个会话确认的。依据是什么（组织架构图、offer letter、内部邮件，还是你的记忆）？ | OQ-2.3 保持 ❓；A8 不执行；TEKsystems 简历里的 "(total headcount)" 写法列入 D 组 |
| **B2 ⚠** | 职称：VV "Head of Technical Centre"、AI Park "VP of Technical Department"。你在 10-15 确认的是 "…Development"。哪份文件上是现在这个写法（雇佣信、合同、名片、离职证明）？ | CF-16 继续保持 ⚠️，把 10-17 的选择记为第三个数据点；02 / 03 职称行不改 |
| **B3 ⚠** | 日期依据：AI Park 起始月 2016 年 4 月（[R22] 写的是 5 月）；恒顺源 2017 年 10 月 – 2019 年 9 月（[R22] 写的是 2018 年 3 月 – 2019 年 8 月）。依据是社保记录、工商登记还是合同？ | CF-06、CF-05 维持"默认 A，未核原件" |
| **B4** | Miro 在这三家公司具体用来做什么（流程梳理、头脑风暴、复盘、架构图）？ | A7 只写"用过"；TEKsystems 简历里 "Workflow mapping in Miro" 列入 D 组 |
| **B5** | GBD "KYC supporting 200+ countries" 是指**设计上的覆盖能力**（不是实际用户分布）吗？确认的话就关闭 CF-11，§0A 改为 📄 | §0A 维持 ⚠️；PA-10.2 用时不带数字 |
| **B6** | SQL、RHEL 的雇主锚点（UOB？更早的哪家公司？） | skills 里锚点仍为 ❓，简历技能行不列这两项 |

---

## C. 只能记为推断，或不入库

| # | 内容 | 原因 |
|---|---|---|
| C1 | "25 = 两个团队合计"（TU-07） | 已在 03 X-02（CEW 15 + CCD 10）✅，重复 |
| C2 | Baidu / Sohu / Renren 的月份（TU-09） | 已在 02 §2 [R22]，重复（只保留 A10 的版式规则） |
| C3 | "用 Miro 做 workflow mapping" | 用途属于推断，等 B4 |
| C4 | "通过美国的技术支持团队与美国协作" | 你已澄清没有直接对接，不作为事实入库，只登记 A3 限制 |
| C5 | 简历措辞（"flagship programme"、"Multi-programme delivery" 等） | 是简历写法，不是事实 |

---

## D. 可能影响已投递简历的更正

扫描了 `applications\`，目前只有 `2026-10-17_TEKsystems_Program-Manager` 一个申请。

| 优先级 | 简历原句 | 依赖 | 如果结果不是 Y |
|---|---|---|---|
| 🔴 高（背调） | VV *"Head of Technical Centre"*、AI Park *"VP of Technical Department"* | B2 | 职称必须与雇佣信一致，否则背调不过 |
| 🔴 高（背调） | *"Led a 40-person project team (total headcount)"*、*"Led VV's 140-person technology organisation (total headcount)"* | B1 | 改回不带人数的写法 |
| 🟠 中 | *"Workflow mapping in Miro"* | B4 | 改成 "Miro" 或换成实际用途 |
| 🟢 低 | Sohu 发布流程、亚太协作、MVP 排序 | A1 / A2 / A4 | 如果你选 N，要从简历删除 |
| 🟢 信息 | `templates\wilson-2026_TPM_Bank_template.docx` 仍是旧职称 "…Development" | B2 | 模板只作版式参考，不是事实源；B2 = Y 时建议同步更新 |

---

## 未采纳（审批后填写）

| # | 你的决定 | 日期 |
|---|---|---|
| — | — | — |
