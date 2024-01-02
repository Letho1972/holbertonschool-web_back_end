#!/usr/bin/env python3

"""Write a type-annotated func make_multiplier that takes a float multi"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its argument by the given multiplier.

    Args:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    take a single argument and multiplies it by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
