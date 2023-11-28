from django.db import models

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "Contact Info"
