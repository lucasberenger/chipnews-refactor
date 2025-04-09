from sqlalchemy.orm import Session
from models.user_model import User
from utils.hash import verify_password, hash_password
from schemas.user_dto import UserCreate


def get_all_users(db: Session) -> list[User]:
    """ List all users from db"""
    return db.query(User).all()


def get_user(db: Session, email: str) -> User | None:
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user and hash the password"""
    user = User(**user.model_dump())
    user.password = hash_password(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, email: str, password: str) -> User:
    """Authenticate user by email and password"""
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    
    return user