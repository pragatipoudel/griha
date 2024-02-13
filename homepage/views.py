from django.shortcuts import render
from contacts.models import ContactInfo
from griha.common import get_common_content

from django.http import HttpResponse

def home_page(request):
    context = {
        'current_page': 'home',
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)
