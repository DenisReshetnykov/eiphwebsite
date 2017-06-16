from django.db import models
from django.utils import timezone

import email

from unittest.util import _MAX_LENGTH

from cryptography.hazmat.primitives.ciphers.modes import Mode

# Create your models here.
class Image(models.Model):
    img_link = models.FilePathField()
    img_description = models.CharField(max_length=250)
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    
class Users(models.Model):
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE)
    email = models.CharField(max_length=250) #Надо добавить валидатор
    name = models.CharField(max_length=100)
    
class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    content = models.TextField()
    time = models.TimeField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    is_visible = models.BooleanField()
    
class Connections(models.Model):
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    id_tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    
class Comments(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.TimeField()
    
#class Spam(models.Model):
#    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
#    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
#    is_spam = models.BooleanField()
    
class Rate(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    rating = models.IntegerField()
    