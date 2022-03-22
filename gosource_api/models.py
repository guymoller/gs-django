from django.db import models

# Create your models here.

from django.db import models
from django.db.models import JSONField

class Message(models.Model):
    payload = JSONField()
    cc_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name