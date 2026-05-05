from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# === COLOR PALETTE ===
MS_BLUE = RGBColor(0x00, 0x78, 0xD4)
DARK_NAVY = RGBColor(0x00, 0x20, 0x50)
TEAL_ACCENT = RGBColor(0x00, 0xBC, 0xF2)
LIGHT_GRAY_BG = RGBColor(0xF5, 0xF5, 0xF5)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
MID_GRAY = RGBColor(0x6E, 0x6E, 0x6E)
FOOTER_GRAY = RGBColor(0x99, 0x99, 0x99)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BULLET_BLUE = RGBColor(0x00, 0x5A, 0x9E)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# === GRADIENT HELPER ===
def set_gradient_fill(shape, color1, color2, angle=0):
    """Apply a two-stop linear gradient fill to a shape."""
    spPr = shape._element.spPr
    # Remove existing fill
    for child in list(spPr):
        if child.tag.endswith('}solidFill') or child.tag.endswith('}gradFill') or child.tag.endswith('}noFill'):
            spPr.remove(child)
    gradFill = spPr.makeelement(qn('a:gradFill'), {})
    gsLst = gradFill.makeelement(qn('a:gsLst'), {})
    # Stop 1
    gs1 = gsLst.makeelement(qn('a:gs'), {'pos': '0'})
    srgb1 = gs1.makeelement(qn('a:srgbClr'), {'val': '%02X%02X%02X' % (color1[0], color1[1], color1[2])})
    gs1.append(srgb1)
    gsLst.append(gs1)
    # Stop 2
    gs2 = gsLst.makeelement(qn('a:gs'), {'pos': '100000'})
    srgb2 = gs2.makeelement(qn('a:srgbClr'), {'val': '%02X%02X%02X' % (color2[0], color2[1], color2[2])})
    gs2.append(srgb2)
    gsLst.append(gs2)
    gradFill.append(gsLst)
    lin = gradFill.makeelement(qn('a:lin'), {'ang': str(angle * 60000), 'scaled': '1'})
    gradFill.append(lin)
    spPr.append(gradFill)

def no_line(shape):
    shape.line.fill.background()

# === FOOTER ===
def add_footer(slide):
    """Add subtle footer text to bottom of slide."""
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(4), Inches(0.4))
    tf = footer_box.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.text = 'Agent 365  |  Proof of Value'
    p.font.size = Pt(9)
    p.font.color.rgb = FOOTER_GRAY
    p.font.name = 'Segoe UI Light'
    p.alignment = PP_ALIGN.LEFT

# === NOTES ===
def add_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

# === CONTENT SLIDE (REDESIGNED) ===
def add_title_bar(slide, title_text):
    """85% width title band with rounded feel, positioned with left margin."""
    bar_width = Inches(11.333)  # ~85% of slide width
    bar = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(0.45),
        bar_width, Inches(1.1)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = MS_BLUE
    no_line(bar)
    # Minimal corner rounding
    bar.adjustments[0] = 0.04
    tf = bar.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.5)
    tf.margin_right = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(24)
    p.font.color.rgb = WHITE
    p.font.name = 'Segoe UI Semibold'
    p.font.bold = True
    p.alignment = PP_ALIGN.LEFT

def add_accent_line(slide):
    """Thin teal accent line below the title bar."""
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.65),
        Inches(2.5), Inches(0.04)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = TEAL_ACCENT
    no_line(line)

def add_bullets(slide, bullets):
    """Styled bullets with visual hierarchy - em-dash markers, proper spacing."""
    left_margin = Inches(1.2)
    top = Inches(2.0)
    txBox = slide.shapes.add_textbox(left_margin, top, Inches(10.5), Inches(4.8))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        # Use em-dash bullet marker for visual distinction
        p.text = '\u2014  ' + bullet
        p.font.size = Pt(16)
        p.font.color.rgb = DARK_GRAY
        p.font.name = 'Segoe UI'
        p.space_after = Pt(16)
        p.space_before = Pt(4)
        # Indent formatting
        p.level = 0
        pPr = p._p.get_or_add_pPr()
        pPr.set('marL', str(int(Inches(0.3))))
        pPr.set('indent', str(int(Inches(-0.3))))

def add_slide_bg(slide):
    """Add subtle light gray background."""
    bg_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), SLIDE_W, SLIDE_H
    )
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = LIGHT_GRAY_BG
    no_line(bg_shape)
    # Send to back
    sp = bg_shape._element
    sp.getparent().remove(sp)
    slide.shapes._spTree.insert(2, sp)

def content_slide(title, bullets, notes=''):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_slide_bg(slide)
    add_title_bar(slide, title)
    add_accent_line(slide)
    add_bullets(slide, bullets)
    add_footer(slide)
    if notes:
        add_notes(slide, notes)
    return slide

