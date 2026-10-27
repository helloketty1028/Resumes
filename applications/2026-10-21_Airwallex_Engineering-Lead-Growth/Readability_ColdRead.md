# Cold-read 06 — Airwallex Engineering Lead/Manager, Growth (SG/SH)

Inputs read: resume `wilson-2026_SM_Internet_Airwallex_V1_0_0_draft.txt` and `06_Airwallex_JD.md`. Red change-markup ignored. The JD has no requirements section, so I judged against the 8 responsibilities and the "Attributes We Value" paragraph.

## VERDICT: REVISE

The recruiter can name three matches, so that test passes. The second test fails: I quote five sentences a non-engineer recruiter could not follow or would stumble on (more than two). Page 1 is readable. The jargon sits in the Achievements bullets and in a few Experience bullets.

---

## (a) HR recruiter, 30 seconds

**1. Who is he.** He is a senior engineering leader with 18+ years of experience. He is a Vice President (VP2) at UOB, a Tier-1 bank, since Oct 2022. He leads about 25 onshore and offshore engineers on payment and lending platforms, and he still writes and reviews code. Earlier he was a start-up and scale-up tech head and co-founder (consumer and fintech) in Singapore and China. The headline "Engineering Lead — Consumer & Fintech Platforms" matches the way the page reads. He is Singapore PR.

**2. Three strongest matches to the JD.**
1. **Leading engineers with a people-management loop** (JD 1, 7, partly 8). The resume shows 25 engineers led through squad leads and engineering managers, 1:1s, mentoring and performance management. It also shows 140-person and 40-person organisations earlier.
2. **Hands-on design plus code review** (JD 3, 4, 5). He reviews core pull requests daily, co-designs solutions, and personally built the payment hub's core modules. He also built the AI code-review service that is in production.
3. **Working with product owners on requirements, backlog and plans** (JD 2, 6), and the "use AI" attribute. He turns requirements into technical solutions, backlogs and release plans. The AI code-review service doubles as the "uses AI to work smarter" signal.

Consumer, onboarding and KYC experience is a fourth, softer match to the Growth team's "onboarding" theme.

**3. Biggest doubt.** The Growth domain is missing. The JD is about user acquisition, funnels, experimentation, A/B testing frameworks, marketing-platform integrations and high-traffic pages. The resume has no growth, funnel, experimentation or marketing work. The only "A/B" is prompt A/B testing for the AI reviewer. Second doubt: his current title reads "Technical Delivery Manager" at VP level in a bank, so a recruiter may wonder whether he is an engineering lead or a delivery or programme manager. That is a level and pace question for a founder-style company.

**4. Sentences I could not follow, or that are too technical for HR (quoted exactly).**
1. "Designed and built a production AI code-review service in a regulated bank: a Spring Boot service runs headless Claude Code agents on each pull request alongside SonarQube, cutting senior engineers' review time by an estimated ~80% as human review rounds fell to 1–2 per pull request."
2. "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration of cross-border payments: phased coexistence took MX-rich messaging live in May and August 2025, ahead of SWIFT's November 2025 deadline, and was retired in August 2026 with no service interruption."
3. "Established delivery KPIs — deployment frequency, MTTR, incident trend and change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate); contributed to bank-wide SDLC, coding and code-review standards."
4. "Coordinate P1–P3 production incidents end to end — escalation, stakeholder communication, RCA and post-incident reports; with no separate SRE team, the platform teams own production support, SLIs/SLOs and Splunk-based monitoring."
5. "Led VV's 140-person technology organisation (total headcount) and, at Golden Bridge, a 40-person project team (total headcount), introducing Agile/Scrum from scratch and CI on Jenkins and Amazon ECR."

Borderline: the "Hands-On Engineering" keyword row and "personally built the payment hub's core modules — transaction initiation, concurrency control, the corporate- and user-role permission matrix and status processing." I read these as ATS keywords and skipped them, so I did not count them.

---

## (b) Hiring manager, about 3 minutes

**1. Can he do this job?**

