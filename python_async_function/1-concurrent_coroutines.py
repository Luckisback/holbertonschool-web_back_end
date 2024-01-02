#!/usr/bin/python3

""" A function that import a module from a previous file
and use a routine to display in sorted time"""


import asyncio
from typing import List
from importlib import import_module
wait_random = import_module('0-basic_async_syntax').wait_random


async def wait_n(n :int, max_delay : int) -> List[float]:
    l = []
    async def wait_and_append():
        nonlocal l
        for i in range(n):
            a = await wait_random(max_delay)
            l.append(a)
    await asyncio.gather(*(wait_and_append() for _ in range(n)))
    return sorted(l)
