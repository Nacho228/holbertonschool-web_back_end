#!/usr/bin/env python3
""" Asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it."""
from typing import Union
import asyncio
import random


async def wait_random(max_delay: Union[int, float] = 10):
    """ """
    rndm = random.uniform(0, max_delay)
    await asyncio.sleep(rndm)
    return (rndm)
