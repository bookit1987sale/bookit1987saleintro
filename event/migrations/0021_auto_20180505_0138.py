# Generated by Django 2.0.2 on 2018-05-05 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_auto_20180504_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilityforday',
            name='scheduled_end',
            field=models.CharField(choices=[('12:15 AM', '12:15 AM'), ('12:30 AM', '12:30 AM'), ('12:45 AM', '12:45 AM'), ('1:00 AM', '1:00 AM'), ('1:15 AM', '1:15 AM'), ('1:30 AM', '1:30 AM'), ('1:45 AM', '1:45 AM'), ('2:00 AM', '2:00 AM'), ('2:15 AM', '2:15 AM'), ('2:30 AM', '2:30 AM'), ('2:45 AM', '2:45 AM'), ('3:00 AM', '3:00 AM'), ('3:15 AM', '3:15 AM'), ('3:30 AM', '3:30 AM'), ('3:45 AM', '3:45 AM'), ('4:00 AM', '4:00 AM'), ('4:15 AM', '4:15 AM'), ('4:30 AM', '4:30 AM'), ('4:45 AM', '4:45 AM'), ('5:00 AM', '5:00 AM'), ('5:15 AM', '5:15 AM'), ('5:30 AM', '5:30 AM'), ('5:45 AM', '5:45 AM'), ('6:00 AM', '6:00 AM'), ('6:15 AM', '6:15 AM'), ('6:30 AM', '6:30 AM'), ('6:45 AM', '6:45 AM'), ('7:00 AM', '7:00 AM'), ('7:15 AM', '7:15 AM'), ('7:30 AM', '7:30 AM'), ('7:45 AM', '7:45 AM'), ('8:00 AM', '8:00 AM'), ('8:15 AM', '8:15 AM'), ('8:30 AM', '8:30 AM'), ('8:45 AM', '8:45 AM'), ('9:00 AM', '9:00 AM'), ('9:15 AM', '9:15 AM'), ('9:30 AM', '9:30 AM'), ('9:45 AM', '9:45 AM'), ('10:00 AM', '10:00 AM'), ('10:15 AM', '10:15 AM'), ('10:30 AM', '10:30 AM'), ('10:45 AM', '10:45 AM'), ('11:00 AM', '11:00 AM'), ('11:15 AM', '11:15 AM'), ('11:30 AM', '11:30 AM'), ('11:45 AM', '11:45 AM'), ('12:00 PM', '12:00 PM'), ('12:15 PM', '12:15 PM'), ('12:30 PM', '12:30 PM'), ('12:45 PM', '12:45 PM')], max_length=15, verbose_name='end time of day'),
        ),
        migrations.AlterField(
            model_name='availabilityforday',
            name='scheduled_start',
            field=models.CharField(choices=[('12:00 AM', '12:00 AM'), ('12:15 AM', '12:15 AM'), ('12:30 AM', '12:30 AM'), ('12:45 AM', '12:45 AM'), ('1:00 AM', '1:00 AM'), ('1:15 AM', '1:15 AM'), ('1:30 AM', '1:30 AM'), ('1:45 AM', '1:45 AM'), ('2:00 AM', '2:00 AM'), ('2:15 AM', '2:15 AM'), ('2:30 AM', '2:30 AM'), ('2:45 AM', '2:45 AM'), ('3:00 AM', '3:00 AM'), ('3:15 AM', '3:15 AM'), ('3:30 AM', '3:30 AM'), ('3:45 AM', '3:45 AM'), ('4:00 AM', '4:00 AM'), ('4:15 AM', '4:15 AM'), ('4:30 AM', '4:30 AM'), ('4:45 AM', '4:45 AM'), ('5:00 AM', '5:00 AM'), ('5:15 AM', '5:15 AM'), ('5:30 AM', '5:30 AM'), ('5:45 AM', '5:45 AM'), ('6:00 AM', '6:00 AM'), ('6:15 AM', '6:15 AM'), ('6:30 AM', '6:30 AM'), ('6:45 AM', '6:45 AM'), ('7:00 AM', '7:00 AM'), ('7:15 AM', '7:15 AM'), ('7:30 AM', '7:30 AM'), ('7:45 AM', '7:45 AM'), ('8:00 AM', '8:00 AM'), ('8:15 AM', '8:15 AM'), ('8:30 AM', '8:30 AM'), ('8:45 AM', '8:45 AM'), ('9:00 AM', '9:00 AM'), ('9:15 AM', '9:15 AM'), ('9:30 AM', '9:30 AM'), ('9:45 AM', '9:45 AM'), ('10:00 AM', '10:00 AM'), ('10:15 AM', '10:15 AM'), ('10:30 AM', '10:30 AM'), ('10:45 AM', '10:45 AM'), ('11:00 AM', '11:00 AM'), ('11:15 AM', '11:15 AM'), ('11:30 AM', '11:30 AM'), ('11:45 AM', '11:45 AM'), ('12:00 PM', '12:00 PM'), ('12:15 PM', '12:15 PM'), ('12:30 PM', '12:30 PM')], max_length=15, verbose_name='start time of day'),
        ),
    ]
