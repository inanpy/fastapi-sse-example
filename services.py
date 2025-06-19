import asyncio
import json


async def event_generator():
    counter = 0
    while True:
        data = {"message": f"Ping {counter}"}
        yield f"data: {json.dumps(data)}\n\n"
        counter += 1
        await asyncio.sleep(1)
