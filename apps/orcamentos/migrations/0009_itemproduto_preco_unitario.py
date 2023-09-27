# Generated by Django 4.2.5 on 2023-09-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0008_itemmaodeobra_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemproduto',
            name='preco_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Preco Unitario'),
        ),
    ]