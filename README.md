# Datadog Live Debugger and Source Code Integration audit

Overnight checkpoint: 8 October 2026, 04:23 UTC (00:23 New York). Runtime and source testing are paused at explicit authorization gates. This is a resumable report, not a completed end-to-end audit.

The report has two distinct parts:
1. Beginner usability: a structured walkthrough of fresh Datadog and APM onboarding, with no recruited participants or blind timing claim.
2. Detailed functional QA: exact case definitions, observed results, concrete blockers and remaining runtime/source/permission/lifecycle checks.

## Read the results

- [Annotated PDF](report.pdf) and [editable Word report](report.docx)
- [Severity-ranked findings](findings.md#severity-ranked-finding-index)
- [High severity only](high-severity.md), [Medium](findings.md#medium-severity), [Low](findings.md#low-severity)
- [All 63 case outcomes and full plan](QA_MATRIX.md)
- [Evidence, timestamps and recording boundaries](EVIDENCE.md)
- [Beginner glossary](glossary.md)
- [Video catalog with all reviewed excerpts and archive status](VIDEOS.md)
- [Authenticated UI QA motion](authenticated-ui-qa-excerpt.mp4), [account/setup transitions](account-setup-excerpt.mp4), and [public onboarding](early-onboarding-excerpt.mp4)

## What is established

HIGH 0 · MEDIUM 1 · LOW 3. Two confirmed documentation/layout defects and two separately labeled UX recommendations have individual evidence pages with inline annotated screenshots and full-size links. The medium finding is the invalid Python module launch example, reproduced locally with positive controls.

63 cases accounted for: 2 scoped PASS, 2 FINDING, and 59 BLOCKED.

Scoped passes cover manual-route entry and pre-install cancellation/reload. The separate [executed subchecks](EXECUTED_CHECKS.md) preserve zero-session inventory, isolated documentation-command reproduction, modal, keyboard, navigation and empty-list observations without promoting their entire parent cases. No successful runtime variable capture, exact deployed-source mapping, A-only/B-denied repository boundary, or expiry/disable behavior was verified.

## Current stop and resume state

The Agent and sample are stopped; source integration remains unconnected. At 04:12 UTC the session inventory was All 0 / Active 0 / Inactive 0 with filters cleared. Test accounts, the public audit repository and private fixture A are intentionally retained. Full all-settings cleanup reconciliation is not certified.

Resume after the specific telemetry-payload approval and official GitHub App A-only installation approval. First establish a real capture at the known fixture line, then validate exact deployed SHA and the never-granted B boundary. Run the shortest actual expiry test through its terminal state. Further role/revocation or controlled-failure tests need their own stated gates. The [matrix](QA_MATRIX.md) preserves each case's prerequisites, steps, expected result and cleanup.

All clocks are UTC unless stated otherwise. Screenshots are actual browser captures; red borders are annotations. Public files omit credentials, private account identifiers, private browser/session URLs and raw authenticated recordings. No generated mockup is represented as evidence.
