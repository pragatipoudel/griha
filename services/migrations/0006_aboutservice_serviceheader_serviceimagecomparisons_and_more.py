# Generated by Django 4.2.7 on 2025-01-19 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_rename_header_image_service_thumbnail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='services/about/')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tagline', models.TextField(blank=True)),
                ('header_image', models.ImageField(upload_to='services/header/')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImageComparisons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_left', models.ImageField(upload_to='services/comparisons/')),
                ('label_left', models.CharField(max_length=100)),
                ('image_right', models.ImageField(upload_to='services/comparisons/')),
                ('label_right', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services/about/')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProcessStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=200)),
                ('step_description', models.TextField()),
                ('rank', models.IntegerField(default=1)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.serviceprocess')),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='ServiceValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('rank', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='ServiceWalkthrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True)),
                ('walkthrough_link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='project_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnail',
            field=models.ImageField(upload_to='services/thumbnails/'),
        ),
        migrations.DeleteModel(
            name='AdditionalImage',
        ),
        migrations.AddField(
            model_name='servicewalkthrough',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='servicevalue',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='serviceprocess',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='serviceimagecomparisons',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='serviceheader',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='aboutservice',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
