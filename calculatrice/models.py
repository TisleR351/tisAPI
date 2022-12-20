# Django imports
from django.db import models
# DRF imports
# Application imports


class Operation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=15)
    input1 = models.FloatField(default=0)
    input2 = models.FloatField(default=0)
    result = models.FloatField()

    def __str__(self):
        return f'{self.type}, {self.input1}, {self.input2}'
