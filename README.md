# Datadog Live Debugger and Source Code Integration audit

The live-case ledger is frozen at 13:15:00 UTC with eight distinct findings. The offline ddtrace 4.11.0 verification finalized at 13:15:37 and was confirmed at 13:16:33 UTC; that separately dated addendum adds Medium FUNC02 without changing any original-case status. The combined report has nine distinct findings: 0 High, 4 Medium and 5 Low, with five remaining unconfirmed topics. See [FUNC02](findings/FUNC02-unbound-locals-serialized-as-null.md).

V9 live-QA evidence checkpoint: **8 October 2026 at 13:15:00 UTC**, with a separately dated offline-verification addendum confirmed at **13:16:33 UTC**. The audit is ongoing. Frozen V8 describes the earlier 10:50:59 UTC checkpoint; later work is not retroactively attributed to that freeze.

Nine distinct findings in the combined report: **0 High, 4 Medium and 5 Low**. 63 original cases: **16 scoped PASS, 7 FINDING, 8 IN_PROGRESS, 8 PENDING and 24 BLOCKED**. Five unconfirmed topics are tracked separately; the null-display topic is now confirmed within FUNC02’s SDK scope.

## Read the results

- [Current status and retained test assets](CURRENT_STATUS.md)
- [Severity-ranked findings](findings.md#severity-ranked-finding-index), [High only](high-severity.md), [Medium](findings.md#medium-severity), [Low](findings.md#low-severity)
- [All 63 case outcomes](QA_MATRIX.md), [57 separately scoped checks](EXECUTED_CHECKS.md), [evidence and timestamps](EVIDENCE.md)
- [Unconfirmed observations](UNCONFIRMED_OBSERVATIONS.md) and [video catalog](VIDEOS.md)
- [Earlier V8 annotated PDF](report.pdf) and [earlier V8 editable Word report](report.docx): both retain the 10:50:59 UTC V8 snapshot with seven findings until separately regenerated
- [Beginner glossary](glossary.md)

## New verified results since V8

- [FUNC02, Medium](findings/FUNC02-unbound-locals-serialized-as-null.md): actual ddtrace 4.11.0 helpers serialize unbound/deleted locals identically to explicit None, although definedness distinguishes them. The offline result was confirmed after the live cutoff; hosted transport-payload attribution remains unverified.

- [FUNC01, Medium](findings/FUNC01-unsaved-condition-reset.md): a message-only save in one tab twice erased an unsaved condition in another tab, without an observed warning. The stored predicate remained correct; capture corruption is not established.
- F04 completes the functional malformed-condition/correction controls and retains existing Low UX03 for unmatched-template feedback. F05 passes the exact nonexistent-name, false-definedness and available-local controls. The later unassigned/deleted-local SDK defect is a separate FUNC02 finding, confirmed after the live cutoff.
- F12 verifies explicit resume of the expired target, preserved identity, fresh SDK-timestamped capture and stop/reload cleanup. F16 verifies message-only capture and restoration of variables in a newer event.
- F21 passes the tested Targeted name-redaction controls. X06 passes two sampled overlapping-request association checks; the two samples came from different pairs and are not a completely collected concurrent pair.
- F13 passes the tested individual/sibling/session hierarchy sequence. This does not establish the final all-session, runtime or settings inventory.
- F07 and F10 are partial: function-exit and line-context controls advanced, while entry remains untested; applying a draft to an individually disabled probe reactivated it, but intended disabled-edit semantics remain unresolved.

## Established baseline retained

The numeric quantity 2/3/4 controls, full 24-line deployed-source match, conditional revision/no-match recovery, and bounded expiry/history controls from V8 remain established. The quantity-three boundary error is deliberately planted in the synthetic application. The approved same-A-only source-integration repair does not erase historical SCI01; B remains ungranted.

## Remaining limits and evidence availability

The original 63 definitions and cleanup requirements are preserved. Blank/comment-line behavior, function entry, stale saved-write variants, deeper value/cycle checks, restricted identities, source-isolation variants and several lifecycle checks remain incomplete or blocked. C01/C02 remain IN_PROGRESS; stopping one session does not prove all captures, traffic or retained settings are reconciled.

Reviewed stills 103–135 and the new finding page are prepared in this checkpoint. Later controls described in prose have no invented screenshot or video links while their safe derivatives remain pending. No public upload of V9 or its new evidence is implied by this prepared directory.

Sources 01–12 retain their finalized media totals. Source 12's eight archive files were publicly verified at commit `7cdd468`; four highlight-package files remain pending publication verification. Source 13 began at 11:18:29 UTC and was still recording at the cutoff. A later status update confirms the raw recording is finalized; final duration, retained coverage, motion privacy review and public availability are not established here. See [exact media boundaries](VIDEOS.md).

## Later unscored status

At 13:17:59 UTC, the session inventory with My sessions enabled showed All 4 / Active 0 / Inactive 4. This later observation is outside the frozen case ledger. It does not establish final runtime/traffic, fixture, settings or grant cleanup; C01/C02 retain their 13:15 IN_PROGRESS outcomes.
