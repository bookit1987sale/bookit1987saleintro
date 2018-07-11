# Generated by Django 2.0.2 on 2018-06-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_sced', '0002_availabilityforday_not_avail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilityforday',
            name='scheduled_end',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='end time of day'),
        ),
        migrations.AlterField(
            model_name='availabilityforday',
            name='scheduled_start',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='start time of day'),
        ),
    ]
