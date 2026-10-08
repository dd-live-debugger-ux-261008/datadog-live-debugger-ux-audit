# Unconfirmed observations and remaining questions

V9 evidence checkpoint: 2026-10-08 13:15:00 UTC. This current five-topic inventory is **outside the nine distinct combined findings and all severity totals**. The four V8 topics are retained below, followed by the disabled-draft candidate. Six topics were unconfirmed at the 13:15 live cutoff; the separate 13:16:33 FUNC02 verification resolves the null-display topic within its stated SDK scope. It records bounded observations that do not yet establish another product defect.

| Observation | What was established | What is not established / next discriminating check |
|---|---|---|
| Initial Enable logs state | The first successful session showed the message, while existing Logs were later visible; returning and reloading showed events without a Logs setting change. | Whether this was expected setup propagation, a stale view, or misleading guidance. Repeat on a comparable healthy new session with separate navigation and timing controls. |
| Early wildcard HTTP 400 and recovery guidance | Two 05:15/05:19 creates, including a plain-message control, showed instrumentation-invalid toasts and HTTP 400; Configuration showed no environments. A later healthy staging baseline succeeded. | The root cause of the early rejection, whether runtime readiness was sufficient, and whether a specific-environment control at the same instant would have succeeded. Do not label this a silent failure or prove a capture defect from those attempts. |
| Countdown and edited-child lifetime behavior | At the 10:50:59 scored-case cutoff, definition edits and later expiry were observed without a controlled Apply/deadline comparison. A later 11:33 follow-up found the older failed line-9999 probe already expired while the later-edited line-17 probe still captured and the session header showed 6 minutes. | Edits did not renew every sibling. The visible session countdown appears tied to active child lifetimes; that is an interpretation needing explanation, not a demonstrated session-wide TTL defect. The 11:33 follow-up narrows this candidate; V9 scores separately evidenced explicit-resume behavior under F12 without claiming a session-wide TTL defect. |
| Invalid line 9999 marker near file end | The source view showed a marker near the file end while the invalid target was tested. Runtime status separately reported `NoFunctionsAtLine` ERROR. A new valid line-17 probe then captured. | No runtime relocation to another executable line is proved. Inspect selected-target identity and probe location before treating the visual marker as execution placement. Blank/comment-line behavior is still untested. |

## Relationship to frozen V8

The 11:33 UTC observation occurred after the frozen V8 10:50:59 UTC cutoff. V8 remains unchanged. V9 includes the later explicit-resume/stop controls and records F12 PASS, while the edited-child/countdown interpretation remains unconfirmed.

## Corrected or unresolved accessibility interpretation

- The earlier assessment that When was disabled was corrected by an ordinary supported click. The control is operable, and actual conditional capture passed. This is not a product finding.
- The Line field's computed accessible name remains unresolved. Archived attributes alone do not establish it. The verified UX03 template-error feedback issue remains separate; no screen-reader run or global WCAG finding is claimed.

Repository B discovery no-match is a coverage limitation, not proof of private-content denial or a security finding. The original 63-case statuses remain in the [matrix](QA_MATRIX.md).

[Confirmed/scoped findings](findings.md) · [Evidence](EVIDENCE.md) · [Current status](CURRENT_STATUS.md)

## Fifth topic: Apply reactivates an individually disabled probe

During 13:04:34–13:05:38 UTC, both tabs showed the individual probe DISABLED. A pre-existing dirty message draft still had Apply available; applying it re-instrumented the probe and new rows appeared. The question is whether the action communicates renewed collection clearly and follows the intended disabled-edit contract. This remains **UNCONFIRMED**, without severity, a security-bypass claim or a disable-contract-violation claim.

[Datadog's creating-logpoints documentation](https://docs.datadoghq.com/tracing/live_debugger/#creating-logpoints) generally describes instrumentation/capture after logpoint modifications. It does not expressly define this disabled-edit scenario. Individual, session and service/environment disable scopes must remain distinct. F13's separate hierarchy controls do not automatically settle the stale-draft contract. F10 remains IN_PROGRESS. The still showing a new row retained an older OUTDATED capture in its details pane; those locals are not attributed to the new row. Safe derivatives for this branch remain pending; no raw or invented evidence link is supplied.

## Separate test-setup follow-up

The never-called probe's draft message references a name that is not in the function's scope. Correct it to an in-scope local or literal before the final authorized positive invocation. This is a setup task under X03, **not a sixth current product candidate or a finding**. [Waiting-state evidence](evidence/continuation-13/locals-126-131/129-never-called-waiting-for-events-safe.png).

FUNC01's twice-reproduced unsaved-condition loss is confirmed and lives in the finding inventory, not this candidate count. The current candidate inventory reflects the separately dated FUNC02 verification; the original case outcomes remain frozen at 13:15 UTC.

## Resolved by the separately dated SDK verification

The unassigned/deleted-local topic was unconfirmed at the live cutoff. An actual installed-package reproduction in ddtrace 4.11.0 finalized at 13:15:37 UTC and was confirmed at 13:16:33 UTC. It demonstrates that unbound/deleted locals serialize with the same NoneType/isNull representation as explicit None while definedness distinguishes them. It is now [Medium FUNC02](findings/FUNC02-unbound-locals-serialized-as-null.md), outside this five-topic inventory. Hosted transport-payload attribution remains unverified; F05’s narrower original PASS is unchanged.
