#!/usr/bin/env python3

"""Write a type-annotated function sum_mixed_list which takes a list mxd_lst"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in the given list.

   Args:
    - mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
    - float: The sum of the elements in the list as a float.
    """
    result_sum = 0.0
    for num in mxd_lst:
        result_sum += float(num)
    return result_sum
