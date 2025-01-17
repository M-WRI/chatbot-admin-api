from pydantic import BaseModel, EmailStr

class UserSignup(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str

class UserLogin(BaseModel):
    email: str
    password: str