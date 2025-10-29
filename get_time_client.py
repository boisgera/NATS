# Python Standard Library
from math import inf
import time
import uuid

# Third-Party Libraries
import asyncio
import nats


async def get_time(nats_client=None, subject="clock", delay=1.0) -> None:
    if nats_client is None:
        nats_client = await nats.connect()
    self = str(uuid.uuid4())
    sub = await nats_client.subscribe(self)
    await nats_client.publish("get_time", self.encode("utf-8"))
    message = await sub.next_msg(timeout=inf)
    epoch = message.data.decode("utf-8")
    print(f"Current time: {epoch}")


if __name__ == "__main__":
    asyncio.run(get_time())
