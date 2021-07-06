from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from dashboard.forms import *
# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        products = Produit.objects.all().filter(dispo=True)
        context = {'products': products}
        return render(request, "client/home.html", context)


class StoreView(View):
    def get(self, request, idc=None):

        if idc != None:
            categores = get_object_or_404(Categorie, id=idc)
            products = Produit.objects.filter(categorie=categores, dispo=True)
            prod_count = products.count()
        else:
            products = Produit.objects.all().filter(dispo=True)
            prod_count = products.count()

        context = {'products': products, 'prod_count': prod_count}
        return render(request, "client/store.html", context)


class productDetail(View):
    def get(self, request, idc, idp):
        try:
            product = get_object_or_404(Produit, categorie__id=idc, id=idp)
        except Exception as e:
            raise e
        context = {'product': product}
        return render(request, 'client/product_detail.html', context)


class CartView(View):
    def get(self, request):
        cart = request.session.get(settings.CART_SESSION_ID, {})
        cart_total_price = 0
        for key, val in cart.items():
            product = Produit.objects.get(id=key)
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['price'] = product.prixPro
            cart[str(product.id)]['total_price'] = float(cart[str(product.id)]['price']) * float(
                cart[str(product.id)]['quantity'])
            cart_total_price += cart[str(product.id)]['total_price']
        context = {'cart': cart, 'cart_total_price': cart_total_price}

        return render(request, 'client/cart.html', context)


def add_to_cart(request, prod_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    product = Produit.objects.get(id=prod_id)
    product_id = str(product.id)
    if product_id not in cart:
        cart[product_id] = {'quantity': 1, 'price': str(product.prixPro)}
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('store')


def remove_from_cart(request, prod_id):
    cart = request.session.get(settings.CART_SESSION_ID)
    if str(prod_id) in cart:
        del cart[str(prod_id)]
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart')


def update_cart(request, prod_id):
    cart = request.session.get(settings.CART_SESSION_ID)
    product = Produit.objects.get(id=prod_id)
    cart[str(prod_id)]['quantity'] = request.POST.get('quantity')
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart')


def rechercher(request):
    products = Produit.objects.filter(nomPro__icontains=request.POST.get("cle"))
    return render(request, "client/store.html", {'products': products})


class Register(View):
    def get(self, request):
        user_form = UserForm()
        costumer_form = CostumerForm()
        return render(request, 'client/register.html', {'user_form': user_form, 'costumer_form': costumer_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        costumer_form = CostumerForm(request.POST, request.FILES)

        if user_form.is_valid() and costumer_form.is_valid():
            # Créez un nouvel objet utilisateur mais évitez de l'enregistrer pour le moment
            new_user = user_form.save(commit=False)
            # Définir le mot de passe choisi
            new_user.set_password(user_form.cleaned_data['password'])
            # Enregistrer l'objet Utilisateur
            new_user.is_costumer = True
            new_user.save()
            new_costumer = costumer_form.save(commit=False)
            new_costumer.user = new_user
            # Enregistrer l'objet Client
            new_costumer.save()
            return render(request, 'client/register_done.html', {'new_user': new_user})
        return HttpResponse('Données invalides')


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'client/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('store')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        return redirect("home")


def user_logout(request):
    logout(request)
    return redirect('home')


def is_costumer(user):
    if user.is_authenticated and user.is_costumer:
        return True
    return False


@user_passes_test(is_costumer, login_url='/login/')
def order_create(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.Costumer = request.user.costumer
            order.etatCom = "En attente"

            order.save()

            for key, val in cart.items():
                product = Produit.objects.get(id=int(key))
                ProduitCommande.objects.create(commande=order, produit=product, prix=val['price'], qte=val['quantity'])
            # Vider le panier
            del request.session[settings.CART_SESSION_ID]
            return render(request, 'client/order_created.html', {'order': order})
    else:
        cart_total_price = 0
        for key, val in cart.items():
            cart_total_price += float(cart[key]['price']) * float(cart[key]['quantity'])
        form = OrderCreateForm()
        return render(request, 'client/create_order.html', {'form': form, 'cart_total_price': cart_total_price})


@user_passes_test(is_costumer, login_url='/login/')
def clientdashbord(request):
    if request.method == 'GET':
        # comande = Produit.objects.all().filter(dispo=True)
        client = Costumer.objects.get(user_id=request.user.id)

        # print(request.user.id)
        comandes = Commande.objects.filter(Costumer__user=request.user).first()
        
        produitcomm = ProduitCommande.objects.filter(commande__Costumer=client)
        totaleprice = produitcomm.aggregate(Sum('prix'))
        print(comandes)
        # print(produitcomm.count())
        Totalcom = client.commande_set.count()
        context = {"comandes": comandes, "Totalcom": Totalcom, "totaleprice": totaleprice, "produitcomm": produitcomm, "client": client}
        return render(request, "client/clientdashbord.html", context)



@user_passes_test(is_costumer, login_url='/login/')
def clientprofile(request):
    if request.method == 'GET':
        client = Costumer.objects.get(user_id=request.user.id)
        comandes = Commande.objects.filter(Costumer__user=request.user).first()
        context={"client": client, "comandes": comandes}
        return render(request, "client/clientprofile.html", context)



@user_passes_test(is_costumer, login_url='/login/')
def clientedit(request, pk):
    if request.method == 'GET':
        client = Costumer.objects.get(user_id=pk)
        user_form = UserForm(instance=client.user)
        costumer_form = CostumerForm(instance=client)
        context = {"user_form": user_form, "costumer_form": costumer_form}
        return render(request, "client/editclient.html", context)
    if request.method == 'POST':
        client = Costumer.objects.get(user_id=pk)
        user_form = UserForm(request.POST, instance=client.user)
        costumer_form = CostumerForm(request.POST, instance=client)
        if user_form.is_valid() and costumer_form.is_valid():
            user_form.save()
            costumer_form.save()
            return redirect('clientprofile')