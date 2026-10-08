# Runtime continuation screenshot privacy and provenance manifest

Lossless RGB PNG derived from genuine original screenshots. Only rectangular crops and fully opaque privacy masks are applied; no scaling, blur, generative redraw, replacement UI, annotations, or stitched regions. Original files are unchanged. Coordinates are source-space, zero-based, half-open (left, top, right, bottom). Opaque masks are RGB (32,32,32).

Personal account headers, avatars, repository identifiers, and unrelated application content are excluded or fully occluded. No raw email or one-time authentication-code screens are included. Blurred source placeholders visible inside Datadog are part of the original application UI, not new privacy edits.

Interrupted installation-flow recovery candidate only: the original form had been left open about 75 minutes. Fresh-install behavior and underlying cause are unestablished. No app revoke/reinstall. The initial ten images show draft validation and source-connection state. Added submission evidence below shows visible rejection; no successful session creation or variable capture is claimed.

All ten files were inspected before editing. Retained pixels were compared exhaustively against their original source crop, and each masked pixel was verified fully opaque. All PNGs contain only IHDR, IDAT, and IEND chunks; no source JPEG bytes, EXIF, thumbnails, comments, or trailing data are embedded. Original source SHA-256 hashes are included for provenance.

## 30-github-return-empty-integration-public.png

Captured: 2026-10-08T04:50:15Z

Datadog GitHub Apps configuration remains at Get Started / Connect GitHub Account after callback. Crop removes personalized top bar and navigation.

Source: 30-github-return-empty-integration.jpg

Source SHA-256: ef26e90d90d396aa7d073b6ed2213edaa60bc652a2c87420c1b5422edebe1518

Public SHA-256: 751e19f1183d5c91ecac21c6dbcf9240bac70021a12c93a4ca9f21875c5ca452

Crop: [160, 78, 1180, 676]; output dimensions: [1020, 598].
Masks: [].

## 32-github-installed-a-only-public.png

Captured: 2026-10-08T04:51:29Z

GitHub lists Datadog Official as installed. This viewport does not show the selected repository; scope evidence is screenshot 38. Crop removes account header, avatar, and unrelated settings navigation.

Source: 32-github-installed-a-only.jpg

Source SHA-256: 18e3b940bbf28cfc19f1fea681cf4086f7e51a540399f03f66bdad43f69fe270

Public SHA-256: 72e7278a55d342ff67d1f3035983dd2c27d8ed2bed6564931bb61f47f54f889a

Crop: [326, 154, 1136, 523]; output dimensions: [810, 369].
Masks: [].

## 37-github-authorized-apps-public.png

Captured: 2026-10-08T04:56:26Z

GitHub Authorized GitHub Apps lists Datadog Official with Never used. Crop removes identity header and navigation; opaque masks remove application count and unrelated authorized-app row.

Source: 37-github-authorized-apps.jpg

Source SHA-256: de7476176bcf511b67ffafd9d2160cd524110444771be13d1c95b9cfdbebacd5

Public SHA-256: 595a345ebe6bcf399a2f3a4b78ba8d222a9ce9140d07534f27dbdb2da666f146

Crop: [326, 154, 1136, 545]; output dimensions: [810, 391].
Masks: [[326, 268, 780, 311], [326, 322, 1136, 410]].

## 38-a-only-after-b-created-public.png

Captured: 2026-10-08T05:06:05Z

GitHub repository access shows Only select repositories and Selected 1 repository after the separate fixture was created. Opaque mask hides private account/repository identity. The visible screenshot alone does not identify the selected repository; the test log establishes it as fixture A.

Source: 38-a-only-after-b-created.jpg

Source SHA-256: 8c0a7069b0766d68f9841a97cb8ea42194ac517f84bc816b6119942db59b3deb

Public SHA-256: fd408f359261462780844108eb16574625159a092b98d89de157617851e6635e

Crop: [325, 26, 1140, 665]; output dimensions: [815, 639].
Masks: [[417, 323, 807, 352]].

## 33-service-all-environments-warning-public.png

Captured: 2026-10-08T04:53:17Z

Manual logpoint dialog warns that Live Debugger is not enabled and all-environments creation will not enable it automatically. Draft only; no capture.

Source: 33-service-all-environments-warning.jpg

Source SHA-256: 4f0739e2ef28ce56495e32a636dc0e89e406dafc1d675cdb24c6fc632e6a4932

Public SHA-256: 7f57c4ebea516ef2e4b61f2487573ea289879cdf5c255543ecf1ba2363407d76

