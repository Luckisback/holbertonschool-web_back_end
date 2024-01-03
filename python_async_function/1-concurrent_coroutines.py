#!/usr/bin/env python3

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    """ Sort the delays in ascending order """
    sorted_delays = sorted(delays)
    return sorted_delays
