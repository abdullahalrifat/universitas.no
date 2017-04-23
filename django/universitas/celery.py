# -*- coding: utf-8 -*-
"""
Configuration for the task runner celery
"""

from celery import Celery  # type: ignore

# set the default Django settings module for the 'celery' program.

app = Celery('universitas')

# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
