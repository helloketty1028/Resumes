# JD Matching Analysis — 05 Solderfield · Chief Technology Officer/Director (Business Partner)

- **JD:** JobStreet 95022480 · https://sg.jobstreet.com/job/95022480 · 全文：`JD.md`
- **Draft:** `resume source file (working copy)` → `out/wilson-2026_SM_Bank_Solderfield_V1_0_0_draft.docx/.pdf`
- **Batch match score（照抄 card，批次覆盖率公式，非本次重算）：83** · triage tier B
- 简历位置代码：HL = headline · S-P1/P2/P3 = Summary 段落 · C1–C7 = Core Competencies 行 · A1–A7 = Selected Achievements · UOB-scope / UOB-1…11 · GBD-1…3 · VV-scope / VV-1…4 · HSY-1 · AIP-1…3 · E-Baidu / E-Sohu / E-Renren · EDU

---

## (a) 分类：SM × BNK

- **Family = SM（Senior Manager）。** 岗位要求"leading the technical and commercial development of the software solutions business"：技术路线、架构现代化、团队与交付、商机、谈判、结项回款、持续支持——这是"技术负责人 + 业务负责人"的组合，多数 Required 条目（Q2 技术领导、Q4 产品化、Q5–Q6 商务、Q7 交付、Q9 创业式担当）落在 SM 一侧；ATL 证据（中间件、API、微服务、报文转换）只在 Q3 需要时借用。
- **Lens = BNK。** 雇主是银行解决方案 ISV（IBM ISV business partner，面向银行做交易处理、关键接口报文处理、Silverlake 数据迁移、DR 服务），Q1 明确 "Proven experience in banking technology and solutions is mandatory"。因此保留银行术语（ISO 20022、MAS TRM、SIT/UAT、DR），首次出现处做通俗展开。
- 与 card 一致（card：SM × BNK）。

## (b) Fast-reject 与资格

- **Fast-reject（05 §4 清单）：无命中。** 无 C#/.NET 主栈、kdb+/q、Murex/Treasury-FX、OMS、制造业、Azure/Databricks CDAO、财务 AI、跨境物流、SAS、GPU 推理等信号。
- **资格项 1 — 雇佣形式（未核实，阻断项）：** 广告写 "join us as business partners"、"partnership opportunity"，但 JobStreet 标注 Full time + 医疗/牙科/津贴。Wilson 不接受非受薪安排 → **投递前必须确认为受薪雇佣**（见 OQ-1）。简历本身不做任何回应。
- **资格项 2 — 地点/形式：** Paya Lebar，Full time；Wilson 为 Singapore PR → 无障碍。
- **平台信号（推断，非 JD 资格条款）：** 公司产品基于 IBM iSeries (AS/400) 与 IBM Linux/Unix，并做 Silverlake Axis 数据迁移。Wilson 无 iSeries/AS400、无 Silverlake 记录（card 已定：不提及）；有 Linux (RHEL) 与 SQL（✅ CF-N6）和多次数据迁移（X-01）。

## (c) Evidence matrix（每条明确要求一行）

