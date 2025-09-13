"""
Assignment 1 - Lists & Dictionaries Warm-Up
CSC148 Prep Assignment

Complete the functions below.
Do NOT use built-in functions like reversed(), max(), or sum() 
where it defeats the purpose.
"""


def reverse_list_iterative(lst: list[int]) -> list[int]:
    """Return a new list that is lst reversed, computed iteratively.

    >>> reverse_list_iterative([1, 2, 3])
    [3, 2, 1]
    """
    ...

def reverse_list_recursive(lst: list[int]) -> list[int]:
    """Return a new list that is lst reversed, computed recursively.

    >>> reverse_list_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    ...


def count_frequencies(lst: list[str]) -> dict[str, int]:
    """Return a dictionary mapping each unique string in lst 
    to the number of times it appears.

    >>> count_frequencies(["a", "b", "a", "c", "b", "a"])
    {'a': 3, 'b': 2, 'c': 1}
    """
    ...


def nested_max(lst: list) -> int:
    """Return the maximum integer in a possibly nested list of integers.

    >>> nested_max([1, [2, [3, 4]], 5])
    5
    >>> nested_max([[[-1, -5], -2], -3])
    -1
    """
    ...


def top_student(grades: dict[str, list[int]]) -> str:
    """Return the name of the student with the highest average grade.

    >>> top_student({"Alice": [100, 90], "Bob": [70, 80, 90], "Carol": [95, 100]})
    'Carol'
    """
    ...