# Generated by Django 2.0.2 on 2018-04-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_clientevent_gap_mins_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientevent',
            name='gap_mins_used',
        ),
        migrations.AddField(
            model_name='clientevent',
            name='second_part',
            field=models.BooleanField(default=False),
        ),
    ]