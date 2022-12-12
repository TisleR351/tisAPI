# Django imports
# DRF imports
from rest_framework.serializers import ModelSerializer
# Application imports
from bissextile.models import Year


class YearListSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'year', 'bissextile']


class YearPostSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ['year', 'bissextile']

