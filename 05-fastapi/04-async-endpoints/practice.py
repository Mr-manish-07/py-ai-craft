"""
04 - Async Endpoints & Concurrency — Practice Exercises
==================================================
Overview: Async vs sync route handlers, event loops, non-blocking I/O, and background tasks.
"""
from fastapi import FastAPI

app = FastAPI(title="04 - Async Endpoints & Concurrency")


@app.get("/")
def root():
    return {"message": "Welcome to 04 - Async Endpoints & Concurrency practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
