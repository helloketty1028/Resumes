# 01 — Resume Master Rules

**Version:** v1.0 · 2026-10-16 · **Status:** ACTIVE (items marked ⚠️ / ❓ await your confirmation)
**Role of this file:** The rulebook for every other file and every tailored resume: truth rules, status icons, ownership verbs, writing style, confidentiality, review method and the pre-delivery QA checklist. **It holds no career facts.**
**Migrated from:** Project instructions (12 rules) · `master-career-profile.md` v2.2 §0, §4 standing rules, §9 · `project-achievement-library.md` v3.1 §0 · `technical-skills-inventory.md` v2.1 usage rule · your confirmed preferences (memory) · decisions of 2026-10-16.

---

## 1. File System and Single Source of Truth

| File | Owns (authoritative for) | Never contains |
|---|---|---|
| `01_Resume_Master_Rules.md` | Rules, icons, verbs, style, confidentiality, QA | Career facts |
| `02_Candidate_Profile.md` | Identity, timeline, titles, education, positioning, role-family headlines, capability matrix, role scope summaries | Achievement wording, metrics bank |
| `03_Achievement_Library.md` | Every achievement, its safe wording, ownership, relevance, metrics bank, interview examples | Layout, JD rules |
| `04_Resume_Layout_Spec.md` | Word page, fonts, spacing, headings, section order, pagination | Content |
| `05_JD_Keyword_and_Matching_Rules.md` | JD parsing, matching matrix, keyword mapping, ordering, compression, gaps, fast-reject, family × industry lens | Career facts (references IDs only) |
| `technical-skills-inventory.md` (auxiliary) | Skill depth (P/A/F/X) and evidence anchors | — |
| `fact-check-and-open-questions.md` (auxiliary) | Conflict register, high-risk claims, open questions, decision log | — |
| `archive/` | Superseded versions — read-only | — |

**One fact, one home.** A fact is written in full only in its authoritative file; other files cite it by ID (e.g. `PA-01.1`, `CF-07`, `FU-1`). Do not copy text between files.

**Update flow for a new or changed fact:**
```
New info ─► fact-check register (log source + date) ─► status icon decided ─► 02 or 03 updated ─► change log entry in that file
```

---

## 2. Truth Rules (Project rules 1–12, applied)

1. Uploaded career documents and your explicit confirmations are the primary sources. A user correction outranks older wording; keep its source and date `[CONF yyyy-mm-dd]`.
2. Never invent or inflate employers, titles, dates, technologies, responsibilities, team sizes, scope or results.
3. Keep hands-on coding, architecture, technical leadership, delivery management and people management distinct (tags in §4).
4. Separate confirmed facts, interpretations and items needing confirmation (icons in §3).
5. Preserve history: nothing is deleted from 02 or 03; retirement needs your explicit decision and the item moves to a "retired" table, not into oblivion.
6. Every tailored resume starts with JD analysis and an evidence matrix (05) before any rewriting.
7–8. The master files (02, 03) are never replaced by, or edited into, a tailored resume.
9. Concise, natural, professional English for senior technology roles.
10. Optimise for genuine fit, recruiter readability and honest ATS keywords — no stuffing.
11. Ask focused questions when a missing fact would materially change the resume.
12. Never disclose confidential employer or customer information (§7).

**Fact-handling details**
- Employment dates, project dates and document dates are different things; keep supplied precision; never invent months or gap explanations.
- Keep production observations, load tests, design targets and estimates distinct; an estimate is always labelled as one (e.g. PA-07.3 "estimated ~80%").
- Team size is scope, not an outcome. "Led a team of N" ≠ "hired N".
- A historical technology does not prove current hands-on proficiency.
- Conflicting sources: keep both originals, mark ⚠️, and do not choose a version without your decision.

---

## 3. Unified Status Icons (replaces the two earlier systems)

