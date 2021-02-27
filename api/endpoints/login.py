from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user import UserIn
from ..crud import usercrud
from ..db import get_db
from ..auth import logindep, get_user

router = APIRouter()


@router.post("/login")
async def login(token=Depends(logindep)):
    return token
