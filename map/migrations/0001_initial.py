# Generated by Django 3.1.7 on 2022-01-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('type', models.TextField()),
                ('latitide', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
