# C3 Edit Review: independent fact and readability check

**Reviewer:** independent (did not write these edits) · **Date:** 2026-10-26
**Scope:** the 25 entries in `c3/c3_edits.json`, checked against `resume_before_c3_NN.json`, `drafts/NN/resume.json`, the rendered `*_draft.txt` and `*_draft.pdf` files, and `*report.json` for NN = 01–10.
**Method:** I ran a field-level JSON diff (before vs after) for every resume. I confirmed each "after" string appears in both the rendered PDF (`pdftotext`) and the TXT, and that each "before" string is gone. Page count comes from `pdfinfo`, and page boundaries come from `pdftotext -layout` per page. The render files are newer than every `resume.json`, so they show the current state.

**Result:** 21 PASS · 4 FIX (#1, #9, #18, #20)

## Edit table

| # | Item | After (short) | Verdict PASS/FIX | Note |
|---|---|---|---|---|
| 1 | 01 K3 business team | "Reports status, risks and decisions to senior management, the steering committee and the business team." | **FIX** | Faithful to K3. Readability problem: the sentence ends Summary ¶3, which is about pre-UOB roles ("Began as… then spent 2016–2022… at start-ups and scale-ups…"). A present-tense UOB activity tacked onto that paragraph can be misread as describing the start-up roles, and "the steering committee" has no referent. Replacement below. |
| 2 | 01 K5 SonarQube scope | "99% SonarQube coverage on all code," | PASS | Faithful to K5. Reads naturally. |
| 3 | 01 PA-03.5 CRQ/CAB | "Personally prepare the change request for every production release on both platform lines and present … to the Change Advisory Board (CAB)." | PASS | Says no more than PA-03.5 (it leaves out impact assessment and "(SIT/UAT sign-off)", which is acceptable). Present tense matches the sibling bullets. Not a duplicate of Achievement "SIT/UAT sign-off for every release", which is a different fact. Non-blocking: `ids` is empty and should be `["PA-03.5"]`. |
| 4 | 01 PA-03.5 competency | "…Splunk observability; SIT/UAT and Change Advisory Board (CAB) release approval" | PASS | Derived from PA-03.5. CAB is spelled out at first use (page 1). Still 2 lines. |
| 5 | 02 K2 singular | "…to senior management and the steering committee." | PASS | Not duplicated elsewhere in 02. |
| 6 | 02 K5 SonarQube scope | "99% SonarQube coverage gate on all code" | PASS | — |
| 7 | 03 K2 singular | "…to senior management and the steering committee." | PASS | Not duplicated elsewhere in 03. |
| 8 | 03 K5 SonarQube scope | "99% SonarQube coverage gate on all code" | PASS | 03 is exactly at the limit for 3-line bullets (6/30 = 1 in 5). This edit did not add a line. |
| 9 | 04 K3 business team | "Reports status, risks and decisions to senior management, the steering committee and the business team." | **FIX** | Faithful to K3. Readability problem: Summary ¶3 opens with "**Before UOB**, built and re-architected…", so a present-tense UOB activity ending that paragraph contradicts the paragraph's own frame. Replacement below. |
| 10 | 04 K3 de-duplicate | "Act as the primary interface between business stakeholders, … architects and engineering managers." | PASS | This removes the stacking correctly: the reporting fact now appears only in the Summary. The bullet still reads as complete. |
| 11 | 04 K5 SonarQube scope | "…with a 99% SonarQube coverage gate on all code, automated regression…" | PASS | Competency line stays at 2 lines. |
| 12 | 04 PA-03.5 CRQ/CAB | (same PA-03.5 bullet as #3) | PASS | Sits in the "Reliability, Security & Governance" group, which fits. No overlap with the KPI bullet. Non-blocking: set `ids` to `["PA-03.5"]`. |
| 13 | 05 K2 singular | "…to senior management and the steering committee." | PASS | — |
| 14 | 05 K5 SonarQube scope | "a 99% SonarQube coverage gate on all code" | PASS | — |
| 15 | 06 K1 scale-ups | "…leading technology and delivery at start-ups and scale-ups before joining a Tier-1 bank." | PASS | Faithful to K1. No "technology companies" left. |
| 16 | 08 K1 scale-ups | "…digital platforms at start-ups and scale-ups — a smart-parking IoT platform…" | PASS | Faithful to K1. Summary ¶1 still says "fintech and SaaS start-ups". That is not a contradiction, so it stays as is. |
| 17 | 08 PA-03.5 CRQ/CAB | (same PA-03.5 bullet as #3) | PASS | Opens the "Governance, Risk & Production" group. No duplicate. Non-blocking: set `ids` to `["PA-03.5"]`. |
| 18 | 08 PA-03.5 competency | "…SIT/UAT sign-off, change control (CRQ/CAB), secure SDLC…" | **FIX** | "CRQ" is ITSM/Remedy jargon that appears nowhere else in 08. The bullet says "change request" and never "(CRQ)". "CAB" is also not spelled out on page 1, where it first appears. An HR reader cannot decode either term. Replacement below. It matches the wording already used in 01. |
| 19 | 09 K1 scale-ups | "…a project-manager-and-architect role (2020–2022) at start-ups and scale-ups, building 0-to-1 platforms." | PASS | Faithful. "at start-ups and scale-ups" covers both role groups (2016–2020 and 2020–2022), as "at start-ups" did before. |
| 20 | 09 K2 singular | Summary ¶3, Competencies "Stakeholders & Bids" and the UOB bullet: "…senior management and the steering committee" | **FIX** | The K2 wording is correct everywhere. However, the edit kept a duplicate on lines it touched: Summary ¶3 "Reports status, risks and decisions to senior management and the steering committee…" and UOB bullet "Report status, risks and decisions to senior management and the steering committee, and work closely with…" state the same fact almost word for word. Edits #10 and #24 removed exactly this stacking in 04 and 10, so 09 is now inconsistent with them. Replacement below. (The edit log also lists one row for three changed locations; this is non-blocking.) |
| 21 | 09 K5 SonarQube scope | "a 99% SonarQube coverage gate on all code" | PASS | — |
| 22 | 09 PA-03.5 CRQ/CAB | (same PA-03.5 bullet as #3) | PASS | Follows the KPI bullet that ends "SIT/UAT sign-off on every release". The two bullets state different facts, so this is not stacking. Non-blocking: set `ids` to `["PA-03.5"]`. |
| 23 | 10 K3 business team | "Reports status, risks and decisions to senior management, the steering committee and the business team, and holds decision or joint-decision authority on vendor selection and technology investment." | PASS | Faithful to K3, and grammatical. ¶3 is a general paragraph that follows the UOB paragraph, so the present tense reads correctly. (The overlap with the UOB bullet "Hold decision or joint-decision authority…" existed before C3. This edit did not create it.) |
| 24 | 10 K3 de-duplicate | "Work closely with teams in India, Thailand and Indonesia across time zones." | PASS | Removes the stacking correctly. Non-blocking: the bullet's `ids` still carries `C-RPT`, which no longer applies. |
| 25 | 10 K2 singular | Competencies: "Senior management and the steering committee, vendor selection…" | PASS | A keyword list, so its overlap with the Summary is acceptable. |

## Exact replacement text for FIX items

**#1, resume 01, `summary[2]`, last sentence**
- Replace: `Reports status, risks and decisions to senior management, the steering committee and the business team.`
- With: `At UOB, reports status, risks and decisions to senior management, the steering committee and the business team.`
- Layout: the paragraph's last line ("steering committee and the business team.") has about 90 characters free, so the extra 8 characters keep it at 4/4 lines.

**#9, resume 04, `summary[2]`, last sentence**
- Replace: `Reports status, risks and decisions to senior management, the steering committee and the business team.`
- With: `At UOB, reports status, risks and decisions to senior management, the steering committee and the business team.`
- Layout: same as #1 (the last line is short, so the paragraph stays at 4/4 lines).

**#18, resume 08, `competencies[3][1]`**
- Replace: `change control (CRQ/CAB),`
- With: `change control and Change Advisory Board (CAB) approval,`
- Layout: adds 31 characters. Line 2 of this competency ("secure SDLC, MAS TRM (Singapore technology-risk rules)") has about 70 characters free, so it should stay at 2/2 lines.

**#20, resume 09, `experience[0].groups[2].bullets[0].text`** (the same treatment as #24 in resume 10)
- Replace: `Report status, risks and decisions to senior management and the steering committee, and work closely with teams in India, Thailand and Indonesia across time zones.`
- With: `Work closely with teams in India, Thailand and Indonesia across time zones.`
- Also change that bullet's `ids` from `["X-02","C-RPT"]` to `["X-02"]`.
- Layout: this saves one line on page 2. Page 3 may pull up a line, so re-render to confirm.

After these four edits, **re-render 01, 04, 08 and 09** and re-check the reports. The layout for these fixes has not been verified, because they have not been rendered yet.

## Layout check (current renders)

| NN | Report layout_ok | Pages (pdfinfo) | 3-line bullets | P2 starts with PROFESSIONAL EXPERIENCE | Orphan headings |
|---|---|---|---|---|---|
| 01 | True | 3 | 5/32 | Yes | None (P2 ends on an AI Park bullet, which continues on P3) |
| 02 | True | 3 | 5/33 | Yes | None (P3 opens with the AI Park heading) |
| 03 | True | 3 | 6/30 (= 1 in 5, at the limit) | Yes | None |
| 04 | True | 3 | 5/30 | Yes | None |
| 05 | True | 3 | 5/31 | Yes | None |
| 06 | True | 3 | 5/30 | Yes | None |
| 07 | True | 3 | 5/34 | Yes | None |
| 08 | True | 3 | 4/31 | Yes | None |
| 09 | True | 3 | 5/31 | Yes | None |
| 10 | True | 3 | 5/32 | Yes | None (P3 opens with the EARLIER EXPERIENCE heading) |

Every report shows `lint: []`, `line_flags: []` and `page1_has_all_achievements: True`.

## Leftover scan (all 10 after-JSONs and rendered TXTs)

- "steering committees" (plural): **none**
- "business terms": **none**
- "led the build of" (VV): **none**. VV now reads "built its microservices platform from scratch" or "Built VV's microservices platform…" everywhere, in line with K4.
- "technology companies" (meant as "scale-ups"): **none**
- Every "99% SonarQube" mention now carries "on all code" (01, 02, 03, 04, 05, 09). The SonarQube mentions without a coverage figure (01 competency, 07, 10, and the AI-review lines) need no change.

## Non-blocking notes (outside the C3 verdicts)

- The four new PA-03.5 bullets (01, 04, 08, 09) have no source `ids`. For traceability, set them to `["PA-03.5"]`.
- **Resume 07 (no C3 edits):** the same Summary-vs-bullet stacking as #20 already existed before C3. Summary ¶2 says "…reports to senior management and the steering committee." The UOB bullet says "…report delivery status to senior management and the steering committee." I suggest a separate approval to trim the bullet to: `Act as the interface between business, product, operations, compliance and engineering managers.`
