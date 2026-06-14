from sqlalchemy.orm import Session

from app.agent import CustomerSupportAgent

from app.database.repository import (
    ConversationRepository
)


class ChatService:

    def __init__(self):

        self.agent = CustomerSupportAgent()

        self.repository = (ConversationRepository())

    def process_message(self, db: Session, message: str) -> str:

        answer = self.agent.ask(message)

        self.repository.create(db=db, user_message=message, ai_response=answer)

        return answer