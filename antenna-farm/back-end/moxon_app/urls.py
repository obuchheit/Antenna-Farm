from django.urls import path
from . import views

urlpatterns = [
    path('moxon/', views.moxon_calculate, name='moxon_calculator')
]