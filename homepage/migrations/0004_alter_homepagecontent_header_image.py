# Generated by Django 4.2.7 on 2023-11-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_homepagecontent_tag_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecontent',
            name='header_image',
            field=models.ImageField(upload_to='media/homepage/header/'),
        ),
    ]