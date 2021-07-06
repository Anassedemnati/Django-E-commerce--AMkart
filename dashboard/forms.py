from django import forms
from django.contrib.auth.models import User
from .models import *


class ComandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"


        labels = {
            "modePaiement": "Mode de paiement",
            "etatCom": "Etat de la commande",
            "modePaiement": "Mode de paiement",
            "prixTax": "Tax",
            "prixLivraison": "Prix de livraison",
            "prixTotal": "Prix total",
            "dateCom": "Date de commande",
            "dateLivraison": "Date de livraison",
            "categorie": "Categorie",
            "Costumer": "Client",

        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
        labels = {
            "nomPro": "Nom",
            "image": "Image",
            "marque": "Marque",
            "descriptionPro": "Description",
            "prixPro": "Prix",
            "contiteStock": "Contite en Stock",
            "categorie": "Categorie",
            "utilisateur": "Utilisateur",
            "dispo": "Disponible",
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"
        labels = {
            "nomCat": "Nom",
            "descriptionCat": "Description",
        }


class AdresseLivraisonForm(forms.ModelForm):
    class Meta:
        model = AdresseLivraison
        fields = "__all__"


class AdminUserForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ('date_of_birth', 'photo')
        labels = {
            "date_of_birth": "Date de naissance"
        }