Crop: [44, 48, 1121, 713]; output dimensions: [1077, 665].
Masks: [].

## 34-line-zero-validation-public.png

Captured: 2026-10-08T04:54:43Z

Line 0 keeps Start Debug Session disabled. The application-rendered blurred source placeholder is retained exactly.

Source: 34-line-zero-validation.jpg

Source SHA-256: 3e9d1f45ae698f4ac44944d275ee6b2da61d295368ee7c6c2bfed99864e5f194

Public SHA-256: 8f4366461376ab3f3366ec2b945501bef63d65dd85a2f1aeb8ecd125b099fa61

Crop: [52, 48, 1114, 713]; output dimensions: [1062, 665].
Masks: [].

## 35-line-out-of-range-draft-public.png

Captured: 2026-10-08T04:55:10Z

Line 9999 permits a draft and enables Start Debug Session. It was not submitted; no runtime rejection or line relocation was tested. This is not a confirmed defect.

Source: 35-line-out-of-range-draft.jpg

Source SHA-256: 3de7d7076d8b24e77f72f46be121d1c50a51f1c8e654bfce82ebcb9a99913f28

Public SHA-256: c8bb7b098593e035647b126c5f52535ba84043b98ef9641147f3855f0fae7c44

Crop: [52, 48, 1114, 713]; output dimensions: [1062, 665].
Masks: [].

## 36-source-unavailable-guidance-public.png

Captured: 2026-10-08T04:55:34Z

Expanded source guidance states that the file was not found and names missing permissions or incorrect source integration tags as possible causes.

Source: 36-source-unavailable-guidance.jpg

Source SHA-256: a3dfe51cbff5edad4f5976656ca383d755ccc821a0edb0cec01cf20a60d72ea0

Public SHA-256: d9d139668fe599a8753b20745ab99920d5d229e810a5f5f15b20bc1c9b0bbd93

Crop: [44, 48, 1121, 713]; output dimensions: [1077, 665].
Masks: [].

## 40-unmatched-brace-actual-public.png

Captured: 2026-10-08T05:06:52Z

