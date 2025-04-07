from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.user_model import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get('/')
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users