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
    liste_create_CategorieAPIView,
    liste_create_PieceAPIView,
    ret_update_CategorieAPIView,
    ret_update_PieceAPIView
)

urlpatterns = [

    # URL : Pieces

    path('listePiece/',liste_create_PieceAPIView,name='listeCreerPiece'),
    path('listePiece/<int:pk>/detail',ret_update_PieceAPIView,name='retUpdatePiece'),

     # URL : fournisseurs

    path('listeCategorie/',liste_create_CategorieAPIView,name='listeCreerCategorie'),
    path('listeCategorie/<int:pk>/detail',ret_update_CategorieAPIView,name='retUpdateCategorie'),

     
]
