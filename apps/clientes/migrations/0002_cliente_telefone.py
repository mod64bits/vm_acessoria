# Generated by Django 4.1 on 2023-01-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Telefone'),
        ),
    ]
