"""
09 - Basic Production Concerns — Practice Exercises
==================================================
Overview: CORS middleware, rate limiting, logging, health check endpoints, and environment settings.
"""
from fastapi import FastAPI

app = FastAPI(title="09 - Basic Production Concerns")


@app.get("/")
def root():
    return {"message": "Welcome to 09 - Basic Production Concerns practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
