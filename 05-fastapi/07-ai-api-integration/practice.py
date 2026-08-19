"""
07 - AI API Integration — Practice Exercises
==================================================
Overview: Connecting OpenAI/Anthropic/custom LLM clients inside FastAPI endpoints.
"""
from fastapi import FastAPI

app = FastAPI(title="07 - AI API Integration")


@app.get("/")
def root():
    return {"message": "Welcome to 07 - AI API Integration practice!"}


# Add your endpoint exercises here


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice:app", host="127.0.0.1", port=8000, reload=True)
