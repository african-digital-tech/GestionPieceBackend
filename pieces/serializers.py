
from attr import field
from rest_framework import  serializers
from pieces.models import Categorie, Piece


class CategorieSerializer(serializers.ModelSerializer):
    '''
        liste des categories de pieces
    '''

    class Meta:
        model = Categorie
        fields= '__all__'


class PieceSerializer(serializers.ModelSerializer):
    '''
        Liste de toutes les pièces
    '''

    class Meta:
        model= Piece
        field = '__all__'