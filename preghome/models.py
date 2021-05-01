import random, os
#import PIL 
#from PIL import _imaging
#import _imaging, Image
from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from pregweb.utils import unique_slug_generator

# Create your models here.
#now as well i want to upload my images to acertain path but which one

#since i dont want my images to appear as images in the url conf
#iwant to make them appear as files


#since iam handling all kinds of images i just want to make sure that all large images
#are resized to some kind of size that is favourable.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)#base name returns the last 
	name, ext = os.path.split(filepath)#os.path.split("/home/lutalo/joseph/joseph.txt")
	#("/home/lutalo/joseph", "joseph.txt")
	return name, ext
def upload_image_path(instance, filename):#
	print(instance)
	print(filename)
	new_filename = random.randint(1, 3910209312)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return  "shop/{new_filename}/{final_filename}".format(
		new_filename=new_filename, 
		final_filename=final_filename
	)


class ProductQuerySet(models.query.QuerySet):#this is for creating custom query sets, since 
#featured was returned as an error 
	def available(self):
		return self.filter(available=True)
	def featured(self):
		return self.filter(featured=True, available=True)
	def toprated(self):
		return self.filter(toprated=True)
	def search(self, query):
		lookups = (Q(name__icontains=query) | 
				  Q(description__icontains=query)   | 
				  Q(price__icontains=query) |
				  Q(tag__name__icontains=query)

				)
		#tags are used to handle forexample t shirt minus hyphen since it doesnot return prdct
		#Q(tag__name__icontains=query)
		#tshirt, t-shirt, t shirt
		return self.filter(lookups).distinct()##distinct is to avoid returning the same product twice.


class ProductManager(models.Manager):#this manager aids in generating id querysets.
	def get_queryset(self):#get_queryset() method should return aQuerset with the properties u
	#require	
#===since get_queryset() returns aQuerset object, u can use filter(), exclude() and all the
#other QuerySet methods on it
		return ProductQuerySet(self.model, using=self._db)#==what does self._db imply,..findout
	def all(self):
#====managers use the _db parameter to define on which database queryset the manager uses should 
#operate on, this is to optionally override it incase u have , multiple databases and u want yo
#manager to operate on aspecific one
		return self.get_queryset().available()
	def featured(self):
		return self.get_queryset().featured()
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)#takes over Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None

	def get_toprated(self):
		return self.get_queryset().toprated()
	def search(self, query):
		return  self.get_queryset().available().search(query)#
		##available is used to return available products

class Product(models.Model):#i want this to be my base model in the shop app
	category_name = models.CharField(max_length=120)
#essence is that when the category is deleted the product in category should as well be deleted	
	name = models.CharField(max_length=120)
	slug = models.SlugField(default="abc", unique=True, db_index=True)#since every product needs aslug generator
	description = models.TextField(blank=False)#every product will need adescription
	price = models.PositiveIntegerField(blank=False)
	image = models.FileField(upload_to=upload_image_path, blank=False)#field is amust required
	#do ineed the featured field
	featured = models.BooleanField(default=False)
	available= models.BooleanField(default=True)
	toprated = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)#since we need the time 
	updated_at = models.DateTimeField(auto_now=True)
	

	objects = ProductManager()

	class Meta:
		ordering = ["name"]
		index_together = (("id", "slug"))#to specify an index for id and slug, helps improve performance
	#of queries	

	def get_absolute_url(self):#this returns directly the detail of the project
		return reverse("preghome:detail", args=[self.id,self.slug])

	def __str__(self):
		return self.name

	def save_img(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)
		output_size = (125, 125)
		img.thumbnail(output_size)
		img.save(self.image.path)
		super(Product, self).save()


def product_pre_save_receiver(sender, instance,  *args, **kwargs):#this is supposed to generate
#urls automatically incase one object doesnot have
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)

#django.db.models.signals.pre_save is sent at the beginning of amodel's save() method
#sender=== the model class , instance === the actual instance being saved	


class BookNurse(models.Model):
	contact = models.CharField(max_length=120)
	location = models.CharField(max_length=120)
	no_days  = models.IntegerField()


	def __str__(self):
		return self.contact