# === SECTION DIVIDER (REDESIGNED) ===
def section_divider(title, subtitle=''):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Full-slide gradient background (dark navy to MS blue)
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), SLIDE_W, SLIDE_H
    )
    no_line(bg)
    set_gradient_fill(bg, (0x00, 0x20, 0x50), (0x00, 0x78, 0xD4), angle=135)

    # Geometric accent — subtle diamond shape, semi-transparent feel
    accent = slide.shapes.add_shape(
        MSO_SHAPE.DIAMOND, Inches(9.5), Inches(0.5), Inches(3.0), Inches(3.0)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = RGBColor(0x00, 0x5A, 0x9E)
    no_line(accent)
    # Set transparency via alpha
    solidFill = accent._element.spPr.find(qn('a:solidFill'))
    if solidFill is not None:
        srgbClr = solidFill.find(qn('a:srgbClr'))
        if srgbClr is not None:
            alpha = srgbClr.makeelement(qn('a:alpha'), {'val': '25000'})
            srgbClr.append(alpha)

    # Second geometric accent — bottom left
    accent2 = slide.shapes.add_shape(
        MSO_SHAPE.DIAMOND, Inches(0.5), Inches(4.5), Inches(2.5), Inches(2.5)
    )
    accent2.fill.solid()
    accent2.fill.fore_color.rgb = TEAL_ACCENT
    no_line(accent2)
    solidFill2 = accent2._element.spPr.find(qn('a:solidFill'))
    if solidFill2 is not None:
        srgbClr2 = solidFill2.find(qn('a:srgbClr'))
        if srgbClr2 is not None:
            alpha2 = srgbClr2.makeelement(qn('a:alpha'), {'val': '15000'})
            srgbClr2.append(alpha2)

    # Title text centered
    title_box = slide.shapes.add_textbox(Inches(2), Inches(2.5), Inches(9.333), Inches(2.0))
    tf = title_box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.color.rgb = WHITE
    p.font.name = 'Segoe UI Light'
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(22)
        p2.font.color.rgb = TEAL_ACCENT
        p2.font.name = 'Segoe UI'
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(12)

    # Thin horizontal accent line
    divider_line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(5.5), Inches(4.7), Inches(2.333), Inches(0.04)
    )
    divider_line.fill.solid()
    divider_line.fill.fore_color.rgb = TEAL_ACCENT
    no_line(divider_line)

    return slide

def hide_slide(slide):
    slide._element.set('show', '0')

# === TITLE SLIDE ===
slide = prs.slides.add_slide(prs.slide_layouts[6])
# Gradient background
bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), SLIDE_W, SLIDE_H)
no_line(bg)
set_gradient_fill(bg, (0x00, 0x20, 0x50), (0x00, 0x78, 0xD4), angle=120)

# Large geometric accent - top right
accent_tr = slide.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(9.0), Inches(-1.0), Inches(5.0), Inches(5.0))
accent_tr.fill.solid()
accent_tr.fill.fore_color.rgb = RGBColor(0x00, 0x5A, 0x9E)
no_line(accent_tr)
solidFill = accent_tr._element.spPr.find(qn('a:solidFill'))
if solidFill is not None:
    srgbClr = solidFill.find(qn('a:srgbClr'))
    if srgbClr is not None:
        alpha = srgbClr.makeelement(qn('a:alpha'), {'val': '20000'})
        srgbClr.append(alpha)

# Small accent - bottom left
accent_bl = slide.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(-0.5), Inches(5.5), Inches(3.0), Inches(3.0))
accent_bl.fill.solid()
accent_bl.fill.fore_color.rgb = TEAL_ACCENT
no_line(accent_bl)
solidFill2 = accent_bl._element.spPr.find(qn('a:solidFill'))
if solidFill2 is not None:
    srgbClr2 = solidFill2.find(qn('a:srgbClr'))
    if srgbClr2 is not None:
        alpha2 = srgbClr2.makeelement(qn('a:alpha'), {'val': '12000'})
        srgbClr2.append(alpha2)

