"""tisAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django imports
from django.urls import path, include
from django.contrib import admin
# DRF imports
from rest_framework.urlpatterns import format_suffix_patterns
# Application imports
from bissextile.views import YearList, YearDetail, YearRangeList, YearRangeDetail, HistoryList
from calculatrice.views import AdditionList, MultiplicationList, DivisionList, SoustractionList, ModuloList, AllList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/history/', HistoryList.as_view(), name='history'),
    path('api/years/', YearList.as_view(), name='years'),
    path('api/years_range/', YearRangeList.as_view(), name='years_range'),
    path('api/years/<int:pk>/', YearDetail.as_view()),
    path('api/years_range/<int:pk>/', YearRangeDetail.as_view()),
    path('api/addition/', AdditionList.as_view(), name='addition'),
    path('api/soustraction/', SoustractionList.as_view(), name='soustraction'),
    path('api/multiplication/', MultiplicationList.as_view(), name='multiplication'),
    path('api/modulo/', ModuloList.as_view(), name='modulo'),
    path('api/division/', DivisionList.as_view(), name='division'),
    path('api/listoperation/', AllList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
