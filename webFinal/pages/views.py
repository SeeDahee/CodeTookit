from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView

from blog.models import sketches

from django.views.generic import ListView



class HomePageView(TemplateView):
	template_name = 'home.html'

class compPageView(TemplateView):
	template_name = 'compForm.html'


class maskPageView(TemplateView):
	template_name = 'mask.html'


class blogPageView(TemplateView):
	template_name = 'blog_list.html'
	
