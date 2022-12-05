from django.contrib import admin
from bissextile.models import Year

# Register your models here.
class YearAdmin(admin.ModelAdmin):

    list_display = ('id', 'year', 'is_bissextile')

admin.site.register(Year)