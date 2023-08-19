from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='nadyammex@gmail.com',
            first_name='Admin',
            last_name='Home',
            is_staff=True,
            is_superuser=True
         )

        user.set_password('U123456789')
        user.save()