# Title text block
title_box = slide.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(9.0), Inches(4.0))
tf = title_box.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
# Main title
p = tf.paragraphs[0]
p.text = 'Agent 365'
p.font.size = Pt(52)
p.font.color.rgb = WHITE
p.font.name = 'Segoe UI Light'
p.font.bold = True
p.alignment = PP_ALIGN.LEFT
# Subtitle
p2 = tf.add_paragraph()
p2.text = 'Proof of Value'
p2.font.size = Pt(36)
p2.font.color.rgb = TEAL_ACCENT
p2.font.name = 'Segoe UI'
p2.font.bold = False
p2.alignment = PP_ALIGN.LEFT
p2.space_before = Pt(4)
# Spacer
p3 = tf.add_paragraph()
p3.text = ''
p3.space_before = Pt(20)
# Tagline
p4 = tf.add_paragraph()
p4.text = 'Govern AI Agents with the Controls You Already Trust'
p4.font.size = Pt(16)
p4.font.color.rgb = WHITE
p4.font.name = 'Segoe UI'
p4.alignment = PP_ALIGN.LEFT
p4.space_before = Pt(8)
# Customer/date line
p5 = tf.add_paragraph()
p5.text = '[Customer Name]  \u00b7  [Date]  \u00b7  4\u20136 Week Engagement'
p5.font.size = Pt(13)
p5.font.color.rgb = RGBColor(0xB0, 0xD0, 0xF0)
p5.font.name = 'Segoe UI'
p5.alignment = PP_ALIGN.LEFT
p5.space_before = Pt(12)

# Thin accent bar
accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(4.55), Inches(3.0), Inches(0.04))
accent_bar.fill.solid()
accent_bar.fill.fore_color.rgb = TEAL_ACCENT
no_line(accent_bar)

add_notes(slide, 'Welcome everyone. Today we\'re kicking off the Agent 365 Proof of Value \u2014 a focused engagement designed to show you how Microsoft brings AI agents under the same governance controls you already rely on for your people. Over the next 4 to 6 weeks, we\'ll prove this with your real agents, in your real environment.')

# === SLIDE 2 ===
content_slide('AI Agents Are Growing \u2014 Governance Isn\'t Keeping Up',
    ['Organizations are deploying 10\u201350+ AI agents across departments \u2014 often without IT visibility',
     'Shadow agents create blind spots in identity, data protection, and compliance',
     'Traditional tools weren\'t built for non-human actors operating at machine speed',
     'The gap between agent adoption and agent governance widens every quarter'],
    'Here\'s the challenge: your teams are already building and adopting AI agents. But most governance tooling was designed for human users. Agents don\'t fit that mold natively. The result is shadow agents, ungoverned data access, and compliance gaps that auditors will eventually find. This is the problem Agent 365 was built to solve.')

# === SLIDE 3 ===
content_slide('One Platform. Same Controls. Now for Agents.',
    ['Discover and register every agent \u2014 eliminate shadow AI',
     'Assign identity and least-privilege access through Entra ID',
     'Apply the same DLP, sensitivity labels, and insider risk policies',
     'Detect threats and respond in Defender \u2014 agents as first-class assets',
     'Maintain full audit trail using M365 compliance fabric'],
    'Agent 365 isn\'t a bolt-on product or a separate console. It extends the Microsoft 365 platform you already operate \u2014 Entra for identity, Purview for data protection, Defender for threat detection, and the M365 Admin Center for management. Your agents get the same controls as your employees.')

# === SLIDE 4 ===
content_slide('Proof of Value \u2014 Your Agents, Your Environment, Real Results',
    ['6 use cases covering the full agent governance lifecycle',
     'Executed against 3+ agents you identify from your environment',
     'Built on your existing Entra, Purview, and Defender configurations',
     'Measurable success criteria for every use case',
     'Clear path from PoV to production rollout'],
    'This isn\'t a theoretical exercise. We\'ll work with agents your teams actually use \u2014 or plan to deploy. We\'ll configure each use case against your existing security and compliance posture, measure success against specific criteria, and at the end you\'ll have a clear decision framework for broader rollout.')

# === UC1 ===
section_divider('Use Case 1', 'Agent Inventory and Discovery')

content_slide('Do You Know Every Agent Operating in Your Tenant?',
    ['Shadow agents bypass security review and operate without IT awareness',
     'Without a registry, there\'s no way to apply policy, revoke access, or audit behavior',
     'Agent 365 provides a native registry in M365 Admin Center with auto-discovery',
     'Goal: Zero shadow agents \u2014 every agent visible, classified, and accountable'],
    'Let\'s start with the most fundamental question: do you actually know how many AI agents are operating in your environment right now? Most organizations can\'t answer that confidently. Agent 365 provides a built-in registry in the M365 Admin Center that auto-discovers agents \u2014 no connectors, no third-party CMDB sync.')

content_slide('Live Demo: Agent Registry and Auto-Discovery',
    ['Navigate to Settings \u2192 Org settings \u2192 Agent management \u2192 Agent registry',
     'Review auto-discovered agents vs. manually registered agents',
     'Classify an unregistered agent (assign owner, purpose, risk tier)',
     'Demonstrate real-time discovery of a newly deployed agent',
     'Show filtering and search across agent inventory'],
    'In this demo, we\'ll open the M365 Admin Center and walk through the agent registry. You\'ll see agents that were auto-discovered alongside those that were manually registered. We\'ll classify an unregistered agent live, then deploy a test agent and watch it appear in the registry within minutes.\n\nDetailed procedure: demo-steps.md, UC1')

