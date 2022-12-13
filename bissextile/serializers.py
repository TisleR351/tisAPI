# Django imports
# DRF imports
from rest_framework.serializers import ModelSerializer, DateTimeField
# Application imports
from bissextile.models import Year, YearRange


class YearSerializer(ModelSerializer):
    date_created = DateTimeField(format="%d%m%Y %H:%M:%S")
    class Meta:
        model = Year
        fields = ['id', 'date_created', 'year', 'bissextile']


class YearDetailSerializer(ModelSerializer):
    date_created = DateTimeField(format="%d%m%Y %H:%M:%S")
    date_updated = DateTimeField(format="%d%m%Y %H:%M:%S")

    class Meta:
        model = Year
        fields = ['id', 'year', 'bissextile', 'date_created', 'date_updated']


class YearRangeSerializer(ModelSerializer):
    date_created = DateTimeField(format="%d%m%Y %H:%M:%S")
    class Meta:
        model = YearRange
        fields = ['id', 'year1', 'year2', 'year_range', 'date_created']


class YearRangeDetailSerializer(ModelSerializer):
    date_created = DateTimeField(format="%d%m%Y %H:%M:%S")
    date_updated = DateTimeField(format="%d%m%Y %H:%M:%S")

    class Meta:
        model = YearRange
        fields = ['id', 'year1', 'year2', 'year_range', 'date_created', 'date_updated']


class HistorySerializer(ModelSerializer):
    date_created = DateTimeField(format="%d%m%Y %H:%M:%S")
    class Meta:
        model = YearRange
        fields = ['date_created', 'id', 'year1', 'year2', 'year_range']
