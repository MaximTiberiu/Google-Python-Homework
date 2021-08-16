from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.username}"
