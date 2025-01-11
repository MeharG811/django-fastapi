from models.models import User

def create_user(username: str, email: str):
    user = User(username=username, email=email)
    user.save()
    return user

def get_user_by_username(username: str):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None
