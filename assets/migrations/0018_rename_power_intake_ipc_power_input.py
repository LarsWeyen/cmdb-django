# Generated by Django 4.1.7 on 2023-04-21 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_ipc_display_adapter_ipc_memory_ipc_power_intake_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipc',
            old_name='power_intake',
            new_name='power_input',
        ),
    ]