# Datadog Live Debugger and Source Code Integration audit

Work in progress. Last updated: 2026-10-08 03:02 UTC.

Public repository: [datadog-live-debugger-ux-audit](https://github.com/dd-live-debugger-ux-261008/datadog-live-debugger-ux-audit).

This audit follows two tracks: the experience of a beginner unfamiliar with Datadog and APM, and professional QA of runtime behavior, source identity, permissions, error handling, and lifecycle.

## Read the current results

- [Annotated report PDF](report.pdf)
- [Editable report](report.docx)
- [Severity-ranked finding index](findings.md#severity-ranked-finding-index)
- [High severity findings only](high-severity.md)
- [Medium severity findings](findings.md#medium-severity)
- [Low severity findings](findings.md#low-severity)
- [Beginner glossary](glossary.md)
- [Detailed QA test plan](QA_MATRIX.md)

The PDF and Word document contain actual browser screenshots with separate red-border annotations. The screenshots are not generated mockups. The [80-second early onboarding video](early-onboarding-excerpt.mp4) is real motion capture with browser chrome removed, captions, and red borders. It covers public signup and documentation, not a completed authenticated debugger workflow.

Video chapters: 00:00 overview; 00:20 region-choice UX; 00:34 documentation navigation; 00:58 Python command defect.

## Current state

- Fresh test Datadog and GitHub accounts reached authenticated welcome/home screens.
- Public onboarding and Python documentation were reviewed in a real browser.
- One Python quickstart command defect was reproduced locally, with working positive controls.
- One desktop documentation layout defect was observed in two scroll positions.
- A region-selection decision-support recommendation is recorded separately from confirmed defects.
- A synthetic Python fixture has eight passing local tests and one intentional expected failure for its planted pricing bug.
- Authenticated product exploration is ongoing. No successful Datadog variable capture, exact deployed-source match, repository authorization boundary, or expiry test is claimed yet.

The matrix contains 54 baseline cases plus nine separately labeled supplementary edge cases, all a test plan. Its case count is not the count of tests executed. Cases remain NOT RUN until evidence establishes their outcome. This repository will be updated incrementally as results become available.

## Evidence conventions

All times are UTC. Screenshot timestamps identify capture-file creation; approximate raw recording offsets are separate. An edited video's timestamps will differ from the raw capture.

The public artifacts exclude credentials, API keys, account identifiers, private session URLs, and unrelated account information. Underlying screenshot pixels remain unchanged beneath the report annotations.

## Scope

The audit uses dedicated synthetic data and a local pricing example. It does not test production applications, customer data, load capacity, or the complete Datadog security model. Planned negative and permission cases are explicitly distinguished from observed failures.

At audit close, every planned case will have an explicit executed outcome, a concrete blocker, or an unsupported classification. The ongoing plan is not presented as exhausted coverage.
