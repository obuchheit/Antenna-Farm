from django.urls import path
from .views import Calculator

urlpatterns = [
    path('calculate/', Calculator.as_view(), name='calculator')
]