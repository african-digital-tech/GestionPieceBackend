from django.contrib.admin   import ModelAdmin

class ClientFilter( ModelAdmin):
    list_display = (
        "id", "nom_client",  "prenom_client",
        "telephone_client", "estBonClient","date_creation"
        )
    
    list_filter = ("estBonClient",)
    
class CommandClientFilter( ModelAdmin):
    list_display = ("id","numCommande" ,"vendeur","client","totalCommande","date_creation")

class InfosCommandeClientFilter( ModelAdmin):
    list_display = ("id","commande" ,"piece","quantite","prix_unitaire","date_creation")
    
class FactureClientFilter( ModelAdmin):
    list_display = ("id","numFacture","commande" ,"date_creation")

class PaiementFilter( ModelAdmin):
    list_display = ("id","facture","montant","date_creation")
    
class AgentCommercialFilter( ModelAdmin):
    list_display = ("id", "nom_agent", "prenom_agent",
                    "email_agent","magasin",
                    "telephone_agent" ,"date_creation")
    
    list_filter  = ("magasin",)