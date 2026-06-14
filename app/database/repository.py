from sqlalchemy.orm import Session

from app.database.models import Conversation


class ConversationRepository:

    def create(self, db: Session, session_id: str, user_message: str, ai_response: str) -> Conversation:

        conversation = Conversation(session_id=session_id, user_message=user_message, ai_response=ai_response)

        db.add(conversation)

        db.commit()

        db.refresh(conversation)

        return conversation
    
    def get_by_session(self, db: Session, session_id: str):

        return (
            db.query(Conversation)
            .filter(
                Conversation.session_id == session_id
            )
            .order_by(
                Conversation.id
            )
            .all()
        )
