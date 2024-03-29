# Generated by Django 4.2.5 on 2023-09-22 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0004_orcamento_total_alter_orcamento_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='total_equipamentos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Equipamentos'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='total_lucro',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Lucro'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='total_mao_de_obra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Mão de Obra'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='validade',
            field=models.DateField(default=datetime.date(2023, 10, 9), verbose_name='Validade'),
        ),
    ]
