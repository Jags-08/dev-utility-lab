---
title: "Add hypothesis property-based testing for math_ops"
labels: ["enhancement", "testing", "good first issue"]
---

### Description
Currently, our `math_ops.py` functions (like `fibonacci`, `is_prime`) are tested with traditional unit tests containing specific known inputs. 

To improve robustness, we should integrate the `hypothesis` library to implement property-based testing. This will automatically generate a wide range of edge-case inputs (large integers, negative numbers, etc.) to ensure our functions behave predictably and don't panic unexpectedly.

### Tasks
- [ ] Add `hypothesis` to `requirements-dev.txt`
- [ ] Create a new test file `tests/test_math_properties.py`
- [ ] Implement property tests for `add`, `gcd`, and `lcm`.
- [ ] Ensure CI passes.
