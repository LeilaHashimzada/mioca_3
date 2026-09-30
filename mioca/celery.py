import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mioca.settings")
app = Celery("mioca")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# python3 -m celery -A mioca worker -l info
# celery -A mioca worker --beat --scheduler django --loglevel=info