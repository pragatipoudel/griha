from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    description = models.TextField()
    header_image = models.ImageField(upload_to="projects/header/")
    slug = models.SlugField(default = "", null = False)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    additional_images = models.ImageField(upload_to="projects/additional/")

    def __str__(self):
        return self.project.name


