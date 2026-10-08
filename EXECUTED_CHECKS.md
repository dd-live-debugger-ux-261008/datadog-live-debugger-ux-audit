# Supplemental executed checks

These 25 narrowly scoped checks are separate from the 63 original-case outcomes. A PASS covers only the stated observation, including historical snapshots. It does not imply runtime capture or an end-to-end pass.

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
| U16 Runtime prerequisite snapshots | PASS | 04:47:03; 04:54:47 | Agent/trace/SDK readiness and RC enabled/key-authorized were verified at these instants; later scope stop means this is not current liveness. | [Evidence](EVIDENCE.md#approved-setup-milestones) |
| U17 A-only installed scope | PASS | 04:51:29; 05:06:05 | GitHub installation plus persisted one-repository selection verified, identified privately as A. B created afterward remains ungranted. Datadog association failed. | [Evidence](evidence/38-a-only-after-b-created-public.png) |
| U18 Wildcard setup warning | PASS | 04:53:17 | Manual draft explains all-environment creation will not auto-enable the service and offers Configuration or a specific environment. | [Evidence](evidence/33-service-all-environments-warning-public.png) |
| U19 Invalid line draft controls | PASS | 04:54–04:55 | Line 0, -1 and abc kept Start disabled; 9999 enabled an unsubmitted draft and 17 restored the baseline. No runtime target validation. | [Evidence](evidence/34-line-zero-validation-public.png) |
| U20 Source guidance | PASS | 04:55:34 | Missing-source explanation identifies permissions or tags as possible causes and links Learn More; it does not claim fetched source. | [Evidence](evidence/36-source-unavailable-guidance-public.png) |
| U21 Template rejection and recovery | PASS | 05:06:52–05:38:08 | An actual unmatched brace disabled Start; blur added a red field outline. Correcting the brace enabled Start. Initial auto-balanced attempt excluded. | [Evidence](evidence/40-unmatched-brace-actual-public.png) |
| U22 Fixture file integrity | PASS | By 05:10 | Downloaded A pricing.py and app.py match the local baseline byte-for-byte; intended return target remains line 17. This is not Datadog source mapping. | [Evidence](EVIDENCE.md#fixture-integrity) |
| U23 Python Function draft | PASS | 05:39:50 | Function mode accepts Module pricing and Function calculate_quote as an enabled draft. No submit or entry/exit capture. | [Evidence](evidence/48-python-function-draft-public.png) |
| U24 Edited draft cancellation | PASS | 05:43 | Closing and reopening resets to Line mode and empty File/Line, retaining service/environment. No unsaved draft was published; reopened draft closed. | [Evidence](EVIDENCE.md#later-bounded-checks) |
| U25 Latest zero inventory | PASS | By 05:45 | After rejected creates and draft cancellation, All 0 / Active 0 / Inactive 0 remained. A-only installation unchanged; active lifecycle semantics untested. | [Evidence](EVIDENCE.md#later-bounded-checks) |
