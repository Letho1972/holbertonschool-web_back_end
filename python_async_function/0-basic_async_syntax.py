#!/usr/bin/env python3

"""Write an asynchronous coroutine that takes in an integer argument"""


import asyncio
import random

# Definition of the asynchronous coroutine


async def wait_random(max_delay: float = 10) -> float:
    # Generates a random delay between 0 and max_delay as a float value
    delay = random.uniform(0, max_delay)

    # Waits for the generated duration
    await asyncio.sleep(delay)

    # Returns the generated delay
    return delay

# Main function to run the coroutine in the asyncio event loop


async def main():
    # Calls and awaits the result of the wait_random coroutine
    result = await wait_random()

    # Prints the generated random delay
    print(f"Random delay: {result} seconds")
