from django.db import models

# Create your models here.

class FamilyMethod(models.Model):
	method_name = models.CharField(max_length=120,blank=False)
	img = models.FileField(blank=False)
	slug = models.SlugField(max_length=200,blank=False,default='slug_here')
	description = models.TextField(blank=False)


	def get_absolute_url(self):
		return reverse("shop:detail", args=[self.id,self.slug])
		
	def __str__(self):
		return self.method_name