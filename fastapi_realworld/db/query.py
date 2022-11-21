import email

from fastapi_realworld.schemas import User, UserJwt, UserLogin, UserRegistration
from fastapi_realworld.utils import generate_jwt, password_hash, verify_password
from sqlalchemy.orm import Session

from .user import User as UserModel


def create_user(db: Session, user: UserRegistration):
    password = password_hash(user.password)
    user_schema = UserJwt(email=user.email, username=user.username)
    jwt = generate_jwt(user_schema.dict())
    model = UserModel(username=user.username,
                      email=user.email,
                      password=password,
                      token=jwt)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def login_user(db: Session, user: UserLogin) -> "UserModel | bool":
    user_db = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not user_db:
        return False
    if not verify_password(user.password, user_db.password):
        return False
    
    return user_db


def get_user_by_username(db: Session, username: str) -> "User | bool":
    user_db = db.query(UserModel).filter(UserModel.username == username).first()
    if not user_db:
        return False
    return user_db