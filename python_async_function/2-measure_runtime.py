#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
, and returns total_time / n."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function that mesures time 
    Params:
    n: int
    max_delay: int
    Return: total_time / n float 
    """
    start_timer = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_timer = time.time()
    total_time = stop_timer - start_timer
    result = (total_time / n)

    return result
