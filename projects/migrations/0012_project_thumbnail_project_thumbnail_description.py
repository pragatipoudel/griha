# Generated by Django 4.2.7 on 2025-01-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='projects/thumbnails/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail_description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
