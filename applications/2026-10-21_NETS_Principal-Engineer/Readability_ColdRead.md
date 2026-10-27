# 01 NETS Principal Engineer — Cold Read

Inputs used: the resume draft text and PDF page images (3 pages), and the NETS JD. Nothing else.

**VERDICT: REVISE.** The recruiter can name three matches, but I would quote five unclear or jargon-heavy sentences (the limit is two).

## (a) HR recruiter, 30 seconds

**1. Who is he?** A very senior (VP-level), Java-based payments technologist with 18+ years of experience, based in Singapore (PR). His most recent role is Vice President (VP2) / Technical Delivery Manager at UOB since Oct 2022, running cross-border payments and retail lending platforms. The headline says "Principal Engineer", but his actual titles are VP, Head of Technical Centre and Project Manager & Architect.

**2. Three strongest matches to the JD**
1. **Payment-domain depth.** Payment-initiation hub, ISO 20022 migration, settlement integration with core banking, reconciliation, and card/e-wallet integrations (Alipay, UnionPay, Visa/Mastercard, Google Pay, GrabPay).
2. **The JD's Java stack.** Java, Spring Boot, REST, MySQL, RHEL, Docker/Kubernetes, AWS, enterprise integration patterns, Kafka and other messaging.
3. **Technical authority plus hands-on.** He owns the architecture, reviews pull requests daily, writes core modules, set bank-wide code-review standards, and does mentoring, 1:1s and vendor governance. This matches "design authority" and "remain hands-on".

**3. Biggest doubt or red flag.** The level and role type do not match. He is a VP / Delivery Manager applying for a Principal Engineer role. Page 2 reads heavily as management and delivery (RAID, vendor budget reviews, SOW negotiation). Second doubt: NETS is a card-switching and acceptance business, and the resume never mentions card authorisation, switching, POS/QR or PCI-DSS. His payments work looks bank-side and cross-border.

**4. Sentences I could not understand, or that are too technical for HR (exact quotes)**
1. "Planned and architected a phased, Blue/Green-style coexistence deployment for the ISO 20022 (SWIFT MT-to-MX) migration of cross-border payments: took MX-rich messaging live in May and August 2025, ahead of SWIFT's November 2025 deadline, and retired coexistence in August 2026 with no service interruption."
2. "With no separate SRE function, own production support for the payment platforms — SLA tracking, SLIs/SLOs, Splunk-based monitoring and alerting, and capacity baselines."
3. "Lead the 10-engineer backend team of a regional customer-360 platform live since 2022: evaluated Cloudera as its processing framework, designed the customer data models and built its data-analysis module and Spring Batch jobs."
4. "Led the re-architecture of the fifth-generation CMS (SSH to Spring MVC; memcached cluster to Redis cluster)." "SSH" reads as Secure Shell to a non-engineer.
5. "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006)". The credential is opaque, and its value is unclear.

Also unclear but not counted: "99% SonarQube coverage" (coverage of what?) and the tagline "Hands-On Java Architecture · Resilience by Design".

**Presentation note.** Much of the text on all three pages is red (summary, achievements, most UOB bullets). It looks like change markup. If this is the version a recruiter receives, it reads as an unfinished draft. Please confirm the final is black.

## (b) Hiring manager, about 3 minutes

**1. Can he do this job?**
- **Clearly evidenced:**
  - Java and Spring Boot, microservices, REST, MySQL, Redis, RHEL, Docker/Kubernetes and AWS.
  - Payment initiation, validation and settlement integration, and reconciliation.
  - ISO 20022 programme delivery, DR and failover drills, and MAS TRM / DPIA / secure SDLC.
  - CI/CD and quality gates, P1–P3 incident ownership, and code and design reviews with standards set bank-wide.
  - Vendor governance and decision authority, and mentoring, 1:1s and performance management.
- **Thin:**
  - Low-latency and high-throughput claims have no numbers (no TPS, no latency before/after). "Millisecond-level" and "99.9%+" are unscoped.
  - Multi-year modernisation roadmap: the ISO 20022 programme is the only recent example.
  - Executive communication is asserted ("Used to explaining...") rather than shown.
  - Cloud and API management: AWS only, no Azure or GCP.
- **Missing from the resume:**
  - Solace JMS (Kafka, RocketMQ and SQS appear instead).
  - PCI-DSS and tokenisation.
  - Card authorisation, switching, POS, QR, and card-scheme integration or mandates.
  - Mobile/SDK experience (advantageous only).
  - PostgreSQL (MySQL is shown, which the JD accepts).

**2. Hard red flags**
- **Title and level.** The resume is positioned as "Principal Engineer", but the last role is delivery and management. The summary says "18+ years of Java engineering", yet since 2016 every role is head-of, VP or manager.
- **Dates.**
  - Nothing is shown between Baidu (ended Dec 2014, listed under Earlier Experience) and AI Park (started Apr 2016): a gap of about 16 months.
  - Hengshunyuan (Oct 2017 – Sep 2019) overlaps VV (Apr 2019 – Jun 2020).
  - Short gaps appear in Jun–Nov 2020 and Jul–Oct 2022.
  - Four roles in 2016–2022 each lasted about 14–24 months.
- **Overstatement risks.**
  - "Personally built" the hub's core modules versus the later "write core modules for significant changes".
  - "Cut senior engineers' review time by an estimated ~80%" is an estimate and unverified.
  - "40-person" and "140-person" teams are qualified as "total headcount", which is honest but reads awkwardly.
- **Scale.** "Millions of accounts" appears, but no transaction volume is given. NETS runs 130,000+ acceptance points.