content_slide('How We Measure Success for Agent Discovery',
    ['100% of known agents appear in the registry within 24 hours of deployment',
     'Auto-discovery identifies at least 1 previously unknown agent in your tenant',
     'Every registered agent has an assigned owner and risk classification',
     'Zero agents operating outside the registry by end of PoV'],
    'Success here is binary and measurable. By the end of this use case, every agent in your environment should be visible in the registry. We specifically look for the "aha moment" \u2014 when auto-discovery surfaces an agent that IT didn\'t know about.')

content_slide('Unified Registry \u2014 Native, Not Bolted On',
    ['Built into M365 Admin Center \u2014 same console your admins already use daily',
     'Auto-discovery is native to the platform \u2014 no API integrations or third-party scanners',
     'Agent metadata lives in the same directory as users, groups, and devices',
     'Competing solutions require separate inventory tools with manual sync'],
    'The key differentiator here is "native." You\'re not installing a third-party scanner or building API integrations to populate a CMDB. Agent discovery is built into the same Admin Center your IT team already opens every morning.\n\nCISO Talking Points:\n- "We eliminate shadow agent risk at the platform layer \u2014 agents are registered as they\'re created, not after they\'re discovered."\n- "The registry is authoritative. It doesn\'t depend on network scanning or API polling that can miss ephemeral agents."\n- "Visibility is the prerequisite for governance. Native inventory means governance starts at creation."\n\nCIO Talking Points:\n- "No new procurement for agent discovery tooling \u2014 it\'s included in your existing M365 licensing."\n- "Your IT ops team doesn\'t learn a new console."\n- "Automatic coverage means no integration project to scope, fund, or maintain."\n\nIf asked about CMDB: CMDBs track what you tell them to track. Native registry captures agents at creation \u2014 before anyone has to remember to register them.\nIf asked about non-Microsoft agents: Third-party agents can be registered via API or admin onboarding. Microsoft-platform agents require zero effort.')

# UC1-5 HIDDEN
s = content_slide('Under the Hood: Agent Discovery Flow',
    ['Agents register via Entra app registration or are detected through M365 API activity',
     'Discovery engine monitors authentication events, Graph API calls, and resource access',
     'Newly detected agents surface in registry with "Unclassified" status',
     'Admins receive alerts for unregistered agent activity',
     'Full audit trail from first detection through classification'],
    'Here\'s how it works technically. The discovery engine monitors your tenant\'s authentication and API activity. When it detects a non-human identity behaving as an agent, it surfaces that entity in the registry. Your admins get notified, classify it, and from that point forward it\'s under governance.')
hide_slide(s)

# === UC2 ===
section_divider('Use Case 2', 'Agent Identity and Least-Privilege Access')

content_slide('If Agents Don\'t Have Identity, They Can\'t Have Boundaries',
    ['Agents today often share service accounts or use over-privileged app registrations',
     'Without dedicated identity, you can\'t apply conditional access or audit individually',
     'Agent 365 gives each agent an Entra Agent ID \u2014 same identity fabric as employees',
     'Enables scoped tokens, conditional access policies, and per-agent sign-in logs'],
    'Think about how your agents authenticate today. Shared service accounts? Broad app registrations with more permissions than needed? Agent 365 gives each agent its own Entra identity \u2014 same fabric, same policies, same logs as your human users.')

content_slide('Live Demo: Entra Agent ID and Conditional Access',
    ['Create an Entra Agent ID for a test agent',
     'Assign scoped permissions using least-privilege principles',
     'Apply a conditional access policy (e.g., restrict to specific network or resource)',
     'Trigger agent activity and observe sign-in log entry',
     'Demonstrate token scoping and permission boundary enforcement'],
    'In this demo, we\'ll create a dedicated Entra Agent ID, assign it the minimum permissions needed for its function, and apply a conditional access policy. Then we\'ll trigger the agent to act, and you\'ll see its activity appear in the sign-in logs.\n\nDetailed procedure: demo-steps.md, UC2')

content_slide('How We Measure Success for Agent Identity',
    ['Each PoV agent has a dedicated Entra Agent ID (no shared accounts)',
     'Conditional access policy correctly blocks agent activity outside defined boundaries',
     'Sign-in logs capture every agent authentication event with full detail',
     'Token scoping prevents access beyond assigned permissions',
     'Least-privilege verified: agent cannot access resources outside its scope'],
    'We\'ll validate that every agent in the PoV has its own identity, that conditional access actually stops the agent when boundaries are crossed, and that sign-in logs capture full authentication details.')

