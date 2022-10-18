
from django.db import models
from exercices.models import Exercice

# Model du package gestion du stock

class Categorie(models.Model):
    intitule = models.CharField(max_length=50)
    dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id',"intitule", "-dateCreation"]

    def __str__(self):
        return self.intitule
    
class Gerant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    #dateCreation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id','nom','prenom', 'telephone', 'email']
    
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
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id','nom','prenom', 'telephone', 'pays']
    
    def __str__(self):
        return f'{self.nom} {self.prenom}' 
class PieceStockée(models.Model):
    designation = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name="pieces")
    quantiteStockee = models.IntegerField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id','designation','quantiteStockee', 'categorie' ]
    
    def __str__(self):
        return f'{self.designation}'
    
class Magasin(models.Model):
    nom = models.CharField(max_length=255)
    listPieceSortie = models.ManyToManyField(to=PieceStockée,through='InfosSortie', 
                                            through_fields=('magasin','piece'), related_name="magasinSortie")
    
    listPieceEntree = models.ManyToManyField(to=PieceStockée,through='QuantitéStock',
                                            through_fields=('magasin','piece'),related_name="magasinEntree")
    
    dateCreation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id','nom', '-dateCreation']
    
    def __str__(self):
        return f'{self.nom}'


class QuantitéStock(models.Model):
    piece = models.ForeignKey(PieceStockée,on_delete=models.CASCADE, related_name='info_local')
    quantiteStockee = models.IntegerField(default=0)
    magasin = models.ForeignKey(Magasin,on_delete=models.CASCADE, related_name="info_quantite")
    prix = models.FloatField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id','piece','magasin', 'prix']
    
    def __str__(self):
        return f'{self.piece}'


class InfosSortie(models.Model):
    magasin = models.ForeignKey(Magasin,on_delete=models.CASCADE, related_name="info_sortie")
    piece = models.ForeignKey(PieceStockée,on_delete=models.CASCADE, related_name='info_sortie')
    
    quantite = models.IntegerField(default=0)
    prixSortie = models.FloatField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['id','piece', 'magasin', 'quantite', 'prixSortie']

    def __str__(self):
        return f'{self.piece}' 


class CommandeFournisseur(models.Model):
    gerant = models.ForeignKey(Gerant,on_delete=models.CASCADE, related_name='liste_commande')
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE, related_name='liste_commande')
    numCommande = models.CharField(max_length=250,unique=True)
    dateCommande = models.DateTimeField(auto_now_add=True)
    exercice = models.ForeignKey(Exercice,on_delete=models.CASCADE, related_name="commande_fournisseur")
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id','gerant', 'fournisseur', 'numCommande', 'dateCommande']

    def __str__(self):
        return f'{self.numCommande}'

class LigneCommande(models.Model):
    commandeFournisseur = models.ForeignKey(CommandeFournisseur,on_delete=models.CASCADE, related_name="info_ligneCommande")
    pieceStockée = models.ForeignKey(PieceStockée,on_delete=models.CASCADE, related_name='info_ligneCommande')
    quantiteCommande = models.IntegerField(default=0)
    quantiteRecu = models.IntegerField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id','commandeFournisseur', 'quantiteCommande', 'quantiteRecu']

    def __str__(self):
        return f'{self.commandeFournisseur}'

class Facture(models.Model):
    numFacture = models.CharField(max_length=12,unique=True)
    total = models.FloatField(default=0)
    commandeFournisseur = models.ForeignKey(CommandeFournisseur,on_delete=models.CASCADE, related_name='detail_facture')
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'numFacture', 'total', 'commandeFournisseur']

    def __str__(self):
        return f'{self.numFacture}'


class PaiementFournisseur(models.Model):
    facture = models.ForeignKey(Facture,on_delete = models.CASCADE, related_name='paiement')
    montantPaye = models.FloatField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'montantPaye', 'facture']

    def __str__(self):
        return f'{self.facture}'