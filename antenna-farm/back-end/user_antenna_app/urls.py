from django.urls import path
from .views import AllAntennas

urlpatters = [
    path('', AllAntennas.as_view(), name='all_antennas'),
]