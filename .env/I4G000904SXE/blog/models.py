from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Created_date = models.DateTimeField(default=datetime.now)
    Published_date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.Title

    def __str__(self) -> str:
        return self.Text


