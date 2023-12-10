from allauth.account.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def on_user_logged_in(request, **kwargs):
    messages.success(request, 'Başarıyla giriş yaptınız.')

@receiver(user_logged_out)
def on_user_logged_out(request, **kwargs):
    messages.success(request, 'Başarıyla çıkış yaptınız.')
