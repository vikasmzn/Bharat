# Generated by Django 4.1.5 on 2023-01-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bharat_dashboard', '0005_alter_press_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='press_release',
            name='hyperlink',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]