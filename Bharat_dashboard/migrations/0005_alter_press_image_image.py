# Generated by Django 4.1.5 on 2023-01-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bharat_dashboard', '0004_press_image_press_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='press_image',
            name='image',
            field=models.FileField(blank=True, upload_to='photo/Press-image'),
        ),
    ]