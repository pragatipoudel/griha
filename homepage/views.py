from django.shortcuts import render
from contacts.models import ContactInfo
from projects.models import Project
from services.models import Service
from reviews.models import Review
from griha.common import get_common_content

from django.http import HttpResponse

def home_page(request):
    projects = Project.objects.all()[:3]
    services = Service.objects.all()[:3]
    reviews = Review.objects.all()[:2]

    context = {
        'current_page': 'home',
        'projects': projects,
        'services': services,
        'reviews': reviews,
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)
