# Generated by Django 4.2.5 on 2023-09-20 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0003_alter_orcamento_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='validade',
            field=models.DateField(default=datetime.date(2023, 10, 5), verbose_name='Validade'),
        ),
    ]
