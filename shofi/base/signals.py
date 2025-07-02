from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import os

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    # Only run for the auth app or your specific app
    if sender.name == 'django.contrib.auth' or sender.name == 'your_app':
        if os.environ.get('CREATE_SUPERUSER', '').lower() == 'true':
            User = get_user_model()
            username = os.environ.get('SUPERUSER_NAME')
            email = os.environ.get('SUPERUSER_EMAIL')
            password = os.environ.get('SUPERUSER_PASSWORD')
            
            if username and email and password:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(username, email, password)
                    print(f"Superuser {username} created successfully")
