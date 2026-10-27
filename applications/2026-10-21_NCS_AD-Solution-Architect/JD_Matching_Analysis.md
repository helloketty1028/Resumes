# JD Matching Analysis — NCS · #EG Associate Director – Solution Architect (Technical)

- **JD:** JobStreet 94992125 · https://sg.jobstreet.com/job/94992125 · 全文见 `JD.md`
- **Resume:** `wilson-2026_ATL_Internet_NCS_V1_0_0`（draft，红字 = 非 approved 原句）
- **Sources read:** Drafting_Brief · card 09 · 01 v1.1 · 02 v3.1 · 03 v4.1 · 05 v1.0 · technical-skills-inventory v2.3 · fact-check v2.4 · base_Talentvis / base_TEKsystems JSON（未读 LIB_*.txt，不需要）

## (a) Classification

**ATL × INT.** JD 的核心是 "design, implementation, and governance of reusable solution assets"、solution sign-off、asset architecture ownership —— 全部是 architecture / tech-leader 信号（05 §2）。NCS 是 systems integrator / AI tech services 公司，服务 enterprise 与 public-sector 客户，不是银行或 fintech，所以用 INT lens：前置 0-to-1 可复用平台（GBD multi-tenant SaaS、VV shared back-end platform），银行术语（ISO 20022、MAS TRM）首次出现时解释。UOB 仍作为 "enterprise technology environment" 的主证据。

## (b) Fast-reject / eligibility

- **Fast-reject（05 §4）：** 无命中 —— 没有 C#/.NET、kdb+、Murex、manufacturing、Azure/Databricks、GPU inference 等要求。"specific stack to be defined by CTO" 不构成 stack 限制。
- **Eligibility：** 无 work-pass 问题（Singapore PR）；JD 未要求证书（TOGAF 未列，未写）。
- **Seniority:** "Associate Director level or equivalent is preferred" —— Wilson 现为 VP2；Associate Director 与 VP 在新加坡大致可比，但这是**推断**，简历里不写任何对等说法。
- **Batch match score（card 复制，coverage formula）：75** · tier B。

## (c) Evidence matrix

| # | JD requirement (shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| 1 | Solution architecture within a systems integrator **or enterprise technology environment** | Req | PA-01.2, S2, PA-05.1, 02 §6.1 | Direct（enterprise 侧）/ Gap（SI 侧） | Headline; Summary P1–P2; Achievement "Integration architecture"; UOB Architecture & Design | solution architect, integration architecture |
| 2 | Scalable platform design and reusable asset development | Req | PA-10.1, PA-13, PA-16.1 (SaaS model) | Direct — 可复用平台（multi-tenant、shared back-end）；"reusable solution assets" 的 SI 资产库意义上为 Transferable（bridge：自建可配置多租户平台 = 复用资产） | Summary P1/P3; Achievements "Multi-tenant platform", "Shared platform"; Competencies row 1 | scalable, reusable platform design, multi-tenant SaaS |
| 3 | Microservices, cloud-native, API-first | Req | PA-10.1, PA-11.4, PA-16.4, PA-01.2; skills inv. §2/§5/§7 | Direct（microservices、API contracts、AWS/K8s 为 A 级）；"API-first" 作为术语未使用 —— 证据是 API contracts / API gateway | Competencies rows 2–3; GBD, VV, AI Park bullets | microservices, cloud-native, API contracts, API gateway |
| 4 | Communication & stakeholder management, client-facing and internal leadership | Req | C-RPT (X-02), PA-16.2, X-05, X-02 | Direct（internal leadership、steering、vendor）；client-facing 为 Transferable（bridge：AI Park 政府投标 + vendor/third-party 对接），非 SI 客户交付 | Summary P3; Competencies "Stakeholders & Bids"; UOB Stakeholders & Production | stakeholder, steering committees, technical bids |
| 5 | Associate Director level or equivalent | Pref | 02 §2 (VP2), X-02 | Transferable（未声明对等） | UOB title | — |
| 6 | Technical solution sign-off; collaborate with pre-sales on technical narratives | Req (resp.) | PA-03.1 (SIT/UAT sign-off), S5, PA-16.2, S7 | Direct（release sign-off、设计评审）；pre-sales 仅 AI Park 技术标书（S7）→ Transferable | Competencies row 1; Achievement "Technical bids"; UOB Delivery Oversight | technical sign-off, technical bids |
| 7 | Delivery oversight; sign off deployed solutions vs architecture/performance/security standards | Req (resp.) | PA-01.1, PA-01.5, PA-03.1/03.2, PA-01.4 | Direct | UOB Delivery Oversight | delivery, quality gates, SIT/UAT sign-off |
| 8 | Asset architecture ownership — blueprints, integration patterns, scalability models; consistent implementation with engineering leads | Req (resp.) | PA-01.2, PA-10.1, PA-13, S5, S6 | Direct（integration patterns、架构设计 + 与工程师共同设计）；"blueprints"、"vertical expansion" 无原词证据 → 未使用 | Achievements 1–4; Competencies rows 1–2 | integration patterns, architecture |
| 9 | Cross-functional collaboration with product, engineering, client stakeholders; technical authority | Req (resp.) | X-02 (MVP sequencing), PA-01 §9 | Direct（internal）；client 侧同 #4 | UOB Stakeholders & Production | MVP scope, dependencies |
| 10 | Governance — architectural standards, documentation, review mechanisms; mentor engineers | Req (resp.) | PA-03.3 (contributed, CF-15), S5, X-02 | Direct（review mechanisms、mentoring）；"establish standards" → 只能写 **contributed to**（锁定动词）；documentation practices 无证据 → 未写 | Achievement "Architecture governance"; Competencies row 4; UOB bullet (mentoring) | architecture-review governance, standards, mentoring |
| 11 | Liaison between technical and non-technical stakeholders | Req (resp.) | C-RPT, X-02, 01 §6 voice | Direct | Summary P3; UOB Stakeholders | explains technical choices in business terms |
| 12 | Risk management — identify, assess, mitigate technical risks | Req (resp.) | PA-01.5 (RAID), PA-01.1 (phased rollout), X-01, PA-02.1, X-06 | Direct | Competencies "Risk & Resilience"; Achievement "Secure by design"; UOB Delivery | risks and dependencies (RAID), DR, encryption |
| 13 | Deep technical knowledge guiding solution development | Req (resp.) | S6, PA-01.4, PA-05.2, PA-11.4 | Direct | UOB Architecture & Design; VV | core modules, latency, JVM tuning |
| 14 | AI management consulting for enterprises and public sector (listing extra) | Inferred | PA-07.1/07.2, PA-08, S9 | Transferable（applied AI 交付 + 治理）；consulting / public-sector 为 Gap | Competencies "Applied AI"; Achievement "Production AI service" | applied AI, human-in-the-loop governance |

