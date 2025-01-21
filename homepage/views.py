from django.shortcuts import render
from django.views.decorators.http import require_POST
from contacts.models import ContactInfo
from projects.models import Project
from services.models import Service
from reviews.models import Review
from process.models import Process
from gallery.models import MainGallery
from griha.common import get_common_content
from homepage.forms import InquiryForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.http import HttpResponse

def home_page(request):
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    reviews = Review.objects.filter(verified=True)[:3]
    process = Process.objects.first()
    gallery = MainGallery.objects.first()
    contact_info = ContactInfo.objects.first()

    context = {
        'current_page': 'home',
        'projects': projects,
        'process': process,
        'services': services,
        'gallery': gallery,
        'reviews': reviews,
        'contact_info': contact_info,
        **get_common_content(),
    }
    return render(request, 'homepage/home-page.html', context)


@require_POST
def submit_inquiry(request):
    form = InquiryForm(request.POST, auto_id=True, use_required_attribute=True)
    contact_info = ContactInfo.objects.first()

    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        phone = form.cleaned_data["phone"]

        html_message =  render_to_string(
            template_name='homepage/inquiry-email.html',
            context={
                'name': name,
                'email': email,
                'message': message,
                'phone': phone,
            }
        )
        plain_message = strip_tags(html_message)
        
        send_mail(
            f"Inquiry from {name}",
            plain_message,
            settings.EMAIL_HOST_USER,
            [contact_info.email],
            fail_silently=False,
            html_message=html_message
        )

        return render(request, 'homepage/inquiry.html', {
            **get_common_content(),
            'inquiry_form': form,
            'submitted': True
        })
        
    return render(request, 'homepage/inquiry.html', {
        **get_common_content(),
        'inquiry_form': form,
        'submitted': False
    })
