from .models.user import User
from .db import Base, engine
from fastapi import FastAPI
from .endpoints import user, login
app = FastAPI()

# Include all the Models here
Base.metadata.create_all(bind=engine)

app.include_router(user.router, tags=["User"], prefix="/user")
app.include_router(login.router, tags=["Auth"])
