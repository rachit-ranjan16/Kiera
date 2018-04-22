from django.db import models

# Create your models here.


class Status(models.Model):
    status = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)