# signals.py

from allauth.account.signals import user_logged_in, user_signed_up
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(user_logged_in)
def user_logged_in_receiver(request, user, **kwargs):
    token, _ = Token.objects.get_or_create(user=user)
    print(f'COOKIES: {token}')


@receiver(user_signed_up)
def user_signed_up_receiver(request, user, **kwargs):
    token, _ = Token.objects.get_or_create(user=user)
    print(f'COOKIES: {token}')
