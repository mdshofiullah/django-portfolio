from django.core.management import call_command
from django.contrib.auth import get_user_model
import os

def create_superuser():
    User = get_user_model()
    if os.environ.get('CREATE_SUPERUSER', '').lower() == 'true':
        try:
            if not User.objects.filter(username=os.environ['SUPERUSER_NAME']).exists():
                User.objects.create_superuser(
                    os.environ['SUPERUSER_NAME'],
                    os.environ['SUPERUSER_EMAIL'],
                    os.environ['SUPERUSER_PASSWORD']
                )
                print(f"Superuser {os.environ['SUPERUSER_NAME']} created")
        except Exception as e:
            print(f"Superuser creation error: {str(e)}")

if __name__ == '__main__':
    import django
    django.setup()
    create_superuser()
