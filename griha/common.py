from contacts.models import ContactInfo

def get_common_content():
    return {
        'contact_info': ContactInfo.objects.first()
    }