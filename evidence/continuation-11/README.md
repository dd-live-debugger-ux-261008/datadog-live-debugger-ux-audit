# Sanitized live debugger evidence

The original JPEG files were retained unchanged. Safe PNGs use only integer-coordinate crops and opaque identity masks. All retained, unmasked pixels exactly match the decoded originals. Screenshot 67 has a separately labeled annotation copy with three red outlines. No UI was reconstructed.

Coordinates, file SHA-256 values, decoded pixel hashes, annotation geometry, and pixel-preservation checks appear in manifest.json and per-image provenance JSON files.

## Captions

### 60: 60-github-free-plan-visible-safe.png

Visible GitHub billing overview shows current metered usage $0, current included usage $0, and a GitHub Free subscription at $0.00 per month. This screenshot does not show an Actions minute allowance or quota.

### 62: 62-runtime-sdk-registration-safe.png

Visible GitHub Actions log excerpt reports live_debugging_registered=true, python_client_present=true, sdk_4_11_0_present=true, and symbol_database_registered=true. These status booleans establish reported SDK registration in the excerpt; they are not themselves evidence of captured application values.

### 63: 63-staging-environment-available-safe.png

The new-session environment dropdown visibly offers staging, with the manual New Session control below. Runtime/service identity is masked.

### 64: 64-logpoint-before-submit-safe.png

The pre-submit logpoint form visibly targets pricing.py line 17 in staging and requests all variables up to 3 levels deep. The Start Debug Session button is still present; the screenshot does not by itself establish submission.

### 65: 65-initial-enable-logs-state-safe.png

The initial debugger view simultaneously shows INSTRUMENTING, No events, an Enable logs to view events banner, and a file-not-found-in-repository warning. This records the displayed state, not proof that a Logs setup change is required.

### 66: 66-log-explorer-receiving-events-safe.png

Log Explorer visibly contains 45 logs and recent nonzero histogram bars. The onboarding popover partially obscures the table. This still frame confirms that logs are present; the absence of an intervening setup mutation comes from the run chronology, not the pixels alone.

### 67: 67-verified-quantity-three-safe.png

Verified capture displays quantity=3, discount_eligible=False, discount_cents=0, subtotal_cents=3600, total_cents=3600, and unit_price_cents=1200. The intended application total of 3240 is task context, not text shown in the screenshot. The pricing discrepancy is the planted application bug, not a Datadog defect. EVENTS RECEIVED and the repository-source warning are also visible.

### 68: 68-session-duration-menu-safe.png

The open Set Session Duration menu visibly offers 1 Hour, 1 Day, 2 Days, and 1 Week. The shortest displayed option is 1 Hour. The screenshot does not establish a universal API or product minimum outside this menu.

### 69: 69-verified-quantity-two-safe.png

Verified capture displays quantity=2, discount_eligible=False, discount_cents=0, subtotal_cents=2400, total_cents=2400, and unit_price_cents=1200. This is the quantity-two comparison capture.

## Limits

- Source 60 does not contain the numeric Actions allowance or quota.
- Source 62 is a visible runtime status excerpt, not a full raw log or a capture result.
- Source 64 shows a pre-submit form.
- Source 65 records a transient displayed state. Source 66 confirms logs exist; chronology is needed to establish that no setup mutation intervened.
- Source 67 records a planted application bug. It must not be described as a Datadog pricing or capture defect.
- Source 68 supports the shortest option in the displayed menu, not a claim about all product/API limits.

Only the files named *-safe.png and the explicitly annotated 67 PNG are prepared for screenshot publication. Do not publish the original JPEGs.
