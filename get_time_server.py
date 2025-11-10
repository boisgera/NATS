# Python Standard Library
from math import inf
import time

# Third-Party Libraries
import asyncio
import nats


async def server(nats_client=None, subject="clock", delay=1.0) -> None:
    if nats_client is None:
        nats_client = await nats.connect()
    sub = await nats_client.subscribe("get_time")
    while True:
        message = await sub.next_msg(timeout=inf)
        sender = message.data.decode("utf-8")
        epoch = time.time()
        await nats_client.publish(sender, str(epoch).encode("utf-8"))
        await asyncio.sleep(delay)


if __name__ == "__main__":
    asyncio.run(server())
