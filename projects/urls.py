from django.urls import path

from . import views

urlpatterns = [
    path("", views.projects_list_page, name="project-list-page"),
    path("<slug:slug>/", views.project_detail_page, name="project-detail-page")
]