| # | JD requirement (JD wording, shortened) | Type | Evidence ID | Status | Resume location | Keyword used |
|---|---|---|---|---|---|---|
| Q1 | Proven experience in banking technology and solutions — mandatory | Req | 02 §2 / §6.1; PA-01; PA-04.1; PA-05; S2 | Direct（UOB 自 2022-10，约 4 年；JD 未写年限要求） | HL, S-P1, A1, A2, UOB 全段 | "Banking technology leader", "Tier-1 bank" |
| Q1.1 | strong knowledge of banking operations | Req | PA-04.1; PA-01 §1/§5（cut-off 窗口）; X-06 | Direct（技术侧：负责支付发起、贷款服务与催收的技术，不是运营岗） | UOB-scope, C1 | "retail lending servicing and collections" |
| Q1.2 | transaction processing | Req | S6 / PA-01.3; PA-01.4 | Direct | UOB-1, UOB-2 | "payment-transaction initiation, concurrency control" |
| Q1.3 | integration requirements | Req | PA-01.2; S2; PA-05.3 + S2 | Direct | A1, UOB-3, C1 | "core-banking integration", "daily account summaries from core banking" |
| Q1.4 | delivery standards | Req | PA-03.1–03.4 | Direct | A6, UOB-7, C5 | "release governance", "secure SDLC", "MAS TRM" |
| Q2 | experience as a CTO, Solution Architect, Technical Director or equivalent senior technology leader | Req | 02 §2 titles; S3; S8; X-02 | Direct（以"同等职位"成立：VP of Technical Department、Head of Technical Centre、Project Manager & Architect、UOB VP2）；从未任 CTO，不写 | S-P2, 各段职衔 | "head-of-technology and architect roles" |
| Q2.1 | responsibility for architecture, engineering teams and solution delivery | Req | PA-01.2; PA-01.5; X-02; S3; S4 | Direct | S-P1, S-P2, A1, UOB-5, GBD-1, VV-1 | "leading 25 onshore and offshore engineers", "140-person technology organisation (total headcount)" |
| Q3 | designing secure, scalable and resilient solutions | Req | X-01; PA-02.1; PA-01.4 | Direct | A6, UOB-2, UOB-6 | "encryption", "DR and failover drills", "99.9%+ availability" |
| Q3.1 | middleware | Req | PA-01.2; PA-02（real-time payment middleware） | Direct | HL, S-P1, A1, C2 | "payment middleware" |
| Q3.2 | APIs | Req | PA-01.2（API contracts） | Direct | A1, C2 | "API contracts", "API design" |
| Q3.3 | microservices | Req | PA-10.1; PA-11.1; PA-16.4; PA-17.1 | Direct | A3, VV-1, AIP-3, E-Baidu, C2 | "microservices" |
| Q3.4 | message transformation | Req | PA-01 §1（hub 报文由 SWIFT MT 迁到 ISO 20022 MX）; PA-01.2（enrichment）; Apache Camel ✅ | Transferable / 🔶 — 桥：hub 的报文从 MT 迁到 MX、在 Camel 上做 enrichment；MT/MX 映射由 hub 还是下游 SWIFT 网关完成，记录中没有（OQ-2） | 仅 C1；Summary 改用 "ISO 20022 (SWIFT MT-to-MX) messaging" | "ISO 20022 (MT-to-MX) message transformation" |
| Q3.5 | workflow automation | Req | PA-07.1/07.2; PA-08; S9 | Direct（用 AI agent 自动化人工流程）；无 BPM / workflow-engine 产品记录 | UOB-4, C2 | "AI workflow automation" |
| Q3.6 | legacy system modernisation | Req | PA-01.1; PA-18.1; PA-17.1 | Direct | A2, E-Sohu, E-Baidu, C2 | "legacy modernisation", "legacy SWIFT MT" |
| Q4 | convert project-specific implementations into reusable, configurable software products | Req | PA-10.1 + 02 §6.3（customisable multi-tenant SaaS）; [TPL]/[LIB] "reusable backend services"; PA-16 §4（SaaS model）; PA-13（通用型 B2B 产品）; PA-10.2（rule models） | Transferable — 桥：0-to-1 做出可配置多租户 SaaS 产品、为 IoT 平台引入 SaaS 模式；**没有"把银行项目成果转成商业产品"的记录** | HL, S-P1, C3, A3, AIP-2, GBD-3, VV-3 | "Productised SaaS", "configurable", "reusable services", "SaaS model" |
| Q4.1 | sound practices for intellectual property ownership | Req | — | Gap | 不写 | — |
| Q4.2 | documentation | Req | 仅 X-06（post-incident reports） | Gap（产品文档实践无记录） | 不写 | — |
| Q4.3 | version management | Req | PA-01.5（release planning、每 2–3 个月升级）; PA-03.1 | Transferable — 发布规划与治理；产品版本管理无记录 | C3, UOB-5, A6 | "release planning and governance" |
| Q4.4 | ongoing support | Req | PA-02.3; X-06; PA-11.5 | Direct | UOB-8, VV-4 | "production support", "emergency-response plans" |
| Q5 | identify opportunities, engage clients, assess requirements, develop proposals, demonstrations and proofs of concept | Req | PA-16.2 + S7; PA-15 §4/§9; X-02（MVP scope）; 02 §5 vendor technical evaluation | Transferable / 部分 — 乙方侧只有 AI Park 技术标（S7）；城市试点≈PoC；版权方 BD；无演示、无报价方案记录 | A4, C4, HSY-1, S-P3 | "technical bids and tender responses", "pilots", "business development" |
| Q6 | solution costing, pricing, contract negotiation; scope, payment milestones, acceptance criteria, support commitments; profitability | Req | X-02; X-05 / CF-N1; PA-13（cost evaluation）; 预算权（fact-check §6） | Transferable（甲方侧：选型、SOW/licence 谈判、供应商预算与绩效评审、内部成本评估）/ Gap（乙方报价、成本测算、付款里程碑、P&L） | A5, C4, S-P3, VV-3 | "buyer-side", "SOW/licence negotiation", "budgets", "cost evaluation" |
| Q7 | managing projects from requirements and design through development, testing, deployment, client acceptance, operational handover and project closure | Req | PA-01.5; PA-03.1/03.2; PA-10.3; PA-11.2; PA-13; X-06 | Direct（需求→部署→生产支持）；验收 = Transferable（SIT/UAT sign-off、GMS 验收治理）；商务结项/移交 = Gap（他的团队自己运维生产，无移交） | S-P3, C6, UOB-5, A6, GBD-1, VV-3 | "Delivers end to end", "SIT/UAT sign-off", "launch readiness", "acceptance" |
| Q8 | secure development | Req | PA-03.4; X-01 | Direct | C5, UOB-7, A6 | "secure SDLC" |
| Q8.1 | access controls | Req | PA-01.3（corporate-/user-role permission matrix） | Direct | A6, UOB-1, C5 | "role-based access control", "permission matrix" |
| Q8.2 | audit trails | Req | PA-03 §7 "audit-ready releases" 📄; pain.002 status tracking | Unverified — 无明确审计轨迹设计记录；不写（OQ-5） | 不写 | — |
| Q8.3 | change management | Req | PA-01 §6（change control） | Direct | C5, S-P3 | "change control" |
| Q8.4 | testing | Req | PA-03.1; PA-03.2 | Direct | A6, UOB-7, C5 | "SIT/UAT sign-off", "automated regression and penetration testing" |
| Q8.5 | release governance | Req | PA-03.1 | Direct | A6, C5 | "release governance" |
| Q8.6 | operational resilience within banking environments | Req | PA-02.1; X-06 | Direct | A6, UOB-8, C5 | "disaster recovery (DR) and failover", "99.9%+ availability" |
| Q9 | entrepreneurial mindset; ownership of business outcomes | Req | PA-15.1 | Direct | A7, S-P2, HSY | "Co-founded", "Entrepreneurial ownership" |
| Q9.1 | ability to build teams | Req | PA-11.1; S3; S4 | Direct | S-P2, VV-1, GBD-1 | "Built VV's technology organisation … from scratch", "Led a 40-person project team (total headcount)" |
| Q9.2 | collaborate with fellow business partners; long-term business growth | Req | PA-15 §9（co-founders）; X-02 | Transferable（联合创始人经历；跨团队协作） | S-P2, A7 | — |
| Q10 | degree in Computer Science / IT / Engineering preferred; certifications advantageous | Pref | 02 §3 | Direct（计算机科学与技术硕士；软件设计师（中级）；PMP 在读；SRE 培训） | EDU | "Computer Science and Technology" |
| R1 | define technology roadmap, solution platforms, architecture modernisation strategy; banking knowledge → reusable products with IP ownership | Req | PA-01.1; PA-01.5（roadmap）; PA-11.1（technology selection） | 路线图/现代化 = Direct；银行知识产品化与 IP = Gap | A2, UOB-5, VV-1 | "roadmap", "modernisation" |
| R2 | requirements analysis, solution architecture, feasibility assessments, PoC; proposals (scope, resources, timelines, costs, value) | Req | PA-01.2; 02 §5 / [LIB] vendor evaluation; PA-16.2 pilots; X-02 MVP | 需求/架构 = Direct；可行性 = Transferable（供应商技术评估）；PoC ≈ 城市试点；含报价的方案 = Gap | A1, UOB-9, UOB-10, A4 | "technical evaluation", "MVP scope" |
| R3 | pursue opportunities; client and partner relationships; technical presentations, demonstrations, tender responses | Req | PA-16.2; PA-15 §4/§9; PA-01 §9（steering） | Transferable — 技术标与版权方关系；汇报对象为内部（高管、steering committee） | A4, HSY-1, UOB-11 | "tender responses", "rights holders" |
| R4 | negotiations on pricing, scope, payment milestones, acceptance criteria, IP rights, support obligations | Req | X-02（SOW/licence，甲方）; X-02 MVP | Transferable（甲方侧、范围协商）/ Gap（报价、里程碑、IP 条款） | A5, UOB-10 | "SOW/licence negotiation", "MVP scope" |
| R5 | oversee implementation, resources, quality, security, testing, deployment; risks, dependencies, scope changes, client expectations; commitments and profitability | Req | PA-01.5; PA-03; X-02 MVP; PA-10.3 | Direct（盈利性 = Gap，仅预算责任） | UOB-5, UOB-7, UOB-10, GBD-1, GBD-2 | "RAID", "dependencies", "scope trade-offs", "capacity" |
| R6 | client acceptance, documentation, operational handover, final invoicing and payment follow-up, lessons learned, reusable components | Req | PA-03.1（SIT/UAT sign-off）; PA-13（acceptance）; X-06（post-incident reports, RCA） | Transferable / Gap — 无开票、催款、乙方结项记录 | A6, VV-3, UOB-8 | "acceptance", "post-incident reports" |
| R7 | maintenance and support arrangements, product improvements, renewals, enhancements, wider adoption | Req | PA-02.3; X-06; PA-11.5; PA-01.5（每 2–3 个月升级） | 支持与迭代 = Direct；乙方续约 = Gap | UOB-5, UOB-8, VV-4 | "production support", "upgrades every 2–3 months" |
| EL-1 | "join us as business partners" / "partnership opportunity"（JobStreet 标 Full time） | Elig | card ⚠ | Unverified — 只接受受薪岗位，投递前确认（OQ-1） | — | — |
| EL-2 | Paya Lebar, Singapore; full time | Elig | 02 §1 | Direct | header | "Singapore PR" |
| I-1 | IBM iSeries (AS/400) 与 IBM Linux/Unix 平台（公司简介） | Inferred | skills inventory: RHEL ✅ P | iSeries/AS400 = Gap（不提）；Linux (RHEL) 已列 | C7 | "Linux (RHEL)" |
| I-2 | 数据迁移/移植，含 Silverlake Axis（公司简介） | Inferred | X-01 | 数据迁移 = Transferable（支付、贷款、客户数据平台）；Silverlake = Gap | UOB-6, C6 | "data migration" |
| I-3 | 关键接口报文处理、24x365、交易管理、性能与 DR 服务（公司简介） | Inferred | PA-01; PA-01.4; PA-02.1; X-06 | Direct | UOB-scope, UOB-1, UOB-2, UOB-8, A6 | "mission-critical", "latency", "DR" |

