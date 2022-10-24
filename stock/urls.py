"""GestionPieceBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from .views import (
    liste_create_FactureAPIView,
    liste_create_CommandeFournisseurAPIView,
    liste_create_FournisseurAPIView,
    liste_create_gerantAPIView,
    liste_create_InfosSortieAPIView,
    liste_create_LigneCommandeAPIView,
    liste_create_MagasinAPIView,
    liste_create_PaiementFournisseurAPIView,
    liste_create_QuantitéStockéeAPIView,
    ret_update_CommandeFournisseurAPIView,
    ret_update_FactureAPIView,
    ret_update_FournisseurAPIView,
    ret_update_gerantAPIView,
    ret_update_InfosSortieAPIView,
    ret_update_LigneCommandeAPIView,
    ret_update_MagasinAPIView,
    ret_update_PaiementFournisseurAPIView,
    ret_update_QuantitéStockAPIView
)

urlpatterns = [

    # URL : Gerants

    path('gerants/',liste_create_gerantAPIView,name='listeCreerGerant'),
    path('gerants/<int:pk>/detail',ret_update_gerantAPIView,name='retUpdateGerant'),

     # URL : fournisseurs

    path('fournisseurs/',liste_create_FournisseurAPIView,name='listeCreerfournisseurs'),
    path('fournisseurs/<int:pk>/detail',ret_update_FournisseurAPIView,name='retUpdatefournisseurs'),

     # URL : magasins

    path('magasins/',liste_create_MagasinAPIView,name='listeCreermagasins'),
    path('magasins/<int:pk>/detail',ret_update_MagasinAPIView,name='retUpdatemagasins'),

    # URL : QuantitéStock

    path('QuantitéStock/',liste_create_QuantitéStockéeAPIView,name='listeCreerQuantitéStock'),
    path('QuantitéStock/<int:pk>/detail',ret_update_QuantitéStockAPIView,name='retUpdateQuantitéStock'),


     # URL : InfosSorties

    path('InfosSorties/',liste_create_InfosSortieAPIView,name='InfosSortiesCreate'),
    path('InfosSorties/<int:pk>/detail',ret_update_InfosSortieAPIView,name='InfosSortiesUpdate'),

     # URL : CommandeFournisseur

    path('CommandeFournisseurs/',liste_create_CommandeFournisseurAPIView,name='CommandeFournisseurCreate'),
    path('CommandeFournisseurs/<int:pk>/detail',ret_update_CommandeFournisseurAPIView,name='CommandeFournisseurUpdate'),

     # URL : LigneCommande

    path('LigneCommandes/',liste_create_LigneCommandeAPIView,name='LigneCommandeCreate'),
    path('LigneCommandes/<int:pk>/detail',ret_update_LigneCommandeAPIView,name='LigneCommandeUpdate'),

     # URL : Facture

    path('Factures/',liste_create_FactureAPIView,name='FactureListe'),
    path('Factures/<int:pk>/detail',ret_update_FactureAPIView,name='FactureUpdate'),

     # URL : PaiementFournisseurs

    path('PaiementFournisseurs/',liste_create_PaiementFournisseurAPIView,name='PaiementFournisseurListe'),
    path('PaiementFournisseurs/<int:pk>/detail',ret_update_PaiementFournisseurAPIView,name='PaiementFournisseurUpdate'),

]
