from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo_Objects(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200)
    # title = models.CharField(max_length=100)
    # priority = models.IntegerField(default=5)
