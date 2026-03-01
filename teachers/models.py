from django.db import models
from accounts.models import User


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    subjects = models.ManyToManyField("subjects.Subject")
    classes = models.ManyToManyField("classes.ClassRoom")

    def __str__(self):
        return self.user.username
