#!/usr/bin/env python3

""" Write a type-annotated function concat that takes a string """

def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Parameters:
    - str1 (str): The first string.
    - str2 (str): The second string.

    Returns:
    - str: The concatenated string.
    """
    result = str1 + str2
    return result