content_slide('Why This Matters: No Parallel Identity Store',
    ['Agents live in the same Entra ID directory as your employees',
     'Same conditional access engine \u2014 no separate policy framework to maintain',
     'Sign-in logs are unified \u2014 human and agent activity in one view',
     'No third-party identity broker or agent-specific IAM tool required',
     'Your identity team already knows how to operate this'],
    'Here\'s what separates this from every other approach: there\'s no parallel identity store. Your agents are in the same directory as your people.\n\nCISO Talking Points:\n- "Agents get identities in the same Entra ID tenant your workforce uses. Conditional access, PIM, and access reviews apply without modification."\n- "Least-privilege for agents isn\'t a new initiative \u2014 it\'s an extension of the initiative you\'re already running for human identities."\n- "Workload identities for agents support the same zero-trust principles."\n\nCIO Talking Points:\n- "Zero new identity infrastructure to procure, deploy, or staff."\n- "Your IAM team\'s existing skills apply directly. No retraining, no new vendor certification."\n- "Access reviews for agents use the same workflow your managers already complete."\n\nIf asked "Agents aren\'t users": They\'re workload identities \u2014 a purpose-built identity type in Entra ID for non-human entities.\nIf asked about high-privilege agents: Same answer as for human admins: PIM with just-in-time elevation, time-bound access, and approval workflows.')

# === UC3 ===
section_divider('Use Case 3', 'Sensitive Data Protection')

content_slide('Your DLP Policies Protect Users \u2014 Do They Protect Against Agents?',
    ['AI agents process, summarize, and move sensitive data at scale',
     'Without DLP enforcement, agents can exfiltrate data faster than any insider',
     'Agent 365 extends Purview DLP and sensitivity labels to agent activities',
     'Same policies, same audit trail, same eDiscovery \u2014 now covering agents too'],
    'Your Purview DLP policies already protect against users sharing sensitive data inappropriately. But what about your agents? They process documents, summarize emails, move data between systems \u2014 all at machine speed. Agent 365 extends the same Purview policies to agent activities.')

content_slide('Live Demo: Purview DLP and Sensitivity Labels with Agents',
    ['Configure a DLP policy that applies to agent activities',
     'Trigger an agent to process a sensitivity-labeled document',
     'Observe DLP enforcement: agent action blocked or flagged',
     'Review the audit log entry showing the policy match',
     'Show insider risk signal generated by agent data handling pattern'],
    'We\'ll configure a DLP policy that explicitly covers agent activities, then ask an agent to process a document marked "Confidential." You\'ll see the policy fire \u2014 blocking the agent from sharing that content externally.\n\nDetailed procedure: demo-steps.md, UC3')

content_slide('How We Measure Success for Data Protection',
    ['DLP policy correctly blocks agent from violating data handling rules',
     'Sensitivity labels are respected by agents \u2014 labeled content is not downgraded or stripped',
     'Audit log captures every agent interaction with sensitive content',
     'Insider risk signal fires when agent exhibits anomalous data access pattern',
     'eDiscovery can surface agent-touched content using same search tools'],
    'Success means your existing DLP rules work identically for agents as they do for users. Sensitivity labels must be respected. Every interaction is auditable, and your compliance team can use the same eDiscovery tools.')

content_slide('Why This Matters: One Policy Framework for Users and Agents',
    ['Same Purview DLP rules protect both human users and AI agents',
     'No separate data classification system for agent-accessed content',
     'Audit trail feeds the same compliance reports auditors already accept',
     'eDiscovery searches naturally include agent activity \u2014 no separate export',
     'Competing solutions require duplicate policy sets with manual reconciliation'],
    'The differentiator is unification. You don\'t write one set of DLP rules for users and another for agents.\n\nCISO Talking Points:\n- "Your DLP investment extends to agents automatically. The rules you spent years tuning protect agent interactions without rework."\n- "Sensitivity labels travel with the data \u2014 whether a human or an agent touches it."\n- "Policy violations by agents produce the same alerts, in the same console, investigated by the same team."\n\nCIO Talking Points:\n- "No new data protection platform to procure. Your existing Purview investment covers agents."\n- "No \'agent DLP project\' to fund. Existing policies extend with configuration, not reimplementation."\n- "Cost of data protection governance doesn\'t scale linearly with agent count."\n\nIf asked about human-pattern DLP: Agents interact through the same channels \u2014 email, SharePoint, Teams, OneDrive. Enforcement points are identical.\nIf asked about different thresholds: Purview supports agent-scoped policy variants with different thresholds while reusing same sensitive information types.')

# === UC4 ===
section_divider('Use Case 4', 'Threat Detection and Response')

