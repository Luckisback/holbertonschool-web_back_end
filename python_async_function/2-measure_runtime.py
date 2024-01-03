#!/usr/bin/env python3

import asyncio
import time
from typing import List
from concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_execution = total_time / n
    return average_time_per_execution
