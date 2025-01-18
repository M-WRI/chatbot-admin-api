from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, Base
from app.modules.auth.routes import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome Stranger!"}

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])