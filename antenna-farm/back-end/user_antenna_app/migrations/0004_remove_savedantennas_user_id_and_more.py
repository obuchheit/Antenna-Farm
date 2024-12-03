# Generated by Django 5.1.3 on 2024-12-03 04:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_antenna_app', '0003_alter_savedantennas_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedantennas',
            name='user_id',
        ),
        migrations.AddField(
            model_name='savedantennas',
            name='boom_materiel',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='savedantennas',
            name='boom_width',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='savedantennas',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='savedantennas',
            name='title',
            field=models.CharField(default='antenna'),
        ),
        migrations.AddField(
            model_name='savedantennas',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saved_antennas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='savedantennas',
            name='antenna_type',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='savedantennas',
            name='frequency',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='savedantennas',
            name='material',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='savedantennas',
            name='material_width',
            field=models.FloatField(null=True),
        ),
    ]