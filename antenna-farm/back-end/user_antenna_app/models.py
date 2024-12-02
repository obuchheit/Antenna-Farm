from django.db import models
from user_app.models import AppUser

class SavedAntennas(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    antenna_type = models.CharField()
    frequency = models.FloatField()
    material = models.CharField()
    material_width = models.FloatField()

