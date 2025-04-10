from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from schemas.token_dto import Token
from schemas.user_dto import UserCreate, UserResponse, LoginData
from services.user_service import authenticate_user, get_user, create_user
from utils.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES 
from datetime import timedelta


router = APIRouter(prefix='/auth')

@router.post('/register', response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_user(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    create_user(db, user)
    return user

@router.post('/login', response_model=Token)
async def login_for_access_token(user_data: LoginData, db: Session = Depends(get_db))-> Token | None:
    user = authenticate_user(db, user_data.email, user_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")