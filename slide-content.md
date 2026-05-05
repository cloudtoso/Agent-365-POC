# Agent 365 Proof of Value — Slide Content

> **Deck Purpose:** Customer enablement presentation demonstrating that Agent 365 brings AI agents under the same identity, security, compliance, and observability controls already trusted for users.
> **Audience:** IT decision-makers, security leads, compliance officers
> **Estimated Duration:** 60–90 minutes (including demos)

---

## INTRO SECTION

---

### Slide 1: Title Slide

**Title:** Agent 365 — Proof of Value

**Bullets:**
- Govern AI Agents with the Controls You Already Trust
- [Customer Name] | [Date]
- 4–6 Week Engagement

**Speaker Notes:**
Welcome everyone. Today we're kicking off the Agent 365 Proof of Value — a focused engagement designed to show you how Microsoft brings AI agents under the same governance controls you already rely on for your people. Over the next 4 to 6 weeks, we'll prove this with your real agents, in your real environment.

**Visual Suggestion:** Full-bleed hero image showing a network of interconnected AI agent icons flowing into a unified Microsoft 365 shield. Customer logo and Microsoft logo side by side.

---

### Slide 2: The Governance Gap

**Title:** AI Agents Are Growing — Governance Isn't Keeping Up

**Bullets:**
- Organizations are deploying 10–50+ AI agents across departments — often without IT visibility
- Shadow agents create blind spots in identity, data protection, and compliance
- Traditional tools weren't built for non-human actors operating at machine speed
- The gap between agent adoption and agent governance widens every quarter

**Speaker Notes:**
Here's the challenge: your teams are already building and adopting AI agents. But most governance tooling was designed for human users — login screens, DLP policies, compliance audits. Agents don't fit that mold natively. The result is shadow agents, ungoverned data access, and compliance gaps that auditors will eventually find. This is the problem Agent 365 was built to solve.

**Visual Suggestion:** Split-screen graphic — left side shows a proliferation of agent icons (chatbots, copilots, custom agents) growing chaotically; right side shows a question mark over traditional governance tools (firewalls, IAM consoles). A visible "gap" between the two halves.

---

### Slide 3: What Agent 365 Delivers

**Title:** One Platform. Same Controls. Now for Agents.

**Bullets:**
- Discover and register every agent — eliminate shadow AI
- Assign identity and least-privilege access through Entra ID
- Apply the same DLP, sensitivity labels, and insider risk policies
- Detect threats and respond in Defender — agents as first-class assets
- Maintain full audit trail using M365 compliance fabric

**Speaker Notes:**
Agent 365 isn't a bolt-on product or a separate console. It extends the Microsoft 365 platform you already operate — Entra for identity, Purview for data protection, Defender for threat detection, and the M365 Admin Center for management. Your agents get the same controls as your employees. No parallel identity stores. No separate evidence chains. No new consoles for your SOC team to learn.

**Visual Suggestion:** Hub-and-spoke diagram with "Agent 365" at center, spokes connecting to M365 Admin Center, Entra ID, Purview, Defender XDR, and M365 Apps (Outlook, Teams, SharePoint). Each spoke labeled with its governance function.

---

### Slide 4: What We'll Prove in 4–6 Weeks

**Title:** Proof of Value — Your Agents, Your Environment, Real Results

**Bullets:**
- 6 use cases covering the full agent governance lifecycle
- Executed against 3+ agents you identify from your environment
- Built on your existing Entra, Purview, and Defender configurations
- Measurable success criteria for every use case
- Clear path from PoV to production rollout

**Speaker Notes:**
This isn't a theoretical exercise. We'll work with agents your teams actually use — or plan to deploy. We'll configure each use case against your existing security and compliance posture, measure success against specific criteria, and at the end you'll have a clear decision framework for broader rollout. Let's look at what each use case covers.

**Visual Suggestion:** Timeline graphic showing 6 numbered milestones across a 4–6 week bar. Each milestone labeled with its use case name. A "Go/No-Go" decision gate at the end.

---

