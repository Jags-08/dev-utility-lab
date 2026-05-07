# dev-utility-lab

A growing collection of clean, reusable Python utility functions for everyday development tasks.

## Features

- **Math Utilities**: Arithmetic, factorial, Fibonacci sequences, prime checking, GCD, and LCM.
- **String Manipulation**: Reversing strings and checking palindromes.
- **Randomization**: Random integers, choices, and list shuffling.
- **File & Data Operations**: Reading files safely and parsing JSON documents.
- **Security Utilities**: Generating random passwords.

## Example Usage

Here are examples of how to use our utilities with the new modular package layout:

```python
from dev_utils.math_ops import add, is_prime
from dev_utils.data_ops import read_json
from dev_utils.random_ops import generate_password

# Math operations
print(add(5, 3))           # Output: 8
print(is_prime(11))        # Output: True

# Data operations
data = read_json('config.json')
print(data)

# Security operations
pwd = generate_password(16)
print(f"Generated secure password: {pwd}")
```

## Getting Started

Since `dev-utility-lab` is structured as a proper Python package, you can install it directly into your environment using `pip`!

1. Clone the repository to your local machine.
2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```
3. Import from the `dev_utils` package into your Python projects.

## Project Structure

```
dev_utils/
├── __init__.py     # Exposes all utilities
├── math_ops.py     # add, factorial, is_prime, fibonacci, gcd, lcm, etc.
├── string_ops.py   # reverse_string, is_palindrome
├── random_ops.py   # random_int, random_choice, shuffle_list, generate_password
└── data_ops.py     # read_file, read_json
```

## Testing and CI

This repository uses **pytest** for automated testing and **GitHub Actions** for Continuous Integration (CI). 

Every time code is pushed or a Pull Request is opened against the `main` branch, GitHub Actions will automatically provision an Ubuntu server, install the dependencies, and run the entire test suite. This ensures that we maintain a highly reliable and heavily tested utility library without any manual validation required on PRs!

To run tests locally:
```bash
pip install -r requirements-dev.txt
pip install -e .
pytest tests/
```

