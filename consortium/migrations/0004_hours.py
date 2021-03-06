# Generated by Django 2.0.2 on 2018-05-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0003_auto_20180425_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=15, unique=True, verbose_name='Day of the week')),
                ('start', models.TimeField(verbose_name='start time of day')),
                ('end', models.TimeField(verbose_name='end time of day')),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Company Hours For Day Of The Week',
                'verbose_name_plural': 'Company Hours For Days Of The Week',
                'ordering': ['day'],
            },
        ),
    ]
