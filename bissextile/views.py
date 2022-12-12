# Django imports
# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Application imports
from bissextile.models import Year
from bissextile.serializers import YearListSerializer, YearPostSerializer


class YearList(APIView):
    def get(self, request, format=None):
        years = Year.objects.all()
        serializer = YearListSerializer(years, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        annee = int(request.POST.get("year"))
        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
            bissextile = True
        else:
            bissextile = False
        request.data._mutable = True
        request.data.update({"year": annee, "bissextile": bissextile})
        request.data._mutable = False
        serializer = YearPostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for year in Year.objects.all():
            if year.year == request.POST.get("year"):
                print("L'objet est déjà créé et son ID est:" + str(year.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)