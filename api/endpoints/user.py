from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user import UserIn
from ..crud import usercrud
from ..db import get_db
from ..auth import get_user
router = APIRouter()


@router.post("/new")
async def new_user(user: UserIn, db: Session = Depends(get_db)):
    return usercrud.create(user, db)


@router.post("/me")
async def get_all_user(user=Depends(get_user)):
    return user
