from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_tutorial.settings')

app = Celery('celery')

ettings', namespace='CELERY')

app.autodiscover_tasks()