## (d) Three-dimension review（无总分）

**Job fit.** JD Top-5 Required（solution architecture in enterprise env · scalable/reusable platform · microservices/cloud-native/API · stakeholder communication · sign-off/delivery oversight）在 page 1 均有可见证据：Headline + Summary P1–P2（#1）、Achievements 2–3（#2）、Competencies rows 2–3（#3）、Summary P3 + Stakeholders row（#4）、Competencies row 1 + Achievement 4（#6/#7）。最大缺口是 **systems-integrator / client-facing 交付** —— 简历里没有伪装成 SI 经历，以 enterprise 架构 + vendor/third-party 集成 + AI Park 投标作为 bridge。

**Factual-reliability risks.**
- 全部数字来自 03 §0A / §4：18+ years、25 engineers、10-engineer、15-engineer、40-person (total headcount)、140-person (total headcount)、99.9%+、99% SonarQube、every 2–3 months、May 2025 / Aug 2026、~100k、~1,500、2 months ahead。无 ~80%（为保持 AI 条两行内未使用，非事实原因）。
- 动词按 ownership：S6 "Personally built"（O1）；PA-13、PA-10.1 "designed / architected"（O2）；bank-wide standards "Contributed to"（CF-15）；AI Park "Brought Spring Cloud microservices into the architecture"（O2）；140/40 headcount 旁不用 "built"。
- 标题：VV = Head of Technical Centre、AI Park = VP of Technical Department（S8）。注意 02 §2 仍把 FU-3/CF-16 标为 ⚠️，但 brief S8 已确认，按 brief 执行。
- 无 CEW / CCD / GMS / vendor 名 / MEPS+；lint 0 hits。
- 中等风险点：Competency "non-functional requirements (latency, availability, security)" 是对 PA-01.4 / PA-02.1 / X-01 的归纳（🔶），面试需能举例。

**Document quality.** Layout OK: True · 3 pages · page 1 = header + summary + competencies + 7 achievements · page 2 以 PROFESSIONAL EXPERIENCE 开头 · 无 orphan heading · 30 个 bullet/achievement/earlier 项中 5 个 3 行（≤ 1/5）· headline 1 行 · summary 4/4/3 行 · 1,224 words（低于 1,350–1,550 指南但已占满 3 页）· lint 0。未做：人工目视检查 PDF 版式（只依赖 renderer 估算）。

## (e) Honest gap handling

- **SI / client-facing architecture：** 不声称；Summary 与 Achievements 只写 enterprise（bank）架构、vendor/third-party 集成、AI Park 技术投标。
- **Pre-sales：** 只有 AI Park 技术标书（S7）；不写 vendor 侧 pricing / proposal ownership。
- **"Establish architectural standards"：** 只能写 "contributed to"（锁定）；简历未暗示他设立了 NCS 式的标准体系。
- **Associate Director：** 不写对等。
- **TOGAF / IM8 / public-sector：** 不写。
- **Documentation practices / blueprints：** 无原词证据，未写。

## (f) Open questions for Wilson（只列会改变事实或定位的）

1. **Spring Cloud / Kubernetes depth（skills inv. A/P ❓）** —— 本稿放在 "Cloud-Native Architecture" 行（架构级）。若你在 GBD/VV 亲手写过 Spring Cloud 代码，可升级为 hands-on。**Default：** 保持架构级。
2. **AI code-review ~80% 估算** —— 本稿为控制行数没用。若你希望 page 1 带一个结果数字，可替换 "it advises but never approves or merges" 半句。**Default：** 不加。
3. **GBD 业务性质（OQ-1.9）** —— NCS 服务公共部门客户，"online-game businesses" 可能引起 HR 疑问。**Default：** 按 S9 原样写，不展开。
