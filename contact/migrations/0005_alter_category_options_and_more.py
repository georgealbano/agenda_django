# Generated by Django 4.2.5 on 2024-06-22 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='descripition',
            new_name='description',
        ),
    ]
