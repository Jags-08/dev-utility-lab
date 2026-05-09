# Getting Started

Welcome to `dev-utility-lab`! This guide will help you set up and start using the toolkit.

## Prerequisites
- Python 3.8 or higher.
- `pip` package manager.

## Installation

### From Source (Editable Mode)
This installs both the Python library and the built-in CLI:

```bash
git clone https://github.com/Jags-08/dev-utility-lab.git
cd dev-utility-lab
pip install -e .
```

## Using as a Python Library
Once installed, you can import functions directly into your scripts:

```python
from dev_utils.math_ops import add, factorial
from dev_utils.random_ops import generate_password

# Arithmetic
print(f"5 + 10 = {add(5, 10)}")

# Complex Math
print(f"5! = {factorial(5)}")

# Security Utilities
password = generate_password(length=16)
print(f"New password: {password}")
```

## Using as a CLI Tool
The installation automatically aliases `dev-utils` globally in your terminal. For an interactive feel, simply use the help command:

```bash
dev-utils --help
```

See the [CLI Examples](cli-examples.md) guide for sophisticated terminal use cases!