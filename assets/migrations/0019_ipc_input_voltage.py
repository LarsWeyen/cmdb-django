# Generated by Django 4.1.7 on 2023-04-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_rename_power_intake_ipc_power_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipc',
            name='input_voltage',
            field=models.CharField(default='12 VDC', max_length=20),
            preserve_default=False,
        ),
    ]