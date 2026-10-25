# Resume Style Review — `wilson-2026_TPM_Bank_template.docx`

**Date:** 2026-10-16
**Scope:** Format, presentation and how well ATS software can read the file. I made no content rewrites.
**Companion file:** `Resume_Layout_Spec.md` v2.0 (measured values and the fixed/adaptive rules).
**Checks performed:**
- Inspected the DOCX XML: styles, numbering, section properties, paragraph properties, table properties and metadata.
- Rendered the file to PDF with LibreOffice, which substitutes Carlito, a font metric-compatible with Calibri. The result was 3 pages, and I reviewed each page visually.
- Ran `pdftotext` to check the text-extraction order.

**Checks not performed:** rendering in Word itself, a parse through any real ATS (Workday, Taleo, SuccessFactors and so on), and printing.

---

## 1. Overall Verdict

The template's hierarchy is clean and conservative, the right style for a bank: navy section headings with a rule, teal employer lines, and a dense but readable 9.5 pt body. Page 1 works as a self-contained "one-page summary" of you. Its structure, typography and single-column flow should stay as they are.

There are three kinds of weakness:
1. **Leftover inconsistencies** from iterative editing: 3 heading treatments, mixed colours, and 2 empty spacer paragraphs.
2. **Narrow margins and no page numbers**, which you have already decided to change.
3. **File hygiene**: the stale metadata title and the theme-dependent colour.

None of these affects how a recruiter reads the content. All are cheap to fix once in a clean base file.

---

## 2. What Works — Keep

| # | Characteristic | Why it works |
|---|---|---|
| K1 | Single column, real text throughout, no text boxes, images or Word header content | Safe for ATS parsing. The extraction order matches the visual order (checked with `pdftotext`). |
| K2 | Page 1 as the summary zone, with a forced break before Experience | A recruiter gets the full pitch in one page, and pages 2–3 serve as the evidence. |
| K3 | Narrative summary in 3 paragraphs (identity → capability → technical depth) | Reads naturally, matches your preference, and keeps keywords in context. |
| K4 | Competency table with a shaded label column | Fast to scan. A simple 2-column grid with no merged cells keeps ATS risk low. |
| K5 | `Label:` + sentence bullets in Achievements and earlier roles | Gives the reader a scannable lead-in and places keywords naturally in the bold labels. |
| K6 | Sub-headings for the current role only | Breaks a 10-bullet role into readable themes without adding a heading level to older roles. |
| K7 | Right-tab dates on the employer line, in `Mmm YYYY – Mmm YYYY` format | Standard format that parsers read reliably and the eye scans easily. |
| K8 | One-line Earlier Experience entries | Covers about 8 years of history in 4 lines and keeps the document to 3 pages. |
| K9 | Restrained palette: navy and teal plus grey table rules | Looks professional when printed in greyscale. |

---

## 3. Issues Found (ranked)

| # | Severity | Issue | Evidence | Fix in the base file |
|---|---|---|---|---|
| R1 | **High (hygiene)** | The metadata Title reads `Wilson Zhang — Resume — MAS System Manager`. It would travel with every future application built from this file. `lastModifiedBy` = `zhang heng`, which differs from the name in the header. | `docProps/core.xml` | Clear the Title or set it for each JD. Clear the author fields, or set them to your chosen name. |
| R2 | Medium | Margins of 1.04/1.09 cm are tighter than most printers' safe area and look crowded. | `pgMar` 590/620 twips | ✅ Already decided: use 1.27 / 1.5 cm. |
| R3 | Medium | No page numbers on a 3-page document, so loose printed pages cannot be put back in order. | No footer part exists | ✅ Already decided: add a footer page number (format pending, OQ-L1). |
| R4 | Medium | Section headings use three different treatments: 14 pt, 12 pt, and 11 pt teal for EARLIER EXPERIENCE. | `sz` 28 / 24 / 22 | Use one size for all headings: 12 pt navy (OQ-L2). |
| R5 | Medium | Empty spacer paragraphs. P008 carries a heading rule and merges with the next heading's rule, adding about 20 pt of blank space above SELECTED ACHIEVEMENTS. P070 sits before Education. | Paragraphs with no runs | Delete both and rely on "spacing before". Hidden structure like this breaks when content length changes. |
| R6 | Low–Med | The teal employer colour is tied to `themeColor=accent1`. If the file is opened or pasted under a different Office theme, the colour changes silently. | 13 runs | Hard-code `156082` and remove the theme link. |
| R7 | Low | The headline is 134 characters and wraps, leaving "Governance" alone on line 2. | Render, page 1 | Keep it to ≤ 110 characters on one line. |
| R8 | Low | Inconsistent colour across roles. The UOB title line is `404040` while the other title lines are black. The UOB scope paragraph mixes `303030` and black runs. On AI Park's employer line, "\| China" is teal, while on other employer lines the location is black. | Run properties | Titles all `404040` italic. Body all black. Location always black. |
| R9 | Low | Capitalisation after a colon differs. Achievement bullets have a capital ("Defined…"); experience bullets are lowercase ("designed…"). | Text | Choose one. I recommend a capital everywhere, because each label is followed by a full sentence. |
| R10 | Low | Education bullets use line spacing 1.15; everywhere else uses 1.03. | `line` value | Use 1.03. |
| R11 | Low | Title lines and sub-headings lack keep-with-next, so either could be left alone at the foot of a page. | Only 11 keepNext flags | Add keep-with-next to both. |
| R12 | Low | Page 1 is 79% full because the forced break leaves blank space; page 3 is 78% full. | Render | Aim for page 1 at 85–100%. Use the spare space for one competency row or a 6th/7th achievement before trimming elsewhere. |
| R13 | Info | An unused list definition is present (`numId=1`, `●`). | `numbering.xml` | Remove it so new bullets cannot pick up the wrong list. |
| R14 | Info | "Singapore" appears twice in the contact line ("Singapore PR … Singapore"). | Contact line | Optional: keep only "Singapore PR". Some recruiters do want a city field, though, so this is your choice. |
| R15 | Info (style) | A first-person "my teams" appears in a UOB bullet, and the UOB bullets mix present tense ("Own…, Lead…") with past tense. | P022, P031–35 | Content rule, not layout: implied first person, present tense for ongoing duties, past tense for completed outcomes. |

