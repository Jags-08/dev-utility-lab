# dev-utility-lab

A growing collection of clean, reusable Python utility functions for everyday development tasks.

## Features

- **Math Utilities**: Functions for basic arithmetic, factorial, Fibonacci sequences, prime checking, GCD, and LCM.
- **String Manipulation**: Tools for reversing strings and checking for palindromes.
- **Randomization**: Helpers for generating random integers, making random choices, and shuffling lists.
- **File Operations**: Simple functions to safely read file contents.

## Example Usage

Here are a few examples of how to use the provided functions:

```python
from utils import add, is_prime, reverse_string, shuffle_list

# Math operations
print(add(5, 3))           # Output: 8
print(is_prime(11))        # Output: True

# String manipulation
print(reverse_string("hello"))  # Output: "olleh"

# List operations
my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))    # Output: [3, 1, 5, 2, 4] (randomized)
```

## Getting Started

1. Clone the repository to your local machine.
2. Import `utils.py` into your Python projects.
3. Start using the utility functions!

