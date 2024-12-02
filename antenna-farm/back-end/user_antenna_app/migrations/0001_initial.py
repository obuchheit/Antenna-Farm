# Generated by Django 5.1.3 on 2024-12-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedAntennas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antenna_type', models.CharField()),
                ('frequency', models.FloatField()),
                ('material', models.CharField()),
                ('material_width', models.FloatField()),
            ],
        ),
    ]
