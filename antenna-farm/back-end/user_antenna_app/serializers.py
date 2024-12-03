from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import SavedAntennas

class AllAntennasSerializer(ModelSerializer):
    class Meta:
        model = SavedAntennas
        exclude = ['user']    