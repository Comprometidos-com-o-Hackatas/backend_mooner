import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

BROKER_URL = 'amqps://vvonqxhz:VZJ604srrslOgFTor2L2ge36GrDUhUzp@toad.rmq.cloudamqp.com/vvonqxhz'

app = Celery('config', broker=BROKER_URL)

app.conf.update(
    broker_connection_retry_on_startup=True,
)

app.conf.task_always_eager = False

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')