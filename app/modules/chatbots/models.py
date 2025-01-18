from sqlalchemy import Column, UUID, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from app.db.session import Base

class Chatbot(Base):
    __tablename__ = "chatbots"
    
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Foreign Key
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)

    # Relationships
    profile = relationship("ChatbotProfile", uselist=False, back_populates="chatbot", cascade="all, delete-orphan")
    sessions = relationship("Session", back_populates="chatbot", cascade="all, delete-orphan")
    user = relationship("User", back_populates="chatbots")


class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(UUID, primary_key=True, index=True)
    chatbot_id = Column(UUID, ForeignKey("chatbots.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    chat_user_id = Column(UUID, nullable=False) 
    end_time = Column(DateTime, nullable=True)

    # Relationships
    interaction = relationship("Interaction", uselist=False, back_populates="session", cascade="all, delete-orphan")
    chatbot = relationship("Chatbot", back_populates="sessions")
    user = relationship("User", back_populates="sessions")

class Interaction(Base):
    __tablename__ = "interactions"
    
    id = Column(UUID, primary_key=True, index=True)
    session_id = Column(UUID, ForeignKey("sessions.id"), nullable=False)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    session = relationship("Session", back_populates="interactions")