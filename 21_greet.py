import asyncio
import math


import nats
import typer

app = typer.Typer()

async def greet(name):
    nc = await nats.connect("demo.nats.io")
    await nc.publish("name", f"👋 Greetings {name}!".encode("utf-8"))
    await nc.drain()
    await nc.close()

async def async_main(name: str = "anonymous", dt : float = 1.0):
    await greet(name)

@app.command()
def main(name: str = "anonymous", dt : float = 1.0):
    asyncio.run(async_main(name, dt))

if __name__ == "__main__":
    app()
