# Django imports
from rest_framework.test import APITestCase
# DRF imports
from django.urls import reverse_lazy
# Application imports
from bissextile.models import Year, YearRange


class TestYear(APITestCase):
    url = reverse_lazy('years')

    def test_post(self):
        response = self.client.post(self.url, {"year": 1900, "bissextile": False}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": 1, "year": 1900, "bissextile": False}
        self.assertEqual(response.data, expected)

    def test_list(self):
        Year.objects.create(year=1900, bissextile=False)
        YearRange.objects.create(year1=1900, year2=1920, year_range="1904,1908,1912,1916,1920")
        Year.objects.create(year=1992, bissextile=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [{"id": 1, "year": 1900, "bissextile": False},
                    {"id": 2, "year": 1992, "bissextile": True}]
        self.assertEqual(expected, response.json())


class TestYearRange(APITestCase):
    url = reverse_lazy('years_range')

    def test_post(self):
        response = self.client.post(self.url, {"year1": 1900, "year2": 1920, "year_range": "1904,1908,1912,1916,1920"}, format='json')
        self.assertEqual(response.status_code, 201)
        expected = {"id": 1, "year1": 1900, "year2": 1920, "year_range": "1904,1908,1912,1916,1920"}
        self.assertEqual(response.data, expected)

    def test_list(self):
        expected = {}
        Year.objects.create(year=1900, bissextile=False)
        year1 = YearRange.objects.create(year1=1900, year2=1920, year_range="1904,1908,1912,1916,1920")
        year2 = YearRange.objects.create(year1=1920, year2=1940, year_range="1920,1924,1928,1932,1936,1940")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected[str(year1.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[1900, 1920], [1904, 1908, 1912, 1916, 1920]]
        expected[str(year2.date_created.strftime("%d%m%Y %H:%M:%S"))] = [[1920, 1940], [1920, 1924, 1928, 1932, 1936, 1940]]
        self.assertEqual(expected, response.json())


class HistoryTest(APITestCase):
    url = reverse_lazy('history')
    def test_list(self):
        year1 = Year.objects.create(year=1900, bissextile=False)
        year2 = YearRange.objects.create(year1=1900, year2=1920, year_range="1904,1908,1912,1916,1920")
        year3 = Year.objects.create(year=1992, bissextile=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = {str(year1.date_created.strftime("%d%m%Y %H:%M:%S")): [1900, False],
                    str(year2.date_created.strftime("%d%m%Y %H:%M:%S")): [[1900, 1920], [1904, 1908, 1912, 1916, 1920]],
                    str(year3.date_created.strftime("%d%m%Y %H:%M:%S")): [1992, True]}
        self.assertEqual(expected, response.json())