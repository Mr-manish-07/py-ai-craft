from fastapi import FastAPI

app = FastAPI(title="Modular AI API")

@app.get("/")
def root():
    return {"status": "ok"}
