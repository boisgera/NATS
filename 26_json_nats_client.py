# Python Standard Library
import asyncio
import math
import json

# Third-Party Libraries
import nats
import typer
from typer.cli import app


async def async_main(subject: str):
    nats_client = await nats.connect("demo.nats.io")
    reply = nats_client.new_inbox()
    sub = await nats_client.subscribe(reply)
    await nats_client.publish(
        "chuck-norris-jokes",
        subject.encode("utf-8"),
        reply=reply,
    )
    msg = await sub.next_msg(math.inf)
    data = json.loads(msg.data.decode("utf-8"))
    for joke_data in data["result"]:
        print(f"- {joke_data['value']}")


app = typer.Typer(help="fetch Chuck Norris jokes based on free-text queries.")


@app.command()
def main(subject: str):
    asyncio.run(async_main(subject))

if __name__ == "__main__":
    app()