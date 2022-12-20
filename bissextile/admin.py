from django.contrib import admin
from bissextile.models import Year, YearRange
from calculatrice.models import Operation

# Register your models here.

admin.site.register(Year)
admin.site.register(YearRange)