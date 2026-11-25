# GithubCopilotTests
Testing what copilot can do

## How `async` and `await` work in `first_agent.py`

- `async def` defines a coroutine: a function that can pause.
- `await` pauses the coroutine until an operation finishes.
- The event loop, started by `asyncio.run()`, runs other work during the pause and then resumes the coroutine.

### Step by step

Read from top to bottom:

```text
┌────────────────────────────────────────────────────┐
│ 1. Start                                           │
│    asyncio.run(main())                             │
│                                                    │
│    asyncio = Python's built-in library for async   │
│    code. run() starts the event loop (the          │
│    scheduler) and runs main(). main() is written   │
│    'async def', so it is allowed to pause.         │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 2. Open the client                                 │
│    async with CopilotClient()                      │
│                                                    │
│    async = this can pause. 'async with' opens      │
│    something now and closes it later, pausing if   │
│    needed.                                         │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 3. Create the session                              │
│    await client.create_session()                   │
│                                                    │
│    await = pause here until the session is ready.  │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 4. Create a flag (not set yet)                     │
│    done = asyncio.Event()                          │
│                                                    │
│    asyncio.Event() = an on/off flag that async     │
│    code can wait for.                              │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 5. Choose who handles Copilot's events             │
│    session.on(handle_event)                        │
│                                                    │
│    No await: registering is immediate.             │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 6. Send the question                               │
│    await session.send(PROMPT)                      │
│                                                    │
│    await = pause until the question is sent.       │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 7. main() PAUSES                                   │
│    await done.wait()                               │
│                                                    │
│    await = pause until the flag is set. The event  │
│    loop stays free to receive the reply.           │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 8. The reply arrives                               │
│    handle_event(event)                             │
│                                                    │
│    A normal 'def' function (no async): it never    │
│    needs to pause.                                 │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 9. Copilot is finished (session idle)              │
│    done.set()                                      │
│                                                    │
│    Turns the flag on, which wakes up main().       │
└──────────────────────────┬─────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────┐
│ 10. main() CONTINUES                               │
│    end of 'async with'                             │
│                                                    │
│    Closes the session and client. The program      │
│    ends.                                           │
└────────────────────────────────────────────────────┘
```
