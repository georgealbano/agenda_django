# Generated by Django 5.0.6 on 2024-06-18 18:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_datee',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
