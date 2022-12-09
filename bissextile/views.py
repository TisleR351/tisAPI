from rest_framework.viewsets import ModelViewSet

# Create your views here.

from bissextile.models import Year
from bissextile.serializers import YearSerializer

class YearViewset(ModelViewSet):

    serializer_class = YearSerializer

    def get_queryset(self):
        return Year.objects.all()