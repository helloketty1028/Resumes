# Fact Library Change Log — 可读性标准 + OQ-R1 / OQ-R2

**日期**：2026-10-20 · **依据**：`Fact_Library_Update_Review.md` 及 Wilson 的逐项决定 · **快照（修改前原样）**：`master\v2.0-draft\archive\snapshot_2026-10-20_readability-standard\`（01、04、fact-check）

## 已应用

| 文件 | 版本 | 章节 | 改动 |
|---|---|---|---|
| 01_Resume_Master_Rules.md | v1.0 → v1.1 | §6 Spelling 行 | 英式拼写（新加坡标准），JD 目标职位名按原文引用；✅，OQ-R1 关闭（RD-01、RD-02） |
| | | §6 Summary length 行 | 约 3 个短段（≈⅓ 页）；取代 "about one page"；✅，OQ-R2 关闭 |
| | | §6 Bullets 行 | 一条一事；目标 2 行、上限 3 行（约 1/5 可到 3 行）；结果在前、技术在后；每条 ≤3–4 个技术名词（RD-04） |
| | | §6 Numbers 行 | 每条 1–2 个数字；人数用安全写法 HR-9（RD-04） |
| | | §6A（新增） | 三类读者；首页回答三问；通俗语言（RD-03） |
| | | §9 清单一行 | "British spelling consistent (§6); JD role titles quoted as written." |
| | | §11 | OQ-R1、OQ-R2 原位标 ✅ Closed，保留原问题；OQ-R3 仍未决 |
| | | §12 | 新增 v1.1 行 |
| 04_Resume_Layout_Spec.md | v1.1 → v1.2 | §3A（新增） | 可读性限值表 🔶（RD-06） |
| | | §6 | 新增一行：渲染 PDF 的限值与首页构成检查 |
| | | §8 | 新增 v1.2 行 |
| fact-check-and-open-questions.md | v2.3 → v2.4 | §0 | 新增 D-12（拼写）、D-13（可读性标准）、D-14（Summary 长度） |
| | | §0A | `01 §11` 行更新为各 OQ 的最新状态 |
| | | §7 | 新增 v2.4 行 |

**未改动**：02、03、05、skills inventory；未删除任何内容。

## 校验

- 回读三个文件的改动区域，表格与标题结构完好；行尾与快照一致（LF）。
- 与快照逐行比对：01 只有 8 行被替换，04 只有版本行被替换，fact-check 只有版本行与 §0A 一行被替换，其余均为新增。
- 全库搜索 `OQ-R1`、`OQ-R2`、"one page"：除已关闭的记录外，无遗留的矛盾表述。

## 回归检查

- **拼写**：已投的 TEKsystems、Talentvis 以及模板、6 份 LIB 均无美式 -ize；`TPM_Internet_LIB_V5` 用美式 "program"（26 次），以后从它取材要改为 "programme"（软件含义与 JD 职位名除外）。
- **Bullet 长度**（pdftotext 近似）：TEKsystems 33 条 = 1 行 9 / 2 行 17 / 3 行 6 / 4 行 1；Talentvis 38 条 = 5 / 21 / 11 / 1。按新规则，TEKsystems 需处理 1 条 4 行；Talentvis 需处理 1 条 4 行并压缩约 3–4 条 3 行。
- **首页构成**：两份都已满足 04 §3A（Summary、Core Competencies、Selected Achievements 均在第 1 页）。
- **段落限值**（04 §3A，4 行）：两份的 Summary 第一段分别为 5 行和 6 行，超过限值；两份的 Summary 末尾都有只剩一个词的末行。已投简历不追改；该限值是 🔶，按下一次渲染结果再确认。
- 不涉及任何事实、Metrics Bank、02、03、skills。
