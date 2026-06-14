from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Conversation(Base):

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_message: Mapped[str] = mapped_column(String)

    ai_response: Mapped[str] = mapped_column(String)
