from rest_framework.viewsets import ModelViewSet

# Create your views here.

from bissextile.models import Year
from bissextile.serializers import YearSerializer

class YearViewset(ModelViewSet):

    serializer_class = YearSerializer

    def get_queryset(self):
        queryset = Year.objects.all()
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset