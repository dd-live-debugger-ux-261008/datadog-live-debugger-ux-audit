# Datadog audit findings

V11 web checkpoint: evidence through **8 October 2026, 18:51:18 UTC**. The 63 original definitions are preserved: **22 scoped PASS, 8 FINDING, 12 IN_PROGRESS, 2 PENDING and 19 BLOCKED**. Findings remain **10: 0 High, 4 Medium and 6 Low**. Seven unresolved topics are outside severity totals. Further original-case work is planned; dated runtime and cleanup updates are kept separately.

The [PDF](report.pdf) and [Word report](report.docx) remain the checked **31-page V9 snapshot**, with nine findings, live-case cutoff 13:15:00 UTC and separate SDK verification confirmed 13:16:33 UTC. They have not been regenerated for this web checkpoint; use the web pages for run 4, source controls and retained-state checks.

Part 1 covers new-user usability. Part 2 covers Live Debugger and Source Code Integration QA. Both use this shared index. Historical findings retain their evidence and now include verified recovery where available.

## Severity ranked finding index

[High only](high-severity.md) · [Medium](#medium-severity) · [Low](#low-severity) · [Beginner glossary](glossary.md) · [V9 annotated report](report.pdf)

| ID | Severity | Type | Part | Finding and online evidence |
|---|---|---|---|---|
| DOC01 | MEDIUM | Confirmed documentation bug | 2 | [Python quickstart uses an invalid module command](findings/DOC01-python-launch-command.md) |
| SCI01 | MEDIUM | Scoped recovery issue | 2 | [Interrupted GitHub connection does not recover through Connect](findings/SCI01-interrupted-github-recovery.md); same-scope reinstall recovery now verified |
| FUNC01 | MEDIUM | Confirmed unsaved-draft loss | 2 | [A remote message-only save erases another tab’s unsaved condition](findings/FUNC01-unsaved-condition-reset.md) |
| FUNC02 | MEDIUM | Confirmed SDK serialization defect | 2 | [Unbound/deleted Python locals serialize identically to explicit None](findings/FUNC02-unbound-locals-serialized-as-null.md); offline verification confirmed 13:16:33 UTC after live cutoff |
| DOC02 | LOW | Confirmed layout bug | 1 | [Contents rail splits section names mid-word](findings/DOC02-documentation-navigation.md) |
| UX01 | LOW | UX recommendation | 1 | [Permanent region choice needs decision support](findings/UX01-region-choice.md) |
| UX02 | LOW | UX recommendation | 1 | [Empty service states do not explain setup recovery](findings/UX02-empty-state-recovery.md) |
| UX03 | LOW | Scoped feedback issue | 1 | [Invalid log template lacks an explanatory error message](findings/UX03-invalid-log-template-feedback.md) |
| UX04 | LOW | Scoped navigation recovery issue | 1 | [View in Logs opens a not-indexed pane for a recoverable indexed snapshot](findings/UX04-view-in-logs-event-link.md) |
| FUNC03 | LOW | Confirmed diagnostic specificity issue | 2 | [Blank-line rejection suggests an unsupported decorator](findings/FUNC03-blank-line-decorator-diagnostic.md) |

Every finding page links genuine screenshot evidence and its scope. Motion is linked where privacy-reviewed footage is available. UX04's matching row/count is not visible in its annotated still; exact identity matches and row-click recovery were verified separately. The source 12 archive is publicly verified at `7cdd468` and its reviewed highlight package at `9edb46e`. Its transition limits are documented in the video catalog.

## High severity

There are **no confirmed High-severity findings** in the established evidence. [Dedicated High-only view](high-severity.md). This does not rate untested areas as safe or defect-free.

## Medium severity

- [FUNC02 Unbound and deleted Python locals serialize as null](findings/FUNC02-unbound-locals-serialized-as-null.md): actual installed ddtrace 4.11.0 helper controls reproduce the loss of absent-versus-None distinction. Offline result finalized 13:15:37 and confirmed 13:16:33 UTC; hosted transport payload remains uninspected. No original-case outcome is changed.

- [FUNC01 Unsaved condition lost after a remote message-only save](findings/FUNC01-unsaved-condition-reset.md): reproduced twice. The stored condition stayed correct; stale saved-write conflicts and capture corruption are not established. [Annotated before](evidence/continuation-13/two-tab-132-135/134-unsaved-predicate-before-remote-save-outlined.png) · [Annotated after](evidence/continuation-13/two-tab-132-135/135-unsaved-predicate-overwritten-by-remote-save-outlined.png). [Reviewed source 13 motion and its visibility limits](recordings/continuation-13/highlights/CONTINUATION_HIGHLIGHTS.md) are available; the complete overwrite transition remains still/chronology evidence.

- [DOC01 Python quickstart uses an invalid module command](findings/DOC01-python-launch-command.md): isolated reproduction fails, while supported script/module forms pass. The live baseline later captured via the supported script form; published documentation is not claimed fixed. [Screenshot](evidence/annotated/DOC01-python-launch-command.png) · [Video](early-onboarding-excerpt.mp4), 00:58–01:20.
- [SCI01 Interrupted GitHub connection does not recover through Connect](findings/SCI01-interrupted-github-recovery.md): the historical interrupted flow remained unconnected after fresh-context retry. An approved same-A-only uninstall/reinstall at 09:49–09:55 repaired association, and later source verification passed. The approximately 75-minute pause is not a proved cause.

## Low severity

- [FUNC03 Blank-line rejection suggests an unsupported decorator](findings/FUNC03-blank-line-decorator-diagnostic.md): line 10 is blank, the function has no decorators, and line 17 captures correctly. The rejection is appropriate; the explanation is misleading. [Annotated error](evidence/control-phase-155-167/annotation/163-line-10-unsupported-decorator-hint-outlined.png) · [Source 14 chapter map](recordings/continuation-14/highlights/CONTINUATION_HIGHLIGHTS.md), diagnostic at 03:42.

- [DOC02 Contents rail splits section names mid-word](findings/DOC02-documentation-navigation.md): observed at default desktop zoom in two scroll positions. [Screenshot](evidence/annotated/DOC02-documentation-navigation.png) · [Video](early-onboarding-excerpt.mp4), 00:34–00:58.
- [UX01 Permanent region choice needs decision support](findings/UX01-region-choice.md): recommendation that preserves the clear permanent-choice warning. [Screenshot](evidence/annotated/UX01-region-choice.png) · [Video](early-onboarding-excerpt.mp4), 00:20–00:34.
- [UX02 Empty service states do not explain setup recovery](findings/UX02-empty-state-recovery.md): first-run no-service/no-environment views lack a concrete nearby recovery step. Later healthy staging capture is verified and does not prove that a healthy service was previously missing. [Service screenshot](evidence/annotated/UX02-empty-service-list.png) · [Setup screenshot](evidence/annotated/UX02-no-environments.png).
- [UX03 Invalid log template lacks an explanatory error message](findings/UX03-invalid-log-template-feedback.md): red-border/disabled-button validation and correction work, but the tested state lacks explanatory syntax-error text. No screen-reader or global WCAG failure is asserted.
- [UX04 View in Logs opens a not-indexed pane for a recoverable indexed snapshot](findings/UX04-view-in-logs-event-link.md): repeated on two exact snapshot identities; a row click recovers details. [Annotated screenshot](evidence/continuation-12/94-view-in-logs-not-indexed-outlined.png). No root cause or data-loss claim.

## Severity rubric and evidence types

- HIGH: core task blocked or significant incorrect behavior with no reasonable workaround.
- MEDIUM: material task failure or misleading behavior with bounded demonstrated impact.
- LOW: localized readability, discoverability, or friction without demonstrated task failure.

Confirmed bugs have direct evidence. UX recommendations describe an improved experience. Hypotheses remain unverified. Environment/setup limits constrain coverage and are not automatically product findings. Test priority P0/P1/P2 is separate from severity.

## Current scope and remaining coverage

63 original cases: **22 scoped PASS, 8 FINDING, 12 IN_PROGRESS, 2 PENDING and 19 BLOCKED**. [Full outcomes](QA_MATRIX.md) and [72 supplemental records](EXECUTED_CHECKS.md) preserve exact scope. The distinct finding records are not a count of case outcomes.

Numeric live capture, one exact deployed-source match, conditional controls and one bounded expiry result are verified. B discovery no-match is not a private-content-denial test. Roles, deployment variants, remaining lifecycle/cleanup checks and other listed cases remain open. The planted application pricing bug is not a Datadog finding. [Unconfirmed observations](UNCONFIRMED_OBSERVATIONS.md) are explicitly excluded from severity totals.

## Evidence boundaries

F04 and B09 retain the same UX03 finding, without duplication. FUNC02 remains the separately verified SDK defect. FUNC03 adds one Low diagnostic finding after run 4. F10's Apply-feedback question remains unconfirmed and has no severity. The PDF/Word retain the explicitly dated nine-finding V9 snapshot; this web checkpoint contains the current ten-finding inventory.
