
from rest_framework import generics
from .serializers import *
from .models import *

class ExerciceListAPIView(generics.ListCreateAPIView):
    """
    """
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer

create_list_ExerciceAPIView = ExerciceListAPIView.as_view()

class ExerciceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer
    
upd_Del_Retr_ExerciceAPIView = ExerciceDetailAPIView.as_view()
