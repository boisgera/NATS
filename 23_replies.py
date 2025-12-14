import asyncio
import math

import nats
import typer

app = typer.Typer()

async def greet(to, reply_to):
    await nc.publish(to, f"👋 Greetings {to}!".encode("utf-8"), reply=reply_to)

async def display_reply(reply_to):
    print(f"🕵️ Waiting for reply with subject {reply_to}") 
    msg = await sub.next_msg(timeout=math.inf)
    print(f"💬 Reply received: {msg.data.decode('utf-8')}")


async def async_main(to):
    global nc, sub
    nc = await nats.connect("demo.nats.io")
    reply_to = nc.new_inbox()
    sub = await nc.subscribe(reply_to)
    async with asyncio.TaskGroup() as tg:
        tg.create_task(display_reply(reply_to))
        tg.create_task(greet(to, reply_to))

@app.command()
def main(to: str):
    asyncio.run(async_main(to))


if __name__ == "__main__":
    app()
