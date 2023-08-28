#!/usr/bin/env python3
""" type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float."""


def sum_list(input_list: list) -> float:
    """
    Returns the sum of all floats
    from input_list
    Params: input_list
    Return: float
    """
    return sum(map(float, input_list))
