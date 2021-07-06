from django.urls import path
from . import views

urlpatterns = [
    path('', views.DshbordView, name='dashboard'),
    path('produit/', views.ProductList, name='listProduct'),
    path('produit/create', views.ProducView, name='ProductCreate'),
    path('produit/<str:pk>/edit', views.Produc_edit, name='editProduct'),
    path('produit/<str:pk>/delete', views.Produc_delete, name='deleteProduct'),
    path('commande/', views.ComandeList, name='listCommande'),
    path('commande/<str:pk>/edit', views.Comand_edit, name='editCommande'),
    path('commande/<str:pk>/delete', views.Comand_delete, name='deleteCommande'),
    path('commande/create', views.ComandeView, name='CommandeCreate'),
    path('categorie/', views.CategorieList, name='listCategorie'),
    path('categorie/<str:pk>/edit', views.categorie_edit, name='editCategorie'),
    path('categorie/<str:pk>/delete', views.categorie_delete, name='deleteCategorie'),
    path('categorie/create', views.categorie_View, name='createCategorie'),
    path('adminUsers/', views.AdminUserListView, name="adminUsersList"),
    path('adminUsers/create', views.AddAdminUserView, name="adminUsersCreate"),
    path('adminUsers/<str:pk>/Detaille', views.userDetaille, name='userDetaille'),
    path('user/<str:pk>/delete', views.userdelete, name='deleteuser'),
    path('logina/', views.UserLogin.as_view(), name='logina'),
    path('logout', views.logoutadmin, name='logouta'),
    path('client/', views.cientListView, name="clientList"),
    path('client/<str:pk>/Detaille', views.clientDetaille, name='clientDetaille'),
    path('client/<str:pk>/delete', views.Clientdelete, name='deleteclient'),
    path('commande/<str:pk>/Detaille', views.ComandeDetaille, name='CommandeDetaille'),


]


