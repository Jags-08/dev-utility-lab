# Engineering Standards & Guidelines

All repositories under this operational umbrella must adhere to strict engineering constraints to project highly mature development practices.

## 1. Commits & Branches
*   **Linear History:** Squash and merge all PRs into `main`. The root commit tree must remain pristine.
*   **Branch Naming:**
    *   `feat/your-feature-name`
    *   `fix/bug-description`
    *   `docs/what-changed`
    *   `chore/maintenance-task`
*   **Commit Messages:** Must follow Conventional Commits format (`type: brief description`). Let GitHub auto-generate the squashed commit body using PR descriptions.

## 2. PR Structure & Quality
*   Every PR *must* have a description. Naked PRs are prohibited.
*   PRs must explicitly state what tests were added or modified to validate the change.

## 3. Code Standards
*   **Coverage:** Minimum 90% test coverage enforced natively via Pytest and coverage pipelines.
*   **Linting:** `ruff` must pass completely without warnings on all Python codebases prior to commit. Pre-commit hooks should enforce this locally.
*   **Typing:** Strict `mypy` typing required. Standardized to Python 3.11+.

## 4. Documentation Minimums
*   All public API functions must contain docstrings detailing Parameters, Return types, and at least one reproducible `Example:`.
*   All projects must have an Architecture or usage flow-chart in their `README.md`.
