from django.contrib import admin

from pieces.models import Categorie, Piece

# Register your models here.

class CategorieFilter(admin.ModelAdmin):
    list_display=('id','intitule')

class PieceFilter(admin.ModelAdmin):
    list_display=('id','designation','categorie')
    list_filter = ('categorie',)

admin.site.register(Categorie,CategorieFilter)
admin.site.register(Piece,PieceFilter)
