from django.shortcuts import render, get_object_or_404
from django.http import Http404
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
    project = get_object_or_404(Project, slug=slug)
    if project.disabled:
        raise Http404

    context = {
        'project': project,
        'reviews': project.review_set.filter(verified=True),
        **get_common_content(),
    }

    return render(request, "projects/project-detail-page.html", context)

