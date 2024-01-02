#!/usr/bin/env python3

""" Write a type-annotated function to_kv and returns a tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v as arguments
    and returns a tuple with the first element as the string k
    and the second element as the square of v (annotated as a float).
    """
    result = (k, float(v) ** 2)
    return result
