# Generated by Django 4.2.7 on 2024-02-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactinfo_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
