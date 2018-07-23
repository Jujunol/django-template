from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
