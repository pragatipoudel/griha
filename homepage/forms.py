from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class InquiryForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = PhoneNumberField(label="Phone Number", required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=True, )
    captcha = ReCaptchaField(
        required = True,
        error_messages= {
            'required': 'Please complete the reCAPTCHA challenge.'
        },
        widget = ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
                'data-size': 'compact',
            }
        )
    )
