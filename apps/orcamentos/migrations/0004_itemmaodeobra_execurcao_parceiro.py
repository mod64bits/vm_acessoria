# Generated by Django 4.1 on 2023-02-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0003_alter_orcamento_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmaodeobra',
            name='execurcao_parceiro',
            field=models.BooleanField(default=False, verbose_name='Execultado Por Parceiro'),
        ),
    ]
