from django.core.mail import send_mail

from shop.celery import app
# from .models import Contact
from .send_email import send

@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    send_mail(
        'NEW ORDER',
        'CHECK YOUR ORDER',
        'tima.j.zh@gmail.com',
        ['awequamy@gmail.com'],
        fail_silently=False,
        )