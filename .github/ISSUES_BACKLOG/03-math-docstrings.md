---
title: "Docs: Add usage examples for all math_ops functions"
labels: ["documentation", "good first issue"]
---

### Description
The docstrings in `dev_utils/math_ops.py` explain what the functions do, but they lack concrete usage examples within the docstrings themselves.

Adding `Examples:` blocks to the docstrings will make the code much more accessible and will help if we ever auto-generate documentation via Sphinx/MkDocs later.

### Tasks
- [ ] Update `factorial` docstring with an example.
- [ ] Update `gcd` and `lcm` docstrings with examples.
- [ ] Update `is_prime` docstring with examples handling edge cases (0, 1, negatives).
