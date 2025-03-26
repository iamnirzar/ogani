from django.db import models
from .models import*
from django.db.models import Sum
from ckeditor.fields import RichTextField
# Create your models here.

class Register(models.Model):
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.CharField(max_length=20)
    number = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.username
    
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    sizename = models.CharField(max_length=10)
    
    def __str__(self):
        return self.sizename
    

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
    Size = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True)
    description = RichTextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    image=models.ImageField(upload_to="image")
    name=models.CharField(max_length=100,blank=True,null=True)
    price = models.IntegerField(null=True, blank=True)
    qty=models.IntegerField(default=1)
    total_price=models.IntegerField(default=1)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    
    def total_cart_price():
        total = Cart.objects.aggregate(Sum('total_price'))['total_price__sum']
        return total

    def __str__(self):
        return self.name
    
class add_to_wishlist(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="image")
    name=models.CharField(max_length=100,blank=True,null=True)
    price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Billingdetails(models.Model):
    INDIAN_STATES = [
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
]
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    lname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField()
    phone=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=250,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    state=models.CharField(max_length=50,choices=INDIAN_STATES,blank=True,null=True)
    postcode=models.IntegerField(blank=True,null=True)
    # payment_mode=models.CharField(max_length=50,blank=True,null=True)
    # order_id=models.CharField(max_length=50,blank=True,null=True)
    # date=models.DateTimeField(auto_now_add=True)
    # status=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name
