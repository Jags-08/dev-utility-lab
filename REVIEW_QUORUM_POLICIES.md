# Review Quorum Policies

Establishes strict requirements: N-2 reviewers required for standard merges, N-1 for architectural mutations, and emergency bypass constraints.

## Exception Handling & Deadlocks

In the event of a 48-hour N-2 deadlock, the temporal reviewer escalation chain triggers automatically. Bypass is prohibited.

## Quorum Escalation Safety

If the primary review council is unable to reach consensus within 7 days (extended absence default), the StewardshipLead assumes tie-breaking authority to prevent operational deadlock.
## Multi-Stage Review Escalation
If a PR fails at any stage (Governance, Survivability, or Operations), it is returned to the author. Re-submission triggers a full restart of the asynchronous pipeline.