from django.db import models

# Create your models here.
class Hotel(models.Model):
    Image=models.ImageField(upload_to="Room Images",null=True,blank=True)
    Category=models.CharField(max_length=1800,null=True,blank=True)
    Description=models.CharField(max_length=1500,null=True,blank=True)
    Price_Range=models.CharField(null=True,blank=True,max_length=1000)


class Hotel_staff(models.Model):
    Person_Name=models.CharField(max_length=500,null=True,blank=True)
    Designation=models.CharField(max_length=500,null=True,blank=True)
    Person_Image=models.ImageField(upload_to="Team Members",null=True,blank=True)

class Features(models.Model):
    Category_name=models.CharField(max_length=6000,null=True,blank=True)
    Amount=models.IntegerField(null=True,blank=True)
    Information=models.CharField(max_length=6000,null=True,blank=True)
    Product=models.CharField(max_length=6000,null=True,blank=True)
    Image=models.ImageField(upload_to="Hotel Features",null=True,blank=True)


class Amenities(models.Model):
    Amenities_name=models.CharField(max_length=900,null=True,blank=True)
    Amenities_des=models.CharField(max_length=500,null=True,blank=True)
    Amenities_des=models.CharField(max_length=1500,null=True,blank=True)
    Amenities_image=models.ImageField(upload_to="Amenties",null=True,blank=True)



class Advanced_Category(models.Model):
    Image1=models.ImageField(upload_to="Rooms",null=True,blank=True)
    Image2=models.ImageField(upload_to="Rooms",null=True,blank=True)
    Image3=models.ImageField(upload_to="Rooms",null=True,blank=True)
    Name=models.CharField(max_length=500,null=True,blank=True)
    Description=models.CharField(max_length=600,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Product = models.CharField(max_length=6000, null=True, blank=True)



##############################################################################
##############################################################################

class Room(models.Model):
    Room_Num=models.AutoField(primary_key=True)
    Room_Type=models.CharField(max_length=500,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Category=models.CharField(max_length=500,null=True,blank=True)
    Room_Image=models.ImageField(upload_to="Frontend Availability Table",null=True,blank=True)


class Food_And_Beverages(models.Model):
    Item_Id=models.AutoField(primary_key=True)
    Item_Type=models.CharField(max_length=100,null=True,blank=True)
    Item_Name=models.CharField(max_length=100,null=True,blank=True)
    Item_Price=models.IntegerField(null=True,blank=True)
    Item_Image=models.ImageField(upload_to="Frontend Beverages Section",null=True,blank=True)