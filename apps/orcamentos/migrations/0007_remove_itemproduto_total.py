# Generated by Django 4.2.5 on 2023-09-24 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0006_alter_itemmaodeobra_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemproduto',
            name='total',
        ),
    ]
