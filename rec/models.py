from django.db import models

# Create your models here.


class Cache(models.Model):
    image_id = models.IntegerField()
    prediction = models.CharField(max_length=5)
