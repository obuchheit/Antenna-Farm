from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import SavedAntennas

class AllAntennasSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SavedAntennas
        exclude = ['user']    