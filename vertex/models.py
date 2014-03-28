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
    
    def get_followers(self): # a person => you
    	followers_list = []
    	for edge in Edge.objects.filter(vertex_head_id =self.user_id):
	    	followers_list += Vertex.objects.filter(user_id = edge.vertex_tail_id)
    	return followers_list
    	
    def get_following(self): # you => a person
    	followings_list = []
    	for edge in Edge.objects.filter(vertex_tail_id =self.user_id):
    		followings_list += Vertex.objects.filter(user_id = edge.vertex_head_id)
    	return followings_list
    
	def is_connected_to(self,vertex_id): # you => vertex_id ???
		if len(Edge.objects.filter(vertex_tail_id = self.user_id , vertex_head_id = vertex_id)) == 0:
			return False
		else:
			return True
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname+' '+self.lastname
        
class Edge(models.Model,object): 
	""" tail ==> head """
	vertex_head_id = models.CharField(max_length=100)
	vertex_tail_id = models.CharField(max_length=100)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.vertex_tail_id+' ==> '+self.vertex_head_id
	
# Create your models here. 

