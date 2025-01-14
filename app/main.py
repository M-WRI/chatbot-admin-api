from fastapi import FastAPI
from app.db.session import engine, Base
from app.modules.auth.routes import router as auth_router

app = FastAPI()

# Initialize database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome Stranger!"}

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])