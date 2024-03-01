from django.core.management.base import BaseCommand
from django.conf import settings

from .mng import Bots, token


# Название класса обязательно - "Command"
class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        Bots(token.first)
        Bots.lst[0].start()
        # Бесконечный цикл бота