# Datadog audit findings

The live-case ledger is frozen at 13:15:00 UTC with eight distinct findings. The offline ddtrace 4.11.0 verification finalized at 13:15:37 and was confirmed at 13:16:33 UTC; that separately dated addendum adds Medium FUNC02 without changing any original-case status. The combined report has nine distinct findings: 0 High, 4 Medium and 5 Low, with five remaining unconfirmed topics. See [FUNC02](findings/FUNC02-unbound-locals-serialized-as-null.md).

V9 evidence checkpoint: 2026-10-08 13:15:00 UTC. Nine distinct findings in the combined report: **0 High, 4 Medium and 5 Low**. Frozen V8 had seven findings at 10:50:59 UTC. Five current unconfirmed topics remain outside these totals.

Part 1 covers new-user usability. Part 2 covers Live Debugger and Source Code Integration QA. Both use this shared index. Historical findings retain their evidence and now include verified recovery where available.

## Severity ranked finding index

[High only](high-severity.md) · [Medium](#medium-severity) · [Low](#low-severity) · [Beginner glossary](glossary.md) · [Earlier V8 annotated report](report.pdf)

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

Every finding page links genuine screenshot evidence and its scope. Motion is linked where privacy-reviewed footage is available. UX04's matching row/count is not visible in its annotated still; exact identity matches and row-click recovery were verified separately. The source 12 archive is publicly verified at commit `7cdd468`; its reviewed highlight package remains pending publication verification. Its transition limits are documented in the video catalog.

## High severity

There are **no confirmed High-severity findings** in the established evidence. [Dedicated High-only view](high-severity.md). This does not rate untested areas as safe or defect-free.

## Medium severity

- [FUNC02 Unbound and deleted Python locals serialize as null](findings/FUNC02-unbound-locals-serialized-as-null.md): actual installed ddtrace 4.11.0 helper controls reproduce the loss of absent-versus-None distinction. Offline result finalized 13:15:37 and confirmed 13:16:33 UTC; hosted transport payload remains uninspected. No original-case outcome is changed.

- [FUNC01 Unsaved condition lost after a remote message-only save](findings/FUNC01-unsaved-condition-reset.md): reproduced twice. The stored condition stayed correct; stale saved-write conflicts and capture corruption are not established. [Annotated before](evidence/continuation-13/two-tab-132-135/134-unsaved-predicate-before-remote-save-outlined.png) · [Annotated after](evidence/continuation-13/two-tab-132-135/135-unsaved-predicate-overwritten-by-remote-save-outlined.png). Source 13 motion privacy review is pending.

- [DOC01 Python quickstart uses an invalid module command](findings/DOC01-python-launch-command.md): isolated reproduction fails, while supported script/module forms pass. The live baseline later captured via the supported script form; published documentation is not claimed fixed. [Screenshot](evidence/annotated/DOC01-python-launch-command.png) · [Video](early-onboarding-excerpt.mp4), 00:58–01:20.
- [SCI01 Interrupted GitHub connection does not recover through Connect](findings/SCI01-interrupted-github-recovery.md): the historical interrupted flow remained unconnected after fresh-context retry. An approved same-A-only uninstall/reinstall at 09:49–09:55 repaired association, and later source verification passed. The approximately 75-minute pause is not a proved cause.

## Low severity

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

63 original cases: **16 scoped PASS, 7 FINDING, 8 IN_PROGRESS, 8 PENDING and 24 BLOCKED**. [Full outcomes](QA_MATRIX.md) and [57 supplemental checks](EXECUTED_CHECKS.md) preserve exact scope. The distinct finding records are not a count of case outcomes.

Numeric live capture, one exact deployed-source match, conditional controls and one bounded expiry result are verified. B discovery no-match is not a private-content-denial test. Roles, deployment variants, remaining lifecycle/cleanup checks and other listed cases remain open. The planted application pricing bug is not a Datadog finding. [Unconfirmed observations](UNCONFIRMED_OBSERVATIONS.md) are explicitly excluded from severity totals.

## V9 evidence boundary

F04 and B09 both refer to existing UX03; this is not a second finding. FUNC01 is the only new confirmed finding within the 13:15 live cutoff. The separate 13:16:33 offline-verification addendum confirms Medium FUNC02. Disabled-draft reactivation remains unconfirmed without severity. V9 text/stills are prepared without a new public-availability claim. The PDF/Word remain dated V8 until separately regenerated.
