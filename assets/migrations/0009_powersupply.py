# Generated by Django 4.1.7 on 2023-04-04 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_camera_resolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('manufacturer', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('serial', models.CharField(max_length=150)),
                ('voltage', models.CharField(max_length=25)),
                ('form_factor', models.CharField(max_length=25)),
                ('wattage', models.CharField(max_length=25)),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]