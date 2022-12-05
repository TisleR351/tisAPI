from django.db import models

# Create your models here.

class Year(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    year = models.IntegerField()
    is_bissextile = models.BooleanField(default=False)

    def __int__(self):
        return self.year