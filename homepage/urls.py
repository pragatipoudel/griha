from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("inquiry/", views.submit_inquiry, name="submit-inquiry"),
]