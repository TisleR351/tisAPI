# Django imports
# DRF imports
from rest_framework.serializers import ModelSerializer
# Application imports
from bissextile.models import Year, YearRange


class YearSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'year', 'bissextile']


class YearDetailSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'year', 'bissextile', 'date_created', 'date_updated']


class YearRangeSerializer(ModelSerializer):
    class Meta:
        model = YearRange
        fields = ['id', 'year1', 'year2', 'year_range']

class YearRangeDetailSerializer(ModelSerializer):
    class Meta:
        model = YearRange
        fields = ['id', 'year1', 'year2', 'year_range', 'date_created', 'date_updated']