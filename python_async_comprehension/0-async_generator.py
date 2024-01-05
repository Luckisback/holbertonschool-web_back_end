#!/usr/bin/env python3

""" A Asyncronous generator """
import asyncio
import random


async def async_generator():
    """ definition of the Asyncronous generator """
    
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
