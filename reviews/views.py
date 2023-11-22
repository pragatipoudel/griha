from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .forms import ReviewForm
from .models import Review

def reviewsListPage(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    context = {'reviews': reviews, 'form': form}
    return render(request, "reviews/list.html", context)

