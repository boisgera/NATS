
Async Python:
  - Use `async`, `await` and `asyncio.run` is synchronous mode.
  - decompose `await f(...)`: `create_task` + await it;
  - tasks in parallel.
  - asyncio.sleep vs time.sleep

Links:
  - <https://github.com/nats-io/nats.py>
  - <https://nats-io.github.io/nats.py/>

Elementary needs:
  - NATS server
  - channels, publish, subscribe, read

  - Q: sync API vs async API?

TODO:
  - publish a heartbeat every second
  - publish server time every second
  - publish the ISS location in JSON every second
  - install a factorial server
  - offer a remote calling service (cloudpickle/b64 of a function)
  - install a universal server (see <https://joearms.github.io/published/2013-11-21-My-favorite-erlang-program.html>)
  - mailbox system?
  - heartbeat + supervision with restart?