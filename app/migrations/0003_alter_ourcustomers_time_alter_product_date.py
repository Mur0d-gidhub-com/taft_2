# Generated by Django 4.1.6 on 2023-04-18 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_design_pile_design_pile_height_design_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourcustomers',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 8, 16, 3, 393869)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 18)),
        ),
    ]