**Page 1 覆盖检查（JD 前五项 Required）：** Q1 银行 → S-P1、C1、A1、A2、A6；Q2 技术领导 → S-P1、S-P2；Q3 架构/现代化 → C2、A1、A2；Q4 产品化 → HL、S-P1、C3、A3；Q5 提案/BD → C4、A4、S-P3。五项在第 1 页均有可见证据；Q4、Q5 为 Transferable，措辞未掩饰。

## (d) 三维评审（不打总分、不给百分比）

**1. Job fit**
- **强：** Q1 银行（Direct，现职 Tier-1 银行支付与贷款平台）、Q2 技术领导（以同等职位成立）、Q3 架构与现代化（中间件、API、微服务、MT→MX 无中断迁移；报文转换为 🔶）、Q7 交付（需求→部署→生产支持）、Q8 治理与质量（除 audit trails 外均 Direct）、Q9 创业与组建团队、Q10 学历。公司业务线（关键报文处理、交易管理、DR、数据迁移、改造重构、应用维护）与 UOB 及早期经历高度对口。
- **中：** Q4 产品化（做过产品和 SaaS 模式，但不是"把银行项目转成产品"；IP、文档缺）；Q5 提案/BD（只有 AI Park 技术标与版权方 BD）。
- **弱：** Q6 乙方商务（只有甲方侧经验；报价、成本测算、付款里程碑、P&L 均无）；R6 商务结项（开票、催款无）。
- **资格风险：** 雇佣形式未确认（OQ-1），是投递前的阻断项。
- **级别：** 51–100 人公司的 CTO 级岗位；Wilson 的管理规模（VV 140 人 total headcount、UOB 25 人、四家 IT 服务商）匹配；无 CTO 头衔，headline 不写 CTO。

