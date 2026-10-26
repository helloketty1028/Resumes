# Fact Library Update Review — UOB 发布前变更审批（CRQ / CAB）

**日期**：2026-10-26 · **场景**：我补充的新事实 · **状态**：✅ 已按你的决定应用（2026-10-26）— 见 `Fact_Library_Change_Log.md`
**来源**：Wilson 2026-10-26 原话："在 UOB，每次 PI 前的预上线流程中，我亲自准备 CRQ，并出席在 CAB 讲解上线计划、风险控制等" [CONF 2026-10-26]
**读取的文件**：03_Achievement_Library v4.1（PA-01、PA-03、X-02、X-04、X-06）· fact-check-and-open-questions v2.4 · 02 v3.1（只读）· applications\ 下各申请的审计文件与简历

---

## 差异识别

| 临时 ID | 类型 | 关联现有 ID | 现有表述 | 建议 | 图标 | 所有权 | 目标 |
|---|---|---|---|---|---|---|---|
| A1 | ADD | PA-03（发布治理）；相邻 PA-01 §6 "Agile governance with change control" [LIB] | 03 只有 "CI/CD release governance and SIT/UAT sign-off"、"change control"，**没有个人亲自做 CRQ / CAB 的记录** | 新增子成就 PA-03.5，并在 PA-03 §4、§9、§10 各补一处 | ✅ [CONF 2026-10-26] | 个人亲自执行（在 PA-03 现有 O3 + O4 之外） | 03 PA-03 |
| A2 | ADD | — | — | fact-check 登记决策 D-15 | — | — | fact-check §0 |

与现有事实**无冲突**：PA-01 §6 的 "change control" [LIB] 得到印证，但不升级它的状态（那条说的是治理框架，A1 说的是个人行为，两者分开记）。

---

## A. 可批准的更新

**A1 — 03 PA-03（v4.1 → v4.2）**

① §4 Responsibilities & decisions，句末追加：
> **Personally prepares the change request (CRQ) before every {release} and presents the go-live plan and risk controls at the Change Advisory Board (CAB)** ✅[CONF 2026-10-26].

② §9 Stakeholders：`architecture-review board` 后加 `, Change Advisory Board (CAB)`。

③ §10 Interview，追加：
> · "How do you get a high-risk change approved?" / "Walk me through your release approval process." → CRQ preparation, CAB presentation of go-live plan and risk controls.

④ 表格新增一行：
| PA-03.5 | Change approval — CRQ and CAB | CONF 2026-10-26 | ✅ | Personally prepare the change request for every {release} and present the go-live plan and risk controls to the Change Advisory Board. |

⑤ §5.4 change log 记一条 v4.2。

**写法说明**：只写你说的内容（go-live plan、risk controls）。原话里的"等"**不展开**：rollback、影响评估、回退方案等都没有写进去，你确认后才能加。"CRQ" 对外写成 "change request"，"CAB" 写全称；这两个是 ITIL 通用术语，不属于内部名称。

**A2 — fact-check（v2.4 → v2.5）**：§0 新增 D-15，内容为 "CRQ / CAB 个人职责确认，入 PA-03.5"，并记 change log。

---

## B. 需要你回答的问题（每条附不回答时的默认处理）

| ID | 问题 | 为什么要问 | 默认处理 |
|---|---|---|---|
| B1 | "PI" 指什么？(a) 每次生产发布 / production implementation；(b) SAFe 的 Program Increment；(c) 其他 | 决定 `{release}` 怎么写。SAFe 的 PI 是规划周期，不是一次上线；写错了面试时会被追问 | 写成 "every production release" |
| B2 | 范围：只有 CEW（跨境支付），还是 CEW + CCD 两条平台线都由你做 CRQ / CAB？ | 决定写成 "for the payment platform" 还是 "for both platform lines"；与 03 未决项 C6 同类 | 不写范围（不说 both） |

---

## C. 只能记为推断 / 不入库的内容

- 不推断 ITIL 认证或"ITIL change management"技能深度（skills inventory 不改）。
- 不推断 CAB 的频率、你的角色（presenter / requester，不是 CAB 成员或主席）、审批通过率。

## D. 可能影响已投递简历的更正

- 无更正。TEKsystems 简历第 29 条 "…change control…"（来源 PA-01 §6）与 A1 一致，不受影响；A1 只是让以后的 TPM 简历多一条可用证据。

---

## 决定

| ID | 决定 | 日期 |
|---|---|---|
| A1 | E — ① ④ 在 go-live plan、risk controls 之外追加 rollback plan、impact assessment、test results (SIT/UAT sign-off)、database changes；② ③ 按提议 | 2026-10-26 |
| A2 | Y（随 A1，D-15 文本按最终措辞） | 2026-10-26 |
| B1 | (a) 每次生产发布 → "every production release" [CONF 2026-10-26] | 2026-10-26 |
| B2 | CEW + CCD 两条平台线 → "for both platform lines" [CONF 2026-10-26] | 2026-10-26 |
