from django.db import models
from django.utils import timezone
import datetime

class Vertex(models.Model,object):
    password = models.CharField(max_length=50)
    user_id = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    sex = models.BooleanField(default = 1) # 1 for male  // 0 for female
    birthdate = models.DateField()
    reg_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname+' '+self.lastname

class Friends(models.Model):
    name = models.CharField(max_length = 200)
    members = models.ManyToManyField(Vertex,through = 'Edge')
    def __unicode__(self):
        return self.name
class Edge(models.Model):
    vertex = models.ForeignKey(Vertex)
    group = models.ForeignKey(Friends)
    


class Flow(models.Model): 
    vertexes = models.ManyToManyField(Vertex)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.text
    
# Create your models here. 

