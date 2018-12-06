from django.db import models

# Create your models here.

class  student(models.Model):
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=20)
    roll = models.CharField(max_length=20,unique = True)
    dob = models.DateField(default='')
    email = models.EmailField(max_length = 40,unique = True)
    phone = models.CharField(max_length=20)
    branch = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    year = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
