from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="njutcka@mail.ru",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            telegram_id=1111912904,
        )

        user.set_password("123456")
        user.save()