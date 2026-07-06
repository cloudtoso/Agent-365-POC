# Agent 365 Proof of Concept — Deck Outline

**Created:** 2026-05-05  
**Author:** Holden (Lead)  
**Status:** Draft for team review  
**Recommended Total Slides:** 38–42

---

## Narrative Arc

The deck follows a **"see it → secure it → prove it → use it"** progression:

1. **Opening** — Frame the problem (ungoverned AI agents) and the promise (enterprise control).
2. **Use Cases 1–2** — Visibility and identity foundations ("see it, secure it").
3. **Use Cases 3–4** — Active protection layer ("protect it, defend it").
4. **Use Case 5** — Evidence and governance ("prove it").
5. **Use Case 6** — Business value payoff ("use it").
6. **Close** — Summarize measurable outcomes, next steps.

Each use case section follows a consistent 5-slide pattern: Context → Capability → Demo → Success Criteria → Differentiator. This gives the audience a predictable rhythm while keeping engagement high.

---

## Section Breakdown

### Section 0: Opening (4 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 1 | **Agent 365 Proof of Concept** | Title slide — set branding and context | Title/branding |
| 2 | **The Agent Governance Gap** | Frame the problem: AI agents are proliferating without the controls we apply to human users | Educational |
| 3 | **What Agent 365 Delivers** | One-slide value prop: identity, security, compliance, observability — one platform | Educational |
| 4 | **POC Scope & Timeline** | Set expectations: Microsoft-platform agents, 4–6 weeks, 6 use cases, roles involved | Educational |

**Flow note:** Slides 2–3 create urgency then resolve it. Slide 4 grounds the audience in what they'll see today.

---

### Section 1: Agent Inventory & Discovery (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 5 | **Use Case 1: See Every Agent** | Section header — set context for discovery | Educational |
| 6 | **Why Inventory Comes First** | Explain you can't secure what you can't see; shadow agent risk | Educational |
| 7 | **Demo: Agent Registry Walkthrough** | Step-by-step demo showing how to pull all agents into a single registry view | Demo walkthrough |
| 8 | **Success Criteria** | Measurable outcomes: 100% agent enumeration, classification by type/owner/scope | Success criteria |
| 9 | **Differentiator: Unified Registry** | Why this matters vs. manual tracking or multi-tool sprawl | Differentiator |

**Flow note:** This section establishes the foundation — every subsequent use case builds on knowing what agents exist.

---

### Section 2: Agent Identity & Least-Privilege Access (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 10 | **Use Case 2: Treat Agents Like Identities** | Section header — agents deserve Entra ID governance | Educational |
| 11 | **From Service Accounts to Agent Identities** | Explain the shift: agents need managed identities, conditional access, least-privilege | Educational |
| 12 | **Demo: Entra ID Agent Identity & Access Controls** | Step-by-step demo showing agent identity creation, permission scoping, conditional access policies | Demo walkthrough |
| 13 | **Success Criteria** | Measurable outcomes: every agent has scoped identity, no standing admin, CA policies enforced | Success criteria |
| 14 | **Differentiator: Identity-First Agent Governance** | Why Entra-native beats bolt-on RBAC; ties to Zero Trust | Differentiator |

**Flow note:** Transitions from "we can see them" to "we can control what they access." Natural escalation.

---

### Section 3: Sensitive Data Protection (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 15 | **Use Case 3: Protect Data from Agent Actions** | Section header — DLP and sensitivity labels for agents | Educational |
| 16 | **Extending Purview to the Agent Layer** | Explain how sensitivity labels and DLP policies already trusted for users now cover agent interactions | Educational |
| 17 | **Demo: Purview DLP & Sensitivity Labels for Agents** | Step-by-step demo showing label enforcement on agent-generated content and DLP policy triggers | Demo walkthrough |
| 18 | **Success Criteria** | Measurable outcomes: labeled content respected by agents, DLP violations blocked/logged | Success criteria |
| 19 | **Differentiator: Same Compliance Stack, New Surface** | Why reusing Purview (not a new tool) reduces adoption friction and audit complexity | Differentiator |

**Flow note:** Moves from identity controls to data controls — the "what can they touch" question.

---

