from django.shortcuts import render

# Create your views here.
from .models import HealthBlog


def list_blog(request):
	query = HealthBlog.objects.all()
	return render(request, "healthblog/blog.html",{'qs':query})