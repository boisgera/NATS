from math import inf

import asyncio
import nats


async def main() -> None :
    nats_client = await nats.connect("nats://7.tcp.eu.ngrok.io:11933")
    sub = await nats_client.subscribe("clock")

    while True:
        message = await sub.next_msg(timeout=inf)
        print("epoch:", message.data.decode("utf-8"))

if __name__ == '__main__':
    asyncio.run(main())

