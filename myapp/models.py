from django.db import models
from .models import*
# Create your models here.

class User(models.Model):
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    confirmpassword = models.CharField(max_length=8)

    def __str__(self):
        return self.username
    
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    colorname = models.CharField(max_length=20)

    def __str__(self):
        return self.colorname

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image= models.ImageField(upload_to="image")
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    Color = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.name
    
