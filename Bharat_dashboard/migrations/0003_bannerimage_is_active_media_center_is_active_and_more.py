# Generated by Django 4.1.5 on 2023-01-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bharat_dashboard', '0002_media_center_our_focus_our_members_our_vision'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='media_center',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='our_focus',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='our_members',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='our_vision',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
