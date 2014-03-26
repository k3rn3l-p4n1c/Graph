from django.db import models
import datetime
from django.utils import timezone

class Vertex(models.Model,object):
    password = models.CharField(max_length=50)
    user_id = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    sex = models.BooleanField() # 1 for male  // 0 for female
    birthdate = models.DateField()
    reg_date = models.DateTimeField('date published')
    #statues = models.CharField(max_length=30)
    #varificationCode = models.models.CharField(max_length=50)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname+' '+self.lastname
# Create your models here. 

