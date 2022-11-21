from fastapi_realworld.db.query import create_user

def test_successfull_registration(client):
    user_data = dict(
        username="test_username",
        password="123321admin",
        email="test@email.com"
    )
    user_post = client.post("/api/users", json=user_data)
    assert user_post.status_code == 200
    user_post = user_post.json()
    assert user_post["email"] == "test@email.com"
    assert user_post["username"] == "test_username"
    assert user_post["bio"] is None
    assert user_post["image"] is None
    assert len(user_post["token"].split(".")) == 3 
    
    
def test_with_two_unique_data_registration(client):
    user1_data = dict(
        username="username",
        password="123",
        email="test@gmail.com"
    )
    user2_data = dict(
        username="username",
        password="123",
        email="test@email.ru"
    )
    user1_post = client.post("/api/users", json=user1_data)
    assert user1_post.status_code == 200
    user2_post = client.post("/api/users", json=user2_data)
    assert user2_post.status_code == 400
    assert "detail" in user2_post.json()
    
    
def test_successfull_login(client, user):
    data = dict(
        email="pytest@mail.com",
        password="123321"
    )
    post = client.post("/api/users/login", json=data)
    assert post.status_code == 200
    post = post.json()
    assert post["email"] == "pytest@mail.com"
    assert post["username"] == "pytestusername"
    assert post["bio"] is None
    assert post["image"] is None
    assert len(post["token"].split(".")) == 3 
    
    
def test_invalid_email(client):
    data = dict(
        email="pyt222est@mail.com",
        password="123321"
    )
    post = client.post("/api/users/login", json=data)
    assert post.status_code == 404


def test_invalid_pass(client):
    data = dict(
        email="pytest@mail.com",
        password="123555321"
    )
    post = client.post("/api/users/login", json=data)
    assert post.status_code == 404
    
    
def test_current_user(client, user):
    header = {"Authorization": f"Bearer {user.token}"}
    a = client.get("/api/user", headers=header)
    assert a.status_code == 200