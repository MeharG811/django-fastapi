import pytest
from httpx import AsyncClient
from djanngo_fastapi_project.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "test@example.com"}

@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "test@example.com"}
