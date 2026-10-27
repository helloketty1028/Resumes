# Batch Triage — JobStreet "cto" search (Singapore, ≥ S$10k/month, 7 classifications)

- **工具 / 模式：** 工具 C v1.0 · `triage`（只做阶段一，停在审批门 C1，不生成简历）
- **日期：** 2026-10-20 · **来源：** JobStreet 搜索 URL（用户提供；WebFetch 因 URL 过长被代理拒绝 → 改用 Claude in Chrome 读取）
- **事实库（只读，开工时记录）：** `master\v2.0-draft\` — 01 v1.1 (2026-10-20 10:05) · 02 v3.1 (2026-10-17) · 03 v4.1 (2026-10-17) · 04 v1.2 (2026-10-20) · 05 v1.0 (2026-10-16) · skills inventory v2.3 · fact-check v2.4 (2026-10-20)。批次中未发现改动。
- **full 模式（2026-10-21 启动，2026-10-26 完成）：** A/B 档 10 份已出**终稿**（审批门 C3 于 2026-10-26 通过）。下载链接见 §2 最后一列，汇总见 [Batch_Summary.md](Batch_Summary.md)；职位名称已链接到 JobStreet 原帖。
- **Project knowledge 副本未作为事实来源**（工具 A §2 规则 3）。

## 0. 漏斗（135 → 20 → 档位）

| 步骤 | 数量 | 说明 |
|---|---|---|
| 搜索结果 | 135 | 5 页全部抓取，清单见 `Search_Results_2026-10-20.md` |
| 标题级预筛排除 | 106 | IC 工程师 / 产品 / UX / 网络安全与 GRC / 企业内部 IT 与基础设施 / 咨询销售 / 其他领域；以及命中 05 §4 fast-reject（C++ 低延迟股票、SAP 项目、Databricks、CargoWise 等） |
| 已申请或此前评估过（不重复分诊） | 9 | 见 §4 |
| **读取 JD 全文并分诊** | **20** | 超出工具 C 建议的 2–8 份；本表用于挑选，C1 后建议只推进 3–5 份 |

## 1. 评分口径（应用户 2026-10-20 22:55 明确要求加入；仅本批次，不改变 D-03 规则）

- **匹配度分数 = Required 证据覆盖率**：Direct = 1，Transferable = 0.5，Gap / Unverified = 0；分母 = JD 明写的 Required 条数（Preferred 不计）。
- 分数**不含**资历落差、薪资、雇佣形式、岗位新旧等风险，这些在“阻断项 / 风险”列单列；**命中 Eligibility 或 fast-reject 的一律 X 档，不论分数**。
- 不是面试概率。档位（A/B/C/X）仍是主判断，分数是辅助排序。

## 2. 分诊总表（按档位、分数排序）

| # | 公司 | 职位 (Job ID) | 档位 | 匹配度 | Family×Lens | D/T/G/U | 阻断项 / 主要 gap | Eligibility / 其他风险 | 与旧申请重复 | 建议动作 | 简历（终稿，C3 已批 2026-10-26） |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NETS | [Principal Engineer](https://sg.jobstreet.com/job/95218038) (95218038) | **A** | **87** | ATL×BNK | 11/4/0/0 | 支付生态仍为 T：有电商 / 本地生活的支付接入与结算对账（Renren Mall、糯米、VV-Life，C1 补充），无交换 / POS / QR 收单 / 卡组织直连认证；Solace JMS 无记录；PCI-DSS 仅控制目标层面 | 无；薪资未披露 | 无 | **优先推进**。底稿 `Archi_Bank_LIB_V5`，需重新取材（payments + hands-on） | **[DOCX](../../2026-10-21_NETS_Principal-Engineer/wilson-2026_ATL_Bank_NETS_V1_0_0.docx) · [PDF](../../2026-10-21_NETS_Principal-Engineer/wilson-2026_ATL_Bank_NETS_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_NETS_Principal-Engineer/wilson-2026_ATL_Bank_NETS_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_NETS_Principal-Engineer/JD_Matching_Analysis.md) |
| 2 | Private Advertiser（金融服务） | [Head of Technology Development](https://sg.jobstreet.com/job/95063994) (95063994) | **A** | **95** | SM×BNK | 10/1/0/0 | chatbot / 移动 App 项目弱（PA-14 ⛔） | 薪资上限 S$12k（C1：底线可谈，看总包）；雇主匿名；“lean team” | 无 | 可投，但先定薪资底线（Q1）。底稿 `Senior_Tech_Bank_LIB_V5` 微调 | **[DOCX](../../2026-10-21_PrivateAdvertiser_Head-of-Technology-Development/wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0.docx) · [PDF](../../2026-10-21_PrivateAdvertiser_Head-of-Technology-Development/wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_PrivateAdvertiser_Head-of-Technology-Development/wilson-2026_SM_Bank_PrivateAdvertiser_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_PrivateAdvertiser_Head-of-Technology-Development/JD_Matching_Analysis.md) |
| 3 | Stripe | [Engineering Manager, Disputes Foundation](https://sg.jobstreet.com/job/88429529) (88429529) | **A** | **93** | SM×INT（fintech 按互联网招聘，OQ-P2） | 6/1/0/0 | “8+ yrs full-time software development”：纯 IC 约 2008–2014，之后为带队 + hands-on（X-04） | 发布 30d+，**先确认仍开放**；Stripe 面试编码 / 系统设计门槛高 | 记忆：此前做过 Stripe TPM（LPM）定制版 → 需口径一致 | 确认开放后推进；底稿取 Talentvis `SM_Internet` V1 | **[DOCX](../../2026-10-21_Stripe_EM-Disputes-Foundation/wilson-2026_SM_Internet_Stripe_V1_0_0.docx) · [PDF](../../2026-10-21_Stripe_EM-Disputes-Foundation/wilson-2026_SM_Internet_Stripe_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_Stripe_EM-Disputes-Foundation/wilson-2026_SM_Internet_Stripe_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_Stripe_EM-Disputes-Foundation/JD_Matching_Analysis.md) |
| 4 | DBS Bank | [SVP, Engineering Lead, Core Banking Technology](https://sg.jobstreet.com/job/95272188) (95272188) | **B** | 93 ↑ | ATL×BNK | 6/1/0/0 | Core Banking 领域：G→T（C1 答复：CBPR+ / C360 与核心系统集成——结算、账户日汇总、组合分析；是集成侧经验，不是核心系统本身） | VP2 → SVP 职级跳跃 | 无 | 值得一试；Gap 诚实写成“相邻领域”。底稿 `Archi_Bank_LIB_V5` | **[DOCX](../../2026-10-21_DBS_SVP-Engineering-Lead-Core-Banking/wilson-2026_ATL_Bank_DBS_V1_0_0.docx) · [PDF](../../2026-10-21_DBS_SVP-Engineering-Lead-Core-Banking/wilson-2026_ATL_Bank_DBS_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_DBS_SVP-Engineering-Lead-Core-Banking/wilson-2026_ATL_Bank_DBS_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_DBS_SVP-Engineering-Lead-Core-Banking/JD_Matching_Analysis.md) |
| 5 | Solderfield | [CTO / Director（Business Partner）](https://sg.jobstreet.com/job/95022480) (95022480) | **B** | 83 | SM×BNK | 6/3/0/0 | 售前 / 定价 / 合同谈判仅买方经验（X-02）；产品化为 GBD SaaS 迁移证据 | **“business partner” 雇佣形式不明**（可能非受薪）；IBM iSeries/AS400 技术栈；51–100 人公司 | 无 | 先向雇主确认是否受薪雇佣；非受薪则不投（C1） | **[DOCX](../../2026-10-21_Solderfield_CTO-Director/wilson-2026_SM_Bank_Solderfield_V1_0_0.docx) · [PDF](../../2026-10-21_Solderfield_CTO-Director/wilson-2026_SM_Bank_Solderfield_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_Solderfield_CTO-Director/wilson-2026_SM_Bank_Solderfield_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_Solderfield_CTO-Director/JD_Matching_Analysis.md) |
| 6 | Airwallex | [Engineering Lead/Manager, Growth](https://sg.jobstreet.com/job/88086261) (88086261) | **B** | 81 | SM×INT | 6/1/1/0 | Growth 工程（漏斗、A/B 框架、营销平台）= Gap；hands-on 设计实现为 T | **JD 不完整**（无 Requirements 段，按 §10 最高 B）；发布 30d+；SG / 上海双地 | 无 | 中等优先；先确认仍开放 | **[DOCX](../../2026-10-21_Airwallex_Engineering-Lead-Growth/wilson-2026_SM_Internet_Airwallex_V1_0_0.docx) · [PDF](../../2026-10-21_Airwallex_Engineering-Lead-Growth/wilson-2026_SM_Internet_Airwallex_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_Airwallex_Engineering-Lead-Growth/wilson-2026_SM_Internet_Airwallex_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_Airwallex_Engineering-Lead-Growth/JD_Matching_Analysis.md) |
| 7 | Landi International | [Chief Technology Officer](https://sg.jobstreet.com/job/95323660) (95323660) | **B** | 75 | SM×BNK（支付硬件） | 5/5/0/0 | POS 终端 / 联网设备（AI Park IoT 为桥接，T）；多国市场技术战略（T）；从未任 CTO 头衔（HR-1：可写目标职位，历史职位不改） | 外国公司，未经 JobStreet 雇主核验；薪资未披露 | 无 | **推荐**：支付 + 海外市场 + 中文背景匹配度高。底稿 `Senior_Tech_Bank_LIB_V5` | **[DOCX](../../2026-10-21_Landi_CTO/wilson-2026_SM_Bank_Landi_V1_0_0.docx) · [PDF](../../2026-10-21_Landi_CTO/wilson-2026_SM_Bank_Landi_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_Landi_CTO/wilson-2026_SM_Bank_Landi_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_Landi_CTO/JD_Matching_Analysis.md) |
| 8 | Income Insurance | [Head, Technology Transformation](https://sg.jobstreet.com/job/95105986) (95105986) | **B** | 75 | TPM×BNK | 3/3/0/0 | “15+ yrs leading large-scale transformation”（T）；企业级项目组合 / 收益实现无记录 | PMP 等为 preferred（PMP 进行中） | 无 | 推荐：符合“进入新业务领域”的动机。底稿 `TPM_Bank_LIB_V5` | **[DOCX](../../2026-10-21_Income_Head-Technology-Transformation/wilson-2026_TPM_Bank_Income_V1_0_0.docx) · [PDF](../../2026-10-21_Income_Head-Technology-Transformation/wilson-2026_TPM_Bank_Income_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_Income_Head-Technology-Transformation/wilson-2026_TPM_Bank_Income_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_Income_Head-Technology-Transformation/JD_Matching_Analysis.md) |
| 9 | NCS | [Associate Director – Solution Architect (Technical)](https://sg.jobstreet.com/job/94992125) (94992125) | **B** | 75 | ATL×INT | 2/2/0/0 | SI 售前 / 客户侧架构（T）；可复用资产（GBD SaaS，T） | 同属 Singtel 集团：**Singtel Delivery Manager 申请进行中** | Singtel / NCS（记忆） | 投前核对与 Singtel 申请的口径一致 | **[DOCX](../../2026-10-21_NCS_AD-Solution-Architect/wilson-2026_ATL_Internet_NCS_V1_0_0.docx) · [PDF](../../2026-10-21_NCS_AD-Solution-Architect/wilson-2026_ATL_Internet_NCS_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_NCS_AD-Solution-Architect/wilson-2026_ATL_Internet_NCS_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_NCS_AD-Solution-Architect/JD_Matching_Analysis.md) |
| 10 | CMA CGM | [APAC Head of AI and Innovation](https://sg.jobstreet.com/job/95377348) (95377348) | **B** | 71 | SM×INT | 3/4/0/0 | 低代码 / Citizen Developer 平台、组织数字素养项目无记录；Power BI 仅 F/P | 仅限本地雇佣（PR 符合）；物流行业（不是 fast-reject 的 cross-border logistics 业务，但需小心措辞） | 无 | 可投；AI 作为支柱而非身份（01 §5）。发布仅 9 小时 | **[DOCX](../../2026-10-21_CMA-CGM_APAC-Head-AI-Innovation/wilson-2026_SM_Internet_CMACGM_V1_0_0.docx) · [PDF](../../2026-10-21_CMA-CGM_APAC-Head-AI-Innovation/wilson-2026_SM_Internet_CMACGM_V1_0_0.pdf)** · [红字草稿](../../2026-10-21_CMA-CGM_APAC-Head-AI-Innovation/wilson-2026_SM_Internet_CMACGM_V1_0_0_draft.docx) · [匹配分析](../../2026-10-21_CMA-CGM_APAC-Head-AI-Innovation/JD_Matching_Analysis.md) |
| 11 | JERA Global Markets | [Senior Manager, IT Performance & PMO](https://sg.jobstreet.com/job/95387860) (95387860) | **C** | 79 | TPM×INT | 4/3/0/0 | COBIT / NIST / ITIL 框架（T/G）；审计证据协调无记录 | **定位偏离**：二线报告 / PMO 支持角色，明确“无预算权、不指挥”，8–12 年经验 → 降级风险 | 无 | 不建议，除非想转治理报告方向 | — |
| 12 | Standard Chartered | [Global Head, Software Engineering](https://sg.jobstreet.com/job/95294993) (95294993) | **C** | 67 | SM×BNK | 5/6/1/0 | **全球大型工程组织领导 = Gap**（现 25 人；VV 140 为总人数） | VP2 → 全球 Head（MD 级）跨度过大 | 记忆：此前评估过 SCB WRB Engineering Lead | 不建议本轮投入 | — |
| 13 | FPT Asia Pacific | [Chief Architect](https://sg.jobstreet.com/job/91427867) (91427867) | **C** | 67 | ATL×INT | 3/2/1/0 | **TOGAF / EA 框架 = Gap**（05 §7.2）；SI 售前投标仅 AI Park | 职责写“for FPT Thailand”，地点 / 出差待确认；30d+ | 无 | 低优先 | — |
| 14 | JAC Recruitment（零售客户） | [Head of Technology (Retail & Digital)](https://sg.jobstreet.com/job/95002023) (95002023) | **C** | 65 | SM×INT | 4/5/1/0 | **SAP S/4HANA + POS/WMS 实操 = Gap**；零售行业 mandatory：只有电商 / 本地生活平台（Renren Mall、Nuomi、VV-Life）可作桥接 | 申请量高；S$20–25k | 无 | 不建议（企业 ERP 权重，与此前 Canon 类似） | — |
| 15 | Activate Interactive | [Associate Solutions Director](https://sg.jobstreet.com/job/93501149) (93501149) | **C** | 65 | TPM×INT | 5/3/2/0 | **新加坡公共部门项目经验（IM8）= Gap**；PMP / ITIL / AWS 证书列为要求 | 供应商侧利润率 / 计费管理 | 无 | 不建议 | — |
| 16 | Temasek International | [VP/Director, Technology, Cloud Platform](https://sg.jobstreet.com/job/89229682) (89229682) | **C** | 62 | SM×BNK | 3/4/1/0 | **数据中心 / 全球网络 / 云平台运维 = Gap** | JD 不完整（只有职责）；30d+ | 无 | 不建议 | — |
| 17 | Intellipro（猎头，AI SaaS 客户） | [Chief Technology Officer](https://sg.jobstreet.com/job/95315793) (95315793) | **C** | 50 | SM×INT | 2/4/2/0 | **销售 / GTM、技术布道与行业影响力 = Gap**；咨询经验仅 Pureland（⛔ 未定披露） | 雇主问题“任 CTO 年数”→ 0；须附 cover letter | Talentvis CTO 已定稿（同类 AI CTO） | 不建议 | — |
| 18 | Singapore International Foundation | [Head/Deputy Director, Data & Technology](https://sg.jobstreet.com/job/95237586) (95237586) | **X** | 69 | SM×INT | 4/3/1/0 | build-vs-buy 决策无经验（项目画像已确认） | **Eligibility：JD 明写 “Singaporean”**，你是 PR | 无 | 不投 | — |
| 19 | MUFG Bank | [Director, APAC Head of Platform Services](https://sg.jobstreet.com/job/93336713) (93336713) | **X** | 62 | SM×BNK | 6/4/3/0 | **基础设施平台核心领域 = Gap**（hosting、虚拟化、Windows/Linux 服务器群、AWS+Azure 运维）；**云证书列为要求** | 30d+ | 记忆：此前评估过 MUFG VP Technical Lead Payments | 不投 | — |
| 20 | TEKsystems (Allegis) | [Senior Programme Manager – AI datacenter](https://sg.jobstreet.com/job/95291624) (95291624) | **X** | 38 | TPM×INT | 1/1/2/0 | **Fast-reject：GPU 基础设施为核心要求**（05 §4）；10 年数据中心经验必需 | 东南亚长期出差 | 同一猎头 TEKsystems（2026-10-17 已定稿 Program Manager） | 不投 | — |


## 3. 逐份证据要点（Required → 证据 ID → 状态）

**1 NETS Principal Engineer** — 10y+ 技术权威 → 02 §2、X-04 **D** · 大型现代化 / 迁移、多供应商并行 → PA-01.5、X-05 **D** · Java/Spring Boot/REST/RHEL/容器/云/EIP → PA-01.3、skills (Java P, RHEL P, K8s A, AWS A, Camel) **D**（Solace JMS 无记录）· 低延迟高可用交易系统 → PA-01.4、PA-02.1 **D** · 数字支付生态（交换、POS、QR、卡、清结算、卡组织）→ PA-01（发起端）、PA-04（催收读卡账户数据）+ 支付方式接入与结算对账（C1 补充，待入库）**T** · 云集成 / API 管理 → PA-10.1 **D** · PCI-DSS / 加密 / 令牌化 / DR → X-01、PA-02.1，PCI-DSS 仅控制目标 **T** · DevSecOps / CI/CD / 可观测性 → PA-03.2、PA-02.2 **D** · 工程标准与护栏 → PA-03.3（contributed）、X-04 **D** · 多轨并行、受监管 → X-02 **D** · 战略 + hands-on → X-04 **D** · 与银行 / 卡组织关系 → X-05（供应商）**T** · 沟通 **T** · 带教高级工程师 → X-02 **D**。

**2 Private Head of Technology Development** — 学位（硕士 CS）**D** · 8y 技术 + 管理 **D** · 金融 / 强监管 → MAS TRM（PA-03.4）**D** · 多学科团队 → X-02 **D** · 渠道 / 触点领域：CMS（PA-18）、API 网关（PA-10）、支付网关（PA-01、PA-11.2）、B2B/B2C 集成 **D**，chatbot（PA-14 ⛔）与移动 App 弱 → 整体 **T** · Jira/Confluence **D** · Java/JavaScript **D** · 按期交付（PA-01.1）**D** · Scrum（PA-10.3）**D** · 干系人 **D** · 远程 / 混合团队（离岸 5+ 年）**D**。

**3 Stripe EM** — 3+ 年 EM → X-02 **D** · 8+ 年全职开发 → Renren / Sohu / Baidu 2008–2014 + X-04 **T** · 招聘与培养 → PA-10.3、PA-11.1 **D** · 模糊环境带头 → PA-10.1、PA-15.1 **D** · 生产系统运维严谨 → X-06、PA-02 **D** · 可扩展系统 → PA-10.1 **D** · 跨时区协作 → X-02（India / Thailand / Indonesia）**D**。Preferred：支付行业 **D**。

**4 DBS SVP Core Banking** — 大规模交易处理 → PA-01 **D** · 带队且深度参与架构 → X-04 **D** · Java/Spring Boot、React、微服务、EDA、CI/CD、Linux/中间件、K8s、MongoDB → skills **D** · 分布式 / 高可用 → PA-02.1 **D** · **Core Banking 领域（Deposits、Loans、GL、Settlement）→ G**（贷款服务 PA-04、客户 360 PA-05 为相邻）· 平台现代化 → PA-01 **D** · 干系人 **D**。

**5 Solderfield** — 银行技术（mandatory）→ PA-01 **D** · CTO/SA/技术总监等同 → 02 §2 **D** · 中间件 / API / 微服务 / 报文转换 / 遗留现代化 → PA-01（MT→MX，Camel）**D** · 产品化 → PA-10.1 **T** · 商机与提案 → PA-16.2 **T** · 定价与合同谈判 → X-02（买方 SOW/licence）**T** · 端到端交付 → PA-01.5 **D** · 银行治理（访问控制、变更、发布、韧性）→ PA-03、PA-02 **D** · 创业心态 → PA-15 **D**。

**6 Airwallex**（JD 无 Requirements 段，按职责拆）— 带团队 / 目标 / 反馈 **D** · 与 PM 拆需求出方案 **D** · 亲自设计实现 → X-04 **T** · 设计评审 / 代码评审 → X-04 **D** · Backlog **D** · 招聘培养 **D** · 跨团队协作 **D** · Growth 工程（A/B 框架、漏斗、营销平台）**G**。

**7 Landi CTO** — 学位 **D** · 15y + 5y 高管 → 02 §2（2016–2020 技术负责人 + UOB VP2）**T** · 海外市场技术战略 → PA-13（东南亚）、PA-10.2 **T** · 支付 / 金融科技 → PA-01 **D** · 支付终端 / 联网设备 → PA-16（IoT 停车场设备）**T** · 多市场交付、本地化、支持 → PA-16.2 **T** · 分布式技术 + PM 团队 → X-02 **D** · 预算 / 资源 / 产能 → X-02、X-05 **D** · 对董事会沟通 → 指导委员会（PA-01.5）**T** · 新兴技术 / AI 产品 → PA-07 **D**。

**8 Income** — 15+ 年转型领导 **T** · 企业级项目 **T** · 现代化 / 数字化 / AI 采用 → PA-01、PA-07 **D** · C-suite 干系人 **T** · 供应商生态 → X-05 **D** · 学位 **D**。

**9 NCS AD SA** — SI / 企业架构经验 → PA-01.2、PA-10.1 **D** · 可复用资产 **T** · 微服务 / 云原生 / API-first **D** · 客户侧沟通 **T**。

**10 CMA CGM** — 学位 **D** · 10y+ 技术领导 + 生产级 AI → PA-07 **D** · 全球矩阵组织影响力 **T** · 企业级部署与创新 → PA-01、PA-10.1 **D** · Power BI / 低代码 / GenAI 框架 **T** · 组织变革与数字素养 → PA-03 §6（AI 辅助工程辅导）**T** · ROI → PA-07.3（估算）**T**。

**11–20**：要点见总表“阻断项”列；全文要求见 `inbox\`。

## 4. 已申请 / 此前评估过（未重复分诊）

| 搜索序号 | 职位 | 状态 |
|---|---|---|
| 101 | Talentvis — CTO (Enterprise AI) 95342414 | `applications\2026-10-20_Talentvis_CTO\` 已有终稿 |
| 125 | Singtel — Delivery Manager 90510835 | 申请进行中（HR 筛选，记忆） |
| 19 | StarHub — AVP, TPM Lead 91789647 | 此前评估过；页面显示 “Visited application site” |
| 102 | So Drama! — Head, Technology & Platform Solutions 94829653 | 此前评估并做过定制版 |
| 99 / 48 | MTC / PERSOL — Head of IT (CargoWise) | 此前评估（物流 Head IT 版本）；CargoWise gap |
| 44 | Canon — Senior Director (IT) | 此前 fast-reject |
| 41 / 11 | WSG — Product Owner (Job Matching) | 产品岗，此前 WSG 类岗位不匹配 |

> 以上“此前评估”来自记忆记录；`applications\` 下只有 TEKsystems、Talentvis 两个目录。

## 5. 共性问题（每条只问一次；不回答时按默认处理）

| # | 问题 | 涉及 JD | 不回答时的默认处理 |
|---|---|---|---|
| Q1 | 求职筛选条件（OQ-J1）：月薪底线是否仍为 S$12k？是否接受“business partner”这类非受薪安排？是否仍排除银行？ | 2、5、4、12、19 | 银行不排除（D-07 未执行）；Private（上限 12k）保留但标风险；Solderfield 视为“待确认雇佣形式”，不进入 C2 |
| Q2 | 有没有接触过**卡交换 / POS 终端 / QR / 卡组织接入**（哪怕是对接或评审）？ | 1、7 | 记为 Gap，只用支付发起 + 催收读卡账户数据作桥接 |
| Q3 | 除 AI Park 投标外，有没有**乙方售前 / 方案报价 / RFP 应答 / 合同谈判**经历（GBD、VV、Hengshunyuan）？ | 5、9、13、15、17 | 只用 PA-16.2 作证据，其余记 Gap |
| Q4 | UOB 是否接触过 **Core Banking 领域**（存款、总账、结算）或与核心系统的集成？ | 4 | 记为 Gap，写“adjacent: lending servicing, customer-360, payments” |
| Q5 | 项目画像里已确认“GBD 40 / VV 140 为总人数，直接下属最多 15–20 人”，但 03 中 OQ-2.3 仍标 ❓。是否作为回灌候选？ | 4、7、12（组织规模类要求） | 本批简历按 03 现状处理：不写 140；记入回灌候选 |
| Q6 | 当前编码占比口径保持 X-04（不写百分比）即可？Stripe / Airwallex 面试会追问近期 hands-on | 3、6 | 按 X-04 措辞，不写百分比 |

## 6. 批次观察（只给依据，不替你决定）

- **定位分散**：20 份横跨 SM（10）、ATL（5）、TPM（5），行业有支付、银行、保险、零售、物流、能源、SI。真正同时满足“支付 / 受监管 + 技术领导 + 你的主线”的只有 **NETS、Landi、Private Head of Tech Dev、DBS**；Stripe / Airwallex 是 fintech 但按互联网方式招聘。
- **建议集中 3–5 份**：A 档 3 份 + Landi（B，行业与中文背景加分）+ Income 或 DBS 其一。这样在 SM×BNK、ATL×BNK 两个格子内复用素材，减少跨简历不一致风险。
- **两份 30d+ 旧帖**（Stripe、Airwallex）先确认仍开放再投入。
- **“cto” 关键词搜索噪声大**：135 条中只有 3 条是真 CTO 岗，且都偏销售 / 合伙 / 海外战略。下次可改用 “Head of Technology / Head of Engineering / Principal Engineer payments” 等关键词。

## 7. C1 答复记录（2026-10-20 23:22）

| # | 你的答复 | 处理 |
|---|---|---|
| Q1 | 月薪底线可谈，看总包；不接受非受薪安排；从不排除银行 | Private 风险降级；Solderfield 待雇主确认是否受薪 |
| Q2 | 做电商平台时引入支付网关：银行卡绑定支付接口、卡组织结算与对账 | 待补：哪家雇主、时期、你的角色（设计 / 编码 / 带队）→ 确认后 NETS、Landi 的支付生态项证据加强（仍为 T：无交换 / POS 终端） |
| Q3 | 只有 AI Park 有投标、写标书经验 | 维持原判（售前类要求 = T/G） |
| Q4 | CBPR+、C360 都与 core banking 协作：支付记录结算、账户数据每日汇总、组合分析 | DBS 由 86 → 93；措辞须为“integrated with core banking”，不写成拥有核心系统（与 CF-N4“hub 不做清结算”一致） |
| Q5 | 询问“回灌候选”含义；要求对 03 中未明确项给出确认提醒 | 见会话中的确认提醒（OQ-2.3） |
| Q6 | 询问 X-04 口径与“百分比”含义 | 已解释，待你确认 |
| Q2b（23:41） | Renren Mall、糯米：技术专家，亲自写核心代码并设计（Alipay、微信支付、银联）；VV-Life：技术负责人兼架构师（银联、Visa/Mastercard、Google Pay、GrabPay） | ⚠ 微信支付 2013-08 上线，晚于 Renren 任期（2008.7–2012.3）→ 默认 Renren = Alipay + 银联；VV 默认写“经收单 / 网关接入”。NETS、Landi、Private 分数不变（仍为 T 或已计入） |
| Q4b | 确认：结算由核心系统执行，你的系统发送并接收结果 | DBS 93 保持 |
| Q5b | (a) GBD 40 人含外包；(b) VV 有完整技术管理架构，你不管理全部技术人员，直接工作关系约 15–20 人 | (a) 与已定稿写法 “(total headcount)” 一致；(b) 有两种理解，待你选定（见 §7.1） |
| Q6b | X-04 改述为“每天 review 新提交的核心 PR”；不写百分比 | 50 / 20 两个数字是否保留待确认；默认本批不用 |
| Q2c（10-21 10:30） | Renren / 糯米按默认分配；VV：你本人未直接做卡组织直连，技术团队做过 | B-01 ✅；直连的接入形式待补（B-02）；NETS 分数不变 |
| Q5c | VV 140 选理解 ①：全部在你负责的技术中心之下，由下级经理分层管理 | 与两份终稿一致（B-05 ✅） |
| Q6c | X-04 按新说法写，不用 50 / 20 | B-06（50 / 20 不退役，只是本批不用） |
| O-1 | 职位名再确认：Head of Technical Centre / VP of Technical Department | 本批沿用；回灌走 TU-13 |
| O-2 | GBD 按默认措辞 “multi-tenant SaaS for online-game businesses” | OQ-1.9 保持未决 |
| O-3 | C7 并发控制模块：要写，是技术优势 | B-09，用素材库原句 |
| O-4 | VV “10M 并发”、糯米 “5–10M QPS”：保留 | 不退役；口径确认前不进简历（B-10） |

### 7.1 与已定稿简历的一致性提示（工具 C §7，提前列出）

| 事实项 | TEKsystems 终稿 | Talentvis 终稿 | 本批新答复 | 状态 |
|---|---|---|---|---|
| VV 140 人 | Led VV's 140-person technology organisation (total headcount) | 同左（2026-10-20 你批准的措辞） | 不管理全部技术人员，直接工作关系 15–20 人 | ✅ 一致（10-21 选理解 ①） |
| GBD 40 人 | Led a 40-person project team (total headcount) | 同左 | 含外包 | ✅ 一致 |
| UOB 日常 review | 未写 | ~50 code modules（deep review of ~20） | 每天 review 新提交的核心 PR | ✅ 口径收窄，两者均属实（10-21） |
| VV / AI Park 职位名 | Head of Technical Centre / VP of Technical Department | 同左 | — | ✅ 10-21 再确认；02 仍为旧写法，待 TU-13 入库 |

以上新事实均为**回灌候选**，阶段六汇总进 `Batch_Fact_Update_Proposal.md` 由你逐条决定；本工具不写事实库。

## ★ 审批门 C1
请选择进入阶段二（定位卡）的 JD 编号，可调整档位，并回答 Q1–Q6（可只答部分）。triage 模式到此结束。

## 8. full 模式进度（2026-10-26）

- **终稿：** 10 份全黑终稿（去掉 `_draft`）已放进各申请文件夹。都是 3 页，版式检查通过，禁用词 0 处。
- **审计与修订：** 每份都经过独立事实审计、HR 冷读、修订；C3 的改动另做了一次独立复核。
- **C3 答复（2026-10-26）：** K1 VV、GBD 可称 scale-ups · K2 只有一个 steering committee · K3 改为“向 business team 汇报状态、风险和决策” · K4 VV 微服务框架代码由你亲手编写，保留 “built” · K5 99% SonarQube 门禁覆盖全部代码 · PA-03.5（CRQ / CAB）已加入 01、04、08、09。
- **相关文件：** 汇总 [Batch_Summary.md](Batch_Summary.md) · 一致性检查 [Batch_Consistency_Check.md](Batch_Consistency_Check.md) · C3 改动复核 [C3_Edit_Review.md](C3_Edit_Review.md) · 定位卡 [Batch_Positioning.md](Batch_Positioning.md) · 回灌候选 [Batch_Fact_Update_Proposal.md](Batch_Fact_Update_Proposal.md)
- **下一步：审批门 C4。** 回灌候选逐条选 Y / E / Q / L / N，默认 N。

