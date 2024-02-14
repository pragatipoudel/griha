from django.shortcuts import render, get_object_or_404
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
    service = get_object_or_404(Service, slug=slug)

    context = {
        'service': service,
        **get_common_content(),
    }
    return render(request, "services/service-detail-page.html", context)
