# OSS Fork & Momentum Workflow

## Target: `psf/requests` (or similar high-profile Python repo)

We are actioning the day 1 target through a clean fork-and-branch execution.

## Execution Steps

**1. Create Fork & Clone**
```bash
# Ensure GitHub CLI is logged in
gh auth login

# Fork and clone locally
gh repo fork psf/requests --clone
cd requests
```

**2. Branch Naming**
Create a highly specific, scoped branch name:
```bash
git checkout -b docs/clarify-timeout-advanced-usage
```

**3. Target Fix**
* Navigate to `docs/user/advanced.rst` (or equivalent file).
* Find the `Timeouts` section.
* Add a professional clarification note about tuple-based timeouts (e.g., `(connect_timeout, read_timeout)`).

**4. Commit Strategy**
```bash
git add docs/user/advanced.rst
git commit -m "docs: clarify tuple usage for connection vs read timeouts"
git push origin docs/clarify-timeout-advanced-usage
```

**5. PR Draft Information**
* **Title:** `docs: clarify tuple-based timeouts in advanced usage`
* **Description:** 
  > Hello! While reviewing the advanced usage documentation for timeouts, I noticed the distinction between the connection timeout and read timeout in a tuple `(connect, read)` could be slightly more explicit for beginners to avoid `ReadTimeout` confusion. 
  > 
  > This minor patch adds a brief example block to clarify. Let me know if you'd like any wording changes!

**Why this is perfect for Day 2:**
It seeds an OSS pull request on a massive repository without stepping on core logic toes. It ensures your graph shows cross-repo activity (Open Sourcerer growth) completely separate from your internal Java engineering.