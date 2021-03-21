from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')




class Post(models.Model):
    title = models.CharField(max_length=300)    
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    title_tag = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts',  blank=True)
    snippet = models.CharField(max_length=255)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('home')


    def get_total_likes(self):
        return self.likes.count()

 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profile")
    instagram_url = models.CharField(max_length=300, blank=True)
    twitter_url = models.CharField(max_length=300, blank=True)
    facebook_url = models.CharField(max_length=300, blank=True) 
    website_url = models.CharField(max_length=300, blank=True)   


    def __str__(self):
        return str(self.user)

    
    def get_absolute_url(self):
        return reverse('home')



 