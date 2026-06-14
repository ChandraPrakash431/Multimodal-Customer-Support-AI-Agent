from sqlalchemy.orm import Session

from app.agent import CustomerSupportAgent

from app.database.repository import (ConversationRepository)


class ChatService:

    def __init__(self):

        self.agent = CustomerSupportAgent()

        self.repository = (ConversationRepository())

    def process_message(self, db: Session, session_id: str, message: str) -> str:

        history = self.repository.get_by_session(db=db, session_id=session_id)

        context = ""

        for item in history:

            context += (
                f"User: {item.user_message}\n"
                f"Assistant: {item.ai_response}\n"
            )

        answer = self.agent.ask_with_context(context=context, message=message)

        self.repository.create(db=db, session_id=session_id, user_message=message, ai_response=answer)

        return answer
