from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ReviewForm
from .models import Review, ReviewPageContent
from griha.common import get_common_content

def reviews_list_page(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(verified=True)
    review_page_contents = ReviewPageContent.objects.first()
    context = {
        'reviews': reviews,
        'form': form,
        'current_page': 'reviews',
        **get_common_content(),
        'review_page_contents': review_page_contents

    }
    return render(request, "reviews/reviews-list.html", context)

