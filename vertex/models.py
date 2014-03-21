from django.db import models
import datetime
from django.utils import timezone

class Vertex(models.Model):
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
        
# Create your models here.
