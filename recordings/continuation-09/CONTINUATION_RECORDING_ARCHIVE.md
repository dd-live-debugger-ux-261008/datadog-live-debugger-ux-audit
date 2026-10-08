# Historical APM continuation: recording archive

Source 09 is fully accounted: **26:32.70 recorded, 21:30.90 retained in three videos, and 05:01.80 withheld**. These are continuous retained UI sections, including original waiting time. This is a privacy-edited archive, not an unredacted or uninterrupted video of the entire audit. All prior archives and V6 artifacts remain unchanged.

## Videos

| File | Duration | Bytes |
| --- | ---: | ---: |
| [source-09-part-01-sanitized.mp4](source-09-part-01-sanitized.mp4) | 04:02.95 | 1,455,682 |
| [source-09-part-02-sanitized.mp4](source-09-part-02-sanitized.mp4) | 07:50.00 | 4,670,633 |
| [source-09-part-03-sanitized.mp4](source-09-part-03-sanitized.mp4) | 09:37.95 | 4,129,017 |

All outputs are 1280 × 900 H.264 at the original 20 fps, with no audio. Each source range is captioned with raw offsets and UTC. Embedded chapters map the cuts. Genuine UI pixels are retained inside privacy crops; no reconstructed screens or screenshot slideshows are used.

## Exact retained intervals

| Source seconds | UTC (2026-10-08) | Output file | Output seconds | Observation |
| --- | --- | --- | --- | --- |
| 5.80–116.50 | 05:49:24.80–05:51:15.50 | source-09-part-01-sanitized.mp4 | 0.00–110.70 | APM service discovery and service summary |
| 150.40–282.65 | 05:51:49.40–05:54:01.65 | source-09-part-01-sanitized.mp4 | 110.70–242.95 | Staging environment and service version menus |
| 399.85–702.75 | 05:55:58.85–06:01:01.75 | source-09-part-02-sanitized.mp4 | 0.00–302.90 | Widen Time Frame recovers historical indexed spans |
| 796.40–963.50 | 06:02:35.40–06:05:22.50 | source-09-part-02-sanitized.mp4 | 302.90–470.00 | Historical HTTP span overview and context menu |
| 971.35–1075.25 | 06:05:30.35–06:07:14.25 | source-09-part-03-sanitized.mp4 | 0.00–103.90 | Service resources and configuration overview |
| 1118.65–1592.70 | 06:07:57.65–06:15:51.70 | source-09-part-03-sanitized.mp4 | 103.90–577.95 | SDK configuration freshness guidance and retained wait |

## Every withheld interval

| Source seconds | UTC (2026-10-08) | Duration | Reason |
| --- | --- | ---: | --- |
| 0.00–5.80 | 05:49:19.00–05:49:24.80 | 5.80s | Initial recorder/tooling preparation and browser navigation; includes privacy boundary padding. |
| 116.50–150.40 | 05:51:15.50–05:51:49.40 | 33.90s | GitHub report and recording archive administration; includes privacy boundary padding. |
| 282.65–399.85 | 05:54:01.65–05:55:58.85 | 117.20s | GitHub recording upload, report publication and repository administration; includes privacy boundary padding. |
| 702.75–796.40 | 06:01:01.75–06:02:35.40 | 93.65s | GitHub recording highlights and repository administration; includes privacy boundary padding. |
| 963.50–971.35 | 06:05:22.50–06:05:30.35 | 7.85s | Brief GitHub upload/publishing tab interruption; includes privacy boundary padding. |
| 1075.25–1118.65 | 06:07:14.25–06:07:57.65 | 43.40s | GitHub upload commit, publishing verification and repository administration; includes privacy boundary padding. |

## Crops and masks

Coordinates are source x, y, width, height in the original 1364 × 1024 frame. Every motion section uses crop [252, 280, 1004, 620]. The crop excludes browser chrome, greeting/profile areas, the private trace-identity header, and the browser status strip. No opaque masks were needed within this reviewed motion crop. Separate screenshot derivatives use their own documented crops/masks. All pixels outside the motion crop are excluded. H.264 is lossy re-encoding.

## Evidence limits

- This recording demonstrates historical APM service and trace exploration. A service or historical span does not establish a running debug session, live variable capture, source integration success or successful source retrieval.
- The APM environment selector offers staging. The initial 15-minute live-search view has no matching traces. Widen Time Frame changes to a historical window with 47 indexed spans; the empty initial window is not proof that ingestion never occurred.
- The indexed GET /quote span has HTTP 200 status. Its private trace identifier is excluded by the crop. The motion does not visually establish every lower span-tag value read separately during the audit.
- The SDK Configurations drawer states that no configuration data was detected for this service in the last 15 minutes, and advises checking the running service, instrumentation telemetry and telemetry intake accessibility. Its empty state does not establish a single root cause.
- Screenshot 49 predates recording 09. Screenshots 56 and 57 were captured after recording 09 and independently show version, environment and baseline commit pixels; they are explicitly screenshot-only and are not inserted into either motion export.
- All source-caption clocks are UTC reconstructed from recorder start. Datadog chart/list timestamps use the timezone displayed in the application, including UTC-07:00. Those application timestamps are not capture timestamps.
- The archive retains original waiting time inside each continuous section. Every removed interval is recorded in the archive manifest. No screenshots, generated content or reconstructed UI substitute for captured motion.
- All sections use source crop [252,280,1004,620], excluding browser chrome, profile/greeting regions, trace identity headers, footer/status URLs and offscreen details. Cropped-out controls or data are not evidence that they are absent in the product.

## Review and integrity

Review covered full-source overviews, every-frame page-state scanning, dense privacy transitions, 323 sampled output OCR frames, full-size representative output checks and decoded output validation. The original raw SHA-256 is unchanged: c894964abf0dd7c8ad41bb62c54f13da5319cb22e3194393ed5e76702b4d6449.

The exact mapping, source/output fingerprints and media metadata are in [continuation-recording-manifest.json](continuation-recording-manifest.json). Public file hashes are in [SHA256SUMS.txt](SHA256SUMS.txt). Raw recordings, private screenshots, contact sheets and build scripts are not in this upload folder.
