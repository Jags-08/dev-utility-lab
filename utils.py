import random

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

def is_prime(n):
    """
    Checks if a number is prime.
    
    A prime number is only divisible by 1 and itself.
    The loop runs from 2 up to the square root of n since any factor 
    greater than the square root must pair with a factor smaller than it.
    """
    if n < 2:
        return False
    # Check divisibility up to the square root of the number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def random_int(a, b):
    """
    Returns a random integer N such that a <= N <= b.
    """
    return random.randint(a, b)

def random_choice(lst):
    """
    Returns a randomly selected element from the non-empty sequence lst.
    """
    return random.choice(lst)

def lcm(a, b):
    """
    Computes the Least Common Multiple (LCM) of a and b.
    Requires gcd(a, b) to be available.
    """
    return abs(a * b) // gcd(a, b)

def gcd(a, b):
    """
    Computes the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a




