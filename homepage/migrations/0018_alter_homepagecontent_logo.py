# Generated by Django 4.2.7 on 2024-12-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_virtualwalkthrough_home_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecontent',
            name='logo',
            field=models.ImageField(upload_to='homepage/header'),
        ),
    ]
