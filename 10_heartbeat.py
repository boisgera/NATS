import asyncio
import datetime
import sys


import nats
import typer


app = typer.Typer()

async def heartbeat(name, dt):
    nc = await nats.connect("demo.nats.io")

    while True:
        await nc.publish("❤️", name.encode("utf-8"))
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"{time} ❤️ {name}", file=sys.stderr)
        await asyncio.sleep(dt)


@app.command()
def main(name: str = "anonymous", dt : float = 1.0):
    asyncio.run(heartbeat(name, dt))


if __name__ == "__main__":
    app()
