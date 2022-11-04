from django.urls import include, path
from .views import (
    create_list_ExerciceAPIView, upd_Del_Retr_ExerciceAPIView
)

urlpatterns = [
    path("", create_list_ExerciceAPIView, name='listCreateExercice'),
    path("<int:pk>/detail", upd_Del_Retr_ExerciceAPIView,
         name='updDelRetrExercice'),
]
