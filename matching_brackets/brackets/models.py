from __future__ import unicode_literals
from django.db import models

class Query(models.Model):
    value = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.value