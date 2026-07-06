# Agent 365 POC — Final Review Verdict

**Reviewer:** Holden (Lead)  
**Date:** 2026-05-05  
**Documents Reviewed:** deck-outline.md, demo-steps.md, slide-content.md, differentiators.md

---

## Overall Verdict: APPROVED WITH NOTES

The deliverable set is strong, cohesive, and ready for assembly with minor corrections. A presales engineer could pick these up today and deliver a credible customer engagement.

---

## Strengths

1. **Structural alignment is excellent.** Naomi's slide content follows the deck outline's 5-slide pattern (Context → Capability → Demo → Success Criteria → Differentiator) faithfully across all 6 use cases. The narrative arc ("see it → secure it → prove it → use it") reads cleanly from slide 1 through the close.

2. **Amos's demo procedures are production-grade.** Prerequisites, click-by-click steps, expected results tables, validation checkpoints, troubleshooting tips, and time estimates — this is exactly what a presales engineer needs. The "Pro Tip" to pre-run UC4 simulations is the kind of field wisdom that saves demos.

3. **Avasarala's differentiators are layered for audience.** CISO, CIO, and Audit/Compliance talking points for each UC give the presenter persona-specific ammunition. Objection handling is realistic and non-dismissive. Technical accuracy notes are honest about limitations — this builds trust, not risk.

4. **Consistency of core messaging.** All four docs hammer the same unified theme: "same platform, same policies, same console, zero new tools." This repetition is deliberate and effective for customer memory.

5. **Terminology is consistent.** "Microsoft Entra," "Microsoft Purview," "Microsoft Defender XDR," "M365 Admin Center," "Copilot Studio," "Agent 365" — used correctly and consistently across all docs. No abbreviation drift (e.g., no "AAD" or "MDE" shortcuts).

6. **Demo-to-slide mapping works.** Each demo walkthrough slide in Naomi's content corresponds to a full procedure in Amos's doc. The demo slides use placeholder-friendly language ("Amos will guide you through each click") that correctly defers to the procedure doc.

---

## Issues Found

### Minor Issues (fix before assembly, low effort)

| # | File | Section | Issue |
|---|------|---------|-------|
| 1 | `slide-content.md` | Slide UC1-2 | References "AI Agents section" in Admin Center, but `demo-steps.md` UC1 uses "Settings → Org settings → Agent management → Agent registry." Navigation path should match. |
| 2 | `slide-content.md` | Slide UC1-4 | Title says "No Connectors. No Bolt-Ons." but deck outline slide 9 title is "Differentiator: Unified Registry." Titles should align or the outline should be updated to reflect final titling. |
| 3 | `deck-outline.md` | Section 1 | Outline specifies 5 slides (slides 5–9) but `slide-content.md` has 5 slides for UC1 *plus* an extra architecture slide (UC1-5: "Under the Hood"). Same pattern repeats for UC5 (extra architecture slide UC5-5). This makes 6 slides per UC for UC1 and UC5 vs. 5 for others. |
| 4 | `slide-content.md` | UC6-2 | Demo walkthrough describes "allow read, block send-as" for Outlook and "allow post, block DMs" for Teams. Amos's UC6 demo steps use a different scenario: "block Outlook Calendar connection." These should be reconciled — either both show connection-level blocking or both show granular action-level permissions. |
| 5 | `differentiators.md` | UC1 | References "Azure AI Agent Service" in technical accuracy notes. Amos's demo and Naomi's slides use "AI Foundry" / "Azure AI Foundry agents." Standardize on one term. |
| 6 | `demo-steps.md` | UC4, Step 9 | References "Defender → Settings → AI protection" as a possible nav path. This is speculative/preview-dependent. Flag as "if available" more prominently or move to a conditional section. |

### Observations (not blocking, note for v2)

