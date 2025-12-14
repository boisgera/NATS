import asyncio
import math


import nats
import typer

app = typer.Typer()

async def greet(sender, to):
    nc = await nats.connect("demo.nats.io")
    await nc.publish(to, f"👋 Greetings {to}!".encode("utf-8"), reply=sender)
    await nc.drain()
    await nc.close()

async def async_main(sender, to):
    await greet(sender, to)

@app.command()
def main(sender : str, to: str):
    asyncio.run(async_main(sender, to))

if __name__ == "__main__":
    app()
