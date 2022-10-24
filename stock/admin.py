from django.contrib import admin
from pieces.models import Piece

from stock.models import CommandeFournisseur, Facture, Fournisseur, InfosSortie, LigneCommande, Magasin, Gerant, PaiementFournisseur, QuantitéStock

# Register your models here.

class GerantFilter(admin.ModelAdmin):
    list_display = ('id','nom','prenom','email','telephone')
    #list_filter = ('pays',)

admin.site.register(Gerant,GerantFilter)

class FournisseurFilter(admin.ModelAdmin):
    list_display = ('id','nom','prenom','telephone','pays')
    list_filter = ('pays',)

admin.site.register(Fournisseur,FournisseurFilter)


class MagasinFilter(admin.ModelAdmin):
    list_display = ('id','nom', 'dateCreation')
    list_filter = ('nom',)

admin.site.register(Magasin,MagasinFilter)



################################

class InfosSortieFilter(admin.ModelAdmin):
    list_display = ('id','magasin','piece','quantite','prixSortie')
    list_filter = ('magasin',)

admin.site.register(InfosSortie,InfosSortieFilter)

class QuantitéStockFilter(admin.ModelAdmin):
    list_display = ('id','magasin','piece','quantiteStockee','prix')
    list_filter = ('magasin',)

admin.site.register(QuantitéStock,QuantitéStockFilter)


class CommandeFournisseurFilter(admin.ModelAdmin):
    list_display = ('id','numCommande','fournisseur','dateCommande','gerant')
    list_filter = ('fournisseur',)

admin.site.register(CommandeFournisseur,CommandeFournisseurFilter)


class LigneCommandeFilter(admin.ModelAdmin):
    list_display = ('id','commandeFournisseur','piece','quantiteCommande','quantiteRecu')
    list_filter = ('commandeFournisseur',)

admin.site.register(LigneCommande,LigneCommandeFilter)



class FactureFilter(admin.ModelAdmin):
    list_display = ('id','numFacture','commandeFournisseur','total')
    #list_filter = ('piece',)

admin.site.register(Facture,FactureFilter)


class PaiementFournisseurFilter(admin.ModelAdmin):
    list_display = ('id','facture','montantPaye')
    #list_filter = ('piece',)

admin.site.register(PaiementFournisseur,PaiementFournisseurFilter)
