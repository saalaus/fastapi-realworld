from fastapi import HTTPException
from fastapi_realworld.schemas import UserRegistration
import pytest
import jwt
from fastapi_realworld.utils import generate_jwt, password_hash, verify_password, decode_jwt

def test_password_hash():
    password = "123"
    hashing_password = password_hash(password)
    assert password != hashing_password
    assert verify_password(password, hashing_password) is True
    assert verify_password("321", hashing_password) is False
    
    
def test_jwt():
    user = UserRegistration(
        email="test@mail.ru",
        password="123",
        username="pytest"
        ).dict()
    jwt_token = generate_jwt(user)
    assert len(jwt_token.split(".")) == 3
    decode = decode_jwt(jwt_token)
    assert decode["email"] == "test@mail.ru"
    assert decode["password"] == "123"
    assert decode["username"] == "pytest"
    with pytest.raises(HTTPException) as e:
        decode_jwt("123.123.321")