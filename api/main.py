from dotenv import load_dotenv
from .models.user import User
from .db import Base, engine
from fastapi import FastAPI
from .endpoints import user, login
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_dotenv(verbose=True)

# Include all the Models here
Base.metadata.create_all(bind=engine)

app.include_router(user.router, tags=["User"], prefix="/user")
app.include_router(login.router, tags=["Auth"])
