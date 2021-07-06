from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('store/', views.StoreView.as_view(), name='store'),
    path('store/<int:idc>/', views.StoreView.as_view(), name='producct_by_cat'),
    path('store/<int:idc>/product/<int:idp>/', views.productDetail.as_view(), name='product_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:prod_id>/', views.add_to_cart, name='cartAdd'),
    path('cart/remove/<int:prod_id>/', views.remove_from_cart, name='cartRemove'),
    path('cart/update/<int:prod_id>/', views.update_cart, name='cartupdate'),
    path('rechercher/', views.rechercher, name='rechercher'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.order_create, name='order_create'),
    path('client/dashboard', views.clientdashbord, name='clientdashbord'),
    path('client/profile', views.clientprofile, name='clientprofile'),
    path('client/<int:pk>/edit', views.clientedit, name='clienteditinfo'),

]
