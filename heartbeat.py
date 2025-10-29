# Python Standard Library
pass

# Third-Party Libraries
import asyncio
import nats


async def heartbeat(nats_client=None, subject="heartbeat", data=b"", delay=1.0):
    if nats_client is None:
        nats_client = await nats.connect()
    while True:
        await nats_client.publish(subject, data)
        await asyncio.sleep(delay)


async def main():
    await heartbeat()


if __name__ == "__main__":
    asyncio.run(main())
