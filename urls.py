from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from services import event_generator


def register_routes(app: FastAPI):
    @app.get("/sse")
    async def sse_endpoint():
        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream"
        )
