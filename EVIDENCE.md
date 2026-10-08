# Evidence and checkpoint scope

The live-case ledger is frozen at 13:15:00 UTC with eight distinct findings. The offline ddtrace 4.11.0 verification finalized at 13:15:37 and was confirmed at 13:16:33 UTC; that separately dated addendum adds Medium FUNC02 without changing any original-case status. The combined report has nine distinct findings: 0 High, 4 Medium and 5 Low, with five remaining unconfirmed topics. See [FUNC02](findings/FUNC02-unbound-locals-serialized-as-null.md).

V9 evidence checkpoint: 8 October 2026 at 13:15:00 UTC. Frozen V8 ended at 10:50:59 UTC; its historical sections remain dated. Earlier sections are historical observations with explicit timestamps; their old blockers and zero-session inventory do not describe the current state. This remains an ongoing audit, not end-to-end completion.

## Checkpoint and gates

The initial and additional runtime approvals were received. The hosted synthetic baseline now has a registered debugger SDK client, actual numeric-template captures and a verified source match. The approved same-A-only reinstall repaired the interrupted source association. B remains private and never granted; discovery no-match is not a content-denial test. Independent role contexts and several controlled deployment/failure-injection variants remain unavailable.

Current cases: 16 PASS, 7 FINDING, 8 IN_PROGRESS, 8 PENDING and 24 BLOCKED, totaling 63. Nine distinct findings in the combined report: 0 High, 4 Medium and 5 Low. Five current unconfirmed topics remain outside finding totals. [Current status](CURRENT_STATUS.md) · [Case ledger](execution-ledger.json) · [Unconfirmed inventory](UNCONFIRMED_OBSERVATIONS.md).

G1 is established for the tested healthy baseline. G2 is established for A source retrieval and deployed-revision matching, with B still ungranted; the broader B retrieval boundary remains unproved. G3/G4 case-specific prerequisites must still be satisfied. Readiness, capture, source, access boundaries and cleanup are separate claims. The retained runtime/control/experimental assets are intentional; full cleanup is not certified.

The sections through “Template error feedback inspection” below preserve earlier evidence. Current continuation evidence follows under “Hosted readiness and environment” and later sections.

## Published public onboarding video

[Early onboarding excerpt](early-onboarding-excerpt.mp4) is 80 seconds of real motion capture, cropped to remove browser chrome, with captions and red outlines. Chapters: 00:00 overview; 00:20–00:34 permanent region choice; 00:34–00:58 documentation contents rail; 00:58–01:20 Python launch example. Source recording: 02:14:27–02:21:01 UTC, 393.7 seconds, 1364 × 1024 pixels, 20 fps. Edited offsets are not wall-clock times. This excerpt shows no successful runtime capture.

## Authenticated first run

03:21–03:24 UTC: empty service and environment states, manual entry, disabled Start, Close recovery, source-integration entry. Screenshots E10 at 03:21:54 and E13 at 03:23:59 are published with [UX02](findings/UX02-empty-state-recovery.md). The service image excludes the account greeting. No healthy service was established.

## Informed navigation and keyboard smoke

03:33–03:40 UTC: Home → APM intro → global search → Live Debugger navigation; actual 125% browser zoom; modal Tab focus, Escape and focus return; reset to 100%. This was informed navigation, not a blind beginner timing study. The first attempted zoom shortcut was ineffective and is excluded from evidence. At that timestamp, editor, long-path and field-validation behavior had not yet been established; later field checks are recorded separately.

## Empty session list controls

03:56–03:58 UTC: search, status, owner and date controls exercised with zero sessions. Status and owner filters persisted after reload; Clear Filter reset them. October 1–7 displayed correctly as a custom range. No populated-result correctness is claimed.

## Source integration pre install

03:59–04:00 UTC: custom setup showed organization-owner prerequisite and feature-to-permission explanations. Read Repository Contents described read-only functions with minimum Contents Read plus Push webhook; the visible custom draft dropdowns showed broader Read & Write defaults. Secrets access was described as names only. Official and custom drafts were canceled; reload still showed Not Connected. No effective grant or content retrieval was established. No App installation was submitted.

## Empty modal recovery

03:33–03:40 and 04:01–04:02 UTC: Close, Escape, Back, Forward, refresh and two open/Close cycles returned cleanly from the empty-service modal. Ctrl+Enter did not submit disabled Start. Attempts to fill an optional control failed in the test automation locator before input; those attempts are not product defects.

<a id="final-state"></a>

## Earlier final state at 04 12 UTC

04:12 UTC: live read-only accessibility inspection found All 0 / Active 0 / Inactive 0 with filters cleared. This check occurred after recording stopped and has no motion footage. No sessions/logpoints were created. Agent/sample processes were stopped by 03:39 UTC, and no App grant was submitted. Test accounts, the public audit repository and private fixture A are intentionally retained. At 04:22:42 UTC, two completed local setup helpers were stopped and each showed zero remaining owned processes. Private configuration was retained without inspection. Complete all-settings/account cleanup is not certified; C02 was blocked at that historical timestamp and is now IN_PROGRESS for full inventory reconciliation.

## Earlier authenticated recording boundaries

Authenticated source recording 4 ran 03:20:17–03:58:35 UTC, 2298.45 seconds, 1364 × 1024, 20 fps. Recording 5 ran 03:59:03–04:11:58 UTC, 775.30 seconds; useful UI activity ends around 04:02. Setup, publishing and idle time do not count as product-test time. Raw authenticated files contain browser/account metadata and are not published. The [181.30-second reviewed authenticated excerpt](authenticated-ui-qa-excerpt.mp4) is now available. See the [video catalog](VIDEOS.md) and [exact source/crop manifest](edited-video-manifest.md). The [historical safe archive](recordings/RECORDING_ARCHIVE.md) for sources 01–06 through 04:35:24 is available; later recording 07 remains separate.

A capture restart gap around 02:33 means GitHub account creation and the initial authenticated welcome are screenshot-only. No reconstructed account-creation footage is presented as original recording.

## Local reproduction

DOC01 was independently checked at 02:31:35 UTC with an inert script and again at 03:19:52 UTC with a guarded entrypoint, using Python 3.12.14. The invalid module invocation exits 1; both script and suffix-free module alternatives exit 0. Import-time code can execute before the invalid command errors. No Datadog SDK/Agent or telemetry was involved in these checks.

Local sample tests at 02:36 UTC: 8 passes and 1 intentional expected failure. Quantity 2 gives 2400 cents, quantity 3 gives 3600 rather than intended 3240, quantity 4 gives 4320. The planted boundary bug belongs to the demo application, not Datadog.

## Published supplemental screenshots

