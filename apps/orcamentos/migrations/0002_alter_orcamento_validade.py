# Generated by Django 4.2.4 on 2023-08-12 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orcamentos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orcamento",
            name="validade",
            field=models.DateField(
                default=datetime.date(2023, 8, 28), verbose_name="Validade"
            ),
        ),
    ]
