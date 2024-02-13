from django.shortcuts import render
from .models import Project, AdditionalImage
from griha.common import get_common_content

from django.shortcuts import HttpResponse

def projects_list_page(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
        'current_page': 'projects',
        **get_common_content(),
    }

    return render(request, "projects/project-list-page.html", context)

def project_detail_page(request, slug):
    project = Project.objects.get(slug=slug)
    

    context = {
        'project': project,
        **get_common_content(),
    }

    return render(request, "projects/project-detail-page.html", context)

