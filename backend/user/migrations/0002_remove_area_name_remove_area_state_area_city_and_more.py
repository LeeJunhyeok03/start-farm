# Generated by Django 4.2.4 on 2023-08-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='name',
        ),
        migrations.RemoveField(
            model_name='area',
            name='state',
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='province',
            field=models.CharField(max_length=200, null=True),
        ),
    ]