- [APM first-run introduction](evidence/17-apm-first-run-public.png): top 76 pixels removed to omit account greeting.
- [Global Live Debugger search](evidence/18-search-live-debugger-public.png): search-panel-only crop.
- [Verified 125 percent browser zoom](evidence/19-debugger-zoom125-public.png): top 40 pixels removed.
- [Modal at 125 percent zoom](evidence/20-logpoint-modal-zoom125.jpg): unchanged clean original.
- [Source-reading permission explanation](evidence/26-github-read-source-requirements.jpg): unchanged clean original.

Each image was visually reviewed after cropping. Remaining pixels match the actual source screenshot; no UI was generated or redrawn. [Supplemental executed checks](EXECUTED_CHECKS.md) provide exact scope.

## Authenticated edited motion

The authenticated excerpt shows real UI motion at normal speed. UX02 is visible at 00:00–00:13.80 and 02:42.80–02:50.80; manual entry at 00:13.80; keyboard recovery at 01:23.30; history recovery at 01:35.30; filters at 02:01.30; permission preview at 02:50.80. The [20.25-second account/setup excerpt](account-setup-excerpt.mp4) masks the test identity and omits OAuth screens. Neither video shows runtime capture or an installed SCI connection.

## Approved setup milestones

- 04:46:24: approved configured runtime launch. Agent/trace-agent 7.84.2, ddtrace 4.11.0 and Python 3.13.5.
- 04:47:03: safe status showed 31 synthetic requests, Remote Configuration query succeeded, organization enabled and key authorized, with no last error or startup failure.
- 04:48:02: additional LLM Observability intake destination interrupted the execution scope; no capture proved.
- 04:50:17: service became selectable (screenshot file 04:50:47).
- 04:51:29: [GitHub lists Datadog Official as installed](evidence/32-github-installed-a-only-public.png). This screenshot does not show repository scope.
- 04:54:47: narrowed runtime snapshot showed 32 requests and authorized RC after disabling EVP forwarding and LLM SDK/Agent flags. The additional destination boundary recurred at 04:54:55; no ongoing runtime or capture is claimed.
- 04:56:26: [Authorized GitHub Apps also lists Datadog Official](evidence/37-github-authorized-apps-public.png), marked Never used. This label alone does not establish the cause of failed association.
- 05:06:05: [Persisted repository selection shows one repository](evidence/38-a-only-after-b-created-public.png), verified privately as A. The account/repository identity is masked in the public image; B remains ungranted.

## Interrupted GitHub recovery

[SCI01](findings/SCI01-interrupted-github-recovery.md) records the scoped recovery failure. The authorization form had remained open about 75 minutes. The eventual callback reached the Datadog organization chooser; selecting the intended organization returned an unconnected Get Started page. Connect led back to existing installation settings with Save disabled. Fresh navigation via the official integration catalog and verification of the intended organization/site did not recover the association. No callback replay, app revoke or uninstall occurred in that original check. The later approved same-scope repair and fresh-install positive control are recorded below. Datadog UI build observed: 35.143254999.

## Draft validation after service discovery

