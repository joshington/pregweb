from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import FamilyMethod


def method_list(request):
	queryset = FamilyMethod.objects.all()
	return render(request, "familyplan/methods.html", {"qs":queryset})

def method_detail(request,id,slug):
	method = get_object_or_404(FamilyMethod, id=id, slug=slug)
	return render(request, 'familyplan/method_detail.html', {'object':method})