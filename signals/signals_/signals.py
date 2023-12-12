from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_(sender, request, user, **kwargs):
    print('Logged-in Signal...')
    print('Sender :', sender)
    print('Request :', request)
    print('User :', user)
    print(f'Kwargs : {kwargs}')
    
# user_logged_in.connect(login_, sender=User)

@receiver(user_logged_out, sender=User)
def logout_(sender, request, user, **kwargs):
    print('Logged-out Signal...')
    print('Sender :', sender)
    print('Request :', request)
    print('User :', user)
    print(f'Kwargs : {kwargs}')
    
# user_logged_out.connect(logout_, sender=User)

def login_failed(sender, credentials, request, **kwargs):
    print('Login-failed Signal...')
    print('Sender :', sender)
    print('Credentials :', credentials)
    print('Request :', request)
    print(f'Kwargs : {kwargs}')
    
user_login_failed.connect(login_failed)