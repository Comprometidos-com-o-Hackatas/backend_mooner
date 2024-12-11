import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

BROKER_URL = 'redis://default:vo0nNYwJoubyuPd8Oy2sQjXrJh0dlHja@redis-16798.c11.us-east-1-3.ec2.redns.redis-cloud.com:16798'

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')