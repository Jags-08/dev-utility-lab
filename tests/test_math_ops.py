import pytest
from dev_utils.math_ops import add, factorial, is_even, is_prime, fibonacci, gcd, lcm

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(11) is True
    assert is_prime(1) is False
    assert is_prime(-7) is False

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5

def test_gcd():
    assert gcd(48, 18) == 6

def test_lcm():
    assert lcm(4, 6) == 12
