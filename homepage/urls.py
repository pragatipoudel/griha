from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    # path("r3F8y/new-home-page-draft/", views.home_page, name="new-home-page")
]