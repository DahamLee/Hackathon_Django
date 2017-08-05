from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='post', max_length=30, blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=100, blank=True)

    class Meta:
        ordering = ['-pk',]

    def add_comment(self, user, content):
        return self.comment_set.create(author=user, content=content)

