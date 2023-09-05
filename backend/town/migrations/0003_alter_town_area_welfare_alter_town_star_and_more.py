# Generated by Django 4.2.4 on 2023-08-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0002_town_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='town',
            name='area_welfare',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='town',
            name='star',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='town',
            name='town_citizen',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='town',
            name='town_culture',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='town',
            name='town_facility',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='town',
            name='town_welfare',
            field=models.FloatField(default=0),
        ),
    ]