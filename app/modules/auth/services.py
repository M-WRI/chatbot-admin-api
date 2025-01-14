from sqlalchemy.orm import Session
from app.modules.auth.utils import hash_password
from app.modules.auth.utils import verify_password
# Import from the users module
from app.modules.users.models import User

def create_user(db: Session, email: str, password: str):
    """Create a new user with a hashed password and role USER."""
    hashed_password = hash_password(password)
    user = User(email=email, password=hashed_password, role="USER")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    """Authenticate a user by email and password."""
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user