## USE CASE 1 — Agent Inventory and Discovery

---

### Slide UC1-1: Scenario — You Can't Govern What You Can't See

**Title:** Do You Know Every Agent Operating in Your Tenant?

**Bullets:**
- Shadow agents bypass security review and operate without IT awareness
- Without a registry, there's no way to apply policy, revoke access, or audit behavior
- Agent 365 provides a native registry in M365 Admin Center with auto-discovery
- Goal: Zero shadow agents — every agent visible, classified, and accountable

**Speaker Notes:**
Let's start with the most fundamental question: do you actually know how many AI agents are operating in your environment right now? Most organizations can't answer that confidently. Agent 365 provides a built-in registry in the M365 Admin Center that auto-discovers agents — no connectors, no third-party CMDB sync. If it's running in your tenant, you'll see it.

**Visual Suggestion:** Screenshot mockup of the M365 Admin Center showing an "AI Agents" registry blade with a list of discovered agents, their status (registered/unregistered), and owner assignments.

---

### Slide UC1-2: Demo Walkthrough — Discovery in Action

**Title:** Live Demo: Agent Registry and Auto-Discovery

**Bullets:**
- Navigate to Settings → Org settings → Agent management → Agent registry
- Review auto-discovered agents vs. manually registered agents
- Classify an unregistered agent (assign owner, purpose, risk tier)
- Demonstrate real-time discovery of a newly deployed agent
- Show filtering and search across agent inventory

**Speaker Notes:**
In this demo, we'll open the M365 Admin Center and walk through the agent registry. You'll see agents that were auto-discovered alongside those that were manually registered. We'll classify an unregistered agent live, then deploy a test agent and watch it appear in the registry within minutes. Amos will guide you through each click.

**Visual Suggestion:** Annotated screenshot sequence showing the navigation path: Admin Center → AI Agents → Agent List → Agent Detail card with classification fields highlighted.

---

### Slide UC1-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Agent Discovery

**Bullets:**
- 100% of known agents appear in the registry within 24 hours of deployment
- Auto-discovery identifies at least 1 previously unknown agent in your tenant
- Every registered agent has an assigned owner and risk classification
- Zero agents operating outside the registry by end of PoV

**Speaker Notes:**
Success here is binary and measurable. By the end of this use case, every agent in your environment should be visible in the registry. We specifically look for the "aha moment" — when auto-discovery surfaces an agent that IT didn't know about. That's the value of native discovery vs. manual inventory.

**Visual Suggestion:** Scorecard-style graphic with four green checkboxes and the criteria listed beside each. A "0 shadow agents" metric prominently displayed.

---

### Slide UC1-4: Differentiator — Native to M365

**Title:** Unified Registry — Native, Not Bolted On

**Bullets:**
- Built into M365 Admin Center — same console your admins already use daily
- Auto-discovery is native to the platform — no API integrations or third-party scanners
- Agent metadata lives in the same directory as users, groups, and devices
- Competing solutions require separate inventory tools with manual sync

**Speaker Notes:**
The key differentiator here is "native." You're not installing a third-party scanner or building API integrations to populate a CMDB. Agent discovery is built into the same Admin Center your IT team already opens every morning. The agent registry lives in the same directory fabric as your users and devices. This isn't a connector — it's a first-class platform capability.

**Visual Suggestion:** Side-by-side comparison: Left — "Traditional Approach" with multiple disconnected tools and sync arrows; Right — "Agent 365" with a single Admin Center console containing everything. Fewer boxes, fewer arrows, one pane of glass.

---

### Slide UC1-5: Architecture — How Auto-Discovery Works

*(Optional — include for technical audiences)*

**Title:** Under the Hood: Agent Discovery Flow

**Bullets:**
- Agents register via Entra app registration or are detected through M365 API activity
- Discovery engine monitors authentication events, Graph API calls, and resource access
- Newly detected agents surface in registry with "Unclassified" status
- Admins receive alerts for unregistered agent activity
- Full audit trail from first detection through classification

