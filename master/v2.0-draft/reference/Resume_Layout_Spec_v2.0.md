# Resume Layout Specification

**Version:** v2.0 · 2026-10-16
**Reference file:** `wilson-2026_TPM_Bank_template.docx` [TPL]
**Method:** I read the DOCX XML directly (`document.xml`, `styles.xml`, `numbering.xml`, `settings.xml`) and rendered it to PDF with LibreOffice. LibreOffice uses Carlito, which has the same metrics as Calibri, and produced 3 A4 pages. Word's own `app.xml` also records 3 pages.
**Scope:** This file covers format only. The wording in [TPL] is **not** a content source. Content comes only from the verified master files: `Wilson_Master_Career_Profile.md` and `03_Achievement_Library.md`.

**Legend**
- 📏 **Observed:** measured directly in the XML or the rendered pages.
- 🔍 **Interpreted:** a reasonable reading of the observed pattern, not stated anywhere in the file.
- ❓ **Not inferable:** the file cannot tell us this.
- ✅ **Your decision:** overrides [TPL].
- **FIXED / ADAPT:** whether the rule stays constant across job descriptions or may vary per JD (see §11).

> **Corrections to `04_Resume_Layout_Spec.md` v1.0.** That spec contained four errors, which this version fixes:
> 1. Professional Experience **does** start on a forced new page (`pageBreakBefore`).
> 2. Title lines and sub-headings are **italic**.
> 3. Only section headings and employer lines carry keep-with-next. Title lines and sub-headings do not.
> 4. The teal employer colour is tied to the document theme (`accent1`), not set as a hard-coded colour.

---

## 1. Page Count and Page Structure

```
┌──────────── PAGE 1: "Summary zone" ─────────────┐  ┌──────────── PAGE 2 ────────────┐  ┌──────────── PAGE 3 ────────────┐
│              WILSON ZHANG (name)                │  │ PROFESSIONAL EXPERIENCE ───────│  │ …previous role, continued       │
│     status | phone | email | location           │  │ Employer | Location     Dates  │  │ Employer | Location     Dates  │
│  Headline: target role | 3 focus areas          │  │ Title (italic)                 │  │ Earlier roles (1 line each)    │
│ PROFESSIONAL SUMMARY ───────────────────────────│  │ Scope paragraph                │  │ EARLIER EXPERIENCE ────────────│
│  3 narrative paragraphs                         │  │ Sub-heading (bold italic)      │  │ EDUCATION, CERTS & LANGUAGES ──│
│ CORE COMPETENCIES ──────────────────────────────│  │  • bullets                     │  │  • 4 lines                     │
│  2-column table, 7 rows                         │  │ Employer 2 …                   │  │                                │
│ SELECTED ACHIEVEMENTS ──────────────────────────│  │ Employer 3 (starts here)       │  │ (~22% blank)                   │
│  • 7 "Label: sentence" bullets                  │  │                                │  │                                │
│ (~21% blank, from the forced break)             │  │ (100% full)                    │  │                                │
└──────────── forced page break ──────────────────┘  └────────────────────────────────┘  └────────────────────────────────┘
```

| Item | Rule | Source | Type |
|---|---|---|---|
| Total length | 3 pages, about 2,000 words | 📏 | FIXED: no more than 3 pages |
| Page 1 | Header, Summary, Core Competencies and Selected Achievements only. Together these form the "one-page summary". | 📏 + 🔍 matches your "Summary about one page" preference | FIXED |
| Page 1 → 2 transition | `pageBreakBefore` on the PROFESSIONAL EXPERIENCE heading | 📏 | FIXED |
| Pages 2–3 | Experience flows freely, then Earlier Experience, then Education | 📏 | ADAPT (role depth) |
| Page fill (rendered) | Page 1 ≈ 79%, page 2 ≈ 100%, page 3 ≈ 78% | 📏 | Target: page 1 at 85–100% |
| Section order | Summary → Competencies → Achievements → Experience → Earlier → Education | 📏 | FIXED |

---

## 2. Page Setup

