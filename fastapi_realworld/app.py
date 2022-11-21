from fastapi import Depends, FastAPI
from fastapi_realworld.db.db import Base, engine
from jwt import encode as encode_jwt

from .routers import articles, profiles, tags, users

app = FastAPI()
app.include_router(users.router, prefix="/api")
app.include_router(tags.router, prefix="/api")
app.include_router(profiles.router, prefix="/api")
app.include_router(articles.router, prefix="/api")

Base.metadata.create_all(engine)