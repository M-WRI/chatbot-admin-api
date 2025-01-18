from sqlalchemy import Column, UUID, String
from app.db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="USER", nullable=False)

    # Relationship
    chatbots = relationship("Chatbot", back_populates="user_id", cascade="all, delete-orphan")