from django import forms
from .models import Review
from django_recaptcha.fields import ReCaptchaField
from projects.models import Project

class ReviewForm(forms.ModelForm):
    captcha =  ReCaptchaField(
        required = True,
        error_messages= {
            'required': 'Please complete the reCAPTCHA challenge.'
        }
    )

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['project', 'rank']
