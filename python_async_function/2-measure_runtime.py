#!/usr/bin/env python3

import time
from typing import List
import importlib
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    result = wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_task = total_time / n
    return average_time_per_task
