from fastapi import FastAPI

from app.routes.chat_routes import router
from app.database.init_db import create_tables

create_tables()

app = FastAPI(title="Customer Support AI Agent", version="1.0.0")

app.include_router(router)

@app.get("/health")

def health():
    return {"status": "healthy"}
