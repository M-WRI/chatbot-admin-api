from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.utils import get_db
from app.modules.auth.schemas import UserSignup, Token, UserLogin
from app.modules.auth.services import create_user, authenticate_user
from app.modules.auth.jwt_handler import create_access_token
# Import from the users module
from app.modules.users.models import User

router = APIRouter()

@router.post("/signup", response_model=Token)
def signup(user_data: UserSignup, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.email == user_data.email).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered",
        )
    user = create_user(db, email=user_data.email, password=user_data.password)
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signin", response_model=Token)
def login(login_request: UserLogin, db: Session = Depends(get_db)):

    user = authenticate_user(db, login_request.email, login_request.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token({"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}