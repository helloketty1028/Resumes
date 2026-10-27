# Resume Change Log — NCS · Associate Director – Solution Architect (Technical)

- **Output:** `wilson-2026_ATL_Internet_NCS_V1_0_0_draft.docx`（+ .pdf / .txt / report）
- **Base:** `base_Talentvis_SM_Internet.json`（主要句子来源）+ `base_TEKsystems_TPM_Internet.json`（VV / GBD / Hengshunyuan 句子）；card 09 指定的 `LIB_..._Archi_Internet` 未读 —— approved JSON + 03 已覆盖所需内容。
- **Positioning:** ATL × INT —— 可复用平台 + 集成架构的 Solution Architect，以 Tier-1 bank 的 "designed and delivered" 作为可信度锚点；与同集团 Singtel Delivery Manager 申请保持事实一致（标题、日期、人数、数字未做任何变体）。

## Material content decisions

| Area | Decision | Source ID |
|---|---|---|
| Headline | 用 card headline 的缩短版："Solution Architect — Reusable Platforms & Integration Architecture \| Designed and Delivered in a Tier-1 Bank"。去掉 "Cloud-Native Delivery"，否则超过一行 | card 09, 02 §7.2 |
| Summary P1 | 首句对准 JD 核心（scalable, reusable platforms + accountable through delivery and production） | 02 §4, 02 §6 |
| Summary P2 | UOB：25 engineers、hub 集成架构（含 core banking，按 S2）、daily review、安全/韧性控制、"contributes to" 架构评审治理 | X-02, PA-01.2, S2, S5, X-01, PA-03.3 |
| Summary P3 | 可复用平台（GBD / VV）、AI Park 投标、对业务方解释技术取舍、mentoring | PA-10.1, PA-13, PA-16.2, C-RPT, X-02 |
| Competencies | 7 行，按 JD Required 顺序：Solution Architecture → Integration & APIs → Cloud-Native Architecture → Governance & Standards → Risk & Resilience → Stakeholders & Bids → Applied AI。Spring Cloud / Kubernetes / AWS 放在 "Architecture" 行（skills inv. A 或 A/P ❓），不放 hands-on 行；hands-on 行只放 P 级（Java、Spring Boot、Apache Camel）。MAS TRM 首次出现在此行并解释 | skills inv. §2/§5, S9 |
| Achievement 1 | PA-01.2 approved 句 + S2 "handing payments to core banking for settlement"；去掉 pain.002 | PA-01.2, S2 |
| Achievement 2 | PA-10.1；加 "customisable"（02 §6.3 原词），去掉 analytics 以控制两行 | PA-10.1 |
| Achievement 3 | PA-13，"middle-platform" → "shared back-end platform"（readability lesson）；不写 GMS 名称；技术栈省略 | PA-13 |
| Achievement 4 | PA-03.3（contributed）+ S5 的 daily review / co-design 部分；去掉 "beyond my own squads"（第一人称） | PA-03.3, S5 |
| Achievement 5 | PA-16.2 原句 + "At AI Park" | PA-16.2, S7 |
| Achievement 6 | "Enterprise-grade trust" approved 句的缩短版（去掉 secure SDLC / DPIA，Governance 行已有） | X-01, PA-02.1 |
| Achievement 7 | PA-07.1 + PA-07.2 + S9（May 2026, formal approval, never approves or merges）；未写 ~80%（行数） | PA-07.1/07.2, S9 |
| UOB scope | 两条平台线 + millions of accounts，"operating under MAS TRM" | 02 §6.1 |
| UOB Architecture & Design | S6 原句（含 concurrency control）· PA-01.4 原句 · customer-360：10-engineer、daily account summaries from core banking for portfolio analysis（S2）、Cloudera 评估、亲自写 Spring Batch jobs | S6, PA-01.4, PA-05.1–05.3, S2 |
| UOB Delivery Oversight | ISO 20022 条用 "ran old and new message formats side by side" 替代 "MX-rich / coexistence"；PA-01.5 拆出 scope/roadmap/RAID 条（"risks and dependencies"，RAID 缩写只在 competencies 解释一次）；PA-03.1/03.2 合并 approved 句 | PA-01.1, PA-01.5, PA-03.1/03.2 |
| UOB Stakeholders & Production | C-RPT 原句 · MVP sequencing 原句（对应 JD "delivery pragmatism"）· X-06 approved 句 · X-02 + X-05 合并（mentoring、vendor selection 决策权、四家 IT service vendors） | X-02, X-05, X-06, PA-02.3 |
| Golden Bridge | 3 条：PA-10.2 rule models · AWS deployment（技术压到 4 个）+ DPIA 展开 + X-01 · 40-person (total headcount) + hybrid delivery | PA-10.2, PA-10.3, X-01, S4 |
| VV | 4 条：S3 140-person（"built" 不与 headcount 同句，改为 "designed its microservices platform"）· PA-11.4 · PA-11.2 + S1（UnionPay、Visa/Mastercard、Google Pay、GrabPay + settlement reconciliation）· PA-11.3 + PA-11.5 | S3, PA-11.1–11.5, S1 |
| AI Park | 2 条：PA-16.1 + SaaS model（去掉 "online payment and recommendations" 以免 3 行）· PA-16.4 原句 | PA-16.1, PA-16.4, S8 |
| Earlier | Hengshunyuan 一行（TEK approved 句缩短）· Baidu：PA-17.1 + S1 支付网关（Alipay、WeChat Pay、UnionPay）· Sohu：去掉括号迁移细节，改为 "onto Spring MVC and a Redis cluster" · Renren：PA-19 + S1（Alipay、UnionPay，无 WeChat Pay） | PA-15, PA-17.1, PA-18.1, PA-19, S1 |
| Education | 4 行 exact（brief §3） | 02 §3 |

