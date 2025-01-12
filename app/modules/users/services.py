from sqlalchemy.orm import Session
from app.modules.users.models import User
from app.modules.users.schemas import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, password=user.password)  # Hash password in production!
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user