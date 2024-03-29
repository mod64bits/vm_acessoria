# Generated by Django 4.2.5 on 2023-09-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone'),
        ),
    ]
