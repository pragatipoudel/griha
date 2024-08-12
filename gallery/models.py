from django.db import models


class MainGallery(models.Model):
    def __str__(self):
        return 'Main Gallery'

    class Meta:
        verbose_name_plural = 'Galleries'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(MainGallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="gallery/main/")

    def __str__(self):
        return self.image.name