content_slide('Your SOC Monitors Users and Endpoints \u2014 Who\'s Monitoring Agents?',
    ['Compromised agents can be weaponized for lateral movement, data theft, or privilege escalation',
     'Agent-specific attack patterns (prompt injection, token theft, scope creep) need dedicated detection',
     'Agent 365 makes agents first-class Defender XDR assets with runtime protection',
     'Same SOC console, same alert queue, same incident response playbooks'],
    'Your SOC monitors users and endpoints around the clock. But what about agents? A compromised agent with broad permissions is an attacker\'s dream. Agent 365 brings agents into Defender XDR as first-class assets.')

content_slide('Live Demo: Threat Detection and Attack-Path Visualization',
    ['View agent assets in Defender XDR console',
     'Trigger a simulated anomalous agent behavior',
     'Observe alert generation in real time',
     'Walk through attack-path visualization showing potential blast radius',
     'Demonstrate SOC response: isolate agent, revoke tokens, investigate timeline'],
    'In this demo, we\'ll show your agents appearing as managed assets in the Defender console. Then we\'ll simulate anomalous behavior \u2014 an agent accessing resources outside its normal pattern. You\'ll see the alert fire, the attack-path visualization, and the SOC response workflow.\n\nDetailed procedure: demo-steps.md, UC4')

content_slide('How We Measure Success for Threat Detection',
    ['Defender generates alert within defined SLA for anomalous agent behavior',
     'Attack-path visualization accurately shows agent\'s potential blast radius',
     'SOC can isolate a compromised agent and revoke tokens from the same console',
     'Runtime protection prevents agent from executing blocked actions',
     'Incident timeline includes full agent activity history for forensics'],
    'We\'ll measure detection time, accuracy of the attack-path visualization, and the SOC\'s ability to respond from a single console. The key validation is end-to-end: anomalous behavior \u2192 alert \u2192 visualization \u2192 response \u2192 containment.')

content_slide('Why This Matters: One Console, One Incident Queue',
    ['Agents appear alongside users, devices, and apps in Defender XDR',
     'No separate SIEM integration or custom detection rules needed',
     'Attack-path analysis natively understands agent permissions and access patterns',
     'SOC response actions (isolate, revoke, block) work identically for agents',
     'Competing solutions require separate agent monitoring tools with manual SIEM forwarding'],
    'The differentiator is "first-class." Agents aren\'t bolted onto Defender as a custom data source \u2014 they\'re native assets.\n\nCISO Talking Points:\n- "Agent threats appear in the same Defender incident queue as user and endpoint threats \u2014 one priority list, one triage workflow."\n- "Correlation between agent and human activity happens automatically."\n- "Your SOC doesn\'t need an \'agent security\' specialization. Existing Defender skills apply directly."\n- "Automated response playbooks can isolate or disable a compromised agent the same way they isolate an endpoint."\n\nCIO Talking Points:\n- "No new security tool to procure for agent-specific threat detection."\n- "SOC headcount doesn\'t increase proportionally with agent count."\n- "MTTD and MTTR benefit from the same automation and AI-assisted investigation."\n\nIf asked about alert fatigue: Correlation reduces total alert volume. A compromised agent + DLP flag = one correlated incident, not three separate alerts.\nIf asked about agent-specific dashboards: Defender supports filtered views \u2014 agent-specific dashboards while benefiting from unified correlation.')

# === UC5 ===
section_divider('Use Case 5', 'Audit, Compliance, and Lifecycle')

content_slide('When Auditors Come Knocking, Can You Show the Agent Evidence Chain?',
    ['Regulatory frameworks increasingly expect governance over autonomous AI systems',
     'Auditors need a complete trail: who deployed it, what it accessed, when it was deactivated',
     'Agent 365 provides full lifecycle audit through M365 compliance fabric',
     'Same evidence format auditors already accept for user activities'],
    'Here\'s a scenario playing out right now: your compliance team passes an audit, but the auditor asks, "What about your AI agents?" If you can\'t answer that in the same compliance framework they already trust, you have a finding.')

content_slide('Live Demo: Full Audit Trail and Lifecycle Management',
    ['Review complete audit trail for an agent (deployment through operation)',
     'Execute lifecycle drill: block agent, deactivate agent, delete agent',
     'Verify each lifecycle action generates audit entry with timestamp and actor',
     'Show data retention policy applying to agent audit records',
     'Demonstrate compliance report including agent activities'],
    'We\'ll walk through the full lifecycle of an agent in audit terms. You\'ll see the trail from deployment through every action it took. Then we\'ll execute a lifecycle drill \u2014 blocking, deactivating, and deleting \u2014 verifying each action is audited.\n\nDetailed procedure: demo-steps.md, UC5')

