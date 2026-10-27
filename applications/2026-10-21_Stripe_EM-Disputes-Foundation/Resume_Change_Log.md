# Resume Change Log — wilson-2026_SM_Internet_Stripe_V1_0_0_draft

**Date:** 2026-10-21 · **JD:** Stripe — Engineering Manager, Disputes Foundation · JobStreet 88429529 (posted 30d+; confirm still open)
**Card:** `cards/03.md` (tier A, batch match score 93, SM × INT) · **Folder for filing:** `2026-10-21_Stripe_EM-Disputes-Foundation`
**Base:** approved Talentvis JSON (`base_Talentvis_SM_Internet.json`, SM × INT), plus approved TEKsystems sentences where they fitted better. Red marking is done by the renderer against the Talentvis final, the TEKsystems final and [TPL]. Red means the wording was not found verbatim in one of those three approved files.
**Fact sources:** 01 v1.1 · 02 v3.1 · 03 v4.1 · 05 v1.0 · skills v2.3 · fact-check v2.4 · Drafting Brief §4 (S1–S9).

## Positioning

| Item | Decision | Source / reason |
|---|---|---|
| Family × lens | SM × INT; file stem `wilson-2026_SM_Internet_Stripe_V1_0_0` | Card; 05 §2 (OQ-P2 decided per JD: fintech hiring like an internet company) |
| Headline | Card wording kept exactly: "Engineering Manager — Payment Platforms & Production Systems \| Hands-On Java · Platform Teams · Cross-Time-Zone Delivery". This names the target role only, and no past title is changed. It is 120 characters, longer than the brief's ≈105 guide, but measures as one rendered line (501 of 510 pt). Check in Word that it does not wrap | 01 §5; Brief §6 |
| Summary | Three paragraphs (3 / 4 / 3 rendered lines). P1: hands-on EM for payment platforms, engineer → technical lead (2008–2014) → 0-to-1 team and organisation leadership (2016–2022), with no year count for development. P2: VP at UOB, 25 engineers in two platform teams, millions of accounts, hands-on, partners, production operations. P3: platforms other teams depend on, VV 140 (total headcount), breadth of payments experience | Card storyline; 02 §2; X-02; S3; S5; PA-01/04/05/10; S1 |
| Summary vs. page-1 detail | Facts detailed in the Achievements are only referenced in the Summary, in different words. The daily core-PR review is in A3, the ISO 20022 cutover in A4, India / Thailand / Indonesia in A2 and the GBD 40 in Golden Bridge. P2 says "leads production operations" so it does not repeat the incident bullet's "teams own production support". "Millions of accounts" is kept in P2 and dropped from the UOB scope line | Brief §6 "merge, don't stack"; 01 §6 |
| Summary verbs | P3 uses "Designs and delivers" (O2 + O3), not "Builds", because Golden Bridge was O2 + O3 with O1 unconfirmed (OQ-2.2) | 01 §4 |

## Content decisions