### Section 4: Threat Detection & Response (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 20 | **Use Case 4: Detect Compromised Agents** | Section header — Defender for agent-layer threats | Educational |
| 21 | **Agent-Specific Threat Vectors** | Explain new attack surfaces: prompt injection, credential theft, anomalous agent behavior | Educational |
| 22 | **Demo: Defender Detects Anomalous Agent Behavior** | Step-by-step demo showing alert generation, investigation, and response for a compromised agent scenario | Demo walkthrough |
| 23 | **Success Criteria** | Measurable outcomes: alerts fire on anomaly, MTTD < X minutes, automated containment available | Success criteria |
| 24 | **Differentiator: SOC Integration, Not Another Console** | Why Defender-native means existing SOC workflows apply — no retraining | Differentiator |

**Flow note:** Escalates from prevention to active defense. Satisfies CISO audience directly.

---

### Section 5: Audit, Compliance & Lifecycle (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 25 | **Use Case 5: Prove It to Auditors** | Section header — full activity records and lifecycle governance | Educational |
| 26 | **Cradle-to-Grave Agent Governance** | Explain lifecycle management: provisioning, activity logging, offboarding, retention | Educational |
| 27 | **Demo: Audit Trail & Agent Offboarding** | Step-by-step demo showing activity log queries, compliance reports, and agent decommissioning workflow | Demo walkthrough |
| 28 | **Success Criteria** | Measurable outcomes: immutable audit trail, offboarding completes in < 24h, no orphaned permissions | Success criteria |
| 29 | **Differentiator: Compliance-Ready from Day One** | Why built-in audit beats retrofitted logging; maps to regulatory frameworks | Differentiator |

**Flow note:** "Prove it" section — gives the compliance lead their evidence story before pivoting to business value.

---

### Section 6: Productivity Integration (5 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 30 | **Use Case 6: Agents That Work Where You Work** | Section header — Outlook, Teams, Word, SharePoint integration | Educational |
| 31 | **Governed Productivity, Not Governed Friction** | Explain that admin controls don't block productivity — agents operate in familiar surfaces with guardrails | Educational |
| 32 | **Demo: Agents in Teams & SharePoint with Admin Controls** | Step-by-step demo showing agent interactions in M365 apps and the admin controls governing them | Demo walkthrough |
| 33 | **Success Criteria** | Measurable outcomes: agents active in ≥3 M365 surfaces, user satisfaction maintained, no policy bypass | Success criteria |
| 34 | **Differentiator: Native M365 Integration** | Why platform-native agents outperform bolt-on copilots that lack admin control surfaces | Differentiator |

**Flow note:** Ends on the positive — after all the security/compliance rigor, this shows the payoff for end users.

---

### Section 7: Summary & Next Steps (4 slides)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| 35 | **POC Outcomes at a Glance** | Single-page summary: 6 use cases, key metrics achieved, governance posture | Educational |
| 36 | **CIO/CISO Decision Framework** | What evidence the POC produces for go/no-go approval decisions | Educational |
| 37 | **Recommended Next Steps** | Expand scope, production rollout path, timeline for full deployment | Educational |
| 38 | **Thank You & Contact** | Closing slide with team contacts, resources, and follow-up commitments | Closing |

**Flow note:** Quick, decisive close. No new concepts — just synthesis and action.

---

## Appendix Slides (optional, 2–4 slides as needed)

| # | Slide Title | Purpose | Content Type |
|---|------------|---------|--------------|
| A1 | **Roles & Responsibilities** | Reference: exec sponsor, IT admin, identity admin, data security lead, SOC analyst, business owners | Reference |
| A2 | **Agent Types in Scope** | Reference: M365 Copilot, Copilot Agent Builder, Copilot Studio, M365 Copilot Chat, SharePoint agents, Azure AI Foundry agents, first-party agents | Reference |
| A3 | **Glossary** | Key terms for mixed-audience understanding | Reference |

---

## Title Slide Content (Suggested)

> **Agent 365 Proof of Concept**  
> *Bringing AI Agents Under Enterprise Control*  
> [Customer Logo] | [Microsoft Logo]  
> [Date] | [Presenter Name]

---

## Closing Slide Content (Suggested)

> **Next Steps**  
> ✓ Review POC findings with your governance board  
> ✓ Identify expansion candidates (additional agent types)  
> ✓ Schedule production readiness review  
>  
> *Your agents. Your rules. Your platform.*  
> [Contact details] | [Resources link]

---

## Design Notes for Naomi (Content Author)

- Each "Demo walkthrough" slide should have a placeholder for Amos's step-by-step instructions (numbered list format)
- Success criteria slides should use a checklist or scorecard visual
- Differentiator slides should use a comparison format (Agent 365 vs. alternative approaches)
- Keep text minimal — this is a presentation, not a document. Target ≤6 bullet points per slide.
- Use the consistent 5-slide pattern per UC to build audience rhythm and predictability.