content_slide('How We Measure Success for Audit and Compliance',
    ['Complete audit trail exists from agent deployment through deletion',
     'Each lifecycle state change generates a timestamped audit entry',
     'Data retention policies correctly apply to agent audit records',
     'Compliance report export includes agent activities in accepted format',
     'No gaps in evidence chain \u2014 auditor can reconstruct full agent history'],
    'Success here means an auditor can pick up the compliance report, see agent activities alongside user activities, and trace any agent\'s full history from deployment to deletion.')

content_slide('Why This Matters: No Parallel Evidence Chain',
    ['Agent audit data feeds the same M365 compliance fabric used for users',
     'Auditors already accept this format \u2014 no new validation required',
     'Data retention, legal hold, and eDiscovery apply uniformly',
     'No separate compliance tool generating evidence that auditors must learn to trust',
     'Competing solutions create a second evidence chain requiring separate attestation'],
    'The power here is trust. Your auditors already accept evidence from M365 compliance tools. Agent activities feed that same system.\n\nCISO Talking Points:\n- "Agent lifecycle events are captured in the same unified audit log your compliance team already queries."\n- "Retention policies that apply to human activity audit data apply to agent activity audit data."\n- "When auditors ask \'how do you govern agents?\', the answer is \'the same way we govern everything else.\'"\n\nCIO Talking Points:\n- "No new compliance tooling procurement. Agent audit evidence lives in existing M365 compliance infrastructure."\n- "Your compliance team doesn\'t need new skills or certifications."\n- "Audit preparation cost doesn\'t increase with agent adoption."\n\nIf asked about auditor unfamiliarity: They\'ll question it less if it\'s in a system they already trust.\nIf asked about agent-specific reports: The unified audit log supports filtered queries for agent-specific views.')

# UC5-5 HIDDEN
s = content_slide('Under the Hood: How Agent Lifecycle Feeds Compliance',
    ['Every agent action generates a unified audit log entry (same schema as user events)',
     'Lifecycle state changes trigger compliance workflow notifications',
     'Retention labels auto-apply to agent audit records based on classification',
     'eDiscovery index includes agent-generated content and interactions',
     'Export APIs produce audit packages in standard regulatory formats'],
    'Technically, every agent action writes to the same unified audit log as user actions \u2014 same schema, same retention handling. When an agent changes lifecycle state, compliance workflows fire automatically.')
hide_slide(s)

# === UC6 ===
section_divider('Use Case 6', 'Productivity Integration')

content_slide('Agents in Outlook, Teams, Word, and SharePoint \u2014 Governed or Ungoverned?',
    ['AI agents increasingly operate within productivity tools \u2014 drafting emails, posting in Teams, editing documents',
     'Without governance, these agents act with unbounded access across your collaboration surface',
     'Agent 365 enables governed connections with real-time allow/block enforcement',
     'Same productivity surface users know \u2014 no separate agent UI or plug-in'],
    'Your users work in Outlook, Teams, Word, and SharePoint. Increasingly, so do AI agents. The question is: are those agents operating under the same governance as your people?')

content_slide('Live Demo: Allow/Block Enforcement in Real Time',
    ['Block an entire connection (e.g., "Block Outlook Calendar connection")',
     'Demonstrate that the blocked connection prevents all agent access',
     'Show enforcement in real time',
     'Review audit trail capturing the blocked connection attempt',
     'Apply connection-level blocking across multiple M365 apps'],
    'We\'ll apply connection-level blocking by disabling specific connections for an agent. This approach is simpler and more dramatic for demos than granular action-level permissions.\n\nDetailed procedure: demo-steps.md, UC6')

content_slide('How We Measure Success for Productivity Integration',
    ['Agent successfully operates within allowed boundaries in Outlook, Teams, Word, and/or SharePoint',
     'Blocked actions are denied in real time (sub-second enforcement)',
     'Allow/block policies can be changed and take effect without redeploying the agent',
     'Audit trail captures both allowed and blocked actions with full context',
     'End users experience no disruption \u2014 governance is invisible to them'],
    'We need to prove three things: allowed actions work smoothly, blocked actions are denied instantly, and policy changes take effect without requiring agent redeployment.')

content_slide('Why This Matters: No Separate Agent UI',
    ['Agents operate natively within M365 apps \u2014 no separate interface for users to learn',
     'Governance is platform-level \u2014 not a per-app plug-in that can be bypassed',
     'Allow/block enforcement is real-time and centrally managed',
     'Users interact with agent output in the apps they already use daily',
     'Competing solutions require browser extensions, sidebars, or standalone agent portals'],
    'The differentiator is seamlessness. Your users don\'t need a new app, a browser extension, or a sidebar.\n\nCISO Talking Points:\n- "Agents in familiar surfaces means users follow established security behaviors."\n- "No new client application means no new attack surface to secure, patch, or monitor."\n- "Security controls that apply to Teams and M365 apps apply to agent interactions within them."\n\nCIO Talking Points:\n- "Adoption cost is near zero. Users interact with agents in Teams and M365 apps they already use daily."\n- "No client deployment project. No MDM profile updates."\n- "IT admin overhead is configuration, not infrastructure."\n\nIf asked about specialized interfaces: Adaptive Cards in Teams support complex workflows without leaving the familiar surface.\nIf asked about controlling visibility: Agent visibility controlled through same Teams app permission policies and Entra ID group assignments.')