| Item | [TPL] value | Standard going forward | Source |
|---|---|---|---|
| Paper | A4 portrait (11906 × 16838 twips) | Same | 📏 |
| Margins | T/B 620 twips = **1.09 cm**; L/R 590 twips = **1.04 cm** | **T/B 1.27 cm, L/R 1.5 cm** (taken from the LIB V5 documents) | 📏 / ✅ no narrow margins |
| Text width | 10726 twips = 18.92 cm | 10206 twips = 18.0 cm, which is **5% narrower** | derived |
| Header / footer distance | 708 twips = 1.25 cm | Same | 📏 |
| Header | None | None | 📏 FIXED |
| Footer / page number | **None** | ✅ Add a page number. The format is still open: OQ-L1 suggests "Page X of Y", right-aligned, 8 pt, grey `7F7F7F`. | 📏 / ✅ |
| Columns | Single column | Single column | 📏 FIXED |
| Default tab stop | 720 twips | Same | 📏 |

> ⚠️ The standard margins reduce line length by about 5% and the usable page height by about 1%. Content that filled 3 pages in [TPL] will grow by roughly 0.15 pages. Absorb this by **condensing content**, never by shrinking fonts or margins.

---

## 3. Typography and Colour

| Token | Value | Where it is used | Source |
|---|---|---|---|
| Font | **Calibri** for all text, set in `docDefaults`. This overrides the theme font Aptos. | Everywhere | 📏 FIXED |
| Base size | **9.5 pt** (`sz=19`) | Body, bullets, title line, dates, headline | 📏 FIXED |
| Navy `1F3864` (hard-coded) | Name, headline, section headings and their rules, sub-headings | | 📏 FIXED |
| Teal `156082` (`themeColor=accent1`) | Employer names; also the EARLIER EXPERIENCE heading | | 📏. Hard-code the hex value (see review R6). |
| Grey `404040` | UOB title line only | | 📏 ⚠️ inconsistent |
| Dark grey `303030` | Parts of the UOB scope paragraph | | 📏 ⚠️ almost invisible; drop it |
| Black / auto | Body text, dates, "\| Location" on employer lines | | 📏 |
| Table border `BFBFBF` 0.25 pt; label-cell fill `EEF2F8` | Core Competencies | | 📏 FIXED |
| Language tag | `en-SG`, with British spelling (programme, optimisation, licence) | | 📏 FIXED |

---

## 4. Header Block (centred, no Word header)

| Line | Format | Content pattern | Source | Type |
|---|---|---|---|---|
| Name | 17 pt, bold, navy, ALL CAPS typed (not the caps style); spacing after 0.5 pt | `WILSON ZHANG` | 📏 | Format FIXED. ⚠️ Your preference is for the header to read "Wilson". Confirm the exact rendering (OQ-L7). |
| Contact | 9 pt, black; items separated by `␣␣\|␣␣`; spacing after 1 pt | `Singapore PR \| +65 … \| email \| Singapore` | 📏 | FIXED. No photo, date of birth or NRIC. |
| Headline | 9.5 pt, bold, navy; spacing after 2 pt | `<Target-role title> — <Domain>  \|  <Focus 1> · <Focus 2> · <Focus 3>` | 📏 | **ADAPT** (wording); pattern FIXED |

- 📏 The headline is 134 characters and wraps onto a second line, leaving one word ("Governance") alone on it. Keep it to **≤ 110 characters (one line)** at the standard margins.
- 🔍 The headline frames the target role. It is not a job title you have held (see the factual rule in `01`).

---

## 5. Section Heading

| Attribute | Value | Source |
|---|---|---|
| Text | ALL CAPS, typed in capitals, bold, navy | 📏 |
| Size | **14 pt** for SUMMARY, EXPERIENCE and EDUCATION; **12 pt** for COMPETENCIES and ACHIEVEMENTS; **11 pt teal** for EARLIER EXPERIENCE | 📏 ⚠️ three different treatments |
| Rule | Bottom border, single, 0.75 pt (`sz=6`), navy, 1 pt gap | 📏 |
| Spacing | Before 5.5 pt, after 2.25 pt, line spacing 1.5 (`line=360 auto`) | 📏 |
| Pagination | Keep with next | 📏 |
| **Standard** | One treatment for every heading: **12 pt bold navy with a navy rule** (OQ-L2) | 🔍 recommendation |

---

## 6. Summary Section (page 1)

### 6.1 Professional Summary

| Item | [TPL] | Rule | Type |
|---|---|---|---|
| Form | 3 narrative paragraphs with no bullets or labels | Narrative only, matching your stated preference | 📏 FIXED |
| Length | 46 / 42 / 28 words, about 116 words in total; 3 + 3 + 2 rendered lines | **100–130 words, 7–9 lines** | 📏 FIXED range |
| Paragraph format | 9.5 pt; single line spacing; spacing after 6 pt; left-aligned (not justified) | | 📏 FIXED |
| Paragraph 1: identity | Seniority label, 18+ years, sectors, current role and scope | Always first | 📏 FIXED order |
| Paragraph 2: capability | The JD's core capability cluster, followed by a "proven ability" sentence | | 📏 **ADAPT** wording |
| Paragraph 3: technical depth | Engineering, architecture and domain background | | 📏 **ADAPT** emphasis |

