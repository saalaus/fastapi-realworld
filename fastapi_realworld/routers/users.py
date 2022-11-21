from fastapi import APIRouter, Depends, HTTPException
from fastapi_realworld.db.db import get_db
from fastapi_realworld.db.query import create_user, get_user_by_username, login_user
from fastapi_realworld.schemas import User, UserLogin, UserRegistration
from fastapi_realworld.utils import decode_jwt, token_oauth
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Users"])


@router.post("/users", response_model=User)
async def registration(user: UserRegistration, db=Depends(get_db)):
    try:
        return create_user(db, user)
    except IntegrityError:
        raise HTTPException(400, "User with this username or email has exist")


@router.post("/users/login", response_model=User)
async def login(user: UserLogin, db=Depends(get_db)):
    user_db = login_user(db, user)
    if not user_db:
        raise HTTPException(404, "User not found")
    return user_db


@router.get("/user", response_model=User)
async def current_user(token=Depends(token_oauth), db=Depends(get_db)):
    payload = decode_jwt(token.credentials)
    user = get_user_by_username(db, payload["username"])
    return user


@router.put("/user")
async def update_user(token=Depends(token_oauth), db=Depends(get_db)):
    ...
