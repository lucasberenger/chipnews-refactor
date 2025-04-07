from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True