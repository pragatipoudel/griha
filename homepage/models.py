from django.db import models


class HomePageContent(models.Model):
    tag_line = models.TextField(blank=True)
    welcome_message = models.TextField(blank=True)
    header_image = models.ImageField(upload_to="homepage/header/")
    header_video = models.FileField(upload_to="homepage/header/", blank=True)
    logo = models.ImageField(upload_to="homepage/header", blank=True)
    small_logo = models.ImageField(upload_to="homepage/header", blank=True)
    fav_icon = models.ImageField(upload_to="homepage/header", blank=True)

    def __str__(self):
        return "Home Page Content"


class AboutContent(models.Model):
    background_image = models.ImageField(upload_to="homepage/about/", blank=True)
    summary = models.TextField()
    home_page = models.OneToOneField(HomePageContent, on_delete=models.CASCADE)

    def __str__(self):
        return "Content for about us"


class TagLine(models.Model):
    home_page = models.OneToOneField(HomePageContent, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    services = models.TextField(blank=True)
    gallery = models.TextField(blank=True)
    walkthrough = models.TextField(blank=True)

    def __str__(self):
        return 'Tag lines for homepage'
