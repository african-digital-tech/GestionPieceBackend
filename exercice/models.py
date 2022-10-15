from email.policy import default
from enum import unique
from django.db import models
from psycopg2 import Date

# Create your models here.

class Exercice(models.Model):
    debut = models.DateField(unique=True)
    fin = models.DateField(unique=True)
