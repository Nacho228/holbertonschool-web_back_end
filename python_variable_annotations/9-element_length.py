#!/usr/bin/env python3
"""Annotate the below functions parameters and
return values with the appropriate types"""
from typing import Iterable, Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return [(i, len(i)) for i in lst]"""
    return [(i, len(i)) for i in lst]
