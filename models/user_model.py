from sqlalchemy import Column, Boolean, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    password = Column(String, unique=True)
    is_active = Column(Boolean, default=True)