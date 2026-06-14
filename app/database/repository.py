from sqlalchemy.orm import Session

from app.database.models import Conversation


class ConversationRepository:

    def create(self, db: Session, user_message: str, ai_response: str) -> Conversation:

        conversation = Conversation(user_message=user_message, ai_response=ai_response)

        db.add(conversation)

        db.commit()

        db.refresh(conversation)

        return conversation
