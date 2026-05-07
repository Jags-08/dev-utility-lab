import pytest
import sys
import os

# Add the parent directory to the path so we can import utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import (
    add,
    factorial,
    reverse_string,
    is_palindrome,
    is_even,
    is_prime
)

def test_add():
    """Test the addition utility function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_factorial():
    """Test the factorial utility function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    
    # Test that a negative number raises a ValueError
    with pytest.raises(ValueError):
        factorial(-1)

def test_reverse_string():
    """Test the string reversal utility."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("racecar") == "racecar"

def test_is_palindrome():
    """Test the palindrome checker, including space/case ignorance."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("No lemon no melon") is True

def test_is_even():
    """Test the even number checker."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True

def test_is_prime():
    """Test the prime number checker."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(11) is True
    assert is_prime(1) is False  # 1 is not prime
    assert is_prime(-7) is False
