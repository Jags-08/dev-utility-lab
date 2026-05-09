import random
import string
from typing import List, TypeVar

T = TypeVar('T')

def random_int(a: int, b: int) -> int:
    """
    Returns a random integer N such that a <= N <= b.
    """
    return random.randint(a, b)

def random_choice(lst: List[T]) -> T:
    """
    Returns a randomly selected element from the non-empty sequence lst.
    """
    return random.choice(lst)

def shuffle_list(lst: List[T]) -> List[T]:
    """
    Shuffles a list in place and returns it.
    """
    random.shuffle(lst)
    return lst

def generate_password(length: int = 12) -> str:
    """
    Generates a random password of a given length using letters and digits.
    
    Example:
        pwd = generate_password(16)
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
