# Generated by Django 4.2.5 on 2023-10-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asesora', '0003_cliente_fktipoempresa_visita_fkcliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]
