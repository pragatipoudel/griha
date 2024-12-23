# Generated by Django 4.2.7 on 2024-12-14 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_aboutcontent_tagline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcontent',
            name='tagline',
        ),
        migrations.CreateModel(
            name='TagLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True)),
                ('services', models.TextField(blank=True)),
                ('gallery', models.TextField(blank=True)),
                ('walkthrough', models.TextField(blank=True)),
                ('home_page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.homepagecontent')),
            ],
        ),
    ]
