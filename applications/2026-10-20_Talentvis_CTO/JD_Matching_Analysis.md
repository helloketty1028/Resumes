# JD Matching Analysis — Talentvis (client: enterprise AI software co.) · CTO · JobStreet 95342414

**Date:** 2026-10-20 · **Stage:** 1 (analysis & positioning) — awaiting approval gate 1
**JD completeness:** full posting read (JD.md). Client company not named → no company research possible.

## 0. Sources actually read (local = authoritative)
| File | Local version | Project-knowledge copy |
|---|---|---|
| master/v2.0-draft/01_Resume_Master_Rules.md | v1.0 (2026-10-16) | v1.0 — same |
| master/v2.0-draft/02_Candidate_Profile.md | **v3.1** (2026-10-17) | v3.0 — older (lacks D-11 name decision) |
| master/v2.0-draft/03_Achievement_Library.md | **v4.1** (2026-10-17) | v4.0 — older (lacks PA-07 go-live May 2026 + approval, PA-08 O1 / Apr 2026, X-02 cross-time-zone) |
| master/v2.0-draft/04_Resume_Layout_Spec.md | **v1.1** (2026-10-17) | v1.0 — older |
| master/v2.0-draft/05_JD_Keyword_and_Matching_Rules.md | v1.0 | v1.0 — same |
| master/v2.0-draft/technical-skills-inventory.md | **v2.3** | v2.2 — older (lacks Miro) |
| master/v2.0-draft/fact-check-and-open-questions.md | **v2.3** | v2.2 — older (lacks D-09–D-11) |
Layout reference: templates/wilson-2026_TPM_Bank_template.docx (layout only). Project-knowledge copies not used as fact sources.

