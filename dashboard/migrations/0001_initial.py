# Generated by Django 3.2 on 2021-06-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='images/admins/')),
            ],
        ),
        migrations.CreateModel(
            name='AdresseLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresseLiv', models.TextField(blank=True, max_length=256, null=True)),
                ('villeLiv', models.CharField(max_length=200)),
                ('codePostal', models.IntegerField()),
                ('payeLiv', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCat', models.CharField(max_length=100, null=True)),
                ('descriptionCat', models.TextField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modePaiement', models.CharField(choices=[('cart', 'carte'), ('paypal', 'paypal'), ('au livraison', 'au livraison')], max_length=20)),
                ('prixTax', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('prixLivraison', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('prixTotal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dateCom', models.DateField(auto_now_add=True)),
                ('etatCom', models.CharField(choices=[('En attente', 'En attente'), ('En cours de livraison', 'En cours de livraison'), ('Livré', 'Livré')], max_length=30)),
                ('dateLivraison', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPro', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/produit')),
                ('marque', models.CharField(max_length=100, null=True)),
                ('descriptionPro', models.TextField(blank=True, max_length=600, null=True)),
                ('prixPro', models.DecimalField(decimal_places=2, max_digits=7)),
                ('contiteStock', models.IntegerField()),
                ('dispo', models.BooleanField(default=True)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.IntegerField(null=True)),
                ('prix', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.produit')),
            ],
        ),
    ]
