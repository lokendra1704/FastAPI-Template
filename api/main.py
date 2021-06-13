from dotenv import load_dotenv
from .models.user import User
from .db import Base, engine
from fastapi import FastAPI
from .endpoints import user, login, images
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all the Models here
Base.metadata.create_all(bind=engine)

app.include_router(user.router, tags=["User"], prefix="/user")
app.include_router(login.router, tags=["Auth"])
app.include_router(images.router, tags=["img"])
