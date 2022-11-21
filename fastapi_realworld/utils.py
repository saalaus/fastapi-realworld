from fastapi import HTTPException
from passlib.context import CryptContext
import jwt
from fastapi.security import HTTPBearer
from fastapi_realworld.schemas import UserRegistration

token_oauth = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"])
SECRET_KEY = "super secret_key"
JWT_ALGORITHM = "HS256"


def password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def generate_jwt(payload: dict):
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode_jwt(jwt_token: str) -> dict:
    try:
        return jwt.decode(jwt_token, key=SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(404, "User not found")