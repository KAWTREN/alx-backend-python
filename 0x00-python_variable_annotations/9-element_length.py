#!/usr/bin/env python3
"""Module Documentation"""
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """values with the appropriate types"""
    return [(i, len(i)) for i in lst]
