from rest_framework import serializers

class RelatedGerantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(read_only=True)
    prenom = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
