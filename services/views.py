from django.shortcuts import render
from .models import Service, AdditionalImage
from griha.common import get_common_content
from django.shortcuts import HttpResponse


def services_list_page(request):
    services = Service.objects.all()

    context = {
        'services': services,
        'current_page': 'services',
        **get_common_content(), 
    }
    return render(request, "services/service-list-page.html", context)


def service_detail_page(request, slug):
    return HttpResponse("You are at Service Detail Page")
