# Generated by Django 2.0.2 on 2018-04-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20180426_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientevent',
            name='gap_mins_used',
            field=models.PositiveIntegerField(default=0),
        ),
    ]