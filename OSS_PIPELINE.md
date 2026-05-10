# Operations: OSS Contribution Pipeline

A systematic approach to contributing to external Open Source Software (OSS) to predictably scale the **Open Sourcerer** and **Pull Shark** achievements while building authentic long-term maintainer trust.

## Phase 1: Repository Discovery
*   **Target Profile:** 100-5,000 stars. Active within the last 7 days. Welcoming maintainer tone.
*   **Discovery Queries:**
    *   `org:pallets topic:flask is:open` (Flask ecosystem)
    *   `label:"good first issue" language:python interactions:>5`
    *   `topic:testing label:"help wanted"`

## Phase 2: Issue Filtering & Selection
*   **High Probability Targets:** 
    1.  Test coverage gaps.
    2.  Documentation typos or missing examples.
    3.  Deprecation warnings (e.g., upgrading an old `datetime` format).
*   **Avoid:** 
    *   Major feature request pipelines (takes too long to merge).
    *   "Fix a typo in a comment" across the whole repo (flagged as spam).

## Phase 3: The Contribution Protocol
1.  **Fork & Clone:** Execute work locally. Verify all local tests pass completely before staging.
2.  **Branch Naming:** `fix/issue-#-brief-desc` or `docs/add-usage-examples`.
3.  **PR Structure:** 
    *   Use the repository's provided PR template.
    *   If none exists, clearly state: **Problem**, **Solution**, **Testing Done**.
    *   Keep the PR scope fiercely precise. 1 issue = 1 PR.

## Phase 4: Follow-up & Merge Optimization
*   **SLA:** Respond to maintainer code-review comments within 12 hours.
*   **Etiquette:** Thank maintainers for their time. Do not ping them requesting reviews unless 14 days have passed.
*   **Trust Building:** Once your first PR is merged, immediately ask: *"Thanks for merging! Are there any other low-hanging tests/docs I could help cover this week?"*
