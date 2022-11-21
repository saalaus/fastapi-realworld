from fastapi import APIRouter, Depends
from fastapi_realworld.utils import token_oauth


router = APIRouter(tags=["Profiles"])


@router.get("/profiles/<username>")
async def get_user_profile(username: str):
    ...


@router.post("/profiles/<username>/follow")
async def follow_user(username: str, token=Depends(token_oauth)):
    ...


@router.delete("/profiles/<username>/follow")
async def unfollow_user(username: str, token=Depends(token_oauth)):
    ...
