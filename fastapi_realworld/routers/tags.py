from fastapi import APIRouter


router = APIRouter(tags=["Articles"])


@router.get("/tags")
async def get_tags():
    ...