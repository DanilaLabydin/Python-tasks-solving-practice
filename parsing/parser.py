import asyncio
from time import time


import aiometer
import httpx


session = httpx.AsyncClient()


async def scrape(url):
    response = await session.get(url)
    return response.status_code


async def run():
    _start = await aiometer.run_on_each(scrape)
