#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and should be annotated as a float. 
"""
from typing import Union
from typing import Tuple



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Cast an int or float v and str k to
    a Tuple being [k, v]
    Params: 
    k: str.
    v: float or int.
    Return: tuple[k, v]
    """
    squared = (v * v)
    return (k, squared)
