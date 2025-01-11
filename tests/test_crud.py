import pytest
from crud import crud
from models.models import User

@pytest.mark.django_db
def test_create_user():
    user = crud.create_user(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"

@pytest.mark.django_db
def test_get_user_by_username():
    crud.create_user(username="testuser", email="test@example.com")
    user = crud.get_user_by_username("testuser")
    assert user is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"
