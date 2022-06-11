from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CLoudinaryField 



# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile_picture = CLoudinaryField('image')
    bio = models.CharField(max_length=250)
    email = models.EmailField(max_length=60)
    phone_number = models.IntegerField(blank = True)
    username = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user

