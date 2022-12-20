# Django imports
from rest_framework.test import APITestCase
# DRF imports
from django.urls import reverse_lazy
# Application imports
from calculatrice.models import Operation


class TestAddition(APITestCase):
    url = reverse_lazy('addition')

    def test_post(self):
        response = self.client.post(self.url, {"input1": 10, "input2": 7}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": response.data['id'], "type": "Addition", "input1": 10,
                    "input2": 7, "result": 17}
        self.assertEqual(response.data, expected)

    def test_list(self):
        addition = Operation.objects.create(input1=10, input2=5, result=15, type="Addition")
        Operation.objects.create(input1=10, input2=15, result=150, type="Multiplication")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {}
        expected[str(addition.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[10, 5],
                                                                            15, "Addition"]
        self.assertEqual(expected, response.json())


class TestSoustraction(APITestCase):
    url = reverse_lazy('soustraction')

    def test_post(self):
        response = self.client.post(self.url, {"input1": 10, "input2": -7}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": response.data['id'], "type": "Soustraction", "input1": 10,
                    "input2": -7, "result": 17}
        self.assertEqual(response.data, expected)

    def test_list(self):
        addition = Operation.objects.create(input1=10, input2=5, result=5, type="Soustraction")
        Operation.objects.create(input1=10, input2=15, result=150, type="Multiplication")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {}
        expected[str(addition.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[10, 5],
                                                                            5, "Soustraction"]
        self.assertEqual(expected, response.json())


class TestMultiplication(APITestCase):
    url = reverse_lazy('multiplication')

    def test_post(self):
        response = self.client.post(self.url, {"input1": 10, "input2": 7}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": response.data['id'], "type": "Multiplication", "input1": 10,
                    "input2": 7, "result": 70}
        self.assertEqual(response.data, expected)

    def test_list(self):
        addition = Operation.objects.create(input1=10, input2=15, result=25, type="Addition")
        Operation.objects.create(input1=10, input2=15, result=150, type="Multiplication")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {}
        expected[str(addition.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[10, 15],
                                                                            150, "Multiplication"]
        self.assertEqual(expected, response.json())


class TestDivision(APITestCase):
    url = reverse_lazy('division')

    def test_post(self):
        response = self.client.post(self.url, {"input1": 70, "input2": 7}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": response.data['id'], "type": "Division", "input1": 70,
                    "input2": 7, "result": 10}
        self.assertEqual(response.data, expected)

    def test_post_by_zero(self):
        response = self.client.post(self.url, {"input1": 70, "input2": 0}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Vous êtes débile, vous ne pouvez pas diviser par 0")

    def test_list(self):
        addition = Operation.objects.create(input1=10, input2=15, result=25, type="Addition")
        Operation.objects.create(input1=10, input2=5, result=2, type="Division")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {}
        expected[str(addition.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[10, 5],
                                                                            2, "Division"]
        self.assertEqual(expected, response.json())


class TestModulo(APITestCase):
    url = reverse_lazy('modulo')

    def test_post(self):
        response = self.client.post(self.url, {"input1": 70, "input2": 8}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": response.data['id'], "type": "Modulo", "input1": 70,
                    "input2": 8, "result": 6}
        self.assertEqual(response.data, expected)

    def test_post_by_zero(self):
        response = self.client.post(self.url, {"input1": 50, "input2": 0}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Vous êtes débile, vous ne pouvez pas diviser par 0")

    def test_list(self):
        addition = Operation.objects.create(input1=10, input2=15, result=25, type="Addition")
        Operation.objects.create(input1=15, input2=10, result=5, type="Modulo")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {}
        expected[str(addition.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[15, 10],
                                                                            5, "Modulo"]
        self.assertEqual(expected, response.json())
