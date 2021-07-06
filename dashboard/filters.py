import django_filters
from django_filters import CharFilter
from .models import *


class ProduitFilter(django_filters.FilterSet):
    nomPro = CharFilter(field_name='nomPro', lookup_expr='icontains')
    marque = CharFilter(field_name='marque', lookup_expr='icontains')
    class Meta:
        model = Produit
        fields = "__all__"
        exclude = ['nomPro', 'image', 'descriptionPro', 'prixPro', 'contiteStock', 'marque', 'dispo']
