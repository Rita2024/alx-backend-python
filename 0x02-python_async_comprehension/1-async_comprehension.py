#!/usr/bin/env python3
"""1-async_comprehension.py"""

from typing import List

async_gen = __import__("0-async_generator").async_gen


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing
    over async_generator then returns 10 random numbers.
    """
    result = [number async for number in async_gen()]

    return result
