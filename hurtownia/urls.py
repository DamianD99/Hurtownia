from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='hurtownia-index'),
    path('', views.start, name='start'),
    path('developer/', views.developer, name='hurtownia-developer'),
    path('produkty/', views.produkty, name='produkty'),
    path('produkty_delete/<str:pk>/', views.delete_produkt, name='post_delete'),      #to ejst do viev nazwy def
    path('produkt_update/<str:pk>/', views.update_produkt, name='post_update'),      #to ejst do viev nazwy def
    path('zamówienia/', views.zamówienia, name='zamówienia'),
    path('klijenci/', views.klijent, name='klijent'),
    path('kijent_pokaz/<str:pk>/', views.klijent_pokaz, name='klijent-pokaz'),

    path('<int:id>/<slug:slug>/', views.pokaz_produkt, name='pokaz_produkt'),
    path('contact/', views.sendMail, name='contact'),
    path('serwis/', views.serwis, name='serwis'),
    path('zwrot/', views.zwrot, name='zwrot'),
    path('reklamacja/', views.reklamacja, name='reklamacja'),
    path('zwroty_admin/', views.zwroty_admin, name='zwrot-admin'),



]
