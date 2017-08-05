from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=15)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']


class Relation(models.Model):
    user1 = models.ForeignKey(User, related_name='request_user')
    user2 = models.ForeignKey(User, related_name='response_user')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            (
                'user1', 'user2'
            ),
        )