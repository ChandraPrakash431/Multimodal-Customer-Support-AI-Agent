from fastapi import FastAPI

from app.routes.chat_routes import router
from app.routes.rag_routes import (router as rag_router)
from app.routes.document_routes import (router as document_router)
from app.database.init_db import create_tables

create_tables()

app = FastAPI(title="Customer Support AI Agent", version="1.0.0")

app.include_router(router)
app.include_router(rag_router)
app.include_router(document_router)

@app.get("/health")

def health():
    return {"status": "healthy"}
