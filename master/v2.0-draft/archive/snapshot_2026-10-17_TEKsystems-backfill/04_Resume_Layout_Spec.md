# 04 — Resume Layout Spec (Word)

**Version:** v1.0 · 2026-10-16 · **Status:** ACTIVE — values marked 🔶 or ❓ must be confirmed on the first rendered resume
**Role of this file:** Page, font, spacing, heading, section-order and pagination rules for every tailored Word resume. Holds no content.
**Base sample:** `C:\Users\surface\resumes\templates\wilson-2026_TPM_Bank_template.docx` **[TPL]** — the standard style [CONF 2026-10-16]. All 📏 values below were **measured from that file** (python-docx / XML inspection, rendered to PDF = 3 pages), not invented.
**Your adjustments [CONF 2026-10-16]:** (1) do **not** use [TPL]'s narrow margins; (2) add page numbers.

Legend: 📏 measured from [TPL] · 🔶 proposed (needs confirmation on first render) · ❓ not yet specified · ⚠️ inconsistency inside [TPL]

---

## 1. Page Setup

| Item | Value | Source |
|---|---|---|
| Paper | A4, 21.0 × 29.7 cm, portrait | 📏 |
| Margins in [TPL] | T 1.09 / B 1.09 / L 1.04 / R 1.04 cm — **narrow, not to be used** | 📏 + [CONF] |
| **Margins (standard)** | **T 1.27 / B 1.27 / L 1.5 / R 1.5 cm** — the values used in the six [LIB] V5 docx | 🔶 sourced from [LIB]; confirm |
| Header / footer distance | 1.25 cm | 📏 ([TPL] and [LIB] agree) |
| Text width | 18.0 cm (= 10 206 twips) with the standard margins ([TPL]: 18.92 cm / 10 726 twips) | derived |
| Header | None | 📏 |
| **Footer — page number** | Page number in the footer | [CONF]; format ❓ (e.g. "Page X of Y", right-aligned, 8–9 pt grey — choose on first render, OQ-L1) |
| Manual page breaks | None — pagination by keep-with-next only | 📏 (0 page breaks, 11 keepNext) |

> ⚠️ **Page-count risk:** [TPL] fills exactly 3 pages at 18.92 cm text width. The standard margins cut the line width by ~5%, so the same content may spill onto page 4. Compress content per 05 §6, not by shrinking fonts or margins.

---

## 2. Fonts and Colours

| Item | Value | Source |
|---|---|---|
| Body font | Calibri (explicit in docDefaults; theme fonts Aptos are overridden) | 📏 |
| Body size | 9.5 pt | 📏 |
| East-Asian font | Theme minorEastAsia (no Chinese text expected) | 📏 |
| Language tag | en-SG | 📏 |
| Primary accent | Navy `1F3864` — name, headline, section headings, sub-headings, heading rules | 📏 |
| Employer accent | Teal-blue `156082` — employer lines | 📏 |
| Title line text | Dark grey `404040` | 📏 |
| Scope paragraph text | `303030` | 📏 |
| Body text | Black `000000` / automatic | 📏 |
| Table borders / shading | Border `BFBFBF` 0.25 pt; label-cell shading `EEF2F8` | 📏 |

---

## 3. Element Styles (top to bottom)