## Exclusions and reasons

| Excluded | Reason |
|---|---|
| ~50 / ~20 core modules | Brief S5：本 batch 不用 |
| AI review ~80%、ramp-up、defect | ~80% 为行数取舍（可用）；ramp-up / defect 为 C1/C3 held |
| eMemo AI agent（PA-08） | 只在 Applied AI 行提及，未单列 —— 与 NCS 架构岗相关度低于前 7 条 |
| RAG contribution（S9） | 篇幅；JD 的 AI consulting 只是 listing 附加信息 |
| PA-04.1 lending & collections | 只在 scope 提及平台线；对 SA 岗相关度低 |
| PA-01.7 hub context line / MEPS+ | MEPS+ 禁写；hub 描述已在 Achievement 1 |
| VV big-data team（PA-12）、AI Park recognition step（PA-16.3） | 相关度低（●），压缩阶梯第 1 步 |
| "blueprints"、"API-first"、"documentation practices"、"establish standards" | JD 词无原词证据（05 §5）；standards 锁定为 "contributed to" |
| Systems-integrator / client-facing claim、Associate Director 对等、TOGAF、IM8 | Gap，不伪装（card 09 Gaps） |
| Pureland、10M DAU、1,000+ car parks、Flink、GenAI chatbot、CTO | Brief §3 Never write |

## Rendered result

- Layout OK: **True** · pages **3** · page 1 = header + summary + competencies + all 7 achievements · page 2 starts with PROFESSIONAL EXPERIENCE · page numbers in footer · orphan headings none
- Items: 30（7 achievements + 19 experience bullets + 4 earlier）· **5 at 3 lines**（Achievement 1 Integration architecture、Achievement 7 Production AI service、UOB ISO 20022 delivery bullet、Hengshunyuan、Baidu）— 均因保留 S2 / S9 / PA-01.1 的锁定限定语或 S1 新事实
- Headline 1 line · Summary 4 / 4 / 3 lines（171 words）· total 1,224 words
- Runs: 92 total, 52 red（新组合或改写的句子；approved 原句保持黑色）
- Lint: **0 hits**

## Post-audit and cold-read revisions (2026-10-26)

