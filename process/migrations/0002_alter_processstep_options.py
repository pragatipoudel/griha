# Generated by Django 4.2.7 on 2024-08-12 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processstep',
            options={'ordering': ['step_number']},
        ),
    ]
