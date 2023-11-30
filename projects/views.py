from django.shortcuts import render

from django.shortcuts import HttpResponse

def projects_list_page(request):
    return HttpResponse("You are at projects.")
