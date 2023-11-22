from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Review

def reviewsListPage(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, "reviews/list.html", context)

    