**3. Interview questions**
1. When did you last write and ship production code in the payment hub? What share of your week is code versus management? Walk me through one design trade-off you made.
2. What peak TPS and latency did the thread-pool and JVM tuning achieve, before and after? What did "99.9%+ under peak load" cover?
3. What have you done on real-time card authorisation or switching, scheme mandates, PCI-DSS and tokenisation? How would your Kafka/RocketMQ experience transfer to Solace JMS?
4. You are a VP and Technical Delivery Manager today. Why a Principal Engineer role, and how would you act as design authority across several concurrent tracks without line management?
5. Walk me through 2014–2020: the Dec 2014 – Apr 2016 period, the overlap between Hengshunyuan and VV, and the short tenures.

**4. Would I interview him?** **Yes.** The payment-hub architecture, the hands-on evidence and the governance track record fit this role. I would use the interview to test card-switching, PCI-DSS and Solace depth, and to confirm he wants to be a hands-on principal rather than a manager.

## Suggestions (wording, order, cuts only)

1. **Plain-language the ISO 20022 bullet.**
   - Current: "Planned and architected a phased, Blue/Green-style coexistence deployment for the ISO 20022 (SWIFT MT-to-MX) migration ... took MX-rich messaging live in May and August 2025 ... retired coexistence in August 2026 with no service interruption."
   - Rewrite: "Planned and architected the ISO 20022 (SWIFT MT-to-MX) migration of cross-border payments as a phased rollout, with old and new message formats running side by side. Went live in May and August 2025, ahead of SWIFT's November 2025 deadline, and ended the side-by-side running in August 2026 with no service interruption."
   - Drop "Blue/Green-style" and "MX-rich" from the Achievements version and keep them in the UOB bullet if needed. I am assuming "MX-rich" means the new richer message format.
2. **Translate the production-support and data-platform jargon.**
   - Current: "With no separate SRE function, own production support for the payment platforms — SLA tracking, SLIs/SLOs, Splunk-based monitoring and alerting, and capacity baselines."
   - Rewrite: "Own production support for the payment platforms (no separate SRE team): service-level tracking, Splunk monitoring and alerting, and capacity baselines."
   - Current: "evaluated Cloudera as its processing framework".
   - Rewrite: "chose the Cloudera big-data processing framework", or cut the clause.
3. **Cut or clarify the obscure items.**
   - Current: "(SSH to Spring MVC; memcached cluster to Redis cluster)".
   - Rewrite: "Led the re-architecture of the fifth-generation CMS to Spring MVC and Redis." Cutting the parenthetical removes the Secure Shell misreading.
   - Cut the "Software Designer (Intermediate) — Qualification Certificate of Computer and Software Technology Proficiency (2006)" line, or shorten it to "Software Designer (Intermediate), China, 2006".
   - Replace "99% SonarQube coverage" with the exact measure. If it is test coverage, say "99% unit-test coverage enforced by SonarQube quality gates" (see the question below).
4. **Order.** The headline says "Principal Engineer", so lead the Selected Achievements with "Hands-on core engineering" and put "Payment-hub design" second. The UOB block already opens with the hands-on bullets, so keep that order.
5. **Cut.** Remove the Core Competencies row "Technical Leadership", which repeats Achievements and the UOB bullets. Remove or shorten the tagline "Resilience by Design". Shorten the third summary paragraph, which runs to five lines of career history.

## Facts the resume does not show (questions, not text to add)

- What peak TPS, latency before/after and availability scope back the performance and 99.9%+ claims?
- Has he worked on card authorisation, switching, POS/QR, PCI-DSS or tokenisation, even indirectly, and has he used Solace JMS?
- What does "99% SonarQube coverage" measure?
- What did he do between Dec 2014 and Apr 2016, and between the Hengshunyuan and VV overlap dates?
- Does "MX-rich" mean the richer ISO 20022 message format, and what did "coexistence" involve in practice?
- Does "SSH" in the Sohu bullet mean Struts/Spring/Hibernate?
- What is the transaction volume behind "millions of accounts"?
- Is the submitted resume black text rather than the red markup shown in this draft?

---

## Resolution (2026-10-26)

**Applied**
- Suggestion 1 — ISO 20022 achievement replaced by the batch canonical sentence (old and new formats "side by side"; "Blue/Green-style", "MX-rich" and "coexistence" removed).
- Suggestion 2 — production-support bullet reworded with the subject first and SRE, SLIs/SLOs expanded (kept, not cut, because the JD asks for observability); Cloudera clause now reads "big-data processing framework".
- Suggestion 3 — Sohu line rewritten without the "SSH" parenthetical (canonical Sohu sentence).
- Suggestion 4 — Selected Achievements now lead with "Hands-on core engineering".
- Suggestion 5 (partial) — tagline "Resilience by Design" shortened to "Hands-On Java Architecture & Resilience".
- Also: RAID, RCA, SOW, DPIA expanded or replaced; MVP sentence now has subject-first form.

**Not applied, and why**
- Cut / shorten the Software Designer certificate line — the line is a verified document (02 §3) and the education lines are fixed by the Revision Brief.
- Replace "99% SonarQube coverage" with "unit-test coverage" — would add an unconfirmed fact (coverage basis is open, PA-03 §8); left as a question for Wilson.
- Cut the "Technical Leadership" competency row — it is the page-1 evidence for the JD's required mentoring, standards and code-review items.
- Shorten Summary paragraph 3 — renders at 4 lines (within limit) and carries the only page-1 evidence of the e-commerce payment background and senior-stakeholder communication.
- Numbers (TPS, latency, transaction volume), card switching/POS/QR, PCI-DSS, tokenisation, Solace, gap-period explanations — would add facts not on record (several are on the batch "never write" list).
- Red text — draft markup only; the final is rendered black with `--final`.
