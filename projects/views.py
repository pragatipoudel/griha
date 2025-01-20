from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Project
from griha.common import get_common_content

from django.shortcuts import HttpResponse


def project_detail_page(request, slug):
    project = get_object_or_404(Project, slug=slug)

    context = {
        'project': project,
        **get_common_content(),
    }

    return render(request, "projects/project-detail-page.html", context)

