# Generated by Django 4.2.7 on 2023-11-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_homepagecontent_header_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecontent',
            name='tag_line',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
