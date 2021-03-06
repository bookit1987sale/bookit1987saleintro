# Generated by Django 2.0.2 on 2018-04-26 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20180426_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientevent',
            name='staff',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_client_event', to='staffer.StaffMember', verbose_name='Staff Member'),
        ),
        migrations.AlterField(
            model_name='staffevent',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name="I'm cancelling this request"),
        ),
    ]
