# Generated by Django 4.2.7 on 2025-01-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_aboutservice_serviceheader_serviceimagecomparisons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprocessstep',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='services.serviceprocess'),
        ),
    ]
