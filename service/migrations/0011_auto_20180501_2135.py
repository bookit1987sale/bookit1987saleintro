# Generated by Django 2.0.2 on 2018-05-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20180429_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='retail_service',
            field=models.CharField(max_length=130, unique=True, verbose_name='service description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_branch', to='service.Branch', verbose_name='Service Type'),
        ),
    ]