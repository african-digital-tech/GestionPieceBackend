from datetime import datetime
from email.policy import default
from secrets import choice
from django.db import models
#from exercice.models import Exercice

from pieces.models import Piece

# Model du package gestion du stock

class Gerant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)

    class Meta:
        ordering = ['id','nom','prenom']
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Fournisseur(models.Model):
    choiceList = [
        ('BF',"Burkina Faso"),
        ('GH',"Ghana"),
        ('CI',"Côte d'Ivoire"),
        ('CH',"Chine")]
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    pays = models.CharField(max_length=255,choices=choiceList)

    class Meta:
        ordering = ['id','nom','prenom']
    
    def __str__(self):
        return f'{self.nom} {self.prenom}' 


class Magasin(models.Model):
    nom = models.CharField(max_length=255)
    dateCreation = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['id','nom']
    
    def __str__(self):
        return f'{self.nom}'

class PieceStockée(models.Model):
    piece = models.ForeignKey(Piece,on_delete=models.CASCADE)
    quantiteStockee = models.IntegerField(default=0)

    class Meta:
        ordering = ['id','piece']
    
    def __str__(self):
        return f'{self.piece}'



class QuantitéStock(models.Model):

    piece = models.ForeignKey(Piece,on_delete=models.CASCADE)
    quantiteStockee = models.IntegerField(default=0)
    magasin = models.ForeignKey(Magasin,on_delete=models.CASCADE)
    prix = models.FloatField(default=0)
    class Meta:
        ordering = ['id','piece','magasin']
    
    def __str__(self):
        return f'{self.piece}'


class InfosSortie(models.Model):
    magasin = models.ForeignKey(Magasin,on_delete=models.CASCADE)
    piece = models.ForeignKey(PieceStockée,on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    prixSortie = models.FloatField(default=0)

    class Meta :
        ordering = ['id','piece']

    def __str__(self):
        return f'{self.piece}' 


class CommandeFournisseur(models.Model):
    gerant = models.ForeignKey(Gerant,on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    numCommande = models.CharField(max_length=250,unique=True)
    dateCommande = models.DateTimeField(default = datetime.now)
    #exercice = models.ForeignKey(Exercice,on_delete=models.CASCADE,default=1)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.numCommande}'

class LigneCommande(models.Model):
    commandeFournisseur = models.ForeignKey(CommandeFournisseur,on_delete=models.CASCADE)
    pieceStockée = models.ForeignKey(PieceStockée,on_delete=models.CASCADE)
    quantiteCommande = models.IntegerField(default=0)
    quantiteRecu = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.commandeFournisseur}'

class Facture(models.Model):
    numFacture = models.CharField(max_length=12,unique=True)
    total = models.FloatField(default=0)
    commandeFournisseur = models.ForeignKey(CommandeFournisseur,on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.numFacture}'


class PaiementFournisseur(models.Model):
    facture = models.ForeignKey(Facture,on_delete = models.CASCADE)
    montantPaye = models.FloatField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.facture}'