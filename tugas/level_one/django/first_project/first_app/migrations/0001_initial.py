# Generated by Django 5.0.4 on 2024-11-08 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=264)),
                ('license_plate', models.CharField(max_length=15, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OwnershipRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.vehicletype'),
        ),
    ]
