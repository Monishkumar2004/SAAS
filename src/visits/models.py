from django.db import models

# Create your models here.

class PageVisits(models.Model):
    path = models.TextField(blank=True, null = True, max_length=255)
    timestamp = models.DateTimeField(auto_now=True)