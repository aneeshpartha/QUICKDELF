from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    # Using default available field  of auth.user
    user = models.OneToOneField(User,on_delete='No')

    # Adding new fields to the user

    DOB = models.DateField (blank = True)
    gender = models.CharField(max_length=6)
    Cardnumber = models.BigIntegerField (blank = True)

    # Username will be returned when an new object is created
    def __str__(self):
        return self.user.username


# Hotel class. This class is for hotel fields. The class will contain all the information such as hotelname,hotelnumber,hoteladdress

class hotels(models.Model):

    hotelname = models.CharField(max_length=50 , blank=False,unique=True)
    hotelnumber = models.IntegerField()
    hoteladdress = models.CharField(max_length=100,blank=True)
    hotelimage = models.CharField(max_length=100, blank=True)


# Class Items. Class for storing items available in a particular restaurant. The class contains fields like itemname, itemprice, itemdescription, itemphoto and itemamount

class items(models.Model):
    hotel = models.ForeignKey(hotels,on_delete=models.CASCADE)
    itemname = models.CharField(max_length=50, blank=False)
    itemprice = models.FloatField
    itemdescription = models.CharField(max_length=200)
    itemphoto = models.CharField(max_length=200)
    itemamount = models.DecimalField(max_digits=5,decimal_places=2 , blank=False,default=0)

# class Cardvalidation . This class is used for validation user card information which will be used in payment field.

class cardvalidation(models.Model):
    cardname = models.CharField(max_length=50)
    cardnumber = models.IntegerField(default=0)
    cvv =  models.IntegerField(default=0)
