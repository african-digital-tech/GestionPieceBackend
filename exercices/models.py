
from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null

# Create your models here.

class Exercice(models.Model):
    debut       = models.DateField(unique=True)
    fin         = models.DateField(unique=True,blank=True,null=True)
    initiateur  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    etat        = models.BooleanField(default=False)
    class Meta :
        ordering = ['-debut', '-fin', 'initiateur']
    
    def __str__(self):
        return "{} - {}".format(self.debut, self.fin)
