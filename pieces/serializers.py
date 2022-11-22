
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
    read_only = True
    class Meta:
        model= Piece
        fields = ('id','designation')
        depth = 2