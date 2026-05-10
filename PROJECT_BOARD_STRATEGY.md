# Project Board Strategy

Deploying GitHub Project Boards simulates a rigorous agile environment, enhancing the visible maturity of the profile.

## The Global Ecosystem Board
Use a single Organization/User-level GitHub Project board to funnel all issues across the ecosystem (Flagship + Micro-repos) into one macroscopic view.

## Board Columns (Kanban Style)
1.  **Backlog:** All incoming ideas, un-triaged issues, and non-immediate documentation needs.
2.  **To Do (Current Sprint):** The specific 3-5 issues targeted for the active week.
3.  **In Progress:** Issues actively assigned and being worked on locally right now. Limit WIP (Work In Progress) to 2 items max to ensure PRs actually get finished.
4.  **In Review:** PR generated, awaiting CI pass or maintainer read over.
5.  **Done:** Merged and closed.

## Milestone Management
*   Attach every repo issue to a Milestone matching a Semantic Version (`v0.2.0`, `v1.0.0`).
*   Close the Milestone formally alongside the GitHub Release deployment.
*   This visualizes "Engineering Completion Percentages" directly on the repository homepage.

## Sprint Simulation
*   **Duration:** 2 Weeks.
*   **Grooming:** Every other Monday (see `WEEKLY_OPERATIONS.md`), pull items from Backlog into To Do. If an item sits in Backlog for >3 months without movement, convert it to a Discussion or close it.
