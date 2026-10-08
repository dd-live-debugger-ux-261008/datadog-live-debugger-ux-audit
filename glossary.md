# Beginner glossary

- **APM:** Application Performance Monitoring. Traces show how requests move through application operations.
- **Agent:** A process near an application that receives and forwards supported telemetry and configuration.
- **SDK or tracer:** A language-specific library inside an application. Python uses ddtrace.
- **Trace:** A record following one request or task.
- **Span:** One operation within a trace.
- **Service:** A named application or component. The name alone does not identify its environment or code revision.
- **Environment:** A deployment label such as staging or production.
- **Version:** A release identifier used to distinguish deployments.
- **Remote Configuration:** A supported channel for configuration changes to reach a running Agent or SDK.
- **Debug session:** A bounded investigation with debugger configuration and results. Inspect its actual expiry and active state.
- **Logpoint:** A code location and rule that collect messages or values without editing deployed source for each observation.
- **Snapshot or captured locals:** Values observed at a particular execution. Redaction, truncation, sampling, and context affect what is available.
- **Source Code Integration:** Repository access plus runtime-to-revision mapping that lets telemetry point to source. A connected account alone does not prove correct mapping.
- **Commit SHA:** A Git revision identifier. Captured data should link to the deployed revision rather than silently showing the latest branch.
- **Redaction:** Removing or masking selected data. A redacted value differs from a missing or unavailable value.

[Back to the audit](README.md) · [Findings](findings.md)

- **ARIA:** Labels, states and relationships that can help assistive technology interpret an interface. Missing one attribute alone does not prove an accessibility failure.
- **WCAG:** Web Content Accessibility Guidelines. The focused checks in this report are not a complete conformance audit.
