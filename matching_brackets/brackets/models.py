from __future__ import unicode_literals
from django.db import models

#####
# Model: Modelo da classe Query (A consulta eh uma entrada simples de no maximo 1000 caracters)
#####

class Query(models.Model):
    value = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.value