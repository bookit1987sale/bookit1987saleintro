# Generated by Django 2.0.2 on 2018-06-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_sced', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabilityforday',
            name='not_avail',
            field=models.BooleanField(default=False, verbose_name='Not available on this day'),
        ),
    ]
