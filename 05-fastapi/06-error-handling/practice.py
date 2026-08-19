"""
06 - Error Handling in FastAPI — Practice Exercises
==================================================
Overview: HTTPException, custom exception handlers, validation error interception, and error schemas.
"""
from fastapi import FastAPI

app = FastAPI(title="06 - Error Handling in FastAPI")


@app.get("/")
def root():
    return {"message": "Welcome to 06 - Error Handling in FastAPI practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
