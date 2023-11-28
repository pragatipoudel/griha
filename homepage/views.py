from django.shortcuts import render
from .models import HomePageContent

from django.http import HttpResponse

def homePage(request):
    homePageContents = HomePageContent.objects.first()
    context = {'homePageContents': homePageContents}
    return render(request, 'homepage/home-page.html', context)
