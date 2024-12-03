from django.urls import path
from .views import AllAntennas, AntennaManager

urlpatters = [
    path('', AllAntennas.as_view(), name='all_antennas'),
    path('<int:id>/', AntennaManager.as_view(), name='antenna_details')
]