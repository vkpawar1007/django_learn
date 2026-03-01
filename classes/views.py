from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ClassRoomSearializer , AssignClassTeacherSearilizer , ListClassSearialzer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ClassRoom
from teachers.models import Teacher

class CreateClassRoomAPIView(APIView):
    
    def post(self, request):
        searialzer = ClassRoomSearializer(data = request.data)
        if searialzer.is_valid():
            classroom = searialzer.save()
            return Response(
                {
                    "message":"Class created",
                    'id':classroom.id
                },
                status= status.HTTP_201_CREATED
            )
        
        return Response(searialzer.errors , status=status.HTTP_400_BAD_REQUEST)
    

class AssignClassTeacherAPIView(APIView):

    def post(self, request,class_id):
        serializer = AssignClassTeacherSearilizer(data =request.data)
        if serializer.is_valid():
            classroom = get_object_or_404(ClassRoom,id=class_id)

            teacher = get_object_or_404(
                    Teacher,
                    id = serializer.validated_data['class_teacher_id']
            )

            classroom.class_teacher = teacher

            classroom.save()

            return Response({"message": "Class teacher assigned"})
        return Response(serializer.errors, status=400)
    

class listClassAPIVIew(APIView):
    def get(self ,request):
        
        classroom = ClassRoom.objects.all().order_by('id')
        serialzer = ListClassSearialzer(classroom,many=True)
        return Response(serialzer.data)