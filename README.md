# NATS

The "Neural Autonomic Transport System", a cross-platform messaging technology.

[![NATS logo](images/nats-horizontal-color.png)](https://nats.io/)


## Prerequisites

Learn the basics of Python async:

- [ ] [IDS tutorial][github-asyncio]

For further information, use the [asyncio documentation][asyncio].

[github-asyncio]: https://github.com/boisgera/asyncio
[asyncio]: https://docs.python.org/3/library/asyncio.html

## Getting Started

- [ ] Have a look at [NATS : Connective Technology for Adaptive Edge & Distributed Systems](https://nats.io/),

- [ ] Install the [official NATS Python client and tools](https://github.com/nats-io/nats.py),

- [ ] Test the NATS client with `01_hello_world.py` (demo server),

- [ ] Install and start the NATS server binary/service,

- [ ] Adapt hello world to test your local NATS server.

## Primitives

Learn the basics of the [NATS Python client API](https://nats-io.github.io/nats.py/modules.html):

- [ ] `connect`

- [ ] `subscribe`

- [ ] `publish`

- [ ] `Subscription` and `Subscription.next_msg`

- [ ] `Message` and `Message.data`



Elementary needs:
  - NATS server
  - channels, publish, subscribe, read

  - Q: sync API vs async API?

## Tools

TODO:
  - publish a heartbeat every second
  - publish server time every second
  - publish the ISS location in JSON every second
  - install a factorial server
  - offer a remote calling service (cloudpickle/b64 of a function)
  - install a universal server (see <https://joearms.github.io/published/2013-11-21-My-favorite-erlang-program.html>)
  - mailbox system?
  - heartbeat + supervision with restart?