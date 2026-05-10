# Open Source Targets Strategy (Open Sourcerer Accelerator)

To scale the "Open Sourcerer" achievement authentically, we must strategically target repositories where contributions are valued, reviewed quickly, and merged successfully.

## Targeting Criteria
1.  **Fast Merge/Response Times:** Repositories known for active maintainers (check recent closed PR history).
2.  **Clear Scope:** Repositories with well-defined `good first issue` or `help wanted` tags.
3.  **Low to Medium Star Count (100 - 5,000):** These repos are often desperate for help and don't have the massive PR backlog of mega-projects like Django or Pandas.
4.  **Alignment:** Python, Flask, CLI tools, testing libraries.

## Target Categories & Specific Strategies

### Category 1: Testing & Utility Libraries (Python)
These libraries constantly need edge-case coverage and documentation updates.
*   **Search Queries:** `topic:python topic:testing`, `topic:utility language:python`
*   **Ideal Contribution:** Adding test coverage for obscure parameters, fixing typos in docstrings, standardizing type hints.
*   **Expected Turnaround:** 1-3 days.
*   **Strategy:** Find files lacking 100% coverage, write a quick test, submit PR.

### Category 2: Flask Extensions
The Flask ecosystem consists of hundreds of smaller, unmaintained extensions.
*   **Search Queries:** `topic:flask-extension`, `flask-*`
*   **Ideal Contribution:** Modernizing code for newer Python versions (e.g., updating `setup.py` to `pyproject.toml`), fixing deprecation warnings from newer Flask versions.
*   **Expected Turnaround:** 3-7 days.
*   **Strategy:** Run tests on Python 3.11+, fix any `DeprecationWarning` exceptions, submit refactor PRs.

### Category 3: CLI Tools & Developer Environments
Similar alignment to `dev-utility-lab`.
*   **Search Queries:** `topic:cli language:python`, `topic:developer-tools`
*   **Ideal Contribution:** Improving error messages (making them more user-friendly), adding shell completion scripts, formatting code with `ruff` or `black` (if project accepts formatting PRs).
*   **Expected Turnaround:** 2-5 days.
*   **Strategy:** Use the tool, find a confusing error message, patch the exception handler locally, submit a PR explaining the UX improvement.

### Category 4: Documentation Sites
Projects using MkDocs or Sphinx.
*   **Ideal Contribution:** Fixing broken links, correcting markdown syntax, adding missing examples from the codebase into the docs.
*   **Expected Turnaround:** 1-2 days.
*   **Strategy:** Read documentation of tools you use, fix typos immediately via GitHub UI or quick local clone.

## Anti-Spam Guidelines
*   **DO NOT** submit PRs that only fix a single typo unless it's in a critical README header. Bundle typo fixes into larger "Docs Cleanup" PRs.
*   **DO NOT** run automated formatters on a whole repository without opening an issue first to ask permission.
*   **ALWAYS** run the project's test suite locally before submitting. A failing CI run on your PR damages credibility.
