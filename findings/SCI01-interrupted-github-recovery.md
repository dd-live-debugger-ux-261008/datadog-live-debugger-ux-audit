# SCI01 Interrupted GitHub connection does not recover through Connect

MEDIUM · Scoped functional recovery issue · Part 2 professional QA · Case S11

[Severity index](../findings.md#severity-ranked-finding-index) · [High only](../high-severity.md) · [PDF](../report.pdf)

## Annotated screenshot

[![Datadog remains at Get Started after the interrupted GitHub callback, with the offered Connect action outlined](../evidence/30-github-return-empty-integration-public-annotated.png)](../evidence/30-github-return-empty-integration-public-annotated.png)

[Full-size annotated image](../evidence/30-github-return-empty-integration-public-annotated.png) · [Full-size sanitized original](../evidence/30-github-return-empty-integration-public.png). Captured 04:50:15 UTC. The personalized top bar/navigation is cropped out; the separate annotated version adds only the disclosed red outline.

## Corroborating states

[![GitHub lists Datadog Official as installed](../evidence/32-github-installed-a-only-public.png)](../evidence/32-github-installed-a-only-public.png)

[Full-size installed-app state](../evidence/32-github-installed-a-only-public.png), 04:51:29 UTC. This image verifies installation only; repository scope is below.

[![Authorized GitHub Apps lists Datadog Official](../evidence/37-github-authorized-apps-public.png)](../evidence/37-github-authorized-apps-public.png)

[Full-size user-authorization state](../evidence/37-github-authorized-apps-public.png), 04:56:26 UTC. Unrelated application/account areas are masked. Never used is the observed label, not a diagnosis.

[![GitHub repository selection remains one selected repository](../evidence/38-a-only-after-b-created-public.png)](../evidence/38-a-only-after-b-created-public.png)

[Full-size saved scope](../evidence/38-a-only-after-b-created-public.png), 05:06:05 UTC. The private identity is masked; private test observation verifies that the selected repository is A, and B remains ungranted.

## Preconditions and reproduction

1. Start the official GitHub connection from the intended Datadog organization with a personal GitHub test account.
2. Leave the installation form open approximately 75 minutes before granting the explicitly approved A-only installation. Complete required reauthentication.
3. On return, select the intended Datadog organization. Observe Get Started / Connect GitHub Account without a success or error confirmation.
4. Use Connect again. GitHub opens the existing installation settings; the unchanged settings have Save disabled and no usable completion route.
5. Navigate fresh through Integrations → GitHub → official GitHub Apps. Verify the intended Datadog organization and site. The page still offers the unconnected flow. Cancel any selection draft and reload; persisted scope remains A-only.

The delay is a reproduction precondition, not an established cause. No claim is made that a fresh uninterrupted install fails. No callback URL was replayed and no app was revoked or uninstalled.

## Expected and actual

Expected: the documented Install & Authorize flow returns a Datadog connection confirmation. If interrupted, an offered recovery route should complete association or identify the remaining step/error. [Official Datadog flow](https://docs.datadoghq.com/integrations/github/).

Actual: GitHub installation and user authorization are present, but Datadog remains unconnected. The visible Connect retry returns to unchanged installed-app settings and does not restore association. Fresh catalog navigation in the verified account context gives the same state.

Impact: source linking cannot be completed through the offered route in this interrupted state. Manual debugger entry remains available. No workaround that restores source association was verified. Severity is Medium for this bounded recovery failure; broader fresh-install behavior and the backend cause remain unproven.

Suggested recovery: detect or explain partial association, offer a supported same-scope resume, and preserve the selected Datadog organization. Confirm success or give a specific actionable error rather than repeating the initial Connect route.

## Evidence boundaries

Installation before 04:49:33 is screenshot-only. Subsequent recovery has reviewed genuine motion: [highlight 00:00–00:10.50 and 01:19.50–01:31.50](../recordings/continuation-07/highlights/approved-setup-continuation-highlights.mp4). [Full retained sections and omissions](../recordings/continuation-07/CONTINUATION_RECORDING_ARCHIVE.md) preserve wider context. Raw recordings remain private. The earlier published videos do not show the completed installation. [Exact screenshot provenance](../evidence/runtime-privacy-provenance.md) · [Current video catalog](../VIDEOS.md).

This finding does not claim successful source retrieval, a permissions leak, wrong deployed revision, live captured variables or an active debugger session. GitHub distinguishes installation from user authorization; both lists were checked here. [GitHub authorization model](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps).
