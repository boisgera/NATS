# Python Standard Library
import asyncio
import json
import math

# Third-Party Libraries
import httpx
import nats
import nats.aio.client
import nats.aio.msg
import typer

# Chuck Norris jokes API URL (see: https://api.chucknorris.io/).
API_URL = "https://api.chucknorris.io/jokes"

# Accept a plain text request, the subject of the joke search.

app = typer.Typer()


async def fetch_and_reply(
    httpx_client: httpx.AsyncClient,
    nats_client: nats.aio.client.Client,
    request: nats.aio.msg.Msg,
) -> None:
    query = request.data.decode("utf-8")
    response = await httpx_client.get(f"{API_URL}/search", params={"query": query})
    response.raise_for_status()
    json_response = response.json()
    await nats_client.publish(
        request.reply,
        json.dumps(json_response).encode("utf-8"),
    )


async def async_main():
    httpx_client = httpx.AsyncClient()
    nats_client = await nats.connect("demo.nats.io")
    sub = await nats_client.subscribe("chuck norris jokes")
    while True:
        message = await sub.next_msg(math.inf)
        asyncio.create_task(
            fetch_and_reply(httpx_client, nats_client, message)
        )


@app.command()
def main(subject: str):
    asyncio.run(async_main(subject))


if __name__ == "__main__":
    app()
