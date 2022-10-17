from pyexpat import model
from django.db import models

# Create your models here.


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    tweet = models.TextField()

    class Meta:
        ordering = ['created_at', 'name']
