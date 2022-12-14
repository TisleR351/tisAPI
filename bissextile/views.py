# Django imports
from django.http import Http404
# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Application imports
from itertools import chain
from bissextile.models import Year, YearRange
from bissextile.serializers import YearSerializer, \
    YearDetailSerializer, \
    YearRangeSerializer, \
    YearRangeDetailSerializer

class YearList(APIView):

    def bissextile(self, annee):
        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
            return True
        else:
            return False

    def get(self, request, format=None):
        years = Year.objects.all()
        serializer = YearSerializer(years, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        annee = int(request.POST.get("year"))
        bissextile = self.bissextile(annee)
        request.data._mutable = True
        request.data.update({"year": annee, "bissextile": bissextile})
        request.data._mutable = False
        serializer = YearSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for year in Year.objects.all():
            if year.year == request.POST.get("year"):
                print("L'objet est déjà créé et son ID est:" + str(year.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class YearDetail(APIView):
    def get_object(self, pk):
        try:
            return Year.objects.get(pk=pk)
        except Year.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        year = self.get_object(pk)
        serializer = YearDetailSerializer(year)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        year = self.get_object(pk)
        serializer = YearDetailSerializer(year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        year = self.get_object(pk)
        year.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class YearRangeList(APIView):
    def get(self, request, format=None):
        result = {}
        for object in YearRange.objects.all():
            tab_int = []
            try:
                for elmts in object.year_range.split(","):
                    tab_int.append(int(elmts))
                tableau = [[object.year1, object.year2], tab_int]
            except:
                tableau = [[object.year1, object.year2], [None]]
            result[str(object.date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
        return Response(result)

    def post(self, request, format=None):
        annee_range = []
        annee1 = int(request.POST.get("year1"))
        annee2 = int(request.POST.get("year2"))
        cpt = 0
        for i in range(annee2 - annee1 + 1):
            if YearList().bissextile(annee1+i):
                cpt += 1
                annee_range.append(str(annee1+i))
                string_annee = ",".join(str(x) for x in annee_range)
            if cpt == 0:
                string_annee = ""
        request.data._mutable = True
        request.data.update({"year1": annee1, "year2": annee2, "year_range": string_annee})
        request.data._mutable = False
        serializer = YearRangeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for year in YearRange.objects.all():
            if year.year1 == request.POST.get("year1") and year.year2 == request.POST.get("year2"):
                print("L'objet est déjà créé et son ID est:" + str(year.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class YearRangeDetail(APIView):
    def get_object(self, pk):
        try:
            return YearRange.objects.get(pk=pk)
        except YearRange.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = {}
        try:
            tab_int = []
            for elmts in self.get_object(pk).year_range.split(","):
                tab_int.append(int(elmts))
            tableau = [[self.get_object(pk).year1, self.get_object(pk).year2], tab_int]
        except:
            tableau = [[self.get_object(pk).year1, self.get_object(pk).year2], [None]]
        result[str(self.get_object(pk).date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
        return Response(result)

    def put(self, request, pk, format=None):
        year = self.get_object(pk)
        serializer = YearRangeDetailSerializer(year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        year = self.get_object(pk)
        year.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HistoryList(APIView):
    def get(self, request, format=None):
        list_history = sorted(chain(Year.objects.all(), YearRange.objects.all()),
                          key=lambda instance: instance.date_created)
        result = {}
        for object in list_history:
            if type(object) == Year:
                tableau = [object.year, object.bissextile]
                result[str(object.date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
            else:
                tab_int = []
                try:
                    for elmts in object.year_range.split(","):
                        tab_int.append(int(elmts))
                    tableau = [[object.year1, object.year2], tab_int]
                except:
                        tableau = [[object.year1, object.year2], [None]]
                result[str(object.date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
        return Response(result)