from django.urls import path

from . import views

urlpatterns = [
    path("", views.projects_list_page, name="project-list-page")
]