# === CLOSING ===
section_divider('Summary & Next Steps', 'From Proof of Value to Production')

content_slide('What We Proved: Agent Governance That Works Today',
    ['\u2705 UC1: Every agent discovered and registered \u2014 zero shadow agents',
     '\u2705 UC2: Dedicated identity with least-privilege \u2014 same fabric as employees',
     '\u2705 UC3: DLP and sensitivity labels enforced \u2014 same policies as users',
     '\u2705 UC4: Threat detection and response \u2014 agents as first-class Defender assets',
     '\u2705 UC5: Full audit trail \u2014 compliance fabric auditors already trust',
     '\u2705 UC6: Governed productivity integration \u2014 real-time allow/block, no plug-ins'],
    'Let\'s bring it all together. Over these weeks, we proved that Agent 365 delivers real, measurable governance across every dimension. And we did it using the tools and frameworks your teams already operate. No new consoles, no parallel systems, no learning curve.')

content_slide('Broader Rollout: Extending Agent Governance Across Your Organization',
    ['Expand from 3+ PoV agents to full agent estate',
     'Integrate agent governance into existing change management processes',
     'Align agent lifecycle policies with your compliance calendar',
     'Enable self-service agent registration with guardrails for development teams',
     'Establish ongoing monitoring cadence with SOC team'],
    'The PoV proved the technology works with your agents in your environment. The next step is broader rollout \u2014 extending governance to your full agent estate, integrating with change management, and enabling self-service registration.')

content_slide('Let\'s Keep the Conversation Going',
    ['Your Microsoft account team: [Account Team Contacts]',
     'Agent 365 documentation: [Link to docs]',
     'PoV completion report: [Will be delivered at engagement close]',
     'FastTrack support for production deployment: [Link/contact]',
     'Community and feedback: [Tech Community link]'],
    'Thank you for your time and partnership throughout this Proof of Value. Your account team is here to support next steps. We\'ll deliver the formal PoV completion report within one week of engagement close. Let\'s govern your agents the way you govern your people.')

# === APPENDIX ===
section_divider('Appendix', 'Reference Materials')

content_slide('Roles & Responsibilities',
    ['Executive Sponsor \u2014 Approves scope, provides access, makes go/no-go decision',
     'IT Admin \u2014 Configures M365 Admin Center, manages agent registry',
     'Identity Admin \u2014 Manages Entra ID agent identities, conditional access policies',
     'Data Security Lead \u2014 Configures Purview DLP, sensitivity labels for agents',
     'SOC Analyst \u2014 Monitors Defender alerts, investigates agent threats, runs response',
     'Business Owners \u2014 Identify agents for PoV, validate success criteria alignment'],
    'Reference slide: Roles involved in the Agent 365 Proof of Value engagement.')

content_slide('Agent Types in Scope',
    ['Microsoft 365 Copilot',
     'Copilot Agent Builder agents',
     'Copilot Studio agents',
     'Microsoft 365 Copilot Chat',
     'SharePoint agents',
     'Azure AI Foundry agents',
     'First-party Microsoft agents'],
    'Reference slide: Agent types supported in the Agent 365 PoV. Note: Agent 365 is the governance capability set within Microsoft 365 \u2014 not a separately licensed product.')

content_slide('Glossary',
    ['Agent 365 \u2014 Microsoft 365 governance capability set for AI agents (not a separate SKU)',
     'Entra Agent ID \u2014 Workload identity in Entra ID purpose-built for agent governance',
     'Unified Audit Log \u2014 M365 compliance system of record for all user and agent activity',
     'Conditional Access \u2014 Policy engine enforcing identity-based access rules',
     'DLP (Data Loss Prevention) \u2014 Purview policies preventing unauthorized data exposure',
     'Sensitivity Labels \u2014 Classification and protection tags that travel with content'],
    'Reference slide: Key terms for mixed-audience understanding.')

# Save
output_path = r'C:\Users\chrwilliams\Agent365-PoV\Agent365-PoV-Deck.pptx'
prs.save(output_path)
print(f'SUCCESS: Saved to {output_path}')
print(f'Total slides: {len(prs.slides)}')
