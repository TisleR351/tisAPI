# Django imports
# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Application imports
from calculatrice.models import Operation
from calculatrice.requetes import Requetes
# Create your views here.

class AdditionList(APIView):
    def get(self, request, format=None):
        return Requetes.get(Requetes(), "Addition")

    def post(self, request, format=None):
        return Requetes.post(Requetes(), request, "Addition")


class SoustractionList(APIView):
    def get(self, request, format=None):
        return Requetes.get(Requetes(), "Soustraction")

    def post(self, request, format=None):
        return Requetes.post(Requetes(), request, "Soustraction")


class MultiplicationList(APIView):
    def get(self, request, format=None):
        return Requetes.get(Requetes(), "Multiplication")

    def post(self, request, format=None):
        return Requetes.post(Requetes(), request, "Multiplication")


class DivisionList(APIView):
    def get(self, request, format=None):
        return Requetes.get(Requetes(), "Division")

    def post(self, request, format=None):
        return Requetes.post(Requetes(), request, "Division")


class ModuloList(APIView):
    def get(self, request, format=None):
        return Requetes.get(Requetes(), "Modulo")

    def post(self, request, format=None):
        return Requetes.post(Requetes(), request, "Modulo")


class AllList(APIView):
    def get(self, request, format=None):
        result = {}
        for elmt in Operation.objects.all():
            tableau = [[elmt.input1, elmt.input2], elmt.result, elmt.type]
            result[str(elmt.date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
        return Response(result)