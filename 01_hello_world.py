import asyncio
import nats

async def main():
    nc = await nats.connect("demo.nats.io") # official NATS demo server
    #nc = await nats.connect() # local NATS server

    sub = await nc.subscribe("foo")
    await nc.publish("foo", b"Hello from Python!")
    msg = await sub.next_msg()
    print("Received:", msg)

    await nc.flush()
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())