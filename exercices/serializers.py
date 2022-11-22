from rest_framework import serializers
from .models import (Exercice)

class ExerciceSerializer(serializers.ModelSerializer):
    """
        Serializer pour les Exercices
    """
    class Meta:
        model = Exercice
        fields= '__all__'


