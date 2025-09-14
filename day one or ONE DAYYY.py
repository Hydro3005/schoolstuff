"""
Assignment 0 - Functions Warm-Up
CSC148 Prep Assignment

Complete the functions below.
"""

def factorial_iterative(n: int) -> int:
    """Return n! computed iteratively.
    Precondition: n >= 0
    """
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result 


def factorial_recursive(n: int) -> int:
    """Return n! computed recursively.
    Precondition: n >= 0
    """
    # base case
    if n == 0 or n == 1:
        return 1
    #recursive case
    return n * factorial_recursive(n - 1)



def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, ignoring case and spaces.

    Examples:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Race car")
    True
    >>> is_palindrome("hello")
    False
    """
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]


def max_in_list(lst: list[int]) -> int:
    """Return the maximum element in lst.
    Precondition: len(lst) > 0
    """
    return max(lst)

               