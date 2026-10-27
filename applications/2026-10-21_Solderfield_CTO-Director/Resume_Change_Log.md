# Resume Change Log — 05 Solderfield · CTO/Director (Business Partner)

- **File:** `drafts/05/resume.json` → `out/wilson-2026_SM_Bank_Solderfield_V1_0_0_draft.docx/.pdf`
- **Base:** `base_Talentvis_SM_Internet.json`（主框架与多数已批准句）+ `base_TEKsystems_TPM_Internet.json`（UOB-10/11、VV-1 原句、AI Park 首句）+ `LIB_Senior_Tech_Bank` / `LIB_Archi_Bank`（供应商技术评估、reusable backend services 的 📄 依据）。
- **Positioning:** SM × BNK（按 card）。银行技术负责人 + 支付中间件 + 产品化 SaaS + 设计到交付；商务经验明确标为甲方侧，乙方仅 AI Park 技术标（S7）。

## 1. 与 card 的偏差（均有理由）

| 位置 | Card | 实际 | 理由 |
|---|---|---|---|
| Headline | "… Payment Middleware, Message Transformation & Productised SaaS \| Solution Design to Delivery"（119 字符） | "Banking Technology Leader — Payment Middleware & Productised SaaS \| Solution Design to Delivery"（97 字符） | 原句实测占行宽 98.8%，超过 ≈105 字符指引、有折行风险；"message transformation" 是 🔶 词，放在 C1 一处即可 |
| S-P1 首句 | "… ISO 20022 message transformation … turned platforms into configurable products" | "… payment middleware between a Tier-1 bank's channels and its core banking — validation, enrichment and ISO 20022 (SWIFT MT-to-MX) messaging — and has taken a configurable SaaS product from 0 to 1" | 首次出现展开 ISO 20022；避免与 C1 重复；"turned platforms into products" 改为记录支持的说法（GBD 是 0-to-1 建产品，非项目转产品）；18+ 年放在句尾、UOB 写 "since 2022"，不暗示 18 年银行经验 |
| 能力表标签 | "Commercial"、"Banking Governance"、"Delivery" | "Bids & Commercial"、"Governance & Quality"（JD 原标题）、"End-to-End Delivery"（JD 原标题） | 标签对应 JD 条目，HR 一眼可对 |
| C3 Productisation | "version and release management" | "release planning and governance" | 产品版本管理无记录 |
| C5 | 含 "encryption"、"DR" | 去掉 encryption（已在 A6、UOB-6），展开 "disaster recovery (DR)" | 两行限制 + 首次出现展开缩写 |
| C7 Technical | Java…SQL | 另加 Apache Camel、Kafka、Docker、Jenkins、SonarQube、Splunk | 均有技能清单锚点 |
| A3 标签/文本 | "Configurable product from 0 to 1" | 标签 "Configurable SaaS product"；文本加 "reusable services for …" | 为 C3 "reusable backend services" 提供可见证据（[TPL] 已批准说法） |
| A5 | "Commercial authority" | "Buyer-side commercial authority" | card 缺口规则：甲方经验须如实标注 |
| A6 | PA-03.1 + X-01 | 另加 PA-02.1（DR 演练、99.9%+） | JD Q8 "operational resilience"；省略 "under peak load"（篇幅；Metrics Bank 行无此条件） |
| UOB | 9–10 条；PA-04.1 作为 bullet | 11 条；PA-04.1 并入 UOB scope 行；新增 AI workflow automation（PA-07/PA-08/S9）与供应商技术评估（02 §5 / [LIB]） | JD Q3 明列 "workflow automation"；"Commercial & Stakeholders" 组需真实内容（可行性评估）；PA-04.1 作背景放 scope 行不占 bullet |
| "C-RPT" | — | 解读为 TEK 已批准的 stakeholder-interface/steering 汇报句（UOB-11） | card 未定义该代号 |
| Hengshunyuan | 1–2 条 | 1 条（PA-15.2 + BD） | 第 2 条（技术栈）会使该段跨页；平台所有权已在 A7 |
| AI Park | 2 条 | 3 条：PA-16.1（TEK 原句）+ "Introduced a SaaS model for future business and government customers."（保留 02 §6.6 的 "future"）+ PA-16.4 | 拆句后少一条 3 行 bullet，且 SaaS 模式更醒目 |
| Earlier | S1 "only if space" | Baidu、Renren 均加 S1 支付集成；Sohu 缩短 | 支付集成对银行方案岗位相关；有空间 |

## 2. 主要内容决定（来源 ID）