| Element | Size / weight / colour | Alignment | Spacing (before / after) | Line spacing | Source |
|---|---|---|---|---|---|
| Name | 17 pt, bold, `1F3864` | Centre | 0 / 0.5 pt | ~1.03 | 📏 |
| Contact line | 9 pt, `000000`; items separated by "  \|  " | Centre | 0 / 1 pt | ~1.03 | 📏 |
| Headline | 9.5 pt bold `1F3864` (bold lead + rest) | Centre | 0 / 2 pt | ~1.03 | 📏 |
| Section heading | Bold `1F3864`, ALL CAPS text, bottom border single 0.75 pt `1F3864` | Left | 5.5 / 2.25 pt | 1.5 | 📏 |
| — heading size | **14 pt** (Summary, Experience, Education) vs **12 pt** (Core Competencies, Selected Achievements) | | | | ⚠️ inconsistent in [TPL] — OQ-L2 |
| Summary paragraph | 9.5 pt, normal | Left | 0 / 6 pt | single | 📏 |
| Core Competencies | 2-column table: label cell 9 pt **bold** on `EEF2F8`, content cell 9 pt; column widths 2 500 / 8 226 twips (≈23% / 77%) → rescale to 18.0 cm text width | — | — | — | 📏 |
| Achievement bullet | "**Label:** sentence" — bold label run + normal run | Left | 0 / 1.1 pt | ~1.03 | 📏 |
| Employer line | 11 pt bold `156082`: "Employer  \|  Location" + right-aligned tab → dates | Left, right tab at text width (10 726 twips in [TPL] → 10 206 at standard margins) | 5 / 0.25 pt | 1.5 | 📏 |
| Title line | 9.5 pt `404040` | Left | 0 / 1.25 pt | ~1.03 | 📏 |
| Scope / context paragraph | 9.5 pt `303030` (UOB) or black | Left | 0 / 1.25 pt | ~1.03 | 📏 |
| Sub-heading inside a role | 9.5 pt bold `1F3864` (e.g. "Production & Service Management") | Left | 2.25 / 0.75 pt | ~1.03 | 📏 |
| Experience bullet | 9.5 pt; "•" bullet; indent left 280 twips, hanging 200 twips | Left | 0 / 1.1 pt | ~1.03 | 📏 |
| Earlier-experience heading | Styled as an employer line (11 pt `156082`) instead of a section heading | — | — | — | ⚠️ inconsistent in [TPL] — OQ-L3 |

Keep-with-next on: section headings, employer lines, title lines and sub-headings 📏 — so a heading never sits alone at the foot of a page.

---

## 4. Section Order (as in [TPL])

```
NAME
Contact line  (status | phone | email | location)
Headline      (target-role framing — see 02 §7)
PROFESSIONAL SUMMARY          — narrative, per 01 §6
CORE COMPETENCIES             — 2-column table, ~7 rows
SELECTED ACHIEVEMENTS         — ~7 bold-label bullets
PROFESSIONAL EXPERIENCE       — reverse chronological
   UOB → Golden Bridge → VV Technology → AI Park
EARLIER EXPERIENCE            — one line each: Hengshunyuan, Baidu, Sohu, Renren
EDUCATION, CERTIFICATIONS & LANGUAGES
```
📏 order measured from [TPL]. In [TPL] Hengshunyuan sits under Earlier Experience despite being later than AI Park — a deliberate compression choice in that file 📄; the general rule is in 05 §5.

---

## 5. Header Content Rules

| Field | Rule | Status |
|---|---|---|
| Name | [TPL] shows **"WILSON ZHANG"**; 02 FU-6 records your 2026-10-15 answer "Wilson" | ⚠️ follow 02 §1 once FU-6 is closed |
| Status | "Singapore PR" | ✅ (02 §1) |
| Photo, date of birth, marital status, NRIC | Never | 01 §7 |

---

## 6. Export and Checks

- Save as `.docx`; produce a PDF for review and inspect the rendered pages (page count, page numbers, heading orphans) before delivery.
- Content must be real text (no text boxes or images for content); the competency table is acceptable for ATS but keep it simple (no merged cells) 📏 [TPL] has none.
- Red `FF0000` markup only in drafts (01 §10).

---

## 7. Not Yet Specified

| ID | Item |
|---|---|
| OQ-L1 | Page-number format and position. |
| OQ-L2 | One section-heading size (14 pt or 12 pt) for all sections. |
| OQ-L3 | Earlier Experience: real section heading, or keep [TPL]'s employer-line style. |
| OQ-L4 | Do Bank-lens and Internet-lens resumes share this one layout? (Assumed yes until you say otherwise.) |
| OQ-L5 | Chinese-language resume layout — not specified; no sample. |
| OQ-L6 | Cover-letter layout — not specified; no sample. |

## 8. Change Log
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-16 | Created from measurements of [TPL]; margins replaced by [LIB] values and page number added per your decision; three internal inconsistencies of [TPL] flagged. |
