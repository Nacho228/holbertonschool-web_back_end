#!/usr/bin/env python3
""" type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all floats and int
    from mxd_list
    Params: mxd_list
    Return: float
    """
    return sum(mxd_lst)
