# Generated by Django 3.1.2 on 2021-11-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('lte_exists', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
            ],
        ),
    ]
