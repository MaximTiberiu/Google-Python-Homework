from django.contrib.auth.models import User
from django.db import models

from user.models import UserExtend


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    user = models.ForeignKey(UserExtend, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} -> {self.datetime}"
