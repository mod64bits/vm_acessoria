# Generated by Django 4.2.1 on 2023-05-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="E-mail"
            ),
        ),
    ]
