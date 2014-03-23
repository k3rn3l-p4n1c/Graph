from django.db import models
import datetime
from django.utils import timezone

class Vertex(models.Model,object):
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    sex = models.BooleanField() # 1 for male  // 0 for female
    birthdate = models.DateField()
    reg_date = models.DateTimeField('date published')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name    
# Create your models here. 