| JD responsibility | Evidence | Strength |
|---|---|---|
| 1. Lead a team, set goals, give feedback and development plans | 25 engineers via squad leads and EMs; 1:1s, mentoring, performance management | Strong |
| 2. Work with PMs to analyse requirements and produce technical solutions and execution plan | Requirements and solution design with product owners; release plans; MVP scoping | Strong |
| 3. Hands-on design, implement, deliver | Payment hub core modules; customer-360 data-analysis module and Spring Batch jobs; AI code-review service | Strong |
| 4. Analyse and validate team technical designs | "co-design solutions with engineers and own the architecture"; formal architecture and risk approval | Good |
| 5. Review code, ensure standards | Reviews core pull requests daily; code-review standards; AI reviewer | Strong |
| 6. Build a backlog with the PM toward the roadmap | Backlog prioritisation and sprint planning with product owners | Good |
| 7. Hiring, training, development | Mentoring and coaching teams on AI-assisted engineering. Hiring and interviewing are not shown anywhere. | Thin |
| 8. Collaboration with local/global engineering, infra and PM teams | India, Thailand and Indonesia teams; infra, ops, compliance, architecture | Good |
| Growth domain: acquisition funnels, onboarding optimisation, A/B frameworks, marketing platforms, high-traffic pages | Only KYC/onboarding rules (Golden Bridge), the 100k DAU consumer app, and millisecond response-time tuning. No experimentation or funnel metrics. | Missing / thin |
| "Builder", "zero-to-one", "get stuff done" | Golden Bridge 0 to 1, VV-Life first release, audio-learning app from market research to production | Good |

**2. Hard red flags.**
- **Domain mismatch.** The resume has no growth, experimentation or marketing-technology evidence, and the JD is built around those.
- **Role-shape ambiguity.** The headline says hands-on lead, but the current job title is "Vice President / Technical Delivery Manager" and many bullets are governance (change control, KPI reporting, escalation). I would want to know how much he codes today.
- **Headcount inconsistency.** The Summary says "leading 25 onshore and offshore engineers". Experience says "Lead two onshore/offshore teams" and separately "10-engineer backend team". It is not clear how many are direct reports or what the 25 breaks down into.
- **Dates and gaps.**
  - Co-founder (Oct 2017 – Sep 2019) overlaps VV Technology (Apr 2019 – Jun 2020) by about five months.
  - There is a gap of about 16 months between Baidu (ends Dec 2014) and AI Park (starts Apr 2016).
  - There is a gap of about 4 months between VV (Jun 2020) and Golden Bridge (Nov 2020).
  - Several stints are short: Baidu 7 months, VV 14 months, Golden Bridge 20 months.
- **Soft overstatement flags.**
  - "99% SonarQube coverage gate" is unusually high and reads like a typo or an aspiration.
  - "~80% ... estimated" is an estimate of unclear basis.
  - "(total headcount)" suggests the numbers include people he did not directly manage.
- **Possible level and pace mismatch.** A bank VP with a 25-person remit moving to run one Growth squad at a founder-style company. The resume does not say why.

**3. Interview questions.**
1. Walk me through any experimentation or A/B work you have owned: funnel metrics, experiment platform, what you shipped and what moved. What would you do in your first 90 days on a Growth team?
2. In the last 12 months, what code did you personally write and merge to production? Roughly what share of your week is coding, design and review versus governance?
3. Of the 25 engineers, how many report to you, how many are managers, and how do you set goals and run performance reviews? Describe a time you managed someone out or coached someone up.
4. Describe how you hire. How many engineers have you interviewed and hired, and what is your bar?
5. Why move from a VP role in a Tier-1 bank to a hands-on engineering lead role here? Explain the Oct 2017 – Sep 2019 overlap and the Dec 2014 – Apr 2016 gap, and what you would want from a fast, experiment-driven environment.

**4. Would I interview him?** **Maybe, leaning yes for a screening call.** Leadership, hands-on depth, code review, product partnership and AI use are all clearly evidenced and match six of the eight responsibilities. The call is to test Growth and experimentation depth and how much he really codes today.

---

## Suggestions (wording, order, cuts only)

**Top three wording changes**

1. Sentence (Faster code review bullet):
   > "Designed and built a production AI code-review service in a regulated bank: a Spring Boot service runs headless Claude Code agents on each pull request alongside SonarQube, cutting senior engineers' review time by an estimated ~80% as human review rounds fell to 1–2 per pull request."
   Rewrite: "Designed and built an AI code-review service now live in a regulated bank: it reviews each pull request automatically, alongside SonarQube checks, and cut senior engineers' review time by an estimated ~80% as human review rounds fell to 1–2 per pull request." The tech names (Spring Boot, headless Claude Code) already appear in Core Competencies and in the Experience section, so the Achievement line does not need them.

