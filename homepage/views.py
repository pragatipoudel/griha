from django.shortcuts import render
from contacts.models import ContactInfo
from projects.models import Project
from services.models import Service
from reviews.models import Review
from process.models import Process
from griha.common import get_common_content

from django.http import HttpResponse

def home_page(request):
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    reviews = Review.objects.filter(verified=True)[:3]
    process = Process.objects.first()

    context = {
        'current_page': 'home',
        'projects': projects,
        'process': process,
        'services': services,
        'reviews': reviews,
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)
