# Generated by Django 4.1.7 on 2023-05-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0024_alter_maintenance_distrispot_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.AlterField(
            model_name='rfid',
            name='frequency',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='rfid',
            name='voltage',
            field=models.CharField(max_length=25),
        ),
    ]
