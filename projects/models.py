from django.db import models
from services.models import Service
from django.utils.text import slugify


class Project(models.Model):
    name = models.CharField(
        max_length=200,
        unique = True
        )
    location = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    summary = models.TextField()
    description = models.TextField()
    header_image = models.ImageField(upload_to="projects/header/")
    services = models.ManyToManyField(Service, blank=True)
    slug = models.SlugField(default = "", null = False)
    rank = models.IntegerField(default=1)
    disabled = models.BooleanField(default=False)
    walkthrough_link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rank']


class AdditionalImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/additional/")

    def __str__(self):
        return self.project.name


