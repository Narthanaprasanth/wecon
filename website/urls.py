from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    
    path('products/', views.products_page, name='products_page'),

    path('e7018/', views.e7018, name='e7018'),

    path('e6013/',views.e6013,name='e6013'),

]