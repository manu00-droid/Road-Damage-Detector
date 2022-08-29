
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.core.validators import FileExtensionValidator

class picture(models.Model):

    pic = models.ImageField(upload_to="userPics/",validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])
class zipFile(models.Model):
    zip=models.FileField(upload_to="userZip/",validators=[FileExtensionValidator( ['zip'] ) ])
class zipFile_csv(models.Model):
    zip=models.FileField(upload_to="userZip/",validators=[FileExtensionValidator( ['zip'] ) ])
    csv=models.FileField(upload_to="userZip/csv",validators=[FileExtensionValidator( ['csv','xlsx'] ) ])
    
    
    

class users(models.Model):
    first_Name=models.CharField(max_length=150)
    last_Name=models.CharField(max_length=150)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=150)
    type=models.CharField(max_length=150)

class Project(models.Model):
    p_id=models.CharField(primary_key=True,max_length=150)
    p_name=models.CharField(max_length=150)
    start_date=models.DateField(auto_now=True)

class Project_det(models.Model):
    humid = models.IntegerField()
    pH = models.IntegerField()
    temp=models.IntegerField()
    # start_time = models.TimeField()
    date_field = models.DateField(auto_now=True)
    road_len_const = models.IntegerField()
    p_name=models.CharField(max_length=150)
    p_id=models.IntegerField(default=0)
    p_no=models.IntegerField(default=0)

class LatLng(models.Model):
    lat=models.FloatField(default=2)
    lng=models.FloatField(default=2)
    date=models.DateField(auto_now=True)
    route=models.CharField(max_length=150,default=2)
    cityAdress=models.CharField(max_length=150,default=2)    
    stateAdress=models.CharField(max_length=150,default=2)    
    countryAdress=models.CharField(max_length=150,default=2)    
    postaladd=models.IntegerField(default=2)
    
