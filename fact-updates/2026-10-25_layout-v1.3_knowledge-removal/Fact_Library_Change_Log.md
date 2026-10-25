# Fact Library Change Log — 04 v1.3 版式更正 + 移除 Project Knowledge 副本

**日期**：2026-10-25 · **依据**：Wilson 的决定："从 Knowledge 移除，只用本地文件" · **快照（修改前原样）**：`master\v2.0-draft\archive\snapshot_2026-10-25_layout-v1.3\`（04、prompts 01、prompts 02）

## 已应用（本地）

| 文件 | 版本 | 章节 | 改动 |
|---|---|---|---|
| 04_Resume_Layout_Spec.md | v1.2 → v1.3 | §1 Page breaks 行 | 0 个手工分页符；PROFESSIONAL EXPERIENCE 标题有 1 个强制分页（`pageBreakBefore`） |
| | | §2 Employer accent 行 | teal `156082` 在 [TPL] 中绑定 `themeColor=accent1`（13 个 run）→ 写死色值 |
| | | §2 Title line text 行 | `404040` 只用在 UOB 和 Golden Bridge；VV、AI Park 为自动色，标 ⚠️ |
| | | §3 Title line、Sub-heading 行 | title 行为斜体；子标题为粗斜体 |
| | | §3 keep-with-next 段 | 按实测改写：11 段 = 各节标题 + 雇主行 + 1 个空 spacer（P022）；title 行和子标题按 🔶 标准补加 |
| | | §8 | 新增 v1.3 行 |
| prompts/01_JD_Resume_Tailoring.md | — | §2 规则 3、§7 第 5 项 | 改为只用本地文件；Knowledge 不再存放副本；汇报改为列出实际读取的本地文件 |
| prompts/02_Fact_Library_Maintenance.md | — | §7 最后一条 | 不再同步到 Knowledge |
| master/v2.0-draft/reference/（新增） | — | — | `Resume_Layout_Spec_v2.0.md`、`Resume_Style_Review_2026-10-16.md`：从 Knowledge 原样另存，只作参考 |

**验证方法**：4 处更正都直接对照 `templates\wilson-2026_TPM_Bank_template.docx` 的 `word/document.xml` 复核过（分页、斜体、keepNext、颜色），不是照抄 v2.0。v2.0 中"`404040` 只用于 UOB"有误（Golden Bridge 也用），已按实测修正。

**未改动**：01、02、03、05、fact-check、skills inventory；没有删除任何本地内容。

## 已应用（claude.ai Project「Career & Resume」→ Knowledge）

删除全部 11 份文档，Knowledge 现为 0：
`master/Wilson_Master_Career_Profile.md`、`master/project-achievement-library.md`、`master/Resume_Layout_Spec.md`、`master/Resume_Style_Review.md`、`master/01_Resume_Master_Rules.md`、`master/02_Candidate_Profile.md`、`master/03_Achievement_Library.md`、`master/04_Resume_Layout_Spec.md`、`master/05_JD_Keyword_and_Matching_Rules.md`、`master/fact-check-and-open-questions.md`、`master/technical-skills-inventory.md`

## 事件记录

- 2026-10-25 执行过程中发现本地 `archive\Wilson_Master_Career_Profile_v1.0.md`、`archive\project-achievement-library_v2.1.md` 已从磁盘消失。原因：Wilson 在资源管理器中手动删除（2026-10-25 确认，属有意操作）。执行中曾用 `git show HEAD:<path>` 恢复，需再次删除，并在提交时记为删除。
- 之后每删一批 Knowledge 文档都校验本地 sha1，均未受影响，确认 Knowledge 删除不会连带删除本地文件。

## 待办

- [ ] 手动修改 Project Instructions §2：现在仍写着"consult the Project Knowledge files"，需改为指向本地路径（替换文本见会话回复）。
- [ ] 视需要在 fact-check 的决策日志里登记一条 D-15（Knowledge 移除 + 04 v1.3）。
- [ ] 提交 Git（本次改动尚未提交）。
