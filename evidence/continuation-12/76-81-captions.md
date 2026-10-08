# Continuation 12 source-backed controls: 76–81

These additional stills retain source code and capture data while masking account, runtime/service, and private repository identities. Every retained unmasked pixel is identical to the decoded original. No UI was reconstructed; no source or previous evidence file was modified.

## Timestamp and source-verification limits

The task owner independently read the actual Logs JSON snapshot timestamp 1791455041812, which converts to 2026-10-08 10:24:01.812 UTC. This is separate evidence from UI timestamp parameters and displayed event-list rows. The exact JSON timestamp is not printed in these stills. Screenshot 80 does not display the offscreen JSON Attributes fields. Screenshot 78 visibly prints the full source revision; screenshot 81 displays only its abbreviated selector f506150.

## Captions

### 76: 76-control-template-with-source-safe.png

The pre-submit logpoint form visibly displays retrieved pricing.py source, line 17, environment staging, the CONTROL quantity={quantity} total={total_cents} template, and capture of all variables up to 3 levels deep. The source includes discount_eligible = quantity > 3 and its explicit intentional-bug comment. The Start Debug Session button remains visible; this still records the prepared form rather than proving submission.

### 77: 77-control-events-with-source-safe.png

The debugger simultaneously shows retrieved source around pricing.py line 17, EVENTS RECEIVED, the CONTROL numeric template, approximately 30 events captured, and rendered event messages for quantities 2, 3, and 4 with totals 2400, 3600, and 4320. Event-list timestamps use the displayed UTC-07:00 offset. They are displayed row times, not independently established screenshot-acquisition or selected-capture timestamps.

### 78: 78-continuation-runtime-registered-safe.png

The visible runtime status excerpt reports live_debugging_registered=true, python_client_present=true, sdk_4_11_0_present=true, symbol_database_registered=true, sample_ready=true, and git_sha=f5061500e8bf30880aebcf7966ba64df44d2ccde. The full source revision remains visible. The complete updated_at values visible here include 2026-10-08T10:21:17.852526+00:00 and 2026-10-08T10:21:33.651416+00:00; these are runtime-status update times, not the later captured application snapshot time. This excerpt reports readiness and registration rather than independently proving an application capture.

### 79: 79-post-handover-control-capture-safe.png

The source-backed capture displays CONTROL quantity=3 total=3600 and all six captured values: quantity=3, discount_cents=0, discount_eligible=False, subtotal_cents=3600, total_cents=3600, unit_price_cents=1200. Retrieved source at pricing.py line 17 and EVENTS RECEIVED remain visible. This is the planted application bug, not a Datadog defect. The task owner independently verified the actual Logs JSON snapshot timestamp as 1791455041812 (2026-10-08 10:24:01.812 UTC). That exact timestamp is not printed in this still and must be attributed to the separate Logs JSON verification, not a UI timestamp parameter or a different event-list row.

### 80: 80-control-source-stacktrace-safe.png

The visible Logs stacktrace shows pricing.py line 17 in calculate_quote, retrieved source with line 17 highlighted, a GitHub source-link control, and quantity=3, discount_cents=0, discount_eligible=False, subtotal_cents=3600, total_cents=3600, unit_price_cents=1200. The second frame shows app.py line 32 in do_GET; private repository prefixes are masked. The JSON Attributes header is visible at the bottom, but its timestamp and source metadata fields are offscreen. The exact snapshot timestamp 1791455041812 (2026-10-08 10:24:01.812 UTC) and full source-revision association were separately verified by the task owner in Logs JSON; this screenshot must not be cited as displaying those offscreen fields.

### 81: 81-linked-revision-pricing-safe.png

The source-provider page visibly displays pricing.py with line 17 highlighted, the intentional quantity > 3 boundary bug, and the intended discount for orders of three or more in its docstring. The revision selector visibly reads f506150. The full deployed revision f5061500e8bf30880aebcf7966ba64df44d2ccde is separately established by the task owner and is printed in screenshot 78; the full revision is not visible in this screenshot. The file-history banner separately shows abbreviated commit 78457e9, which must not be confused with the selected revision. Repository and account identities are masked.

