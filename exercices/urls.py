from django.urls import include, path
from .views import (
    create_list_ExerciceAPIView, upd_Del_Retr_ExerciceAPIView
)

urlpatterns = [
    path("exercice/",create_list_ExerciceAPIView , name='listCreateExercice'),
    path("exercice/<int:pk>/",upd_Del_Retr_ExerciceAPIView , name='updDelRetrExercice'),
]