- 04:53:17: [Wildcard environment warning](evidence/33-service-all-environments-warning-public.png) explains that an all-environment logpoint will not enable the service automatically and provides Configuration/specific-environment guidance.
- F06: pricing.py was added manually. 0, -1 and abc kept Start disabled. [Line 0 evidence](evidence/34-line-zero-validation-public.png), 04:54:43. [Line 9999](evidence/35-line-out-of-range-draft-public.png), 04:55:10, enabled an unsubmitted draft. Line 17 restored the target. That draft check did not test runtime installation. The later line-9999 runtime rejection is recorded below; relocation is not established.
- 04:55:34: [Source guidance](evidence/36-source-unavailable-guidance-public.png) states the file was not found and names permissions/tags as possible causes, with Learn More. No fetched source.
- F04: the first opening brace was automatically balanced, so it was not an invalid-input test. Deleting the closing brace produced QA quantity={quantity and [disabled Start](evidence/40-unmatched-brace-actual-public.png) at 05:06:52. [Correcting the template](evidence/41-valid-template-recovery-public.png) at 05:08:14 enabled Start. No submit occurred. Conditional-expression/runtime variants were untested at that timestamp; later valid predicate controls are recorded below, while invalid/non-Boolean variants remain pending.
- The earlier assessment that When was disabled was corrected by a normal supported click. In the healthy continuation the control is operable and actual predicates capture correctly. No conditional-control defect is asserted.

## Fixture integrity

Synthetic A pricing.py and app.py were downloaded through GitHub's raw-file control and compared byte-for-byte with the baseline. pricing.py is 1048 bytes, SHA-256 3414cf40e6c1a4cca691ec4fe9c9657c74edede5dcb66e907c9aaa09ddf17ed4. app.py is 2664 bytes, SHA-256 748a1032a072168fbe8fa61b8eb330a5eb07b182750dfcd572299f2b1e6b3128. Exact private repository/commit identities are retained for test attribution but are not public source-access proof. The intended pricing return remains line 17.

## Continuation recording and retained state

Genuine motion recording 07 began at 04:49:33 after the inbox and one-time code were closed. Installation and reauthentication before that are screenshot-only; no code was captured. Continuation originals are private; only reviewed crops/masks are published. [Screenshot provenance](evidence/runtime-privacy-provenance.md) gives UTC clocks, exact edits and hashes. The [recording 07 retained-section archive](recordings/continuation-07/CONTINUATION_RECORDING_ARCHIVE.md) and [edited highlights](recordings/continuation-07/highlights/CONTINUATION_HIGHLIGHTS.md) are now available with exact intervals and omissions.

Two baseline creation attempts were rejected at 05:15:51 and 05:19:57; the fresh unfiltered Sessions List showed All 0 / Active 0 / Inactive 0. No successful session/logpoint creation. The baseline and reopened drafts were later closed, as recorded below. A new complete session/resource inventory at continuation close is still required. Accounts, private A/B repositories and approved A-only GitHub installation are retained. The earlier zero-session/no-App-grant checkpoint must not be mistaken for the current setup state.

## Baseline submission attempts

05:15:51.407 UTC: baseline submit used the discovered service, the only offered wildcard environment, manually added pricing.py line 17, numeric template QA quantity={quantity} total={total_cents}, All variables capture and depth 3. The UI briefly showed loading, then a real transient toast: “Error creating logpoint: The instrumentation is not valid, please check your configuration.” The browser console recorded HTTP 400. [Actual first-attempt toast frame](evidence/submit-error-toast-public.png), raw07 offset 1579.5 seconds, and [plain-message rejection](evidence/44-plain-template-submit-result-public.png), screenshot file 05:19:58, preserve the visible message. A later accessibility snapshot missed the transient toast; this was not silent failure.

05:19:57 UTC: a plain QA baseline message with the same service/environment/file/line/capture settings produced the same visible error. No variable-template-specific cause is established. A fresh Sessions List with My sessions cleared and all filters reset showed All 0 / Active 0 / Inactive 0.

The draft's Go to Configuration link opened a new tab while retaining the draft. Live read-only page inspection reported no environments for the selected service and Source Code Integrations Not Connected. The first screenshot45 did not include the empty-state heading below the fold. [Screenshot46](evidence/46-settled-service-no-environments-public.png), captured 05:28:43 after recording 07 stopped 05:26:29, clearly shows the settled service-specific no-environments result. It is screenshot-only evidence; the purple graphic is the empty-state magnifier. Neither paused runtime nor missing source association is established as the cause of the server rejection. These are observed setup failures with unresolved prerequisites, not a claimed runtime-capture defect.

## Later bounded checks

- 05:38:08: after blur, the invalid template gained a red field outline while Start remained disabled. [Actual visual feedback](evidence/47-invalid-template-after-blur-public.png). Correcting the brace restored enabled Start; validation was not visually absent.
- 05:39:50: [Python Function-mode draft](evidence/48-python-function-draft-public.png) accepted Module pricing and Function calculate_quote. No function logpoint was submitted; entry/exit/context capture remains untested.
- 05:43: closing the edited Function draft and reopening New Session restored Line mode and empty File/Line, retaining service/environment. The reopened draft was closed. No unsaved draft was published; saved-entity persistence is untested.
- By 05:45: final observed unfiltered inventory remained All 0 / Active 0 / Inactive 0. The A-only installation was unchanged; the proposed reset was not performed.
- Personal Organizations settled at exactly one intended organization. Its initial zero count was a loading state, not a finding.
- Runtime source configuration explicitly supplies the intended service, staging environment and version 0.1.0. Static SDK registration/settings checks do not prove actual SDK registration or ingested environment tags; no wrong-flag explanation is inferred.

These checks are screenshot/live-inspection evidence after recording 07 stopped. Source 08 is 42.05 seconds of tooling preparation only; no reset footage. [Complete recorded-source catalog](VIDEOS.md).

## Historical APM ingestion and freshness

During this historical check the runtime stayed stopped. Widening an empty recent APM search recovered 47 indexed spans. An inspected GET /quote span from 04:54:43 UTC reports HTTP 200, language Python, env staging, version 0.1.0 and the baseline A commit. These are ingested tags, not merely configured metadata. [Indexed results](evidence/continuation-09/53-historical-search-47-spans.png) · [Actual version tag](evidence/continuation-09/56-screenshot-only-ingested-version.png) · [Actual env and commit](evidence/continuation-09/57-screenshot-only-ingested-env-commit.png).

The tag stills 56/57 were captured after source 09 stopped, and are not reconstructed into that motion. Image 54 shows a span overview, not the below-fold tags. Some UI time controls display UTC-07:00; report clocks are UTC. Historical APM ingestion proves neither current process liveness nor source retrieval or a debugger logpoint capture. No span-specific debugger action or Code Origin section was found in the inspected span view; this alone is not a feature defect.

[SDK Configurations](evidence/continuation-09/55-sdk-no-recent-config.png) explicitly states no configuration data detected in the last 15 minutes, with runtime, instrumentation telemetry and intake guidance. That freshness window is compatible with the stopped runtime. SDK Remote Configuration client registration was unverified at that earlier checkpoint. The later hosted registration and actual captures are separate evidence. Earlier broad “SDK readiness” wording should be read narrowly as local sample startup and Agent-side status, not registered debugger clients.

## Template error feedback inspection

At 06:25–06:28, an unmatched template disabled Start and gained a red border after blur. No text explaining that syntax error was observed in the view or recorded accessibility snapshot. The inspected textarea's error-related ARIA attributes were absent. Correcting the brace removed the border and enabled Start; no submission occurred. [UX03](findings/UX03-invalid-log-template-feedback.md) records this Low scoped feedback issue and its positive control. A Line naming concern remains provisional, because the archived attributes do not establish the computed name. No screen-reader run or global WCAG conclusion is claimed.

Source09 historical APM motion and source 10 feedback motion have separately reviewed archives/highlights. All ten recorded sources are accounted in [VIDEOS.md](VIDEOS.md). Source10 ended 06:28:13.75; the draft was closed and no session/logpoint was created. The runtime and source-association blockers were unchanged at that historical cutoff; the later continuation below supersedes them.


## Hosted readiness and environment

At 09:20:37.055 UTC the hosted synthetic runtime reported a running sample, synthetic requests, authorized Agent Remote Configuration and one matching Python SDK client registered for LIVE_DEBUGGING and LIVE_DEBUGGING_SYMBOL_DB. This is a bounded readiness observation, not capture proof. [Safe field-only derivative](evidence/continuation-11/hosted-readiness-20261008T092037Z.json) · [SDK registration screenshot](evidence/continuation-11/62-runtime-sdk-registration-safe.png) · [Staging available](evidence/continuation-11/63-staging-environment-available-safe.png).

The deployed source SHA is `f5061500e8bf30880aebcf7966ba64df44d2ccde`. A later manual runtime handover preserved the baseline; subsequent actual snapshots establish continuing capture separately. [Later registered runtime](evidence/continuation-12/78-continuation-runtime-registered-safe.png) · [Post-handover capture](evidence/continuation-12/79-post-handover-control-capture-safe.png).

## Recorded first success

Source 11 records the first successful manual submission around 09:28:14.9, the initial instrumenting/Enable logs state, populated Logs around 09:29:43, session events after reload around 09:30:01 and first visible quantity-three locals at 09:31:17.100. No Logs setting change occurred. These times include operator navigation and waiting; they are not an ingestion-latency benchmark or a blind first-user study.

Quantity-three locals showed subtotal 3600, eligibility False, discount 0 and total 3600. The quantity-two comparison at 09:36:41.750 showed total/subtotal 2400 and discount 0. The planted quantity-three application bug is not a Datadog defect. [First locals screenshot](evidence/continuation-11/67-verified-quantity-three-red-outlines.png) · [Quantity-two screenshot](evidence/continuation-11/69-verified-quantity-two-safe.png) · [Source 11 highlight chapters](recordings/continuation-11/highlights/CONTINUATION_HIGHLIGHTS.md).

The duration menu displayed 1 Hour, 1 Day, 2 Days and 1 Week. This establishes only the displayed menu, not a universal product/API minimum. [Duration screenshot](evidence/continuation-11/68-session-duration-menu-safe.png).

## Verified numeric baseline

F01 is PASS for `pricing.py:17` in staging using `QA quantity={quantity} total={total_cents}`, All variables, depth 3. The full numeric-template and actual-local controls were observed at 10:03:50.811 (quantity 3), 10:04:08.659 (quantity 2) and 10:04:21.432 (quantity 4):

| Quantity | Subtotal | Eligible | Discount | Total |
|---|---:|---|---:|---:|
| 2 | 2400 | False | 0 | 2400 |
| 3 | 3600 | False | 0 | 3600 |
| 4 | 4800 | True | 480 | 4320 |

[Quantity 3](evidence/continuation-12/73-numeric-template-quantity-3-safe.png) · [Quantity 2](evidence/continuation-12/74-numeric-template-quantity-2-safe.png) · [Quantity 4](evidence/continuation-12/75-numeric-template-quantity-4-safe.png) · [Normalized safe controls](evidence/continuation-12/f01-numeric-capture-controls.json).

The derivative distinguishes observed UTC from UI navigation timestamp parameters. Those parameters are not assumed to be execution times. Earlier wildcard HTTP 400 attempts remain historical; their cause is not proved by the later successful specific-environment baseline.

## Verified source association recovery

After a fresh retry preserved the interrupted-flow failure, an approved same-A-only uninstall/reinstall removed the old installation around 09:49, completed fresh authorization around 09:54 and reached connected configuration around 09:55. B remained ungranted. [Connected screenshot](evidence/continuation-11/71-source-integration-installed-safe.png) · [SCI01 detailed recovery](findings/SCI01-interrupted-github-recovery.md#verified-same-scope-recovery).

The approximately 75-minute pause is a recorded precondition, not a proved cause. Source 11 stops at 09:53:41.25, before final authorization and callback; their completion is screenshot-only. C03 is PASS only for the documented invocation workaround and controlled association repair with subsequent actual capture/source checks. It does not certify all bugs fixed.

## Verified deployed source

A real control event has `debugger.snapshot.timestamp` 1791455041812, corresponding to 10:24:01.812 UTC. The [snapshot JSON screenshot](evidence/continuation-12/82-control-snapshot-execution-timestamp-safe.png) directly shows that SDK timestamp; identifying values and private prefixes are masked.

Datadog source was visible beside the captured event. The rendered provider link was followed at 10:25:48 to repository A, deployed revision `f5061500e8bf30880aebcf7966ba64df44d2ccde`, `pricing.py` line 17. All 24 source lines and the nearby arithmetic/return keys matched the unchanged deployed oracle. The older `78457e9` file last-change commit is distinct from the selected deployed revision.

[Datadog source/stacktrace](evidence/continuation-12/80-control-source-stacktrace-safe.png) · [Followed provider source](evidence/continuation-12/81-linked-revision-pricing-safe.png) · [Screenshot captions and provenance](evidence/continuation-12/README.md).

S02 is PASS for this event/revision/file/line/content comparison only. Other revisions, path variants and B private-content denial remain separate tests.

## Out-of-range runtime control

The isolated `pricing.py:9999` probe was submitted at 10:29:40 and became ERROR by 10:30:21. At 10:31:26 its detail reported 1/1 instances and `NoFunctionsAtLine`. A normal line-17 gutter click created a separate probe at 10:32:04; it received events by 10:32:29 and later predicate captures confirmed actual locals.

[Invalid target before submission](evidence/continuation-12/83-out-of-range-before-submit-safe.png) · [Runtime error](evidence/continuation-12/84-out-of-range-runtime-error-safe.png) · [Separate valid recovery](evidence/continuation-12/85-valid-line-recovery-events-safe.png).

F06 remains PENDING because blank/comment-line branches are untested. A marker near the file end does not prove runtime relocation. The error and recovered probe are separate identities, not a claim that the invalid probe was repaired in place.

## Conditional capture controls

`quantity == 3` with COND3 was applied at 10:33:25. Nine observed post-activation rows from 10:33:33–10:34:01 showed quantity 3; actual locals matched subtotal/total 3600, false eligibility and discount 0.

`quantity == 4` with COND4 was applied at 10:35:03. Six rows from 10:35:19–10:35:38 showed quantity 4; actual locals matched subtotal 4800, discount 480, true eligibility and total 4320. The previously selected COND3 capture gained OUTDATED feedback while new COND4 rows arrived.

[COND3 apply](evidence/continuation-12/86-condition-three-before-apply-safe.png) · [Quantity-three capture](evidence/continuation-12/87-condition-three-captured-safe.png) · [OUTDATED old capture](evidence/continuation-12/88-condition-revision-outdated-capture-safe.png) · [Quantity-four capture](evidence/continuation-12/89-condition-four-captured-safe.png).

F02 is PASS for these controls. Row times are UI event-list observations, not independently established execution timestamps. Ordinary click interaction corrected the earlier disabled-When assessment; no product finding is based on that assessment.

## No match and recovery

`quantity == 101` with NOMATCH was applied at 10:36:32. At 10:37:55 the definition remained 101, there were zero observed NOMATCH rows and the UI said Captured 1m ago. Independent baseline 2/3/4 rows continued through 10:37:50. Old COND4 rows remained identifiable. This is a bounded observation, not an exhaustive indexed-backend query.

The condition was removed and RECOVER applied at 10:38:25. New rows resumed at 10:38:39.866 (quantity 3), 10:38:41.278 (quantity 2) and 10:38:46.537 (quantity 4), with expected totals. F03 is PASS for the tested no-match interval and recovery.

[No-match state](evidence/continuation-12/91-no-match-retained-old-events-safe.png) · [Recovered rows](evidence/continuation-12/92-condition-removal-recovery-events-safe.png).

## Repository boundary limit

A-only grant and actual A source retrieval are verified. Searching the ungranted B repository in the source picker returned no match. [Discovery screenshot](evidence/continuation-12/90-repository-b-discovery-no-match-safe.png).

S03 remains PENDING: discovery absence does not prove denied private-content retrieval. The exact never-granted B file/commit request through a supported route has not been established. B has never been granted; no permission-enforcement pass or security failure is inferred.

## Source value explanation

The captured quantity-three values and actual Datadog source `quantity > 3` explain the planted bug: false eligibility, discount 0 and total 3600. Tested snapshot/session context survived Logs/provider visits and return. [Source beside quantity-three values](evidence/continuation-12/95-source-branch-quantity-three-safe.png).

View in Logs twice opened a requested-event-not-indexed pane, around 10:25 for the control and at 10:41:47 for the target. In each case a row click recovered the event and the exact requested snapshot ID, probe and SDK timestamp matched the recovered indexed-row JSON. [UX04 Low finding](findings/UX04-view-in-logs-event-link.md).

The [annotated screenshot 94](evidence/continuation-12/94-view-in-logs-not-indexed-outlined.png) shows the error and query context only. Its matching row/count is obscured. Identity comparison and row-click recovery are separate interaction/payload observations; no root cause, internal-navigation-encoding explanation or data-loss claim is made.

## Verified expiry and control

F11 and X04 pass for this bounded expiry alternative:

- 10:45:35.975: target observed ACTIVE with 1 second left.
- 10:45:50.640: first observed INACTIVE/EXPIRED, bounding the observed UI transition within 14.665 seconds.
- 10:45:41.045: last target SDK snapshot timestamp, distinct from its 10:45:43.820 UI log-row time.
- 10:47:16.596: no newer target rows observed; retained history still available.
- 10:47:30.402: independent later-expiring control's SDK snapshot timestamp, with quantity-four locals matching 4800/480/4320 and true eligibility.
- 10:49:21.580 reload and a fresh direct link around 10:50: expired state and history persist.

[Expired state](evidence/continuation-12/99-target-inactive-expired-safe.png) · [Live control](evidence/continuation-12/100-active-control-after-target-expiry-safe.png) · [Reload](evidence/continuation-12/101-expired-target-after-reload-safe.png) · [Direct link](evidence/continuation-12/102-expired-target-direct-link-safe.png) · [Safe timing derivative](evidence/continuation-12/expiry-timing-observations.json).

No exact internal deadline, instantaneous stop or precise propagation lag is inferred. The last target snapshot falls inside the bounded observation interval, not after a proved internal stop. Screenshots, rendered-UI reads and payload timestamp checks are separate evidence types. Source 12 foreground motion is partly obscured by a context menu. The target active-to-expired transition is not visible in the desktop movie; an already-expired after-state is retained. The screenshots, rendered-UI reads and payloads establish the bounded transition and are not substituted into the video.

At the V8 cutoff, the expired original target was not a zero-session cleanup result; later control/experimental sessions remained intentional test assets. V9 adds the explicit-resume/stop and hierarchy controls below. Broader lifecycle variants and final settings/runtime/grant reconciliation remain open.

## Public evidence and media provenance

[Continuation 11 reviewed stills](evidence/continuation-11/README.md) and [continuation 12 reviewed stills](evidence/continuation-12/README.md) include image-level crops, opaque masks, hashes and separately disclosed annotations. No UI is reconstructed; raw journals and raw setup logs are not public artifacts.

Sources 01–12 finalized local package totals: 233:02.05 recorded, 157:48.50 retained, 75:13.55 withheld; 21 archive MP4s. Eight highlights total 18:57.75, overlapping archive footage. Source 12 is 50:50.85 recorded, 40:03.20 retained and 10:47.65 omitted; its complete safe archive is publicly verified at commit `7cdd468`, while the four highlight-package files remain pending publication verification. [Video catalog](VIDEOS.md).

## V9 reviewed evidence and publication boundary

This checkpoint includes four frozen safe-still packs: 103–116 (44 allowlisted files), 117–125 (29), 126–131 (20) and 132–135 (20), totaling 113 files. Their 109 checksum entries were independently rechecked before copying. Pixel crops/masks, annotations and scope limitations remain documented in the unchanged manifests. No raw screenshots, credentials, private account routes or internal review files are publication inputs.

[103–116 manifest](evidence/continuation-13/manifest.json) · [117–125 manifest](evidence/continuation-13/fixtures-117-125/manifest.json) · [126–131 manifest](evidence/continuation-13/locals-126-131/manifest.json) · [132–135 manifest](evidence/continuation-13/two-tab-132-135/manifest.json).

These files and V9 text are prepared locally; their public availability is not yet verified. Function/disable/hierarchy observations from later stills are attributed prose until separately reviewed safe derivatives are available. Source 13 is ongoing motion, not a finalized media package. Counts stop at 13:15:00 UTC even if work continues afterward.

## Explicit resume and stop

F12: **PASS**. The previously expired session was explicitly resumed at 11:29:26 UTC. The session and probe identities were preserved, the recorder observed a fresh one-hour duration, and safe still 104 shows ACTIVE with 59 MINUTES LEFT and actual quantity 2 locals totaling 2400. The independent SDK payload timestamp check independently records a new capture at 11:29:48.334 UTC. The session was explicitly stopped at 11:30:21 and the recorder verified INACTIVE/DISABLED after reload around 11:31:40. Historical rows remain available.

The original expired-session re-enable flow, preserved identity, renewed duration, fresh capture and disable-again cleanup are supported. Prior V8 reload/direct-link checks and safe 103 establish that page navigation alone had not reactivated the expired target. This PASS does not establish an exact backend deadline or instantaneous stop.

[Reviewed still 103](evidence/continuation-13/103-expired-session-before-resume-safe.png) · [Reviewed still 104](evidence/continuation-13/104-resumed-session-active-capture-safe.png) · [Reviewed still 105](evidence/continuation-13/105-resumed-session-inactive-disabled-safe.png).

Cleanup: Case-specific cleanup complete as observed after reload around 11:31:40 UTC. This is not an all-session or runtime cleanup claim.

## Condition validation and recovery

F04: **FINDING**. The remaining malformed-condition controls were executed separately: quantity == and bare quantity showed validation marks/red-field feedback and the recorder observed disabled Apply with Fix validation errors before saving. Correcting to quantity == 2 was applied at 11:36:30 UTC, followed by VALID2 quantity=2 rows from approximately 11:36:53. The unmatched-template rejection and valid correction were already executed in V8.

All original functional input variants now have a supported rejection/correction result. FINDING retains the existing LOW UX03 explanation/accessibility-feedback issue associated with the unmatched-template variant; it does not mean condition validation failed. No new finding or severity count is added.

[Reviewed still 106](evidence/continuation-13/106-invalid-condition-draft-safe.png) · [Reviewed still 107](evidence/continuation-13/107-nonboolean-condition-validation-safe.png) · [Reviewed still 108](evidence/continuation-13/108-valid-condition-correction-events-safe.png).

Cleanup: Invalid draft inputs were replaced by a valid condition, and later F05/F16 revisions superseded the experiment. A global stop of the experimental session is not established; C01 remains open.

## Missing name and definedness

F05: **PASS**. Referencing missing_qa_value in the log message produced ERROR and an Evaluation errors panel naming No such local variable with an Edit Logpoint recovery path. Replacing the expression with isDefined(missing_qa_value) rendered False without that error panel. The subsequent control containing isDefined(quantity) rendered present=True, while the missing-local check remained False and quantity=2.

The requested absent-reference, definedness-false and available-local positive controls are all observed. Missing data is distinguishable from the Boolean False result. The exact edits are attributed to recorder chronology, while safe 109/110/112/114 directly show their rendered outcomes. This verdict is restricted to the original exact nonexistent-name/definedness/available-local controls; later unassigned, deleted and branch-only locals are a separate semantic-review candidate and do not broaden this PASS.

[Reviewed still 109](evidence/continuation-13/109-missing-local-actionable-error-safe.png) · [Reviewed still 110](evidence/continuation-13/110-definedness-false-recovery-safe.png) · [Reviewed still 112](evidence/continuation-13/112-message-only-explanation-safe.png) · [Reviewed still 114](evidence/continuation-13/114-capture-restored-locals-safe.png).

Cleanup: The direct missing-local expression was superseded by valid definedness expressions and capture continued. Final disabling of the shared experimental session is still part of C01; it is not claimed here.

## Variable capture toggle

F16: **PASS**. Variable capture was turned off and applied at 11:42:14 UTC. New MESSAGE_ONLY events retained the rendered message but showed Logpoint does not contain debugging information rather than a captured-locals panel. Capture was re-enabled at 11:43:25. The selected older message-only event was marked OUTDATED with guidance that future logs would contain variables. A subsequent event had actual quantity-two locals again.

The original off/apply/new-event/on/new-event sequence is supported. Historical event semantics are explicit: old message-only captures were not represented as retroactively gaining variables, and a newer capture displayed locals.

[Reviewed still 111](evidence/continuation-13/111-message-only-definition-safe.png) · [Reviewed still 112](evidence/continuation-13/112-message-only-explanation-safe.png) · [Reviewed still 113](evidence/continuation-13/113-capture-reenabled-future-logs-guidance-safe.png) · [Reviewed still 114](evidence/continuation-13/114-capture-restored-locals-safe.png).

Cleanup: Capture variables was restored, satisfying the case-specific restore-or-disable cleanup. Shared experimental-session shutdown remains open under C01.

## Function exit and line context

Still 116 shows the earlier quantity-three exit capture and four visible return entries. The later complete quantity-four return-object check and line-context error are recorder-observed results; that earlier still is not offered as a picture of the later controls. Safe derivatives of those later states remain pending.

F07: **IN_PROGRESS**. A whole-function pricing.calculate_quote probe using FUNCTION returned={@return} renders a full quantity-four return dictionary: quantity 4, unit price 1200, subtotal 4800, eligibility True, discount 480 and total 4320. The pane is labeled Values on exit. Applying @return in a line-17 message instead produces an explicit Evaluation errors panel naming No such local variable: @return, with editing guidance; the recorder verifies accurate quantity-two locals totaling 2400. No explicit entry/exit selector was found in the tested manual editor, and entry capture was not executed.

Default function-exit capture, a full returned-value positive control and the method-only contextual return expression’s explicit line-context error are now supported. This advances the original context matrix, but no entry-mode control ran. The absence of a selector in the inspected editor is an unresolved availability branch, not proof that entry is unsupported everywhere. Keep IN_PROGRESS rather than imply an entry/exit comparison was completed.

[Reviewed still 115](evidence/continuation-13/115-function-logpoint-draft-safe.png) · [Reviewed still 116](evidence/continuation-13/116-function-exit-return-capture-safe.png).

Remaining scope:
- Resolve entry-capture support for the available manual editor/runtime. If supported, execute the original entry control and verify that yet-unassigned locals are not fabricated; otherwise document a verified supported limitation.
- Complete the required entry-versus-exit comparison only if an entry route exists; do not relabel the observed default exit as entry.

Cleanup: OPEN: no final stop/removal of the separate function-return and line-context experiments is established by the F13 stop of the shared complex-fixture session. C01/C02 remain open.

## Complex object display

F22: **IN_PROGRESS**. Real run-3 complex-fixture events are captured. Typed empty list and map are visible with size 0. The recorder additionally verifies exact Unicode content and left.leaf=11 versus right.leaf=22. Nested and cyclic structures can be expanded; a long synthetic string is visible in clipped form. Bounded cycle/depth semantics remain unresolved.

The old prepared-local-only deployment blocker is obsolete because the fixture now executes and produces actual captures. The original case remains incomplete: observed expansion and values do not establish full long-string truncation/recovery, search/collapse behavior, explicit depth/cycle handling or cleanup.

[Reviewed still 117](evidence/continuation-13/fixtures-117-125/117-complex-fixture-captured-safe.png) · [Reviewed still 118](evidence/continuation-13/fixtures-117-125/118-nested-leaf-display-safe.png) · [Reviewed still 119](evidence/continuation-13/fixtures-117-125/119-cycle-fixture-expanded-view-safe.png).

Remaining scope:
- Inspect the long string beyond its clipped preview; verify the full value or explicit size/truncation explanation without treating a partial preview as complete.
- Complete and record expand/collapse/search behavior for the required collections and nested values.
- Establish bounded cyclic structure handling and any depth/truncation explanation; current nested self expansion does not establish termination or truthful completeness.
- Verify responsiveness during the required interaction sequence and distinguish any capture-depth limit from the rendered tree behavior.

Cleanup: OPEN: disable the complex-fixture experiment and revert/remove the fixture variant when authorized dependent tests are complete. No final restoration is established. Later F13 verifies whole-session stop of the shared fixture session at 13:13:55, but does not itself establish fixture/runtime removal or every case-specific direct-link inventory check.

X07 remains IN_PROGRESS: Unicode content and distinct nested leaves do not cover every key/value combination or sensitive children under a non-sensitive parent. Unicode content and the clipped right leaf 22 are recorder-attributed, not fully pictured. Repeated self expansion does not establish unbounded behavior or a defect.

## Targeted redaction controls

F21: **PASS**. At the real run-3 synthetic fixture line 32, event details in Targeted mode show numeric_control=90210, bool_control=True and harmless_text=plain synthetic text. The dummy accessToken and password fields remain visible as string types and credentials as a dictionary type, without their values. Expansion gives an explicit name-based-redaction explanation. The recorder reports that protection was not lowered.

The original synthetic-control redaction behavior is now executed: benign controls are readable, sensitive-name fields are explicitly redacted rather than silently missing, and the configured Targeted mode remains in effect. This is a behavioral PASS for the tested names and fixture, with required experiment removal still open under C01/C02 and reviewed safe derivatives now available. It is not a general proof of redaction at every nested depth or across protection modes.

[Reviewed still 120](evidence/continuation-13/fixtures-117-125/120-targeted-redaction-controls-safe.png) · [Reviewed still 121](evidence/continuation-13/fixtures-117-125/121-targeted-name-redaction-explanations-safe.png).

Cleanup: OPEN: removing/disabling the redaction logpoint and restoring/removing the extra fixture has not been established. The behavioral PASS does not close original cleanup or global C01/C02. Preserve normal redaction. Later F13 verifies whole-session stop of the shared fixture session at 13:13:55, but does not itself establish fixture/runtime removal or every case-specific direct-link inventory check.

The password explanation is below the visible area of still 121 and remains recorder-attributed. The still records observed Targeted mode, not a history of settings changes.

## Sampled overlapping request association

X06: **PASS**. Two sampled executions from the deployed overlapping-request fixture are associated correctly across captured locals, indexed Logs identity, request trace and source link. Sample A is pair 41/index 101, quantity 2/total 2400, overlap_confirmed=True, SDK time 12:23:34.913 UTC. Sample B is pair 53/index 202, quantity 4/total 4320, overlap_confirmed=True, SDK time 12:32:41.298 UTC. The recorder verified each indexed Logs snapshot identity and matching per-sample trace correlation, expected GET request, status 200, version 0.2.0 and the same deployed-revision source link at the intended concurrency line 79. Both samples belong to the same intended probe/session.

PASS for the original overlapping-request snapshot-association checks as sampled: each inspected snapshot has internally consistent request-specific values, trace context and deployed-revision source-link association. The samples are from different pair indices; they do not form a completely collected concurrent pair, and no exhaustive concurrency or all-request isolation result is claimed. Actual capture clears the obsolete prepared-local-only blocker. Traffic/fixture cleanup remains open; reviewed safe derivatives are now available.

[Reviewed still 122](evidence/continuation-13/fixtures-117-125/122-concurrent-sample-a-pair-41-safe.png) · [Reviewed still 123](evidence/continuation-13/fixtures-117-125/123-concurrent-sample-b-pair-53-safe.png) · [Reviewed still 124](evidence/continuation-13/fixtures-117-125/124-concurrent-sample-a-trace-context-safe.png) · [Reviewed still 125](evidence/continuation-13/fixtures-117-125/125-concurrent-sample-b-trace-context-safe.png).

Cleanup: OPEN: stop bounded traffic and remove/disable the temporary concurrency probe/fixture when dependent QA is complete. The accidentally added adjacent-line probe is disabled and excluded; this does not establish final session/runtime cleanup. C01/C02 remain IN_PROGRESS. Later F13 verifies whole-session stop of the shared fixture session at 13:13:55, but does not itself establish fixture/runtime removal or every case-specific direct-link inventory check.

Exact indexed identity, full trace metadata and provider-link association are recorder-attributed. The supplied SDK milliseconds were independently converted to UTC; these times are distinct from displayed event headings. Screenshots do not expose every claimed field. The two samples are more than nine minutes apart and never represented as a matched concurrent pair.

## Never called installation control

X03: **IN_PROGRESS**. A probe targeting the never-called function at line 69 was created around 12:43 UTC. At the recorder check 12:54:53 it remained WAITING FOR EVENTS with one instance and zero events, while called siblings had fresh events. Reviewed stills 129 directly shows that waiting/no-events state. The earlier line-9999 controlled target had reported ERROR/NoFunctionsAtLine. The final healthy-function invocation has not been executed.

Actual creation and the bounded no-traffic observation clear the obsolete prepared-local-only blocker. The displayed waiting state differs from the earlier controlled installation-error state, but WAITING FOR EVENTS and an instance count are not explicit installation-success evidence. The required final invocation and resulting actual event remain untested, so this is partial progress only.

[Reviewed still 129](evidence/continuation-13/locals-126-131/129-never-called-waiting-for-events-safe.png).

Remaining scope:
- Resolve the never-called probe template before invoking it: the pictured template references quantity, which is not an in-scope local/parameter of the inspected never-called fixture function. Use a valid fixture-local or literal message to avoid confounding the positive control.
- Inspect available runtime/installation detail; do not promote WAITING FOR EVENTS or one instance into explicit installed/healthy proof.
- Execute the healthy function once through an authorized supported route and verify the actual captured event against the fixture oracle.
- Complete the state comparison after that positive event, keeping the earlier line-9999 error’s separate runtime/context and observation time explicit.

Cleanup: OPEN: disable the never-called test definition and verify the failed-installation definition remains disabled/expired. No final all-session cleanup or positive invocation is established. Later F13 verifies whole-session stop of the shared fixture session at 13:13:55, but does not itself establish fixture/runtime removal or every case-specific direct-link inventory check.

## Two tab unsaved draft loss

F09: **FINDING**. Medium FUNC01: in two tabs editing the same logpoint, stored quantity == 4 remains the baseline. Tab B changes its unsaved predicate to quantity == 3 and is dirty. Tab A saves only a message-template edit. B’s rendered predicate silently resets to quantity == 4 and its Apply action becomes disabled, with no visible warning/conflict text. This loss of the unsaved draft was reproduced around 13:01 and again at 13:02:52 UTC; the second repetition changes the saved message from TAB_A2 to TAB_A3.

A reproducible unsaved-draft loss is established in the two-tab branch, so F09 is FINDING with Medium FUNC01. The stored quantity-four predicate remains correct. This does not establish a conflict between two saved writes, backend capture corruption, wrong active predicate or completion of the original stale-save/reload/new-event matrix.

[FUNC01 finding and annotated before/after](findings/FUNC01-unsaved-condition-reset.md).

Remaining scope:
- Execute the original branch in which stale tab B actually submits a different-field change after tab A saves; do not substitute unsaved-draft loss for conflicting saved-write behavior.
- Reload both tabs and inspect the final accepted definition and any conflict/last-write explanation.
- Capture new events after the final saved state and verify their actual active definition and values.
- Restore the baseline or disable the test experiment, and verify final cleanup.

Cleanup: OPEN: no final baseline restoration, test disable or global cleanup is established for the two-tab experiment. C01/C02 remain IN_PROGRESS.

## Individual disable and draft Apply

F10: **IN_PROGRESS**. During the 13:04:34–13:05:38 UTC recorded interval, tab A disabled the individual line-63 probe while tab B already had an unsaved message draft. Both tabs displayed DISABLED. Tab B retained an enabled Apply button; applying the draft re-instrumented the probe and a fresh STALE_EDIT quantity-four log row appeared. No session-wide or service/environment-wide disable was tested.

The individual-probe stale-draft branch has now executed and clears the no-result state. Applying a modification to a disabled probe produced renewed collection, but the available documentation does not explicitly define disabled-edit semantics. Treat reactivation-feedback as UNCONFIRMED rather than another finding. Reload and the stale session-level child-edit branch remain unfinished. The shared session was separately stopped under F13 at 13:13:55; global cleanup remains open.

Remaining scope:
- Reload both tabs and inspect the accepted enabled/disabled state and definition.
- Select the new STALE_EDIT capture and inspect its own details/identity; the existing screenshot details pane is an OUTDATED older BRANCH result.
- Repeat the original session-level disable with a child logpoint and inspect parent/child behavior.
- Resolve the intended disabled-edit contract and assess whether the Apply action clearly communicates renewed collection before deciding on a product finding.
- After executing any remaining stale session-edit branch, restore and re-verify final inactivity; do not substitute F13’s explicit Enable path for that branch.

Cleanup: The affected shared session was finally stopped under F13 at 13:13:55, with the line-63 target and checked sibling children disabled. That scoped final state is now established, but the F10 reload and stale session-level child edit branch remain untested. Global inventory remains under C01/C02.

[Official Datadog documentation](https://docs.datadoghq.com/tracing/live_debugger/#creating-logpoints) permits instrumentation after modifications generally but does not expressly resolve disabled-edit semantics. The older OUTDATED details pane does not establish the new row’s payload. No new finding, security conclusion or service/environment disable result is inferred.

## Individual and session hierarchy

The final 13:13:55 stop is recorder-attributed. The captured earlier stop at 13:11:44 is not relabeled as the final stop. The 13:13:17.602 capture time below is a displayed UI row time, not an independently verified SDK execution timestamp.

F13: **PASS**. The sibling/session hierarchy sequence completed before cutoff: line 44 was disabled at 13:10:25 while 54/63 continued capture; the whole session was stopped at 13:11:44 and both tabs showed INACTIVE/DISABLED. Explicit Enable logpoint for line 44 at 13:12:18 made the aggregate session ACTIVE while 54/63 remained DISABLED. A new line-44 event was displayed at 13:13:17.602. Final whole-session stop at 13:13:55 was verified as INACTIVE with 44/54/63 DISABLED.

PASS for the observed individual-disable, whole-session stop, explicit child re-enable and sibling-state sequence, with case-specific whole-session cleanup. The enabled child resumed capture without reactivating checked siblings. Aggregate ACTIVE following explicit child enable is consistent with the observed hierarchy. This is not the F10 stale session-level edit branch or a service/environment Disable test.

Cleanup: COMPLETE for this shared session as recorder-verified at 13:13:55: INACTIVE, with checked children 44/54/63 DISABLED. Other sessions/runtime/fixtures remain under C01/C02; no global cleanup claim.

## Local value semantics

The caught-exception control shows typed error/control fields in a real capture. The quotient-null row is not pictured in still 126 and is recorder-attributed; exception-object internals and complete stack behavior are unproved. Unassigned/deleted and branch-only local rows display null, while assigned controls show 42 and 404. At the live cutoff, exact indexed payload/component interpretation was still needed before assigning a defect. The later offline-verification addendum below establishes the tested SDK defect; hosted transport attribution remains unverified. F05's original nonexistent-name and definedness PASS is not altered.

[Caught-exception capture](evidence/continuation-13/locals-126-131/126-caught-exception-locals-safe.png) · [Unassigned/deleted display](evidence/continuation-13/locals-126-131/127-unassigned-deleted-locals-display-safe.png) · [Assigned control](evidence/continuation-13/locals-126-131/128-assigned-local-positive-control-safe.png) · [Branch-unbound control](evidence/continuation-13/locals-126-131/130-branch-unbound-display-control-safe.png) · [Branch-assigned control](evidence/continuation-13/locals-126-131/131-branch-assigned-display-control-safe.png) · [Later FUNC02 verification](findings/FUNC02-unbound-locals-serialized-as-null.md).

## Remaining cleanup inventory

The resumed original target was stopped and reloaded inactive earlier. The shared complex-fixture session completed F13’s final whole-session stop at 13:13:55 and checked children 44/54/63 were disabled. Separate function-return/line-context experiments and the full global session/probe/runtime inventory are not yet established as cleaned up.

One target cleanup is confirmed; there is no reconciled final all-session/logpoint inventory, final active count, or final post-stop traffic check. Do not claim that all capture is stopped.

Several case-specific capture stops are verified, including the shared fixture session’s final F13 stop at 13:13:55. Runtime/traffic, fixture removal, source grants, settings and identity restoration have not received a complete before/after inventory; separate function/line-return experiments remain unclosed.

No final runtime/settings/grant restoration can be inferred from a stopped individual session or from a recording file. Preserve the full inventory task.

C01/C02 remain IN_PROGRESS. The later session stop is a scoped result, not an all-environment cleanup certificate. Preserve the original cleanup requirements in the 63-case ledger. No post-cutoff result is incorporated into the original-case outcomes above; the separately dated addenda follow below.

## Offline verification addendum after 13:15 UTC

An actual installed ddtrace 4.11.0 package reproduction finalized at **13:15:37 UTC** and was confirmed at **13:16:33 UTC**. Unbound and deleted names absent from frame locals serialize through the measured helpers as NoneType/isNull, identically to explicitly assigned None. Definedness is false for the missing names and true for explicit None; numeric assigned controls remain correct. This establishes [Medium FUNC02](findings/FUNC02-unbound-locals-serialized-as-null.md) for the tested SDK/version. The hosted transport capture payload was not inspected, so the hosted transport path and any independent UI cause are not declared established.

[Result](evidence/sdk-locals-4.11.0/result.json) · [Reproduction](evidence/sdk-locals-4.11.0/reproduce.py) · [Version-tagged source provenance](evidence/sdk-locals-4.11.0/source-provenance.json) · [Portable offline command](evidence/sdk-locals-4.11.0/run-offline.sh).

The frozen live ledger remains 16 PASS, 7 FINDING, 24 BLOCKED, 8 PENDING and 8 IN_PROGRESS. The combined findings become nine (0 High, 4 Medium, 5 Low); the current unconfirmed inventory becomes five. The separate SDK check does not change original F05 or retrospectively convert live U51 into a pre-cutoff confirmation.

## Later unscored cleanup and recording status

At **13:17:59 UTC**, the session inventory with **My sessions enabled** showed **All 4 / Active 0 / Inactive 4**. This is a later status observation, not evidence available at the live cutoff. C01/C02 remain as originally scored at 13:15; runtime/traffic, fixture, settings and grant reconciliation are not proved by the zero-active session list alone. Source 13’s raw recording was subsequently finalized. Its exact duration, reviewed retained/withheld coverage and motion export are not established here.
