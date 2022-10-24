from django.shortcuts import render
from rest_framework import  generics,permissions
from rest_framework.response import Response
import rest_framework.status as status
from stock.models import CommandeFournisseur, Facture, Fournisseur, Gerant, InfosSortie, LigneCommande, Magasin, PaiementFournisseur, QuantitéStock

from stock.serializers import CommandeFournisseurSerializer, FactureSerializer, FournisseurSerializer, GerantSerializer, InfosSortieSerializer, LigneCommandeSerializer, MagasinSerializer, PaiementFournisseurSerializer, QuantitéStockSerializer

#### Gerant
 
class GerantListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Gerant.objects.all()
    serializer_class = GerantSerializer
    paginator = None
liste_create_gerantAPIView = GerantListCreateAPIView.as_view()


class RetriveUpdateDelGerant(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Gerant.objects.all()
    serializer_class = GerantSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_gerantAPIView = RetriveUpdateDelGerant.as_view()

##### Fournisseur

class FournisseurListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
    paginator = None
liste_create_FournisseurAPIView = FournisseurListCreateAPIView.as_view()

class RetriveUpdateDelFournisseur(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_FournisseurAPIView = RetriveUpdateDelFournisseur.as_view()




##### Magasin

class MagasinListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Magasin.objects.all()
    serializer_class = MagasinSerializer
    paginator = None
liste_create_MagasinAPIView = MagasinListCreateAPIView.as_view()

class RetriveUpdateDelMagasin(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Magasin.objects.all()
    serializer_class = MagasinSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_MagasinAPIView = RetriveUpdateDelMagasin.as_view()



##### QuantitéStock

class QuantitéStockListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = QuantitéStock.objects.all()
    serializer_class = QuantitéStockSerializer
    paginator = None
liste_create_QuantitéStockéeAPIView = QuantitéStockListCreateAPIView.as_view()


class RetriveUpdateDelQuantitéStock(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = QuantitéStock.objects.all()
    serializer_class = QuantitéStockSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_QuantitéStockAPIView = RetriveUpdateDelQuantitéStock.as_view()



##### InfosSortie

class InfosSortieListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = InfosSortie.objects.all()
    serializer_class = InfosSortieSerializer
    paginator = None
liste_create_InfosSortieAPIView = InfosSortieListCreateAPIView.as_view()

class RetriveUpdateDelInfosSortie(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = InfosSortie.objects.all()
    serializer_class = InfosSortieSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_InfosSortieAPIView = RetriveUpdateDelInfosSortie.as_view()



##### CommandeFournisseur

class CommandeFournisseurListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = CommandeFournisseur.objects.all()
    serializer_class = CommandeFournisseurSerializer
    paginator = None
liste_create_CommandeFournisseurAPIView = CommandeFournisseurListCreateAPIView.as_view()

class RetriveUpdateDelCommandeFournisseur(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = CommandeFournisseur.objects.all()
    serializer_class = CommandeFournisseurSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_CommandeFournisseurAPIView = RetriveUpdateDelCommandeFournisseur.as_view()



##### LigneCommande

class LigneCommandeListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = LigneCommande.objects.all()
    serializer_class = LigneCommandeSerializer
    paginator = None
liste_create_LigneCommandeAPIView = LigneCommandeListCreateAPIView.as_view()

class RetriveUpdateDelLigneCommande(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = LigneCommande.objects.all()
    serializer_class = LigneCommandeSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_LigneCommandeAPIView = RetriveUpdateDelLigneCommande.as_view()



##### Facture

class FactureListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    paginator = None
liste_create_FactureAPIView = FactureListCreateAPIView.as_view()

class RetriveUpdateDelFacture(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_FactureAPIView = RetriveUpdateDelFacture.as_view()



##### PaiementFournisseur

class PaiementFournisseurListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = PaiementFournisseur.objects.all()
    serializer_class = PaiementFournisseurSerializer
    paginator = None
liste_create_PaiementFournisseurAPIView = PaiementFournisseurListCreateAPIView.as_view()

class RetriveUpdateDelPaiementFournisseur(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = PaiementFournisseur.objects.all()
    serializer_class = PaiementFournisseurSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_PaiementFournisseurAPIView = RetriveUpdateDelPaiementFournisseur.as_view()