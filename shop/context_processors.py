from datetime import datetime

from Ecom import settings
from dashboard.models import Categorie


def menu_Cat(request):
    Cat = Categorie.objects.all()
    return dict(Cat=Cat)


def cart(request):
    return {'cart': request.session.get(settings.CART_SESSION_ID)}



