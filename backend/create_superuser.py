import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth.models import User

# Check if admin exists, if not, create it
if not User.objects.filter(username='admin').exists():
    print("Creating superuser 'admin'...")
    # CHANGE 'admin123' TO YOUR DESIRED PASSWORD BELOW
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created!")
else:
    print("Superuser 'admin' already exists.")
    