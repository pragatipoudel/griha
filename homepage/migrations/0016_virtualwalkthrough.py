# Generated by Django 4.2.7 on 2024-12-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_tagline_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualWalkthrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('walkthrough_link', models.URLField()),
            ],
        ),
    ]
