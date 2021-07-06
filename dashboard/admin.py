from django.contrib import admin
from .models import *
from shop.models import *
# Register your models here.
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Categorie)
admin.site.register(AdminUser)
admin.site.register(AdresseLivraison)
admin.site.register(ProduitCommande)
admin.site.register(Costumer)
admin.site.register(User)

