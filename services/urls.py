from django.urls import path

from . import views

urlpatterns = [
    path("", views.services_list_page, name="service-list-page"),
    # path("<slug:slug>/", views.service_detail_page, name="service-detail-page")
]