| Icon | Meaning | Resume use |
|---|---|---|
| ✅ | **Confirmed** — your explicit confirmation or a primary document | Yes |
| 📄 | **Documented** — stated in one of your own resumes ([R22] 2022 resume, [LIB] V5 libraries), not separately confirmed | Yes, as worded in 03 |
| 🔶 | **Interpretation** — a defensible framing of confirmed facts | Yes, with care |
| ❓ | **Needs confirmation** — incomplete, unattributed or hard to defend | Only the parts outside `{…}` slots |
| ⚠️ | **Conflict** — sources disagree; unresolved | No, until you decide |
| ⛔ | **Hold** — implausible, anachronistic or proposed for retirement | No |

Source codes: `[R22]` 2022 standalone resume · `[LIB]` six V5_0_0 libraries · `[CONF yyyy-mm-dd]` your confirmation · `[CERT-SS]` / `[CERT-BC]` certificates · `[TPL]` `templates/wilson-2026_TPM_Bank_template.docx`.

---

## 4. Capability Tags and Ownership → Permitted Verbs

**Capability tags:** [HC] hands-on coding · [AR] architecture/design · [TL] technical leadership · [DM] delivery/programme management · [PL] people leadership · [CV] commercial/vendor/budget · [GV] governance/risk/security.

| Ownership level (03) | Meaning | Permitted verbs | Not permitted |
|---|---|---|---|
| **O1** | Personally built/coded | built, implemented, coded, developed, wrote | — |
| **O2** | Designed and led the build | designed, architected, led the build of, defined | "built" (implies own code) unless O1 also applies |
| **O3** | Owned delivery / programme | owned, delivered, ran, planned, coordinated | "designed" unless O2 also applies |
| **O4** | Governed through managers | led (through squad leads / EMs), oversaw, governed | "built", "coded" |
| **O5** | Contributed | contributed to, supported, participated in | "set", "established", "owned" |

Locked wording: bank-wide standards = **"contributed to"** (CF-15). UOB hands-on = daily review + design + core-module coding on significant changes — **never** "full-time engineer" and **never** a coding-time percentage (X-04).

---

## 5. Positioning Standing Rules [CONF]

- Wilson is a long-career **IT technical + management professional** with substantial big-data analytics and applied-AI project experience. **Never** repackage him as an "AI engineer" or "big data engineer" to fit a JD; AI and data are pillars, not the identity.
- No "CTO" or "Chief Architect" title anywhere (HR-1). Accurate: "head-of-technology roles (2016–2020)".
- A headline may name the **target** role; historical titles stay exactly as in 02.
- Three role families × two industry lenses are defined in 02 §7 and 05 §2.

---

## 6. Writing Style

| Area | Rule | Status |
|---|---|---|
| Language | English for resumes; Chinese for our working discussion | ✅ |
| Spelling | British spelling (organisation, programme, optimise), as used consistently in [LIB] and [TPL] | 🔶 default — ❓ confirm (OQ-R1) |
| Professional Summary | A short **narrative overview of the whole career** — not one bullet per role; natural, non-mechanical, crisp, professional; not casual [CONF 2026-10-16] | ✅ |
| Summary length | Preference says "about one page" [CONF]; [TPL] uses 3 short paragraphs (~⅓ page) | ⚠️ conflict — OQ-R2 |
| Voice in application text | Sincere; an 18-year IT professional who is now a bank IT technical expert [CONF] | ✅ |
| Bullets | Action + context + supported result; quantitative or qualitative evidence both valid; no generic claims; no technology dumps | ✅ |
| Bold lead-in | "Label: sentence" bullets are used in Selected Achievements and earlier roles in [TPL] | 📄 see 04 |
| Tense | Present tense for current scope (UOB "Own…", "Lead…"); past tense for completed work | 🔶 matches [LIB]/[TPL] |
| Merging | Merge and condense overlapping content; never stack repeated descriptions across Summary, Achievements and Experience [CONF] | ✅ |
| Length | Tailored resume ≤ 3 pages [CONF] | ✅ |
| Numbers | Only from 03 §Metrics Bank with its attribution; keep "~", "estimated", "internal measure" qualifiers | ✅ |

