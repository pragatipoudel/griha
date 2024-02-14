from django.db import models
from homepage.models import HomePageContent
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    summary = models.TextField()
    description = models.TextField(blank=True)
    header_image = models.ImageField(upload_to="services/header/")
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="services/additional/")

    def __str__(self):
        return self.service.name

