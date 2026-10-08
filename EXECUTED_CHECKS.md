# Supplemental executed checks

These **63 narrowly scoped records** are separate from the 63 original cases. U01–U57 preserve earlier dated records; U58–U63 add run-4 observations. A PASS covers only its stated scope and timestamp. Supplemental records never enlarge the original-case denominator or imply end-to-end completion. The historical U51 uncertainty was later resolved within FUNC02’s SDK scope. Historical pending statements are superseded only by explicitly dated later evidence.

| Check | Result | UTC | Verified scope | Evidence |
|---|---|---|---|---|
| U01 Informed navigation | PASS | 03:33–03:40 | Home → APM introduction → global search → Live Debugger reached the intended route. No blind timing claim. | [Evidence](evidence/18-search-live-debugger-public.png) |
| U02 Manual entry without source | PASS | 03:21–03:24 | Manual session route opens without Source Code Integration. No successful runtime start. | [Evidence](findings/UX02-empty-state-recovery.md) |
| U03 Missing service prevents submit | PASS | 03:21–03:24; 04:01–04:02 | Start is disabled without service; Ctrl+Enter does not submit. | [Evidence](EVIDENCE.md#empty-modal-recovery) |
| U04 Actual 125 percent zoom | PASS | 03:33–03:40 | Native browser menu shows 125%; modal remains usable; reset to 100% verified. Failed shortcut attempt excluded. | [Evidence](evidence/19-debugger-zoom125-public.png) |
| U05 Modal focus and Escape | PASS | 03:33–03:40 | Tab focus cycles through modal controls; Escape closes and restores New Session focus. | [Evidence](evidence/20-logpoint-modal-zoom125.jpg) |
| U06 Modal history navigation | PASS | 03:33–03:40 | Back removes modal and reaches APM intro; Forward returns New Session without ghost modal. Empty-service context only. | [Evidence](EVIDENCE.md#empty-modal-recovery) |
| U07 Refresh and repeated Close | PASS | 04:01–04:02 | Refresh dismisses the empty-service modal; two open/Close cycles return correctly. No editable saved configuration. | [Evidence](EVIDENCE.md#empty-modal-recovery) |
| U08 Empty list filter persistence | PASS | 03:56–03:58 | Search/status/owner controls were exercised; status/owner persist on reload. No populated-result correctness. | [Evidence](EVIDENCE.md#empty-session-list-controls) |
| U09 Clear Filter and custom dates | PASS | 03:56–03:58 | Clear Filter resets selections. October 1–7 custom range displays correctly. Zero-session list. | [Evidence](EVIDENCE.md#empty-session-list-controls) |
| U10 Pre-install cancellation | PASS | 03:59–04:00 | Official/custom setup canceled; reload remains Not Connected. No App grant. | [Evidence](evidence/26-github-read-source-requirements.jpg) |
| U11 Final session inventory | PASS | 04:12 | All 0 / Active 0 / Inactive 0; filters cleared. Live accessibility observation after video stopped. | [Evidence](EVIDENCE.md#final-state) |
| U12 Python command controls | PASS | 02:31:35; 03:19:52 | Invalid module command exits 1; script and suffix-free module alternatives exit 0. Local-only, not Datadog capture. | [Evidence](findings/DOC01-python-launch-command.md) |
| U13 Published finding images | PASS | Verified by 03:59 | All four finding pages rendered their inline annotated image; the UX02 original-image link opened. Publication QA, not Datadog behavior. | [Evidence](findings.md#severity-ranked-finding-index) |
| U14 Temporary helper shutdown | PASS | 04:22:42 | Two completed local setup helpers stopped; each shows zero remaining owned processes. Private configuration retained without inspection. | [Evidence](EVIDENCE.md#final-state) |
| U15 Service discovery | PASS | 04:50:17 | The synthetic sample became selectable; only wildcard environment was offered. No session or capture. | [Evidence](EVIDENCE.md#approved-setup-milestones) |
| U16 Agent and sample snapshots | PASS | 04:47:03; 04:54:47 | Local Agent intake/sample startup and Agent RC org/key authorization verified at these instants. Debugger SDK client registration and current liveness remain unverified. | [Evidence](EVIDENCE.md#approved-setup-milestones) |
| U17 A-only installed scope | PASS | 04:51:29; 05:06:05 | GitHub installation plus persisted one-repository selection verified, identified privately as A. B created afterward remains ungranted. Datadog association failed. | [Evidence](evidence/38-a-only-after-b-created-public.png) |
| U18 Wildcard setup warning | PASS | 04:53:17 | Manual draft explains all-environment creation will not auto-enable the service and offers Configuration or a specific environment. | [Evidence](evidence/33-service-all-environments-warning-public.png) |
| U19 Invalid line draft controls | PASS | 04:54–04:55 | Line 0, -1 and abc kept Start disabled; 9999 enabled an unsubmitted draft and 17 restored the baseline. No runtime target validation. | [Evidence](evidence/34-line-zero-validation-public.png) |
| U20 Source guidance | PASS | 04:55:34 | Missing-source explanation identifies permissions or tags as possible causes and links Learn More; it does not claim fetched source. | [Evidence](evidence/36-source-unavailable-guidance-public.png) |
| U21 Template rejection and recovery | PASS | 05:06:52–05:38:08 | An actual unmatched brace disabled Start; blur added a red field outline. Correcting the brace enabled Start. Initial auto-balanced attempt excluded. | [Evidence](evidence/40-unmatched-brace-actual-public.png) |
| U22 Fixture file integrity | PASS | By 05:10 | Downloaded A pricing.py and app.py match the local baseline byte-for-byte; intended return target remains line 17. This is not Datadog source mapping. | [Evidence](EVIDENCE.md#fixture-integrity) |
| U23 Python Function draft | PASS | 05:39:50 | Function mode accepts Module pricing and Function calculate_quote as an enabled draft. No submit or entry/exit capture. | [Evidence](evidence/48-python-function-draft-public.png) |
| U24 Edited draft cancellation | PASS | 05:43 | Closing and reopening resets to Line mode and empty File/Line, retaining service/environment. No unsaved draft was published; reopened draft closed. | [Evidence](EVIDENCE.md#later-bounded-checks) |
| U25 Latest zero inventory | PASS | By 05:45 | After rejected creates and draft cancellation, All 0 / Active 0 / Inactive 0 remained. A-only installation unchanged; active lifecycle semantics untested. | [Evidence](EVIDENCE.md#later-bounded-checks) |
| U26 Historical APM ingestion | PASS | 05:49–06:21 | 47 indexed spans recovered; an actual old span carries HTTP 200, Python, staging, version 0.1.0 and the baseline commit. No debugger capture or source retrieval. | [Evidence](evidence/continuation-09/57-screenshot-only-ingested-env-commit.png) |
| U27 APM time-window recovery | PASS | 05:55–06:21 | Empty recent search offered a wider timeframe; one-hour history recovered spans. This is APM search behavior, not debugger result filtering. | [Evidence](evidence/continuation-09/53-historical-search-47-spans.png) |
| U28 SDK freshness guidance | PASS | By 06:15 | SDK Configurations states no data detected in the last 15 minutes and suggests runtime, telemetry and intake checks. Stopped runtime is compatible; no registration-failure conclusion. | [Evidence](evidence/continuation-09/55-sdk-no-recent-config.png) |


## New continuation observations

| Check | Result | UTC | Verified scope | Evidence |
|---|---|---|---|---|
| U29 Hosted SDK registration | PASS | 09:20:37 | Agent authorization and matching debugger/symbol SDK products were observed; registration alone is not capture. | [Evidence](evidence/continuation-11/hosted-readiness-20261008T092037Z.json) |
| U30 First-success timeline | PASS | 09:28–09:31 | Creation, instrumenting, event rows and visible locals were observed. Navigation/waiting is included; this is not measured ingestion latency. | [Evidence](EVIDENCE.md#recorded-first-success) |
| U31 Numeric baseline | PASS | 10:03–10:04 | Rendered numeric template and actual locals matched all quantity 2/3/4 controls. | [Evidence](evidence/continuation-12/f01-numeric-capture-controls.json) |
| U32 A-only source repair | PASS | 09:49–09:55 | Approved same-scope reinstall repaired the interrupted association; B remained ungranted. Successful callback is screenshot-only. | [Evidence](findings/SCI01-interrupted-github-recovery.md#verified-same-scope-recovery) |
| U33 Exact deployed source | PASS | 10:25:48 | In-product source and followed provider link matched deployed SHA, pricing.py line 17 and nearby code; older file last-change revision is distinct. | [Evidence](EVIDENCE.md#verified-deployed-source) |
| U34 Runtime handover control | PASS | 10:21–10:24 | Run 2 registered and an actual control snapshot executed afterward. Creation/status alone is not counted as capture. | [Evidence](evidence/continuation-12/82-control-snapshot-execution-timestamp-safe.png) |
| U35 Expiry and history | PASS | 10:45–10:50 | Active→expired transition was bounded; actual last target SDK timestamp and later live control support stop. Reload/direct link retained expiry/history. | [Evidence](EVIDENCE.md#verified-expiry-and-control) |
| U36 When editor operability | PASS | 10:30:40 | A normal supported click opened When; native disabled was false and no aria-disabled existed. Prior availability assessment was corrected. | [Evidence](EVIDENCE.md#conditional-capture-controls) |
| U37 Invalid-line rejection and recovery | PARTIAL | 10:29–10:33 | Line 9999 produced explicit NoFunctionsAtLine; a separate valid line 17 gutter probe captured. Blank/comment-line variants remain untested. | [Evidence](EVIDENCE.md#out-of-range-runtime-control) |
| U38 Predicate revision control | PASS | 10:33–10:35 | COND3 and COND4 post-activation rows/locals matched predicates; old selected COND3 snapshot was labeled OUTDATED. | [Evidence](EVIDENCE.md#conditional-capture-controls) |
| U39 No-match and restoration | PASS | 10:36–10:39 | Bounded NOMATCH interval had no new matching rows while baseline traffic continued; removing the predicate restored expected 2/3/4 rows. | [Evidence](EVIDENCE.md#no-match-and-recovery) |
| U40 B discovery check | PARTIAL | source 12 | Ungranted B was not found in the source picker. This is discovery evidence, not proof of denied private-content retrieval. | [Evidence](EVIDENCE.md#repository-boundary-limit) |
| U41 Direct event-link recovery | FINDING | 10:24; 10:41 | Two View in Logs errors recovered through exact-identity indexed rows. UX04 is Low; no data loss or cause claimed. | [Evidence](findings/UX04-view-in-logs-event-link.md) |
| U42 Source/value explanation and return | PASS | 10:42:45 | The same control snapshot/context survived return; Datadog source quantity > 3 and captured quantity 3/false/zero discount explained the planted application bug. | [Evidence](EVIDENCE.md#source-value-explanation) |

### Additional scope details for those checks

- U30 includes first visible quantity-three locals at 09:31:17.100 and the quantity-two comparison at 09:36:41.750. These are UI-observation clocks, not execution timestamps or an ingestion benchmark. No Logs setting changed in the observed recovery.
- U31 records the full numeric-template and actual-local 2/3/4 controls at 10:03:50.811–10:04:21.432; the quantity-three bug is deliberately planted in the application.
- U33 includes comparison of all 24 source lines, not only the nearby arithmetic. The selected deployed revision is distinct from the older file last-change label.
- U35 separates the bounded active/expired observation, last target SDK execution time, UI row time, no-newer-row recheck, later independent control and terminal state after reload/direct link. The desktop movie does not show the target's active-to-expired transition; it retains an already-expired after-state. Screenshots, rendered-UI observations and payloads establish the bounded transition. Re-enable/extend was untested at the V8 cutoff; the later explicit-resume control is separately recorded as U43.
- U37 is PARTIAL for the original full case: blank/comment-line branches remain untested. Recovery uses a separate valid probe, and no runtime relocation is inferred.
- U38 observed nine COND3 post-activation rows and six COND4 rows, with matching actual locals and OUTDATED feedback on the old selected capture. Row times are UI observations.
- U39 is a bounded never-match window, not an exhaustive backend query. Independent traffic continued; removing the condition resumed expected quantity 3, 2 and 4 RECOVER rows.
- U40 is PARTIAL: discovery no-match is not a private-content-denial pass.
- U41's early Logs visit was around 10:24–10:25; the target identity was verified at 10:41:47. Each exact requested snapshot ID, probe and timestamp matched the recovered indexed-row JSON. The matching row/count is obscured in screenshot 94. No root cause or data loss is claimed.
- U42 records the tested context after return at 10:42:45. Direct-event navigation friction is scored separately under U41/UX04.

## V9 observations through 13:15 UTC

| Check | Result | UTC | Verified scope | Evidence |
|---|---|---|---|---|
| U43 Explicit resume and stop | PASS | 11:29–11:31 | The expired target was explicitly resumed, retained identity and a renewed displayed duration, produced a fresh SDK-timestamped quantity-two capture, then was stopped and reloaded inactive/disabled. No all-session cleanup claim. | [Scoped evidence](EVIDENCE.md#explicit-resume-and-stop) |
| U44 Condition rejection and correction | PASS | 11:36; earlier invalid controls | Incomplete comparison and bare-local conditions were rejected in draft; a valid Boolean correction produced matching rows. Existing unmatched-template feedback finding UX03 remains separate. | [Scoped evidence](EVIDENCE.md#condition-validation-and-recovery) |
| U45 Missing-name definedness controls | PASS | Source 13, before 13:15 | Exact nonexistent-name evaluation error, absent-name False and available-local True controls were observed. Unassigned/deleted-local semantics are not covered by this PASS. | [Scoped evidence](EVIDENCE.md#missing-name-and-definedness) |
| U46 Message-only and restored variables | PASS | 11:42–11:43 and later capture | Capture off retained message events with an explicit no-debug-information explanation; re-enable applied only to future events, with a newer actual-locals capture. | [Scoped evidence](EVIDENCE.md#variable-capture-toggle) |
| U47 Function exit and line context | PARTIAL | Source 13, before 13:15 | Default function exit, complete return-object inspection and an explicit return-context error on a line advanced F07. Entry mode remains untested; the later safe derivatives are linked in the current evidence section. | [Scoped evidence](EVIDENCE.md#function-exit-and-line-context) |
| U48 Complex-object display | PARTIAL | By 12:23:09 | Typed empty collections, observed expansion and recorder-confirmed distinct 11/22 leaves and Unicode content. Long-string completeness, cycle/depth semantics, search/collapse and deeper protection remain open. | [Scoped evidence](EVIDENCE.md#complex-object-display) |
| U49 Targeted name-redaction controls | PASS | 12:20–12:21 observation window | Benign numeric/Boolean/text controls remained readable; tested dummy sensitive names and the credentials dictionary showed type without values and name-based-redaction guidance. Cleanup remains open. | [Scoped evidence](EVIDENCE.md#targeted-redaction-controls) |
| U50 Sampled overlapping-request association | PASS | SDK 12:23:34.913; 12:32:41.298 | Each of two different-pair samples retained matching locals, indexed identity, trace context and source-link association. This is not a complete pair or exhaustive concurrency proof. | [Scoped evidence](EVIDENCE.md#sampled-overlapping-request-association) |
| U51 Unbound/deleted-local display | UNCONFIRMED | Source 13, before 13:15 | Unassigned/deleted/branch-local rows displayed null; assigned controls displayed 42/404. Exact payload representation and renderer interpretation remain unresolved; no defect or severity assigned. | [Scoped evidence](EVIDENCE.md#local-value-semantics) |
| U52 Never-called no-traffic state | PARTIAL | Created about 12:43; checked 12:54:53 | Waiting with one instance and zero events contrasted with called siblings and an earlier installation error. Installation success and the final positive call remain unproved; template repair is needed. | [Scoped evidence](EVIDENCE.md#never-called-installation-control) |
| U53 Remote save loses unsaved condition | FINDING | 13:01; 13:02:52 repeat | Medium FUNC01: remote message-only save twice replaced the other tab’s unsaved quantity-three condition with stored quantity four. This does not prove conflicting saved-write or capture corruption. | [Scoped evidence](EVIDENCE.md#two-tab-unsaved-draft-loss) |
| U54 Disabled-probe draft Apply | UNCONFIRMED | 13:04:34–13:05:38 | Individual disabled status synchronized to both tabs, but Apply of a dirty draft re-instrumented the probe and new rows appeared. Intended contract and pre-action reactivation feedback remain unresolved. | [Scoped evidence](EVIDENCE.md#individual-disable-and-draft-apply) |
| U55 Individual and session hierarchy | PASS | By 13:13:55 | The reviewed individual/sibling/session disable sequence completed, including final whole-session stop. Scope is that tested hierarchy; all-session/runtime cleanup remains open. | [Scoped evidence](EVIDENCE.md#individual-and-session-hierarchy) |
| U56 Caught-exception local display | PARTIAL | Source 13, before 13:15 | A caught-exception capture displays typed error/control locals. The offscreen quotient-null observation is recorder-attributed; exception internals and complete stack behavior are not established. | [Scoped evidence](EVIDENCE.md#local-value-semantics) |

## Offline verification after the live cutoff

This addendum is outside the 13:15:00 UTC live-QA freeze and does not add or rescore an original case.

| Check | Result | UTC | Verified scope | Evidence |
|---|---|---|---|---|
| U57 Actual SDK absent-local serialization | FINDING | Result finalized 13:15:37; confirmed 13:16:33 | Medium FUNC02: actual installed ddtrace 4.11.0 helpers serialize unbound/deleted names identically to explicit None, while definedness differs. Assigned controls remain correct. Hosted transport payload was not inspected; scope is the tested package/helper controls. | [Finding, reproduction and exact provenance](findings/FUNC02-unbound-locals-serialized-as-null.md) |


## Run 4 records through 14:20:57 UTC

| Check | Result | UTC | Verified scope | Evidence |
|---|---|---|---|---|
| U58 Quiet-target positive invocation | PASS | 13:58:26.856 execution | Quiet one-instance/no-event state differs from explicit install ERROR; one positive call captured 707. Row and execution clocks stay separate. | [Evidence](EVIDENCE.md#run-4-quiet-target-positive-control) |
| U59 Blank and comment target controls | FINDING | Blank diagnostic inspected 14:14:20 | Low FUNC03: blank rejection suggests unsupported decorator despite zero decorators; valid line 17 captures correctly. Local source/SDK provenance separately checked. | [Finding](findings/FUNC03-blank-line-decorator-diagnostic.md) |
| U60 Bounded duplicate submission | PASS | About 14:04:40 and reload | One double-click-plus-Return attempt yields one added definition and count 12 after reload. Exact gesture count is interaction evidence, not a still claim. | [Evidence](EVIDENCE.md#run-4-duplicate-submission-control) |
| U61 Session-level disabled draft Apply | PARTIAL | About 14:16–14:18 | Parent/child consistency and fresh edited-message capture observed; intended reactivation contract and feedback unresolved. No new finding. | [Evidence](EVIDENCE.md#run-4-session-stop-and-stale-apply) |
| U62 Clean no-selection Pause | PASS | 14:13:05–14:13:27 | Same visible recent rows retained before/after Pause. Excludes already-auto-paused selected-event comparison. | [Evidence](EVIDENCE.md#run-4-clean-pause-control) |
| U63 Historical terminal inventory | PARTIAL | 14:20:57 | My sessions off, all filters clear, four inactive sessions and affected-session 12 disabled probes. Runtime terminal; final audit cleanup remains open after later work. | [Evidence](EVIDENCE.md#run-4-terminal-inventory) |
