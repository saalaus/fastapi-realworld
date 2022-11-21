from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    email: EmailStr

class UserLogin(UserBase):
    password : str

class UserRegistration(UserLogin):
    username: str
    
    
class UserJwt(UserBase):
    username: str
    bio: str = Field(default=None)
    image: str = Field(default=None)

class User(UserBase):
    token: str
    username: str
    bio: str = Field(default=None)
    image: str = Field(default=None)
    
    class Config:
        orm_mode = True
        