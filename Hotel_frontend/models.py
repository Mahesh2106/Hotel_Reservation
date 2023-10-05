from django.db import models
import datetime
from Hotel_admin.models import Room
from django.utils import timezone

# Create your models here.
class Registration(models.Model):
    Customer_id=models.AutoField(primary_key=True)
    Customer_Name=models.CharField(max_length=60,null=True,blank=True)
    Proof_Type=models.CharField(max_length=40,null=True,blank=True)
    Proof_Id=models.CharField(null=True,blank=True,max_length=100)
    Proof_Image=models.ImageField(upload_to="Customer Registration",null=True,blank=True)
    Username=models.CharField(max_length=600,null=True,blank=True)
    Password=models.CharField(unique=True,null=True,blank=True,max_length=100)
    Email=models.EmailField(max_length=400,null=True,blank=True)
    Address=models.CharField(max_length=900,null=True,blank=True)
    Address1=models.CharField(max_length=900,null=True,blank=True)
    Phone_number=models.CharField(max_length=11,null=True,blank=True)
    State=models.CharField(max_length=1550,null=True,blank=True)
    Country=models.CharField(max_length=1550,null=True,blank=True)
    Messages=models.CharField(max_length=11000,null=True,blank=True)

######### Room Booking Details ############

class Booking(models.Model):
    Booking_ID=models.AutoField(primary_key=True)
    Booking_Date=models.DateField(default=datetime.datetime.today())
    Check_in=models.DateField()
    Check_in_Time=models.TimeField(auto_now_add=True, blank=True, null=True, verbose_name="In Time")
    Check_Out_Time=models.TimeField(blank=True, null=True, verbose_name="Out Time")
    Check_out=models.DateField()
    Total_Price=models.IntegerField(null=True,blank=True)
    Room_Num=models.ForeignKey(Room,db_index=True,on_delete=models.CASCADE,to_field='Room_Num')
    Cust_ID=models.ForeignKey(Registration,db_index=True,on_delete=models.CASCADE,to_field='Customer_id')
    Email=models.EmailField(max_length=5000,null=True,blank=True)



###########################################


class Newsletter(models.Model):
    Email=models.EmailField(max_length=600,null=True,blank=True,unique=True)

###############################


class Rating(models.Model):
    username=models.CharField(null=True,blank=True,max_length=900)
    rating=models.IntegerField(null=True,blank=True,default=0)
    Description=models.CharField(max_length=5000,null=True,blank=True)

#################################
class PaymentDB(models.Model):
    Customer_ID = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    CardHolder_Name=models.CharField(null=True,blank=True,max_length=900)
    Card_Num=models.CharField(null=True,blank=True,max_length=50)
    Amount=models.CharField(null=True,blank=True,max_length=900)
    Expiry_Date=models.CharField(null=True,blank=True,max_length=50)
    CVV=models.CharField(null=True,blank=True,max_length=10)



class Contact_DB(models.Model):
    Messages=models.CharField(max_length=6000,null=True,blank=True)
    Name_User=models.CharField(max_length=90,null=True,blank=True)
    Email=models.EmailField(max_length=90,null=True,blank=True)
    PhoneNumber=models.CharField(max_length=50,null=True,blank=True)