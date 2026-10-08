# Datadog Live Debugger and Source Code Integration audit

Continuation checkpoint: 8 October 2026 at 06:28 UTC (02:28 New York). Live runtime capture and source association remain incomplete; the specific limits are below.

The report separates beginner onboarding usability from detailed functional QA. It now records **0 High, 2 Medium and 4 Low findings**, including a scoped interrupted-GitHub-connection recovery issue.

63 original cases: 2 scoped PASS, 4 FINDING and 57 BLOCKED.

## Read the results

- [Annotated PDF](report.pdf) and [editable Word report](report.docx)
- [Severity-ranked findings](findings.md#severity-ranked-finding-index), [High only](high-severity.md), [Medium](findings.md#medium-severity), [Low](findings.md#low-severity)
- [All 63 case outcomes](QA_MATRIX.md), [separate executed subchecks](EXECUTED_CHECKS.md), [evidence and timestamps](EVIDENCE.md)
- [Video catalog and archive status](VIDEOS.md), [beginner glossary](glossary.md)

## What changed after approval

The synthetic service became visible. Local Agent intake/sample startup and Agent Remote Configuration authorization were verified at bounded timestamps; later actual APM spans prove historical tracing ingestion. Debugger SDK client registration remains unverified. GitHub's official App is installed and user-authorized with A-only repository scope; private B exists and remains ungranted. Datadog still cannot complete the source association after the interrupted authorization flow. [SCI01](findings/SCI01-interrupted-github-recovery.md) records the expected recovery, observed retry loop, approximately 75-minute pause precondition, and lack of a verified source workaround. Fresh uninterrupted installation behavior is not generalized from this result.

Actual draft checks rejected nonpositive/nonnumeric lines and an unmatched template brace; correcting the template enabled Start again. Line 9999 only enabled an unsubmitted draft, so no out-of-range runtime defect is claimed. Useful wildcard-environment and missing-source guidance was observed after service discovery, separately from the earlier empty-state recommendation.

[UX03](findings/UX03-invalid-log-template-feedback.md) adds a Low feedback issue: invalid syntax has a red border and disables Start, but the tested view/accessibility snapshot lacks an explanatory error message. Correction works; no screen-reader or global WCAG failure is claimed.

## Current limits and retained state

The initial runtime and A-only installation approvals were received. Runtime then stopped at an additional telemetry-destination approval boundary despite narrowing flags. Two baseline creation requests were rejected with a visible instrumentation-invalid error and HTTP 400, including a plain-message control. A fresh unfiltered list remained All 0 / Active 0 / Inactive 0. No captured value was verified. Datadog-retrieved source matching the deployed code, A-only/B-denied retrieval, active stop/expiry, role isolation and other dependent cases remain blocked.

The edited/reopened and later accessibility drafts were closed; no entity was created. Accounts, synthetic A/B repositories and the approved A-only installation remain test assets. Complete current resource/setting cleanup is not certified. The earlier 04:12 zero-session/no-App-grant result is historical, not the current configuration inventory.

The six finding pages use real screenshots with explicit crops/masks and separate annotations. Reviewed video excerpts are available; both the historical and approved-continuation archives are published, with exact coverage and omissions stated in [VIDEOS.md](VIDEOS.md). No generated UI is used as test evidence.
