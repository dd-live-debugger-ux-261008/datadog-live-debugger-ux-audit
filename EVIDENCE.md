# Evidence and checkpoint scope

Checkpoint: 8 October 2026 at 05:45 UTC (01:45 America/New_York). Earlier inventory and recordings retain their stated timestamps. This is a resumable overnight checkpoint. It is not a completed end-to-end debugger audit.

## Checkpoint and gates

The specified runtime payload and official GitHub App installation restricted to A were approved at 04:45:46 UTC. Brief runtime readiness and Remote Configuration snapshots were verified, and the service became discoverable. The runtime then stopped at an additional telemetry-destination approval boundary despite LLM-disabled settings. No debugger event was captured. GitHub installation and user authorization are verified, but Datadog source association remains unconnected after the interrupted flow and fresh-context retries. B exists and remains private and ungranted. Independent roles and several controlled deployment variants are still unavailable.

Earlier Remote Configuration eligibility was unknown with unresolved connectivity; it was not established as disabled or misconfigured. Later readiness snapshots supersede that uncertainty only at their own timestamps. Audit locator/recording failures and additional-destination restrictions are separate from Datadog product findings.

## Published public onboarding video

[Early onboarding excerpt](early-onboarding-excerpt.mp4) is 80 seconds of real motion capture, cropped to remove browser chrome, with captions and red outlines. Chapters: 00:00 overview; 00:20–00:34 permanent region choice; 00:34–00:58 documentation contents rail; 00:58–01:20 Python launch example. Source recording: 02:14:27–02:21:01 UTC, 393.7 seconds, 1364 × 1024 pixels, 20 fps. Edited offsets are not wall-clock times. This excerpt shows no successful runtime capture.

## Authenticated first run

03:21–03:24 UTC: empty service and environment states, manual entry, disabled Start, Close recovery, source-integration entry. Screenshots E10 at 03:21:54 and E13 at 03:23:59 are published with [UX02](findings/UX02-empty-state-recovery.md). The service image excludes the account greeting. No healthy service was established.

## Informed navigation and keyboard smoke

03:33–03:40 UTC: Home → APM intro → global search → Live Debugger navigation; actual 125% browser zoom; modal Tab focus, Escape and focus return; reset to 100%. This was informed navigation, not a blind beginner timing study. The first attempted zoom shortcut was ineffective and is excluded from evidence. Editor, long-path and field-validation behavior remain blocked.

## Empty session list controls

03:56–03:58 UTC: search, status, owner and date controls exercised with zero sessions. Status and owner filters persisted after reload; Clear Filter reset them. October 1–7 displayed correctly as a custom range. No populated-result correctness is claimed.

## Source integration pre install

03:59–04:00 UTC: custom setup showed organization-owner prerequisite and feature-to-permission explanations. Read Repository Contents described read-only functions with minimum Contents Read plus Push webhook; the visible custom draft dropdowns showed broader Read & Write defaults. Secrets access was described as names only. Official and custom drafts were canceled; reload still showed Not Connected. No effective grant or content retrieval was established. No App installation was submitted.

## Empty modal recovery

03:33–03:40 and 04:01–04:02 UTC: Close, Escape, Back, Forward, refresh and two open/Close cycles returned cleanly from the empty-service modal. Ctrl+Enter did not submit disabled Start. Attempts to fill an optional control failed in the test automation locator before input; those attempts are not product defects.

<a id="final-state"></a>

## Earlier final state at 04 12 UTC

04:12 UTC: live read-only accessibility inspection found All 0 / Active 0 / Inactive 0 with filters cleared. This check occurred after recording stopped and has no motion footage. No sessions/logpoints were created. Agent/sample processes were stopped by 03:39 UTC, and no App grant was submitted. Test accounts, the public audit repository and private fixture A are intentionally retained. At 04:22:42 UTC, two completed local setup helpers were stopped and each showed zero remaining owned processes. Private configuration was retained without inspection. Complete all-settings/account cleanup is not certified; C02 remains blocked for full inventory reconciliation.

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

[SCI01](findings/SCI01-interrupted-github-recovery.md) records the scoped recovery failure. The authorization form had remained open about 75 minutes. The eventual callback reached the Datadog organization chooser; selecting the intended organization returned an unconnected Get Started page. Connect led back to existing installation settings with Save disabled. Fresh navigation via the official integration catalog and verification of the intended organization/site did not recover the association. No callback replay, app revoke or uninstall was attempted. Fresh-install behavior is not established. Datadog UI build observed: 35.143254999.

## Draft validation after service discovery

- 04:53:17: [Wildcard environment warning](evidence/33-service-all-environments-warning-public.png) explains that an all-environment logpoint will not enable the service automatically and provides Configuration/specific-environment guidance.
- F06: pricing.py was added manually. 0, -1 and abc kept Start disabled. [Line 0 evidence](evidence/34-line-zero-validation-public.png), 04:54:43. [Line 9999](evidence/35-line-out-of-range-draft-public.png), 04:55:10, enabled an unsubmitted draft. Line 17 restored the target. No out-of-range installation or relocation result.
- 04:55:34: [Source guidance](evidence/36-source-unavailable-guidance-public.png) states the file was not found and names permissions/tags as possible causes, with Learn More. No fetched source.
- F04: the first opening brace was automatically balanced, so it was not an invalid-input test. Deleting the closing brace produced QA quantity={quantity and [disabled Start](evidence/40-unmatched-brace-actual-public.png) at 05:06:52. [Correcting the template](evidence/41-valid-template-recovery-public.png) at 05:08:14 enabled Start. No submit occurred. Conditional-expression and runtime variants remain blocked.
- When was disabled in the not-enabled wildcard-environment draft; the enabled specific-environment case is untested, so no conditional-capture defect is asserted.

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
