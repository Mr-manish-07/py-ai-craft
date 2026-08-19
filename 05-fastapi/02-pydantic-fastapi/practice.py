"""
02 - Pydantic with FastAPI — Practice Exercises
==================================================
Overview: Request body models, response_model, data validation, status codes, and serialization.
"""
from fastapi import FastAPI

app = FastAPI(title="02 - Pydantic with FastAPI")


@app.get("/")
def root():
    return {"message": "Welcome to 02 - Pydantic with FastAPI practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