---

## 7. Confidentiality (rule 12)

Never in recruiter-facing text:
- Internal system names — **CEW, SCV-CCD/CCD** → use "payment-initiation hub", "regional customer-360 platform".
- **Vendor names**, including HCL → "four IT service vendors" [CONF 2026-10-16].
- UOB customer names, volumes, internal ticket/JR numbers, architecture diagrams, vendor commercial terms.
- Personal identifiers from certificates (ID number, date of birth, certificate/file numbers).
- Legal name "Zhang Heng" appears only on application forms / background-check consent, not on the resume (02 §1).

Interview use of internal names is your call; resumes never carry them.

---

## 8. Review Method — three dimensions, no total score [CONF 2026-10-16]

Every tailored output is reviewed in three separate dimensions. **No aggregate %, ATS score, pass threshold or interview probability.** (The earlier JD-fit-% practice is retired.)

1. **Job fit** — each explicit required / preferred criterion → direct / transferable / gap / unverified evidence; eligibility issues stay visible.
2. **Factual reliability** — dates, titles, numbers, names, ownership verbs checked against 02/03; material conflicts listed.
3. **Document quality** — readability, extractable text, layout per 04; list checks passed, issues found, checks not performed.

---

## 9. Pre-Delivery QA Checklist (run on every tailored resume)

**Facts**
- [ ] Every bullet traces to an ID in 03 (or a section in 02); no ❓ / ⚠️ / ⛔ content outside permitted parts.
- [ ] Dates and titles match 02 §2 exactly; no "CTO" / "Chief Architect".
- [ ] Every number matches 03 Metrics Bank, with qualifiers kept.
- [ ] Verbs match ownership level (§4).
- [ ] Skills appear only if anchored in the skills inventory (depth P or A for Summary/bullets).

**Confidentiality**
- [ ] No CEW / SCV-CCD / vendor names / internal numbers (§7).

**Positioning and style**
- [ ] Headline and Summary fit the chosen family × lens (02 §7, 05 §2).
- [ ] Summary is narrative; no stacked repetition with Selected Achievements or Experience.
- [ ] British spelling consistent (pending OQ-R1).

**Document**
- [ ] Layout per 04; ≤ 3 pages; page numbers present; no orphaned headings (keep-with-next).
- [ ] Text extractable (no text boxes for content, no images of text); renders correctly as PDF.
- [ ] File name per §10.

**Review package**
- [ ] Three-dimension review (§8) delivered separately from the resume.
- [ ] Change log listing every material change and why.

---

## 10. Editing and Versioning Conventions [CONF]

- **Surgical edits** over wholesale rewrites, with full transparency on what changed and why.
- Tailored drafts: changes marked in red (`FF0000`) until approved; final version all black.
- File naming: `wilson-2026_[Family]_[Lens]_[Target]_V[major]_[minor]_[patch].docx` 🔶 — the earlier convention was `wilson-2026_[family]_[Target]_V…`; the `[Lens]` segment (`Bank` / `Internet`) is added because of the 2026-10-16 family × lens decision. ❓ confirm (OQ-R3).
- Master files carry a version line and a change log; every structural change bumps the minor version.

---

## 11. Open Rule Questions

| ID | Question |
|---|---|
| OQ-R1 | Confirm British spelling as the standard. |
| OQ-R2 | Summary length: "about one page" (earlier preference) vs ~3 short paragraphs (as in [TPL] and the narrative-summary preference)? |
| OQ-R3 | Confirm the file-naming pattern with the `[Lens]` segment. |

## 12. Change Log
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-16 | Created from the sources listed in the header. Unified the two icon systems into six icons; added ownership-to-verb table, QA checklist, three-dimension review rule (replaces % scoring), vendor-name rule. |
