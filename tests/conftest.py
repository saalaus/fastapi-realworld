import pytest
from fastapi.testclient import TestClient
from fastapi_realworld.app import app
from fastapi_realworld.db.db import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

from fastapi_realworld.db.query import create_user
from fastapi_realworld.db.user import User
from fastapi_realworld.schemas import UserRegistration

SQLALCHEMY_DATABASE_URL = "sqlite:///tests/pytest.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def get_override_db():
    try:
        db = session()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_override_db


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def user():
    db: Session = session()
    user = create_user(db, UserRegistration(email="pytest@mail.com",
                                            password="123321",
                                            username="pytestusername"))
    db.commit()
    yield user
    db.query(User).filter(User.id == user.id).delete()
    db.commit()
    db.close()


@pytest.fixture(autouse=True, scope="session")
def delete_db():
    yield
    engine.dispose()
    import os
    os.remove("tests/pytest.db")
