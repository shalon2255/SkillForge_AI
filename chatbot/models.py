from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class ChatSession(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class ChatMessage(models.Model):

    session = models.ForeignKey(
        ChatSession,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    is_user = models.BooleanField()

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )