# Generated by Django 4.1.5 on 2023-01-18 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bharat_dashboard', '0009_alter_bannerimage_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerimage',
            name='is_active',
        ),
    ]
