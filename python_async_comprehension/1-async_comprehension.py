#!/usr/bin/env python3
"""Async_generator from the previous task and then write a
coroutine called async_comprehension that takes no arguments."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[int]: _description_
    """
    collected = [i async for i in async_generator()]
    return collected
