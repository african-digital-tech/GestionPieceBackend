
from email.policy import default
from venv import create
from django.db import models
from exercices.models import Exercice
from pieces.models import Piece
from django.contrib.auth.models import User
# Model du package gestion du stock


class Categorie(models.Model):
    intitule = models.CharField(max_length=50)
    dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', "intitule", "-dateCreation"]

    def __str__(self):
        return self.intitule


class Gerant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'nom', 'prenom', 'telephone', 'email']

    def __str__(self):
        return f'{self.nom} {self.prenom}'


class Fournisseur(models.Model):
    choiceList = [
        ('BF', "Burkina Faso"),
        ('GH', "Ghana"),
        ('CI', "Côte d'Ivoire"),
        ('CH', "Chine")]

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    pays = models.CharField(max_length=255, choices=choiceList)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'nom', 'prenom', 'telephone', 'pays']

    def __str__(self):
        return f'{self.nom} {self.prenom}'


class Magasin(models.Model):
    nom = models.CharField(max_length=255)
    gerant = models.ForeignKey(
        User, on_delete=models.SET_NULL,null=True)
    listPieceSortie = models.ManyToManyField(to=Piece, through='InfosSortie',
                                             through_fields=('magasin', 'piece'), related_name="magasinSortie")

    listPieceEntree = models.ManyToManyField(to=Piece, through='QuantitéStock',
                                             through_fields=('magasin', 'piece'), related_name="magasinEntree")

    dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'nom','gerant', '-dateCreation']

    def __str__(self):
        return f'{self.nom}'


class QuantitéStock(models.Model):
    piece = models.ForeignKey(
        Piece, on_delete=models.CASCADE, related_name='info_local')
    quantiteStockee = models.IntegerField(default=0)
    magasin = models.ForeignKey(
        Magasin, on_delete=models.SET_NULL, null=True, related_name="info_quantite")
    prix = models.FloatField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'piece', 'magasin', 'prix']

    def __str__(self):
        return f'{self.piece}'


class InfosSortie(models.Model):
    magasin = models.ForeignKey(
        Magasin, on_delete=models.CASCADE, related_name="info_sortie")
    piece = models.ForeignKey(
        Piece, on_delete=models.CASCADE, related_name='info_sortie')

    quantite = models.IntegerField(default=0)
    prixSortie = models.FloatField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'piece', 'magasin', 'quantite', 'prixSortie']

    def __str__(self):
        return f'{self.piece}'


class CommandeFournisseur(models.Model):
    gerant = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.CASCADE, related_name='liste_commande')
    numCommande = models.CharField(max_length=250, unique=True,null=True)
    dateCommande = models.DateTimeField(auto_now_add=True)
    exercice = models.ForeignKey(
        Exercice, on_delete=models.CASCADE, related_name="commande_fournisseur")
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'gerant', 'fournisseur','numCommande'
                , 'dateCommande']

    def __str__(self):
        return f'{self.numCommande}'


    
    
    def save(self,*args, **kwargs):
        num = CommandeFournisseur.objects.count() + 1
        self.numCommande = f'CFOM00000{ num}'
        super(CommandeFournisseur, self).save(*args, **kwargs)
        
class LigneCommande(models.Model):
    commandeFournisseur = models.ForeignKey(
        CommandeFournisseur, on_delete=models.CASCADE, related_name="info_ligneCommande")
    piece = models.ForeignKey(
        Piece, on_delete=models.CASCADE, related_name='info_ligneCommande')
    quantiteCommande = models.IntegerField(default=0)
    quantiteRecu = models.IntegerField(default=0)
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'commandeFournisseur',
                    'quantiteCommande', 'quantiteRecu']

    def __str__(self):
        return f'{self.commandeFournisseur}'


class Facture(models.Model):
    numFacture = models.CharField(max_length=12, unique=True,null=True)
    total = models.FloatField(default=0)
    commandeFournisseur = models.ForeignKey(
        CommandeFournisseur, on_delete=models.CASCADE, related_name='detail_facture')
    #dateCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'numFacture', 'total', 'commandeFournisseur']

    def __str__(self):
        return f'{self.numFacture}'

    def save(self,*args, **kwargs):
        num = Facture.objects.count() + 1
        self.numFacture = f'FC00000{ num}'
        super(Facture, self).save(*args, **kwargs)


class PaiementFournisseur(models.Model):
    facture = models.ForeignKey(
        Facture, on_delete=models.CASCADE, related_name='paiement')
    montantPaye = models.FloatField(default=0)
    datePaiement = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'montantPaye', 'facture','datePaiement']

    def __str__(self):
        return f'{self.facture}'
