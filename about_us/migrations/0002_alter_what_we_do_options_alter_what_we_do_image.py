# Generated by Django 4.1.5 on 2023-01-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='what_we_do',
            options={'verbose_name_plural': 'What we do'},
        ),
        migrations.AlterField(
            model_name='what_we_do',
            name='image',
            field=models.FileField(blank=True, upload_to='What_we_do/about_us'),
        ),
    ]
