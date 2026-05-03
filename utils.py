def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def reverse_string(s):
    """
    Returns the reverse of the input string s.
    """
    return s[::-1]

def is_palindrome(s):
    """
    Checks if the string s is a palindrome.
    Ignores spaces and case.
    """
    # Clean the string by removing spaces and converting to lowercase
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def is_even(n):
    """
    Returns True if n is an even number, False otherwise.
    """
    return n % 2 == 0
