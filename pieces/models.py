from django.db import models

# Create your models here.

class Categorie(models.Model):
    intitule = models.CharField(max_length=50)

    class Meta:
        ordering = ['id',"intitule"]

    def __str__(self):
        return self.intitule

class Piece(models.Model):
    designation = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    class Meta:
        ordering = ['id','designation']

    def __str__(self):
        
        return f'{self.designation} {self.categorie}'
