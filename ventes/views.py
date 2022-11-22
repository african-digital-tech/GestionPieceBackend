from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ClientListAPIView(generics.ListCreateAPIView):
    """
        GET && POST client
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

create_list_clientAPIView = ClientListAPIView.as_view()

class ClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH client
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
upd_Del_Retr_clientAPIView = ClientDetailAPIView.as_view()

class CommandClientListAPIView(generics.ListCreateAPIView):
    """
        GET && POST commande client
    """
    queryset = CommandClient.objects.all()
    serializer_class = CommandClientSerializer

create_list_commandClientAPIView = CommandClientListAPIView.as_view()

class CommandClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH commande client
    """
    queryset = CommandClient.objects.all()
    serializer_class = CommandClientSerializer

upd_Del_Retr_commandClientAPIView= CommandClientDetailAPIView.as_view()

class FactureClientListAPIView(generics.ListCreateAPIView):
    """
        GET && POST facture client
    """
    queryset = FactureClient.objects.all()
    serializer_class = FactureClientSerializer

create_list_factureClientAPIView = FactureClientListAPIView.as_view()

class FactureClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH facture client
    """
    queryset = FactureClient.objects.all()
    serializer_class = FactureClientSerializer

upd_Del_Retr_factureClientAPIView = FactureClientDetailAPIView.as_view()

class AgentCommercialListAPIView(generics.ListCreateAPIView):
    """
        GET && POST agent commercial
    """
    queryset = AgentCommercial.objects.all()
    serializer_class = AgentCommercialSerializer

create_list_agentCommercialAPIView = AgentCommercialListAPIView.as_view()

class AgentCommercialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH agent commercial
    """
    queryset = AgentCommercial.objects.all()
    serializer_class = AgentCommercialSerializer

upd_Del_Retr_agentCommercialAPIView = AgentCommercialDetailAPIView.as_view()

class InfosCommandeClientListAPIView(generics.ListCreateAPIView):
    """ 
        GET && POST info commande client
    """
    queryset = InfosCommandeClient.objects.all()
    serializer_class = ClientSerializer

create_list_infosCommandeClientAPIView = InfosCommandeClientListAPIView.as_view()

class InfosCommandeClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH info commandee client
    """
    queryset = InfosCommandeClient.objects.all()
    serializer_class = InfosCommandeClientSerializer

upd_Del_Retr_infosCommandeClientAPIView = InfosCommandeClientDetailAPIView.as_view()

class PaiementListAPIView(generics.ListCreateAPIView):
    """
        GET && POST paiement client
    """
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

create_list_paiementAPIView = PaiementListAPIView.as_view()

class PaiementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        DELETE, UPDATE, RETRIEVE && PATH paiement client
    """
    queryset = Paiement.objects.all()
    serializer_class = ClientSerializer

upd_Del_Retr_paiementAPIView = PaiementDetailAPIView.as_view()
