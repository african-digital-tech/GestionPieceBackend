
from rest_framework import  serializers
from pieces.models import Piece
from stock.linkSerializers import RelatedGerantSerializer

from stock.models import CommandeFournisseur, Facture, Fournisseur, Gerant, InfosSortie, LigneCommande, Magasin, PaiementFournisseur, QuantitéStock
from django.contrib.auth.models import User

class GerantSerializer(serializers.ModelSerializer):
    '''
        liste des gerants des magasins
    '''

    class Meta:
        model = Gerant
        fields= '__all__'


class UserSerializer(serializers.ModelSerializer):
    '''
        liste des gerants des magasins
    '''

    class Meta:
        model = User
        fields= ('id','username','first_name','last_name','email')


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
    gerantData = serializers.SerializerMethodField()
    class Meta:
        model = Magasin
        fields= ('id','nom','gerant','gerantData','listPieceEntree','listPieceSortie')

    def get_gerantData(self,obj):
        return User.objects.filter(pk=obj.gerant_id).values("id","username","first_name","last_name","email")





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
    magasinData = serializers.SerializerMethodField()
    pieceData = serializers.SerializerMethodField()


    class Meta:
        model = QuantitéStock
        fields= ('id','quantiteStockee','piece','magasin','prix','magasinData','pieceData')
    def get_magasinData(self,obj):
        return Magasin.objects.filter(pk=obj.magasin_id).values('id', 'nom','gerant', 'dateCreation')[0]

    def get_pieceData(self,obj):
        return Piece.objects.filter(pk=obj.piece_id).values('id','designation','categorie')[0]

class CommandeFournisseurSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les commandes fournisseurs
    '''
    #gerants = RelatedGerantSerializer(read_only=True)
    #gerant_nom = serializers.ReadOnlyField(source="gerant.nom")
    gerantData = serializers.SerializerMethodField()
    fournisseurData = serializers.SerializerMethodField()

    class Meta:
        model= CommandeFournisseur
        fields = ('id', 'gerant', 'fournisseur','exercice',
                    'numCommande', 'dateCommande','gerantData','fournisseurData')

    def get_gerantData(self, obj):
        return User.objects.filter(pk=obj.gerant_id).values("id","username","first_name","last_name","email")

    def get_fournisseurData(self,obj):
        return Fournisseur.objects.filter(pk=obj.fournisseur_id).values()[0]
    




class LigneCommandeSerializer(serializers.ModelSerializer):
    '''
        Detail sur une commande fournisseur
    '''
    commandeData = serializers.SerializerMethodField()
    pieceData = serializers.SerializerMethodField()
    class Meta:
        model = LigneCommande
        fields= ('id','quantiteCommande','quantiteRecu','piece','commandeFournisseur','commandeData','pieceData')
    def get_commandeData(self, obj):
        return CommandeFournisseur.objects.filter(pk=obj.commandeFournisseur_id).values()[0]

    def get_pieceData(self,obj):
        return Piece.objects.filter(pk=obj.piece_id).values()[0]
    

class FactureSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les factures fournisseurs
    '''
    commandeData = serializers.SerializerMethodField()
    class Meta:
        model= Facture
        fields = ('id','numFacture','commandeFournisseur','commandeData')

    def get_commandeData(self, obj):
        return CommandeFournisseur.objects.filter(pk=obj.commandeFournisseur_id).values()[0]





class PaiementFournisseurSerializer(serializers.ModelSerializer):
    '''
        liste des informations sur un paiement
    '''
    factureData = serializers.SerializerMethodField()
    class Meta:
        model = PaiementFournisseur
        fields= ('id','facture','montantPaye','datePaiement','factureData')

    def get_factureData(self,obj):
        return Facture.objects.filter(pk=obj.facture_id).values()[0]
