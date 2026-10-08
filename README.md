# Datadog Live Debugger and Source Code Integration audit

Continuation checkpoint: 8 October 2026 at 05:45 UTC (01:45 New York). Live runtime capture and source association remain incomplete; the specific limits are below.

The report separates beginner onboarding usability from detailed functional QA. It now records **0 High, 2 Medium and 3 Low findings**, including a scoped interrupted-GitHub-connection recovery issue.

63 original cases: 2 scoped PASS, 3 FINDING and 58 BLOCKED.

## Read the results

- [Annotated PDF](report.pdf) and [editable Word report](report.docx)
- [Severity-ranked findings](findings.md#severity-ranked-finding-index), [High only](high-severity.md), [Medium](findings.md#medium-severity), [Low](findings.md#low-severity)
- [All 63 case outcomes](QA_MATRIX.md), [separate executed subchecks](EXECUTED_CHECKS.md), [evidence and timestamps](EVIDENCE.md)
- [Video catalog and archive status](VIDEOS.md), [beginner glossary](glossary.md)

## What changed after approval

The synthetic service became visible. Agent/SDK and Remote Configuration readiness were verified at bounded timestamps. GitHub's official App is installed and user-authorized with A-only repository scope; private B exists and remains ungranted. Datadog still cannot complete the source association after the interrupted authorization flow. [SCI01](findings/SCI01-interrupted-github-recovery.md) records the expected recovery, observed retry loop, approximately75-minute pause precondition, and lack of a verified source workaround. Fresh uninterrupted installation behavior is not generalized from this result.

Actual draft checks rejected nonpositive/nonnumeric lines and an unmatched template brace; correcting the template enabled Start again. Line 9999 only enabled an unsubmitted draft, so no out-of-range runtime defect is claimed. Useful wildcard-environment and missing-source guidance was observed after service discovery, separately from the earlier empty-state recommendation.

## Current limits and retained state

The initial runtime and A-only installation approvals were received. Runtime then stopped at an additional telemetry-destination approval boundary despite narrowing flags. Two baseline creation requests were rejected with a visible instrumentation-invalid error and HTTP 400, including a plain-message control. A fresh unfiltered list remained All 0 / Active 0 / Inactive 0. No captured value was verified. Exact deployed-source mapping, A-only/B-denied retrieval, active stop/expiry, role isolation and other dependent cases remain blocked.

The edited and reopened drafts were closed; no entity was created. Accounts, synthetic A/B repositories and the approved A-only installation remain test assets. Complete current resource/setting cleanup is not certified. The earlier 04:12 zero-session/no-App-grant result is historical, not the current configuration inventory.

The five finding pages use real screenshots with explicit crops/masks and separate annotations. Reviewed video excerpts are available; both the historical and approved-continuation archives are published, with exact coverage and omissions stated in [VIDEOS.md](VIDEOS.md). No generated UI is used as test evidence.
