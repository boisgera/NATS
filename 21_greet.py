import asyncio
import math


import nats
import typer

app = typer.Typer()

async def greet(name):
    nc = await nats.connect("demo.nats.io")
    await nc.publish(name, f"👋 Greetings {name}!".encode("utf-8"))
    await nc.drain()
    await nc.close()

async def async_main(name):
    await greet(name)

@app.command()
def main(name: str):
    asyncio.run(async_main(name))

if __name__ == "__main__":
    app()
