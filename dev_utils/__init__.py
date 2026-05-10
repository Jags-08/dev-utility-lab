"""
dev_utils 

A professional Python utility package.
"""

__version__ = "0.2.0"

from .math_ops import add, factorial, is_even, is_prime, fibonacci, gcd, lcm
from .string_ops import reverse_string, is_palindrome
from .random_ops import random_int, random_choice, shuffle_list, generate_password
from .data_ops import read_file, read_json
from .logger import logger, setup_logger
from .config import config, Config

__all__ = [
    "add", "factorial", "is_even", "is_prime", "fibonacci", "gcd", "lcm",
    "reverse_string", "is_palindrome",
    "random_int", "random_choice", "shuffle_list", "generate_password",
    "read_file", "read_json",
    "logger", "setup_logger",
    "config", "Config"
]
