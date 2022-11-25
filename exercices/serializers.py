from rest_framework import serializers

from stock.models import Gerant
from .models import (Exercice)
from django.contrib.auth.models import User

class ExerciceSerializer(serializers.ModelSerializer):
    """
        Serializer pour les Exercices
    """
    gerant = serializers.SerializerMethodField()
    class Meta:
        model = Exercice
        fields= ('id','debut','fin','etat','gerant')

    def get_gerant(self,obj):
        return User.objects.filter(pk=obj.initiateur_id).values("id","username","first_name","last_name","email")[0]


