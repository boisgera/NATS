import asyncio
import math

import nats
from rich.live import Live
from rich.text import Text

names = []

async def collect():
    nc = await nats.connect("demo.nats.io")
    sub = await nc.subscribe("❤️")
    while True:
        message = await sub.next_msg(math.inf)
        name = message.data.decode("utf-8")
        names.append(name)

async def alive(timeout):
    global names
    try:
        await asyncio.wait_for(collect(), timeout=timeout)
    except asyncio.TimeoutError:
        sorted_names = sorted(list(set(names)))
        names = []
        return sorted_names

async def _main(timeout):
    names = await alive(timeout)
    for name in names:
        print(name)

async def main(timeout):
    with Live() as live:
        while True:
            names = await alive(timeout)
            text = "\n".join(names)
            live.update(Text(text))
            await asyncio.sleep(timeout)

if __name__ == "__main__":
    asyncio.run(main(timeout=3.0))