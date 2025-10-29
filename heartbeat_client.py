from math import inf

import asyncio
import nats


async def main() -> None :
    nats_client = await nats.connect()
    sub = await nats_client.subscribe("heartbeat")

    while True:
        await sub.next_msg(timeout=inf)
        print("❤️", end="", flush=True)

if __name__ == '__main__':
    asyncio.run(main())

