from django.db import models
from user_app.models import AppUser

class SavedAntennas(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='saved_antennas', default=1)
    title = models.CharField(default='antenna')
    description = models.TextField(null=True)
    antenna_type = models.CharField(null=True)
    frequency = models.FloatField(null=True)
    material = models.CharField(null=True)
    material_width = models.FloatField(null=True)
    boom_materiel = models.CharField(null=True)
    boom_width = models.FloatField(null=True)

