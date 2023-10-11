from django.core.mail import send_mail


def send(user_email):
    send_mail(
        f'NEW ORDER',
        'CHECK YOUR ORDER',
        'tima.j.zh@gmail.com',
        ['awequamy@gmail.com'],
        fail_silently=False,
        )