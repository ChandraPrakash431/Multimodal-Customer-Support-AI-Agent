from fastapi import APIRouter

from app.documents.rag_service import (RAGService)

from app.models.rag_models import (RAGRequest, RAGResponse)


router = APIRouter(prefix="/rag", tags=["RAG"])

rag_service = RAGService()


@router.post(
    "/query",
    response_model=RAGResponse
)

def query_rag(request: RAGRequest):

    answer = (rag_service.answer_question(request.question))

    return RAGResponse(answer=answer)