### 6.2 Core Competencies

| Item | [TPL] | Rule | Type |
|---|---|---|---|
| Form | 2-column table, 7 rows, no header row, no merged cells | 6–8 rows | 📏 FIXED form |
| Column widths | 2500 / 8226 twips (23% / 77%) | Rescale to 2350 / 7856 twips for the 18.0 cm text width | 📏 / derived |
| Label cell | 9 pt, bold, `EEF2F8` fill, 2–4 words | | 📏 |
| Content cell | 9 pt, comma-separated keywords, 8–17 words, no more than 2 lines | | 📏 |
| Cell margins | Top/bottom 1.25 pt, left/right 4 pt | | 📏 |
| Row order | Most relevant to the JD first. The **Technical** row stays last. | | 🔍 **ADAPT** |

### 6.3 Selected Achievements

| Item | [TPL] | Rule | Type |
|---|---|---|---|
| Count | 7 bullets | 5–7 | 📏 / ADAPT |
| Pattern | **`Bold label:`** followed by a sentence that starts with a capital letter | | 📏 FIXED |
| Label | 2–5 words, naming the capability (for example "Payment resilience:") | | 📏 |
| Length | 27–49 words, 2–3 lines | ≤ 45 words, ≤ 3 lines | 📏 |
| Selection | Cross-role highlights, each with an outcome or metric | Must trace to `03_Achievement_Library` | 🔍 **ADAPT** |

---

## 7. Professional Experience (pages 2–3)

### 7.1 Role block anatomy

```
Employer Name (Abbr)  |  Location                                   Mmm YYYY – Mmm YYYY   ← employer line
Title — Unit, Division                                                                     ← title line (italic)
One scope paragraph: what you own, scale, team                                             ← scope (optional for older roles)
Sub-heading (bold italic navy)                                                             ← current role only
Optional one-line project context paragraph
  • bullet
  • bullet
```

| Element | Format | Spacing (before / after / line) | Source |
|---|---|---|---|
| Employer line | 11 pt bold. Employer name in teal; `␣␣\|␣␣Location` in black. Dates in **9.5 pt bold black**, placed on a **right-aligned tab** at the text width (10726 in [TPL], 10206 at the standard margins). | 5 / 0.25 / 1.5 lines; keep with next | 📏 |
| Title line | 9.5 pt *italic* (`404040` for UOB, auto colour for the others) | 0 / 1.25 / 1.03 | 📏 ⚠️ colour inconsistent |
| Scope or context paragraph | 9.5 pt, regular | 0 / 1.25 / 1.03 | 📏 |
| Sub-heading | 9.5 pt ***bold italic***, navy | 2.25 / 0.75 / 1.03; **no** keep with next | 📏 |
| Bullet | `•` glyph from list `numId=2`; indent left 280, hanging 200 twips (0.49 / 0.35 cm); 9.5 pt | 0 / 1.1 / 1.03 (`line=247`) | 📏 FIXED |
| Date format | `Mmm YYYY – Mmm YYYY` / `– Present`, with a spaced en dash | | 📏 FIXED |

### 7.2 Two bullet styles (observed)

| Role | Structure | Bullets | Source |
|---|---|---|---|
| UOB (current) | Scope paragraph + **4 sub-headings** (Production & Service Mgmt · Programme · Platform Line · Stakeholder/Team); plain bullets with no bold labels | 2 + 4 + 1 + 3 = 10 | 📏 |
| Golden Bridge | Product context line + **bold-label bullets** (`Label:` then a lowercase continuation) | 6 | 📏 |
| VV Technology | Product context line + bold-label bullets | 8 | 📏 |
| AI Park | Product context line + bold-label bullets | 6 | 📏 |

🔍 **Interpretation:** the current role is organised by **sub-headings**. Earlier roles use **bold lead-in labels** in place of sub-headings. Keep this two-level system.

### 7.3 Depth by recency

