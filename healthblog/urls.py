from django.urls import path
from django.conf.urls import url
from .import views
 

app_name = "healthblog"

urlpatterns = [
	path('',views.list_blog, name='list-blog'),
	
]