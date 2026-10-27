# Fact Library Change Log — Interview Bank 回灌（已确认条目）

**日期**：2026-10-26 · **依据**：`Fact_Library_Update_Review.md` 及你的决定（A1–A10 Y、A11 E"通知期统一一个月"、A12–A13 Y；B1–B9 未答 → 默认）
**快照（修改前原样）**：`master\v2.0-draft\archive\snapshot_2026-10-26_interview-bank-backfill\`（02、03、fact-check、skills、05）

## 已应用

| 文件 | 版本 | 章节 | 改动 |
|---|---|---|---|
| 03_Achievement_Library.md | v4.2 → v4.3 | §0A | 第 2 行注明工程师来自四家供应商（A6）；新行：事件指挥时间目标（A5，标明是目标不是结果） |
| | | §1 | PA-20 行 → "⛔ retired 2026-10-26 (D-16)"，期间改为 "2020 – before Oct 2022" |
| | | PA-01 §2 / §3 / §6 / §10 | hub 防重复与重试设计（A1）；MQ（产品 ❓）；付款与 entitlement 数据迁移（A2）；MT/MX 共存期对账，归属 ❓（A3）；3 条面试角度 |
| | | PA-01 表格 | 新增 PA-01.8 safe-retry design、PA-01.9 entitlement-data migration |
| | | PA-07 §5 / §6 / 表格 | 运行控制 4 项入库、4 项挂起（OQ-5.3）；新增 PA-07.7 |
| | | PA-11 §6 / §7 / §10 / §13 / 表格 | 0-to-1 方法（A9）；"用户留下来了"（定性）；新 §13 表现不佳负责人案例（A10）；新增 PA-11.6、PA-11.7（仅面试） |
| | | X-01 | 指向 PA-01.9 |
| | | X-02 | 工程师来自供应商；"performance management" 范围 ❓ OQ-5.5；需求冲突案例；两条 safe wording；面试答法（不说 "hired"） |
| | | X-05 | 注明所带工程师来自这些供应商 |
| | | X-06 | 脱敏 P1 案例（修复归属 slot）；事件指挥做法；可选 safe wording；面试行改为指向该案例 |
| | | PA-20、§5.3、新 §5.5 | Pureland 退役，原卡片保留；新增 Retired items 表 |
| | | §5.4 | 新增 v4.3 行 |
| 02_Candidate_Profile.md | v3.1 → v3.2 | §1 | 新行 Notice period = **One month** ✅[CONF 2026-10-26]，早先"两个月可缩到一个月""约两周"列为 superseded |
| | | §2 行 2、时间线、§6.2 | Pureland：May 2020 [LIB] – ended before Oct 2022；标为"已从工作经历移除"，正文保留 |
| | | §10 | 新增 v3.2 行 |
| fact-check-and-open-questions.md | v2.5 → v2.6 | §0 | 新增 D-16（Pureland）、D-17（本轮入库清单） |
| | | §0A | 索引新增 Batch 5 |
| | | §2 | 新增 CF-17 – CF-27 |
| | | §3 / §5 | TL-4、OQ-1.8 关闭 → D-16 |
| | | §4 | 新增 HR-11 – HR-15；表后加"面试中重复出现"汇总注记 |
| | | §5 | 新增 Batch 5：OQ-5.1 – OQ-5.31 |
| | | §7 | 新增 v2.6 行 |
| technical-skills-inventory.md | v2.3 → v2.4 | Spring Batch 行 | 加 UOB hub 迁移锚点（PA-01.9），深度不变 |
| | | 8 处 Pureland 锚点 | 注记 "removed from work history — not citable, D-16"，深度不变 |
| | | §13 | 新增 v2.4 行 |
| 05_JD_Keyword_and_Matching_Rules.md | v1.0 → v1.1 | §6 可见性规则 | Pureland 从 `on-request` 改为 Never |
| | | §12 | 新增 v1.1 行 |

**与审查文件的两处实现差异（如实说明）**
1. skills inventory 中 Pureland 实际出现 **8 处**（审查文件写 7 行；第 8 处在 §134 支付领域清单行），全部按同一方式加注。
2. "面试中重复出现的已有条目"没有逐行追加，而是在 fact-check §4 表后加了一段汇总注记（信息相同；03 §0A / X-04 未改动）。

**未改动**：01、04；Interview Bank 下任何文件；旧申请目录下任何简历。没有删除任何内容。

## 校验

- 与快照逐行比对：02 −4 / +7；03 −14 / +44；fact-check −3 / +65；skills −10 / +11；05 −2 / +4（"−" 均为被就地改写的行，无内容被删除）。
- 残留检查为空：`⛔ until disclosure`、`May 2020 – Present`、`2020.5 → present`、`on-request only: Pureland`、`generic flow only`。
- 新 ID 唯一：PA-01.8、PA-01.9、PA-07.7、PA-11.6、PA-11.7、D-16、D-17、CF-17 – 27、HR-11 – 15、OQ-5.1 – 5.31；03 中引用的 OQ-5.1 / 5.2 / 5.3 / 5.4 / 5.5 / 5.7 / 5.8 在 fact-check 均能找到。

## 回归检查（不自动改旧简历）

| 优先级 | 影响 | 申请 | 原句 | 建议 |
|---|---|---|---|---|
| 🔴 高 | SB-12 / OQ-5.5 | Talentvis、Airwallex、Landi、NETS、PrivateAdvertiser、Stripe | "…squad leads and engineering managers, with 1:1s, mentoring and performance management" | 已投递不改；面试被问绩效时按真实情况答（工程师来自供应商）。OQ-5.5 回答前，新简历不写 "performance management" |
| 🟢 无影响 | SB-12 | 全部 12 份 | "Lead 25 onshore and offshore engineers"、"four IT service vendors" | 仍准确 |
| 🟢 无影响 | SD-20 | 全部 12 份 | — | docx 文本无 Pureland |
| 🟠 中 | SD-20 | LinkedIn | 仍显示 Pureland | 按你的决定暂不改；面试答法见 D-16 |
| 🟠 中 | SB-05 | Singtel（面试 2026-10-23） | "about 2 weeks" | 下次联系时更正为"一个月" |
| 🟢 无影响 | CF-17 | 全部 12 份 | "ahead of SWIFT's November 2025 deadline" | 与 03 一致；冲突仅在口述 |

---

# 补充轮 — 2026-10-27（R1、R2a、R3、R5；R4 维持现状）

**快照**：`master\v2.0-draft\archive\snapshot_2026-10-27_oq-answers\`（03、fact-check）

| 文件 | 版本 | 章节 | 改动 |
|---|---|---|---|
| 03_Achievement_Library.md | v4.3 → v4.4 | X-02 | squad lead 来自供应商 ✅；供应商人员的 "performance management" = 需求开发、进度、交付、上线、事件处理全过程的表现评估 ✅；解除新简历的用词限制；EM 是否来自供应商仍 ❓ OQ-5.5；面试答法 +1 |
| | | PA-07 §6、PA-07.7 | 模型端点 = in-region on AWS, private dedicated connection ✅；"无外网访问 / 代码不出行"仍挂起，并注明原表述与 AWS 端点不符 |
| | | §5.4 | v4.4 行 |
| fact-check-and-open-questions.md | v2.6 → v2.7 | §0 / §2 / §5 / §7 | D-18；CF-22 关闭（CCD 10 + CEW 15）；OQ-5.3、OQ-5.5 部分关闭并改写剩余问题；v2.7 行 |

**未改动**：02、skills、05（Pureland 按 (a) 维持"已退役、保留档案"）。没有删除任何内容。
**校验**：与快照比对 03 −5 / +6，fact-check −4 / +6（"−"都是就地改写的行）。

**回归更新**：6 份写有 "1:1s, mentoring and performance management" 的简历（Talentvis、Airwallex、Landi、NETS、PrivateAdvertiser、Stripe）由 🔴 降为 🟢——措辞成立，面试按 X-02 的口径回答。

---

# 补充轮 2 — 2026-10-27（直接回复，即视为批准）

**快照**：`master\v2.0-draft\archive\snapshot_2026-10-27b_oq-answers\`（03、fact-check）

| 文件 | 版本 | 改动 |
|---|---|---|
| 03_Achievement_Library.md | v4.4 → v4.5 | X-02：engineering managers = UOB 正式员工 ✅，面试答法同步；PA-07 §6：网络控制改写并确认（无公网访问，唯一出口是到模型端点的专线，代码不经公网）；rejection rate 记为"尚无数据，目前观察约为零"（观察值，不出简历）；PA-07.7 加 "no public-internet access" |
| fact-check-and-open-questions.md | v2.7 → v2.8 | D-19；OQ-5.3 只剩"误报抑制怎么做"；OQ-5.5 只剩"EM 是否计入 25 人" |

**未改动**：02、skills、05。没有删除任何内容。

---

# 补充轮 3 — 2026-10-27（OQ-5.5、OQ-5.3 关闭）

**快照**：`master\v2.0-draft\archive\snapshot_2026-10-27c_oq-answers\`（03、fact-check）

| 文件 | 版本 | 改动 |
|---|---|---|
| 03_Achievement_Library.md | v4.5 → v4.6 | §0A 第 2 行、X-02：EM 是 UOB 正式员工，不计入 25 人；PA-07 §5 / §6：PoLP + SoD 框架、按任务的临时授权、URL allowlist（只含模型端点）+ 限速 ✅；工具调用前置检查记为**未实现，不得声称**；误报处理 = 一个 squad 试点、按反馈调 prompt、再推广 ✅；§10 新增 2 条面试角度 |
| fact-check-and-open-questions.md | v2.8 → v2.9 | D-20；OQ-5.3、OQ-5.5 关闭；OQ-5.12 部分回答 |

**未改动**：02、skills、05、简历措辞（PA-07.7 不变）。没有删除任何内容。
