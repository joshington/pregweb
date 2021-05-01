from django.urls import path
from django.conf.urls import url
from .import views
 

app_name = "familyplan"

urlpatterns = [
	path('methods/', views.method_list,name='method_list'),
	path('<int:id>/<slug:slug>/', views.method_detail, name="detail"),
]