| Section | Decision | Source ID |
|---|---|---|
| Competencies (7 rows) | Engineering Management · Hands-On Engineering · Production Rigour · Platform Engineering · Payments · Developer Productivity & AI · Cloud & Data. **Order differs from the card** (card order: EM · Platform · Payments · Production · Hands-On · Cloud · AI). These rows follow the order of the JD's minimum requirements: EM / mentoring → software development → lead by example → operational rigour → extensible software, then the preferred items. RCA and DR are spelled out at first use | Brief §6; X-02; skills §1–§8; PA-02/03; S2; S1 |
| A1 Platform for other teams | Hub design for digital and branch channels (PA-01.2). Integrated with core banking, which executes settlement (S2), and with vendor and third-party banking systems. The third-party clause makes this 3 lines, kept because it is the nearest analogue to the Disputes team's work with issuers, financial partners and third parties | PA-01.2, PA-01.7, S2 |
| A2 Leading and developing engineers | Squad leads / EMs, 1:1s, mentoring, performance management; cross-time-zone collaboration with India, Thailand and Indonesia (collaboration, not line management). **Moved from 7th to 2nd** because EM experience and developing engineers are minimum requirements 1 and 3 | X-02 |
| A3 Hands-on technical leadership | S5 wording, without ~50 / ~20, plus the S6 merged module list (incl. concurrency control) | S5, S6, X-04, PA-01.3 |
| A4 Operational rigour | **Deviation:** PA-01.1 (phased migration, parallel formats until Aug 2026, no service interruption) + PA-02.1 (personally led DR drills, 99.9%+). The card had X-06 here, but X-06 detail now sits once in the UOB incident bullet, and this brings the 99.9%+ metric onto page 1. "Blue/Green-style" and "under peak load" dropped for length; the Metrics Bank row is plain "99.9%+ availability" | PA-01.1, PA-02.1, 03 §0A |
| A5 0-to-1 extensible platforms | PA-10.1 (multi-tenant SaaS for online-game businesses, no further elaboration per S9) + PA-11.4 (VV millisecond-level services) | PA-10.1, PA-11.4, S9 |
| A6 Developer productivity with AI | Designed and built; each pull request; live since May 2026 after formal architecture and risk approval; advises but never approves or merges; "an estimated ~80%". "Every" was changed back to the approved "each" so adoption scope is not implied (C4 open) | PA-07.1–07.3, S9 |
| A7 Cards and wallets | S1 only: designed and coded at Baidu Nuomi (Alipay, WeChat Pay, UnionPay) and Renren Mall (Alipay, UnionPay); at VV designed a subsystem that integrated UnionPay, Visa/Mastercard, Google Pay and GrabPay payments. WeChat Pay appears under Baidu only. No card-scheme connectivity claim. "Settlement reconciliation" was left out here because VV bullet 2 already carries "reconciliation modules". **Deviation:** the card also put S1 in the Baidu / Renren Earlier lines and the VV bullets; it is stated once, here | S1, B-02 |
| UOB scope | Approved Talentvis line minus "— serving millions of accounts" (now in Summary P2) | Talentvis; X-02 |
| UOB · Platform Engineering | (1) Customer-360: leads the 10-engineer backend team; live since 2022 (launch ownership not claimed, C5); daily account summaries from core banking for portfolio analysis; APIs for several business lines. (2) Lending and collections, approved TEK sentence (**added**: adjacent to disputes as fund recovery, and card portfolios). (3) Latency, approved sentence plus "the payment hub's" for clarity. PA-01.2 is not repeated here because it is A1 | PA-05.1, PA-05.3, S2, PA-04.1, PA-01.4 |
| UOB · Production & Delivery | (4) ISO 20022 programme delivery with the 15-engineer hub team; upgrades every 2–3 months. "RAID" written as "risks and dependencies" for the INT lens. (5) P1–P3 incidents, approved wording, with "no separate SRE team" written as "no separate reliability team" so there is no unexpanded acronym. (6) Delivery KPIs + quality gates + bank-wide standards ("contributed to"), approved Talentvis sentence (3 lines) | PA-01.5, X-06, PA-02.3, CF-N3, PA-03.1–03.3 |
| UOB · Leadership, Partners & Productivity | **Sub-heading renamed** from the card's "Team & Productivity", because people-leadership facts are on page 1 (A2). Bullets: MVP sequencing (TEK, approved); primary stakeholder interface (TEK, approved); investment / vendor-selection / SOW authority + chairs governance of four IT service vendors (buyer side only, S7); AI review production path + coaching (merged so UOB stays at 11); eMemo / quotation validation agent, personally built April 2026 (**added**: automated systems + current hands-on work) | X-02, PA-01 §9, X-05, S7, PA-07.4, PA-03 §6, PA-08, S9 |
| Golden Bridge | Three approved Talentvis bullets unchanged: 40-person project team (total headcount), KYC / rule models (no "200+"), AWS + controls | PA-10.3, S4, PA-10.2, X-01 |
| VV Technology | Title "Head of Technical Centre" (S8). Approved scope. (1) "Built VV's microservices platform from scratch, owning technology selection and the technology budget". The 140 headcount is in Summary P3 only, never next to "built" (Brief §3, HR-9). (2) Product-strategy planning + first VV-Life release 2019 with payment modules (approved). (3) Middle-platform architecture for the B2B online-office product (approved; GMS not named) (**added** in place of the card's PA-11.4, which is in A5). (4) CI/CD + incident priority levels (approved) | PA-11.1, S3, PA-11.2, PA-13, PA-11.3, PA-11.5 |
| Hengshunyuan | Full role, one approved bullet (0 to ~100k DAU) | PA-15.1, D-10 |
| AI Park | Title "VP of Technical Department" (S8). (1) Approved TEK sentence (SaaS clause dropped for length). (2) Technical bids and pilots (approved; only pre-sales experience, S7). **Deviation:** the card's PA-16.4 was replaced because it is nearly the same claim as PA-11.4 in A5 (Spring Cloud + Kafka + caching → millisecond level) | PA-16.1, PA-16.2, S7, S8 |
| Earlier Experience | Baidu: approved sentence (incl. leading web front-end, CMS and QA teams, which shows early team leadership). Sohu: shortened to 2 lines ("memcached to Redis cluster"). Renren: approved | PA-17.1, PA-18.1, PA-19 |
| Education | Four lines exactly as fixed in the brief | 02 §3 |

## Deliberately excluded

| Item | Reason |
|---|---|
| Any hiring claim, hiring numbers, "recruit" | No hiring record in 02/03 (HR-9; skills §12); JD requirement left visible as a gap (Q2 in the analysis) |
| Any year count for software development ("8+ years") | Card; record supports ~6.5 years of full-time engineering (2008–2014) plus hands-on work later |
| Dispute / chargeback wording | No evidence; adjacent experience is used instead |
| "Career development" ([LIB] Senior_Tech) | Not in 03 X-02; 03 / approved wording wins over [LIB] (Q3) |
| US-team or global partner collaboration | D-09 |
| RAG knowledge-assistant contribution (S9) | Optional per card; UOB already at the 11-bullet cap |
| ~50 / ~20 code modules | S5 / B-06: not used in this batch |
| CEW, SCV-CCD, CCD, GMS, HCL, vendor names, MEPS+, CASA, PA-01.7 context line | Confidentiality (01 §7) / brief §3 / INT lens jargon |
| 10M DAU, 10M concurrent, 5–10M QPS, 1,000+ car parks, "10+ payment domains", "100+", GBD "200+" | ⛔ / ⚠️ in 03 §0A; brief §3 |
| Flink, GenAI chatbot (PA-14), delivery-risk forecasting (PA-09) | ⚠️ / ⛔ |
| Defect 70–80% (C1), ramp-up 30–40% (C3) | Measures unconfirmed |
| X-06 "input to MAS regulatory reporting" | INT lens; not needed for this JD |
| X-01 security bullet at UOB | Not asked by the JD; the practice is shown once at Golden Bridge (approved bullet) |
| PA-05.2 customer-360 personal modules | Length; hands-on coding shown in A3 |
| PA-06 VN eTax, PA-12 big data, PA-15.2 licensing, PA-16.3–16.5 | Low relevance, near-duplicates or page budget |
| PA-20 Pureland, PA-21 personal apps, X-03 crypto | ⛔ until disclosure / on-request only |
| Direct card-scheme connectivity, POS, acquiring | Brief §3; B-02 (done by the VV team, not personally) |
| CTO / Chief Architect / "Head of" past titles | HR-1; titles exactly as in the brief |
| Earlier Stripe TPM (LPM) tailored version | Not reused; it contained "10+ interconnected payment domains" (HR-7). Consistency question raised (Q4) |

## Rendered result

- Pages: **3** (LibreOffice PDF) · page 1 = header + Summary + Competencies + all 7 Achievements · page 2 starts with PROFESSIONAL EXPERIENCE · page numbers present · no orphan headings · **Layout OK: True**
- Bullets: 31, of which **5 at 3 lines** (A1, A3, A6, UOB delivery-KPI bullet, Baidu) — within the 1-in-5 limit; Achievements 4 of 7 at 2 lines
- Summary paragraphs 3 / 4 / 3 lines; competency labels 1 line, contents ≤ 2 lines; headline 1 line
- Words: 1,231 (Summary 154). Below the 1,350–1,550 "usually fits" guide; page 3 is about one-third full, by choice, with no padding
- Lint hits: **0**
- Red runs: **43 / 96**. All of the headline, summary, competencies and achievements, except the approved label "Hands-on technical leadership", plus UOB scope, customer-360, latency, ISO 20022 delivery, incidents, investment authority, AI production path, eMemo agent, VV bullet 1 and the Sohu line. Black (approved verbatim): lending, KPI, MVP and stakeholder bullets at UOB; all Golden Bridge bullets; VV scope and bullets 2–4; Hengshunyuan; both AI Park bullets; Baidu and Renren lines; Education
- Iteration notes: first render had 12 / 31 bullets at 3 lines (all 7 achievements). These were tightened to 3 / 31, then JD-relevant detail was restored within the limits (A1 third-party clause, Summary partner clause, eMemo agent, Baidu team clause) → 5 / 31
- Not checked: rendering in Microsoft Word (headline margin is 9 pt); ATS parsing

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/03_Resume_Fact_Audit.md` (R1–R4, notes), `coldread/03_Readability_ColdRead.md` (W1–W3), `brief/Revision_Brief.md` §2. Helper scripts and the pre-revision JSON: `drafts/03/tmp/`.

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Summary P1 | "on Renren's e-commerce platform, Sohu's news CMS and Baidu's Nuomi group-buying system (2008–2014)" | "at Renren, Sohu and Baidu (2008–2014)" | Cold-read W3 (shorten) |
| Summary P3 | "Designs and delivers extensible platforms … has led VV Technology's 140-person technology organisation (total headcount)." | "Designs and delivers platforms … has led VV Technology's 140-person technology organisation through its managers." | Cold-read W1 / 4.1; audit repetition note ("extensible" ×4); canonical VV summary form |
| Comp · Hands-On Engineering | "Java, Spring Boot, Spring Cloud, Apache Camel, …" | "Java, Spring Boot, Apache Camel, …" | R1 safe default |
| Comp · Platform Engineering | "API design, microservices, event-driven …" | "API design, microservices (Spring Cloud), event-driven …" | R1 safe default |
| Comp · Production Rigour | "SLIs/SLOs, disaster-recovery (DR)" | "service-level indicators/objectives (SLIs/SLOs), disaster recovery (DR)" | Revision Brief §1.3 acronyms |
| Comp · Payments | "integration with core-banking settlement" | "hand-off to core banking for settlement" | R2 (canonical S2 competency phrase) |
| Comp · Developer Productivity & AI | "Production AI code review on headless Claude Code agents, prompt A/B evaluation, AgentOps/LLMOps practice, …" | "AI-assisted code review in production, prompt testing, human-in-the-loop governance, delivery KPIs" | Cold-read W2 / 4.6 (detail stays in the UOB bullet) |
| Achievements order | Platform design first | "Leading and developing engineers" first | Cold-read W3 (JD's first requirement is people leadership) |
| Ach · Platform for other teams | "… integrated with core banking, which executes settlement, and with vendor and third-party banking systems." | "… connecting vendor and third-party banking systems and handing payments to core banking for settlement." | Ambiguous "which" (same issue as cold-read 02); canonical S2 hand-off |
| Ach · Operational rigour | "Planned a phased ISO 20022 (SWIFT MT-to-MX) migration … running old and new formats in parallel …; personally led DR drills, sustaining 99.9%+ availability." | Shortened canonical ISO sentence ("Planned and architected the phased move … side by side until August 2026 with no service interruption") + "DR and failover drills for the real-time payment middleware, sustaining 99.9%+" | Revision Brief §2; PA-02.1 scope (cf. audit 01 F1); cold-read 2 (99.9%+ causation) |
| Ach · 0-to-1 platforms | Label "0-to-1 extensible platforms"; SaaS clause without employer; "for online-game businesses" | Label "0-to-1 platforms"; "At Golden Bridge, architected and delivered a 0-to-1 multi-tenant SaaS platform on AWS; …" | Audit notes (A5 does not name Golden Bridge; repetition); business type cut for length (GBD scope stays in the role) |
| UOB · latency | "the payment hub's end-to-end transaction latency" | "the payment-initiation hub's end-to-end transaction latency" | Revision Brief §1.3 ("the hub" at first Experience mention) |
| UOB · delivery KPIs | "MTTR … SIT/UAT sign-off" | "mean time to recovery … system and user-acceptance test sign-off" | Audit readability note (MTTR, SIT/UAT) |
| UOB · MVP sequencing | "When the two platform lines' schedules conflict, agree MVP scope …" | Canonical MVP sentence | Cold-read 4.5 / W2 (no subject); Revision Brief §2 |
| UOB · eMemo agent | "Personally built an AI agent (April 2026) that generates validation prompts …" | Cut | Cold-read W2 / 4.3 (low JD relevance, unexplained terms); UOB now 10 bullets |
| GBD · team | "Led a 40-person project team (total headcount), …" | "Led a 40-person project team, including outsourced staff, …" | Cold-read W1; canonical GBD sentence |
| GBD · KYC | "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution." | "Designed the tiered know-your-customer (KYC) identity checks and the rule models that set authentication levels and bonus eligibility, triggers and distribution." | Cold-read W2 / 4.2 (plain English; same facts) |
| GBD · AWS | "(API Gateway, EC2/ECS, RDS, DynamoDB, SQS/SNS, CloudWatch)" | "(API Gateway, ECS, RDS, DynamoDB)" | R3 safe default |
| VV · scope line | "… everyday services — through data." | "… everyday services." | Cut; removed a one-word second line |
| VV · organisation | "Built VV's microservices platform from scratch, owning …" | Canonical VV sentence ("Led VV's 140-person technology organisation through its managers and built its microservices platform from scratch, …") | Cold-read 4.1 / (b)2: the VV section did not show the 140 cited in the Summary |
| VV · B2B product | "middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS)" | "shared back-end platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ)" | Cold-read W2 / 4.4; R3; canonical VV B2B sentence |
| Earlier · Baidu | "leading the web front-end, CMS development and QA teams" | "leading the web front-end, CMS and QA teams" | Length trim (same fact) |
| Earlier · Sohu | "Led the CMS re-architecture (SSH to Spring MVC; memcached to Redis cluster) and delivered …" | "Led the re-architecture of the fifth-generation CMS onto Spring MVC and a Redis cluster, and delivered its OpenAPI messaging platform." | Canonical Sohu sentence ("Sohu's" dropped; the lead names Sohu) |

**Not changed:** Education certificate line (R4 overruled — verified 02 §3 document); header contact line and UOB title (fixed by the renderer and Drafting Brief §3); "estimated ~80%".

**Rendered result (after revision):** 3 pages · Layout OK **True** · bullets 30, at 3 lines **6** (= 1 in 5; Ach Platform for other teams, Ach Hands-on technical leadership, Ach Operational rigour, Ach Developer productivity with AI, UOB delivery KPIs, Earlier Baidu) · words 1,224 (summary 147) · line flags none · lint hits 0 · pages rasterised and viewed (`drafts/03/tmp/pg-*.png`).

**For Wilson:** (1) Did you personally write Spring Cloud code, or choose it and direct the team (R1)? (2) Is the 99% SonarQube gate on new code or all code? (3) Lens for a fintech such as Stripe: Bank or Internet (OQ-P2)? This draft keeps Internet.


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K2 steering committee (singular) | senior management and steering committees | senior management and the steering committee | C3 answer K2 (2026-10-26) |
| K5 SonarQube scope | 99% SonarQube coverage gate | 99% SonarQube coverage gate on all code | C3 answer K5 (2026-10-26) |
