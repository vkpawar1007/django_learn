from django.db import models
from accounts.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=50)
    class_room = models.ForeignKey('classes.ClassRoom',
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)


    def __str__(self):
        return self.user.username