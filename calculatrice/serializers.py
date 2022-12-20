# Django imports
# DRF imports
from rest_framework.serializers import ModelSerializer
# Application imports
from calculatrice.models import Operation


class OperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = ['id', 'type', 'input1', 'input2', 'result']
