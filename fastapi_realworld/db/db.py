import sqlalchemy
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine("sqlite:///test.sqlite", connect_args={"check_same_thread": False})# for qlite 
session_maker = sessionmaker(engine, autocommit=False, autoflush=False)

class BaseModel:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    
    
Base = declarative_base(cls=BaseModel)

def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()