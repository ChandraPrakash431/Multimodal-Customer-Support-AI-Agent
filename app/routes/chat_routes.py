from fastapi import APIRouter

from app.agent import CustomerSupportAgent
from app.models.chat_models import (ChatRequest, ChatResponse)

router = APIRouter()

agent = CustomerSupportAgent()


@router.post("/chat", response_model=ChatResponse)

def chat(request: ChatRequest) -> ChatResponse:

    answer = agent.ask(request.message)

    return ChatResponse(response=answer)
