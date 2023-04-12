from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers =models.ManyToManyField(User,related_name="followers",blank=True)
    followings =models.ManyToManyField(User,related_name="followings",blank=True)
    profile_picture = models.ImageField(upload_to= 'profilepics')
    

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Wallpaper = models.ImageField(upload_to='posts')
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(User,related_name="likes",blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    tags =TaggableManager()
    # comments = models.TextField(blank=True)
    # download = models.ManyToManyField(User,related_name="downloads")

