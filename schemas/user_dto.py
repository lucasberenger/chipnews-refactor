from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str
    password: str