**Speaker Notes:**
Here's how it works technically. The discovery engine monitors your tenant's authentication and API activity. When it detects a non-human identity behaving as an agent — making Graph calls, accessing resources, authenticating with tokens — it surfaces that entity in the registry. Your admins get notified, classify it, and from that point forward it's under governance.

**Visual Suggestion:** Flow diagram: Agent Activity → Detection Engine (monitors auth + API) → Registry Entry → Admin Alert → Classification → Governed State. Arrows show the lifecycle from "unknown" to "managed."

---

## USE CASE 2 — Agent Identity and Least-Privilege

---

### Slide UC2-1: Scenario — Agents Need Identity, Not Just Credentials

**Title:** If Agents Don't Have Identity, They Can't Have Boundaries

**Bullets:**
- Agents today often share service accounts or use over-privileged app registrations
- Without dedicated identity, you can't apply conditional access or audit individually
- Agent 365 gives each agent an Entra Agent ID — same identity fabric as employees
- Enables scoped tokens, conditional access policies, and per-agent sign-in logs

**Speaker Notes:**
Think about how your agents authenticate today. Shared service accounts? Broad app registrations with more permissions than needed? That's the status quo, and it means you can't apply conditional access per agent, can't audit who did what, and can't revoke one agent without affecting others. Agent 365 gives each agent its own Entra identity — same fabric, same policies, same logs as your human users.

**Visual Suggestion:** Before/After comparison — "Before" shows multiple agents sharing one service account key; "After" shows each agent with its own Entra ID card, conditional access shield, and individual audit trail.

---

### Slide UC2-2: Demo Walkthrough — Identity and Access in Practice

**Title:** Live Demo: Entra Agent ID and Conditional Access

**Bullets:**
- Create an Entra Agent ID for a test agent
- Assign scoped permissions using least-privilege principles
- Apply a conditional access policy (e.g., restrict to specific network or resource)
- Trigger agent activity and observe sign-in log entry
- Demonstrate token scoping and permission boundary enforcement

**Speaker Notes:**
In this demo, we'll create a dedicated Entra Agent ID, assign it the minimum permissions needed for its function, and apply a conditional access policy. Then we'll trigger the agent to act, and you'll see its activity appear in the sign-in logs — just like a human user. We'll also show what happens when the agent tries to exceed its permission boundary. Amos walks through the specifics.

