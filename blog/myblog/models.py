from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')




class Post(models.Model):
    title = models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE, default="admin")
    body = models.TextField()
    title_tag = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='coding')



    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('article-detail', args=str(self.pk))

    

