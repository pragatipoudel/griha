# Generated by Django 4.2.7 on 2023-12-19 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_name'),
        ('reviews', '0004_review_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
        migrations.AddField(
            model_name='review',
            name='project',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project'),
        ),
    ]
