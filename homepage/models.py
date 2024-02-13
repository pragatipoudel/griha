from django.db import models

class HomePageContent(models.Model):
    tag_line = models.CharField(max_length=254, blank=True)
    header_image = models.ImageField(upload_to="homepage/header/")
    header_video = models.FileField(upload_to="homepage/header/", blank=True)
    logo = models.ImageField(upload_to="homepage/header", blank=True)
    nav_bar_logo = models.ImageField(upload_to="homepage/header", blank=True)
    fav_icon = models.ImageField(upload_to="homepage/header", blank=True)

    def __str__(self):
        return "Home Page Content"
