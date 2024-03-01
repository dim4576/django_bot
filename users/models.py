from django.contrib.auth.models import AbstractUser
from django.db import models
from botManager.models import Chats

class CustomUser(AbstractUser):
    tgid = models.ForeignKey(
        Chats,
        editable=True,
        null=True,
        verbose_name='telegram id of user',
        on_delete=models.DO_NOTHING
    )
