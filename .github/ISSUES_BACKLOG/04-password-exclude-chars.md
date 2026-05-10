---
title: "Feature: Add option to exclude specific characters in password generator"
labels: ["enhancement", "feature"]
---

### Description
The `dev_utils.random_ops.generate_password` function is great, but sometimes systems have strict rules prohibiting certain characters (like quotes or brackets).

We should add an `exclude_chars` parameter to the function and the CLI.

### Tasks
- [ ] Update `generate_password` signature: `def generate_password(length: int = 12, exclude_chars: str = "") -> str:`
- [ ] Implement logic to remove `exclude_chars` from the pool of available characters before generation.
- [ ] Update `tests/test_random_ops.py` to verify the exclusion works.
- [ ] Add the flag to the `argparse` CLI implementation in `dev_utils/cli.py`.