依据：`audit/09_Resume_Fact_Audit.md`（1 FAIL、6 REVIEW）、`coldread/09_Readability_ColdRead.md`、`brief/Revision_Brief.md` §2 canonical sentences，以及 coordinator 的一致性规则：permission matrix 和 99.9%+ 只属于 payment-initiation hub / payment middleware；清除 "(total headcount)"、"Blue/Green" 等遗留词。修改前的 JSON 已备份到 `drafts/09/tmp/resume_before_rev.json`。

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| 1. SA6 Secure by design | "…credential management and role-based permissions for payment, lending and customer-data platforms…" | "…encryption and credential management for payment, lending and customer-data platforms under MAS TRM…" | Audit F1：采用审计员的第一个替换句。带 permission matrix 的版本没有用，因为会重复 UOB bullet 1 已写的 permission matrix，也会多出一条 3 行 bullet |
| 2. SA6 availability | "…DR and failover drills, sustaining 99.9%+ availability" | "…DR and failover drills keeping the payment hub and middleware at 99.9%+ availability" | 一致性修改（coordinator 规则）：99.9%+ 只挂在 hub 和 middleware 上 |
| 3. Summary P1 | "spent 2016–2022 in head-of-technology and architect roles at start-ups and scale-ups, building platforms from 0 to 1" | "held head-of-technology roles (2016–2020) and a project-manager-and-architect role (2020–2022) at start-ups, building 0-to-1 platforms" | Audit R-Q1 safe default，并修掉孤立的 "1." |
| 4. Summary P2 | "…reviews designs and code daily, designs the security and resilience controls, and contributes to the bank's architecture-review governance" | "…and core banking, and designs the security and resilience controls" | Audit R-Q2（没有 daily design review 的记录）+ R-Q5（不重复写：daily review 和 governance 都已在 SA4） |
| 5. Summary P3 | "Earlier platforms were built for reuse: … SaaS … shared back-end platform … Explains technical choices in business terms…" | "Designs for reuse, from a customisable multi-tenant SaaS platform to a payment hub that serves several channels. At AI Park, led technical bids… Reports status, risks and decisions to senior management and steering committees, and mentors engineers." | Audit R-Q3（"reuse" 只用于 SaaS 和 hub）、R-Q4、R-Q5（不和 SA2/SA3 重复） |
| 6. Headline | "Solution Architect — Reusable Platforms & Integration Architecture \| Designed and Delivered in a Tier-1 Bank" | "Solution Architect & Technology Leader — Reusable Platforms and Integration Architecture in a Tier-1 Bank" | Cold-read S7：拉近 headline 和实际职位 TDM 的距离 |
| 7. CC Solution Architecture | "technical sign-off through SIT/UAT and release" | "…through acceptance testing (SIT/UAT) and release" | Cold-read 缩写规则：首次出现时展开（完整写 "system and user acceptance testing" 会变成 3 行） |
| 8. CC Integration & APIs | "…channel, vendor, third-party and core-banking integration" | "…channel, vendor and third-party integration, hand-off to core banking for settlement" | Brief §2 core-banking 能力短语（S2） |
| 9. CC Governance & Standards | "daily design and code reviews" | "daily code review and solution co-design" | Audit R-Q2 safe default |
| 10. CC Risk & Resilience | "DR and failover drills" | "disaster recovery (DR) and failover drills" | Cold-read 缩写规则（DR 首次出现） |
| 11. CC Stakeholders & Bids | "explaining technical choices to business and senior stakeholders, steering-committee reporting" | "reporting to senior management and steering committees" | Audit R-Q4 safe default |
| 12. SA1 Integration architecture | "…and handing payments to core banking for settlement" | "…; it hands validated payments to core banking, which executes settlement, and processes the results returned" | Brief §2 canonical（S2, CF-N4） |
| 13. SA3 Shared platform | "Designed the shared back-end platform architecture for VV's B2B … and governed its…" | Canonical VV B2B 句（加了 Spring Boot、MySQL cluster、Redis、RocketMQ；"governing solution design…"），保留 "VV's" 以标明雇主 | Brief §2 canonical；"shared back-end platform" 是 canonical 用词（R-Q3 留给 Wilson 决定） |
| 14. SA4 Architecture governance | "Contributed … ; review core pull requests daily…" | "Contributes … ; reviews core pull requests daily and co-designs solutions…" | Audit polish：统一时态（UOB 现职用现在时） |
| 15. SA7 Production AI service | "in a MAS-regulated bank" | "in a regulated bank" | 行数预算：从 3 行减到 2 行（MAS TRM 在其他地方出现） |
| 16. UOB bullet 1 | "Personally built the hub's core modules" | "Personally built the payment-initiation hub's core modules" | Brief §1.3："the hub" 在 Experience 部分没有前文所指 |
| 17. UOB latency | "through thread-pool and JVM tuning and removal of synchronous blocking" | "by tuning thread pools and the Java runtime (JVM) and removing blocking synchronous calls" | Cold-read S1（白话化；没有采用 "waited idle for another system"，那是对原事实的重新解释） |
| 18. UOB ISO 20022 | "Owned delivery … architected a phased, Blue/Green-style rollout … went live in May 2025 and ended the parallel running in August 2026…" | Brief §2 canonical ISO 20022 句（May and August 2025 上线，2026 年 8 月停用旧路径） | Brief §2 + cold-read S2 + coordinator 规则（去掉 "Blue/Green"） |
| 19. UOB KPIs | "— deployment frequency, MTTR, … — with CI/CD quality gates (99% SonarQube coverage gate, automated regression and penetration testing) and SIT/UAT sign-off for every release" | "(deployment frequency, mean time to recovery, …) and automated quality gates — a 99% SonarQube coverage gate, regression and penetration testing — with SIT/UAT sign-off on every release" | Cold-read S6 + 缩写规则（MTTR）；保留 99% 这个门槛指标 |
| 20. UOB MVP | "When the two platform lines' schedules conflict, agree MVP scope…" | Brief §2 canonical MVP 句 | Brief §2 |
| 21. UOB incidents | "escalation, stakeholder communication, RCA … SLIs/SLOs and Splunk-based monitoring" | "escalation, communication, root-cause analysis … service-level objectives and Splunk monitoring" | 缩写规则（RCA、SLIs/SLOs，后者改成白话）；删掉 "stakeholder" 以避免孤立词，控制在 2 行 |
| 22. GBD KYC | "Designed hierarchical KYC identity verification and rule models for authentication levels and for bonus eligibility, triggers and distribution" | "Designed tiered know-your-customer (KYC) identity verification and rule models for authentication levels and bonus eligibility, triggers and distribution" | Cold-read S3（白话化 + 展开 KYC；没有采用 "payout"，保留原事实用词 "distribution"） |
| 23. GBD team | "Led a 40-person project team (total headcount) with hybrid delivery — Waterfall…, Agile sprints… — and introduced Agile/Scrum and CI…" | Brief §2 canonical GBD 句（"including outsourced staff … owned delivery budget, capacity and launch readiness"） | Brief §2 + cold-read S5 + coordinator 规则（去掉 "(total headcount)"）。hybrid-delivery 细节随之删除 |
| 24. VV scope | "…connecting offline merchants — food, … everyday services — through data." | "VV-Life: a data-driven local-life services platform connecting offline merchants in food, fresh produce, travel and everyday services." | 修掉孤立的 "data."（现在一行），没有新增事实 |
| 25. VV 140 | "Led VV's 140-person technology organisation (total headcount), running technology selection…, and designed its microservices platform from scratch" | Brief §2 canonical VV 句（"through its managers and built its microservices platform from scratch, owning technology selection and the technology budget"） | Brief §2 + coordinator 规则；"built" 是 Wilson 已批准的用词（问题留给 Wilson） |
| 26. AI Park SaaS | "introduced a SaaS model for business and government customers" | "…a SaaS model aimed at business and government customers" | Audit R-Q6 safe default |
| 27. Hengshunyuan | "bringing ~1,500 licensed audio titles onto it at launch and reaching…" | "launching with ~1,500 licensed audio titles and reaching…" | 行数预算（3 行 → 2 行），保留 "~" 限定语 |
| 28. Sohu | "Led the re-architecture of the fifth-generation CMS…" | "…of Sohu's fifth-generation CMS…" | Brief §2 canonical Sohu 句 |

