# Generated by Django 4.2.7 on 2024-08-12 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.process')),
            ],
        ),
    ]