**Visual Suggestion:** Split-screen showing Entra ID portal on left (agent identity creation) and sign-in logs on right (agent's authentication event appearing in real time).

---

### Slide UC2-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Agent Identity

**Bullets:**
- Each PoV agent has a dedicated Entra Agent ID (no shared accounts)
- Conditional access policy correctly blocks agent activity outside defined boundaries
- Sign-in logs capture every agent authentication event with full detail
- Token scoping prevents access beyond assigned permissions
- Least-privilege verified: agent cannot access resources outside its scope

**Speaker Notes:**
We'll validate that every agent in the PoV has its own identity, that conditional access actually stops the agent when boundaries are crossed, and that sign-in logs capture full authentication details. The most compelling moment is when we try to have the agent access something outside its scope — and it's blocked. That's least-privilege working as designed.

**Visual Suggestion:** A checklist-style visual with pass/fail indicators. Include a highlighted "blocked" event in a sign-in log screenshot showing the conditional access policy denying an out-of-scope request.

---

### Slide UC2-4: Differentiator — Same Identity Fabric as Employees

**Title:** Why This Matters: No Parallel Identity Store

**Bullets:**
- Agents live in the same Entra ID directory as your employees
- Same conditional access engine — no separate policy framework to maintain
- Sign-in logs are unified — human and agent activity in one view
- No third-party identity broker or agent-specific IAM tool required
- Your identity team already knows how to operate this

**Speaker Notes:**
Here's what separates this from every other approach: there's no parallel identity store. Your agents are in the same directory as your people. Your identity team applies the same conditional access policies with the same tools they use today. Sign-in logs are unified. There's no new IAM console to learn, no separate policy engine to maintain. It's the same fabric — extended to agents.

**Visual Suggestion:** Single Entra ID directory icon containing both human user icons and agent icons side by side — visually demonstrating they live in the same system. Contrast with a competitor approach showing two separate directories connected by a fragile sync arrow.

---

## USE CASE 3 — Sensitive Data Protection

---

### Slide UC3-1: Scenario — Agents Access Data. Data Needs Protection.

**Title:** Your DLP Policies Protect Users — Do They Protect Against Agents?

**Bullets:**
- AI agents process, summarize, and move sensitive data at scale
- Without DLP enforcement, agents can exfiltrate data faster than any insider
- Agent 365 extends Purview DLP and sensitivity labels to agent activities
- Same policies, same audit trail, same eDiscovery — now covering agents too

**Speaker Notes:**
Your Purview DLP policies already protect against users sharing sensitive data inappropriately. But what about your agents? They process documents, summarize emails, move data between systems — all at machine speed. Without explicit DLP coverage, an agent can inadvertently exfiltrate sensitive data faster than any malicious insider. Agent 365 extends the same Purview policies to agent activities.

**Visual Suggestion:** Illustration showing a sensitivity-labeled document being accessed by both a human user and an AI agent — both subject to the same DLP policy shield. A "blocked" indicator on an attempted policy violation.

---

### Slide UC3-2: Demo Walkthrough — DLP for Agents

**Title:** Live Demo: Purview DLP and Sensitivity Labels with Agents

**Bullets:**
- Configure a DLP policy that applies to agent activities (e.g., block external sharing of "Confidential" content)
- Trigger an agent to process a sensitivity-labeled document
- Observe DLP enforcement: agent action blocked or flagged
- Review the audit log entry showing the policy match
- Show insider risk signal generated by agent data handling pattern

**Speaker Notes:**
We'll configure a DLP policy that explicitly covers agent activities, then ask an agent to process a document marked "Confidential." You'll see the policy fire — blocking the agent from sharing that content externally. The audit log captures the event, and if the pattern is anomalous, you'll see an insider risk signal too. Same tools, same evidence. Amos provides the step-by-step.

**Visual Suggestion:** Sequence of annotated screenshots: (1) DLP policy editor showing agent scope, (2) agent attempting to process labeled doc, (3) DLP block notification, (4) audit log entry with policy match details.

---

### Slide UC3-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Data Protection

**Bullets:**
- DLP policy correctly blocks agent from violating data handling rules
- Sensitivity labels are respected by agents — labeled content is not downgraded or stripped
- Audit log captures every agent interaction with sensitive content
- Insider risk signal fires when agent exhibits anomalous data access pattern
- eDiscovery can surface agent-touched content using same search tools

**Speaker Notes:**
Success means your existing DLP rules work identically for agents as they do for users. Sensitivity labels must be respected — an agent can't strip a "Highly Confidential" label to bypass policy. Every interaction is auditable, and your compliance team can use the same eDiscovery tools to find agent-touched content. No new tools, no new evidence chain.

**Visual Suggestion:** Dashboard mockup showing DLP policy matches split by "User-triggered" and "Agent-triggered" with matching enforcement rates. An eDiscovery search result showing agent-accessed documents.

---

### Slide UC3-4: Differentiator — Same Rules, Same Audit, Same eDiscovery

**Title:** Why This Matters: One Policy Framework for Users and Agents

**Bullets:**
- Same Purview DLP rules protect both human users and AI agents
- No separate data classification system for agent-accessed content
- Audit trail feeds the same compliance reports auditors already accept
- eDiscovery searches naturally include agent activity — no separate export
- Competing solutions require duplicate policy sets with manual reconciliation

**Speaker Notes:**
The differentiator is unification. You don't write one set of DLP rules for users and another for agents. You don't maintain a separate audit trail that auditors have to learn to trust. Your existing compliance reports naturally include agent activity. When your legal team runs eDiscovery, agent-touched content appears alongside user-touched content. One policy framework. One evidence chain.

**Visual Suggestion:** Venn diagram showing "User DLP Policies" and "Agent DLP Policies" as a single overlapping circle (they're the same). Contrast with competitor approach showing two separate circles requiring a "sync" mechanism.

---

## USE CASE 4 — Threat Detection and Response

---

### Slide UC4-1: Scenario — Agents Can Be Compromised. Are You Watching?

**Title:** Your SOC Monitors Users and Endpoints — Who's Monitoring Agents?

**Bullets:**
- Compromised agents can be weaponized for lateral movement, data theft, or privilege escalation
- Agent-specific attack patterns (prompt injection, token theft, scope creep) need dedicated detection
- Agent 365 makes agents first-class Defender XDR assets with runtime protection
- Same SOC console, same alert queue, same incident response playbooks

**Speaker Notes:**
Let's talk about threat detection. Your SOC monitors users and endpoints around the clock. But what about agents? A compromised agent with broad permissions is an attacker's dream — it can move laterally, access sensitive data, and escalate privileges, all at machine speed and without triggering user-based detections. Agent 365 brings agents into Defender XDR as first-class assets.

**Visual Suggestion:** Defender XDR console screenshot showing an agent-related alert in the incident queue alongside user alerts — demonstrating unified SOC visibility. An attack-path visualization showing agent → compromised resource → lateral movement.

---

### Slide UC4-2: Demo Walkthrough — Defender for Agents

**Title:** Live Demo: Threat Detection and Attack-Path Visualization

**Bullets:**
- View agent assets in Defender XDR console
- Trigger a simulated anomalous agent behavior (e.g., unusual resource access pattern)
- Observe alert generation in real time
- Walk through attack-path visualization showing potential blast radius
- Demonstrate SOC response: isolate agent, revoke tokens, investigate timeline

**Speaker Notes:**
In this demo, we'll show your agents appearing as managed assets in the Defender console. Then we'll simulate anomalous behavior — an agent accessing resources outside its normal pattern. You'll see the alert fire, the attack-path visualization showing potential blast radius, and the SOC response workflow: isolate, revoke, investigate. All in the same console your SOC team already uses. Amos guides the walkthrough.

**Visual Suggestion:** Three-panel sequence: (1) Agent listed in Defender asset inventory, (2) Alert firing with severity and attack-path diagram, (3) Response action panel showing "Isolate Agent" and "Revoke Tokens" buttons.

---

### Slide UC4-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Threat Detection

**Bullets:**
- Defender generates alert within defined SLA for anomalous agent behavior
- Attack-path visualization accurately shows agent's potential blast radius
- SOC can isolate a compromised agent and revoke tokens from the same console
- Runtime protection prevents agent from executing blocked actions
- Incident timeline includes full agent activity history for forensics

**Speaker Notes:**
We'll measure detection time, accuracy of the attack-path visualization, and the SOC's ability to respond from a single console. The key validation is end-to-end: anomalous behavior → alert → visualization → response → containment. If your SOC can do this without switching tools or learning a new console, we've proven the value.

**Visual Suggestion:** Timeline graphic showing: Anomalous Event → Detection (with SLA clock) → Alert → Investigation → Response → Containment. Each stage with a measurable metric.

---

### Slide UC4-4: Differentiator — Agents as First-Class Defender Assets

**Title:** Why This Matters: One Console, One Incident Queue

**Bullets:**
- Agents appear alongside users, devices, and apps in Defender XDR
- No separate SIEM integration or custom detection rules needed
- Attack-path analysis natively understands agent permissions and access patterns
- SOC response actions (isolate, revoke, block) work identically for agents
- Competing solutions require separate agent monitoring tools with manual SIEM forwarding

**Speaker Notes:**
The differentiator is "first-class." Agents aren't bolted onto Defender as a custom data source — they're native assets. Your SOC sees them in the same queue, investigates them with the same tools, and responds with the same actions. Attack-path analysis natively understands agent permissions. No custom SIEM rules. No separate monitoring tool feeding alerts into your existing workflow.

**Visual Suggestion:** Unified Defender XDR dashboard showing mixed asset types: users, endpoints, applications, and agents — all in one view with consistent alert severity indicators and response actions.

---

## USE CASE 5 — Audit, Compliance, and Lifecycle

---

### Slide UC5-1: Scenario — Auditors Will Ask About Your Agents

**Title:** When Auditors Come Knocking, Can You Show the Agent Evidence Chain?

**Bullets:**
- Regulatory frameworks increasingly expect governance over autonomous AI systems
- Auditors need a complete trail: who deployed it, what it accessed, when it was deactivated
- Agent 365 provides full lifecycle audit through M365 compliance fabric
- Same evidence format auditors already accept for user activities

**Speaker Notes:**
Here's a scenario playing out right now: your compliance team passes an audit, but the auditor asks, "What about your AI agents? Who governs them? Where's the evidence?" If you can't answer that in the same compliance framework they already trust, you have a finding. Agent 365 ensures agent activities feed the same audit trail, in the same format, through the same compliance fabric.

**Visual Suggestion:** Auditor persona icon reviewing a compliance report that includes both user and agent activities in a unified format. A "complete evidence chain" graphic showing deployment → operation → deactivation with audit entries at each stage.

---

### Slide UC5-2: Demo Walkthrough — Lifecycle and Compliance in Practice

**Title:** Live Demo: Full Audit Trail and Lifecycle Management

**Bullets:**
- Review complete audit trail for an agent (deployment through operation)
- Execute lifecycle drill: block agent, deactivate agent, delete agent
- Verify each lifecycle action generates audit entry with timestamp and actor
- Show data retention policy applying to agent audit records
- Demonstrate compliance report including agent activities

**Speaker Notes:**
We'll walk through the full lifecycle of an agent in audit terms. You'll see the trail from deployment through every action it took. Then we'll execute a lifecycle drill — blocking the agent, deactivating it, and finally deleting it — verifying that each action is audited with full detail. We'll also show that your data retention policies apply to agent records. Amos takes you through each step.

**Visual Suggestion:** Lifecycle state diagram showing: Deployed → Active → Blocked → Deactivated → Deleted, with audit log entries appearing at each transition. Timestamps and actor information visible.

---

### Slide UC5-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Audit and Compliance

**Bullets:**
- Complete audit trail exists from agent deployment through deletion
- Each lifecycle state change (block/deactivate/delete) generates a timestamped audit entry
- Data retention policies correctly apply to agent audit records
- Compliance report export includes agent activities in accepted format
- No gaps in evidence chain — auditor can reconstruct full agent history

**Speaker Notes:**
Success here means an auditor can pick up the compliance report, see agent activities alongside user activities, and trace any agent's full history from deployment to deletion. Every lifecycle action is timestamped and attributed. Data retention applies correctly. The evidence chain has no gaps. If your compliance team says "this is audit-ready," we've succeeded.

**Visual Suggestion:** Mock compliance report page showing agent activities in standard audit format. A "gap analysis" showing zero missing evidence for agent lifecycle events.

---

### Slide UC5-4: Differentiator — Compliance Fabric Auditors Already Trust

**Title:** Why This Matters: No Parallel Evidence Chain

**Bullets:**
- Agent audit data feeds the same M365 compliance fabric used for users
- Auditors already accept this format — no new validation required
- Data retention, legal hold, and eDiscovery apply uniformly
- No separate compliance tool generating evidence that auditors must learn to trust
- Competing solutions create a second evidence chain requiring separate attestation

**Speaker Notes:**
The power here is trust. Your auditors already accept evidence from M365 compliance tools. Agent activities feed that same system — same format, same retention, same legal hold capabilities. You're not asking your auditors to validate a new evidence source. You're showing them agent governance in a framework they already approved. Competitors create parallel evidence chains that require separate attestation.

**Visual Suggestion:** Single compliance "stamp of approval" covering both user and agent evidence. Contrast with competitor approach showing two separate stamps — one for users (accepted) and one for agents (pending validation).

---

### Slide UC5-5: Architecture — Audit and Lifecycle Flow

*(Optional — include for technical audiences)*

**Title:** Under the Hood: How Agent Lifecycle Feeds Compliance

**Bullets:**
- Every agent action generates a unified audit log entry (same schema as user events)
- Lifecycle state changes trigger compliance workflow notifications
- Retention labels auto-apply to agent audit records based on classification
- eDiscovery index includes agent-generated content and interactions
- Export APIs produce audit packages in standard regulatory formats

**Speaker Notes:**
Technically, every agent action writes to the same unified audit log as user actions — same schema, same retention handling. When an agent changes lifecycle state, compliance workflows fire automatically. Retention labels apply based on the agent's classification. And when legal or compliance needs to pull records, eDiscovery searches naturally include agent content.

**Visual Suggestion:** Architecture flow: Agent Actions → Unified Audit Log → Retention Labels Auto-Applied → Compliance Reports / eDiscovery Index / Legal Hold. All flowing through the same M365 compliance pipeline.

---

## USE CASE 6 — Productivity Integration

---

### Slide UC6-1: Scenario — Agents Work Where Your People Work

**Title:** Agents in Outlook, Teams, Word, and SharePoint — Governed or Ungoverned?

**Bullets:**
- AI agents increasingly operate within productivity tools — drafting emails, posting in Teams, editing documents
- Without governance, these agents act with unbounded access across your collaboration surface
- Agent 365 enables governed connections with real-time allow/block enforcement
- Same productivity surface users know — no separate agent UI or plug-in

**Speaker Notes:**
Your users work in Outlook, Teams, Word, and SharePoint. Increasingly, so do AI agents — drafting responses, summarizing threads, editing documents, posting updates. The question is: are those agents operating under the same governance as your people? Agent 365 ensures agents in productivity tools follow the same rules, with real-time allow/block enforcement. No separate agent interface needed.

**Visual Suggestion:** M365 app icons (Outlook, Teams, Word, SharePoint) with both human user and agent avatars operating within them. A governance "shield" overlay showing real-time policy enforcement.

---

### Slide UC6-2: Demo Walkthrough — Governed Productivity Connections

**Title:** Live Demo: Allow/Block Enforcement in Real Time

**Bullets:**
- Block an entire connection (e.g., "Block Outlook Calendar connection")
- Demonstrate that the blocked connection prevents all agent access
- Show enforcement in real time
- Review audit trail capturing the blocked connection attempt
- Apply connection-level blocking across multiple M365 apps to demonstrate simplicity

**Speaker Notes:**
We'll apply connection-level blocking by disabling specific connections for an agent — for example, blocking the Outlook Calendar connection entirely. This approach is simpler and more dramatic for demos than granular action-level permissions. We'll trigger the agent to attempt access through the blocked connection, watch it get denied in real time, and see the block recorded in the audit trail. Amos will walk through each step of the live demo.

**Visual Suggestion:** Two-column demo flow: Left column shows "Allowed" actions succeeding (green checkmarks); Right column shows "Blocked" actions being denied (red X marks). Both columns feed into a unified audit log at the bottom.

---

### Slide UC6-3: Success Criteria — Measurable Outcomes

**Title:** How We Measure Success for Productivity Integration

**Bullets:**
- Agent successfully operates within allowed boundaries in Outlook, Teams, Word, and/or SharePoint
- Blocked actions are denied in real time (sub-second enforcement)
- Allow/block policies can be changed and take effect without redeploying the agent
- Audit trail captures both allowed and blocked actions with full context
- End users experience no disruption — governance is invisible to them

**Speaker Notes:**
We need to prove three things: allowed actions work smoothly, blocked actions are denied instantly, and policy changes take effect without requiring agent redeployment. The user experience is critical too — governance should be invisible to end users. They shouldn't know whether a human or a governed agent performed the action.

**Visual Suggestion:** Performance metric showing enforcement latency (sub-second). A user experience satisfaction indicator showing "no disruption." Policy change → enforcement timeline showing immediate effect.

---

### Slide UC6-4: Differentiator — Same Productivity Surface, No Plug-Ins

**Title:** Why This Matters: No Separate Agent UI

**Bullets:**
- Agents operate natively within M365 apps — no separate interface for users to learn
- Governance is platform-level — not a per-app plug-in that can be bypassed
- Allow/block enforcement is real-time and centrally managed
- Users interact with agent output in the apps they already use daily
- Competing solutions require browser extensions, sidebars, or standalone agent portals

**Speaker Notes:**
The differentiator is seamlessness. Your users don't need a new app, a browser extension, or a sidebar to interact with governed agents. Agents operate natively within Outlook, Teams, Word, and SharePoint. Governance is enforced at the platform level — it can't be bypassed by a clever plug-in configuration. And policy changes are centralized, not scattered across per-app settings.

**Visual Suggestion:** Clean M365 app interface showing agent activity happening naturally within the familiar UI — no extra toolbars, sidebars, or pop-ups. Contrast with competitor approach showing a cluttered interface with separate agent panels and browser extensions.

---

## CLOSING SECTION

---

### Slide C-1: Summary — Six Proofs of Value

**Title:** What We Proved: Agent Governance That Works Today

**Bullets:**
- ✅ UC1: Every agent discovered and registered — zero shadow agents
- ✅ UC2: Dedicated identity with least-privilege — same fabric as employees
- ✅ UC3: DLP and sensitivity labels enforced — same policies as users
- ✅ UC4: Threat detection and response — agents as first-class Defender assets
- ✅ UC5: Full audit trail — compliance fabric auditors already trust
- ✅ UC6: Governed productivity integration — real-time allow/block, no plug-ins

**Speaker Notes:**
Let's bring it all together. Over these weeks, we proved that Agent 365 delivers real, measurable governance across every dimension: visibility, identity, data protection, threat detection, compliance, and productivity. And we did it using the tools and frameworks your teams already operate. No new consoles, no parallel systems, no learning curve.

**Visual Suggestion:** Six-panel scorecard with each use case showing a green "Proven" status, the key metric achieved, and the differentiator in a single line. Clean, executive-summary style.

---

### Slide C-2: Next Steps — From PoV to Production

**Title:** Broader Rollout: Extending Agent Governance Across Your Organization

**Bullets:**
- Expand from 3+ PoV agents to full agent estate
- Integrate agent governance into existing change management processes
- Align agent lifecycle policies with your compliance calendar
- Enable self-service agent registration with guardrails for development teams
- Establish ongoing monitoring cadence with SOC team

**Speaker Notes:**
The PoV proved the technology works with your agents in your environment. The next step is broader rollout — extending governance to your full agent estate, integrating with change management, and enabling self-service registration so development teams can deploy agents responsibly. We'll work with you to build a rollout plan that matches your organizational readiness.

**Visual Suggestion:** Expanding circles graphic: Inner circle = "PoV (3+ agents)" → Middle circle = "Phase 1 (department rollout)" → Outer circle = "Full estate governance." Timeline and milestones labeled on each ring.

---

### Slide C-3: Resources and Contact

**Title:** Let's Keep the Conversation Going

**Bullets:**
- Your Microsoft account team: [Account Team Contacts]
- Agent 365 documentation: [Link to docs]
- PoV completion report: [Will be delivered at engagement close]
- FastTrack support for production deployment: [Link/contact]
- Community and feedback: [Tech Community link]

**Speaker Notes:**
Thank you for your time and partnership throughout this Proof of Value. Your account team is here to support next steps — whether that's a broader rollout plan, FastTrack engagement, or connecting you with engineering for specific scenarios. We'll deliver the formal PoV completion report within one week of engagement close. Let's govern your agents the way you govern your people.

**Visual Suggestion:** Clean contact card layout with Microsoft branding. QR code linking to Agent 365 documentation. Account team photos/names in a professional grid layout.

---

*End of slide content. Last updated: 2026-05-05.*
