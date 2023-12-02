from django.shortcuts import render
from .models import HomePageContent
from contacts.models import ContactInfo
from griha.common import get_common_content

from django.http import HttpResponse

def home_page(request):
    home_page_contents = HomePageContent.objects.first()
    context = {
        'home_page_contents': home_page_contents,
        'current_page': 'home',
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)
