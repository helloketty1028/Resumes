# Wilson Zhang — Fact-Check Register and Open Questions

**Version:** v2.1-DRAFT · 2026-10-15 · Batch 1 answered (see §5.0)
**Rule:** No conflict below has been resolved on your behalf. Where you confirmed a value in an earlier session, it is shown as the **proposed default** and still needs your reconfirmation.

---

## 1. Source Coverage

| Source | Read? | Notes |
|---|---|---|
| `wilson-en-t-d-2022-new.docx` [R22] | ✅ Fully read (body, headers, tables; no comments or tracked changes) | Original kept unchanged |
| Software Designer certificate PDF, 11 pages incl. notarised translation [CERT-SS] | ✅ All key pages viewed (scanned images) | National ID, date of birth and certificate/file numbers deliberately not reproduced |
| British Council certificate, receipt and booking (2 PDFs) [CERT-BC] | ✅ | Receipt amounts and customer number not reproduced (not career data) |
| Shared session `claude.ai/share/b87951e7…` | ✅ Opened. It is the session that built Master v1.0 from the six V5_0_0_1 libraries | The raw library text is not reachable from here; **v1.0 is used as the consolidated [LIB] source** |
| Project doc `master/Wilson_Master_Career_Profile.md` (v1.0) | ✅ | Kept unchanged |
| Local folder `C:\Users\surface\resumes` | ✅ | Contains only the v1.0 copy |
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
| **CF-12** | Baidu tenure | 2014 – 2015 [LIB] | May 2014 – Dec 2014 [R22] | B (more specific) | 🟠 Checkable |
| **CF-13** | Sohu title | Technical Leader [LIB] | Technical Leader / Project Leader [R22] | Either | 🟢 |
| **CF-14** | AI Park pilot dates | 2016 / 2017 / 2017 [CONF] | 2017 / 2018 / 2019 [R22] — after you left | A (already corrected by you) | ✅ Resolved earlier — listed for the record |
| **CF-15** | Standards verb | "Contributed to bank-wide…" [LIB Bank][CONF] | "Set … adopted company-wide" [LIB Internet] | A (locked) | ✅ Resolved earlier |
| **CF-16** | Title wording, AI Park and VV | "VP of Technical **Development**" / "Head of Technical **Development**" [CONF 2026-10-15] | "VP of Technical **Department**" / "Head of Technical **Centre/Center**" [R22][LIB] | Your latest answer (A), unless contracts say otherwise — FU-3 | 🟠 Must match the employment letter at background check |

## 3. Overlaps and Gaps

| ID | Issue | Detail |
|---|---|---|
| **TL-1** | Hengshunyuan overlaps VV | Proposed dates overlap Apr–Sep 2019 (6 months); the R22 dates overlap Apr–Aug 2019 (5 months). ✅ **Explained:** Hengshunyuan was largely dormant; VV was the primary role [CONF]. Resume handling: FU-5 |
| **TL-2** | Gap Jan 2015 – Mar 2016 (~15 months) | ✅ **Explained:** full-time study and self-development before returning to work [CONF]. ❓ Where LeMail/Letv sits on the timeline — FU-2 |
| **TL-3** | Gap Jul – Oct 2022 (~3 months) | ✅ **Explained:** caring for a family member at home [CONF] |
| **TL-4** | Pureland concurrent May 2020 – present | Missing from the 2022 resume (which should have shown it). Overlaps VV, GBD and UOB. Bank conflict-of-interest disclosure. |

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
- **FU-5 (Hengshunyuan dates on resumes)** Pick one: (a) keep Oct 2017 – Sep 2019 and say nothing about the overlap; (b) keep the dates and add "part-time from Apr 2019"; (c) end it at Mar 2019 on resumes and keep the full dates in the master.
- **FU-6 (name)** "Wilson" alone, or "Wilson Zhang"? Singapore recruiters usually expect a surname on the resume header.

### Batch 1 — background-check and credibility items (✅ answered — kept for the record)