**2. 事实可靠性风险**
- 🔶 "ISO 20022 (MT-to-MX) message transformation"（仅 C1）：迁移事实成立，映射由谁完成未记录 → OQ-2。
- 🔶 "configurable"（S-P1、C3、A3 标签、GBD-3）：来源 02 §6.3 为 "customisable"，card 指定用 JD 词 → OQ-3。
- 🔶 "reusable services"（A3）/ "reusable backend services"（C3）：[TPL] 已批准句 "built reusable backend services" + [LIB] 📄，是对多租户共享模块的描述。
- 🔶 HL "Productised SaaS"：GBD SaaS 产品 + AI Park SaaS 模式的概括。
- 📄（[LIB] 级）UOB-9 "technical evaluation of vendors and start-ups"：02 §5 有 ✅ "vendor technical evaluation"，"start-ups" 只见于 [LIB]。
- "Banking technology leader … with 18+ years"：18+ 年挂在整段职业上，UOB 明写 "since 2022"，不暗示 18 年银行经验。
- A6 "99.9%+ availability" 省略了 "under peak load"（篇幅）；与 Metrics Bank 行 "99.9%+ availability" 一致。
- 人数均带限定：S3 "140-person … (total headcount)"、S4 "40-person … (total headcount)"；动词未出现 "built + 人数"。
- 职衔按 S8：VV "Head of Technical Centre"、AI Park "VP of Technical Department"（02 仍记有 2026-10-15 的 "Development" 版本；背调须与聘书一致，FU-3/CF-16）。
- Hengshunyuan 日期 Oct 2017 – Sep 2019 与 VV 重叠（D-10：简历不注明，面试解释）。
- S6 并发控制模块：本批次已确认（C7 关闭方向），按 S6 合并句使用。
- 未使用任何 ⚠️/⛔ 项与估算类数字（~80% 未用）。

