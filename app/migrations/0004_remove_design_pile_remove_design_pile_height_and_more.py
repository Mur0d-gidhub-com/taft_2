# Generated by Django 4.1.6 on 2023-04-18 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_ourcustomers_time_alter_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='pile',
        ),
        migrations.RemoveField(
            model_name='design',
            name='pile_height',
        ),
        migrations.RemoveField(
            model_name='design',
            name='points',
        ),
        migrations.RemoveField(
            model_name='design',
            name='primary_basic',
        ),
        migrations.RemoveField(
            model_name='design',
            name='secondary_basic',
        ),
        migrations.RemoveField(
            model_name='design',
            name='total_weight',
        ),
        migrations.RemoveField(
            model_name='design',
            name='yarn_weight',
        ),
        migrations.AlterField(
            model_name='ourcustomers',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 8, 33, 31, 232561)),
        ),
    ]