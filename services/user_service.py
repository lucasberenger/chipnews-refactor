from sqlalchemy.orm import Session
from models.user_model import User


def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()