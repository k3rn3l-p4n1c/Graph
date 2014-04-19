from django.db import models
import datetime
from django.utils import timezone
import json

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
    def age(self):
    	return datetime.datetime.now().year - self.birthdate.year
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname+' '+self.lastname
        
class Edge(models.Model,object): 
	""" tail ==> head """
	vertex_head_id = models.CharField(max_length=100)
	vertex_tail_id = models.CharField(max_length=100)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.vertex_tail_id+' ==> '+self.vertex_head_id
    
class Flow(models.Model):
	
	vertexes = models.ManyToManyField(Vertex)
	text = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published')
	owner = models.CharField(max_length=100) 
	last_forward_date = models.DateTimeField('date published')
	history = models.TextField(null=True)
	likes = models.IntegerField()
	likers = models.TextField(null=True)
	def get_date(self):
		return str(self.pub_date.date())
	def set_history(self,to_vertex):
		jsonDec = json.decoder.JSONDecoder()
		try:
			history_list = jsonDec.decode(self.history)
			history_list.append(to_vertex)
		except TypeError:
			history_list=list(to_vertex)
			self.history = json.dumps(history_list)
		self.save()
	def get_history(self):
		jsonDec = json.decoder.JSONDecoder()
		try:
			history_list = jsonDec.decode(self.history)
		except TypeError:
			history_list = list()
			return history_list
	def like(self,user_id): 
		jsonDec = json.decoder.JSONDecoder()
		try:
			likers_list = jsonDec.decode(self.likers)
			if user_id in likers_list:
				likers_list.remove(user_id)
				self.likes -= 1
			else:
				likers_list.append(user_id)
				self.likes += 1
			self.likers = json.dumps(likers_list)
			self.save()
		except TypeError:
			likers_list = [user_id]
			self.likes += 1
		self.likers = json.dumps(likers_list)
		self.save()
	def __unicode__(self):
		return self.text
class Comment(models.Model):
	flows = models.ManyToManyField(Flow)
	text = models.CharField(max_length=400)
	pub_date = models.DateTimeField('date published')
	owner = models.CharField(max_length=100) 
	
# Create your models here. 

