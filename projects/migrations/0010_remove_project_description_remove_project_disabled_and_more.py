# Generated by Django 4.2.7 on 2025-01-19 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_servicevalue_service'),
        ('projects', '0009_project_disabled_project_walkthrough_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='disabled',
        ),
        migrations.RemoveField(
            model_name='project',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='location',
        ),
        migrations.RemoveField(
            model_name='project',
            name='services',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='project',
            name='walkthrough_link',
        ),
        migrations.AddField(
            model_name='project',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AdditionalImage',
        ),
    ]
