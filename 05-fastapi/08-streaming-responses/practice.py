"""
08 - Streaming Responses (SSE) — Practice Exercises
==================================================
Overview: StreamingResponse, async generators, Server-Sent Events (SSE), and token streaming for AI.
"""
from fastapi import FastAPI

app = FastAPI(title="08 - Streaming Responses (SSE)")


@app.get("/")
def root():
    return {"message": "Welcome to 08 - Streaming Responses (SSE) practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
