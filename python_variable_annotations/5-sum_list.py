#!/usr/bin/env python3

""" Write a type-annotated function sum_list which takes a list input_list of floats as argument """

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
    - input_list (List[float]): List of floats.

    Returns:
    - float: Sum of the input_list elements.
    """
    return sum(input_list)
