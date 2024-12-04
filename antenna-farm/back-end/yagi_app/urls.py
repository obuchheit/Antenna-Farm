from django.urls import path
from . import views

urlpatterns = [
    path('yagi/', views.dl6wu_yagi, name='yagi_caclulator')
]