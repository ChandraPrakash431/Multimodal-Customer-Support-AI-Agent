from fastapi import FastAPI

from app.routes.chat_routes import router

app = FastAPI(title="Customer Support AI Agent", version="1.0.0")

app.include_router(router)

@app.get("/health")

def health():
    return {"status": "healthy"}
