from fastapi import APIRouter, Depends
from fastapi_realworld.utils import token_oauth


router = APIRouter(tags=["Articles"])


@router.get("/articles")
async def list_articles():
    ...
    
    
@router.get("/articles/feed")
async def feed(token=Depends(token_oauth)):
    ...

    
@router.get("/articles/<slug>")
async def get_article(slug: str):
    ...
    

@router.post("/articles")
async def create_post(token=Depends(token_oauth)):
    ...
    
    
@router.put("/articles/<slug>")
async def update_post(slug: str, token=Depends(token_oauth)):
    ...
    
    
@router.delete("/articles/<slug>")
async def delete_post(slug: str, token=Depends(token_oauth)):
    ...
    
    
@router.post("/articles/<slug>/comments")
async def add_comment(slug: str, token=Depends(token_oauth)):
    ...
    

@router.get("/articles/<slug>/comments")
async def get_comment(slug: str):
    ...
    
    
@router.delete("/articles/<slug>/comments/<id>")
async def delete_comment(slug: str, id: int, token=Depends(token_oauth)):
    ...
    

@router.post("/articles/<slug>/favorite")
async def favorite_article(slug: str, token=Depends(token_oauth)):
    ...
    
    
@router.delete("/articles/<slug>/favorite")
async def unfavorite_article(slug: str, token=Depends(token_oauth)):
    ...