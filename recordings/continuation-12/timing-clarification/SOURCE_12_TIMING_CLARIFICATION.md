# Source 12 timing clarification

The source declares a nominal 20 fps rate but has 61,009 stored frames across 3050.85 seconds. Four adjacent timestamp steps exceed the usual 0.05 seconds; the maximum step is 0.30 seconds. The gaps total 0.40 seconds beyond the usual steps. The uniform 20-fps timeline has 61,017 positions.

In both original frozen manifests, source_start_frame and source_end_frame_exclusive are nominal 20-fps timeline indices computed from seconds. They are not physical stored-frame ordinals. The nominal source rate fps=20 has the same qualification.

This sidecar supplies zero-based stored-frame ordinal ranges and timestamp bounds for every retained archive section and highlight chapter. Half-open source timestamp ranges remain the primary cut references.

The sanitized videos use constant 20-fps playback at original elapsed speed, holding recorded frames across sparse timestamp gaps. No in-between UI image was generated. A cut can begin at the first available stored frame at or after its timestamp, so do not infer finer precision than the available source frames.

All original sanitized videos, manifests, maps and checksums remain unchanged. This clarification corrects frame-number interpretation and records the source timestamp gaps. It does not replace screenshot-only evidence with motion.

Detailed corrected ordinal/timestamp mappings and original-manifest hashes are in [SOURCE_12_TIMING_CLARIFICATION.json](SOURCE_12_TIMING_CLARIFICATION.json).
