from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import *
from shop.models import *
from .filters import *
from .forms import *
from shop.forms import *
# Create your views here.
from django.views import View


# Create your views here.

def is_admin(user):
    if user.is_authenticated and user.is_admin:
        return True
    return False


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def DshbordView(request):
    if request.method == 'GET':
        commands = Commande.objects.all()
        clients = Costumer.objects.all()
        totalCom = Commande.objects.count()
        totalLivre = Commande.objects.filter(etatCom='Livré').count()
        totalenatent = Commande.objects.filter(etatCom='En attente').count()
        context = {'clients': clients, 'totalCom': totalCom, 'totalLivre': totalLivre, 'totalenatent': totalenatent,
                   'commands': commands}
        return render(request, "admin/dashboard.html", context)


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def ProductList(request):
    if request.method == 'GET':
        products = Produit.objects.all()
        prodFilter = ProduitFilter(request.GET, queryset=products)
        products = prodFilter.qs
        context = {'products': products, 'prodFilter': prodFilter}
        return render(request, "admin/listProduct.html", context)


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def ProducView(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, "admin/Formproduit.html", {'form': form})

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("listProduct")


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def Produc_edit(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Produit, id=pk)
        form = ProductForm(instance=product)
        return render(request, 'admin/Formproduit.html', {'form': form})

    if request.method == 'POST':
        product = get_object_or_404(Produit, id=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('listProduct')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def Produc_delete(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Produit, id=pk)
        return render(request, 'admin/deleteProduct.html', {'product': product})

    if request.method == 'POST':
        product = get_object_or_404(Produit, id=pk)
        product.delete()
        return redirect('listProduct')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def ComandeList(request):
    if request.method == 'GET':
        Commandes = Commande.objects.all()
        context = {'Commandes': Commandes}
        return render(request, "admin/listComande.html", context)


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def Comand_edit(request, pk):
    if request.method == 'GET':
        comand = get_object_or_404(Commande, id=pk)
        form = ComandeForm(instance=comand)
        return render(request, 'admin/FormComande.html', {'form': form})

    if request.method == 'POST':
        comand = get_object_or_404(Commande, id=pk)
        form = ComandeForm(request.POST, instance=comand)
        if form.is_valid():
            form.save()
            return redirect('listCommande')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def Comand_delete(request, pk):
    if request.method == 'GET':
        comand = get_object_or_404(Commande, id=pk)
        return render(request, 'admin/deleteComande.html', {'comand': comand})

    if request.method == 'POST':
        comand = get_object_or_404(Commande, id=pk)
        comand.delete()
        return redirect('listCommande')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def ComandeView(request):
    if request.method == 'GET':
        form = ComandeForm()
        return render(request, "admin/FormComande.html", {'form': form})

    if request.method == 'POST':
        form = ComandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("listCommande")


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def CategorieList(request):
    if request.method == 'GET':
        Categories = Categorie.objects.all()
        context = {'Categories': Categories}
        return render(request, "admin/listCategories.html", context)


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def categorie_edit(request, pk):
    if request.method == 'GET':
        categorie = get_object_or_404(Categorie, id=pk)
        form = CategoryForm(instance=categorie)
        return render(request, 'admin/FormCategorie.html', {'form': form})

    if request.method == 'POST':
        categorie = get_object_or_404(Categorie, id=pk)
        form = ComandeForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('listCategorie')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def categorie_delete(request, pk):
    if request.method == 'GET':
        categorie = get_object_or_404(Categorie, id=pk)
        return render(request, 'admin/deleteCategorie.html', {'categorie': categorie})

    if request.method == 'POST':
        categorie = get_object_or_404(Categorie, id=pk)
        categorie.delete()
        return redirect('listCategorie')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def categorie_View(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, "admin/FormCategorie.html", {'form': form})

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("listCategorie")


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def AdminUserListView(request):
    if request.method == 'GET':
        adminUsers = AdminUser.objects.all()
        return render(request, "admin/listUser.html", {'adminUsers': adminUsers})


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def AddAdminUserView(request):
    if request.method == 'GET':
        user_form = UserForm()
        admin_form = AdminUserForm(request.POST)
        context = {'user_form': user_form, 'admin_form': admin_form}
        return render(request, 'admin/FormAdmin.html', context)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        admin_form = AdminUserForm(request.POST, request.FILES)

        if user_form.is_valid() and admin_form.is_valid():
            # Créez un nouvel objet utilisateur mais évitez de l'enregistrer pour le moment
            new_user = user_form.save(commit=False)
            # Définir le mot de passe choisi
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_admin = True
            # Enregistrer l'objet Utilisateur
            new_user.save()
            new_admin = admin_form.save(commit=False)
            new_admin.user = new_user
            new_admin.save()
            return render(request, 'admin/Admin_register_done.html', {'new_user': new_user})
        return HttpResponse('Données invalides')


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def userDetaille(request, pk):
    if request.method == 'GET':
        seller = get_object_or_404(AdminUser, id=pk)

        produits = seller.produit_set.all()
        TotalProd = seller.produit_set.count()
        context = {'seller': seller, 'produits': produits, 'TotalProd': TotalProd}

        return render(request, 'admin/userDetaille.html', context)


@user_passes_test(is_admin, login_url='/dashbord/logina/')
def userdelete(request, pk):
    if request.method == 'GET':
        seller = get_object_or_404(AdminUser, id=pk)
        return render(request, 'admin/deleteUser.html', {'seller': seller})

    if request.method == 'POST':
        seller = get_object_or_404(AdminUser, id=pk)
        seller.delete()
        return redirect('adminUsersList')


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'admin/loginA.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        return redirect("logina")


def logoutadmin(request):
    logout(request)
    return redirect('logina')

@user_passes_test(is_admin, login_url='/dashbord/logina/')
def cientListView(request):
    if request.method == 'GET':
        clientUsers = Costumer.objects.all()
        return render(request, "admin/listClient.html", {'clientUsers': clientUsers})

@user_passes_test(is_admin, login_url='/dashbord/logina/')
def clientDetaille(request, pk):
    if request.method == 'GET':
        client = get_object_or_404(Costumer, id=pk)

        comandes = client.commande_set.all()
        Totalcom = client.commande_set.count()
        context = {'client': client, 'comandes': comandes, 'Totalcom': Totalcom}

        return render(request, 'admin/ClientDetaille.html', context)

@user_passes_test(is_admin, login_url='/dashbord/logina/')
def Clientdelete(request, pk):
    if request.method == 'GET':
        client = get_object_or_404(Costumer, id=pk)
        return render(request, 'admin/deleteclient.html', {'client': client})

    if request.method == 'POST':
        client = get_object_or_404(Costumer, id=pk)
        client.delete()
        return redirect('clientList')

@user_passes_test(is_admin, login_url='/dashbord/logina/')
def ComandeDetaille(request, pk):
    if request.method == 'GET':
        com = get_object_or_404(Commande, id=pk)

        #produitcomm = com.produitcommande_set.all()
        produitcomm = ProduitCommande.objects.filter(commande_id=pk)
        # produits = produitcomm.produit_set.all()
        Totalprod = produitcomm.count()
        totaleprice = produitcomm.aggregate(Sum('prix'))
        context = {'produitcommandes': produitcomm, 'com': com, 'Totalprod': Totalprod, "totaleprice": totaleprice}

        return render(request, 'admin/commandeDetaille.html', context)