- S-P2 "leading VV Technology's 140-person technology organisation (total headcount)" — S3；VV-1 用 PA-11.1 不带人数，人数只出现一次。
- UOB-1 S6 合并句原样（含 concurrency control）。UOB-3 PA-05.2/05.3 + S2（core banking 日账户汇总）。UOB-5 PA-01.5 + TEK 依赖措辞。UOB-6 X-01 数据迁移（对应公司数据迁移业务）。UOB-7 PA-03.2/03.4。UOB-8 X-06/PA-02.3（Talentvis 原句）。UOB-10 X-02 MVP（原句）。
- A1 PA-01.2 + S2/CF-N4（"core banking, which executes settlement"，hub 不结算）。A2 PA-01.1。A4 PA-16.2 + S7。A7 PA-15.1。
- GBD-1 PA-10.3/S4（原句）；GBD-2 PA-10 §4；GBD-3 PA-10.2 +"configurable"（🔶，card 指定）。
- VV-2 PA-11.2 + S1（"integrating … payments with settlement reconciliation"，O2 → "architected"）；VV-3/VV-4 原句。
- 为避免跨段重复，S-P3 改为 "helps select vendors and negotiate SOWs and licences"，S-P2 改为 "heading technology at a smart-parking IoT company"，C3 改为 "business and public-sector customers"。

## 3. 排除项及理由

PA-02.2（MTTR 空槽）· PA-03.3 银行级标准（篇幅）· PA-05.1 Cloudera 评估（篇幅）· PA-06 VN eTax（证据薄）· PA-07.3 ~80% 估算（篇幅；保留人在环）· PA-07.4–07.6（held / 篇幅）· PA-09、PA-14、PA-20 ⛔ · PA-11.4（与 PA-16.4 重复）· PA-12 数据平台、PA-16.3 AI 识别、PA-18.2（与 JD 无关）· PA-16.5（与 VV-4 重复）· PA-21、X-03（on-request / 无关）· S5 hands-on 句（S6 已体现；篇幅）· S9 RAG 贡献（无关）· GBD X-01 安全句（超出 2–3 条预算）· 5+ 年离岸、印/泰/印尼协作（篇幅）· MEPS+、10M、200+、1,000+、CTO 等禁用项。

## 4. 渲染结果

3 页 · **Layout OK: True** · 第 1 页含全部成就 · 第 2 页以 PROFESSIONAL EXPERIENCE 开头 · 无孤立标题 · 页码正常 · 32 条 bullet 中 2 条 3 行（A2、E-Baidu）· 词数 1,241（Summary 162）· 红色 run 51/97 · Lint 0 命中。PDF 已逐页目检；未在 Microsoft Word 中实机检查。

## Post-audit and cold-read revisions (2026-10-26)

Inputs: `audit/05_Resume_Fact_Audit.md` (F1 = U10, R-1, P-1–P-4), `coldread/05_Readability_ColdRead.md`, `brief/Revision_Brief.md` §2. Helper scripts and the pre-revision JSON: `drafts/05/tmp/`.

