from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = "Prashant"

        if User.objects.filter(username=username).exists():
            self.stdout.write("Admin already exists — skipping")
            return

        User.objects.create_superuser(
            username=username,
            email="cyberguy230@gmail.com",
            password="prashant@2064"
        )

        self.stdout.write("Admin created successfully")