#!/usr/bin/env python3
"""_summary_"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """

    start_time = time.time()
    bobaso = [async_comprehension() for i in range(4)]
    await asyncio.gather(*bobaso)
    end_time = time.time()
    return (end_time - start_time)
