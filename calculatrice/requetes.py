# Django imports
# DRF imports
from rest_framework.response import Response
from rest_framework import status
# Application imports
from calculatrice.models import Operation
from calculatrice.serializers import OperationSerializer
# Create your views here.


class Requetes(Operation):
    def get(self, type):
        result = {}
        for elmt in Operation.objects.all():
            if elmt.type == type:
                tableau = [[elmt.input1, elmt.input2], elmt.result, elmt.type]
                result[str(elmt.date_created.strftime("%d%m%Y %H:%M:%S"))] = tableau
        return Response(result)

    def post(self, request, type):
        input1 = int(request.data['input1'])
        input2 = int(request.data['input2'])
        if type == "Addition":
            result = input1 + input2
        elif type == "Soustraction":
            result = input1 - input2
        elif type == "Multiplication":
            result = input1 * input2
        elif type == "Division":
            try:
                result = input1 / input2
            except ZeroDivisionError:
                return Response("Vous êtes débile, vous ne pouvez pas diviser par 0", status=status.HTTP_200_OK)
        elif type == "Modulo":
            try:
                result = input1 % input2
            except ZeroDivisionError:
                return Response("Vous êtes débile, vous ne pouvez pas diviser par 0", status=status.HTTP_200_OK)
        else:
            return Response("Impossible d'attribuer un type à cette opération", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        liste_attributs = {"type": type, "input1": input1, "input2": input2, "result": result}
        serializer = OperationSerializer(data=liste_attributs)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for obj in Operation.objects.all():
            if obj.input1 == request.data['input1'] and obj.input2 == request.data['input2'] and obj.type == type:
                print("L'objet est déjà créé et son ID est:" + str(obj.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)