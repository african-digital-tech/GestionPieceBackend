from rest_framework import serializers
from .models import (
    Client, CommandClient, Paiement, FactureClient, 
    AgentCommercial, InfosCommandeClient
    )

class ClientSerializer(serializers.ModelSerializer):
    """
        Serializer pour les clients
    """
    class Meta:
        model = Client
        fields= '__all__'

class CommandClientSerializer(serializers.ModelSerializer):
    """
        Serializer pour les commandes des clients
    """
    class Meta:
        model = CommandClient
        fields= '__all__'


class PaiementSerializer(serializers.ModelSerializer):
    """
        Serializer pour les paiements clients
    """
    
    class Meta:
        model = Paiement
        fields= '__all__'

class FactureClientSerializer(serializers.ModelSerializer):
    """
        Serializer pour les factures clients
    """
    class Meta:
        model = FactureClient
        fields= '__all__'

class AgentCommercialSerializer(serializers.ModelSerializer):
    """
        Serializer pour les agents commercials
    """
    class Meta:
        model = AgentCommercial
        fields= '__all__'

class InfosCommandeClientSerializer(serializers.ModelSerializer):
    """
        Serializer pour les info sur les commandes clients
    """
    class Meta:
        model = AgentCommercial
        fields= '__all__'
