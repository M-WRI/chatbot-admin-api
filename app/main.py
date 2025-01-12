from fastapi import FastAPI
from app.db.session import engine, Base
from app.modules.users.routes import router as users_router

app = FastAPI()

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users_router, prefix="/api/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome Stranger!"}