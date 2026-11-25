import asyncio
from functools import partial

from copilot import CopilotClient
from copilot.session_events import AssistantMessageData, SessionIdleData

PROMPT = "What is an AI agent?"


# TODO: Define an event handler function that accepts an event argument,
# checks if it is an instance of AssistantMessageData, and prints event.data.content
def handle_event(done, event):
    if isinstance(event.data, AssistantMessageData):
        print(event.data.content)
    elif isinstance(event.data, SessionIdleData):
        done.set()


async def main() -> None:
    # TODO: Initialize CopilotClient using an 'async with' block
    async with CopilotClient() as client:
        # TODO: Create a session using an 'async with' block
        async with await client.create_session() as session:
            done = asyncio.Event()

            # TODO: Register your event handler using session.on()
            session.on(partial(handle_event, done))

            # TODO: Send the prompt "What is an AI agent?" using await session.send()
            await session.send(PROMPT)
            await done.wait()


if __name__ == "__main__":
    asyncio.run(main())
