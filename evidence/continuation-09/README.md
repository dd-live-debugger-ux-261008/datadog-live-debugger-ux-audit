# APM continuation: publication-safe stills

Nine genuine captured UI frames, cropped to the relevant view. Unique trace identity in image 54 and process/runtime/span values in image 56 are covered by opaque black rectangles. No UI has been reconstructed, generated, relabeled, or retouched. Original files and older exports were not modified. These files are prepared locally; this package does not publish them.

## Reading the evidence

Images 49–55 show a service listed in APM, the staging environment selected, an empty visible 15-minute search, and 47 indexed spans in a one-hour historical search. Historical APM data does not establish current Live Debugger instrumentation. The SDK view reports no configuration data for this service in the last 15 minutes.

Images 56 and 57 are screenshot-only captures made after the Raw09 motion recording ended. They are not frames extracted from source09 motion. They show historical ingested span tags for version 0.1.0, environment staging, and git.commit.sha. The actual commit tag pixels are retained with explicit authorization in an isolated view that contains no repository or account identity.

The Widen Time Frame click and the separate Agent-last-seen eligibility guidance are not visible in these stills. The original filename of image 54 mentions source tags, but that frame only shows a span overview; source tags are visible in the later screenshot-only captures. Do not use the presence of historical tags as proof of source retrieval, a currently running commit, successful enablement, a started debug session, or received snapshots.

## Transformation and provenance

Rectangles below use [x, y, width, height] in pixels, with the origin at the top left and half-open extents. Cropping uses original pixels with no resizing. Each output is RGB PNG with source metadata stripped. Outside the documented masks, every output pixel was checked against the corresponding decoded source pixel. All source hashes were checked again after export.

Capture-file modification times are filesystem provenance only. They may reflect copying or export, so they are not independently verified capture times, ingestion times, or trace-event times. Relevant UI time controls show UTC-07:00; filesystem timestamps below are UTC. The screenshot-only timing distinction for images 56–57 comes from the supplied recording sequence and is recorded separately from the filesystem timestamps.

No private source code or secrets were read. Crops exclude global/profile chrome and irrelevant surroundings. The demonstration service name, staging environment, version query, and explicitly authorized isolated commit tag are retained. Every mask is documented below and in manifest.json.

SHA256SUMS authenticates all nine PNG derivatives, this README, and manifest.json. Original hashes are recorded below and in manifest.json; the originals are intentionally not included. All nine media files are below 25 MB.

## 49-reopened-draft-reset.png

The reopened logpoint draft has an all-environments selection, a blank code location, and a disabled Start Debug Session button. The visible warning says Live Debugger is not enabled for this service and that creating an all-environments logpoint will not enable it automatically.

Limits: This is an unsubmitted draft. It does not show successful debugger enablement, instrumentation, a started debug session, or received snapshots.

- Original: `49-reopened-draft-reset.jpg` (1180 × 729 px; 62387 bytes)
- Capture-file modification time (UTC): 2026-10-08T05:43:36.440676Z
- Source crop [x, y, width, height]: [44, 48, 1077, 665]
- Output: 1077 × 665 px; 176381 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `4f0739e2ef28ce56495e32a636dc0e89e406dafc1d675cdb24c6fc632e6a4932`
- Output SHA-256: `7f57c4ebea516ef2e4b61f2487573ea289879cdf5c255543ecf1ba2363407d76`

## 50-apm-service-listed.png

The APM service chooser lists the demonstration service. The visible Last Deploy value is 1h ago.

Limits: A service listing and relative deployment age do not prove a process is currently running or that Live Debugger is enabled.

- Original: `50-apm-service-discovered.jpg` (1180 × 729 px; 65479 bytes)
- Capture-file modification time (UTC): 2026-10-08T05:50:46.739928Z
- Source crop [x, y, width, height]: [160, 77, 1020, 611]
- Output: 1020 × 611 px; 81144 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `9cf3010f53b199070b36af65b0067380f1c3663ae5a4bd583bc08464a37e53ab`
- Output SHA-256: `9b3f72dd53ea10561c733aad9cf713d550285a9cc57c2f7fc7c01c03a64930e0`

## 51-apm-staging-selected.png

The APM service summary has env staging selected, operation sample.request, version All, and a Past 1 Hour window.

Limits: The selected environment and historical summary do not prove current instrumentation or current source-code access. The chart is partially visible and shows a loading indicator.

- Original: `51-apm-staging-selected.jpg` (1165 × 720 px; 87484 bytes)
- Capture-file modification time (UTC): 2026-10-08T05:52:22.721601Z
- Source crop [x, y, width, height]: [158, 76, 991, 644]
- Output: 991 × 644 px; 214446 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `69e3de9477ee9211ed1818d7d2d03f490bb1dfe7b6585e15195d7037acaf5851`
- Output SHA-256: `b677bd65f5d3354c9679bb57a164045cd5e734d5c460e5698c0d262cdf3377cf`

## 52-live-search-15m-empty.png

Live Search uses Past 15 Minutes and filters for staging, sample.request, the demonstration service, and version 0.1.0. The visible results are empty and the displayed rate is 0 spans/s.

Limits: This is only the selected 15-minute query window. It does not establish that no historical spans exist or that the service was never instrumented.

- Original: `52-apm-traces-initial-time-window.jpg` (1165 × 720 px; 93669 bytes)
- Capture-file modification time (UTC): 2026-10-08T05:55:12.564569Z
- Source crop [x, y, width, height]: [158, 76, 991, 644]
- Output: 991 × 644 px; 242728 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `4d8b3f199b89d571056ecac9afe2447cdf3aa6969beed4a358390b8c017039a3`
- Output SHA-256: `34f89545ef59e10fabf772b172c17417642b36c7f74632e5b3305c3b8b1e5dd1`

