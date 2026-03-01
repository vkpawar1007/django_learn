from django.urls import path
from .views import CreateClassRoomAPIView , AssignClassTeacherAPIView ,listClassAPIVIew


urlpatterns = [
    path('classes/create/',CreateClassRoomAPIView.as_view()) , 

    path('classes/<int:class_id>/assign-teacher/' ,AssignClassTeacherAPIView.as_view()),

    path('classes/' , listClassAPIVIew.as_view()),
]