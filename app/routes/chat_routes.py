from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.chat_models import (ChatRequest, ChatResponse)
from app.services.chat_service import ChatService
from app.database.session import (get_db)

router = APIRouter()

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)

def chat(request: ChatRequest, db: Session = Depends(get_db)) -> ChatResponse:

    answer = chat_service.process_message(db=db, session_id=request.session_id, message=request.message)

    return ChatResponse(response=answer)