**3. 文档质量**（已实际渲染并检查 PDF）
- `tools/render.py` 渲染（LibreOffice + Carlito，与 Calibri 等宽度）：**3 页；Layout OK: True**；第 1 页 = 页眉 + Summary + 7 行能力 + 7 条成就；第 2 页以 PROFESSIONAL EXPERIENCE 开头；页脚 "Page X of Y" 正常；无孤立标题；Hengshunyuan 整段留在第 2 页。
- Headline 1 行（97 字符，约 79% 行宽）。Summary 实际渲染 4 / 3 / 3 行。能力表 7 行，每行 2 行内容、标签 1 行。成就 6 条 2 行、1 条 3 行（A2）。经历/早期条目除 E-Baidu（3 行）外均 ≤ 2 行 → **32 条中 2 条为 3 行**。
- 词数 1,241（Summary 162）；红色 run 51/97（红 = 非已批准原句，属预期）。
- Lint 0 命中；美式拼写扫描 0；跨段 5-gram 重复扫描后仅剩 C1 与 A1 共用 "validation, enrichment and status tracking"（能力关键词 vs 成就证据，保留）。
- **未执行：** Microsoft Word 实机渲染（仅 LibreOffice）；ATS 解析测试；人工 cold read。

## (e) 缺口的诚实处理

| 缺口 | 处理 |
|---|---|
| IBM iSeries/AS400、Silverlake | 不提及；面试可说明 Linux (RHEL)/SQL 熟练与多次数据迁移经验，并表明可学习 |
| 乙方报价、成本测算、合同/付款里程碑、开票催款 | 不写；唯一乙方售前证据（AI Park 技术标，S7）照实写；甲方侧经验明确标注 "buyer-side"（A5、C4）与 "as the buyer"（S-P3） |
| 银行项目产品化、IP 归属实践、产品文档 | 不写；产品化证据只用 GBD SaaS 与 AI Park SaaS 模式（非银行） |
| 银行年限约 4 年 | 写 "Vice President at UOB since 2022"，不写银行年限 |
| CTO 头衔 | 从不声称；headline 用 "Banking Technology Leader" |
| Audit trails | 不写（OQ-5） |
| 演示/PoC | 用 "pilots"，不写 "PoC" |

## (f) 需 Wilson 确认的问题（只列会改变事实或定位的；均附默认值）

1. **OQ-1 雇佣形式：** Solderfield 提供的是受薪雇佣（JobStreet 标 Full time + 福利），还是 business partner / 合伙、股权类安排？**默认：未确认受薪前不投递。**
2. **OQ-2 报文转换：** 支付发起 hub 是否自己生成/映射 ISO 20022 MX 报文（共存期也处理 MT），还是由下游 SWIFT 网关映射？**默认：C1 保留 "ISO 20022 (MT-to-MX) message transformation"（🔶，按 card）；若由网关完成，C1 改为 "ISO 20022 (MT-to-MX) migration"。**
3. **OQ-3 GBD 可配置性：** 租户能否不改代码就配置 KYC 层级、认证等级和奖励规则（rule models）？**默认：保留 "configurable"（依据 02 §6.3 "customisable"）；若不能，GBD-3 改回 "rule models"，A3 标签改为 "Multi-tenant SaaS product"。**
4. **OQ-4 Hengshunyuan 版权谈判：** 是否本人与版权方谈判授权条款？**默认：只写 "Ran business development for content licensing"（不写 "negotiated"）；若是，可补 "negotiated licences"，作为 Q6 的商务谈判证据。**
5. **OQ-5 审计轨迹：** hub 设计中是否有审计轨迹（例如为审计保留的支付状态历史）？**默认：不写；若有，在 C5/A6 加入 "audit trails"。**
