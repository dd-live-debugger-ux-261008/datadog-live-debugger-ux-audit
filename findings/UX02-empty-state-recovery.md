# UX02 Empty service states do not explain setup recovery

LOW · UX recommendation · Part 1 new-user usability

[Severity-ranked index](../findings.md#severity-ranked-finding-index) · [High only](../high-severity.md) · [Beginner glossary](../glossary.md)

## Screenshot evidence

[![Actual Live Debugger service picker with a red border around No services found](../evidence/annotated/UX02-empty-service-list.png)](../evidence/annotated/UX02-empty-service-list.png)

[Open full-size annotated screenshot](../evidence/annotated/UX02-empty-service-list.png) · [Open full-size evidence crop](../evidence/10-live-debugger-service-list-public.png)

Captured 2026-10-08 at 03:21:54 UTC. The top 76 pixels containing the account greeting were removed for public sharing. The remaining UI pixels are unchanged except for the separately added red border.

[![Actual Live Debugger Configuration setup section with a red border around No environments found](../evidence/annotated/UX02-no-environments.png)](../evidence/annotated/UX02-no-environments.png)

[Open full-size annotated screenshot](../evidence/annotated/UX02-no-environments.png) · [Open full-size original](../evidence/13-live-debugger-no-environments.jpg)

Captured 2026-10-08 at 03:23:59 UTC. This scrolled screenshot contains no account identifier. The red border is the only pixel change.

**Video evidence:** [Reviewed authenticated UI excerpt](../authenticated-ui-qa-excerpt.mp4), 00:00–00:13.80 (empty service), 00:13.80–00:26.80 (manual entry), and 02:42.80–02:50.80 (empty configuration). See [exact source intervals](../edited-video-manifest.md). The video shows no successful capture or installed source integration.

## Reproduce

1. In the fresh test organization, open APM → Debugger → New Session while no services are available.
2. Open the service picker: it reports “No services found.”
3. Click the visible New Session action in the manual-debugging section. The modal opens, but the same unavailable service is required; Start Debug Session is disabled.
4. Close the modal, then open Configuration and inspect Live Debugger Setup. It instructs the user to enable services/environments, but reports “No environments found.”

## Observed experience

The unavailable selections are clear, but neither captured empty-state message identifies a concrete setup recovery step. The Configuration setup section has no direct Agent/APM recovery link beside its empty state. A complete newcomer must infer which prerequisite is missing and where to fix it.

The separate Source Code Integrations section is described as recommended and offers provider Grant Access actions. Those actions do not explain how to make an absent runtime service or environment appear.

## Recommended experience

Add a contextual “Connect your first service” or prerequisite-check action beside the empty state. Explain which checks are known and unknown, including application instrumentation/APM, environment tagging, compatible SDK/Agent, Remote Configuration, and permissions. Avoid attributing a specific cause when the product has not established it.

**Severity:** LOW. This is recovery/discoverability friction. The test has not established that a correctly configured service is incorrectly absent.

## Positive behavior and boundaries

- Manual debugging remains visible without Source Code Integration. Source linking did not falsely block entry to the manual route.
- Start Debug Session is correctly disabled when no service is selected.
- Closing the modal returns to the prior page; no session was created in this check.
- At the original empty-state checkpoint, runtime ingestion was not established. In the later authorized continuation, a healthy SDK runtime exposes staging and captures the expected numeric values. This does not establish that a correctly configured service was previously absent.
- This finding is limited to the captured empty-state section and modal. It does not claim that no onboarding help exists elsewhere in Datadog.

## Later recovery checks after service discovery

The approved continuation did discover a service. Its wildcard-environment draft provides useful guidance that all-environment creation does not enable the service automatically, with a Go to Configuration link. This positive behavior narrows the earlier empty-account observation.

Two baseline creation attempts later returned an explicit instrumentation-invalid toast and HTTP 400; the error was not silent. The offered Configuration link preserved the draft and opened service-specific setup, where live page inspection reported no environments and source integration remained unconnected. The cause of creation rejection is unresolved; runtime pause and absent source association are not established explanations. This remains a scoped recovery-guidance observation, not evidence that a fully healthy service is incorrectly absent. [Detailed timing and boundaries](../EVIDENCE.md#baseline-submission-attempts).

## Later healthy baseline

The hosted synthetic runtime registered the Live Debugging SDK products; staging became available and a manual session produced actual events and locals before source association was repaired. F01 subsequently verified the complete quantity 2/3/4 numeric-template controls. [Baseline evidence](../EVIDENCE.md#verified-numeric-baseline).

The initial Enable logs message also gave way to populated events after visiting Logs and reloading, without a Logs setting change. This remains a separate unconfirmed observation, not another finding or proof of a Logs-configuration defect. The earlier HTTP 400 cause remains unresolved. [Unconfirmed inventory](../UNCONFIRMED_OBSERVATIONS.md).