| Tier | Treatment | Type |
|---|---|---|
| Current role | Full block: scope paragraph, 3–4 sub-headings, 8–11 bullets | FIXED structure; ADAPT sub-headings |
| Roles 2–4 | Context line + 4–8 bold-label bullets | ADAPT (bullet count by relevance) |
| Earlier roles | **EARLIER EXPERIENCE** section with one bullet per role: `**Employer** — Title, platform (years): one clause` | FIXED form |
| Ordering | Reverse chronological within each section. ⚠️ [TPL] places Hengshunyuan (2017–2019) under Earlier Experience, after AI Park (2016–2017). This is a deliberate compression choice. | 📏 ADAPT (OQ-L3) |

---

## 8. Education, Certifications & Languages

| Item | Format | Source |
|---|---|---|
| Form | Bullets: `**Degree** — University (YYYY – YYYY)` | 📏 |
| Certifications | One bullet joined with ` · `: `**Cert** — detail · **PMP** — in progress · …` | 📏 |
| Languages | `**Languages:** …` | 📏 |
| Line spacing | 1.15. ⚠️ Differs from the 1.03 used elsewhere; use 1.03 throughout. | 📏 |

---

## 9. Pagination and Spacers

| Item | [TPL] | Rule | Source |
|---|---|---|---|
| Forced breaks | 1 (`pageBreakBefore` on PROFESSIONAL EXPERIENCE); no manual page-break characters | Keep this single break | 📏 FIXED |
| Keep with next | 11 paragraphs: section headings and employer lines | **Add** keep with next to title lines and sub-headings so they cannot be stranded at the foot of a page | 📏 / 🔍 |
| Keep lines together | Not used | Optional on bullets ≤ 3 lines | 📏 |
| Empty spacer paragraphs | 2: P008 after the table (carries a navy rule; Word merges it with the next heading's rule, adding about 20 pt of blank space) and P070 before Education | **Remove.** Use paragraph "spacing before" instead. | 📏 |
| Unused list definition | `numId=1` (`●`, 720/360) is defined but not used | Remove it | 📏 |

---

## 10. Typographic Conventions

| Mark | Use | Source |
|---|---|---|
| `␣␣\|␣␣` | Separates contact items, employer from location, and role from focus areas in the headline | 📏 |
| ` — ` (spaced em dash) | Separates a title from its unit, and a label from its detail in Earlier Experience and Education | 📏 |
| ` – ` (spaced en dash) | Date ranges, and ranges such as P1–P3 (unspaced) | 📏 |
| ` · ` (middle dot) | Inline lists in the headline and certifications | 📏 |
| `→` | MT→MX (see the ATS note in the review) | 📏 |
| Capital after colon | Achievements: **capital**. Experience labels: **lowercase**. | 📏 ⚠️ choose one |

---

## 11. Fixed vs Adaptive Summary

| FIXED across all JDs | ADAPT per JD |
|---|---|
| A4, single column, Calibri 9.5 pt, colour tokens, standard margins | Headline wording and its 3 focus areas |
| Section order and heading treatment | Summary paragraphs 2–3 (capability and technical emphasis) |
| Page 1 = summary zone + forced break before Experience | Competency row labels, row order and keywords (6–8 rows) |
| Narrative summary (100–130 words) | Which 5–7 achievements appear, and their labels |
| Achievement and bullet patterns, indents and spacing | UOB sub-headings (choose 3–4 by JD) and the bullets under them |
| Employer / title / date line anatomy and date format | Bullet count per earlier role (4–8) |
| Earlier-experience one-line form | Which roles are promoted from Earlier Experience to full blocks, or demoted |
| No more than 3 pages; page numbers in footer | Bank lens vs Internet lens (same layout, different emphasis; OQ-L4) |
| Contact line fields | File metadata (Title) must match the target JD |

---

## 12. Not Inferable from the File (❓)

| ID | Item |
|---|---|
| OQ-L1 | Page-number format and position: none exist in [TPL]. |
| OQ-L2 | Which heading size is intended: 14 pt, 12 pt or 11 pt teal. |
| OQ-L3 | Whether Hengshunyuan's placement under Earlier Experience is a standing rule or a choice made for this JD only. |
| OQ-L4 | Whether Internet-lens resumes use this same layout. Assumed yes. |
| OQ-L7 | The name rendering in the header: "WILSON ZHANG" in [TPL] vs your preference "Wilson". |
| — | Exact Word pagination. The render used LibreOffice with Carlito (metric-compatible), so Word may shift line breaks by 1–2 lines. Check in Word before sending. |
| — | Whether the mixed colours (`404040` and `303030` vs black) are intentional. They read as leftovers. |
