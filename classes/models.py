from django.db import models


# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(
        "teachers.Teacher" , on_delete= models.SET_NULL , null= True , blank =True
    )

    def __str__(self):
        return self.name
    
