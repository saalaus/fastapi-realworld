from .db import Base
import sqlalchemy as sa


class User(Base):
    username = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    token = sa.Column(sa.String)
    password = sa.Column(sa.String)
    bio = sa.Column(sa.String, nullable=True)
    image = sa.Column(sa.String, nullable=True)
    
    def __str__(self) -> str:
        return f"<User {self.username=} {self.email=} {self.password=} {self.bio=} {self.image=}>"
    
    
