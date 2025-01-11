from fastapi import APIRouter
from crud import crud

router = APIRouter()

@router.post("/users/")
async def create_user(username: str, email: str):
    user = crud.create_user(username, email)
    return {"username": user.username, "email": user.email}

@router.get("/users/{username}")
async def get_user(username: str):
    user = crud.get_user_by_username(username)
    if user:
        return {"username": user.username, "email": user.email}
    return {"error": "User not found"}
