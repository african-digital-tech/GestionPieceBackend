from django.contrib   import admin
from .models import *
from .AdminConfig import *

# Register your models here.
admin.site.register(Client, ClientFilter)
admin.site.register(CommandClient, CommandClientFilter)
admin.site.register(InfosCommandeClient, InfosCommandeClientFilter)
admin.site.register(Paiement, PaiementFilter)
admin.site.register(FactureClient,FactureClientFilter)
admin.site.register(AgentCommercial, AgentCommercialFilter)


