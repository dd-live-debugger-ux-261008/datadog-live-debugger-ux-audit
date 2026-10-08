# Datadog audit findings

Work in progress. Report and online finding pages updated 2026-10-08 03:31 UTC.

Part 1 covers brand-new Datadog/APM usability. Part 2 covers professional Live Debugger and Source Code Integration QA. Both use this shared index.

## Severity ranked finding index

[High only](high-severity.md) · [Medium](#medium-severity) · [Low](#low-severity) · [Beginner glossary](glossary.md) · [Annotated report](report.pdf)

| ID | Severity | Type | Part | Finding and online evidence |
|---|---|---|---|---|
| DOC01 | MEDIUM | Confirmed documentation bug | 2 | [Python quickstart uses an invalid module command](findings/DOC01-python-launch-command.md) |
| DOC02 | LOW | Confirmed layout bug | 1 | [Contents rail splits section names mid-word](findings/DOC02-documentation-navigation.md) |
| UX01 | LOW | UX recommendation | 1 | [Permanent region choice needs decision support](findings/UX01-region-choice.md) |
| UX02 | LOW | UX recommendation | 1 | [Empty service states do not explain setup recovery](findings/UX02-empty-state-recovery.md) |

Every finding page contains an inline annotated screenshot, a full-size image link, the original evidence, a video link with chapter times where published, and the finding's scope and reproduction or assessment.

## High severity

There are currently **no confirmed HIGH-severity findings** in the evidence established so far. [Open the dedicated High-only view](high-severity.md). This does not rate untested areas as safe or defect-free.

## Medium severity

- [DOC01 Python quickstart uses an invalid module command](findings/DOC01-python-launch-command.md): the Python portion fails an isolated reproduction, while correct script/module forms pass. [Screenshot](evidence/annotated/DOC01-python-launch-command.png) · [Video](early-onboarding-excerpt.mp4), 00:58–01:20.

## Low severity

- [DOC02 Contents rail splits section names mid-word](findings/DOC02-documentation-navigation.md): observed at default desktop zoom in two scroll positions. [Screenshot](evidence/annotated/DOC02-documentation-navigation.png) · [Video](early-onboarding-excerpt.mp4), 00:34–00:58.
- [UX01 Permanent region choice needs decision support](findings/UX01-region-choice.md): a recommendation that preserves the clear permanent-choice warning. [Screenshot](evidence/annotated/UX01-region-choice.png) · [Video](early-onboarding-excerpt.mp4), 00:20–00:34.

- [UX02 Empty service states do not explain setup recovery](findings/UX02-empty-state-recovery.md): natural first-run no-service/no-environment views give no concrete recovery step in the captured section. [Service screenshot](evidence/annotated/UX02-empty-service-list.png) · [Setup screenshot](evidence/annotated/UX02-no-environments.png). Public video excerpt pending.

## Severity rubric and evidence types

- HIGH: core task blocked or significant incorrect behavior with no reasonable workaround.
- MEDIUM: material task failure or misleading behavior with a practical workaround.
- LOW: localized readability, discoverability, or friction without demonstrated task failure.

Confirmed bugs have direct evidence. UX recommendations describe an improved experience. Hypotheses remain unverified. Environment and setup limits constrain coverage and are not automatically product findings. Test priority P0/P1/P2 is separate from defect severity.

## Current scope and remaining coverage

Fresh test accounts reached authenticated welcome/home states. Local fixture tests passed except for one intentional expected failure representing the demo's planted pricing bug. That bug is not a Datadog defect.

No successful Datadog variable capture, exact deployed-source match, repository authorization boundary, or expiry result is claimed by this checkpoint. Runtime readiness and service-process availability alone do not establish ingestion.

The [QA matrix](QA_MATRIX.md) preserves 54 baseline cases and adds nine supplementary cases X01–X09. The latest scoped results are B02 → UX02 and B04 → PASS for manual-route discoverability only. F14 and S01 are partially in progress; 59 cases remain planned. The total of 63 is not an executed-test count. They cover first-capture onboarding, missing prerequisites, source permissions and recovery, commit drift, invalid inputs, lifecycle, stale state, redaction, mixed replicas, async correlation, and simultaneous sessions.

At audit close, each case will have an executed outcome, a concrete blocker, or an unsupported classification. The ongoing plan is not presented as exhausted coverage.
