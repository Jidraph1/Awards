from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
from tinymce.models import HTMLField



# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    username = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.user 
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'profile-user')
    title = models.CharField(max_length=100)

