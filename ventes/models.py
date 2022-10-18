from django.db import models
from django.contrib.auth.models import User

from stock.models import Magasin, PieceStockée
# Create your models here.

class Client(models.Model):
    """
        Entité Client
    """
    nom_client       = models.CharField(max_length=100) 
    prenom_client    = models.CharField(max_length=100)
    telephone_client = models.CharField(max_length=10)
    estBonClient     = models.BooleanField(default=False)
    date_creation    = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_creation', 'nom_client','prenom_client']
        constraints = [
            models.constraints.UniqueConstraint(fields=('nom_client','prenom_client', 'telephone_client'), 
                                                name="Unique_client_constraint")
            ]
    
    def  __str__(self):
        return f"{self.nom_client} {self.prenom_client}"
    
class AgentCommercial(models.Model):
    """
        Entité Agents Commercial
    """
    nom_agent       = models.CharField(max_length=100) 
    prenom_agent    = models.CharField(max_length=100)
    telephone_agent = models.CharField(max_length=10)
    email_agent     = models.EmailField(unique=True)
    date_creation   = models.DateTimeField(auto_now_add=True)
    magasin         = models.ForeignKey(Magasin, on_delete=models.CASCADE, related_name='agent')
    
    class Meta:
        ordering = ['-date_creation', 'nom_agent', 'prenom_agent', 'email_agent']
        
    def  __str__(self):
        return f"{self.nom_agent} {self.prenom_agent}"

class CommandClient(models.Model):
    """
        Entite Commande Client
    """
    numCommande      = models.CharField(max_length=100, unique=True) # gene un iterateur numeriq + CMCN
    totalCommande    = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_creation    = models.DateTimeField(auto_now_add=True)
    client           = models.ForeignKey(to=Client, on_delete=models.CASCADE,related_name='list_commande')
    vendeur          = models.ForeignKey(to=AgentCommercial, on_delete=models.CASCADE,related_name='list_commande')
    pieceVendue      = models.ManyToManyField(to=PieceStockée, through='InfosCommandeClient', through_fields=('commande','piece'))
    class Meta:
        ordering = ['-date_creation', 'numCommande', 'totalCommande']

    def __str__(self):
        return self.numCommande
    
class FactureClient(models.Model):
    numFacture       = models.CharField(max_length=100, unique=True) # gene un iterateur numeriq + CMCN
    date_creation    = models.DateTimeField(auto_now_add=True)
    commande         = models.ForeignKey(to=CommandClient, on_delete=models.CASCADE,related_name='facture')
    class Meta:
        ordering = ['-date_creation', 'numFacture']

    def __str__(self):
        return self.numFacture

class Paiement(models.Model):
    """
        Entite Paiement
    """
    montant        = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_creation  = models.DateTimeField(auto_now_add=True)
    facture        = models.ForeignKey(to=FactureClient, on_delete=models.CASCADE, related_name='paiement')
    class Meta:
        ordering   = ['-date_creation', 'montant']

    def __str__(self):
        return f"{self.date_creation}"
    
class InfosCommandeClient(models.Model):
    """
        Entite info sur les commandes Clients
    """
    commande       = models.ForeignKey(to=CommandClient, on_delete=models.CASCADE, related_name='infosCommande')
    piece          = models.ForeignKey(to=PieceStockée, on_delete=models.CASCADE, related_name='infosCommande')
    quantite       = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    prix_unitaire  = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    date_creation  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering   = ['-date_creation', 'quantite', 'prix_unitaire']
    
    def __str__(self):
        return f"{self.date_creation}"