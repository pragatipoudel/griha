# Generated by Django 4.2.7 on 2024-02-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_homepagecontent_header_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='fav_icon',
            field=models.ImageField(blank=True, upload_to='homepage/header'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='logo',
            field=models.ImageField(blank=True, upload_to='homepage/header'),
        ),
    ]
