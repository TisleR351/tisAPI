# Django imports
from django.db import models
# DRF imports
# Application imports

class Year(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    bissextile = models.BooleanField(default=False)
    year = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.year}'

class YearRange(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    year1 = models.IntegerField(default=0)
    year2 = models.IntegerField(default=0)
    year_range = models.CharField(max_length=99999)

    def __str__(self):
        return f'{self.year1}, {self.year2}'
