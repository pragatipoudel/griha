from django.db import models

class Service(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    description = models.TextField()
    header_image = models.ImageField(upload_to="services/header/")
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="services/additional/")

    def __str__(self):
        return self.service.name

