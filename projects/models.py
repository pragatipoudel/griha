from django.db import models
from services.models import Service

class Project(models.Model):
    name = models.CharField(
        max_length=200,
        unique = True
        )
    location = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    description = models.TextField()
    header_image = models.ImageField(upload_to="projects/header/")
    services = models.ManyToManyField(Service)
    slug = models.SlugField(default = "", null = False)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/additional/")

    def __str__(self):
        return self.project.name


