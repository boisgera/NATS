import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # NATS

      - URL: https://nats.io/

      - Python library: https://github.com/nats-io/nats.py
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import asyncio
    from math import inf
    import json
    import time
    return asyncio, inf, json, time


@app.cell
def _():
    import httpx
    import nats
    return httpx, nats


@app.cell
async def _(nats):
    nats_client = await nats.connect()
    nats_client
    return (nats_client,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Services
    """)
    return


@app.cell
def _(asyncio, nats_client):
    async def heartbeat(subject="❤️", data=b"", delay=1.0):
        while True:
            print("*")
            await nats_client.publish(subject, data)
            print("**")
            await asyncio.sleep(delay)
            print("***")
    return (heartbeat,)


@app.cell
def _(asyncio, nats_client, time):
    async def clock(subject="clock", delay=1.0):
        while True:
            epoch = time.time()
            await nats_client.publish(subject, str(epoch).encode("utf-8"))
            await asyncio.sleep(delay)
    return (clock,)


@app.cell
def _(asyncio, inf, nats_client, time):
    async def epoch():
        sub = await nats_client.subscribe("epoch")
        while True:
            message = await sub.next_msg(timeout=inf)
            reply_to = message.data.decode("utf-8")
            epoch = time.time()
            await nats_client.publish(reply_to, str(epoch).encode("utf-8"))
            await asyncio.sleep(0.0)
    return


@app.cell
def _(asyncio, inf, json, nats_client):
    async def greet():
        sub = await nats_client.subscribe("greet")
        while True:
            message = await sub.next_msg(timeout=inf)
            json_data = json.loads(message.data.decode("utf-8"))
            name = json_data["name"]
            reply_to = json_data["reply_to"]
            await nats_client.publish(reply_to, f"Hello {name}! 👋".encode("utf-8"))
            await asyncio.sleep(0.0)
    return


@app.cell
def _(asyncio, httpx, inf, json, nats_client):
    ISS_URL = "http://api.open-notify.org/iss-now.json"
    httpx_async = httpx.AsyncClient()

    async def ISS_location():
        sub = await nats_client.subscribe("ISS_location")
        while True:
            message = await sub.next_msg(timeout=inf)
            reply_to = message.decode("utf-8")
            response = await httpx_async.get(ISS_URL)
            json_data = response.json()
            await nats_client.publish(reply_to, json.dumps(json_data).encode("utf-8")) 
            await asyncio.sleep(0.0)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Select the services
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Test the services
    """)
    return


@app.cell
async def _(asyncio, heartbeat, nats_client, time):
    # 🪲: doesn't work, but clock does (???)
    async def f():
        hb = asyncio.create_task(heartbeat(subject="hb", delay=1.0,  data="."))
    
        _t0 = time.time()
        heartbeat_sub = await nats_client.subscribe("hb")
        for _ in range(10):
            a = await heartbeat_sub.next_msg(timeout=5.0)
            print(a.data)
            _t1 = time.time()
            _dt = _t1 - _t0
            _t0 = _t1
            print(f"{_dt:.1f}")
        await heartbeat_sub.unsubscribe()
        return hb.cancel()
    await f()
    return


@app.cell
def _():
    #_s = await nats_client.subscribe("❤️")
    #[
    #    await _s.next_msg(timeout=3.0),
    #    await _s.next_msg(timeout=3.0),
    #    await _s.next_msg(timeout=3.0),
    #]
    #await _s.next_msg(timeout=3.0)
    return


@app.cell
async def _(asyncio, clock, nats_client, time):
    cl = asyncio.create_task(clock(delay=3.0))

    await asyncio.sleep(5.0)

    _t0 = time.time()
    clock_sub = await nats_client.subscribe("clock")
    for _ in range(10):
        message = await clock_sub.next_msg(timeout=20.0)
        _epoch = float(message.data)
        _t1 = time.time()
        _dt = _t1 - _t0
        _t0 = _t1
        print(f"{_epoch} {_dt:.1f}")
    await clock_sub.unsubscribe()
    cl.cancel()
    return


@app.cell
async def _(nats_client):
    inbox_name = "boisgera" 
    inbox = await nats_client.subscribe(inbox_name)
    return


@app.cell
def _():
    #await inbox.next_msg(timeout=15.0)
    return


if __name__ == "__main__":
    app.run()