| # | File | Observation |
|---|------|-------------|
| 7 | `deck-outline.md` | Outline says 38–42 slides total. With Naomi's extra architecture slides in UC1 and UC5, actual count is ~40 + appendix. Still within range but tight if appendix slides are included in main flow. |
| 8 | `demo-steps.md` | Total demo time sums to ~57–71 minutes across all 6 UCs. Combined with educational slides and transitions, a full session would run 90–110 minutes. Consider noting this exceeds the slide-content header's "60–90 minutes" estimate. |
| 9 | `differentiators.md` | Technical accuracy notes are excellent but should be removed from customer-facing materials before final assembly — they're internal guidance. Ensure assembly process strips these. |
| 10 | `slide-content.md` | Slide 4 says "4–6 Week Engagement" and UC summary says 6 use cases. If a customer wants an abbreviated engagement, there's no guidance on which UCs to cut. Amos's "Abbreviated version" and "Security-focused" variants at the end of demo-steps.md partially address this — cross-reference in the deck. |

---

## Recommendations for v2

1. **Reconcile UC6 demo scenario.** Decide whether the narrative is "connection-level allow/block" (Amos's approach — simpler, more dramatic) or "granular action-level permissions" (Naomi's approach — more sophisticated). I recommend Amos's connection-level approach for live demos (clearer visual payoff) and noting granular controls as a follow-up capability.

2. **Standardize navigation paths.** Create a shared "Portal Navigation Reference" appendix that both Naomi and Amos cite. This prevents drift as UI changes roll out.

3. **Add timing markers to slide content.** Naomi's doc has no per-slide timing guidance. Adding "~2 min" markers per slide would help presenters pace themselves.

4. **Add a "Shortened POC" slide variant.** Include a slide or appendix that maps abbreviated engagement options (3 UCs in 2 weeks, etc.) for customers who can't commit to 4–6 weeks.

5. **Clarify "Agent 365" as a solution name vs. product SKU.** All four docs use it as a solution brand, which is correct. But add a footnote in the deck (slide 3 or appendix) clarifying that Agent 365 is the governance capability set within Microsoft 365 — not a separately licensed product — to preempt customer procurement questions.

---

## Assembly Notes — Building the Final PowerPoint

### Slide Sequence
Follow `deck-outline.md` as the structural master. Insert content from `slide-content.md` slide-for-slide. For UC1 and UC5, include the extra architecture slides (UC1-5, UC5-5) as optional/hidden slides that can be shown for technical audiences.

### Demo Slides
Each "Demo Walkthrough" slide should contain:
- Naomi's bullet summary (what the audience will see)
- A footnote or hyperlink: "Detailed procedure: demo-steps.md, UC[X]"
- In the actual presentation, the presales engineer follows Amos's doc on their second screen while the audience sees the live portal.

### Differentiator Slides
Each "Differentiator" slide should pull:
- Title and bullets from `slide-content.md` (customer-facing)
- Speaker notes enriched with Avasarala's CISO/CIO talking points from `differentiators.md` (pick audience-appropriate persona)
- Objection handling goes into presenter's hidden notes (not shown on screen)

### Speaker Notes Assembly
- Naomi's speaker notes = primary script
- Avasarala's talking points = supplementary ammo (add as "If asked..." bullets in notes)
- Amos's troubleshooting tips = emergency reference (separate printed cheat sheet, not in PPT)

### Appendix
Include deck outline's A1–A3 slides. Add one more: **A4: Technical Accuracy Notes** (compiled from Avasarala's caveats) — internal only, stripped before sending to customer.

### File Handoff
| Deliverable | Goes To | Format |
|-------------|---------|--------|
| Final .pptx | Customer | PowerPoint (stripped of internal notes) |
| demo-steps.md | Presales engineer | Printed or second-screen reference |
| differentiators.md | Presales engineer | Pre-read / objection prep |
| deck-outline.md | Internal archive | Blueprint for future POC decks |

---

*Reviewed and approved with notes by Holden, 2026-05-05. Team delivers v1 assembly; issues 1–6 to be fixed in first pass.*
