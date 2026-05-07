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
