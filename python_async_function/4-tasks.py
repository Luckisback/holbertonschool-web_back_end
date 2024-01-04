#!/usr/bin/python3

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    """ Sort the delays in ascending order """
    sorted_delays = sorted(delays)
    return sorted_delays
