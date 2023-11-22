# Generated by Django 4.2.7 on 2023-11-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
