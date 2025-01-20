from django.db import models
from services.models import Service
from django.utils.text import slugify


class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='projects')
    name = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(default = "", null = False)
    rank = models.IntegerField(default=1)

    thumbnail = models.ImageField(upload_to="projects/thumbnails/")
    thumbnail_description = models.CharField(max_length=200, blank=True)

    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to="projects/gallery/")

    def __str__(self):
        return f'Image for {self.project.name}'
