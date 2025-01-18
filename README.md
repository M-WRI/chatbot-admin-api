# chatbot-admin-api

### Start Virtual Environment:

source venv/bin/activate

### Start App:

uvicorn app.main:app --reload

### Test App:

PYTHONPATH=$(pwd) pytest

### Migrate Database

• alembic revision --autogenerate -m "message"
• alembic upgrade head

### Creating Models and Schemas

You can create relationships with your model classes by the following syntax: Name of class that you want to make a relationship with, back_populates with the entity name
'''
class Chatbot(Base):
**tablename** = "chatbots"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationship
    profile = relationship("ChatbotProfile", uselist=False, back_populates="chatbot", cascade="all, delete-orphan")

‘‘‘

'''
class ChatbotProfile(Base):
**tablename** = "chatbot_profiles"

    id = Column(UUID, primary_key=True, index=True)
    chatbot_id = Column(UUID, ForeignKey("chatbots.id"), nullable=False)
    title = Column(String, nullable=False)
    title_color = Column(String, nullable=True)

    # Relationship
    chatbot = relationship("Chatbot", back_populates="profile")

‘‘‘

The schema looks like the following

'''
class ChatbotSchema(BaseModel):
id: int
name: str
profile: Optional[ChatbotProfileSchema]
sessions: List[SessionSchema]

    class Config:
        orm_mode = True

‘‘‘
