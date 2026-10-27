# Wilson Zhang — Fact-Check Register and Open Questions

**Version:** v2.6 · 2026-10-26 · **Auxiliary file — the single register of conflicts, open questions and decisions** (maintained independently [CONF 2026-10-16]). Icons per `01_Resume_Master_Rules.md` §3.
**Rule:** No conflict below has been resolved on your behalf. Where you confirmed a value in an earlier session, it is shown as the **proposed default** and still needs your reconfirmation.

---

## 0. Decision Log

| ID | Date | Decision [CONF] | Applied in |
|---|---|---|---|
| D-01 | 2026-10-16 | Three role families — Architecture/Tech Leader (ATL), Senior Manager (SM), Technical Project Manager (TPM) — each with a bank/fintech (BNK) and internet (INT) lens | 02 §7, 03 §0, 05 §2 |
| D-02 | 2026-10-16 | Standard layout = `templates/wilson-2026_TPM_Bank_template.docx`, but **not** narrow margins, and with page numbers | 04 |
| D-03 | 2026-10-16 | Review = three dimensions, **no aggregate score**; JD-fit % retired | 01 §8, 05 §10 |
| D-04 | 2026-10-16 | Skills inventory and this fact-check file stay independent auxiliary files | 01 §1 |
| D-05 | 2026-10-16 | Vendor names (incl. HCL) are never written externally | 01 §7, 03 X-05 |
| D-06 | 2026-10-16 | "MEPS+ participant bank" wording explained (UOB payments rely on MAS MEPS+ for clearing/settlement; cross-border payments pass through intermediary banks) — kept with a defensibility note | 02 §8 CF-N7, 03 PA-01 |
| D-07 | 2026-10-16 | Job-search filters — **not answered**; recorded as ⚠️, not enforced | 05 §9, OQ-J1 |
| D-08 | 2026-10-16 | Facts confirmed earlier and now migrated: vendor governance (4 vendors), P1–P3 incidents + MAS-reporting input, no separate SRE team, SRE training, RHEL/SQL, VV/AI Park incident-priority plans, Baidu = 2014 only | 02 §8, 03 X-05/X-06/PA-11.5/PA-16.5, skills inventory |
| D-09 | 2026-10-17 | No direct collaboration with US-based teams at UOB; no other US-team collaboration on record. Do not claim US-team experience; JDs asking for it show it as a gap. Cross-time-zone collaboration that IS on record: India, Thailand, Indonesia (03 X-02) | 03 X-02; 05 §5 matrix use |
| D-10 | 2026-10-17 | FU-5 closed (option a): resumes show Hengshunyuan as Oct 2017 – Sep 2019, overlap with VV not annotated; dormancy explained at interview. Date accuracy vs [R22] (CF-05) still unverified against documents | 02 §2 row 5 |
| D-11 | 2026-10-17 | FU-6 closed: resume headers show "Wilson" only (no surname); legal name Zhang Heng on forms | 02 §1; 04 §5 |
| D-12 | 2026-10-20 | OQ-R1 closed: resumes use British spelling (Singapore Standard English), consistent within a document; a target-role title quoted from the JD keeps the JD's spelling (e.g. "Program Manager") | 01 §6, §9, §11 |
| D-13 | 2026-10-20 | Readability standard adopted for every tailored resume: three readers (HR recruiter, hiring manager, ATS); page 1 answers who / what scale / why this role; bullets target 2 lines, cap 3; 1–2 numbers per bullet; layout limits in 04 §3A. The cold-read test and §9 readability checklist lines (RD-05) were not selected and remain a proposal | 01 §6, §6A; 04 §3A, §6 |
| D-14 | 2026-10-20 | OQ-R2 closed: the Professional Summary is about three short paragraphs (≈⅓ page); the earlier "about one page" wording is superseded | 01 §6, §11 |
| D-15 | 2026-10-26 | Confirmed personal change-approval duty: before every production release ("PI" = production implementation, not a SAFe Program Increment), for both platform lines (CEW + CCD), he prepares the CRQ himself and presents at the CAB — go-live plan, risk controls, rollback plan, impact assessment, test results (SIT/UAT sign-off) and database changes. Role at CAB = presenter; CAB membership, frequency and approval rates not recorded | 03 PA-03 §4, §9, §10; PA-03.5 |
| D-16 | 2026-10-26 | Pureland Holding (Jewelake) removed from the work history. The advisory arrangement ended before he joined UOB (Oct 2022); no outside work now. LinkedIn / resume alignment: not now (his decision). Record: in the Cloudera screen (2026-07-10) he said he was "still the consultant" — inconsistent with this decision. Interview answer: "It ended before I joined UOB; my profile is out of date." End month not recorded (B3 default) | 02 §2, §6.2; 03 PA-20, §5.5; skills inventory; 05 §6 |
| D-17 | 2026-10-26 | Interview Bank back-fill — confirmed facts applied: SA-01 (hub safe-retry design), SD-05 (payment + entitlement data migration), SI-03 (coexistence reconciliation, owner open), SB-04 (sanitised P1), SD-02 (incident-command practice, targets), SB-12 (UOB engineers come from the four IT service vendors), SD-01 (requirement-conflict example), SA-03 (four of eight operating-control sub-points), SI-02 (VV-Life 0-to-1 approach), SI-01 (underperforming-lead example), SB-05 as edited (notice period one month). Closes Interview Bank IB-01 (SB-04), IB-03 (SD-01), IB-04 (SI-01); resolves SC-01, SD-08, SD-11, SD-16. Defaults applied to unanswered B1–B9 | 02 §1; 03 PA-01, PA-07, PA-11, X-01, X-02, X-05, X-06, §0A; skills inventory |

