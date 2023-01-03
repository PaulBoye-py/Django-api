from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200, null=True, default='')
    biography = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
