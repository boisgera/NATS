import asyncio
import math

import nats

names = []

async def collect():
    nc = await nats.connect("demo.nats.io")
    sub = await nc.subscribe("❤️")
    while True:
        message = await sub.next_msg(math.inf)
        name = message.data.decode("utf-8")
        names.append(name)

async def alive(timeout):
    try:
        await asyncio.wait_for(collect(), timeout=timeout)
    except asyncio.TimeoutError:
        sorted_names = sorted(list(set(names)))
        return sorted_names

async def main(timeout):
    names = await alive(timeout)
    for name in names:
        print(name)


if __name__ == "__main__":
    asyncio.run(main(timeout=3.0))