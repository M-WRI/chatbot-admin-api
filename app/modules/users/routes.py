from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.modules.users.schemas import UserCreate, UserOut
from app.modules.users.services import create_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
async def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)