## 0A. Open-Question Index (all files)

| Where | IDs | Topic |
|---|---|---|
| This file §5 | FU-1 – FU-6, OQ-1.8 – 1.11, OQ-2.2 – 2.3, OQ-3.1 – 3.8 | Facts, scope, metrics |
| This file §5 Batch 5 | OQ-5.1 – OQ-5.31 | Interview Bank back-fill (2026-10-26) |
| 03 §6.2 | C1 – C7 | AI review metrics, team mapping, retirements |
| 01 §11 | OQ-R3 open; OQ-R1 ✅ (D-12), OQ-R2 ✅ (D-14) | File naming (spelling and Summary length closed) |
| 02 §9 | OQ-P1 – P3 | SRE training details, fintech lens, MEPS+ flows |
| 04 §7 | OQ-L1 – L6 | Page numbers, heading size, other layouts |
| 05 §11 | OQ-J1 – J2 | Job-search filters, lead-with evidence |

---

## 1. Source Coverage

| Source | Read? | Notes |
|---|---|---|
| `wilson-en-t-d-2022-new.docx` [R22] | ✅ Fully read (body, headers, tables; no comments or tracked changes) | Original kept unchanged |
| Software Designer certificate PDF, 11 pages incl. notarised translation [CERT-SS] | ✅ All key pages viewed (scanned images) | National ID, date of birth and certificate/file numbers deliberately not reproduced |
| British Council certificate, receipt and booking (2 PDFs) [CERT-BC] | ✅ | Receipt amounts and customer number not reproduced (not career data) |
| Shared session `claude.ai/share/b87951e7…` | ✅ Opened. It is the session that built Master v1.0 from the six V5_0_0_1 libraries | The raw library text is not reachable from here; **v1.0 is used as the consolidated [LIB] source** |
| Project doc `master/Wilson_Master_Career_Profile.md` (v1.0) | ✅ | Kept unchanged |
| Local folder `C:\Users\surface\resumes` | ✅ (re-checked 2026-10-16) | Now holds the six `*_LIB_V5_0_0.docx` (text identical to V5_0_0_1), `templates/wilson-2026_TPM_Bank_template.docx` [TPL], `master/` with v1.0 and v2.0-draft |
| **Not ingested** | — | Big Data AI base `wilson-2026_BD_V3_0_0.docx`; V3_0_0 bases (Senior_Tech, Archi, TPM); the `GA` fragment with per-role reasons for leaving; all in `C:\Users\surface\OneDrive\zh\personal CV\2026\` (not connected to this session) → OQ-1.11 |

---

## 2. Conflict Register (sources disagree)

| ID | Topic | Version A | Version B | Proposed default | Risk |
|---|---|---|---|---|---|
| **CF-01** | Bachelor's major | "Mathematics" [R22] | "Information and Computing Science" [LIB] | ✅ **Resolved: Applied Mathematics (应用数学)** — neither version was exact | — |
| **CF-02** | Master's discipline | "Computer Software and Theory" [R22] | "Master of Computer Application" [LIB] | ✅ **Resolved: Computer Science and Technology (计算机科学与技术)**. English degree type: FU-4 | — |
| **CF-03** | Name | "Wilson" / "Wilson Zhang" [R22][LIB] | Legal name **Zhang Heng** on all certificates | ✅ **Resolved: resume shows "Wilson"**; legal name used on forms (surname: FU-6) | 🟢 |
| **CF-04** | Work status | Employment Pass [R22, 2022] | Singapore PR [LIB] | ✅ **Resolved: PR since 2024** | — |
| **CF-05** | Hengshunyuan dates and title | Oct 2017 – Sep 2019, Founder [LIB][CONF] | Mar 2018 – Aug 2019, Co-founder [R22] | Title ✅ **Resolved: Co-founder**. Dates: A proposed (confirmed earlier) — FU-5 | 🟢 |
| **CF-06** | AI Park start | Apr 2016 [CONF] | May 2016 [R22] | A (confirmed earlier) | 🟢 |
| **CF-07** | VV data-platform stack | **Flink** ad-order tracking + Flink causal-inference profiling [LIB] | Flume / Hive / MR / **Spark Streaming / Spark SQL** / YARN; no Flink [R22] | None — ask | 🟠 Deep technical interview risk |
| **CF-08** | Hengshunyuan cloud | AWS [LIB] | Alibaba Cloud (aliyun) [R22] | None — ask | 🟠 |
| **CF-09** | Go | "Never claim Go" [LIB] | "go" in AI Park tech stack [R22] | Keep "never claim" unless you coded Go | 🟢 |
| **CF-10** | AI Park bids won | "4+ city projects" [LIB] | "Shijiazhuang, Handan, Beijing and other" [R22] | None — need the real count | 🟢 |
| **CF-11** | GBD "200+" | "Users across 200+ regions" (live usage) [LIB] | "Supports KYC services in 200+ countries" (capability) [R22] | B (the weaker, safer claim) | 🟠 Overclaim risk |
| **CF-12** | Baidu tenure | 2014 – 2015 [LIB] | May 2014 – Dec 2014 [R22] | ✅ **Resolved: 2014 only** [CONF 2026-10-16]; months from [R22] 📄 | — |
| **CF-13** | Sohu title | Technical Leader [LIB] | Technical Leader / Project Leader [R22] | Either | 🟢 |
| **CF-14** | AI Park pilot dates | 2016 / 2017 / 2017 [CONF] | 2017 / 2018 / 2019 [R22] — after you left | A (already corrected by you) | ✅ Resolved earlier — listed for the record |
| **CF-15** | Standards verb | "Contributed to bank-wide…" [LIB Bank][CONF] | "Set … adopted company-wide" [LIB Internet] | A (locked) | ✅ Resolved earlier |
| **CF-16** | Title wording, AI Park and VV | "VP of Technical **Development**" / "Head of Technical **Development**" [CONF 2026-10-15] | "VP of Technical **Department**" / "Head of Technical **Centre/Center**" [R22][LIB] | Your latest answer (A), unless contracts say otherwise — FU-3 | 🟠 Must match the employment letter at background check |
| **CF-17** | CBPR+ lead time | "went live 2 months ahead of the deadline" (Singtel, spoken 2026-10-23) | 03 PA-01.1: MX-rich May / Aug 2025 vs SWIFT Nov 2025; "2 months ahead of plan" belongs to Baidu (PA-17.1) | B | 🟠 |
| **CF-18** | C360 / hub positioning | C360 = "customer relationship management", "small & middle merchant clients"; hub has "reconciliation" (Singtel #14, JPM #4, IFS, SCB intro) | 03 PA-05 customer-360 (wealth cross-sell, client management); 02 CF-N4 hub does not reconcile | B | 🟠 |
| **CF-19** | Hub functional scope | Routing (rail and correspondent bank), KYC enrichment, compliance validation, duplicate-check service, SWIFT gateway service (JPM #2, #5; SCB intro) | 03 PA-01: initiation, validation, enrichment, authorisation, pain.002 status; processing / settlement outside. Duplicate prevention now covered by PA-01 §2 (a) | B, until you confirm any of these is in the hub | 🟠 |
| **CF-20** | AI review 80% | "review quality / efficiency +80% by our internal measure"; "new joiners 30–40% faster" (JPM #2, IFS #7, #9) | 03 PA-07.3: senior review **time** cut by an **estimated** ~80%; ramp-up C3 open | B | 🟠 |
| **CF-21** | Migration method | "migrated data in batches over several weekends … switched over in a planned maintenance window" (JPM #2 Q10) | 03 PA-01.1 phased Blue/Green-style coexistence; PA-01.9 approved-batch migration | B, until you confirm whether a weekend-batch step existed | 🟢 |
| **CF-22** | UOB team size | "a team of around 10 engineers" (JPM #4, 2026-10-09; IFS #7) | 25 (15 + 10), 03 §0A | B; ask whether it meant CCD only | 🔴 Background check |
| **CF-23** | Stated weakness | "no lending product experience"; experience includes "quantitative trading" (IFS #9 Q5) | 03 PA-04 retail unsecured lending servicing + collections; PA-20 retired (D-16) | B | 🟠 |
| **CF-24** | Arrival in Singapore | "moved to Singapore 6 years ago" (Cloudera, 2026-07) | 02 §2: VV Technology (Singapore) from Apr 2019 | B | 🟢 |
| **CF-25** | Career start | "started my career as a (big) data engineer, about two years" (BoA, SGX) | 02 §2: Renren Senior R&D Engineer 2008–12; 01 §5 positioning rule | B | 🟠 |
| **CF-26** | Reason for leaving VV | "due to Covid the companies moved to China" (SCB intro) | 02 §6.4: the CEO moved the technical team to China; he stayed for family reasons | B | 🟢 |
| **CF-27** | Stack mismatch | Baidu on Spring Cloud with Redis and Kafka (Cloudera); AI review agent "using Spring AI" (SCB intro) | 03 PA-17: Dubbo, Resin, MongoDB, Redis, ZooKeeper, Solr (Spring Cloud released 2015); PA-07: Spring Boot + headless Claude Code | B | 🟠 |

## 3. Overlaps and Gaps

| ID | Issue | Detail |
|---|---|---|
| **TL-1** | Hengshunyuan overlaps VV | Proposed dates overlap Apr–Sep 2019 (6 months); the R22 dates overlap Apr–Aug 2019 (5 months). ✅ **Explained:** Hengshunyuan was largely dormant; VV was the primary role [CONF]. Resume handling: FU-5 |
| **TL-2** | Gap Jan 2015 – Mar 2016 (~15 months) | ✅ **Explained:** full-time study and self-development before returning to work [CONF]. ❓ Where LeMail/Letv sits on the timeline — FU-2 |
| **TL-3** | Gap Jul – Oct 2022 (~3 months) | ✅ **Explained:** caring for a family member at home [CONF] |
| **TL-4** | Pureland concurrent May 2020 – present | ✅ **Closed 2026-10-26 → D-16:** the arrangement ended before Oct 2022; removed from work history. Was: missing from the 2022 resume; overlaps VV, GBD and UOB; bank conflict-of-interest disclosure. |

## 4. Unsupported or High-Risk Claims

| ID | Claim | Source | Why it is risky | Handling until answered |
|---|---|---|---|---|
| **HR-1** | "5 years as CTO" / "Prior CTO … Chief Architect" | [R22] summary; [LIB] headlines | ✅ **Confirmed:** formal titles were VP of Technical Development (AI Park), Co-founder (Hengshunyuan) and Head of Technical Development (VV); none was CTO | **Retire "CTO" and "Chief Architect" as titles in all variants.** "Head-of-technology roles (2016–2020)" is accurate |
| **HR-2** | "Technical platforms with 10 million daily users" / "10M+ DAU" | [R22][LIB]; attributed to **AI Park and VV-Life** [CONF] | Attribution now given. But a parking platform covering 3–4 cities and 1,000+ car parks, and a VV-Life v1 launched in 2019, both reaching 10M **unique** daily users will draw hard follow-up questions | Hold until FU-1 defines the measure |
| **HR-3** | "Technical team of over 100 people" | [R22][LIB] | Probably VV's 140 — not yet confirmed | Do not use until attributed |
| **HR-4** | VV microservice framework "supporting 10 million concurrent HTTP requests" | [R22] | Extreme figure for a 0-to-1 platform; needs test evidence | Do not use |
| **HR-5** | Baidu Nuomi system "serves 5–10 million QPS" | [R22] | Implausible for a merchant-side order system (QPS vs daily requests?) | Do not use |
| **HR-6** | VV GenAI chatbot (RAG, LLM function calling) | [LIB] | Anachronism; absent from the contemporaneous R22 | Do not use |
| **HR-7** | "10+ interconnected payment domains" | [LIB] (Stripe-tailored) | Origin unclear | Do not use |
| **HR-8** | AI-assisted delivery-risk forecasting | [LIB] | No method or outcome | Do not use |
| **HR-9** | "Built a 40-person / 140-person team" | [R22] | v1.0 rule: "never quantify hiring numbers". Team size you led ≠ people you hired | Phrase as "led a team of N" once confirmed |
| **HR-10** | AI Park "1,000+ parking lots" | [R22][LIB] | Company-level figure; may post-date your Sep 2017 exit | Use only with tenure-accurate wording |
| **HR-11** | Incident "payment delay → DB connection-pool misconfiguration → pool governance → detection script" | JPM #5 prep doc | Looks like a template example; not in 03 | Do not use unless real |
| **HR-12** | "That eliminates 60% of causes" (latency) | #15 questionnaire | Invented statistic | Do not use |
| **HR-13** | "Around ten years in large tech companies … serving millions of users" | JPM #4 Q1 | Not in 03 §0A | Do not use |
| **HR-14** | "Millions of payments a day"; "UOB IT department has 3000+ employees"; "UOB is still a local bank" | JPM #4 Q4; #15 | UOB volumes are confidential (01 §7); headcount unsourced; disparaging | Do not use |
| **HR-15** | VV "angel round to Series B & C" | #15 (SCB intro) | No source | Do not use |

**Repeated in interviews (Interview Bank traps, 2026-10-26):** HR-1 (IFS #9 "18 years spanning CTO…"; SCB intro "technical architect" as a title) · HR-2 / FU-1 (SCB intro "ten million daily users") · HR-3 / HR-9 (IFS "100+ engineers"; SCB intro "100+ tech team") · HR-10 (IFS #9 "1,000+ car parks") · CF-07 (SCB intro Flink profiling) · CF-11 (IFS "200-plus regions") · 03 §0A "multi-million daily transactions" ⛔ (IFS) · 03 X-04 no coding-time share (#15, SGX "half my time"). No new IDs; handling unchanged.

---

## 5. Open Questions — in batches

### 5.0 Batch 1 answers received (2026-10-15)

| Q | Your answer | Applied as |
|---|---|---|
| OQ-1.1 | AI Park: VP of Technical Development · Hengshunyuan: Co-founder · VV: Head of Technical Development | No formal CTO; CTO/Chief Architect titles retired (HR-1) |
| OQ-1.2 | AI-Parking and VV-Life both ran 10M-DAU platforms | Attributed; measure pending (FU-1) |
| OQ-1.3 | During the overlap VV was the primary role; Hengshunyuan was largely dormant | TL-1 explained; title Co-founder (CF-05) |
| OQ-1.4 | 2015 gap: study and self-development · Jul–Oct 2022: caring for a family member | TL-2, TL-3 explained |
| OQ-1.5 | Bachelor's, Applied Mathematics, Shenyang University of Technology (2000–2004) · Master's, Computer Science and Technology, Liaoning University (2005–2008) | CF-01, CF-02 resolved |
| OQ-1.6 | "Wilson" | CF-03 resolved |
| OQ-1.7 | Singapore PR, granted 2024 | CF-04 resolved |

### 5.1 Follow-ups from Batch 1 (short)

- **FU-1 (10M DAU)** What exactly does "10M DAU" count — unique daily active users, or daily requests/events/API calls? Was it reached **during your tenure** (AI Park ended Sep 2017; VV ended Jun 2020)? Was it the peak, or designed/load-tested capacity? Accurate alternatives exist for each case (e.g. "platform designed for 10M-DAU scale"), but only the true one can be used.
- **FU-2 (LeMail/Letv)** The 2015 gap is explained as study. When were you at LeMail/Letv, and in what role? If it falls inside Jan 2015 – Mar 2016, a background check could contradict the "study" explanation. The master should record the real dates even if resumes keep omitting them.
- **FU-3 (title wording)** Which English title is on your employment letters: AI Park "VP of Technical **Development**" or "**Department**"; VV "Head of Technical **Development**" or "**Centre**"?
- **FU-4 (degree type)** If the diplomas have an English version: Bachelor of Science? Master of Engineering or Master of Science? Otherwise I'll write "Bachelor's degree, Applied Mathematics" and "Master's degree, Computer Science and Technology".
- ✅ **Closed 2026-10-17 → D-10 (option a).** **FU-5 (Hengshunyuan dates on resumes)** Pick one: (a) keep Oct 2017 – Sep 2019 and say nothing about the overlap; (b) keep the dates and add "part-time from Apr 2019"; (c) end it at Mar 2019 on resumes and keep the full dates in the master.
- ✅ **Closed 2026-10-17 → D-11 ("Wilson").** **FU-6 (name)** "Wilson" alone, or "Wilson Zhang"? Singapore recruiters usually expect a surname on the resume header.

### Batch 1 — background-check and credibility items (✅ answered — kept for the record)

- **OQ-1.1 (HR-1)** Was "CTO" ever your formal title, or the de facto scope? R22's "5 years as CTO" roughly matches AI Park → Hengshunyuan → VV (Apr 2016 – Jun 2020, about 4.2 years) or including GBD. Which roles do you count, and what did business cards or contracts say?
- **OQ-1.2 (HR-2)** "10 million daily users": which platform — Renren, Sohu CMS/News, or Baidu Nuomi? Was it the platform's total user base or the system you owned?
- **OQ-1.3 (TL-1, CF-05)** Hengshunyuan vs VV overlap: did you run Hengshunyuan part-time after joining VV, or did Hengshunyuan effectively end before Apr 2019? Which title is right — Founder or Co-founder? (If co-founder: how many co-founders, and were you the technical co-founder?)
- **OQ-1.4 (TL-2, TL-3)** One line each for Jan 2015 – Mar 2016 and Jul – Oct 2022. Should the master record LeMail/Letv (dates and title) while resumes keep omitting it?
- **OQ-1.5 (CF-01, CF-02)** Exact degree and major names as printed on your diplomas (Chinese and English if you have both).
- **OQ-1.6 (CF-03)** How should your name appear on resumes and application forms, given that certificates say Zhang Heng?
- **OQ-1.7 (CF-04)** Current Singapore status (PR?) and the year it was granted.

### Batch 2 — scope, ownership and metrics

- ✅ **Answered by PA-Q1 (2026-10-16) → 03 PA-01.3, PA-05.2, X-04.** **OQ-2.1** UOB hands-on coding: which modules did you personally write (payment-hub core, concurrency control, AI Code Review, eMemo agent), in which period, and roughly what share of your time?
- **OQ-2.2** GBD "Implement the core modules KYC, Bonus, AnA, Payment": did you code them, or lead the team that did?
- **OQ-2.3 (HR-3, HR-4, HR-5, HR-9)** Team and scale numbers:
  - VV 140 people: direct reports vs total technical org, and the functions included.
  - GBD 40 people: did that include vendors or contractors?
  - "10M concurrent HTTP" (VV) and "5–10M QPS" (Baidu): what was actually measured — peak QPS, daily requests, or a load-test target?
- ↪ **Superseded by 03 C7.** **OQ-2.4 (HR-7)** "10+ payment domains" at UOB: list them, or drop the claim?
- ✅ **Closed 2026-10-26 → D-16.** **OQ-1.8 (TL-4)** Pureland: is it still active? Hours per week? Disclosed to and approved by UOB?
- **OQ-1.9** GBD: casual/social gaming or real-money iGaming? (It changes how the role is worded for banks and regulated employers.)
- **OQ-1.10 (HR-6)** VV chatbot: what was actually built (e.g. intent classification + FAQ retrieval + business API calls), or should it be removed?

### Batch 4 — from TEKsystems back-fill (2026-10-17)

- **OQ-T1 (Miro use case)** What did you use Miro for at VV, Golden Bridge and UOB — workflow/process mapping, brainstorming, retrospectives, architecture sketches? (Skills inventory §11 records use only.)
- Also re-asked on 2026-10-17, already registered: OQ-2.3 (40/140 headcount basis), FU-3 / CF-16 (title wording basis), CF-05 / CF-06 (date basis), CF-11 (200+ capability), OQ-3.8 (SQL / RHEL employer anchor).

### Batch 3 — strengthening (answer when convenient)

- **OQ-3.1** Missing numbers: latency reduction (%/ms), MTTR before/after, cloud-cost saving, how "~80% review efficiency" was measured, eMemo time saved, forecasting method and result.
- **OQ-3.2** Retail lending/collections: any outcome you can quantify?
- **OQ-3.3** C360 and VN eTax: start and end dates, team size, countries/business lines.
- **OQ-3.4** AI Park: team size; number of car parks live when you left (Sep 2017); real count of bids won (CF-10).
- **OQ-3.5 (CF-07, CF-08, CF-09)** VV: Flink or Spark (or both)? Hengshunyuan: AWS or Alibaba Cloud (or both)? AI Park: did you write Go?
- **OQ-3.6** Renren: were you in the advertising R&D team ([R22] reason for leaving)?
- **OQ-3.7** Should the personal Android apps (CamelAcademy, CAMEL 问答闯关) go into the resume library?
- 🔶 **Partly answered:** Spring Batch ✅ (PA-05.2), RHEL ✅ [CONF 2026-10-16] — see skills inventory v2.2. **OQ-3.8** Skills still without an anchor: Netty, ActiveMQ, Node.js, Oracle/PL-SQL, Maven, RHEL, Spring Batch, Spring AI, Liquibase, Amazon MQ, RAG, LangChain, vector DBs, SOA, Informatica — where were they used, if anywhere?
- **OQ-1.11** Should I also ingest the V3_0_0 bases and the BD library from your OneDrive folder? That needs folder access for `C:\Users\surface\OneDrive\zh\personal CV\2026\`.

---

### Batch 5 — Interview Bank back-fill (2026-10-26)

Source: `Interview Bank\inbox\2026-10-25_old-qa\Fact_Update_Proposal.md` (temp IDs SB / SA / SI / SD) and `Interview Bank\prep\_story-build\Fact_Update_Proposal.md` (IB). Review: `fact-updates\2026-10-26_interview-bank-backfill\`.

| ID | From | Question | Default until answered |
|---|---|---|---|
| OQ-5.1 | SB-04 | P1 example: was the messaging-channel fix done by his team or by the channel team? | `{…}` slot in 03 X-06 |
| OQ-5.2 | SI-03 | MT/MX coexistence reconciliation: which team ran it, at which stage? | Interview use only |
| OQ-5.3 | SA-03 | AI review controls: is the model endpoint inside the bank's network (private link / internal gateway) or an external in-region cloud endpoint? How do "no outbound network access" and "code never leaves the bank's network" hold? How is the rejection rate computed; how is false-positive suppression done? | Four sub-points held (03 PA-07 §6) |
| OQ-5.4 | SA-01(d), SB-10 / SA-10, SA-12, SI-07, SD-18 | UOB stack: MQ product? Database (Oracle)? Kafka / Redis on his platforms ("a separate team manages Kafka")? SFTP gateway, Axway API gateway + JWT, SSL hardware gateway? | Not anchored; skills unchanged |
| OQ-5.5 | SB-12 | Are squad leads / EMs also vendor staff? For vendor staff, what does "performance management" cover — input to vendor year-end reviews (X-05) or direct performance management? | New resumes: "1:1s and mentoring" only |
| OQ-5.6 | SC-03 | Besides his teams, is there an ops / L1 desk? | 02 CF-N3 unchanged |
| OQ-5.7 | SD-01 | Requirement-conflict example: were the India developers his vendor offshore team or the collaborating teams in X-02? Which platform, which year? | "offshore developers in India", no platform / year |
| OQ-5.8 | SD-02 | "High-severity issues resolved within half a day": target or actual? | Recorded as a target |
| OQ-5.9 | SB-08 | MVP prioritisation deadlock → trade-offs presented to a senior stakeholder for decision: real practice? | Not stored |
| OQ-5.10 | SB-09 | "In internet companies, led tech and infra team for website environment build": which company? | Not stored |
| OQ-5.11 | SB-11 | Release practice: deploy and verify on standby first; brief production support; rollout + rollback plans; Splunk and server monitoring after go-live — real? | Not stored |
| OQ-5.12 | SA-04 (= C4) | AI review rollout: one squad first, prompts tuned to cut noise, then expanded on request — real? Do all 25 use it? | C4 stays open |
| OQ-5.13 | SA-11 | UOB environment mainly private (not public cloud); hands-on AWS from GBD / VV? | Not stored |
| OQ-5.14 | SA-13 | A "BAU" environment with production-like data; GenAI used to generate test data? | Not stored |
| OQ-5.15 | SA-14 | Built a Spring AI architecture locally and on AWS outside work? (PA-21) | Not stored |
| OQ-5.16 | SA-17 | A legacy application produced production incidents almost every month? | Not stored |
| OQ-5.17 | SI-04 | People practice: hire for the gap, goal / deadline / boundary, 1:1s, fair pay, technical mentoring, "helped squad leads grow into managers" — which are true? | Not stored |
| OQ-5.18 | SI-05 (+ IB-02) | Vendor practice: interview embedded vendor staff, customer data in-house, contract clauses (source code, documentation, exit, audit), defect / stability tracking, daily stand-ups + weekly reviews — which are true? A concrete vendor performance issue? | Not stored |
| OQ-5.19 | SI-06 | BAU vs project backlog reviewed with the business every two weeks? | Not stored |
| OQ-5.20 | SI-09 | "AI writes the first pass on code and tests; engineers review" — team practice? | Not stored |
| OQ-5.21 | SD-03 | AI-assisted refactoring of legacy middleware into reusable APIs; prototype test generation from user stories? | Not stored |
| OQ-5.22 | SD-04 | Research on inward / outward ISO 20022 flows and reports; AI-agent ideas proposed in 2025; department AI team from May 2026 with him as a coding member? | Not stored |
| OQ-5.23 | SD-06 | Two squads, each with a squad lead; 20–30-minute stand-ups; two-week sprints; retrospectives? | Not stored |
| OQ-5.24 | SD-07 + IB-11 | JUnit coverage ≥ 90%? Third-party penetration-test reports? Jenkins deploys JARs; Aldon (Rocket) manages packages? "SonarQube 100%" = used in every pipeline, or a coverage threshold? Is the 99% gate new-code or overall? | 03 PA-03.2 / §0A unchanged |
| OQ-5.25 | IB-12 | "CEW has 50+ code components": change §0A "~50" to "50+"? Scope = hub only (closes the module part of C6)? "~20 core modules in depth" unchanged? | 03 X-04 unchanged |
| OQ-5.26 | IB-05 | Latency: figure, root cause, own part O1 vs O2, C7 concurrency-control module | 03 PA-01.4 unchanged |
| OQ-5.27 | IB-06 | DR drill frequency, scope, RTO / RPO; MTTR before / after | Unchanged |
| OQ-5.28 | IB-07 | Cloudera: alternatives and criteria; C5 led the 2022 launch or took over | Unchanged |
| OQ-5.29 | IB-08 | PA-04 technology, challenges, outcomes; which team owns lending / collections (C6); one concrete two-line schedule conflict | Unchanged |
| OQ-5.30 | IB-13, IB-14, IB-15, IB-16 | Baidu takeover problems; VV reconciliation design (frequency, exception handling); C1–C4 remainder and noise handling; cutover-readiness gate criteria and any CBPR+ critical-path near-miss | Unchanged |
| OQ-5.31 | SB-02, SB-03, SB-06, SB-07 | Confirmed 2026-10-19 but not in this round: urgent changes after P1 / P2; no PET / pre-production rehearsal in the ISO 20022 programme; reason for leaving GBD (caring for parents' health; external "family reasons"); PMP exam not scheduled. Apply in a later round? | Not stored this round |

IB-09 (= CF-11) and IB-10 (= OQ-2.3) are already registered.

## 6. Items Already Confirmed in Earlier Sessions (carried forward, not re-asked)

AI Park 2016.4 – 2017.9 and pilots 2016/2017/2017 · Hengshunyuan 2017.10 – 2019.09 (dates) · Apache Camel in UOB production · led DR/failover drills · managed squad leads/EMs incl. dotted-line · contributed to bank-wide standards · no Istio/Envoy · budget ownership at UOB, GBD, VV, AI Park · encryption, credential-management and data-migration controls led at UOB, GBD, VV/AI Park · PMP in progress; no AWS certification · React hands-on; Swift/Kotlin familiarity · 5+ years offshore management · AI Code Review metrics and governance rule · positioning rule (not an "AI/big data engineer").

## 7. Change Log
| Version | Date | Change |
|---|---|---|
| v2.1-DRAFT | 2026-10-15 | Batch 1 answers applied. |
| v2.2 | 2026-10-16 | Made the single question/decision register: added §0 decision log (D-01 – D-08) and §0A open-question index across all files; source coverage refreshed; CF-12 resolved; OQ-2.1 marked answered, OQ-2.4 superseded by C7, OQ-3.8 partly answered. Nothing removed. |
| v2.3 | 2026-10-17 | TEKsystems back-fill: D-09 (no US-team claim), D-10 (FU-5 closed), D-11 (FU-6 closed); C4 partly answered (03 v4.1). Nothing removed. |
| v2.4 | 2026-10-20 | Readability-standard back-fill: D-12 (spelling), D-13 (readability standard), D-14 (Summary length); OQ-R1 and OQ-R2 closed in 01 §11. Nothing removed. |
| v2.5 | 2026-10-26 | D-15 (CRQ / CAB personal duty, 03 v4.2 PA-03.5). Nothing removed. |
| v2.6 | 2026-10-26 | Interview Bank back-fill: D-16 (Pureland removed; TL-4 and OQ-1.8 closed), D-17 (confirmed facts applied); CF-17 – CF-27; HR-11 – HR-15 plus a "repeated in interviews" note under §4; Batch 5 OQ-5.1 – OQ-5.31; §0A index row. Nothing removed. |
