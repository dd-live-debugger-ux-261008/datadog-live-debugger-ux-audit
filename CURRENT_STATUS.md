# Audit continuation status

8 October 2026 at 10:05 UTC (06:05 New York)

**The planned live-capture baseline now passes.** The debugger SDK registered in the hosted synthetic runtime. At pricing.py line 17 in staging, the message template `QA quantity={quantity} total={total_cents}` rendered correctly and actual captured locals matched all three controls: quantity 2 → total 2400; quantity 3 → total 3600 with discount eligibility False; quantity 4 → subtotal 4800, discount 480, eligibility True and total 4320. F01 is now PASS for this tested baseline. The quantity-3 result exposes the deliberately planted application pricing bug; it is not a Datadog defect.

**Source association recovered after a controlled reinstall.** The same A-only GitHub App scope was removed and reinstalled with approval. The fresh callback reached connected configuration at 09:55 UTC, while private repository B remained ungranted. SCI01 retains the original interrupted-flow result and now has a verified recovery path. This does not prove that the earlier 75-minute pause caused the failure. Exact source retrieval and deployed-revision matching remain separate tests.

The initial runtime and additional telemetry approvals have been received. The audit-workspace reset was recovered using a hosted runtime and the intact public/Library report artifacts. The report continuation source is also now preserved in Library. Prior unpublished originals from the reset workspace are unavailable; published privacy-reviewed evidence remains intact.

The V7 PDF and ledger retain their explicit 06:28 UTC historical cutoff. Their earlier runtime blockers are being reconciled as new tests complete. No new Datadog finding has been confirmed in this continuation, and no end-to-end completion is claimed. The initial “Enable logs” state recovered after navigating to existing logs and refreshing, without a Logs setup change; this remains a scoped observation under retest.

[Historical report](report.pdf) · [Case outcomes](QA_MATRIX.md) · [Findings](findings.md) · [Recording catalog](VIDEOS.md)
