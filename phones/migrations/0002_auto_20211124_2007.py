# Generated by Django 3.1.2 on 2021-11-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
    ]
