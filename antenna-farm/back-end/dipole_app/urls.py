from django.urls import path
from . import views


urlpatterns = [
    path('dipole/', views.dipole_calculate, name='dipole_calculator')
]