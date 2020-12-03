from __future__ import absolute_import
from django.conf import settings
from celery import Celery
import os

# Allow run administrative tasks like manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

# Celery app declaration
func = Celery('main', broker='pyamqp://guest@localhost//')

# Setup
func.config_from_object('django.conf:settings', namespace='CELERY')

# Looks for all the tasks in the project
func.autodiscover_tasks()

'''
func.conf.update(
    BROKER_URL = '//127.0.0.1:8000/',
)
'''