Actual unmatched brace QA quantity={quantity disables Start Debug Session. No session submitted.

Source: 40-unmatched-brace-actual.jpg

Source SHA-256: 2f5950d53b6c265bb68b7069b3b2ac86c22c9037522f5f3b1fec19acc0e5cb31

Public SHA-256: 7d18bc53249650515b85fb0dde31437aad58cfb9f102a6b39244d26fab950308

Crop: [44, 48, 1121, 713]; output dimensions: [1077, 665].
Masks: [].

## 41-valid-template-recovery-public.png

Captured: 2026-10-08T05:08:14Z

Corrected QA quantity={quantity} total={total_cents} enables Start Debug Session. No session submitted.

Source: 41-valid-template-recovery.jpg

Source SHA-256: 6792bfad4f55c9018eb1df02af7674c3602c44ec4fdf67beec005e98c1fa884e

Public SHA-256: 6d5b07890aae6707b892181cc56b07164dc7d224641ee42d5713b1c9fa453d85

Crop: [44, 48, 1121, 713]; output dimensions: [1077, 665].
Masks: [].

## Final verification

All 10 exported PNGs were visually reviewed at original resolution after editing. Source hashes were rechecked and are unchanged. Retained pixels, opaque masks, and PNG metadata/chunk boundaries passed exhaustive checks. The exports have no generative changes or red-box annotations.

## Extension: actual submission error and settled configuration

Source integration evidence is an interrupted installation-flow recovery issue: original form had been left open about 75 minutes; fresh-install behavior and underlying cause are unestablished. No app revoke/reinstall. Screenshots 30–41 show draft validation and source connection state. The added screenshot 44 and raw07 frame show actual visible submission rejection with an error toast, not silent failure. Screenshot 46 shows no environments found. No successful session creation, installed logpoint, or variable capture is claimed. Cause of the configuration rejection remains unresolved.

Screenshot 45 is excluded: the full empty-state heading was below its captured viewport.

### 44-plain-template-submit-result-public.png

Plain-message control QA baseline produces the actual error toast: Error creating logpoint: The instrumentation is not valid, please check your configuration. Complete toast and modal retained. Surrounding header/background excluded or masked. This is a visible submission rejection, not a silent failure.

Source: runtime-screenshots/44-plain-template-submit-result.jpg

Source SHA-256: f71fe8a6f39f6b65673636805f100332703e79dd4be57a6b10c7687e294a0f4c

Public SHA-256: bfc0e0ab6a916d6539cf2596823a23c944c9aa1fd57ace11d65d604f1619c2bf

Crop: [44, 12, 1121, 713]; dimensions: [1077, 701].

Masks: [[44, 12, 260, 48], [920, 12, 1121, 48]].

### 46-settled-service-no-environments-public.png

Settled service-specific Configuration page shows the full No environments found heading and the Live Debugger Setup service picker. Source integration cards above show Grant Access. This clean scrolled screenshot supports the empty-state text; screenshot 45 does not because its heading was below the fold.

Source: runtime-screenshots/46-settled-service-no-environments.jpg

Source SHA-256: bef0cae71e06fbd4d4752c4e61288979eaf4579aa2b422937f912201250927dd

Public SHA-256: d36eba60504aa165d2736df64a4c6218fa08e551e970174b2ce88c7afeeca432

Crop: [158, 35, 1150, 665]; dimensions: [992, 630].

Masks: [].

### submit-error-toast-public.png

Genuine frame extracted from raw07 at offset 1579.5 seconds. Actual error toast above the intact manual-logpoint modal: Error creating logpoint: The instrumentation is not valid, please check your configuration. This attempt used the valid quantity/total template; browser chrome, desktop, and account background excluded or masked. This is a visible submission rejection, not a silent failure.

Source: continuation-review/submit-error-toast.png

Source SHA-256: a18d603b86e9f0613f2c8f29ab2c3cf52138381b3bff68ea979706b35ead110f

Public SHA-256: 85a28ed6b199adb23a410d4a091359d561dbeeb24f77fd210b08c03887badcd3

Crop: [136, 215, 1213, 916]; dimensions: [1077, 701].

Masks: [[136, 215, 352, 251], [1012, 215, 1213, 251]].

### Extension verification

All three additional exported PNGs were visually reviewed at original resolution. Complete error-toast text and full modal are retained in both submission images. The settled configuration heading is fully visible in screenshot 46. Retained-pixel and opaque-mask checks passed; all thirteen original source hashes remain unchanged.

## Final V6 extension: post-blur validation and Python Function draft

Both originals were inspected in full before cropping. These are direct rectangular crops only: no masks, scaling, generated UI, or annotations were needed. Personalized headers and unrelated application content are outside the crops. The red validation border in screenshot 47 is genuine application-rendered UI.

### 47-invalid-template-after-blur-public.png

Captured: 2026-10-08T05:38:08Z

After focus moved to the line field, the invalid log template QA {quantity has a genuine application-rendered red outline and Start Debug Session is disabled. This is draft validation evidence; no session submission or variable capture is claimed. Crop retains the full modal and excludes personalized header and unrelated application navigation.

Source: runtime-screenshots/47-invalid-template-after-blur.jpg

Source SHA-256: 97dd0e1653f1edf258a0d2ec1ec2a4c1c3bd715a6c2aa2faab37b4b7dec6367b

Public SHA-256: 8b593cc1d9d2cc1f57249a80c4c143a5ed88c715f9395b6bd1b2c8f9a967a89c

Crop: [44, 48, 1121, 713]; dimensions: [1077, 665].

Masks: [].

### 48-python-function-draft-public.png

Captured: 2026-10-08T05:39:50Z

Python Function mode shows Module pricing and Function calculate_quote, with valid log template QA {quantity} and Start Debug Session enabled. This is a draft only; no successful submission, installed logpoint, or variable capture is claimed. Crop retains the full modal and excludes personalized header and unrelated application navigation.

Source: runtime-screenshots/48-python-function-draft.jpg

Source SHA-256: 40ab1adfb69cd9ad40a722ed004838e95d662d59b31e1f5808e9231c141df3e3

Public SHA-256: e07316d1cf16bf43c75b550af80410a0574df8f858c203a7f6427341cb9068d9

Crop: [52, 48, 1114, 713]; dimensions: [1062, 665].

Masks: [].

### Final V6 verification

Both additional exported PNGs were visually reviewed at original resolution. All fifteen source hashes and public-image hashes were rechecked; every retained pixel and existing opaque privacy mask passed exhaustive comparison. All fifteen sanitized PNGs contain only IHDR, IDAT, and IEND chunks, with valid CRCs, no trailing bytes, and no embedded metadata. The prior thirteen manifest entries, all prior images, and the SCI01 annotation manifest and annotated image are unchanged.
