#!/usr/bin/env python3

""" A function that waits for a random
number, and return it"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
