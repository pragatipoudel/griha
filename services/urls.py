from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.service_detail_page, name="service-detail-page")
]