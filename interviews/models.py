from django.db import models
from django.contrib.auth.models import User


class InterviewCategory(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class InterviewSession(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        InterviewCategory,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(default=0)

    performance = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    feedback = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.category.name}"