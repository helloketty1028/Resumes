# Fact Library Update Review — 可读性标准 + OQ-R1 / OQ-R2

**日期**：2026-10-20 · **场景**：回答未决问题 + 新增规则 · **状态**：✅ 已按你的决定应用（2026-10-20）— 见 `Fact_Library_Change_Log.md`
**来源**：Wilson 2026-10-20 答复 — (1) 拼写：新加坡职场用什么就用什么；(2) 可读性标准写入 01 §6 和 04 [CONF 2026-10-20]
**读取的文件**：01_Resume_Master_Rules v1.0 · 04_Resume_Layout_Spec v1.1 · fact-check-and-open-questions v2.3 · 05（只读，核对 §6 排序规则与新规则无冲突）· 已投递的两份简历（TEKsystems、Talentvis）及 11 份 docx 的拼写扫描

---

## A. 可批准的更新

| ID | 类型 | 目标 | 内容 | 证据 | 状态 |
|---|---|---|---|---|---|
| RD-01 | CLARIFY（关闭 OQ-R1） | 01 §6 Spelling 行；§9 清单一行；§11 OQ-R1 行 | 拼写 = 英式（新加坡标准） | [CONF 2026-10-20]；Standard Singapore English 采用英式拼写（见下）；现有 11 份 docx 的扫描结果 | ✅ |
| RD-02 | ADD（我的提议） | 01 §6 Spelling 行（追加一句）；§9 清单 | JD 里的目标职位名按原文引用，其余仍英式 | TEKsystems 简历 headline 已是 "Senior Program Manager — Multi-Programme Delivery" | 🔶 待你决定 |
| RD-03 | ADD | 01 §6A（新增） | 三类读者；首页回答三问；通俗语言 | [CONF 2026-10-20] 采用可读性标准；措辞为我的提议 | ✅ 采用 / 🔶 措辞 |
| RD-04 | CLARIFY | 01 §6 Bullets 行、Numbers 行 | Bullet 长度与结构、数字个数的阈值 | 已投两份简历的实测（见 D 组） | ✅ 采用 / 🔶 阈值 |
| RD-05 | ADD | 01 §8 第 3 项；§9 Document 清单 | 冷读测试 + 三条 QA 检查 | [CONF 2026-10-20]；属审查方法，归 §8 比 §6 更合适 | ✅ 采用 / 🔶 措辞 |
| RD-06 | ADD | 04 新增 §3A；§6 追加一行 | 版面可读性限值与渲染检查 | 已投两份简历的实测（见 D 组） | ✅ 采用 / 🔶 值 |

### A1. 精确文字

**RD-01 — 01 §6 Spelling 行**
- 现有：`| Spelling | British spelling (organisation, programme, optimise), as used consistently in [LIB] and [TPL] | 🔶 default — ❓ confirm (OQ-R1) |`
- 改为：`| Spelling | British spelling, the Singapore standard (organisation, programme, optimise, centre), consistent throughout a document [CONF 2026-10-20] | ✅ (OQ-R1 closed → D-12) |`
- 01 §9 现有：`- [ ] British spelling consistent (pending OQ-R1).` → 改为：`- [ ] British spelling consistent (§6).`
- 01 §11 现有：`| OQ-R1 | Confirm British spelling as the standard. |` → 改为：`| OQ-R1 | ✅ Closed 2026-10-20 → D-12: British spelling (Singapore standard). |`

**RD-02 — 追加到 Spelling 行末尾（依赖 RD-01）**
- 追加：`Exception: a target-role title quoted from the JD keeps the JD's spelling (e.g. "Program Manager") so title matching works; "program" in the software sense keeps its usual single-m form.`
- §9 清单改为：`- [ ] British spelling consistent (§6); JD role titles quoted as written.`

**RD-03 — 01 §6 表格之后新增**
```
### 6A. Readability standard — three readers [CONF 2026-10-20]

Every tailored resume is written for three readers at once: an **HR recruiter** (6–10-second screen, often not a technologist), a **hiring manager** (2–3 minutes: fit, credibility, red flags) and an **ATS** (parseable text, honest keywords).

1. **Page 1 answers three questions** — who he is (level and domain), what scale he has worked at, and why he fits this role. The headline is one line naming the target-role positioning (02 §7); the Summary's first sentence speaks to the JD's core requirement; Core Competencies are ordered by the JD's Required priorities and use the JD's own term only where the evidence supports it (05 §5). Each of the JD's top five Required items that the record supports has visible evidence on page 1 (Summary, Core Competencies or Selected Achievements); gaps are never disguised (05 §7).
2. **Plain for non-specialists.** Expand an industry acronym at first use (e.g. CBPR+, ISO 20022 MT→MX). Translate internal terms into common ones (§7). No filler adjectives (results-driven, passionate, dynamic), and no restating the same point in two places (§6 Merging).
```

**RD-04 — 01 §6 两行**
- Bullets 现有：`| Bullets | Action + context + supported result; quantitative or qualitative evidence both valid; no generic claims; no technology dumps | ✅ |`
- 改为：`| Bullets | Action + context + supported result; quantitative or qualitative evidence both valid; no generic claims; no technology dumps. One idea per bullet. Target two rendered lines (≈30 words); a third line only when needed to keep a locked wording or qualifier (§4, 03 §0A) or a headline metric; never more than three, and no more than about one bullet in five at three lines. Scale or result first, technology last; at most 3–4 named technologies per bullet | ✅ · limits 🔶 |`
- Numbers 现有：`| Numbers | Only from 03 §Metrics Bank with its attribution; keep "~", "estimated", "internal measure" qualifiers | ✅ |`
- 改为：`| Numbers | Only from 03 §Metrics Bank with its attribution; keep "~", "estimated", "internal measure" qualifiers. At most 1–2 numbers per bullet, each quick to grasp (scale, time, %); headcount only in the safe wording (HR-9) | ✅ |`

**RD-05 — 01 §8 与 §9**
- §8 第 3 项现有：`3. **Document quality** — readability, extractable text, layout per 04; list checks passed, issues found, checks not performed.`
- 改为：`3. **Document quality** — readability (§6A), extractable text, layout per 04; list checks passed, issues found, checks not performed. Readability includes the cold-read test below.`
- §8 末尾新增：
```
**Cold-read test (readability evidence, not factual evidence).** An independent reviewer that has the rendered PDF and the JD — and no access to the fact library or the drafting process — reads the resume first as an **HR recruiter for 30 seconds**, then as a **hiring manager for about 3 minutes**, and answers: who this is and at what level; the three strongest matches to the JD; the biggest doubt; which sentences are unclear or too technical; whether they would interview. Revise if the recruiter cannot name three matches or flags more than two unclear sentences. Findings change wording, order and length only; they never add facts — a suggestion that would need a new fact becomes a back-fill candidate for Wilson to decide. The reviewer simulates the two readers; it does not replace real feedback. No score is produced (D-03).
```
- §9 Document 块新增三行：
```
- [ ] Page 1 answers who / what scale / why this role; the JD's supported top-five Required items are visible on page 1 (§6A).
- [ ] Acronyms expanded at first use; no filler adjectives; bullet length within the §6 limits.
- [ ] Cold-read test run on the rendered PDF and reported — or stated as not performed (§8).
```

**RD-06 — 04**
- §3 末尾（"Keep-with-next on: …" 段之后、§4 之前）新增：
```
### 3A. Readability limits (checked on the rendered PDF) 🔶 [CONF 2026-10-20]

| Item | Limit |
|---|---|
| Bullet | Target 2 rendered lines at 9.5 pt / 18.0 cm; 3 lines only as allowed in 01 §6 (Bullets); never more than 3; no more than about 1 bullet in 5 at 3 lines |
| Paragraph | Summary and role-scope paragraphs: at most 4 rendered lines each; no text block longer than 4 lines anywhere |
| Page 1 | Header, headline, Summary, Core Competencies and Selected Achievements all start on page 1 |
| Headings | Never alone at the foot of a page (keep-with-next, §3) |
```
- §6 Export and Checks 追加一行：
`- Check on the rendered PDF: bullet and paragraph limits (§3A), page-1 composition (§3A), page count ≤ 3, page numbers, heading orphans. State any check not performed.`

---

## B. 需要你回答的问题

| ID | 问题 | 证据 | 不回答时的默认 |
|---|---|---|---|
| RD-02 | JD 里的目标职位名要不要按原文引用？ | 一行 headline 里已出现 "Program Manager" 与 "Programme Delivery" 并存 | 不写入（保持现状，不加例外） |
| OQ-R2 | Summary 长度：约 3 个短段，还是约一页？ | 已投两份简历的 Summary 都是约 12–13 行（≈⅓ 页），首页放下了 Summary + Core Competencies + 7 条 Selected Achievements。你早先的偏好写的是 "about one page" | 保持 ⚠️ 未决 |
| OQ-R3 | 文件命名带 `[Lens]` 段是否确认？ | 两份申请都已按 `wilson-2026_[Family]_[Lens]_[Company]_V1_0_0` 命名 | 保持 🔶 未决 |

