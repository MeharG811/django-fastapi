

#### Project Structure ###

```bash
    djanngo_fastapi_project/
    │
    ├── djanngo_fastapi_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── models/
    │   ├── __init__.py
    │   ├── models.py
    │   └── migrations/
    │   └── commands/  #to create seeders
    │
    ├── crud/
    │   ├── crud.py
    │
    ├── app_endpoints/
    │   ├── endpoints.py
    │
    ├── tests/
    │   ├── test_endpoints.py  # FastAPI endpoint tests
    │   ├── test_crud.py       # Django ORM tests
    │
    │
    ├── main.py
    └── manage.py
```

#### env ###

```bash
    pip install pytest pytest-django httpx
    pip install fastapi django uvicorn psycopg2
```

#### Run tests ###

```bash
    pytest
```

#### Other Commands

```bash
    python manage.py makemigrations
    python manage.py migrate
    uvicorn main:app --reload --host 0.0.0.0 --port 9000
```

### Refrences

```https

https://sunscrapers.com/blog/fastapi-and-django-a-guide-to-elegant-integration/

```

```https

https://www.stavros.io/posts/fastapi-with-django/

```
