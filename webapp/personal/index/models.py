from django.db import models

from datetime import date
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    read_on=models.DateField('Date Read On',null=True)
    review=models.TextField(blank=True,null=True)
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    about=models.TextField(null=True)
    topic=models.CharField(max_length=200)
    written_on=models.DateField('Written On',default=date.today,null=True )
    content=models.FileField(upload_to='articles/')
class Skill(models.Model):
    name =models.CharField(max_length=100)
class Interest(models.Model):
    interest=models.CharField(max_length=100)
    image= models.ImageField(upload_to="images/interest/")
class Project(models.Model):
    name=models.CharField(max_length=200)
    url=models.URLField(null=True,blank = True)
    desc=models.TextField(null=True)
    report=models.URLField(null=True,blank=True)
    image=models.ImageField(upload_to="images/projects/",null=True, blank=True)
    type=models.CharField(max_length=100)
    done_on=models.DateField('Done On',default=date.today )

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number = models.CharField(max_length=12)
    message=models.TextField()