2. Sentence (Mission-critical migration bullet):
   > "Owned delivery of the ISO 20022 (SWIFT MT-to-MX) migration of cross-border payments: phased coexistence took MX-rich messaging live in May and August 2025, ahead of SWIFT's November 2025 deadline, and was retired in August 2026 with no service interruption."
   Rewrite: "Owned delivery of the cross-border payments move to the new ISO 20022 (SWIFT MX) message standard: went live in two phases (May and August 2025), ahead of SWIFT's November 2025 deadline, and ended the old-and-new transition period in August 2026 with no service interruption." The words "coexistence" and "retired" are ambiguous. Check my reading of "retired" with the author. This bullet is also off-topic for a Growth role, so consider moving it to the bottom of Achievements.

3. Sentence (delivery KPIs and incident bullets):
   > "Established delivery KPIs — deployment frequency, MTTR, incident trend and change-failure rate — with CI/CD quality gates (99% SonarQube coverage gate); ..."
   Rewrite: "Set delivery KPIs (release frequency, time to restore service, incident trend, change-failure rate) with automated CI/CD quality gates; contributed to bank-wide ..." Cutting the "99% SonarQube coverage gate" parenthetical removes both the jargon and the credibility risk. The paired SRE bullet reads better as: "...; with no separate SRE team, my teams own production support, service-level targets and Splunk monitoring."

**Other wording, order and cuts**
- "Led VV's 140-person technology organisation (total headcount) and, at Golden Bridge, a 40-person project team (total headcount) ..." becomes "Led VV's technology organisation (140 people in total) and Golden Bridge's project team (40 in total), introducing Agile/Scrum from scratch and CI on Jenkins and Amazon ECR."
- **Order:** the JD leads with team leadership, so move "Engineering teams at scale" up to second in Selected Achievements, directly under "Hands-on technical leadership". Move the "Mission-critical migration" bullet last (already last, keep it there).
- **Order:** in Core Competencies, move "Consumer Platforms" above "Payments" and "Cloud & Data". It is the closest thing to the Growth domain.
- **Cuts:** the Spark, Flume, Hive and MapReduce big-data bullet at VV; the "Software Designer (Intermediate)" certificate line; and the second sentence in "Earlier Experience" Baidu and Sohu details if space is needed. None of these serves a Growth engineering lead role.
- **Consistency:** the Summary says "Vice President"; Experience says "VP2". Use "Vice President (VP2)" in both or the same short form in both.

## Facts the resume does not show (questions only, nothing to add as text)
- Has he run or built any experimentation, A/B testing, funnel analytics or marketing-platform integration work (apart from prompt A/B tests)?
- How many of the 25 engineers are direct reports, and how many are engineering managers or squad leads?
- Has he hired or interviewed engineers?
- What exactly was "retired" in August 2026 in the ISO 20022 bullet?
- What explains the Dec 2014 – Apr 2016 gap and the 2019 overlap of the co-founder and VV roles?
- How was the ~80% review-time reduction estimated, and is the "99% SonarQube coverage gate" correct as written?
- Is he currently writing production code in his UOB role, and how much of his time does that take?

## Resolution (2026-10-26)

**Applied**
- Top-3 #1, AI code-review achievement: rewritten in plain language (no Spring Boot or headless Claude Code; estimated ~80% and 1–2 rounds kept).
- Top-3 #2, ISO 20022 achievement: replaced with the batch canonical sentence, which explains the side-by-side run and says what was retired ("the old path was retired in August 2026"). It stays last in Selected Achievements.
- Top-3 #3, KPI bullet: MTTR is now "mean time to recovery"; the "(99% SonarQube coverage gate)" parenthetical is cut. Incident bullet: "root-cause analysis (RCA)" and "service-level indicators/objectives (SLIs/SLOs)" are expanded.
- 140/40 bullet: "(total headcount)" replaced with the batch's readable qualifiers ("through its managers"; "including outsourced staff"). The numbers stay.
- Order: "Engineering teams at scale" moved to second place.
- Cut the VV big-data bullet and the Baidu team-list tail. Sohu reworded to the canonical form.
- Consistency: Summary now says "Vice President (VP2)".
- "Payment hub" on page 1 now reads "payment-initiation hub".

**Not applied, with reasons**
- Cutting the "Software Designer (Intermediate)" certificate: overruled. It is a verified document (02 §3; Revision Brief §1.1).
- Moving "Consumer Platforms" above Payments and Cloud & Data: it already sits above both.
- "Led VV's technology organisation (140 people in total)": the batch's canonical readable form is used instead, so all ten resumes word the qualifier the same way.
- "my teams own…" in the incident bullet: first person is not used in this resume. The existing third-person form is kept.
- Growth, experimentation, hiring and coding-share gaps: nothing added, because no evidence is on record. These stay as interview questions.
