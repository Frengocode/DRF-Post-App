from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):

    title = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=datetime.utcnow())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
