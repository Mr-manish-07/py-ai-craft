"""
01 - FastAPI Fundamentals — Practice Exercises
==================================================
Overview: FastAPI app instance, routing, path parameters, query parameters, request handling, and Swagger UI.
"""
from fastapi import FastAPI

app = FastAPI(title="01 - FastAPI Fundamentals")


@app.get("/")
def root():
    return {"message": "Welcome to 01 - FastAPI Fundamentals practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
