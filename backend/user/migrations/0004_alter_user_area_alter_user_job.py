# Generated by Django 4.2.4 on 2023-08-29 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_area_alter_user_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.area'),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.job'),
        ),
    ]
