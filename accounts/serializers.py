from rest_framework import serializers
from .models import User
from teachers.models import Teacher
from students.models import Student
from django.db import transaction

class UserCreateSearializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','email','password','role')

    @transaction.atomic
    def create(self,validate_data):
        passowrd = validate_data.pop('password')
        role = validate_data.get('role')


        # Create User
        user = User(**validate_data)
        user.set_password(passowrd)
        user.save()

        # Auto - Create profile Based on Role
        if role == 'TEACHER':
            Teacher.objects.create(user = user)
        elif role == 'STUDENT':
            Student.objects.create(
                user= user,
                roll_number = "NA",
                class_room = None
            )

        return user
    
class UserListSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','role')
        read_only_fields = fields

