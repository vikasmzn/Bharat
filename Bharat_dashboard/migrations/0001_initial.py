# Generated by Django 4.1.5 on 2023-01-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_image', models.ImageField(blank=True, null=True, upload_to='banner')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('button', models.CharField(blank=True, max_length=100, null=True)),
                ('hyperlink', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Banner Image',
            },
        ),
    ]