
from django.urls import path
from .views import (
    create_list_agentCommercialAPIView, create_list_clientAPIView,
    create_list_commandClientAPIView, create_list_factureClientAPIView,
    create_list_infosCommandeClientAPIView, create_list_paiementAPIView,
    upd_Del_Retr_agentCommercialAPIView, upd_Del_Retr_clientAPIView, 
    upd_Del_Retr_commandClientAPIView, upd_Del_Retr_factureClientAPIView,
    upd_Del_Retr_infosCommandeClientAPIView, upd_Del_Retr_paiementAPIView
)

# Urls de l'api
urlpatterns = [
    #client
    path('client/',create_list_clientAPIView,name="listCreateClient"),
    path('client/detail/<int:pk>',upd_Del_Retr_clientAPIView,name="updDelRetr"),
    
    #  Agent commercial
    path('agentCommercial/',create_list_agentCommercialAPIView,name="listCreateAgent"),
    path('agentCommercial/detail/<int:pk>',upd_Del_Retr_agentCommercialAPIView,name="updDelRetr"),
    
    #Commande client
    path('commandClient/',create_list_commandClientAPIView,name="listCreateCommandClient"),
    path('commandClient/detail/<int:pk>',upd_Del_Retr_commandClientAPIView,name="updDelRetrcommandClient"),
    
    #Facture client
    path('factureClient/detail/<int:pk>',upd_Del_Retr_factureClientAPIView,name="updDelRetrfactureClient"),
    path('factureClient/',create_list_factureClientAPIView,name="listCreate"),
    
    #infos commande client
    path('infosCommandeClient/detail/<int:pk>',upd_Del_Retr_infosCommandeClientAPIView,name="updDelRetrinfosCommandeClient"),
    path('infosCommandeClient/',create_list_infosCommandeClientAPIView,name="listCreateinfosCommandeClient"),
    
    #paiement client
    path('paiement/detail/<int:pk>',upd_Del_Retr_paiementAPIView,name="updDelRetrpaiement"),
    path('paiement/',create_list_paiementAPIView,name="listCreatepaiement"),
    
]
