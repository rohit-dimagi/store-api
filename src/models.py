import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Item(Base):
    __tablename__ = "messages"
    account_id = Column(String)
    message_id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    receiver_number = Column(String(length=20), nullable=False)
    sender_number = Column(String(length=20), nullable=False)

    def __repr__(self):
        return f"<Item account_id={self.account_id} message_id={self.message_id} receiver_number={self.receiver_number} sender_number={self.sender_number}>"
