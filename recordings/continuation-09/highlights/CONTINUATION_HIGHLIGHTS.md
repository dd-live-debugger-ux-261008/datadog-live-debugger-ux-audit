# Historical APM continuation: edited highlights

[historical-apm-continuation-highlights.mp4](historical-apm-continuation-highlights.mp4): **02:07.00**, 1,350,104 bytes, 1280 × 900, H.264, 20 fps, no audio. Genuine motion at normal speed, with privacy crops and explanatory captions. Earlier published highlights and V6 artifacts are unchanged.

## Chapters and original motion sources

| Edit time | Source 09 seconds | Source UTC (2026-10-08) | Chapter |
| --- | --- | --- | --- |
| 00:00.00–00:11.00 | 6.50–17.50 | 05:49:25.50–05:49:36.50 | APM service discovery |
| 00:11.00–00:25.00 | 90.00–104.00 | 05:50:49.00–05:51:03.00 | Historical service summary |
| 00:25.00–00:35.00 | 150.40–160.40 | 05:51:49.40–05:51:59.40 | Staging environment is offered |
| 00:35.00–00:46.00 | 174.00–185.00 | 05:52:13.00–05:52:24.00 | Staging selection and version menu |
| 00:46.00–01:00.00 | 399.85–413.85 | 05:55:58.85–05:56:12.85 | Widen Time Frame recovers historical spans |
| 01:00.00–01:15.00 | 679.00–694.00 | 06:00:38.00–06:00:53.00 | Open an indexed HTTP span |
| 01:15.00–01:25.00 | 797.00–807.00 | 06:02:36.00–06:02:46.00 | Inspect a span context menu |
| 01:25.00–01:37.00 | 971.35–983.35 | 06:05:30.35–06:05:42.35 | Service resource summary |
| 01:37.00–01:49.00 | 1038.00–1050.00 | 06:06:37.00–06:06:49.00 | Service configuration overview |
| 01:49.00–02:07.00 | 1118.65–1136.65 | 06:07:57.65–06:08:15.65 | SDK configuration freshness guidance |

## Evidence limits

- This recording demonstrates historical APM service and trace exploration. A service or historical span does not establish a running debug session, live variable capture, source integration success or successful source retrieval.
- The APM environment selector offers staging. The initial 15-minute live-search view has no matching traces. Widen Time Frame changes to a historical window with 47 indexed spans; the empty initial window is not proof that ingestion never occurred.
- The indexed GET /quote span has HTTP 200 status. Its private trace identifier is excluded by the crop. The motion does not visually establish every lower span-tag value read separately during the audit.
- The SDK Configurations drawer states that no configuration data was detected for this service in the last 15 minutes, and advises checking the running service, instrumentation telemetry and telemetry intake accessibility. Its empty state does not establish a single root cause.
- Screenshot 49 predates recording 09. Screenshots 56 and 57 were captured after recording 09 and independently show version, environment and baseline commit pixels; they are explicitly screenshot-only and are not inserted into either motion export.
- All source-caption clocks are UTC reconstructed from recorder start. Datadog chart/list timestamps use the timezone displayed in the application, including UTC-07:00. Those application timestamps are not capture timestamps.
- The archive retains original waiting time inside each continuous section. Every removed interval is recorded in the archive manifest. No screenshots, generated content or reconstructed UI substitute for captured motion.
- All sections use source crop [252,280,1004,620], excluding browser chrome, profile/greeting regions, trace identity headers, footer/status URLs and offscreen details. Cropped-out controls or data are not evidence that they are absent in the product.

Exact crops, masks, captions, source hashes and output checksums are recorded in [continuation-highlight-manifest.json](continuation-highlight-manifest.json). The full privacy-edited continuation archive retains 21:30.90, separately from this selected highlight.
