#!/usr/bin/env python3
"""wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that spawn wait_random n
    times with the specified max_delay.
    """
    tasks = []
    delays = []
    for _ in range(n):
        tasks.append(asyncio.create_task(task_wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
