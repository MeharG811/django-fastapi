import os
from fastapi import FastAPI
from django.core.wsgi import get_wsgi_application

# Set up Django settings and initialize Django ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djanngo_fastapi_project.settings")
application = get_wsgi_application()

# Create FastAPI app
app = FastAPI()

# Import endpoints and include them
from endpoints import endpoints
app.include_router(endpoints.router,prefix='/user',tags=['user'])
