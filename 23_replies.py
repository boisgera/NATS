import asyncio
import math

import nats
from rich.jupyter import display
import typer

app = typer.Typer()

global nc


async def connect():
    global nc
    nc = await nats.connect("demo.nats.io")


async def greet(to, reply_to):
    await nc.publish(to, f"👋 Greetings {to}!".encode("utf-8"), reply=reply_to)
    await nc.drain()
    await nc.close()

async def display_reply(reply_to):
    print(f"🕵️ Waiting for reply with subject {reply_to}") 
    # 🪲 for some reason, blocked below, even when I (manually) reply.
    msg = await sub.next_msg(timeout=math.inf)
    print("*")
    print(f"💬 Reply received: {msg.data.decode('utf-8')}")


async def async_main(to):
    global sub
    await connect()
    reply_to = "000" # nc.new_inbox()
    sub = await nc.subscribe(reply_to)
    async with asyncio.TaskGroup() as tg:
        tg.create_task(display_reply(reply_to))
        tg.create_task(greet(to, reply_to))


@app.command()
def main(to: str):
    asyncio.run(async_main(to))


if __name__ == "__main__":
    app()
