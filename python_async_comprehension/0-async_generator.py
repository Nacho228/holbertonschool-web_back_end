#!/usr/bin/env python3
""" coroutine called async_generator
that takes no arguments."""
import asyncio
import typing
import random


async def async_generator() -> typing.Generator[float, None, None]:
    """Coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10."""
    for i in range(10):
        rndm = random.uniform(0, 10)
        yield rndm
        await asyncio.sleep(1)
