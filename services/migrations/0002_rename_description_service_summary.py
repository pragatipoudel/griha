# Generated by Django 4.2.7 on 2024-02-14 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='description',
            new_name='summary',
        ),
    ]