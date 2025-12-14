# NATS

The "Neural Autonomic Transport System", a cross-platform messaging technology.

[![NATS logo](images/nats-horizontal-color.png)](https://nats.io/)


## Prerequisites

Learn the basics of Python async:

- [ ] [asyncio IDS tutorial][github-asyncio]

For further information, refer to the [asyncio documentation][asyncio].

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

- [ ] `Subscription`, `Subscription.next_msg` and `Subscription.messages`,

- [ ] `Message` and `Message.data`

## Practice

 - [ ] **Identity.** Select an name to identify yourself (e.g. `boisgera` for myself).

 - [ ] **Heartbeat.** Send every second a message with subject `"❤️"` 
      and with data your (utf-8 encoded) name.

 - [ ] **Alive** Create a python file with an async function `alive` 
   that list (once, alphabetically) each name that has at least one heartbeat 
   over a 3.0 second. Print each name on a line when the python file is
   invoked as a script. 
   
 - [ ] **Watcher**. Use [rich](https://rich.readthedocs.io/en/latest/) 
  to make a script that continuously display the list of heartbeat names.

 - [ ] **Inbox.** Subscribe to the channel which is your name
   and print every message that you receive in this channel.
   Combine this program with the publication of your heartbeat.

 - [ ] **Greetings.** Send a (utf-8 encoded) greeting message to a person who has a heartbeat.

 - [ ] **Reply.** Send another message to someone with a specific
   question. Specific the `reply` argument to `publish` in order
   to get an answer!

 - [ ] **Reply.** If you want to be able to distinguish with certainty what 
   message is specifically target

 - [ ]