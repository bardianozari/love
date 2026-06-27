# my_romantic_project/my_romantic_project/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_romantic_project.settings')

application = get_wsgi_application()