# Generated by Django 2.0.2 on 2018-05-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='main_phone',
            field=models.CharField(blank=True, default='2223334444', max_length=15, verbose_name='main phone'),
        ),
    ]
