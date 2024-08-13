from django.shortcuts import render
from contacts.models import ContactInfo
from projects.models import Project
from services.models import Service
from reviews.models import Review
from process.models import Process
from gallery.models import MainGallery
from griha.common import get_common_content

from django.http import HttpResponse

def home_page(request):
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    reviews = Review.objects.filter(verified=True)[:3]
    process = Process.objects.first()
    gallery = MainGallery.objects.first()
    contact_info = ContactInfo.objects.first()

    context = {
        'current_page': 'home',
        'projects': projects,
        'process': process,
        'services': services,
        'gallery': gallery,
        'reviews': reviews,
        'contact_info': contact_info,
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)


def old_home_page(request):
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    reviews = Review.objects.filter(verified=True)[:3]
    process = Process.objects.first()
    gallery = MainGallery.objects.first()
    contact_info = ContactInfo.objects.first()

    context = {
        'current_page': 'home',
        'projects': projects,
        'process': process,
        'services': services,
        'gallery': gallery,
        'reviews': reviews,
        'contact_info': contact_info,
        **get_common_content(),
    }
    return render(request, 'homepage/old-home-page.html', context)