- **OQ-1.1 (HR-1)** Was "CTO" ever your formal title, or the de facto scope? R22's "5 years as CTO" roughly matches AI Park → Hengshunyuan → VV (Apr 2016 – Jun 2020, about 4.2 years) or including GBD. Which roles do you count, and what did business cards or contracts say?
- **OQ-1.2 (HR-2)** "10 million daily users": which platform — Renren, Sohu CMS/News, or Baidu Nuomi? Was it the platform's total user base or the system you owned?
- **OQ-1.3 (TL-1, CF-05)** Hengshunyuan vs VV overlap: did you run Hengshunyuan part-time after joining VV, or did Hengshunyuan effectively end before Apr 2019? Which title is right — Founder or Co-founder? (If co-founder: how many co-founders, and were you the technical co-founder?)
- **OQ-1.4 (TL-2, TL-3)** One line each for Jan 2015 – Mar 2016 and Jul – Oct 2022. Should the master record LeMail/Letv (dates and title) while resumes keep omitting it?
- **OQ-1.5 (CF-01, CF-02)** Exact degree and major names as printed on your diplomas (Chinese and English if you have both).
- **OQ-1.6 (CF-03)** How should your name appear on resumes and application forms, given that certificates say Zhang Heng?
- **OQ-1.7 (CF-04)** Current Singapore status (PR?) and the year it was granted.

### Batch 2 — scope, ownership and metrics

- **OQ-2.1** UOB hands-on coding: which modules did you personally write (payment-hub core, concurrency control, AI Code Review, eMemo agent), in which period, and roughly what share of your time?
- **OQ-2.2** GBD "Implement the core modules KYC, Bonus, AnA, Payment": did you code them, or lead the team that did?
- **OQ-2.3 (HR-3, HR-4, HR-5, HR-9)** Team and scale numbers:
  - VV 140 people: direct reports vs total technical org, and the functions included.
  - GBD 40 people: did that include vendors or contractors?
  - "10M concurrent HTTP" (VV) and "5–10M QPS" (Baidu): what was actually measured — peak QPS, daily requests, or a load-test target?
- **OQ-2.4 (HR-7)** "10+ payment domains" at UOB: list them, or drop the claim?
- **OQ-1.8 (TL-4)** Pureland: is it still active? Hours per week? Disclosed to and approved by UOB?
- **OQ-1.9** GBD: casual/social gaming or real-money iGaming? (It changes how the role is worded for banks and regulated employers.)
- **OQ-1.10 (HR-6)** VV chatbot: what was actually built (e.g. intent classification + FAQ retrieval + business API calls), or should it be removed?

### Batch 3 — strengthening (answer when convenient)

- **OQ-3.1** Missing numbers: latency reduction (%/ms), MTTR before/after, cloud-cost saving, how "~80% review efficiency" was measured, eMemo time saved, forecasting method and result.
- **OQ-3.2** Retail lending/collections: any outcome you can quantify?
- **OQ-3.3** C360 and VN eTax: start and end dates, team size, countries/business lines.
- **OQ-3.4** AI Park: team size; number of car parks live when you left (Sep 2017); real count of bids won (CF-10).
- **OQ-3.5 (CF-07, CF-08, CF-09)** VV: Flink or Spark (or both)? Hengshunyuan: AWS or Alibaba Cloud (or both)? AI Park: did you write Go?
- **OQ-3.6** Renren: were you in the advertising R&D team ([R22] reason for leaving)?
- **OQ-3.7** Should the personal Android apps (CamelAcademy, CAMEL 问答闯关) go into the resume library?
- **OQ-3.8** Skills still without an anchor: Netty, ActiveMQ, Node.js, Oracle/PL-SQL, Maven, RHEL, Spring Batch, Spring AI, Liquibase, Amazon MQ, RAG, LangChain, vector DBs, SOA, Informatica — where were they used, if anywhere?
- **OQ-1.11** Should I also ingest the V3_0_0 bases and the BD library from your OneDrive folder? That needs folder access for `C:\Users\surface\OneDrive\zh\personal CV\2026\`.

---

## 6. Items Already Confirmed in Earlier Sessions (carried forward, not re-asked)

AI Park 2016.4 – 2017.9 and pilots 2016/2017/2017 · Hengshunyuan 2017.10 – 2019.09 (dates) · Apache Camel in UOB production · led DR/failover drills · managed squad leads/EMs incl. dotted-line · contributed to bank-wide standards · no Istio/Envoy · budget ownership at UOB, GBD, VV, AI Park · encryption, credential-management and data-migration controls led at UOB, GBD, VV/AI Park · PMP in progress; no AWS certification · React hands-on; Swift/Kotlin familiarity · 5+ years offshore management · AI Code Review metrics and governance rule · positioning rule (not an "AI/big data engineer").
