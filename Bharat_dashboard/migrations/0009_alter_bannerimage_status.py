# Generated by Django 4.1.5 on 2023-01-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bharat_dashboard', '0008_bannerimage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive')]),
        ),
    ]
