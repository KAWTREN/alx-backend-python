#!/usr/bin/env python3
"""Module documentation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    def multiplier_function(value: float) -> float:
        """multiplier a float by multiplier"""
        return value*multiplier
    return multiplier_function
