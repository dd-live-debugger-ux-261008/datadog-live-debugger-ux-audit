# Datadog audit findings

Status: work in progress. Updated 2026-10-08 03:02 UTC.

## Severity ranked finding index

[High only](high-severity.md) · [Medium](#medium-severity) · [Low](#low-severity) · [Glossary](glossary.md)

HIGH: no confirmed findings yet. MEDIUM: 1. LOW: 2. These counts do not rate untested product areas.

| ID | Severity | Classification | Finding |
|---|---|---|---|
| [DOC01](#doc01-python-quickstart-uses-an-invalid-module-command) | MEDIUM | Confirmed bug | Python quickstart uses an invalid module command |
| [DOC02](#doc02-contents-rail-splits-section-names-mid-word) | LOW | Confirmed bug | Contents rail splits section names mid-word at desktop width |
| [UX01](#ux01-permanent-region-choice-needs-decision-support) | LOW | UX recommendation | Permanent region choice would benefit from decision support |

Severity describes impact, not test priority. No runtime, source-integration, or security failure is inferred from a case that has not run.

## Severity rubric

- HIGH: core task blocked or significant incorrect behavior with no reasonable workaround.
- MEDIUM: material task failure or misleading behavior with a practical workaround.
- LOW: localized readability, discoverability, or friction without demonstrated task failure.

Types stay separate: confirmed bugs have direct evidence; UX recommendations describe an improved experience; hypotheses are unverified; environment or setup limits are coverage boundaries.

## Medium severity

## DOC01 Python quickstart uses an invalid module command

**Source:** [Live Debugger documentation](https://docs.datadoghq.com/tracing/live_debugger/), Python tab, Enable with environment variables.

**Evidence:** [Original screenshot](evidence/04-python-launch-command.jpg), captured 2026-10-08 at 02:20:19 UTC. The annotated report marks the final line with a red border. The initial raw recording shows this page approximately 05:45–06:20.

**Severity:** MEDIUM. **Type:** Confirmed documentation bug.

**Video:** [Early onboarding excerpt](early-onboarding-excerpt.mp4), 00:58–01:20. This is public documentation footage; the local Python reproduction is separate evidence.

**Observed command:** `ddtrace-run python -m myapp.py`

**Reproduction:** Create a file named `myapp.py` containing only `print("INERT_FIXTURE_EXECUTED")`. On Python 3.12.14, run `python -m myapp.py`. The process prints the fixture marker and exits 1 with a module-specification error. Python suggests using `myapp` instead of `myapp.py` as the module name. Independently reproduced at 02:31:35 UTC.

**Expected:** The launch example uses valid script or module syntax and starts the intended application without a module-resolution error.

**Actual:** The Python portion fails for the minimal script. The invalid invocation imports the module before the error, so top-level application code can execute first. A long-running application was not tested with this command; the reproduction does not establish when such an application would terminate.

**Positive controls:** `python myapp.py` and `python -m myapp` each print the same marker and exit 0.

**Impact:** A copied onboarding example can fail after executing top-level code, diverting a beginner into Python module troubleshooting instead of debugger setup.

**Recommended correction:** Use `ddtrace-run python myapp.py` for a script or `ddtrace-run python -m myapp` for a module. Add a quickstart smoke test that validates process startup.

**Boundary:** The isolated check does not validate the `ddtrace-run` wrapper, Agent, telemetry ingestion, or a successful instrumented Datadog session.

## Low severity

## DOC02 Contents rail splits section names mid-word

**Source:** [Live Debugger documentation](https://docs.datadoghq.com/tracing/live_debugger/), Python tab.

**Evidence:** [Original requirements screenshot](evidence/03-python-requirements.jpg), captured 2026-10-08 at 02:19:51 UTC. Also visible in DOC01's screenshot at another scroll position. Approximate raw recording location: 05:15–05:45.

**Severity:** LOW. **Type:** Confirmed layout bug.

**Video:** [Early onboarding excerpt](early-onboarding-excerpt.mp4), 00:34–00:58.

**Environment:** Default browser zoom; approximately 1180 × 757 browser page viewport. The direct captured image is 1165 × 747 pixels.

**Reproduction:** Open the Python documentation at the observed desktop width. Scroll to Requirements and inspect the right-hand On this page navigation.

**Expected:** Section labels remain readable through word-boundary wrapping or a usable collapsed navigation pattern.

**Actual:** Requirements, Permissions, Datadog configuration, and other labels split in the middle of words.

**Impact:** The outline becomes harder to scan while a new user is assembling several prerequisites.

**Recommendation:** Reserve sufficient rail width or collapse it earlier. Retest common desktop widths, 125–150% zoom, and long translated labels. These additional viewport tests have not yet run.

## UX01 Permanent region choice needs decision support

**Severity:** LOW. **Type:** UX recommendation.

**Evidence:** [Blank signup frame](evidence/08-public-signup-blank-video-frame.png) from the [early onboarding excerpt](early-onboarding-excerpt.mp4), 00:20–00:34. The frame contains no entered identity. It comes from raw capture 00:50, approximately 02:15:17 UTC. The report adds a red border around the region control and warning.

**Observed:** Trial signup includes Select a Region and a clear warning that it cannot be changed later. The captured form gives little in-place guidance about what should drive that choice. The form was observed again at 02:19:25 UTC. The public evidence uses the earlier blank-form state.

**Recommended experience:** Explain account-location implications or link to a region chooser before submission. Preserve the existing clear permanent-choice warning.

**Classification:** An onboarding recommendation, not a demonstrated functional failure. No wrong-region account, data loss, or failed submission was established.

## Current coverage and next gates

Fresh accounts reached signed-in Datadog welcome and GitHub home states. Product exploration continues. The known local fixture result is quantity 3 → 3600 cents rather than the intended 3240, due to an intentionally planted `quantity > 3` comparison. This fixture bug is not a Datadog defect.

Still unverified: Agent/SDK setup, first actual captured locals, exact deployed repository/commit/path/line, never-granted private-repository denial, permission revocation, lifecycle expiry, stale tabs, and cleanup of any future debug entities. The [QA matrix](QA_MATRIX.md) defines these cases without asserting results.

## Planned scenario coverage

The annotated report now includes the requested scenario plan. [QA_MATRIX.md](QA_MATRIX.md) preserves the original 54 baseline cases and adds X01–X09 as separately labeled PLANNED / NOT RUN cases: mixed-commit rolling replicas; same service names across environments and forks; never-executed function versus uninstalled probe; delete/expiry versus late-snapshot races; moved lines across deployment; asynchronous request correlation; cyclic/Unicode values and nested sensitive fields; repository recovery without reinstall; and same-location sessions with different conditions.

This is 63 planned cases, not 63 executed tests. No new outcome is implied by adding the plan.
