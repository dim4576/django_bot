from django.db import models
from django.contrib.auth.models import User


class Chats(models.Model):
    chatId = models.IntegerField(
        verbose_name='id of chat in tg',
    )


class Messages(models.Model):
    chat = models.ForeignKey(
        Chats,
        verbose_name='link to chats',
        on_delete=models.CASCADE,
    )
    bot = models.BooleanField(
        verbose_name='flag for messages sent by bot',
        default=False,
    )
    when = models.DateTimeField(
        verbose_name='when sent message',
        auto_now=True,
    )
    text = models.TextField(
        verbose_name='text content of message'
    )
