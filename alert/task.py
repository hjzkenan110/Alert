from celery import Celery
from django.core.mail import send_mail

from AlertSystem import celery_app

@celery_app.task
def aio_send_mail(title, text, from_address, to_address):
    send_mail(title, text, from_address, to_address, fail_silently=False)
