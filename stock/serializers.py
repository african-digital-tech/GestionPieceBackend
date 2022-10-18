
from rest_framework import  serializers

from stock.models import CommandeFournisseur, Facture, Fournisseur, Gerant, InfosSortie, LigneCommande, Magasin, PaiementFournisseur, PieceStockée, QuantitéStock


class GerantSerializer(serializers.ModelSerializer):
    '''
        liste des gerants des magasins
    '''

    class Meta:
        model = Gerant
        fields= '__all__'


class FournisseurSerializer(serializers.ModelSerializer):
    '''
        Liste de tous les fournisseurs de l'entreprise
    '''

    class Meta:
        model= Fournisseur
        fields = '__all__'


class MagasinSerializer(serializers.ModelSerializer):
    '''
        liste de tous les magasins
    '''

    class Meta:
        model = Magasin
        fields= '__all__'


class PieceStockéeSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les pièces stockées
    '''

    class Meta:
        model= PieceStockée
        fields = '__all__'



class InfosSortieSerializer(serializers.ModelSerializer):
    '''
        liste des informations supplémentaire sur une sortie de pieces
    '''

    class Meta:
        model = InfosSortie
        fields= '__all__'



class QuantitéStockSerializer(serializers.ModelSerializer):
    '''
        liste des informations supplémentaire sur une sortie de pieces
    '''

    class Meta:
        model = QuantitéStock
        fields= '__all__'


class CommandeFournisseurSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les commandes fournisseurs
    '''

    class Meta:
        model= CommandeFournisseur
        fields = '__all__'




class LigneCommandeSerializer(serializers.ModelSerializer):
    '''
        Detail sur une commande fournisseur
    '''

    class Meta:
        model = LigneCommande
        fields= '__all__'


class FactureSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les factures fournisseurs
    '''

    class Meta:
        model= Facture
        fields = '__all__'




class PaiementFournisseurSerializer(serializers.ModelSerializer):
    '''
        liste des informations sur un paiement
    '''

    class Meta:
        model = PaiementFournisseur
        fields= '__all__'


