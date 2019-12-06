from .models import Contacts

def settings(request):
    return {'settings': Contacts.load()}