from fastapi.testclient import TestClient
import pytest 
from app import schemas
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base



# USE THIS HARDCODED VALUES OR put _test end of url and take from env
# SQLALCHEMY_DATABASE_URL = 'posgresql://postgres:pass123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    # we drop before so we can keep the table and understand better the problem
    Base.metadata.drop_all(bind=engine)
    #run our code before we run our test
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)
    #run our code after test finishes



def test_root(client):
    response = client.get('/')
    message = response.json().get('Message')
    print(message)
    assert message == "Ciao, sono Alexandre questa è la mia API"
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users/', json={"email":"siren@gmail.com", "password": "123"})
    
    new_user = schemas.UserOut(**response.json()) # **  for unpacking dictionary
    print(response.json())

    assert new_user.email == "siren@gmail.com"
    assert response.status_code == 201