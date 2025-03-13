import os
from celery import Celery
os.environ.setdefault("DJANGO_SITTINGS_MODULE",'config.sittings')

app=Celery('avia_kassa')

app.config_from_object('django.conf:sittings',namespace='Celery')
app.autodiscover_tasks()
