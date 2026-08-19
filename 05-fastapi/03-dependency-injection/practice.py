"""
03 - Dependency Injection (Depends) — Practice Exercises
==================================================
Overview: FastAPI dependency system, reusable logic, DB session injection, and API key authentication.
"""
from fastapi import FastAPI

app = FastAPI(title="03 - Dependency Injection (Depends)")


@app.get("/")
def root():
    return {"message": "Welcome to 03 - Dependency Injection (Depends) practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
