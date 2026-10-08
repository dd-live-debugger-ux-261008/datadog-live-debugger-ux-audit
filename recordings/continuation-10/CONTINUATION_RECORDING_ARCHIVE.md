# Draft feedback continuation: recording archive

Source 10 is fully accounted: **04:30.75 recorded, 04:22.80 retained in one video, and 00:07.95 withheld**. These are continuous retained UI sections, including original waiting time. This is a privacy-edited archive, not an unredacted or uninterrupted video of the entire audit. All prior archives and V6 artifacts remain unchanged.

## Videos

| File | Duration | Bytes |
| --- | ---: | ---: |
| [source-10-part-01-sanitized.mp4](source-10-part-01-sanitized.mp4) | 04:22.80 | 1,965,930 |

All outputs are 1280 × 900 H.264 at the original 20 fps, with no audio. Each source range is captioned with raw offsets and UTC. Embedded chapters map the cuts. Genuine UI pixels are retained inside privacy crops with labeled opaque browser-UI masks; no reconstructed screens or screenshot slideshows are used.

## Exact retained intervals

| Source seconds | UTC (2026-10-08) | Output file | Output seconds | Observation |
| --- | --- | --- | --- | --- |
| 7.95–8.70 | 06:23:50.95–06:23:51.70 | source-10-part-01-sanitized.mp4 | 0.00–0.75 | Return to the manual session draft |
| 8.70–269.70 | 06:23:51.70–06:28:12.70 | source-10-part-01-sanitized.mp4 | 0.75–261.75 | Draft entry, invalid-template feedback, correction and retained waiting |
| 269.70–270.75 | 06:28:12.70–06:28:13.75 | source-10-part-01-sanitized.mp4 | 261.75–262.80 | Draft closed without submission |

## Every withheld interval

| Source seconds | UTC (2026-10-08) | Duration | Reason |
| --- | --- | ---: | --- |
| 0.00–7.95 | 06:23:43.00–06:23:50.95 | 7.95s | Initial recorder/terminal preparation and transition to the browser; includes privacy boundary padding. |

## Crops and masks

Coordinates are source x, y, width, height in the original 1364 × 1024 frame. Page sections use source crop [252, 280, 1004, 620] with an opaque footer mask [252, 876, 1004, 24]. The modal uses crop [144, 252, 1062, 664] with an opaque mask [144, 876, 810, 40] over a persistent native Chromium tooltip and the browser status area. These masks are labeled. Browser tabs, address bar, account header, desktop and terminal are excluded. All pixels outside each crop are excluded. H.264 is lossy re-encoding.

## Evidence limits

- This recording shows draft-only manual logpoint entry and template validation. No create request is submitted, and no session, logpoint or captured variable is claimed.
- The unmatched template disables Start Debug Session while editing. Moving focus to the Line field produces a visible red outline on the invalid template. Correcting the closing brace restores enabled Start.
- These pixels show visual validation behavior. The accessible name and error-announcement semantics of the controls require separate DOM/accessibility inspection; the motion and stills do not themselves establish a WCAG failure.
- The service/wildcard environment warning remains visible. Enabled Start is a draft-state observation, not proof of valid instrumentation, successful source retrieval or live capture.
- All source-caption clocks are UTC reconstructed from recorder start. Original-speed motion, waiting time and transitions are retained inside the source ranges listed in the archive manifest.
- Browser chrome, account/profile regions, terminal preparation and browser tooltip/status areas are cropped or opaquely masked. Masks may hide adjacent blank UI and are disclosed editorial overlays.
- The screenshots are separate genuine captures. Original 58/59 filenames have a .png suffix but contain JPEG data; the publication derivatives are decoded, metadata-stripped PNG crops. No still image is substituted into the video.
- Previous source09 exports, older recordings and the frozen V6 checkpoint are unchanged.

## Review and integrity

Review covered full-source overviews, every-frame page-state scanning, dense privacy transitions, 66 sampled output OCR frames, full-size representative output checks and decoded output validation. The original raw SHA-256 is unchanged: 73276d04588379f647606755d19d40754f045fe54cdd40b1f930db686a66c7a9.

The exact mapping, source/output fingerprints and media metadata are in [continuation-recording-manifest.json](continuation-recording-manifest.json). Public file hashes are in [SHA256SUMS.txt](SHA256SUMS.txt). Raw recordings, private screenshots, contact sheets and build scripts are not in this upload folder.
