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
    YearRangeSerializer


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
        annee = int(request.data['year'])
        bissextile = self.bissextile(annee)
        liste_attributs = {"year": annee, "bissextile": bissextile}
        serializer = YearSerializer(data=liste_attributs)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for year in Year.objects.all():
            if year.year == int(request.data['year']):
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

    def delete(self, request, pk, format=None):
        year = self.get_object(pk)
        year.delete()
        return Response("L'objet a bien été supprimé", status=status.HTTP_204_NO_CONTENT)


class YearRangeList(APIView):
    def get(self, request, format=None):
        yearsRange = YearRange.objects.all()
        serializer = YearRangeSerializer(yearsRange, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        annee_range = []
        string_annee = ""
        annee1 = int(request.data['year1'])
        annee2 = int(request.data['year2'])
        cpt = 0
        for i in range(annee2 - annee1 + 1):
            if YearList().bissextile(annee1+i):
                cpt += 1
                annee_range.append(str(annee1+i))
                string_annee = ",".join(str(x) for x in annee_range)
            if cpt == 0:
                string_annee = ""
        dict_okay = {"year1": annee1, "year2": annee2, "year_range": string_annee}
        serializer = YearRangeSerializer(data=dict_okay)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for year in YearRange.objects.all():
            if year.year1 == int(request.data['year1']) and year.year2 == int(request.data['year2']):
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
                result[str(object.date_created.strftime("%d/%m/%Y %H:%M:%S"))] = tableau
            else:
                tab_int = []
                try:
                    for elmts in object.year_range.split(","):
                        tab_int.append(int(elmts))
                    tableau = [[object.year1, object.year2], tab_int]
                except:
                        tableau = [[object.year1, object.year2], [None]]
                result[str(object.date_created.strftime("%d/%m/%Y %H:%M:%S"))] = tableau
        return Response(result)