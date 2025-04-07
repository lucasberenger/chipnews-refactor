from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.user_model import User
from services import user_service
from schemas.user_dto import UserResponse
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.get('/', response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail='No users found')

    return users