| Item | Before (short) | After (short) | Reason (audit F#/R# or cold-read) |
|---|---|---|---|
| Summary P1 | "ISO 20022 (SWIFT MT-to-MX) messaging" | "ISO 20022 messaging (SWIFT's MT-to-MX migration)" | Audit P-4 (explain MT/MX; canonical phrasing) |
| Summary P2 | "140-person technology organisation (total headcount)" | "140-person technology organisation through its managers" | Cold-read 4.5 / suggestion 2; canonical VV summary form |
| Summary P3 | "at UOB, helps select vendors and negotiate SOWs and licences as the buyer" | "at UOB, holds decision or joint-decision authority on vendor selection as the buyer" | Cold-read suggestion 3 / (b)2 (one strength for vendor authority); Revision Brief §1.3 |
| Comp · Banking Solutions | "ISO 20022 (MT-to-MX) message transformation" | "ISO 20022 (MT-to-MX) messaging migration" | R-1 safe default |
| Comp · End-to-End Delivery | "RAID, dependencies and scope trade-offs" | "risks, dependencies and scope trade-offs" | Jargon (RAID) |
| Comp · Technical | "…, Linux (RHEL), SQL, Jenkins, SonarQube, Splunk" | "…, Linux (RHEL), SQL" | Cold-read "smaller" (tools already named in the bullets) |
| Ach · Payment middleware | "… integrating channels, vendor systems and core banking, which executes settlement." | "… that connects channels and vendor systems and hands payments to core banking for settlement." | Ambiguous "which" (same issue as cold-read 02); canonical S2 hand-off |
| Ach · Modernisation without disruption | "phased, Blue/Green-style coexistence … live from May 2025 … coexistence retired in August 2026" | Canonical ISO 20022 sentence (now also names the August 2025 phase, as the canonical does) | Revision Brief §2; cold-read near-miss |
| Achievements order | SaaS 3rd, Bids 4th, Buyer-side 5th | Bids 3rd, Buyer-side 4th, SaaS 5th | Cold-read suggestion 3 (commercial evidence higher) |
| Ach · Banking-grade governance | "… personally led DR and failover drills, sustaining 99.9%+ availability." | "… DR and failover drills for the real-time payment middleware, sustaining 99.9%+ availability." | PA-02.1 scope (cf. audit 01 F1); cold-read question "which platform" |
| Ach · Entrepreneurial ownership | "Co-founded an audio-learning platform and owned product, architecture …, ~100k daily active users." | Cut (merged into the Hengshunyuan entry) | Cold-read suggestion 1 |
| UOB · core modules | "Personally built the hub's core modules" | "Personally built the payment-initiation hub's core modules" | Audit P-1; cold-read suggestion 2 |
| UOB · latency | "through thread-pool and JVM tuning and removal of synchronous blocking" | "by tuning thread pools and the Java virtual machine (JVM) and removing synchronous blocking calls" | Cold-read 4.1 / suggestion 2 (no figure added) |
| UOB · customer-360 | "Led the 10-engineer backend team …" | "Lead the 10-engineer backend team …" | Audit P-2 (current team, present tense) |
| UOB · ISO 20022 delivery | "scope, roadmap, RAID, dependencies …" | "scope, roadmap, risks, dependencies …" | Jargon (RAID) |
| UOB · quality gates | "secure SDLC, DPIA and data governance" | "secure SDLC, data protection impact assessments (DPIA) and data governance" | Cold-read 4.2 (DPIA never expanded) |
| UOB · P1–P3 incidents | "Coordinate P1–P3 production incidents … RCA … SLIs/SLOs and Splunk-based monitoring" | "Coordinate P1–P3 incidents … root-cause analysis (RCA) … service-level indicators/objectives and Splunk monitoring" | Cold-read 4.3; Revision Brief §1.3 acronyms |
| UOB · vendor evaluation | "Lead technical evaluation of vendors and start-ups — architectural design, technical credentials and fit with existing systems — as input to …" | "Lead technical evaluation of vendors as input to vendor-selection and SOW/licence decisions." | **F1** (U10) — auditor's replacement verbatim |
| UOB · MVP sequencing | "When the two platform lines' schedules conflict, agree MVP scope …" | Canonical MVP sentence | Revision Brief §2 |
| GBD · team | "Led a 40-person project team (total headcount), …" | "Led a 40-person project team, including outsourced staff, …" | Canonical GBD sentence; cold-read 4.5 |
| VV · scope line | "… everyday services — through data." | "… everyday services." | Cut; removed a one-word second line |
| VV · organisation | "Built VV's technology organisation and its microservices platform (Spring Cloud, Kubernetes, Redis cluster, Elasticsearch, AWS) from scratch, …" | Canonical VV sentence ("Led VV's 140-person technology organisation through its managers and built its microservices platform from scratch, …") | Audit P-3 (five technologies); "built" no longer applied to an organisation (HR-9); Revision Brief §2 |
| VV · B2B product | "middle-platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ, AWS)" | "shared back-end platform architecture (Spring Boot, MySQL cluster, Redis, RocketMQ)" | Cold-read 4.4; audit P-3; canonical VV B2B sentence |
| Hengshunyuan | "Ran business development for content licensing with rights holders, bringing ~1,500 licensed audio titles …" | "Owned product, architecture and technical delivery of an audio-learning platform, reaching a peak of ~100k daily active users; ran content licensing with rights holders, bringing ~1,500 licensed titles and albums onto the platform at launch." | Cold-read (b)2 / suggestion 1 (the two descriptions now match; PA-15.1 + PA-15.2) |
| Earlier · Baidu | "re-architected the merchant-side order system on Dubbo microservices and delivered …" | "re-architected the merchant-side order system and delivered …" | Cold-read suggestion 3 (cut) |
| Earlier · Sohu | "Re-architected the fifth-generation CMS (SSH to Spring MVC, memcached to Redis) and delivered …" | "Led the re-architecture of the fifth-generation CMS onto Spring MVC and a Redis cluster, and delivered its OpenAPI messaging platform." | Canonical Sohu sentence ("Sohu's" dropped; the lead names Sohu); cold-read suggestion 3 |

**Not changed:** Education certificate line; Summary P2 length (kept at 4 lines as the only page-1 trail of the start-up roles); "estimated ~80%".

**Rendered result (after revision):** 3 pages · Layout OK **True** · bullets 31, at 3 lines **5** (Ach Payment middleware, Ach Modernisation, Ach Banking-grade governance, UOB P1–P3 incidents, Earlier Baidu) · words 1,250 (summary 164) · line flags none · lint hits 0 · pages rasterised and viewed (`drafts/05/tmp/pg-*.png`).

**For Wilson:** (1) Did you or the hub team build MT-to-MX message transformation or mapping, or is the migration a change of message standard (R-1)? The JD asks for message transformation. (2) Do you evaluate start-ups, and are "architecture, technical credentials and fit with existing systems" your criteria (F1)? If yes, confirm with a [CONF] date and the detail can return. (3) Is the 99% SonarQube gate on new code or all code?


## C3 decisions applied (2026-10-26)

Wilson's C3 answers: K1 VV/GBD may be called scale-ups · K2 one steering committee · K3 report status, risks and decisions to the business team (no "business terms") · K4 he wrote the VV microservices framework code ("built" stays) · K5 99% SonarQube gate covers all code · PA-03.5 (03 v4.2) approved for 08, 01, 04, 09.

| Item | Before (short) | After (short) | Reason |
|---|---|---|---|
| K2 steering committee (singular) | senior management and steering committees | senior management and the steering committee | C3 answer K2 (2026-10-26) |
| K5 SonarQube scope | 99% SonarQube coverage gate | 99% SonarQube coverage gate on all code | C3 answer K5 (2026-10-26) |
