# Generated by Django 2.0.2 on 2018-06-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20180501_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='staff_trained_for',
            field=models.BooleanField(default=True),
        ),
    ]