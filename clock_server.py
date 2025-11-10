# Python Standard Library
import time

# Third-Party Libraries
import asyncio
import nats


async def clock(nats_client=None, subject="clock", delay=1.0) -> None:
    if nats_client is None:
        nats_client = await nats.connect()
    while True:
        epoch = time.time()
        await nats_client.publish(subject, str(epoch).encode("utf-8"))
        await asyncio.sleep(delay)


async def main():
    await clock()


if __name__ == "__main__":
    asyncio.run(main())
