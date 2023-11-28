from django.db import models

class HomePageContent(models.Model):
    tag_line = models.CharField(max_length=254, blank=True)
    header_image = models.ImageField(upload_to="homepage/header/")
    header_video = models.FileField(upload_to="homepage/header/", blank=True)
