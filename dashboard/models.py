from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from shop.models import *


# Create your models here.
class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/admins/', blank=True)

    def __str__(self):
        return self.user.get_username()


class Categorie(models.Model):
    nomCat = models.CharField(max_length=100, null=True)
    descriptionCat = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.nomCat

    def get_url(self):
        return reverse('producct_by_cat', args=[self.id])


class Produit(models.Model):
    nomPro = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/produit")
    marque = models.CharField(max_length=100, null=True)
    descriptionPro = models.TextField(max_length=600, null=True, blank=True)
    prixPro = models.DecimalField(max_digits=7, decimal_places=2)
    contiteStock = models.IntegerField()
    categorie = models.ForeignKey(
        Categorie, null=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    dispo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + "-" + self.nomPro

    def get_url(self):
        return reverse('product_detail', args=[self.categorie.id, self.id])

    def get_nom(self):
        return self.nomPro


class Commande(models.Model):
    # les mode de paiement
    modePaiement = (
        ('cart', 'carte'),
        ('paypal', 'paypal'),
        ('au livraison', 'au livraison'),
    )
    # les etat de la commande
    etatCom = (
        ('En attente', 'En attente'),
        ('En cours de livraison', 'En cours de livraison'),
        ('Livré', 'Livré'),
    )
    modePaiement = models.CharField(max_length=20, choices=modePaiement)
    prixTax = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    prixLivraison = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    prixTotal = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    dateCom = models.DateField(auto_now_add=True)
    etatCom = models.CharField(max_length=30, choices=etatCom)
    dateLivraison = models.DateField(null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    Costumer = models.ForeignKey(Costumer, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default=" ")
    postal_code = models.CharField(max_length=20, default=" ")
    city = models.CharField(max_length=100, default="Casablanca")

    def __str__(self):
        return str(self.dateCom)


class ProduitCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField(null=True)
    prix = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return str(self.commande.id) + "-" + self.produit.nomPro

    def get_prod_id(self):
        return self.produit.id


class AdresseLivraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    adresseLiv = models.TextField(max_length=256, null=True, blank=True)
    villeLiv = models.CharField(max_length=200)
    codePostal = models.IntegerField()
    payeLiv = models.CharField(max_length=200)

    def __str__(self):
        return str(self.commande_id) + "_" + self.villeLiv + "_" + self.payeLiv
