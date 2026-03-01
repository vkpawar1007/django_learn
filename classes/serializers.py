from rest_framework import serializers
from .models import ClassRoom

class ClassRoomSearializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('id','name')
        

class AssignClassTeacherSearilizer(serializers.Serializer):
    class_teacher_id = serializers.IntegerField()


class ListClassSearialzer(ClassRoomSearializer):
    pass