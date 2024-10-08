from django.db import models
from projects.models import Project

class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    rank = models.IntegerField(default=1)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rank']

class ReviewPageContent(models.Model):
    header_image = models.ImageField(upload_to="reviews/header/")

    def __str__(self):
        return "Review Page Content"