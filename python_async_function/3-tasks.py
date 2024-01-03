#!/usr/bin/env python3
import asyncio
import importlib
module = importlib.import_module("0-basic_async_syntax")


wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
