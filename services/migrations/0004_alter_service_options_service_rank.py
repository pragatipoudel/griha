# Generated by Django 4.2.7 on 2024-02-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-rank']},
        ),
        migrations.AddField(
            model_name='service',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]
