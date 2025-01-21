from contacts.models import ContactInfo
from homepage.models import HomePageContent
from homepage.forms import InquiryForm

def get_common_content():
    home_page_contents = HomePageContent.objects.first()
    return {
        'contact_info': ContactInfo.objects.first(),
        'home_page_contents': home_page_contents,
        'inquiry_form': InquiryForm(auto_id=True, use_required_attribute=True)
    }