from django.db import models

# Create your models here.
class HealthBlog(models.Model):
	title = models.CharField(max_length=100,default='title')
	image = models.FileField(blank=False)#field is amust require
	description = models.TextField(blank=False)#every product will need adescription
	Author = models.CharField(max_length=22,blank=False,default='author_blog')#since we need the time 
	created_at = models.DateTimeField(auto_now_add=True)#since we need the time 

	class Meta:
		ordering = ["-created_at"]


	def __str__(self):
		return self.title
	#of queries	