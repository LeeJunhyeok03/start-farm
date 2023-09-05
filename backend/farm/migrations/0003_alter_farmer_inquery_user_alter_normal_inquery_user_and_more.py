# Generated by Django 4.2.4 on 2023-08-30 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_area_alter_user_job'),
        ('town', '0010_town_update_at'),
        ('farm', '0002_farmer_inquery_normal_inquery_delete_farm_inquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_inquery',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AlterField(
            model_name='normal_inquery',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AlterModelTable(
            name='normal_inquery',
            table='Normal_Inquery',
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='program/')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='town.town')),
            ],
            options={
                'db_table': 'Program',
            },
        ),
    ]