#!/usr/bin/env python3
"""wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """_summary_

    Args:
        max_delay (int): _description_

    Returns:
        asyncio.Task: _description_
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
