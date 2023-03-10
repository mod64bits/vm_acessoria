# Generated by Django 4.1 on 2023-01-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cnpj', models.CharField(blank=True, max_length=30, null=True, verbose_name='CNPJ')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Logo')),
            ],
        ),
    ]