## 53-historical-search-47-spans.png

Historical Search uses Past 1 Hour and displays 47 indexed spans for the demonstration service, including GET /quote entries.

Limits: This still shows the recovered historical result. It does not show the Widen Time Frame click itself, and historical spans do not prove fresh traffic or live debugger instrumentation.

- Original: `53-historical-traces-recovered.jpg` (1165 × 720 px; 141123 bytes)
- Capture-file modification time (UTC): 2026-10-08T05:59:26.865009Z
- Source crop [x, y, width, height]: [158, 36, 991, 684]
- Output: 991 × 684 px; 477744 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `8d942f984eb95a537c68112e88182db3c358613014fa8d1cdaed54cfab554319`
- Output SHA-256: `8378aea330afd13a27f92062e3c8c47d1641e4d728e7e60abc93a5f7c4e1d04f`

## 54-indexed-span-overview.png

An indexed GET /quote span overview shows HTTP 200 and a 159 microsecond duration. The trace identity header is covered by an opaque black mask.

Limits: Despite the original filename, source-tag rows are not visible in this captured frame. It cannot establish a repository, commit, source retrieval, or live instrumentation.

- Original: `54-indexed-trace-source-tags.jpg` (1180 × 729 px; 93696 bytes)
- Capture-file modification time (UTC): 2026-10-08T06:02:35.784133Z
- Source crop [x, y, width, height]: [354, 40, 810, 689]
- Output: 810 × 689 px; 157933 bytes
- Opaque black mask: source [730, 45, 312, 32]; output [376, 5, 312, 32]; RGB [0, 0, 0], opacity 1. Remove the trace identity header, including its unique identifier.
- Original SHA-256: `59dc22bc9e60b2fa15ce5f983cf4b3fbb66b8acb7d6d207bf0434488ea4cc601`
- Output SHA-256: `fda17211af62ad22497a102252d026c4e113620e7f9bdf018a1369e8f0f42b69`

## 55-sdk-no-recent-config.png

SDK Configurations shows 0 of 0 configurations and No SDK Configuration Data. Its visible guidance says no configuration data was detected for this service in the last 15 minutes, and advises checking whether the service is running, instrumentation telemetry is enabled, and the telemetry intake endpoint is accessible.

Limits: This empty SDK configuration view does not prove that a particular prerequisite failed. It does not display the separate Agent-last-seen eligibility wording or prove Live Debugger is currently enabled.

- Original: `55-sdk-config-freshness-guidance.png` (1165 × 720 px; 94344 bytes)
- Capture-file modification time (UTC): 2026-10-08T06:15:52.269960Z
- Source crop [x, y, width, height]: [346, 36, 803, 684]
- Output: 803 × 684 px; 208555 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `54f19784983aa1acf7287ad96f91a6660453e772b09743c2ec91cd095b04a406`
- Output SHA-256: `a70b4764677743bb44004484f8eb219c11f15d506a9cb9083fc9308d181346ee`

## 56-screenshot-only-ingested-version.png

Screenshot-only: a separately captured historical span detail shows version 0.1.0. Process, runtime, and span identifier values are covered by one opaque black mask.

Limits: Captured after the Raw09 motion recording ended; not a frame extracted from source09 motion. The version tag belongs to an ingested historical span and does not prove current instrumentation, a live debugger session, or source retrieval.

- Original: `56-ingested-version-tag.png` (1180 × 729 px; 91402 bytes)
- Capture-file modification time (UTC): 2026-10-08T06:20:42.354976Z
- Capture context: Screenshot-only capture taken after the Raw09 motion recording ended, according to the capture sequence supplied by the recording operator. Not extracted from source09 motion.
- Source crop [x, y, width, height]: [354, 430, 810, 299]
- Output: 810 × 299 px; 75238 bytes
- Opaque black mask: source [508, 546, 300, 84]; output [154, 116, 300, 84]; RGB [0, 0, 0], opacity 1. Remove the values of process_id, runtime-id, and span_id, including adjacent identifier controls.
- Original SHA-256: `c6d3ac1d9d54b743a936f77d06b3a8326af90ab298190e76464737a7dcfcb488`
- Output SHA-256: `efd0d0b2fa9bcbf8802d16b220b1ae5babc9932b8dc84412da6a60b9b9ddbf3f`

## 57-screenshot-only-ingested-env-commit.png

Screenshot-only: a separately captured historical span detail shows env staging and the actual git.commit.sha tag pixels. The isolated view contains no repository or account identity.

Limits: Captured after the Raw09 motion recording ended; not a frame extracted from source09 motion. The commit tag was explicitly retained for this artifact. An ingested commit tag identifies historical trace metadata; it does not establish that source files were retrieved, that the currently running process uses that commit, or that Live Debugger is enabled.

- Original: `57-ingested-env-and-commit.png` (1180 × 729 px; 91764 bytes)
- Capture-file modification time (UTC): 2026-10-08T06:21:31.967837Z
- Capture context: Screenshot-only capture taken after the Raw09 motion recording ended, according to the capture sequence supplied by the recording operator. Not extracted from source09 motion.
- Source crop [x, y, width, height]: [354, 430, 810, 299]
- Output: 810 × 299 px; 94020 bytes
- Masks: none; privacy treatment is the crop only.
- Original SHA-256: `7d3fa3a3b9ebedb809d4409bba573d5c40af09f308b3cae3985a1a60531464bf`
- Output SHA-256: `20f4f7348e91ec26bd609227bd390626e429fa9a377ab7f0d2e40a753d2cf5ad`
