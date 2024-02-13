from contacts.models import ContactInfo
from homepage.models import HomePageContent

def get_common_content():
    home_page_contents = HomePageContent.objects.first()
    return {
        'contact_info': ContactInfo.objects.first(),
        'home_page_contents': home_page_contents,
    }