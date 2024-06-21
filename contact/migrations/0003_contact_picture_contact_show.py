# Generated by Django 4.2.5 on 2024-06-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_created_datee_contact_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
