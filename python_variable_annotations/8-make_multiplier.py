#!/usr/bin/env python3
""" type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that multiplies a float
    with a multiplier
    Params:
    Multiplier: float.
    Return: a function that multiplies a float
    with a multiplier
    """
    def multiplier_function(n: float) -> float:
        """Function that returns a float
        multiplied by a multiplier"""
        return n * multiplier

    return multiplier_function
