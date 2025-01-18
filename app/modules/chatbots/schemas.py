from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from uuid import UUID

class InteractionSchema(BaseModel):
    id: UUID
    request: str
    response: str
    timestamp: datetime
    session_id: UUID

    class Config:
        orm_mode = True

class SessionSchema(BaseModel):
    id: UUID
    start_time: datetime
    end_time: Optional[datetime]
    chat_user_id: UUID
    chatbot_id: UUID
    interaction: Optional[InteractionSchema]

    class Config:
        orm_mode = True

class ChatbotProfileSchema(BaseModel):
    id: UUID 
    chatbot_id: UUID
    title: str
    title_color: Optional[str]

    class Config:
        orm_mode = True

class ChatbotSchema(BaseModel):
    id: int
    name: str
    profile: Optional[ChatbotProfileSchema]
    sessions: List[SessionSchema]

    class Config:
        orm_mode = True