**没有改的：** education 和 "Software Designer (Intermediate)" 证书保持原样（这是已核实的文件）· Cold-read S4 只部分采用：customer-360 bullet 不变，因为 "led the vendor evaluation" 会抬高 ownership，"batch jobs that load account summaries" 也没有记录支持 · S8（把 bids 移到 AI Park 条目）没有采用：会和 SA5 重复，而 page 1 需要保留 pre-sales 证据 · S9（"contributed" 是锁定动词）· S10 / audit polish（Hengshunyuan 的位置）：沿用 Drafting Brief 的顺序和 D-10 的决定 · Header 里重复的 "Singapore" 是 renderer 固定的。

**渲染结果（2026-10-26）：** Layout OK **True** · 3 页 · page 1 = summary + competencies + 全部 7 条 achievements · 30 条 bullet，renderer 估算 3 行的 **4** 条（PDF 实际 3 条：SA1、ISO 20022、Baidu；Sohu 在 PDF 中是 2 行）· Lint **0** · 1,231 词（Summary 143）· red runs 57/92 · 请求修的两处孤立词 "1." 和 "data." 都已修掉。


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K1 scale-ups | a project-manager-and-architect role (2020–2022) at start-ups, building | a project-manager-and-architect role (2020–2022) at start-ups and scale-ups, building | C3 answer K1 (2026-10-26) |
| K2 steering committee (singular) | senior management and steering committees | senior management and the steering committee | C3 answer K2 (2026-10-26) |
| K5 SonarQube scope | 99% SonarQube coverage gate | 99% SonarQube coverage gate on all code | C3 answer K5 (2026-10-26) |
| PA-03.5 CRQ/CAB | — | Personally prepare the change request for every production release on both platform lines and present the go-l | C3: add PA-03.5 (03 v4.2, CONF 2026-10-26) — approved by Wilson |

**Independent C3 edit review (2026-10-26) — fixes applied:**

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| C3 review fix #20 | Report status, risks and decisions to senior management and the steering committee, and wo | Work closely with teams in India, Thailand and Indonesia across time zones. | Independent C3 review: duplicate of Summary ¶3 (no stacking) |
