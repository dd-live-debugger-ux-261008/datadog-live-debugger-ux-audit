# Logpoint draft validation: publication-safe stills

Two genuine captured UI stills show the unbalanced template and the corrected draft. This package is prepared locally; it does not publish anything.

## What the evidence shows

- Image 58: `QA {quantity` has a red outline, and Start Debug Session appears disabled. The supplied interaction record places this after blur and confirms the disabled control.
- Image 59: `QA {quantity}` has balanced braces. The red outline is absent and Start Debug Session is blue; the supplied interaction record confirms the control became enabled.

Neither state was submitted. The visible warning says Live Debugger is not enabled for this service and that an all-environments logpoint will not enable it automatically. An enabled draft does not establish successful debugger enablement, instrumentation, source retrieval, a started debug session, or received snapshots.

A separate DOM inspection reportedly found that the Line control had no accessible name. Pixels alone cannot establish accessible-name semantics, an absent programmatic error association, or a WCAG violation. These stills document visual draft validation and correction; they are not titled or classified as a confirmed accessibility failure.

## Transformation and privacy

Each original is 1180 × 729 px. The source crop is [60, 56, 1046, 648], expressed as [x, y, width, height] with a top-left origin and half-open extents. No resizing or masks were needed. The crop removes global/profile chrome and the surrounding background, including any account or repository context. It retains the generic demonstration service, `pricing.py`, Line 17, the warning, template, and Start control.

The blurred code-preview area was already present in the captured UI. No blur, annotation, generated UI, replacement text, or reconstructed pixels were added. Every output pixel was checked against the corresponding decoded source crop.

Despite their `.png` filenames, both originals contain JPEG-encoded bytes. The originals were preserved exactly. The derivatives are genuine RGB PNG files, losslessly encoded from the decoded cropped source pixels, with embedded source metadata stripped. JPEG compression already present in the originals is not reversed by PNG export.

## Recording context and time caveat

The supplied operator record places source10 motion at 2026-10-08 06:23:43–06:28:13.750 UTC, with a normal stop at 06:28:14 UTC and no submission. These files are screenshot derivatives, not frames extracted from that motion recording. The recording interval is supplied context, not derived from filesystem timestamps.

The UTC modification times listed below are filesystem provenance only. They may reflect copying or export and are not independently verified capture times, UI-event times, ingestion times, or trace-event times.

Only this new publication folder was written. Original screenshots and all previous frozen09/V6 media were not edited or replaced. The folder is flat and contains only two PNGs, this README, the exact crop/hash manifest, and SHA256SUMS. SHA256SUMS covers the two PNGs, README.md, and manifest.json; originals are deliberately excluded.

## 58-invalid-template-draft.png

An unsubmitted logpoint draft shows the unbalanced template QA {quantity with a red outline and a pale, disabled-looking Start Debug Session control. The supplied recording sequence places this state after focus moved away from the template.

Limits: This image supports a visual validation observation only. The control state and blur sequence also rely on the separately supplied interaction record; pixels alone do not establish accessibility semantics or prove that an accessible error was absent.

- Original file: `58-invalid-template-programmatic-feedback.png`
- Original format: JPEG; 75675 bytes
- Original SHA-256: `4cc014ab7786ae0dbc548640d19df828614eeb841e5f507657d3720a83d6bfd1`
- Source filesystem mtime (UTC): 2026-10-08T06:26:32.285084Z
- Crop [x, y, width, height]: [60, 56, 1046, 648]
- Masks: none
- Output: 1046 × 648 px; RGB PNG; 225036 bytes
- Output SHA-256: `d0133627102058f4e4dc7145b621f19f9e350b4085f71b06d079fe30c918f30a`

## 59-corrected-template-draft.png

The draft template is corrected to QA {quantity}. The red outline is absent and Start Debug Session appears blue; the interaction record identifies the corrected draft as enabled.

Limits: An enabled draft is not a submitted logpoint or a started session. The service warning remains visible. This still does not establish successful debugger enablement, current instrumentation, source retrieval, or received snapshots.

- Original file: `59-valid-template-correction.png`
- Original format: JPEG; 75960 bytes
- Original SHA-256: `fc830cdc274f7221ddf3e9b5775b891128af06aea2c34dbcf4cfbd7f4d0fcf20`
- Source filesystem mtime (UTC): 2026-10-08T06:27:24.045986Z
- Crop [x, y, width, height]: [60, 56, 1046, 648]
- Masks: none
- Output: 1046 × 648 px; RGB PNG; 230309 bytes
- Output SHA-256: `7b9b3673e7829c90924b2915eb171d86d7b87ccd86b889f1b8e706c54228ed48`
