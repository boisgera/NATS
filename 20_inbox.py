import asyncio
import datetime
import math
import sys


import nats
import typer

app = typer.Typer()

async def heartbeat(name, dt):
    nc = await nats.connect("demo.nats.io")

    while True:
        await nc.publish("❤️", name.encode("utf-8"))
        await asyncio.sleep(dt)

async def display_inbox(name):
    nc = await nats.connect("demo.nats.io")
    sub = await nc.subscribe(f"name")
    while True:
        message = await sub.next_msg(math.inf)
        text = message.data.decode("utf-8")
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"----- 📬 {time} reply-to: {message.reply}")
        print(text)

async def async_main(name: str = "anonymous", dt : float = 1.0):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(heartbeat(name, dt))
        tg.create_task(display_inbox(name))

@app.command()
def main(name: str = "anonymous", dt : float = 1.0):
    asyncio.run(async_main(name, dt))

if __name__ == "__main__":
    app()