---

## 4. ATS Readability

| Area | Assessment | Risk |
|---|---|---|
| Layout | Single column. No text boxes, shapes, images, columns or Word headers or footers holding content. | ✅ Low |
| Contact details | In the document body, not in a Word header, so parsers can find them. Email is plain text with no hyperlink, which is fine. | ✅ Low |
| Section names | Standard: Professional Summary, Professional Experience, Education. | ✅ Low |
| Competency table | A simple 2×7 grid that most current parsers read row by row. Older parsers may flatten it into run-on text. | 🟡 Low–Med. Make sure core keywords also appear in body bullets. |
| Employer / date line | Employer, location and dates sit on one line, separated by `\|` and a tab. Most parsers handle this. The title is on the next line. | 🟡 Low |
| Earlier Experience | Dates sit inline in parentheses, and some entries give years only. Parsers will **not** create job records for these entries, so an auto-calculated total of years may undercount (2008–2016 looks empty). | 🟡 Medium. Fill in portal job-history fields by hand. |
| Special characters | `→` (MT→MX) may turn into "?" in some systems. Em dashes, en dashes and `·` usually survive. | 🟡 Low. Consider "MT-to-MX" in the DOCX you upload, or keep `→` and accept the risk. |
| Fonts | Calibri is a system font. Nothing needs embedding in the DOCX. | ✅ Low |
| Metadata | Stale title (R1). | 🔴 Hygiene, not parsing |
| File format | Submit the DOCX to ATS portals; send a PDF directly to humans. | — |

---

## 5. Content Carry-Over Guardrail

The template's wording is a **sample, not a source**. Before any sentence from it appears in a future resume, it must trace to `03_Achievement_Library.md` or `Wilson_Master_Career_Profile.md`. The quantified claims in the template are listed below as items to trace. I checked one: the "25 engineers" figure matches X-02, which you confirmed on 2026-10-16. **I did not verify the others.**

`99.9%+ availability` · `99% SonarQube coverage` · `~80% code-review time (estimated)` · `MX-rich live May/Aug 2025; coexistence retired Aug 2026` · `15-engineer team` · `10-engineer backend team` · `~100k DAU` · `millions of real-time events` · `four IT service vendors`

---

## 6. Recommendations: Fixed vs Adaptive

**Lock these in the base file (FIXED):**
- A4 page, single column, Calibri 9.5 pt, navy and teal hard-coded.
- Standard margins of 1.27 / 1.5 cm, plus a page number in the footer.
- Section order, one heading style, and a forced break before Experience.
- The bullet list (`•`, 280/200 twips), spacing tokens and keep-with-next rules.
- The anatomy of the employer, title and date lines, and the date format.
- The narrative summary form (100–130 words) and the `Label:` bullet pattern.
- A maximum of 3 pages, with no spacer paragraphs and no stray colours.

**Let these vary per JD (ADAPT):**
- The headline's role framing and its 3 focus areas.
- Summary paragraphs 2–3.
- Competency rows: which labels, in what order, and which keywords.
- Which 5–7 achievements appear.
- Which 3–4 UOB sub-headings are used, and their bullets.
- Bullet counts for earlier roles.
- Promoting or demoting roles between full blocks and Earlier Experience.
- The metadata Title.

**Next step (once you approve):** build a clean base `.docx` from these rules: corrected margins, footer page number, one heading style, no spacers, hard-coded colours and placeholder text only. Every tailored resume would then start from that file instead of a past application.

---

## 7. Open Questions (decide once)

| ID | Question | My suggestion |
|---|---|---|
| OQ-L1 | Page-number format | "Page X of Y", right-aligned, 8 pt, grey |
| OQ-L2 | Heading size | 12 pt for all headings |
| OQ-L3 | Placement of Hengshunyuan | Decide per JD; the default is Earlier Experience |
| OQ-L7 | Header name: "WILSON ZHANG" or "Wilson …" | Your call. It must match the name on your email and LinkedIn. |
| — | Keep `→` or use "MT-to-MX" | Use "MT-to-MX" in uploaded DOCX files |
