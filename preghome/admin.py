from django.contrib import admin

# Register your models here.
from .models import  Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__str__", "slug"]#under this we put what we want to appear on panel
	class Meta:
		model = Product
admin.site.register(Product, ProductAdmin)