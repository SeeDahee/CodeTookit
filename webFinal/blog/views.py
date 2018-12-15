from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from . models import sketches

class BlogListView(ListView):
	model = sketches
	template_name = 'blog_list.html'


	