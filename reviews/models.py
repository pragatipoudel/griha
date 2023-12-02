from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ReviewPageContent(models.Model):
    header_image = models.ImageField(upload_to="reviews/header/")

    def __str__(self):
        return "Review Page Content"