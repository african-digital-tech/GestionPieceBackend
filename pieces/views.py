from django.shortcuts import render
from rest_framework import  generics,permissions
from rest_framework.response import Response
import rest_framework.status as status

from pieces.models import Categorie, Piece
from pieces.serializers import CategorieSerializer, PieceSerializer
#### Piece
 
class PieceListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    paginator = None
liste_create_PieceAPIView = PieceListCreateAPIView.as_view()


class RetriveUpdateDelPiece(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_PieceAPIView = RetriveUpdateDelPiece.as_view()


#### Categorie
 
class CategorieListCreateAPIView(generics.ListCreateAPIView):
    '''
        get, post
    '''

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    paginator = None
liste_create_CategorieAPIView = CategorieListCreateAPIView.as_view()


class RetriveUpdateDelCategorie(generics.RetrieveUpdateDestroyAPIView):

    '''
        Cette classe permet de faire get update, delete
    '''

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_class = [permissions.IsAdminUser]

ret_update_CategorieAPIView = RetriveUpdateDelCategorie.as_view()

# Create your views here.
