# Datadog Live Debugger and Source Code Integration audit

V12 consolidated checkpoint: evidence frozen at **8 October 2026, 21:51:46.355 UTC**. The 63 original case definitions are preserved: **23 scoped PASS, 8 FINDING, 19 IN_PROGRESS, 2 PENDING and 11 BLOCKED**. There are **10 distinct findings: 0 High, 4 Medium and 6 Low**. Seven unresolved topics remain outside the finding and severity totals. This is an evidence checkpoint, not release signoff.

Live capture and exact source attribution work in the tested setup. This continuation adds actual same-target metadata repairs, concurrent C1/C2 execution, application restart, Agent interruption and a bounded nine-request burst. The new evidence strengthens coverage without adding a confirmed finding or completing every original case branch.

## Read the results

- [Severity-ranked findings](findings.md#severity-ranked-finding-index), [High only](high-severity.md), [Medium](findings.md#medium-severity), [Low](findings.md#low-severity)
- [Part 1 beginner UX](QA_MATRIX.md#track-1-complete-beginner-ux) and [Part 2 detailed functional QA](QA_MATRIX.md#track-2a-live-debugger-functional-depth)
- [All 63 original outcomes](QA_MATRIX.md), [supplemental executed records](EXECUTED_CHECKS.md), [evidence](EVIDENCE.md), [unresolved topics](UNCONFIRMED_OBSERVATIONS.md)
- [Current state and cleanup](CURRENT_STATUS.md), [remaining work and gates](REMAINING_WORK.md), [reviewed recordings](VIDEOS.md), [glossary](glossary.md)

The [37-page V12 PDF](report.pdf) and [editable V12 Word report](report.docx) consolidate this checkpoint and supersede the earlier 31-page V9 documents. The reports and web pages use the same ten-finding inventory and current case accounting.

## What this continuation established

- All six original failing metadata profiles recovered exact A/C1 tags and selected-event source after the actual repair stage. Their service, version and probe identities were preserved. S06 remains partial because generic diagnostics and shared-editor recovery require separate assessment.
- C1 and C2 actually executed concurrently under one service and staging environment. Sampled payload timestamps, distinct values and exact revision/path/line attribution support scoped X01 PASS. The original line-17 target's per-instance behavior on C2 remains unresolved under X05.
- Application restart recovered the same probe with a new process generation. Actual Agent stop and restoration receipts establish an outage and subsequent capture by the same application process. F18 and F19 retain their untested or unresolved branches.
- The bounded burst completed 9 of 9 requests in 0.26 seconds, with healthy checks before and after. It does not establish a capture-rate limit, sampling contract or the original same-target baseline comparison.
- Direct links, Back/Forward and rapid C1 → C2 → C1 selection restored the correct settled capture and source. Immediate frames briefly retained prior content, so S07 remains partial; no persistent mismatch or new defect is claimed.
- Distinct same-basename paths and bounded complex-value controls succeeded. The Unicode/space-path installation error is confounded by the fixture's direct loader, including an ASCII control, and is not a confirmed Unicode product bug.
- The existing FUNC01 dirty-draft loss repeated. Reloads and a fresh row support the accepted state, but a stale second write was never accepted. Earlier scoped S04, S05, S09 and F14 results remain valid within their recorded boundaries.

## Current state and remaining scope

The bounded workflow was observed successful at **21:20:54 UTC**, with explicit completion of its owned-runtime cleanup. At **21:28:36 UTC**, the unfiltered session list showed **All 7 / Active 0 / Inactive 7**. Later retained navigation stayed inactive. C01/C02 remain partial for broader retained-resource, settings, grant and identity reconciliation; accounts, keys, repositories, approved A-only source scope and fixture history are retained.

The grouped campaign has run. The [remaining plan](REMAINING_WORK.md) identifies the specific unfinished original branches and distinguishes them from fixture corrections, independent-identity requirements and approval gates. The production-labeled synthetic probe was never created; its capture still requires explicit approval.

Sources **01–17**, including sources 16 and 17, now have reviewed archives and highlights. Source 15's long idle interval, source 16's foreground limits, source 17's crashes and recovery, and checks made after recording stopped are disclosed in the [catalog](VIDEOS.md). Screenshots use genuine crops, opaque privacy masks and disclosed outlines. No missing motion or UI transition has been reconstructed.
