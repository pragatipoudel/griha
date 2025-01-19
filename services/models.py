from django.db import models
from homepage.models import HomePageContent
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    project_name = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to="services/thumbnails/")
    slug = models.SlugField(default="", null=False)
    rank = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rank']

    @property
    def short_name(self):
        return self.project_name or self.name


class ServiceHeader(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tagline = models.TextField(blank=True)
    header_image = models.ImageField(upload_to="services/header/")

    def __str__(self):
        return f'Header for {self.service.name}'


class AboutService(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="services/about/")

    def __str__(self):
        return f'About {self.service.name}'


class ServiceProcess(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="services/about/")

    def __str__(self):
        return f'Process for {self.service.name}'


class ServiceProcessStep(models.Model):
    process = models.ForeignKey(ServiceProcess, on_delete=models.CASCADE,
                                related_name="steps")
    step_name = models.CharField(max_length=200)
    step_description = models.TextField()
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.step_name

    class Meta:
        ordering = ['rank']


class ServiceWalkthrough(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    walkthrough_link = models.URLField()

    def __str__(self):
        return f'Walkthrough for {self.service.name}'


class ServiceImageComparisons(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    image_left = models.ImageField(upload_to="services/comparisons/")
    label_left = models.CharField(max_length=100)
    image_right = models.ImageField(upload_to="services/comparisons/")
    label_right = models.CharField(max_length=100)

    def __str__(self):
        return f'Image comparisons for {self.service.name}'


class ServiceValue(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="values")
    value_title = models.CharField(max_length=200)
    description = models.TextField()
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.value_title

    class Meta:
        ordering = ['rank']