## C. 不入库 / 仅推断

- 阈值本身（≈30 words、3 行上限、约 1/5、3–4 个技术名词、30 秒 / 3 分钟）是我基于实测的提议，不是你确认过的事实；批准后只作为 🔶 规则，不是 ✅。
- "新加坡职场的拼写"：没有找到官方的职场强制标准。Standard Singapore English 采用英式拼写（Wikipedia）；学校以英式为教学标准，美式在一致使用时也被接受（NUS IPS 论文）。所以写入的是"英式，新加坡标准，文内一致"，不写成"职场规定"。
- 冷读评审是模拟读者的代理，不等于真实 HR 的反馈，已在 RD-05 文字里写明。

## D. 回归检查（已执行）

- **拼写扫描**：11 份 docx（6 份 LIB、模板、两份申请的终稿与草稿）都没有 -ize 类美式拼写。美式 "program" 只出现在两处：`TPM_Internet_LIB_V5`（26 次，素材库）与 TEKsystems 的 headline（JD 职位名）。已投简历不需要更正；以后从 `TPM_Internet_LIB_V5` 取材时要把 "program" 改成 "programme"（软件含义与 JD 职位名除外）。
- **Bullet 长度实测**（pdftotext 近似）：TEKsystems 33 条 = 1 行 9 / 2 行 17 / 3 行 6 / 4 行 1；Talentvis 38 条 = 1 行 5 / 2 行 21 / 3 行 11 / 4 行 1。若严格要求 ≤2 行，两份要裁 7 条和 12 条；按 RD-04 的"3 行上限 + 约 1/5"，TEKsystems 只需处理 1 条 4 行（3 行占 18%），Talentvis 要处理 1 条 4 行并压缩约 3–4 条 3 行（占 29%）。因此 RD-04 采用 3 行上限而不是 2 行硬限。
- **首页构成**：两份简历第 1 页都已包含 Summary、Core Competencies、Selected Achievements（7 条），RD-06 的 Page 1 条款已满足。
- 不涉及 02、03、skills inventory、Metrics Bank，不影响任何事实或已投简历内容。

## E. 随批准项自动应用的记录更新

- 快照：`master\v2.0-draft\archive\snapshot_2026-10-20_readability-standard\`（01、04、fact-check 修改前原样）
- 01：v1.0 → v1.1，change log 新增一行
- 04：v1.1 → v1.2，change log 新增一行
- fact-check：v2.3 → v2.4；Decision Log 新增 D-12（拼写）、D-13（采用可读性标准）、D-14（OQ-R2，仅在你回答后）；§0A 索引中 `01 §11` 一行更新为各 OQ 的最新状态；change log 新增一行
- 所有"关闭"一律原位标注 ✅ Closed，不删除历史

## F. 批准并应用之后（不属于事实库）

- 把工具 A（`01_JD_Resume_Tailoring.md` §4–§5）与工具 C（`03_JD_Batch_Analysis_and_Tailoring.md` §4）改为引用 01 §6A / §6 / §8 与 04 §3A，去掉工具 C 里重复的一份标准，只保留批量场景特有的调度。
- 询问是否把更新后的 01、04、fact-check 同步到 claude.ai Project 里的同名文件（未经你同意不同步）。

---

## G. 决定记录（2026-10-20，AskUserQuestion）

| ID | 你的决定 | 结果 |
|---|---|---|
| RD-01 | Y | 已写入 01 §6 / §9 / §11；OQ-R1 关闭（D-12） |
| RD-02 | Y（按原文引用） | 已并入 01 §6 Spelling 行与 §9 清单 |
| RD-03 | Y | 已写入 01 §6A |
| RD-04 | Y | 已改写 01 §6 Bullets 与 Numbers 行 |
| RD-05 | 未勾选 → 默认 N | 未写入；仍是提议（见 Open_Questions_Summary.md） |
| RD-06 | Y | 已写入 04 §3A 与 §6 |
| OQ-R2 | 约 3 个短段 | 已改 01 §6 Summary length 行，OQ-R2 关闭（D-14） |
| OQ-R3 | 未问 | 保持未决 |
