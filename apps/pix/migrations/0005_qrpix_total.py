# Generated by Django 4.2.5 on 2023-09-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pix', '0004_alter_qrpix_orcamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrpix',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total'),
        ),
    ]
