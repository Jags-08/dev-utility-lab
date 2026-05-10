---
title: "Refactor: Convert legacy string formatting to f-strings"
labels: ["refactor", "tech-debt", "good first issue"]
---

### Description
There are a few places in the older codebase (mostly in error handling or older CLI logic) that might still be using `.format()` or `%s` style string formatting. 

We should standardize the entire codebase to use Python 3.6+ f-strings for better readability and slight performance improvements.

### Tasks
- [ ] Scan `dev_utils/cli.py` for `.format()`.
- [ ] Scan `dev_utils/logger.py` formatting logic.
- [ ] Update to modern f-strings.
- [ ] Verify `pytest` and `ruff` still pass.
