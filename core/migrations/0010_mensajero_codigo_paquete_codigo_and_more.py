# Generated by Django 4.0.5 on 2022-06-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_serviciomensajero_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajero',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='paquete',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='serviciomensajero',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
