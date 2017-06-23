from django.db import models
from django.utils import timezone

import email

from unittest.util import _MAX_LENGTH

from cryptography.hazmat.primitives.ciphers.modes import Mode

# Create your models here.
class ProjectsCategory(models.Model):
    name = models.CharField(max_length=50)
    ancestor = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE)


#Надо разобраться как ссылатся на эту табличку в News    
#class Image(models.Model):
#    img_link = models.FilePathField()
#    img_description = models.CharField(max_length=250)

class Projects(models.Model):
    category = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    decription = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    video_preview = models.URLField(max_length=200)
    time_commitment = models.FloatField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    
class Institution(models.Model):
    title = models.CharField(max_length=250)
    decription = models.TextField()
    
class Authors(models.Model):
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254) 
    name = models.CharField(max_length=100)
    decription = models.TextField()
    
    
class AuthorsConnections(models.Model):
    id_author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    
#Надо разобраться как ссылатся на эту табличку в News      
#class Tags(models.Model):
#    name = models.CharField(max_length=50)
    
#Надо разобраться как ссылатся на эту табличку в News  
#class Connections(models.Model):
#    id_post = models.ForeignKey(Projects, on_delete=models.CASCADE)
#    id_tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    
    
    
    
    
    
    
    
    
    
    
    
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