## 1. Classification
- **Family: SM (Senior Manager)** — C-suite role owning technology strategy, org, roadmap, board/investor communication. Strong **ATL** overlay: "hands-on", architecture reviews, code/system design, debugging.
- **Lens: INT** — product-led enterprise AI software start-up / growth-stage (not a bank or fintech). Bank evidence used for enterprise-grade security, compliance and reliability; bank jargon explained or removed.
- Headline may name the **target** role (CTO is the JD's role, 01 §5 / 02 §7.2 note); no historical CTO title anywhere.

## 2. Fast-reject screen (05 §4)
- **Partial hit — "GPU/model-inference infrastructure as a core requirement":** JD intro asks to "design production inference architectures"; responsibility 1 lists model selection, fine-tuning and inference optimization; preferred: local model / on-device inference. These sit **alongside** agentic workflows, cloud, security, team and business leadership, so inference infra is one pillar, not the sole core. → reported; user decides whether to continue.
- Other signals (C#/.NET, kdb+, Murex, manufacturing, Azure/Databricks CDAO, CFO-AI, logistics, SAS) — no hit.
- Job-search filter (05 §9, recorded not enforced): S$14–20k, permanent full-time, head-of-technology title, non-bank → consistent with the recorded filter.

## 3. JD breakdown
**Required:** R1 AI platform roadmap (model selection, fine-tuning, RAG, agentic workflows, inference optimization, cloud AWS/Azure/GCP) · R2 hands-on architecture review, code/system design, debugging · R3 data privacy, access control, auditability, compliance, cloud/hybrid/on-prem deployment models · R4 scale/mentor/lead distributed engineering + AI team; metrics & standards · R5 translate tech to business value (CEO, board) · R6 customer pilots, investor technical DD, vendor/build-vs-buy · R7 8–12+ yrs engineering · R8 ≥5 yrs senior executive or technical leadership (CTO / VPE / Head of AI) · R9 hands-on design & shipping of production LLM systems, RAG or multi-model GenAI · R10 coding depth: backend, APIs, cloud-native, databases/data pipelines · R11 enterprise requirements: security, SOC2/privacy, scalability, reliability · R12 early/growth-stage execution.
**Preferred:** P1 funding rounds / technical DD / major platform scaling · P2 local model deployment / on-device inference · P3 privacy-sensitive / highly regulated industry.
**Eligibility / screening:** E1 right to work (SG PR ✅) · E2 expected salary · E3 "years of AI Engineering experience" (screening question — answer must be truthful; see §7).
**Seniority signals (Inferred):** reports to CEO/board; C-suite peer; team size not stated (early/growth stage → likely tens, not hundreds).

## 4. Evidence matrix
| # | JD requirement (JD wording) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | "agentic workflows" | Req | PA-07.1 (headless Claude Code agents orchestrated by Spring Boot, live May 2026), PA-08 (AI agent, O1, Apr 2026) | **Direct** | Summary, SA-1/2, UOB | agentic workflows, LLM agents |
| 2 | "model selection, fine-tuning, RAG frameworks, inference optimization" | Req | RAG / LangChain / vector DB = ❓ skills inventory; no model-selection, fine-tuning or inference record | **Gap / Unverified** | not claimed | — |
| 3 | "cloud infrastructure (AWS/Azure/GCP)" | Req | GBD AWS stack (A), VV AWS (A/P); Azure X; GCP none | **Direct (AWS)** / Gap (Azure, GCP) | Skills, GBD, VV | AWS, cloud-native |
| 4 | "own the end-to-end … platform roadmap" | Req | PA-11.1 technology selection + budget (VV), PA-16.1 (AI Park), PA-15.1 (co-founder) | **Transferable** (platform roadmap; not an AI-model roadmap) | Summary, VV, AI Park | technology roadmap |
| 5 | "architecture reviews, code/system design, debugging, high-stakes problem-solving" | Req | X-04, PA-01.3, PA-05.2, X-06 | **Direct** | SA-3, UOB | architecture review, system design, production debugging |
| 6 | "data privacy, access controls, auditability, regulatory compliance" | Req | X-01, PA-01.3 (permission matrix), PA-03.4 (secure SDLC, DPIA, MAS TRM), PA-07.2 (human-in-the-loop, MAS FEAT) | **Direct** | SA-5, UOB | data privacy, access control, auditability |
| 7 | "deployment models (cloud, hybrid, or on-premise)" | Req | cloud (GBD/VV AWS) ✅; UOB hosting model not recorded | Direct (cloud) / **Unverified** (hybrid, on-prem) | cloud only | — |
| 8 | "scale, mentor, lead … distributed engineering and AI team; performance metrics and engineering standards" | Req | X-02 (25 engineers onshore/offshore, 1:1s, performance mgmt; India/Thailand/Indonesia collaboration), PA-03.1 (delivery KPIs), PA-03.3 (contributed to standards), PA-11.1 / PA-12 (VV org + big-data team), PA-10.3 (GBD team) | **Direct** (engineering); **Transferable** (AI team = data/big-data teams) | SA-6, UOB, VV | distributed team, engineering standards, performance metrics |
| 9 | "translate complex technical choices into business value for the CEO, board" | Req | PA-07 §4 (13-slide brief to senior management), PA-01.5 (steering-committee reporting), PA-11 (product-strategy planning with CEO) | **Direct** (CEO/senior mgmt) / Gap (board — none on record) | Summary, UOB, VV | executive communication |
| 10 | "strategic customer pilots" | Req | PA-16.2 (city bids won; pilots Shijiazhuang 2016, Handan 2017, Beijing Chaoyang 2017) | **Direct** (B2G pilots) | AI Park | customer pilots |
| 11 | "technical due diligence sessions with investors" | Req | Hengshunyuan co-founder; fundraising failed [R22] — Wilson's role not recorded | **Unverified** (Q3) | omitted unless confirmed | — |
| 12 | "vendor/build-vs-buy evaluations" | Req | X-02 (vendor selection, SOW/licence), X-05 (4 vendors governance), PA-05.1 (evaluated Cloudera), PA-11.1 (technology selection) | **Direct** | SA-6, UOB | vendor / build-vs-buy evaluation |
| 13 | "8–12+ years in software engineering" | Req | 18+ yrs (02 §1) | **Direct** | Summary | 18+ years |
| 14 | "at least 5 years in a senior executive or technical leadership role (CTO, VP of Engineering, or Head of AI)" | Req/Elig | Head-of-technology roles Apr 2016 – Jun 2020 ≈ 4 yrs 3 mths (AI Park VP Tech Dev, Hengshunyuan Co-founder, VV Head of Tech Dev); + GBD PM & Architect (2020–22) + UOB VP2 (2022–) | **Transferable / borderline**: executive-titled ≈ 4.25 yrs; technical leadership ≥ 10 yrs | Summary ("head-of-technology roles 2016–2020", "VP-level") | head-of-technology |
| 15 | "hands-on experience designing and shipping production LLM-based systems" | Req | PA-07.1 (O1+O2, production since May 2026, formal architecture/risk approval), PA-08 (O1) | **Direct, but recent and narrow** (2 internal agentic systems on Claude) | SA-1/2, UOB first block | production LLM-based systems |
| 16 | "RAG pipelines, or multi-model generative AI architectures" | Req (OR) | RAG ❓; multi-model ❓ (PA-07 combines SonarQube static analysis + LLM — hybrid, not multi-model) | **Gap / Unverified** (Q2) | not claimed | — |
| 17 | "backend systems, APIs, cloud-native …, modern database/data pipelines" | Req | Java career; PA-01.2/01.3 (APIs), PA-05.2 (Spring Batch), PA-12 (Spark/Hive pipeline, R22 version), PA-10.1 (Spring Cloud, K8s, AWS) | **Direct** | Skills, all roles | backend, APIs, data pipelines |
| 18 | "security, SOC2/privacy frameworks, scalability, and high reliability" | Req | PA-02.1 (99.9%+ availability, DR drills), PA-01.1 (no service interruption at cutover), X-01, MAS TRM; PCI-DSS/ISO 27001 working knowledge only; **SOC2 none** | **Direct** (security, reliability) / **Gap** (SOC2) | SA-5, UOB | high reliability, privacy |
| 19 | "early- to growth-stage environment where speed … direct execution matter" | Req | PA-16, PA-15, PA-11, PA-10 (four start-up / scale-up builds 2016–2022) | **Direct** | Summary, Experience | 0-to-1, start-up |
| 20 | "guiding a startup through funding rounds, technical due diligence, or significant platform scaling" | Pref | PA-15 (co-founder; ~100k peak DAU; fundraising failed), PA-11 (platform built from scratch); 10M DAU ⛔ (FU-1) | **Partial** — platform build yes; funding/DD unverified | Hengshunyuan, VV | platform scaling (qualitative) |
| 21 | "local model deployment, on-device inference" | Pref | none | **Gap** | not claimed | — |
| 22 | "privacy-sensitive/ highly-regulated industry environments" | Pref | UOB MAS-regulated bank; PA-07 under MAS FEAT | **Direct** | Summary, UOB | highly regulated |
| E1 | right to work | Elig | Singapore PR since 2024 (02 §1) | **Direct** | header | Singapore PR |
| E3 | "years of AI Engineering experience" | Elig (screening) | production LLM work at UOB (go-live May 2026); earlier applied AI = integration of AI recognition step (AI Park), big-data/analytics (VV) | answer honestly — see §7 | form only | — |

## 5. Three-dimension assessment (no score)
**1. Job fit**
- Strong: hands-on technology leadership (X-04), four start-up/scale-up builds incl. co-founder, cloud-native backend depth, enterprise-grade security/compliance/reliability from a MAS-regulated bank, vendor/build-vs-buy authority, distributed teams.
- Real but thin: production LLM/agentic systems — two internal systems (AI code review, document-validation agent), both 2026, single LLM provider.
- Gaps: fine-tuning, model selection, RAG, inference optimization, local/on-device models, multi-model architecture, SOC2, Azure/GCP depth, board and investor due-diligence experience (unverified).
- Seniority: last C-level-type role ended Jun 2020; current role is VP-level delivery leadership inside a bank, not a start-up executive. Executive-titled tenure ≈ 4.25 yrs vs "≥5 yrs".
- Net: competitive as a **hands-on technology leader who has shipped governed agentic AI**, not as an AI/ML-platform specialist. Shortlisting risk is mainly the AI-model-stack depth the JD lists first.

**2. Factual-reliability risks**
- Must not write CTO as a past title; must not imply ≥5 yrs as CTO.
- Must not list RAG / LangChain / vector DBs / fine-tuning (❓ or none).
- "AI team": only big-data/data-analysis teams are on record — keep as "engineering and data teams".
- VV 140 / GBD 40 team sizes: Project memory records them as total headcount (direct reports ≤15–20); 03 still shows OQ-2.3 ❓ → wording "technology organisation of 140" only if confirmed (Q4).
- 10M DAU, 10M concurrent HTTP, 5–10M QPS, 1,000+ car parks: all ⛔ — not used.
- PA-07 metrics: "~80%" kept as an **estimate**; defect 70–80% (C1 ❓) and ramp-up 30–40% (C3) not used.
- Screening Q "years of AI Engineering" must agree with the resume (no inflated bucket).

**3. Expected document difficulties**
- INT lens: CBPR+/ISO 20022/MAS TRM need plain-English framing; UOB block reordered AI-first.
- Hengshunyuan promoted from one-liner to a short role (co-founder evidence matters for a start-up CTO).
- Standard margins (04 v1.1) + richer start-up sections → page-4 risk; compress via 05 §6 ladder (UOB 8–10 bullets, older roles one line).

## 6. Positioning recommendation
**Headline (choose one):**
- **A (recommended, 🔶 adapted from SM×INT, names target only):** Hands-On Technology Executive — Enterprise Platforms & Production Agentic AI | Start-up Head of Technology · Tier-1 Regulated-Bank Rigour · Cloud-Native Architecture
- **B (📄 SM×INT option 3, verbatim):** Head of Technology — Fintech & Payments Platforms | Tier-1 Bank Rigour with Start-Up Speed · Real-Time Systems · Production AI  *(less AI-product framing)*
- **C (🔶 names target role explicitly):** Technology Leader for CTO Roles — Building Enterprise Platforms, Teams and Governed Agentic AI | Hands-On Architect · 0-to-1 Start-ups · Regulated Delivery

**Summary storyline (narrative, ~1/3–1/2 page):** 18 years from engineer to technology head → engineering and tech-lead years at Renren, Sohu, Baidu → four start-up/scale-up builds 2016–2022 (smart-parking IoT with AI recognition and city pilots; co-founded audio-learning platform to ~100k peak DAU; built VV's technology org, microservices and big-data platform; 0-to-1 multi-tenant SaaS on AWS) → since 2022 VP-level technology leader in a Tier-1 MAS-regulated bank: 25 engineers, mission-critical payments, and designed/built governed agentic AI in production → offer: start-up speed with enterprise-grade security, compliance and reliability.

**Selected Achievements (7, in order):**
1. PA-07.1 + PA-07.2 + PA-07.3 — production agentic AI code-review service, human-in-the-loop governance, formal approval, est. ~80% senior review time saved
2. PA-08 — personally built AI agent for document validation
3. X-04 + PA-01.3 — hands-on: daily review of ~50 modules, core-module coding, production debugging
4. PA-11.1 + PA-12 — built VV technology organisation, microservices and big-data platform from scratch
5. PA-10.1 — 0-to-1 multi-tenant SaaS on AWS (KYC, payments, analytics)
6. X-01 + PA-03.4 + PA-02.1 — enterprise-grade security, privacy, access control, compliance; 99.9%+ availability
7. X-02 + X-05 + PA-05.1 — leader of leaders across distributed teams; vendor selection and build-vs-buy authority

**Experience priorities:**
- UOB (8–10 bullets): AI block first (PA-07, PA-08) → hands-on/architecture (X-04, PA-01.2/01.3) → reliability (PA-01.1, PA-02.1, X-06) → security/compliance (X-01, PA-03.4) → leadership/commercial (X-02, X-05) → quality KPIs (PA-03.1). Drop PA-04, PA-06, PA-05 detail to one line.
- GBD (4 bullets): PA-10.1, PA-10.2, PA-10.3 (team number per Q4).
- VV (5–6): PA-11.1, PA-11.2, PA-11.4, PA-12 (R22 Spark version), PA-13, PA-11.5.
- Hengshunyuan (2): PA-15.1, PA-15.2 (promoted to main experience).
- AI Park (4–5): PA-16.1, PA-16.2, PA-16.3, PA-16.4.
- Baidu / Sohu / Renren: one line each (PA-17.1, PA-18.1, PA-19).
- **Excluded:** PA-20 Pureland (⛔ disclosure plan), X-03 crypto (not relevant), PA-09 / PA-14 (⛔), PA-04 lending detail, PA-06 VN eTax (low relevance), PA-21 personal apps (on-request — see Q5).

**Gap handling (05 §7):** RAG / fine-tuning / inference / on-device / multi-model / SOC2 / Azure-GCP depth — not claimed; Summary frames AI as **applied, governed agentic delivery**. Exec tenure — state "head-of-technology roles (2016–2020)" + "VP-level since 2022"; never "5 years as CTO". Funding/DD — only if Q3 confirms.

## 7. Questions for confirmation (default if unanswered)
- **Q1 Fast-reject partial hit (inference/fine-tuning in roadmap):** continue? — Default: continue; gaps stay visible, not worded around.
- **Q2 RAG / model selection / multi-model:** any real use (e.g. evaluating several LLMs for the review service, retrieval of coding standards into prompts, more than one model in PA-08)? — Default: not claimed.
- **Q3 Investor / fundraising work at Hengshunyuan (or VV):** did you pitch investors or prepare technical DD material? — Default: omitted.
- **Q4 Team sizes:** use "built and led a 140-person technology organisation" (VV) and "40-person project team" (GBD) as total headcount, direct reports ≤15–20? — Default: use with "organisation / team of N" wording (not "hired"), and log in Fact_Update_Proposal.
- **Q5 Personal Android apps (PA-21, incl. multi-agent AI quiz on the Anthropic Messages API, on Google Play):** include one line as current hands-on AI evidence? — Default: excluded (on-request).
- **Q6 Headline:** A / B / C? — Default: A.
- **Note E3 (screening question "years of AI Engineering"):** production LLM/agent work is 2026 at UOB; earlier AI-adjacent work is integration/data, not AI engineering. Choose the truthful bucket; the resume will not state an AI-engineering year count.
