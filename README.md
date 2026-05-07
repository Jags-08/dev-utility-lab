# dev-utility-lab

A growing collection of clean, reusable Python utility functions for everyday development tasks.

## Features

- **Math Utilities**: Arithmetic, factorial, Fibonacci sequences, prime checking, GCD, and LCM.
- **String Manipulation**: Reversing strings and checking palindromes.
- **Randomization**: Random integers, choices, and list shuffling.
- **File & Data Operations**: Reading files safely and parsing JSON documents.
- **Security Utilities**: Generating random passwords.

## Example Usage

Here are examples of how to use our utilities:

```python
from utils import add, is_prime, read_json, generate_password

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

1. Clone the repository to your local machine.
2. Import `utils.py` into your Python projects.
3. Start using the utility functions!

