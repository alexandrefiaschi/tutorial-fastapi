from app import schemas
from jose import jwt
from app.config import settings
import pytest

def test_root(client):
    response = client.get('/')
    message = response.json().get('Message')
    #print(message)
    assert message == "Ciao, sono Alexandre questa è la mia API"
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users/', json={"email":"siren@gmail.com", "password": "123"})
    
    new_user = schemas.UserOut(**response.json()) # **  for unpacking dictionary
    #print(response.json())

    assert new_user.email == "siren@gmail.com"
    assert response.status_code == 201

def test_login_user(client, test_user):
    response = client.post('/login', data={"username": test_user['email'] , "password": test_user['password']})
    #print(response.json())
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
        # extract the id
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert response.status_code == 200

@pytest.mark.parametrize("email, password, error_code",
    [("wrong@gmail.com", "123", 403),
    ("alex@gmail.com", "wrongpass", 403),
    ("wrong@gmail.com", "wrongpass", 403),
    (None, "123", 422), 
    ("alex@gmail.com", None, 422)])
def test_login_failed_user(client, test_user, email, password, error_code):
    response = client.post('/login', data={"username": email , "password": password})
    assert response.status_code == error_code
    #assert response.json().get('detail') == 'Invalid credentials'
    
    #print(response.json())
    
