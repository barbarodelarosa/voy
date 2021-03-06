# Generated by Django 4.0.5 on 2022-07-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_serviciomensajero_mensajero_aceptado'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciomensajero',
            name='paquete_entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='serviciomensajero',
            name='paquete_entregado_hora',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviciomensajero',
            name='servicio_finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
