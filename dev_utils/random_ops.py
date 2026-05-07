import random
import string

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

def shuffle_list(lst):
    """
    Shuffles a list in place and returns it.
    """
    random.shuffle(lst)
    return lst

def generate_password(length=12):
    """
    Generates a random password of a given length using letters and digits.
    
    Example:
        pwd = generate_password(16)
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
