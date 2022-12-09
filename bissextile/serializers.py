from rest_framework.serializers import ModelSerializer
from bissextile.models import Year


class YearSerializer(ModelSerializer):

    class Meta:
        model = Year
        fields = ['year', 'is_bissextile']

