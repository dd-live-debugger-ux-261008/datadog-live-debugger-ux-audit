# Source 13 timing clarification

The source declares a nominal 20 fps rate but its stored frame timestamps are not perfectly uniform. There are 143,336 stored frames, beginning at 0.00 and ending at 7170.00 seconds; the container duration is 7170.05 seconds.

There are 43 timestamp gaps larger than the usual 0.05-second step. The gaps total 3.25 seconds beyond those usual steps. This yields 143,401 positions on a uniform 20 fps timeline, not 143,401 separately stored source frames.

In the original frozen archive/highlight manifests, source_start_frame and source_end_frame_exclusive are nominal 20 fps timeline indices computed from seconds. They are not physical stored-frame ordinals. The nominal rate fps=20 has the same qualification.

This sidecar supplies zero-based stored-frame ordinal ranges and timestamp bounds for every retained archive section and highlight chapter. Half-open source timestamp ranges remain the primary cut references.

The published videos play at constant 20 fps and original elapsed speed. Repeating or holding recorded frames across timestamp gaps is a playback conversion; no in-between UI image was generated. A chosen cut can begin at the first available stored frame at or after its timestamp, so do not infer finer temporal precision than the available recorded frames.

All prior sanitized videos, public manifests, maps and checksums remain unchanged. This clarification changes frame-number interpretation and explicitly records source timing gaps. It does not substitute screenshot-only observations for motion.

Detailed corrected ordinal/timestamp mappings and the hashes of both unchanged original manifests are in [SOURCE_13_TIMING_CLARIFICATION.json](SOURCE_13_TIMING_CLARIFICATION.json).
