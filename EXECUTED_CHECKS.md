# Supplemental executed checks

These are narrowly scoped observations within or alongside the 63 original cases. They are not additional full-case passes, and do not change the original-case denominator. A PASS is limited to the exact described check.

| Check | Result | UTC interval | Observed scope | Evidence |
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

No helper/locator failure is counted as a Datadog defect. Blind first-user timing, real captured values, active lifecycle, source mapping and repository-boundary checks remain blocked in the main ledger.
