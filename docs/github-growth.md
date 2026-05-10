# GitHub Discoverability and Growth Operations

To build a professional, highly visible engineering profile, we must treat GitHub as a discovery platform, utilizing SEO tactics, community management, and consistent release cycles.

## 1. Repository Optimization (SEO & Discoverability)
*   **Targeted Topics:** Ensure all repositories have exactly 5-8 highly relevant topics. For `dev-utility-lab`: `python`, `flask`, `developer-tools`, `workflow-automation`, `cli`.
*   **The "Above the Fold" README:**
    *   Strong headline.
    *   3-4 concise bullet points explaining value.
    *   Badges (CI pass, Coverage, Version).
    *   A compelling visual (Architecture diagram or CLI GIF).
*   **Description:** The repo description must explain *what it is* and *who it's for* in under 100 characters.

## 2. Release Management
*   **Semantic Versioning:** Strict adherence to `vX.Y.Z`. Release notes must separate `Features`, `Fixes`, and `Chores`.
*   **GitHub Releases:** Every tag must be accompanied by a formal GitHub Release.
*   **Frequency:** Aim for one formal release across your ecosystem every 2-3 weeks to trigger "New Release" notifications for watchers.

## 3. Issue and Project Management
*   **GitHub Projects:** Utilize a public GitHub Project board linked to your profile to track the development roadmap across your micro-repo ecosystem. This proves organizational capability.
*   **Issue Templates:** All new repositories must have bug and feature templates to enforce standardized reporting.
*   **Label Taxonomy:** Standardize labels across all repos (`bug`, `enhancement`, `good first issue`, `documentation`, `tech-debt`). 

## 4. Branch Strategy & PR Mechanics
*   **Never Push to Main:** All work must happen on feature branches (`feat/name`, `fix/issue-id`).
*   **PR Descriptions:** Every PR must have a summary, a "Why this is needed" section, and a checklist of testing completed. This creates a highly professional paper trail.
*   **Squash and Merge:** Keep the `main` branch history perfectly linear and clean.

## 5. Community Engagement
*   **Discussions Setup:** Enable GitHub Discussions on the flagship `dev-utility-lab` repository. Seed it with an "Introduce Yourself" thread and a "Q&A" section.
*   **Cross-Linking:** In your OSS PRs to other projects, tactfully link back to your repositories if relevant (e.g., "I encountered this while building `dev-utility-lab`...").
