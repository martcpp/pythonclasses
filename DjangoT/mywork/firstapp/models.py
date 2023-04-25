from django.db import models
from datetime import datetime
# Create your models here.


class testing(models.Model):
    person = models.CharField(max_length=100)
    user = models.CharField(max_length=800)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)