# Generated by Django 4.1.7 on 2023-04-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_alter_camera_ip_address_alter_dvr_ip_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrispot',
            name='type',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='DistrispotType',
        ),
    ]
