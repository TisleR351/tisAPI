from rest_framework import serializers
from bissextile.models import Year


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = ['id', 'date_created', 'date_updated', 'year', 'is_bissextile']