from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    published = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to='pics/')
