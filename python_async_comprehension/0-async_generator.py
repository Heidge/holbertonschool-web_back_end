#!/usr/bin/env python3
"""
Module async_generator
Génère des nombres aléatoires de manière asynchrone.
"""
       
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ async function coroutine random float return """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
